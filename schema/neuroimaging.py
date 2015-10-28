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

"""cubicweb-neuroimage schema"""


from yams.buildobjs import (EntityType,
                            SubjectRelation,
                            String,
                            RichString,
                            Int,
                            Float,
                            Boolean,
                            Bytes)

### IMAGE AND SCAN ############################################################


SCAN_DATA = ('MRIData', 'DMRIData', 'FMRIData')

class Scan(EntityType):
    label = String(maxsize=256, required=True, indexed=True, fulltextindexed=True)
    identifier = String(maxsize=128)
    type = String(maxsize=256, required=True, indexed=True)
    format = String(maxsize=128, indexed=True)
    has_data = SubjectRelation(SCAN_DATA, cardinality='?1', inlined=True)
    study = SubjectRelation("Study", cardinality="1*", inlined=True)
    subject = SubjectRelation("Subject", cardinality="1*", inlined=False)
    score_values = SubjectRelation("ScoreValue", cardinality="*1", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="**", inlined=False)
    description = RichString(fulltextindexed=True)


class MRIData(EntityType):
    sequence = String(maxsize=128, indexed=True)
    # Image technical information
    shape_x = Int(indexed=False)
    shape_y = Int(indexed=False)
    shape_z = Int(indexed=False)
    shape_t = Int(indexed=False)
    voxel_res_x = Float(indexed=False)
    voxel_res_y = Float(indexed=False)
    voxel_res_z = Float(indexed=False)
    # MRI specific. Should be put elsewhere ?
    fov_x = Float(indexed=False)
    fov_y = Float(indexed=False)
    tr = Float(indexed=False)
    te = Float(indexed=False)
    field = String(maxsize=10, indexed=False)
    affine = Bytes()


class DMRIData(EntityType):
    # Image technical information
    voxel_res_x = Float(required=True, indexed=False)
    voxel_res_y = Float(required=True, indexed=False)
    voxel_res_z = Float(required=True, indexed=False)
    # MRI specific. Should be put elsewhere ?
    fov_x = Float(indexed=False)
    fov_y = Float(indexed=False)
    tr = Float(required=True, indexed=False)
    te = Float(required=True, indexed=False)
    shape_x = Int(indexed=False)
    shape_y = Int(indexed=False)
    shape_z = Int(indexed=False)
    field = String(maxsize=10, indexed=False)

class FMRIData(EntityType):
    shape_x = Float()
    shape_y = Float()
    shape_z = Float()
    voxel_res_x = Float(required=True)
    voxel_res_y = Float(required=True)
    voxel_res_z = Float(required=True)
    fov_x = Float()
    fov_y = Float()
    tr = Float()  # add required=True in next major revision
    te = Float()
    field = String(maxsize=10, indexed=True)

