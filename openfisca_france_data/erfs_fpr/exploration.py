#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from openfisca_survey_manager.survey_collections import SurveyCollection


year = 2012
erfs_fpr_survey_collection = SurveyCollection.load(collection = 'erfs_fpr')
yr = str(year)[-2:]  # 12 for 2012
survey = erfs_fpr_survey_collection.get_survey('erfs_fpr_{}'.format(year))
# fpr_menage = survey.get_values(table = 'fpr_menage_{}_retropole'.format(year))
# eec_menage = survey.get_values(table = 'fpr_mrf{}e{}t4'.format(yr, yr))
eec_individu = survey.get_values(table = 'fpr_irf{}e{}t4'.format(yr, yr))
# fpr_individu = survey.get_values(table = 'fpr_indiv_{}_retropole'.format(year))