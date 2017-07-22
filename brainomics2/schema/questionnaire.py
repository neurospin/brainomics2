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


ANSWERS_RTYPE = ("text", "int", "float")


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
    """ Define a Question entity.

    The position attribute defines the euestionnaire associated questions
    order.
    The choices attribute is a csv field with all possible answers. It can be
    used to preserve the database. In this case use an IntAnswer entity to
    store the index of the answer.
    """
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    position = Int(indexed=True)
    text = String(maxsize=1024)
    choices = String()
    type = String(maxsize=10)


class TextAnswer(EntityType):
    value = String(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)


class IntAnswer(EntityType):
    value = Int(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)


class FloatAnswer(EntityType):
    value = Float(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)
