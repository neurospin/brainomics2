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


class Chromosome(EntityType):
    """ Chromosome definition """
    name = String(required=True, unique=True, maxsize=16)
    identifier = String(required=True, indexed=True, maxsize=64)


class Gene(EntityType):
    """ Gene definition """
    hgnc_id = String(maxsize=256, fulltextindexed=True, indexed=True,
                     unique=True)
    gene_id = String(maxsize=256, required=True, indexed=True)
    uri = String(maxsize=256, indexed=True)
    start_position = BigInt(indexed=True)
    end_position = BigInt(indexed=True)
    type = String(required=True, indexed=True, unique=False, maxsize=22)


class Snp(EntityType):
    """ SNP definition """
    rs_id = String(required=True, unique=True, maxsize=24)
    start_position = BigInt(required=True)
    end_position = BigInt(required=True)
    maf = Float(required=True) # minor allele frequency


class CpG(EntityType):
    """ Epigenetic methylation loci """
    cg_id = String(required=True, unique=True, maxsize=24)
    position = BigInt(required=True)


class GenomicMeasure(EntityType):
    """ A genomic measure """
    type = String(maxsize=256, required=True, indexed=True)
    format = String(maxsize=128, indexed=True)
    chip_serialnum = Int()
    completed = Boolean(indexed=True)
    chromset = String(maxsize=64)
    valid = Boolean(indexed=True)
    identifier = String(maxsize=128, fulltextindexed=True)
    label = String(maxsize=64)


class GenomicPlatform(EntityType):
    name = String(required=True, maxsize=64)
