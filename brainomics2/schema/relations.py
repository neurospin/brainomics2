##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Do not deal with composition relation properties since the generated databases
are not expected to be dynamics.
"""

# Cubicweb import
from yams.buildobjs import RelationDefinition
from yams.buildobjs import SubjectRelation
from cubicweb.schema import RRQLExpression

# Local import
from cubes.brainomics2.schema.neuroimaging import SCAN_DATA
from cubes.rql_upload.schema import UPLOAD_RELATION_PERMISSIONS


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


class questionnaire_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Assessment"
    object = "QuestionnaireRun"
    cardinality = "*1"


class questionnaire_questionnaire_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Questionnaire"
    object = "QuestionnaireRun"
    cardinality = "*1"


class study_questionnaire_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "QuestionnaireRun"
    cardinality = "*1"


# Subject

class subject_protocol(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "Protocol"
    cardinality = "?*"


class subject_questionnaire_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "QuestionnaireRun"
    cardinality = "*1"


class external_files(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "FileSet"
    object = "ExternalFile"
    cardinality = "*1"


class subjects(RelationDefinition):
    __permissions__ = UPLOAD_RELATION_PERMISSIONS
    inlined = False
    subject = ("GenomicMeasure", "Study", "ProcessingRun",
               "SubjectGroup", "Center", "Assessment", "Diagnostic",
               "Protocol")
    object = "Subject"
    cardinality = "**"


class subject(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("QuestionnaireRun", "Scan")
    object = "Subject"
    cardinality = "+*"


class study(RelationDefinition):
    __permissions__ = UPLOAD_RELATION_PERMISSIONS
    inlined = False
    subject = ("Subject", "SubjectGroup", "Protocol", "Assessment",
               "ProcessingRun", "Scan", "QuestionnaireRun", "GenomicMeasure")
    object = "Study"
    cardinality = "1*"


class score_definition(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "ScoreValue"
    object = "ScoreDefinition"
    cardinality = "?*"


class score_values(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("Scan", "ProcessingRun", "GenomicMeasure")
    object = "ScoreValue"
    cardinality = "*1"


class scoredefinition_score_values(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "ScoreDefinition"
    object = "ScoreValue"
    cardinality = "*?"


class fileset(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("RestrictedFile", "ExternalFile")
    object = "FileSet"
    cardinality = "**"


class assessments(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("Subject", "Study", "Center", "Protocol")
    object = "Assessment"
    cardinality = "**"


class subjectgroups(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "SubjectGroup"
    cardinality = "*+"


class study_subjectgroups(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "SubjectGroup"
    cardinality = "*+"


class diagnostic(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "Diagnostic"
    cardinality = "*+"


class scan(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = SCAN_DATA
    object = "Scan"
    cardinality = "1*"


class has_data(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Scan"
    object = SCAN_DATA
    cardinality = "*1"


class scans(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Assessment"
    object = "Scan"
    cardinality = "*1"


class subject_scans(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "Scan"
    cardinality = "*1"


class study_scans(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "Scan"
    cardinality = "*1"


class center(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("Assessment", "Subject", "Device")
    object = "Center"
    cardinality = "**"


class device(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Assessment"
    object = "Device"
    cardinality = "?*"


class device_assessments(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Device"
    object = "Assessment"
    cardinality = "*?"


class genomic_measures(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Assessment"
    object = "GenomicMeasure"
    cardinality = "*1"


class genomic_platform_genomic_measures(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "GenomicPlatform"
    object = "GenomicMeasure"
    cardinality = "*1"


class subject_genomic_measures(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "GenomicMeasure"
    cardinality = "*+"


class study_genomic_measures(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "GenomicMeasure"
    cardinality = "*+"


class protocols(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "Protocol"
    cardinality = "*1"


class protocol(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Assessment"
    object = "Protocol"
    cardinality = "?*"


class processing_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("Assessment", "GenomicMeasure", "Scan", "ProcessingRun")
    object = "ProcessingRun"
    cardinality = "**"


class study_processing_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Study"
    object = "ProcessingRun"
    cardinality = "*1"


class subject_processing_runs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Subject"
    object = "ProcessingRun"
    cardinality = "**"


class filesets(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("ProcessingRun", "GenomicMeasure", "Scan", "Device")
    object = "FileSet"
    cardinality = "*+"


class containers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "FileSet"
    object = ("ProcessingRun", "GenomicMeasure", "Scan", "Device")
    cardinality = "+*"


class inputs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "ProcessingRun"
    object = ("GenomicMeasure", "Scan", "ProcessingRun", "QuestionnaireRun")
    cardinality = "**"


# Chromosome

class chromosome_genes(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Chromosome"
    object = "Gene"
    cardinality = "*1"


class chromosome_snps(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Chromosome"
    object = "Snp"
    cardinality = "*?" # *1


class chromosome_cpgs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Chromosome"
    object = "CpG"
    cardinality = "*1"


# Gene

class gene_chromosome(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Gene"
    object = "Chromosome"
    cardinality = "1*"


class gene_snps(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Gene"
    object = "Snp"
    cardinality = "**"


class gene_cpgs(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Gene"
    object = "CpG"
    cardinality = "**"


# Snp

class snp_chromosome(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Snp"
    object = "Chromosome"
    cardinality = "?*" # 1*


class snp_genes(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Snp"
    object = "Gene"
    cardinality = "**"


class genomic_platforms(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Snp"
    object = "GenomicPlatform"
    cardinality = "**"


# CpG

class cpg_chromosome(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "CpG"
    object = "Chromosome"
    cardinality = "1*"


class cpg_genes(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "CpG"
    object = "Gene"
    cardinality = "**"


# GenomicPlatform

class snps(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "GenomicPlatform"
    object = "Snp"
    cardinality = "**"



class genomic_platform(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "GenomicMeasure"
    object = "GenomicPlatform"
    cardinality = "?*"


# Questionnaire

class text_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "QuestionnaireRun"
    object = "TextAnswer"
    cardinality = "*1"


class int_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "QuestionnaireRun"
    object = "IntAnswer"
    cardinality = "*1"


class float_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "QuestionnaireRun"
    object = "FloatAnswer"
    cardinality = "*1"


class question_text_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Question"
    object = "TextAnswer"
    cardinality = "*1"


class question_int_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Question"
    object = "IntAnswer"
    cardinality = "*1"


class question_float_answers(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Question"
    object = "FloatAnswer"
    cardinality = "*1"


class questions(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = "Questionnaire"
    object = "Question"
    cardinality = "+1"


class questionnaire(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("Question", "QuestionnaireRun")
    object = "Questionnaire"
    cardinality = "1*"


class question(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("TextAnswer", "IntAnswer", "FloatAnswer")
    object = "Question"
    cardinality = "1*"


class questionnaire_run(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = False
    subject = ("TextAnswer", "IntAnswer", "FloatAnswer")
    object = "QuestionnaireRun"
    cardinality = "1*"


class file(RelationDefinition):
    __permissions__ = RELATION_PERMISSIONS
    inlined = True
    subject = "QuestionnaireRun"
    object = "RestrictedFile"
    cardinality = "??"
