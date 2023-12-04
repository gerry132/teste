from wagtail.admin.views.reports.audit_logging import LogEntriesView

from django.utils.translation import gettext_lazy as _


class PublicationLogReportsView(LogEntriesView):
    """Site History with publication log"""
    header_icon = 'doc-empty-inverse'
    title = "Site history with publication log"

    LogEntriesView.export_headings['data'] = _("action details")
    list_export = LogEntriesView.list_export + ['data']