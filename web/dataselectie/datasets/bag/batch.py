import logging

from django.conf import settings

from . import models
from ..generic import index
from . import documents

log = logging.getLogger(__name__)

BAG_DOC_TYPES = (
    documents.Nummeraanduiding,
)


class IndexDsBagTask(index.ImportIndexTask):
    name = "index bag data"
    index = settings.ELASTIC_INDICES['DS_INDEX']

    queryset = models.Nummeraanduiding.objects.\
        prefetch_related('verblijfsobject').\
        prefetch_related('standplaats').\
        prefetch_related('ligplaats').\
        prefetch_related('openbare_ruimte')

    def convert(self, obj):
        return documents.doc_from_nummeraanduiding(obj)


class BuildIndexDsBagJob(object):
    name = "Create new search-index for all BAG data from database"

    @staticmethod
    def tasks():
        return [IndexDsBagTask()]
