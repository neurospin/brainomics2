##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# System import
from packaging import version

# Cubicweb import
import cubicweb
cw_version = version.parse(cubicweb.__version__)
if cw_version >= version.parse("3.21.0"):
    from cubicweb import _

from yams.buildobjs import EntityType
from yams.buildobjs import String
from yams.buildobjs import RichString
from yams.buildobjs import Bytes


class RestrictedFile(EntityType):
    """ A downloadable file which may contains binary data
    """
    title = String(required=True, indexed=True, maxsize=256)
    data = Bytes(
        required=True, fulltextindexed=True, description=_('file to upload'))
    data_format = String(
        required=True, maxsize=128,
        description=_('MIME type of the file. Should be dynamically set at '
                      'upload time.'))
    data_encoding = String(
        maxsize=32,
        description=_('encoding of the file when it applies (e.g. text). '
                      'Should be dynamically set at upload time.'))
    data_name = String(
        required=True, fulltextindexed=True,
        description=_('name of the file. Should be dynamically set at upload '
                      'time.'))
    data_sha1hex = String(
        maxsize=40,
        description=_('SHA1 sum of the file. May be set at upload time.'))
    description = RichString(
        fulltextindexed=True, internationalizable=True,
        default_format='text/rest')
