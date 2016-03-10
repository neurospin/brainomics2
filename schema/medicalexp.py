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


class Study(EntityType):
    """ The project """
    name = String(required=True, indexed=True, maxsize=256)
    description = RichString(fulltextindexed=True)
    data_filepath = String()


class SubjectGroup(EntityType):
    """ Group of subject """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=64, required=True, indexed=False)
    type = String(maxsize=64, required=True, 
                  vocabulary=[u"family", u"schedule"])


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


class Protocol(EntityType):
    """ A protocol for a study or a measure """
    identifier = String(required=True, unique=True, maxsize=64)
    name = String(maxsize=256, required=True, unique=True)


class Diagnostic(EntityType):
    """ Diagnostic attributes and links.
    Diagnostic may be based on specific measures, and holds a conclusion
    on BodyLocation/Disease """
    age_at_diagnosis = Int()


class Assessment(EntityType):
    """ Store information about a visit """
    identifier = String(required=True, maxsize=128, unique=True)
    age_of_subject = Float(indexed=True)
    timepoint = String(maxsize=64, indexed=True)


class ProcessingRun(EntityType):
    identifier = String(required=True, maxsize=128, unique=True)
    type = String(maxsize=256, required=True)
    label = String(maxsize=256)
    tool = String(maxsize=256)
    datetime = Date()
    category = String(maxsize=256)
    version = String(maxsize=64)
    parameters = String(maxsize=256)
    note = RichString(fulltextindexed=True)


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
