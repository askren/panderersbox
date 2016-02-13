import os
import pandas as pd
import psycopg2
import numpy as np
from gensim import models
import configuration
import candidates

con = psycopg2.connect(**configuration.get_conn_dict())

model=models.ldamodel.LdaModel.load(configuration.lda_dir + 'cand_lda_model',mmap='r')


def get_important_topics(importances):
    float_importances=importances.astype(np.float)
    totalimportance=np.sum(np.array(float_importances))
    top_features=np.argpartition(importances,-3)[-3:][::-1]
    feature_tooltips=[]
    label_words=[]
    labels=[]
    feature_count=0
    for feature in top_features:
        potential_label_word=model.show_topic(feature,1)[0][0]
        labelnum=1
        while potential_label_word in label_words:
            potential_label_word=model.show_topic(feature,labelnum+1)[labelnum][0]
            labelnum=labelnum+1
        label_word=potential_label_word
        label_words.append(label_word)
        ten_words=[x[0] for x in model.show_topic(feature,10)]
        joinstr=", "
        formatted_ten=joinstr.join(ten_words)
        feature_tooltips.append(formatted_ten)
        pct_pred='{0:.2%}'.format(float_importances[feature]/totalimportance)
        labels.append('%s (%s)' %(label_word,pct_pred))
        feature_count=feature_count+1
    return top_features,labels,feature_tooltips


def get_data(comparison,candidate,labels,top_features,feature_tooltips,party):

    #pull mean info for the right candidate
    topic_string=""
    feature_count=0
    for topic_num in top_features:
        topic_string=topic_string + ", AVG(topic%s) as topic%s"%(topic_num,feature_count)
        feature_count=feature_count+1

    cand_supp_query="SELECT user_candidate.candidate%s FROM user_topics INNER JOIN user_candidate ON (user_topics.user_id = user_candidate.user_id) WHERE user_candidate.candidate='%s' GROUP BY user_candidate.candidate;" %(topic_string, candidate)
    candidate_supp_data=pd.read_sql_query(cand_supp_query,con)

    party_query="SELECT user_candidate.party%s FROM user_topics INNER JOIN user_candidate ON (user_topics.user_id = user_candidate.user_id) WHERE user_candidate.candidate !='%s' AND party = '%s' GROUP BY user_candidate.party;" %(topic_string, candidate, party)
    party_data=pd.read_sql_query(party_query,con)

    all_data=candidate_supp_data.append(party_data)
    all_data['label']='comparison'
    all_data['label'][all_data['candidate']==candidate]="ChosenCandidate"


    all_data.drop('candidate', axis=1, inplace=True)
    all_data.drop('party', axis=1, inplace=True)
    all_data.set_index(['label'],inplace=True)

    flipped=all_data.T
    flipped['index_word']=labels
    flipped['topic_words']=feature_tooltips

    return flipped

def get_scores(candidate, comparison, party):

    cand_query="SELECT candidate, v_%s_party_acc, v_%s_party_roc_auc, v_%s_party_importances FROM candidates WHERE candidate='%s';" %(comparison,comparison,comparison,candidate)
    cand_scores=pd.read_sql_query(cand_query,con)

    acc='{0:.2%}'.format(cand_scores['v_%s_party_acc'%(comparison)][0])
    auc='{0:.2}'.format(cand_scores['v_%s_party_roc_auc'%(comparison)][0])

    importances=np.array(cand_scores['v_%s_party_importances'%(comparison)][0][1:-1].split(","))

    top_features,labels,feature_tooltips=get_important_topics(importances)

    comparison_data=get_data('same',candidate,labels,top_features,feature_tooltips,party)

    return acc,auc,comparison_data
