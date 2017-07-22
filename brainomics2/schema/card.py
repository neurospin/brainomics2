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


class Card(EntityType):
    """ A card is a textual content used as documentation, reference, procedure
    reminder
    """
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers', 'users'),
        'delete': ('managers', 'owners'),
        'update': ('managers', 'owners',),
        }

    title = String(required=True, fulltextindexed=True, maxsize=256)
    synopsis = String(fulltextindexed=True, maxsize=512,
                      description=_("an abstract for this card"))
    content = RichString(fulltextindexed=True, internationalizable=True,
                         default_format='text/rest')
    wikiid = String(maxsize=64, unique=True)
