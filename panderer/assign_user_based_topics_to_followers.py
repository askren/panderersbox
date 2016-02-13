from __future__ import division
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import configuration
from build_database_model import User, UserTopicRepresentation
import logging
from gensim import corpora, models, matutils
import os


logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

engine=create_engine(configuration.get_engine_string())

db_session = scoped_session(sessionmaker(bind=engine))


def add_to_db(doc_lda,current_user):
    num_topics=45
    #Convert the doc_lda to an array
    row=matutils.sparse2full(doc_lda,num_topics)
    user_record=db_session.query(UserTopicRepresentation).filter_by(user_id=current_user).first()
    if user_record:
        user_record.topic0 = row[0].item(),
        user_record.topic1 = row[1].item(),
        user_record.topic2 = row[2].item(),
        user_record.topic3 = row[3].item(),
        user_record.topic4 = row[4].item(),
        user_record.topic5 = row[5].item(),
        user_record.topic6 = row[6].item(),
        user_record.topic7 = row[7].item(),
        user_record.topic8 = row[8].item(),
        user_record.topic9 = row[9].item(),
        user_record.topic10 = row[10].item(),
        user_record.topic11 = row[11].item(),
        user_record.topic12 = row[12].item(),
        user_record.topic13 = row[13].item(),
        user_record.topic14 = row[14].item(),
        user_record.topic15 = row[15].item(),
        user_record.topic16 = row[16].item(),
        user_record.topic17 = row[17].item(),
        user_record.topic18 = row[18].item(),
        user_record.topic19 = row[19].item(),
        user_record.topic20 = row[20].item(),
        user_record.topic21 = row[21].item(),
        user_record.topic22 = row[22].item(),
        user_record.topic23 = row[23].item(),
        user_record.topic24 = row[24].item(),
        user_record.topic25 = row[25].item(),
        user_record.topic26 = row[26].item(),
        user_record.topic27 = row[27].item(),
        user_record.topic28 = row[28].item(),
        user_record.topic29 = row[29].item(),
        user_record.topic30 = row[30].item(),
        user_record.topic31 = row[31].item(),
        user_record.topic32 = row[32].item(),
        user_record.topic33 = row[33].item(),
        user_record.topic34 = row[34].item(),
        user_record.topic35 = row[35].item(),
        user_record.topic36 = row[36].item(),
        user_record.topic37 = row[37].item(),
        user_record.topic38 = row[38].item(),
        user_record.topic39 = row[39].item(),
        user_record.topic40 = row[40].item(),
        user_record.topic41 = row[41].item(),
        user_record.topic42 = row[42].item(),
        user_record.topic43 = row[43].item(),
        user_record.topic44 = row[44].item()
    else:
        topic_dist = UserTopicRepresentation(user_id=current_user,
            topic0 = row[0].item(),
            topic1 = row[1].item(),
            topic2 = row[2].item(),
            topic3 = row[3].item(),
            topic4 = row[4].item(),
            topic5 = row[5].item(),
            topic6 = row[6].item(),
            topic7 = row[7].item(),
            topic8 = row[8].item(),
            topic9 = row[9].item(),
            topic10 = row[10].item(),
            topic11 = row[11].item(),
            topic12 = row[12].item(),
            topic13 = row[13].item(),
            topic14 = row[14].item(),
            topic15 = row[15].item(),
            topic16 = row[16].item(),
            topic17 = row[17].item(),
            topic18 = row[18].item(),
            topic19 = row[19].item(),
            topic20 = row[20].item(),
            topic21 = row[21].item(),
            topic22 = row[22].item(),
            topic23 = row[23].item(),
            topic24 = row[24].item(),
            topic25 = row[25].item(),
            topic26 = row[26].item(),
            topic27 = row[27].item(),
            topic28 = row[28].item(),
            topic29 = row[29].item(),
            topic30 = row[30].item(),
            topic31 = row[31].item(),
            topic32 = row[32].item(),
            topic33 = row[33].item(),
            topic34 = row[34].item(),
            topic35 = row[35].item(),
            topic36 = row[36].item(),
            topic37 = row[37].item(),
            topic38 = row[38].item(),
            topic39 = row[39].item(),
            topic40 = row[40].item(),
            topic41 = row[41].item(),
            topic42 = row[42].item(),
            topic43 = row[43].item(),
            topic44 = row[44].item())

        db_session.add(topic_dist)
    db_session.commit()

def get_doc_lda(doc, dictionary, model,current_user):
    bow=dictionary.doc2bow(doc)
    doc_lda=model[bow]
    add_to_db(doc_lda,current_user)

def main():
    model=models.ldamodel.LdaModel.load(configuration.lda_dir + 'cand_lda_model', mmap='r')
    dictionary=corpora.Dictionary.load(configuration.lda_dir + 'cand_lda_dictionary',mmap='r')

    for user in db_session.query(User):
        logger.info("Working on UserID: %s",user.user_id)
        doc=user.user_content
        if doc:
            new_doc=doc[1:-1].split(',')
            get_doc_lda(new_doc, dictionary, model,user.user_id)

if __name__ == "__main__":
    main()
