import numpy as np
from operator import itemgetter
import candidates
import psycopg2
import pandas as pd
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import configuration


logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

engine=create_engine(configuration.get_engine_string())

db_session = scoped_session(sessionmaker(bind=engine))

con = psycopg2.connect(**configuration.get_conn_dict())

# Utility function to report best scores
def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
              score.mean_validation_score,
              np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")


def do_grid_search(X,y):
    # build a classifier
    clf = RandomForestClassifier(n_estimators=1000, n_jobs=3, class_weight="balanced", max_features='sqrt')

    # use a full grid over relevant parameters
    param_grid = {"max_depth": [10, 20, 30, 40, 50, None],
                  "min_samples_leaf": [1, 3, 5, 10]}

    # run grid search
    grid_search = GridSearchCV(clf, param_grid=param_grid, scoring='roc_auc')
    grid_search.fit(X, y)

    report(grid_search.grid_scores_)


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
    do_grid_search(features,numerical_y)



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
    do_grid_search(features,numerical_y)


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

if __name__ == "__main__":
    main()