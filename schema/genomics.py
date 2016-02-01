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


"""cubicweb-genomics schema"""


from yams.buildobjs import (EntityType,
                            RelationDefinition,
                            SubjectRelation,
                            String,
                            RichString,
                            BigInt,
                            Int,
                            Float,
                            Boolean)


### GENETICS ENTITIES #########################################################

class Chromosome(EntityType):
    """ Chromosome definition """
    name = String(required=True, unique=True, maxsize=16)
    identifier = String(required=True, indexed=True, maxsize=64)
    genes = SubjectRelation('Gene', cardinality='*+', inlined=False)


class Gene(EntityType):
    """ Gene definition """
    name = String(maxsize=256, fulltextindexed=True, indexed=True)
    gene_id = String(maxsize=256, required=True, indexed=True)
    uri = String(maxsize=256, indexed=True)
    start_position = Int(indexed=True)
    stop_position = Int(indexed=True)
    # Allow for translocated genes
    chromosomes = SubjectRelation('Chromosome', cardinality='+*', inlined=False)


class Snp(EntityType):
    """ SNP definition """
    rs_id = String(required=True, unique=True, maxsize=16)
    position = BigInt(required=True, indexed=True)
    chromosome = SubjectRelation('Chromosome', cardinality='1*', inlined=False)
    gene = SubjectRelation('Gene', cardinality='**', inlined=False)
    genomis_platforms = SubjectRelation("GenomicPlatform", cardinality="**", inlined=False)


class GenomicMeasure(EntityType):
    """ A genomic measure """
    type = String(maxsize=256, required=True, indexed=True)
    format = String(maxsize=128, indexed=True)
    chip_serialnum = Int()
    completed = Boolean(indexed=True)
    chromset = String(maxsize=64)
    valid = Boolean(indexed=True)
    platform = SubjectRelation('GenomicPlatform', cardinality='?*', inlined=False)
    subjects = SubjectRelation("Subject", cardinality="**", inlined=False)
    study = SubjectRelation("Study", cardinality="1*", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="**", inlined=False)
    identifier = String(maxsize=128, fulltextindexed=True)
    label = String(maxsize=64)

class GenomicPlatform(EntityType):
    name = String(required=True, maxsize=64)
    snps = SubjectRelation("Snp", cardinality="**", inlined=False)
    genomic_measure =  SubjectRelation("GenomicMeasure", cardinality="*1", inlined=False)

