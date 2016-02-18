##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

from yams.buildobjs import EntityType
from yams.buildobjs import RelationType
from yams.buildobjs import RelationDefinition
from yams.buildobjs import String
from yams.buildobjs import RichString
from yams.buildobjs import Int
from yams.buildobjs import Float
from yams.buildobjs import Date
from yams.buildobjs import Boolean

from yams.buildobjs import SubjectRelation

_ = unicode


###############################################################################
# Shared entities
###############################################################################

class Subject(EntityType):
    """ The subject """
    code_in_study = String(
        required=True, unique=True, fulltextindexed=True, indexed=True,
        maxsize=64)
    identifier = String(required=True, maxsize=128, unique=True)
    surname = String(fulltextindexed=True, maxsize=256)
    gender = String(
        required=True, indexed=True, vocabulary=('male', 'female', 'unknown'))
    handedness = String(
        required=True, indexed=True,
        vocabulary=('right', 'left', 'ambidextrous', 'mixed', 'unknown'))
    position_in_family = String(maxsize=64)

    subject_groups = SubjectRelation('SubjectGroup', cardinality='**')
    diagnostics = SubjectRelation('Diagnostic', cardinality='**', composite='subject')
    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="**", inlined=False)
    scans = SubjectRelation("Scan", cardinality="*1", inlined=False)
    center = SubjectRelation("Center", cardinality="?*", inlined=False)
    subjectgroups = SubjectRelation('SubjectGroup', cardinality='**')


class Study(EntityType):
    """ The project """
    name = String(required=True, indexed=True, maxsize=256)
    description = RichString(fulltextindexed=True)

    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="*1", inlined=False)
    scans = SubjectRelation("Scan", cardinality="*1", inlined=False)
    subjectgroups = SubjectRelation('SubjectGroup', cardinality='*1')
    protocols = SubjectRelation('Protocol', cardinality='*1')


class SubjectGroup(EntityType):
    """ Group of subject """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=64, required=True, indexed=False)

    type = String(maxsize=64, required=True, vocabulary=[u'family', u'schedule'])


class Investigator(EntityType):
    """ Investigator of a study / PI """
    identifier = String(required=True, unique=True, maxsize=64)
    firstname = String(maxsize=256)
    lastname = String(maxsize=256)
    title = String(maxsize=16)
    institution = String(maxsize=256)
    department = String(maxsize=256)


class Center(EntityType):
    """ A center used for study """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=256, required=True, indexed=True)
    department = String(maxsize=256)
    city = String(maxsize=64)
    country = String(maxsize=64)


class Device(EntityType):
    """ Device used in experiments/assessments """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=256, required=True)
    manufacturer = String(maxsize=256)
    model = String(maxsize=256)
    serialnum = String(maxsize=256)
    software_version = String(maxsize=128)
    configurations = RichString(fulltextindexed=True)
    center = SubjectRelation('Center', cardinality='1*', inlined=False)


class Protocol(EntityType):
    """ A protocol for a study or a measure """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=256, required=True, unique=True)


class Diagnostic(EntityType):
    """ Diagnostic attributes and links.
    Diagnostic may be based on specific measures, and holds a conclusion
    on BodyLocation/Disease """
    age_at_diagnosis = Int()

    conclusion = String(maxsize=256, fulltextindexed=True)
    subject = SubjectRelation('Subject', cardinality="?*", inlined=False)


class Assessment(EntityType):
    """ Store information about a visit """
    identifier = String(required=True, maxsize=128, unique=True)
    age_of_subject = Int(indexed=True)
    timepoint = String(maxsize=64, indexed=True)

    center = SubjectRelation('Center', cardinality='1*', inlined=False)
    scans = SubjectRelation('Scan', cardinality='*1', inlined=False)
    genomic_measures = SubjectRelation("GenomicMeasure", cardinality="*1", inlined=False)
    processing_runs = SubjectRelation("ProcessingRun", cardinality="**", inlined=False)
    protocol = SubjectRelation('Protocol', cardinality="?*", inlined=False)


class ProcessingRun(EntityType):
    identifier = String(required=True, maxsize=128, unique=True)
    label = String(maxsize=256)
    tool = String(maxsize=256)
    datetime = Date()
    category = String(maxsize=256)
    version = String(maxsize=64)
    parameters = String(maxsize=256)
    note = RichString(fulltextindexed=True)

    results_filesets = SubjectRelation('FileSet', cardinality='**', inlined=False)
    config_file_sets = SubjectRelation('FileSet', cardinality='**', inlined=False)
    score_values = SubjectRelation("ScoreValue", cardinality="*?", inlined=False)
    label = String(maxsize=64)
    inputs = SubjectRelation(('GenomicMeasure', 'Scan'), cardinality='**')


class FileSet(EntityType):
    identifier = String(required=True,  maxsize=128, unique=True)
    name = String(maxsize=256, required=True)


class ExternalFile(EntityType):
    """ An external resource file (e.g. an absolute/relative filepath).

    If not absolute_path, use the data_filepath of the study
    """
    identifier = String(required=True, maxsize=128, unique=True)
    name = String(maxsize=256)
    absolute_path = Boolean(default=True)
    filepath = String(required=True, indexed=True, maxsize=256)


class ScoreDefinition(EntityType):
    name = String(maxsize=256, required=True,  fulltextindexed=True)
    category = String(maxsize=64, fulltextindexed=True)
    type = String(required=True, indexed=True,
                  vocabulary=('string', 'numerical', 'logical'),)
    unit = String(maxsize=16, indexed=True)
    possible_values = String(maxsize=256, fulltextindexed=True)


class ScoreValue(EntityType):
    text = String(maxsize=2048, fulltextindexed=True)
    value = Float(indexed=True)
    datetime = Date()



###############################################################################
# Shared relations
###############################################################################

class questionnaire_runs(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = ("Assessment", "Study", "Subject")
    object = "QuestionnaireRun"
    cardinality = "*1"
    composite = "subject"
    inlined=False


class external_files(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = "FileSet"
    object = "ExternalFile"
    cardinality = "**"
    composite = "subject"
    inlined=False


class subjects(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = ("Study", "SubjectGroup", "Center", "Assessment")
    object = "Subject"
    cardinality = "**"
    composite = "subject"
    inlined=False


class study(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = ("Subject", "SubjectGroup", "Protocol", "Assessment",
               "ProcessingRun", "Scan", "QuestionnaireRun", "GenomicMeasure")
    object = "Study"
    cardinality = "1*"
    composite = "subject"
    inlined=False


class score_definition(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = "ScoreValue"
    object = "ScoreDefinition"
    cardinality = "1*"
    composite = "object"
    inlined=False


class score_values(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = "ScoreDefinition"
    object = "ScoreValue"
    cardinality = "*1"
    composite = "subject"
    inlined=False


class fileset(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = "ExternalFile"
    object = "FileSet"
    cardinality = "++"
    composite = "object"
    inlined=False


class assessments(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    subject = ("Subject", "Study", "Center", "Protocol")
    object = "Assessment"
    cardinality = "**"
    composite = "subject"
    inlined=False





