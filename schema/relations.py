##########################################################################
# NSAp - Copyright (C) CEA, 2016
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

from yams.buildobjs import RelationDefinition


class questionnaire_runs(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Questionnaire", "Assessment", "Study", "Subject")
    object = "QuestionnaireRun"
    cardinality = "*1"
    composite = "subject"


class external_files(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "FileSet"
    object = "ExternalFile"
    cardinality = "*1"
    composite = "subject"


class subjects(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("GenomicMeasure", "Study", "ProcessingRun",
               "SubjectGroup", "Center", "Assessment")
    object = "Subject"
    cardinality = "**"


class subject(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("QuestionnaireRun", "Diagnostic", "Scan")
    object = "Subject"
    cardinality = "+*"


class study(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Subject", "SubjectGroup", "Protocol", "Assessment",
               "ProcessingRun", "Scan", "QuestionnaireRun", "GenomicMeasure")
    object = "Study"
    cardinality = "1*"
    composite = "object"


class score_definition(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "ScoreValue"
    object = "ScoreDefinition"
    cardinality = "1*"
    composite = "object"


class score_values(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Scan", "ProcessingRun", "ScoreDefinition")
    object = "ScoreValue"
    cardinality = "*1"
    composite = "subject"


class fileset(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("File", "ExternalFile")
    object = "FileSet"
    cardinality = "**"
    composite = "object"


class assessments(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Subject", "Study", "Center", "Protocol")
    object = "Assessment"
    cardinality = "**"
    composite = "subject"


class subjectgroups(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Subject", "Study")
    object = "SubjectGroup"
    cardinality = "*+"


class diagnostic(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Subject"
    object = "Diagnostic"
    cardinality = "?+"


class scans(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Subject", "Study", "Assessment")
    object = "Scan"
    cardinality = "*1"
    composite = "subject"


class center(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Assessment", "Subject", "Device")
    object = "Center"
    cardinality = "**"
    composite = "object"


class genomic_measures(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Assessment", "Subject", "Study", "GenomicPlatform")
    object = "GenomicMeasure"
    cardinality = "*+"


class protocols(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Study"
    object = "Protocol"
    cardinality = "*1"
    composite = "subject"


class protocol(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Assessment"
    object = "Protocol"
    cardinality = "?*"


class processing_runs(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Assessment", "GenomicMeasure", "Scan", "Study", "Subject")
    object = "ProcessingRun"
    cardinality = "**"


class results_filesets(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("ProcessingRun", "GenomicMeasure", "Scan")
    object = "FileSet"
    cardinality = "**"


class config_filesets(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "ProcessingRun"
    object = "FileSet"
    cardinality = "**"


class inputs(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "ProcessingRun"
    object = ("GenomicMeasure", "Scan")
    cardinality = "**"


class genes(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Chromosome"
    object = "Gene"
    cardinality = "*+"


class chromosomes(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Gene"
    object = "Chromosome"
    cardinality = "+*"


class chromosome(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Snp"
    object = "Chromosome"
    cardinality = "?*"
    composite = "object"


class genomic_platforms(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Snp"
    object = "GenomicPlatform"
    cardinality = "**"


class genomic_platform(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "GenomicMeasure"
    object = "GenomicPlatform"
    cardinality = "?*"
    composite = "object"


class snps(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "GenomicPlatform"
    object = "Snp"
    cardinality = "**"


class has_data(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Scan"
    object = ('MRIData', 'DMRIData',
              'FMRIData', 'EEGData', 'ETData', 'PETData')
    cardinality = "?1"
    composite = "subject"


class result(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = True
    subject = "QuestionnaireRun"
    object = "File"
    cardinality = "??"
    composite = "subject"


class open_answers(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Question", "QuestionnaireRun")
    object = "OpenAnswer"
    cardinality = "*1"
    composite = "subject"


class questions(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Questionnaire"
    object = "Question"
    cardinality = "+1"
    composite = "subject"


class questionnaire(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Question", "QuestionnaireRun")
    object = "Questionnaire"
    cardinality = "1+"
    composite = "object"


class answers(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = "Question"
    object = "Answer"
    cardinality = "*1"
    composite = "subject"


class question(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Answer", "OpenAnswer")
    object = "Question"
    cardinality = "1*"


class questionnaire_run(RelationDefinition):
    __permissions__ = {
        'read':   ('managers', 'users', 'guests'),
        'add':    ('managers',),
        'delete': ('managers',)}
    inlined = False
    subject = ("Answer", "OpenAnswer")
    object = "QuestionnaireRun"
    cardinality = "1*"
    composite = "object"
