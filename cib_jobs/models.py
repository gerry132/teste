from django.db import models
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images import get_image_model_string

from cib_content_page.models import ContentPage
from django.utils.functional import cached_property
from django.utils.translation import get_language

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from taggit.models import TagBase, ItemBase

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from django import forms
from wagtail import blocks

from cib_utils.blocks import SelectComponentBlock
from cib_utils.models import BasePage

IMAGE_MODEL = get_image_model_string()


class JobVacanciesTag(TagBase):
    free_tagging = False
    locale = models.CharField(max_length=10, default='en', null=True, blank=True)
    description = models.CharField(
        verbose_name=pgettext_lazy("A tag description", "description"),
        max_length=255, default='', unique=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "job company tag"
        verbose_name_plural = "job company tags"


class TaggedJobVacancies(ItemBase):
    tag = models.ForeignKey(
        JobVacanciesTag, related_name="tagged_jobvacancies", on_delete=models.CASCADE,
        help_text="news tags"
    )
    content_object = ParentalKey(
        to='JobVacancyContentPage',
        on_delete=models.CASCADE,
        related_name='tagged_jobvacancies_items'
    )


class JobVacancyContentPage(ContentPage):
    template = "patterns/pages/job_vacancy_content_page.html"
    parent_page_types = ["JobVacanciesPage"]

    organisation_logo = models.ForeignKey(
        IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    organisation_logo_alt = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Image Alt text"),
        help_text=_("The alt text shown for accessibility: https://axesslab.com/alt-texts/")
    )
    show_on_page = models.BooleanField(blank=False, null=True)
    job_title = models.TextField(blank=True)
    organisation = models.TextField(blank=True)
    address = RichTextField(blank=True, null=True)
    job_index_lead_summary = models.TextField(
        max_length=300,
        help_text="A brief 1-2 sentence job summary. This will appear on the job vacancy index page, not on the "
                  "job posting itself.",
        null=True
    )
    job_description = RichTextField(blank=True, null=True)
    job_forms = StreamField([
        ('heading_with_document', blocks.StructBlock([
            ('heading', blocks.CharBlock(required=True, help_text="Enter your heading text")),
            ('document', DocumentChooserBlock(required=True)),
        ])),
    ], use_json_field=True,
        null=True,
        blank=True)
    contact_email = RichTextField(blank=True, null=True)
    closing_date_title = models.CharField(
        max_length=255,
        blank=True,
    )

    job_vacancy_tags = ParentalManyToManyField("JobVacanciesTag", blank=True)

    content_panels = BasePage.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('go_live_at'),
                FieldPanel('closing_date_title'),
                FieldPanel('expire_at', heading="Closing date/time"),
            ],
            heading="Scheduled publishing", help_text="The expiry date you select will unpublish the job vacancy on "
                                                      "the selected date. It will also automatically output the "
                                                      "selected date as the 'Closing date:' on the published job "
                                                      "vacancy. "
        ),
        MultiFieldPanel(
            [
                FieldPanel('organisation_logo'),
                FieldPanel('organisation_logo_alt'),
                FieldPanel("show_on_page", widget=forms.CheckboxInput),
                FieldPanel('job_title'),
                FieldPanel('organisation'),
                FieldPanel('address'),
                FieldPanel('job_index_lead_summary'),
                FieldPanel('job_description'),
                FieldPanel('job_forms'),
                FieldPanel('contact_email'),
            ],
            heading="Job Details",
        ),
        FieldPanel("body"),
        FieldPanel("jobvacancy_latest_news_snippet"),
        FieldPanel("news_letter_signup_cta"),
        MultiFieldPanel(
            [
                FieldPanel("job_vacancy_tags", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Tags"
        ),

    ]
    settings_panels = ([
        FieldPanel('last_published_custom'),
    ]
    )

    @property
    def current_tags(self):
        return JobVacanciesTag.objects.filter(
            jobvacancycontentpage__id=self.id)


class JobVacanciesPage(BasePage):
    template = "patterns/pages/job_vacancy_page.html"
    subpage_types = [
        'JobVacancyContentPage',
    ]
    description = models.TextField(blank=True)
    company_select_component = StreamField([
        ('publication_select_component', SelectComponentBlock()),
    ], blank=False, null=True, max_num=1)
    jobvacancy_latestnews_snippet = models.ForeignKey(
        'utils.JobsVacanciesAndLatestNewsSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    news_letter_signup_cta = models.ForeignKey(
        'utils.NewsletterSignUpCTASnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @cached_property
    def related_jobs(self):
        return (
            JobVacancyContentPage.objects
            .child_of(self)
            .filter(locale=self.locale)
            .public()
            .live()
            .order_by("-first_published_at")
            .specific()
        )

    content_panels = BasePage.content_panels + [
        FieldPanel("description"),
        FieldPanel("company_select_component"),
        FieldPanel("jobvacancy_latestnews_snippet"),
        FieldPanel("news_letter_signup_cta"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        current_language = get_language()

        all_company_type_tags = JobVacanciesTag.objects.filter(locale=current_language)
        context['all_company_type_tags'] = all_company_type_tags

        selected_company_type = request.GET.get('company_type')

        jobs = []

        for job in self.related_jobs:
            job_company_type_tags = job.current_tags.values_list('slug', flat=True)

            if not selected_company_type or selected_company_type in job_company_type_tags:
                jobs.append(job)

        context['jobs'] = jobs
        context['selected_company_type'] = selected_company_type

        return context
