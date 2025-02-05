from django_opensearch_dsl import Document
from django_opensearch_dsl.registries import registry
from .models import SearchTerm


@registry.register_document
class SearchTermDocument(Document):
    class Index:
        name = 'search_terms'  # Name of the Opensearch index
        settings = {  # See Opensearch Indices API reference
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        # Configure how the index should be refreshed after an update.
        # See Opensearch documentation for supported options.
        # This per-Document setting overrides settings.
        auto_refresh = False

    class Django:
        model = SearchTerm  # The model associated with this Document
        fields = [  # The fields of the model you want to be indexed
            'search_term',
            'count'
        ]
        queryset_pagination = 5000
