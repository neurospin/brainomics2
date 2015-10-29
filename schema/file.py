# -*- coding: utf-8 -*-
##########################################################################
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################
# copyright 2013 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# copyright 2013 CEA (Saclay, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

from yams.buildobjs import EntityType, String, Bytes, RichString

_ = unicode

class File(EntityType):
    """a downloadable file which may contains binary data"""
    title = String(fulltextindexed=True, maxsize=256)
    data = Bytes(required=True, fulltextindexed=True,
                 description=_('file to upload'))
    data_format = String(required=True, maxsize=128,
                         description=_('MIME type of the file. Should be dynamically set at upload time.'))
    data_encoding = String(maxsize=32,
                           description=_('encoding of the file when it applies (e.g. text). '
                                         'Should be dynamically set at upload time.'))
    data_name = String(required=True, fulltextindexed=True,
                       description=_('name of the file. Should be dynamically set at upload time.'))
    data_sha1hex = String(maxsize=40,
                          description=_('SHA1 sum of the file. May be set at upload time.'),
                          __permissions__={'read': ('managers', 'users', 'guests'),
                                           'add': (),
                                           'update': (),
                                           })
    description = RichString(fulltextindexed=True, internationalizable=True,
                             default_format='text/rest')
    fileset = SubjectRelation('FileSet', cardinality='**')
