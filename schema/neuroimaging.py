##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

from yams.buildobjs import EntityType
from yams.buildobjs import String
from yams.buildobjs import RichString
from yams.buildobjs import Int
from yams.buildobjs import Float
from yams.buildobjs import Date
from yams.buildobjs import Boolean
from yams.buildobjs import BigInt
from yams.buildobjs import Bytes


SCAN_DATA = ('MRIData', 'DMRIData', 'FMRIData', 'EEGData', 'ETData', 'PETData')


class Scan(EntityType):
    label = String(maxsize=256, required=True, indexed=True, fulltextindexed=True)
    identifier = String(required=True, maxsize=128, unique=True)
    type = String(maxsize=256, required=True, indexed=True)
    format = String(maxsize=128, indexed=True)


class MRIData(EntityType):
    sequence = String(maxsize=128, indexed=True)
    shape_x = Int(indexed=False)
    shape_y = Int(indexed=False)
    shape_z = Int(indexed=False)
    shape_t = Int(indexed=False)
    voxel_res_x = Float(indexed=False)
    voxel_res_y = Float(indexed=False)
    voxel_res_z = Float(indexed=False)
    fov_x = Float(indexed=False)
    fov_y = Float(indexed=False)
    tr = Float()
    te = Float(indexed=False)
    field = String(maxsize=10, indexed=False)
    affine = Bytes()


class DMRIData(EntityType):
    voxel_res_x = Float(required=True, indexed=False)
    voxel_res_y = Float(required=True, indexed=False)
    voxel_res_z = Float(required=True, indexed=False)
    fov_x = Float(indexed=False)
    fov_y = Float(indexed=False)
    tr = Float()
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
    tr = Float()
    te = Float()
    field = String(maxsize=10, indexed=True)


class EEGData(EntityType):
    duration = String()
    sampling_rate = String()
    temperature = String()
    number_of_channels = String(maxsize=8)


class ETData(EntityType):
    duration = String()


class PETData(EntityType):
    voxel_res_x = Float(required=True, indexed=True)
    voxel_res_y = Float(required=True, indexed=True)
    voxel_res_z = Float(required=True, indexed=True)
    tr = Float()
    te = Float(required=True, indexed=True)
    scene_description = String()
