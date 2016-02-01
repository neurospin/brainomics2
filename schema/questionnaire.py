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

"""cubicweb-questionnaire schema"""

from yams.buildobjs import (EntityType,
                            SubjectRelation,
                            String,
                            Int,
                            Float,
                            Date,
                            Boolean,
                            RichString)


class QuestionnaireRun(EntityType):
    identifier = String(required=True, indexed=True, maxsize=64)
    subject_age = Int()
    iteration = Int(indexed=True)
    questionnaire = SubjectRelation('Questionnaire', cardinality='1*', inlined=False)
    # assessment = SubjectRelation('Assessment', cardinality='1*', inlined=False)
    subject = SubjectRelation('Subject', cardinality='1*', inlined=False)
    result = SubjectRelation("File", cardinality="1?", inlined=False,
                             composite="subject")
    study = SubjectRelation('Study', cardinality='1*', inlined=False)

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


class Answer(EntityType):
    value = String(indexed=True)
    type = String(indexed=True)
    question = SubjectRelation('Question', cardinality='**', inlined=False)
    questionnaire_run = SubjectRelation('QuestionnaireRun', cardinality='1*', inlined=False)

# XXX to remove
class OpenAnswer(EntityType):
    value = String(required=True)
    identifier = String(maxsize=64, indexed=True, unique=True)
    questionnaire_run = SubjectRelation("QuestionnaireRun", cardinality="1*", inlined=False)
