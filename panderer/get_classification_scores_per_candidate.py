import candidates
import psycopg2
import pandas as pd
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import numpy as np
import logging
import candidate_messaging
import configuration
from build_database_model import Candidate

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

engine=create_engine(configuration.get_engine_string())

db_session = scoped_session(sessionmaker(bind=engine))

con = psycopg2.connect(**configuration.get_conn_dict())

def add_to_database(candidate,messaging_topics,same_dict,opp_dict):
    cand_record=db_session.query(Candidate).filter_by(candidate=candidate).first()
    if cand_record:
        cand_record.message_topic0 = messaging_topics['topic0']
        cand_record.message_topic1 = messaging_topics['topic1'],
        cand_record.message_topic2 = messaging_topics['topic2'],
        cand_record.message_topic3 = messaging_topics['topic3'],
        cand_record.message_topic4 = messaging_topics['topic4'],
        cand_record.message_topic5 = messaging_topics['topic5'],
        cand_record.message_topic6 = messaging_topics['topic6'],
        cand_record.message_topic7 = messaging_topics['topic7'],
        cand_record.message_topic8 = messaging_topics['topic8'],
        cand_record.message_topic9 = messaging_topics['topic9'],
        cand_record.message_topic10 = messaging_topics['topic10'],
        cand_record.message_topic11 = messaging_topics['topic11'],
        cand_record.message_topic12 = messaging_topics['topic12'],
        cand_record.message_topic13 = messaging_topics['topic13'],
        cand_record.message_topic14 = messaging_topics['topic14'],
        cand_record.message_topic15 = messaging_topics['topic15'],
        cand_record.message_topic16 = messaging_topics['topic16'],
        cand_record.message_topic17 = messaging_topics['topic17'],
        cand_record.message_topic18 = messaging_topics['topic18'],
        cand_record.message_topic19 = messaging_topics['topic19'],
        cand_record.message_topic20 = messaging_topics['topic20'],
        cand_record.message_topic21 = messaging_topics['topic21'],
        cand_record.message_topic22 = messaging_topics['topic22'],
        cand_record.message_topic23 = messaging_topics['topic23'],
        cand_record.message_topic24 = messaging_topics['topic24'],
        cand_record.message_topic25 = messaging_topics['topic25'],
        cand_record.message_topic26 = messaging_topics['topic26'],
        cand_record.message_topic27 = messaging_topics['topic27'],
        cand_record.message_topic28 = messaging_topics['topic28'],
        cand_record.message_topic29 = messaging_topics['topic29'],
        cand_record.message_topic30 = messaging_topics['topic30'],
        cand_record.message_topic31 = messaging_topics['topic31'],
        cand_record.message_topic32 = messaging_topics['topic32'],
        cand_record.message_topic33 = messaging_topics['topic33'],
        cand_record.message_topic34 = messaging_topics['topic34'],
        cand_record.message_topic35 = messaging_topics['topic35'],
        cand_record.message_topic36 = messaging_topics['topic36'],
        cand_record.message_topic37 = messaging_topics['topic37'],
        cand_record.message_topic38 = messaging_topics['topic38'],
        cand_record.message_topic39 = messaging_topics['topic39'],
        cand_record.message_topic40 = messaging_topics['topic40'],
        cand_record.message_topic41 = messaging_topics['topic41'],
        cand_record.message_topic42 = messaging_topics['topic42'],
        cand_record.message_topic43 = messaging_topics['topic43'],
        cand_record.message_topic44 = messaging_topics['topic44'],
        cand_record.v_same_party_acc=same_dict['avg_acc'],
        cand_record.v_same_party_prec=same_dict['avg_prec'],
        cand_record.v_same_party_recall=same_dict['avg_rec'],
        cand_record.v_same_party_f1=same_dict['avg_f1'],
        cand_record.v_same_party_roc_auc=same_dict['roc_auc'],
        cand_record.v_same_party_importances=same_dict['feature_weights'],
        cand_record.v_opp_party_acc=opp_dict['avg_acc'],
        cand_record.v_opp_party_prec=opp_dict['avg_prec'],
        cand_record.v_opp_party_recall=opp_dict['avg_rec'],
        cand_record.v_opp_party_f1=opp_dict['avg_f1'],
        cand_record.v_opp_party_roc_auc=opp_dict['roc_auc'],
        cand_record.v_opp_party_importances=opp_dict['feature_weights']
    else:
        cand_scores = Candidate(
            message_topic0 = messaging_topics['topic0'],
            message_topic1 = messaging_topics['topic1'],
            message_topic2 = messaging_topics['topic2'],
            message_topic3 = messaging_topics['topic3'],
            message_topic4 = messaging_topics['topic4'],
            message_topic5 = messaging_topics['topic5'],
            message_topic6 = messaging_topics['topic6'],
            message_topic7 = messaging_topics['topic7'],
            message_topic8 = messaging_topics['topic8'],
            message_topic9 = messaging_topics['topic9'],
            message_topic10 = messaging_topics['topic10'],
            message_topic11 = messaging_topics['topic11'],
            message_topic12 = messaging_topics['topic12'],
            message_topic13 = messaging_topics['topic13'],
            message_topic14 = messaging_topics['topic14'],
            message_topic15 = messaging_topics['topic15'],
            message_topic16 = messaging_topics['topic16'],
            message_topic17 = messaging_topics['topic17'],
            message_topic18 = messaging_topics['topic18'],
            message_topic19 = messaging_topics['topic19'],
            message_topic20 = messaging_topics['topic20'],
            message_topic21 = messaging_topics['topic21'],
            message_topic22 = messaging_topics['topic22'],
            message_topic23 = messaging_topics['topic23'],
            message_topic24 = messaging_topics['topic24'],
            message_topic25 = messaging_topics['topic25'],
            message_topic26 = messaging_topics['topic26'],
            message_topic27 = messaging_topics['topic27'],
            message_topic28 = messaging_topics['topic28'],
            message_topic29 = messaging_topics['topic29'],
            message_topic30 = messaging_topics['topic30'],
            message_topic31 = messaging_topics['topic31'],
            message_topic32 = messaging_topics['topic32'],
            message_topic33 = messaging_topics['topic33'],
            message_topic34 = messaging_topics['topic34'],
            message_topic35 = messaging_topics['topic35'],
            message_topic36 = messaging_topics['topic36'],
            message_topic37 = messaging_topics['topic37'],
            message_topic38 = messaging_topics['topic38'],
            message_topic39 = messaging_topics['topic39'],
            message_topic40 = messaging_topics['topic40'],
            message_topic41 = messaging_topics['topic41'],
            message_topic42 = messaging_topics['topic42'],
            message_topic43 = messaging_topics['topic43'],
            message_topic44 = messaging_topics['topic44'],
            v_same_party_acc=same_dict['avg_acc'],
            v_same_party_prec=same_dict['avg_prec'],
            v_same_party_recall=same_dict['avg_rec'],
            v_same_party_f1=same_dict['avg_f1'],
            v_same_party_roc_auc=same_dict['roc_auc'],
            v_same_party_importances=same_dict['feature_weights'],
            v_opp_party_acc=opp_dict['avg_acc'],
            v_opp_party_prec=opp_dict['avg_prec'],
            v_opp_party_recall=opp_dict['avg_rec'],
            v_opp_party_f1=opp_dict['avg_f1'],
            v_opp_party_roc_auc=opp_dict['roc_auc'],
            v_opp_party_importances=opp_dict['feature_weights'],
            candidate=candidate)

        db_session.add(cand_scores)
    db_session.commit()


def run_random_forest(features,numerical_y):
    X_train, X_test, y_train, y_test = train_test_split(features, numerical_y, random_state=0)
    clf=RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3)
    clf=clf.fit(X_train,y_train)

    scores={}

    scores['feature_weights']=clf.feature_importances_.tolist()

    scores['avg_acc']=np.mean(cross_val_score(RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3), features, numerical_y, scoring='accuracy', cv=10))
    scores['avg_prec']=np.mean(cross_val_score(RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3), features, numerical_y, scoring='precision', cv=10))
    scores['avg_rec']=np.mean(cross_val_score(RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3), features, numerical_y, scoring='recall', cv=10))
    scores['avg_f1']=np.mean(cross_val_score(RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3), features, numerical_y, scoring='f1', cv=10))
    scores['roc_auc']=np.mean(cross_val_score(RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt',max_depth=30,min_samples_leaf=3), features, numerical_y, scoring='roc_auc', cv=10))
    return scores


def get_opp_comparison(candidate,data,opp_party):
    party_data=data[data['party']==opp_party]
    candidate_data=data[data['candidate']==candidate]
    full_dataset=party_data.append(candidate_data)
    comparison_dataset=full_dataset.sample(frac=1).reset_index(drop=True)

    y_labels=comparison_dataset['candidate'].tolist()

    numerical_y=np.zeros(np.size(y_labels))
    for item in np.arange(len(numerical_y)):
        if y_labels[item]==candidate:
            numerical_y[item]=1

    features=comparison_dataset.loc[:, ['topic0', 'topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9',
                            'topic10','topic11', 'topic12','topic13','topic14', 'topic15', 'topic16','topic17','topic18',
                            'topic19', 'topic20', 'topic21', 'topic22', 'topic23', 'topic24', 'topic25', 'topic26', 'topic27',
                            'topic28', 'topic29', 'topic30', 'topic31', 'topic32', 'topic33', 'topic34', 'topic35', 'topic36',
                            'topic37', 'topic38','topic39','topic40','topic41','topic42','topic43','topic44']]
    logger.info("Running opposite party model")
    opp_dict=run_random_forest(features,numerical_y)
    return opp_dict


def get_same_comparison(candidate,data,same_party):
    same_data=data[data['party']==same_party]
    party_data=same_data.sample(frac=1).reset_index(drop=True)
    y_labels=party_data['candidate'].tolist()

    numerical_y=np.zeros(np.size(y_labels))
    for item in np.arange(len(numerical_y)):
        if y_labels[item]==candidate:
            numerical_y[item]=1

    features=party_data.loc[:, ['topic0', 'topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9',
                            'topic10','topic11', 'topic12','topic13','topic14', 'topic15', 'topic16','topic17','topic18',
                            'topic19', 'topic20', 'topic21', 'topic22', 'topic23', 'topic24', 'topic25', 'topic26', 'topic27',
                            'topic28', 'topic29', 'topic30', 'topic31', 'topic32', 'topic33', 'topic34', 'topic35', 'topic36',
                            'topic37', 'topic38','topic39','topic40','topic41','topic42','topic43','topic44']]
    logger.info("Running same party model")
    same_dict=run_random_forest(features,numerical_y)
    return same_dict


def main():
    #Go ahead and pull the data across all relevant candidates; leave out candidates who had very few identified followers
    sql_query="SELECT * FROM user_topics INNER JOIN user_candidate ON (user_topics.user_id = user_candidate.user_id);"
    user_level_topic_data=pd.read_sql_query(sql_query,con)

    for candidate in candidates.all_candidates.values():
        logger.info("Working on candidate: %s", candidate.surname)
        same_party=candidate.party

        opp_party=''

        if same_party=='Democrat':
            opp_party='Republican'
        elif same_party=='Republican':
            opp_party='Democrat'

        same_dict=get_same_comparison(candidate.surname,user_level_topic_data,same_party)
        opp_dict=get_opp_comparison(candidate.surname,user_level_topic_data,opp_party)

        messaging_topics=candidate_messaging.get_candidate_messaging(candidate.surname)

        add_to_database(candidate.surname,messaging_topics,same_dict,opp_dict)

if __name__ == "__main__":
    main()