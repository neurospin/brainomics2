##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""cubicweb-questionnaire schema"""

from yams.buildobjs import (EntityType,
                            SubjectRelation,
                            String,
                            Int,
                            RichString)


class QuestionnaireRun(EntityType):
    identifier = String(required=True, indexed=True, maxsize=64)
    label = String(maxsize=64)
    subject_age = Int()
    iteration = Int(indexed=True)

    questionnaire = SubjectRelation('Questionnaire', cardinality='1*', inlined=False)
    subject = SubjectRelation('Subject', cardinality='1*', inlined=False)
    result = SubjectRelation("File", cardinality="?1", inlined=True,
                             composite="subject")
    open_answers = SubjectRelation("OpenAnswer", cardinality="*1", inlined=False)

class Questionnaire(EntityType):
    name = String(required=True, unique=True, maxsize=256)
    identifier = String(required=True, indexed=True, maxsize=64)
    type = String(maxsize=256, required=True)
    version = String(maxsize=16)
    note = RichString(fulltextindexed=True)
    questionnaire_runs = SubjectRelation('QuestionnaireRun', cardinality='*1', inlined=False)
    questions = SubjectRelation('Question', cardinality='1*', inlined=False)


class Question(EntityType):
    identifier = String(required=True, unique=True, indexed=True, maxsize=64)
    position = Int(indexed=True)
    text = String(maxsize=1024)
    questionnaire = SubjectRelation('Questionnaire', cardinality='1*', inlined=False)
    answers = SubjectRelation('Questionnaire', cardinality='**', inlined=False)
    open_answers = SubjectRelation("OpenAnswer", cardinality="*1", inlined=False)


class Answer(EntityType):
    value = String(indexed=True)
    type = String(indexed=True)
    question = SubjectRelation('Question', cardinality='**', inlined=False)
    questionnaire_run = SubjectRelation('QuestionnaireRun', cardinality='1*', inlined=False)

class OpenAnswer(EntityType):
    value = String(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)
    questionnaire_run = SubjectRelation("QuestionnaireRun", cardinality="1*", inlined=False)
    question = SubjectRelation("Question", cardinality="1*", inlined=False)
