##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################


# CubicWeb import
from yams.buildobjs import SubjectRelation
from yams.buildobjs import RelationDefinition
from cubicweb.schema import ERQLExpression
from cubicweb.schema import RRQLExpression
from yams.buildobjs import RelationDefinition
from yams.buildobjs import RelationType

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
from cubes.brainomics2.schema.neuroimaging import DMRIData
from cubes.brainomics2.schema.neuroimaging import EEGData
from cubes.brainomics2.schema.neuroimaging import ETData
from cubes.brainomics2.schema.neuroimaging import PETData
from cubes.brainomics2.schema.neuroimaging import MRIData
from cubes.brainomics2.schema.neuroimaging import FMRIData
from cubes.brainomics2.schema.questionnaire import QuestionnaireRun
from cubes.brainomics2.schema.questionnaire import OpenAnswer
from cubes.brainomics2.schema.questionnaire import Questionnaire
from cubes.brainomics2.schema.questionnaire import Question
from cubes.brainomics2.schema.genomics import GenomicMeasure
from cubes.brainomics2.config import ASSESSMENT_CONTAINER
from cubes.brainomics2.schema.card import Card


###############################################################################
# Define permission relations
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


###############################################################################
# Set permissions
###############################################################################

RESTRICTED_ENTITIES = [
    Scan, FMRIData, DMRIData, PETData, MRIData, EEGData, ETData, FileSet,
    ExternalFile, ScoreValue, ProcessingRun, QuestionnaireRun, OpenAnswer,
    GenomicMeasure]

PUBLIC_ENTITIES = [
    Subject, Center, Study, Questionnaire, Question, Card]

ENTITIES = RESTRICTED_ENTITIES + PUBLIC_ENTITIES + [Assessment]


PUBLIC_PERMISSIONS = {
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

RESTRICTED_PERMISSIONS = {
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

MANAGER_PERMISSIONS = {
    "read": ("managers",),
    "add": ("managers",),
    "update": ("managers",),
    "delete": ("managers",),
}

UNTRACK_ENTITIES = ["CWUser", "CWGroup", "CWSource", "Study", "Center",
                    "Device", "Question", "Questionnaire", "Subject",
                    "GenomicPlatform", "Snp"]
UNTRACK_ENTITIES += ["Assessment"]


def post_build_callback(schema):

    # Get the schema
    entities = schema.entities()
    names = [entity.type for entity in entities]

    # Link each entity to an assessment through an 'in_assessment' relation
    schema.add_relation_type(RelationType("in_assessment", inlined=False))
    for entity in entities:
        if entity.type not in UNTRACK_ENTITIES and not entity.final:
            schema.add_relation_def(
                RelationDefinition(subject=entity.type,
                                   name="in_assessment",
                                   object="Assessment",
                                   cardinality='1*'))

    # Add a container to the assessment entity
    ASSESSMENT_CONTAINER.define_container(schema)

    # Set strict default permissions
    entity_names = [e.__name__ for e in ENTITIES]
    for entity in entities:
        if entity.type not in entity_names:
            entity.permissions = MANAGER_PERMISSIONS

    # Set the relation permissions
    for entity in ENTITIES:
        for relation in entity.__relations__:
            if relation.__class__ is SubjectRelation:
                relation.__permissions__ = RELATION_PERMISSIONS

    # Set the specific entity permissions
    entities[names.index("Assessment")].permissions = ASSESSMENT_PERMISSIONS
    for entity in PUBLIC_ENTITIES:
        entities[names.index(entity.__name__)].permissions = PUBLIC_PERMISSIONS
    for entity in RESTRICTED_ENTITIES:
        entities[names.index(entity.__name__)].permissions = RESTRICTED_PERMISSIONS

