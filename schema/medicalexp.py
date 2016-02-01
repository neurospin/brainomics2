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

"""cubicweb-medicalexp schema"""


from yams.buildobjs import (EntityType,
                            RelationDefinition,
                            SubjectRelation,
                            String,
                            RichString,
                            Int,
                            Float,
                            Date,
                            Boolean)

from yams.constraints import BoundaryConstraint, Attribute

_ = unicode


### PROJECT/SUBJECT SPECIFIC ENTITIES #########################################

class Subject(EntityType):
    """ The subject """
    code_in_study = String(required=True, unique=True, fulltextindexed=True,
                        indexed=True, maxsize=64)
    surname = String(fulltextindexed=True, maxsize=256)
    gender = String(required=True, indexed=True,
                    vocabulary=('male', 'female', 'unknown'))
    handedness = String(required=True, indexed=True,
                        vocabulary=('right', 'left', 'ambidextrous', 'mixed', 'unknown'))
    study = SubjectRelation('Study', cardinality='1*')
    subject_groups = SubjectRelation('SubjectGroup', cardinality='**')
    diagnostics = SubjectRelation('Diagnostic', cardinality='**', composite='subject')
    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="**", inlined=False)
    assessments = SubjectRelation("Assessment", cardinality="**", inlined=False)
    scans = SubjectRelation("Scan", cardinality="*1", inlined=False)
    questionnaire_runs = SubjectRelation("QuestionnaireRun", cardinality="*1", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="*1", inlined=False)
    center = SubjectRelation("Center", cardinality="?*", inlined=False)
    position_in_family = String(maxsize=64)
    subjectgroups = SubjectRelation('SubjectGroup', cardinality='**')


class Study(EntityType):
    """ The project """
    name = String(required=True, indexed=True, maxsize=256)
    description = RichString(fulltextindexed=True)
    assessments = SubjectRelation("Assessment", cardinality="*1", inlined=False)
    subjects = SubjectRelation("Subject", cardinality="*1", inlined=False)
    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="*1", inlined=False)
    scans = SubjectRelation("Scan", cardinality="*1", inlined=False)
    questionnaire_runs = SubjectRelation("QuestionnaireRun", cardinality="*1", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="*1", inlined=False)
    subjectgroups = SubjectRelation('SubjectGroup', cardinality='*1')
    protocols = SubjectRelation('Protocol', cardinality='*1')


class SubjectGroup(EntityType):
    """ Group of subject """
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    name = String(maxsize=64, required=True, indexed=False)
    study = SubjectRelation('Study', cardinality='1*')
    subjects = SubjectRelation('Subject', cardinality='**', inlined=False)
    type = String(maxsize=64, required=True, vocabulary=[u'family', u'schedule'])


class Investigator(EntityType):
    """ Investigator of a study / PI """
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    firstname = String(maxsize=256)
    lastname = String(maxsize=256)
    title = String(maxsize=16)
    institution = String(maxsize=256)
    department = String(maxsize=256)


class Center(EntityType):
    """ A center used for study """
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    name = String(maxsize=256, required=True)
    department = String(maxsize=256)
    city = String(maxsize=64)
    country = String(maxsize=64)
    assessments = SubjectRelation("Assessment", cardinality="*1", inlined=False)
    subjects = SubjectRelation("Subject", cardinality="*?", inlined=False)


class Device(EntityType):
    """ Device used in experiments/assessments """
    name = String(maxsize=256, required=True)
    manufacturer = String(maxsize=256)
    model = String(maxsize=256)
    serialnum = String(maxsize=256)
    software_version = String(maxsize=128)
    configurations = RichString(fulltextindexed=True)
    center = SubjectRelation('Center', cardinality='1*', inlined=False)


class Protocol(EntityType):
    """ A protocol for a study or a measure """
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    name = String(maxsize=256, required=True, unique=True)
    study = SubjectRelation('Study', cardinality='1*', inlined=False)
    # subjects = SubjectRelation('Subject', cardinality="**", inlined=False)
    assessments = SubjectRelation('Assessment', cardinality="*?", inlined=False)


class Diagnostic(EntityType):
    """ Diagnostic attributes and links.
    Diagnostic may be based on specific measures, and holds a conclusion
    on BodyLocation/Disease"""
    age_at_diagnosis = Int()
    conclusion = String(maxsize=256, fulltextindexed=True)
    subject = SubjectRelation('Subject', cardinality="?*", inlined=False)


class Assessment(EntityType):
    """ Store information about a visit """
    age_of_subject = Int(indexed=True)
    timepoint = String(maxsize=64)
    study = SubjectRelation('Study', cardinality='1*', inlined=False)
    center = SubjectRelation('Center', cardinality='1*', inlined=False)
    subject = SubjectRelation('Subject', cardinality='1*', inlined=False)
    scans = SubjectRelation('Scan', cardinality='*1', inlined=False)
    questionnaire_runs = SubjectRelation("QuestionnaireRun", cardinality="*1", inlined=False)
    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="*1", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="**", inlined=False)
    protocol = SubjectRelation('Protocol', cardinality="?*", inlined=False)
    # Add identifier to Assessment entity
    identifier = String(maxsize=128, fulltextindexed=True, unique=True)


class ProcessingRun(EntityType):
    name = String(maxsize=256)
    tool = String(maxsize=256)
    datetime = Date()
    category = String(maxsize=256)
    version = String(maxsize=64)
    parameters = String(maxsize=256)
    note = RichString(fulltextindexed=True)
    results_filesets = SubjectRelation('FileSet', cardinality='**', inlined=False)
    config_file_sets = SubjectRelation('FileSet', cardinality='**', inlined=False)
    score_values = SubjectRelation("ScoreValue", cardinality="*?", inlined=False)
    identifier = String(maxsize=128, fulltextindexed=True)
    label = String(maxsize=64)
    inputs = SubjectRelation(('GenomicMeasure', 'Scan'), cardinality='**')
    study = SubjectRelation('Study', cardinality='1*', inlined=False)
    subjects = SubjectRelation("Subject", cardinality="**", inlined=False)


###############################################################################
### SATELLITE ENTITIES ########################################################
###############################################################################
class FileSet(EntityType):
    """ A composite resource file set """
    name = String(maxsize=256, required=True)
    identifier = String(maxsize=128, unique=True, fulltextindexed=True)
    external_files = SubjectRelation('ExternalFile', cardinality='**')


class ExternalFile(EntityType):
    """ An external resource file (e.g. an absolute/relative filepath)
    """
    name = String(maxsize=256)
    # If not absolute_path, use the data_filepath of the study
    absolute_path = Boolean(default=True)
    filepath = String(required=True, indexed=True, maxsize=256)
    identifier = String(maxsize=128, unique=True, fulltextindexed=True)
    fileset = SubjectRelation('FileSet', cardinality='**')


class ScoreDefinition(EntityType):
    """ A score definition """
    name = String(maxsize=256, required=True,  fulltextindexed=True)
    category = String(maxsize=64, fulltextindexed=True)
    type = String(required=True, indexed=True, vocabulary=('string', 'numerical', 'logical'),)
    unit = String(maxsize=16, indexed=True)
    possible_values = String(maxsize=256, fulltextindexed=True)
    score_values = SubjectRelation('ScoreValue', cardinality='*1', inlined=False)

# XXX Two different etypes for string/numerical values ?
class ScoreValue(EntityType):
    """ A score value """
    score_definition = SubjectRelation('ScoreDefinition', cardinality='1*')
    text = String(maxsize=2048, fulltextindexed=True)
    value = Float(indexed=True)
    datetime = Date()
    # scoregroups = SubjectRelation('ScoreGroup', cardinality='**')

# class ScoreGroup(EntityType):
#     """ A group of score values that should be considered together """
#     identifier = String(required=True, unique=True, indexed=True, maxsize=64)
#     scores = SubjectRelation('ScoreValue', cardinality='**')

