# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from troisponts.urban.dataimport.interfaces import ITroispontsDataImporter


class TroispontsDataImporter(AgorawinDataImporter):
    """ """

    implements(ITroispontsDataImporter)
