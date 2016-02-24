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


class QuestionnaireRun(EntityType):
    identifier = String(required=True, indexed=True, maxsize=64)
    label = String(maxsize=64)
    subject_age = Int()
    iteration = Int(indexed=True)


class Questionnaire(EntityType):
    name = String(required=True, unique=True, maxsize=256)
    identifier = String(required=True, indexed=True, maxsize=64)
    type = String(maxsize=256, required=True)
    version = String(maxsize=16)
    note = RichString(fulltextindexed=True)


class Question(EntityType):
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    position = Int(indexed=True)
    text = String(maxsize=1024)


class Answer(EntityType):
    value = String(indexed=True)
    type = String(indexed=True)


class OpenAnswer(EntityType):
    value = String(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)

