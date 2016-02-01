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


from yams.buildobjs import SubjectRelation, RelationDefinition
from cubicweb.schema import ERQLExpression, RRQLExpression


# Cubes import
from cubes.brainomics2.schema.medicalexp import Assessment
from cubes.brainomics2.schema.medicalexp import Subject
from cubes.brainomics2.schema.medicalexp import FileSet
from cubes.brainomics2.schema.medicalexp import ExternalFile
from cubes.brainomics2.schema.medicalexp import ScoreValue
from cubes.brainomics2.schema.medicalexp import ProcessingRun
from cubes.brainomics2.schema.medicalexp import Center
from cubes.brainomics2.schema.medicalexp import Study
from cubes.brainomics2.schema.neuroimaging import Scan
from cubes.brainomics2.schema.neuroimaging import DMRIData, EEGData, ETData
from cubes.brainomics2.schema.neuroimaging import MRIData
from cubes.brainomics2.schema.neuroimaging import FMRIData
from cubes.brainomics2.schema.questionnaire import QuestionnaireRun
from cubes.brainomics2.schema.questionnaire import Questionnaire
from cubes.brainomics2.schema.questionnaire import OpenAnswer
from cubes.brainomics2.schema.questionnaire import Question
from cubes.brainomics2.schema.genomics import GenomicMeasure
###############################################################################
# Set permissions
###############################################################################

# CWGROUP


class can_read(RelationDefinition):
    subject = "CWGroup"
    object = "Assessment"
    cardinality = "*?"


class can_update(RelationDefinition):
    subject = "CWGroup"
    object = "Assessment"
    cardinality = "*?"

# RIGHTS


class in_assessment(RelationDefinition):
    subject = ("ProcessingRun", "ExternalFile", "Scan", "FileSet", "FMRIData", 
               "DMRIData", "EEGData", "ETData", "MRIData", "ScoreValue", 
               "QuestionnaireRun")
    object = "Assessment"
    cardinality = "1*"
    inlined = True


###############################################################################
# Set permissions
###############################################################################

ENTITIES = [
    Scan, FMRIData, DMRIData, EEGData, ETData, MRIData, FileSet, ExternalFile,
    ScoreValue, ProcessingRun, QuestionnaireRun, OpenAnswer, GenomicMeasure]


DEFAULT_PERMISSIONS = {
    "read": ("managers", "users", "guests"),
    "add": ("managers",),
    "update": ("managers",),
    "delete": ("managers",),
}


ASSESSMENT_PERMISSIONS = {
    "read": (
        "managers",
        ERQLExpression("U in_group G, G can_read X")),
    "add": (
        "managers",
        ERQLExpression("U in_group G, G can_update X")),
    "update": (
        "managers",
        ERQLExpression("U in_group G, G can_update X")),
    "delete": (
        "managers",
        ERQLExpression("U in_group G, G can_update X")),
}


RELATION_PERMISSIONS = {
    "read": (
        "managers",
        "users"),
    "add": (
        "managers",
        RRQLExpression("S in_assessment A, U in_group G, G can_update A")),
    "delete": (
        "managers",
        RRQLExpression("S in_assessment A, U in_group G, G can_update A"))
}


ENTITY_PERMISSIONS = {
    "read": (
        "managers",
        ERQLExpression("X in_assessment A, U in_group G, G can_read A")),
    "add": (
        "managers",
        ERQLExpression("X in_assessment A, U in_group G, G can_update A")),
    "update": (
        "managers",
        ERQLExpression("X in_assessment A, U in_group G, G can_update A")),
    "delete": (
        "managers",
        ERQLExpression("X in_assessment A, U in_group G, G can_update A")),
}


# Set the assessment entity permissions
Assessment.set_permissions(ASSESSMENT_PERMISSIONS)

# Set the subject/center/study/questionnaire/question entities permissions
Subject.set_permissions(DEFAULT_PERMISSIONS)
Center.set_permissions(DEFAULT_PERMISSIONS)
Study.set_permissions(DEFAULT_PERMISSIONS)
Questionnaire.set_permissions(DEFAULT_PERMISSIONS)
Question.set_permissions(DEFAULT_PERMISSIONS)

# Set the permissions on the used entities only
for entity in ENTITIES:
    entity.__permissions__ = ENTITY_PERMISSIONS

# Update the entities list to set relation permissions
ENTITIES.extend([Assessment, Subject, Center, Study, Questionnaire, Question])

# Set the permissions on the ised entities relations only
for entity in ENTITIES:

    # Get the subject relations
    for relation in entity.__relations__:
        if relation.__class__ is SubjectRelation:
            relation.__permissions__ = RELATION_PERMISSIONS
