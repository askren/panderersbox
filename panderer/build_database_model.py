#Model based partly on that in the tweesql package.
from sqlalchemy import Column, ForeignKey, BigInteger, Integer, String, Float, Boolean,Table, create_engine
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

import configuration

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    tweet_id = Column(BigInteger, primary_key=True, nullable=False)
    tweet_text=Column(String)
    tweet_content = Column(String)
    tweet_record=Column(JSON)
    hashtag=Column(String)
    hashtag_content=Column(String)
    in_reply_to_status_id = Column(BigInteger)
    in_reply_to_user_id = Column(BigInteger)
    favorited = Column(Boolean,unique=False)
    retweeted = Column(Boolean,unique=False)
    lang = Column(String)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    users = relationship('User')

class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True, nullable=False)
    screen_name = Column(String)
    location=Column(String)
    user_desc=Column(String)
    verified=Column(Boolean,unique=False)
    followers_count=Column(Integer)
    friends_count=Column(Integer)
    list_count=Column(Integer)
    user_content=Column(String)
    favorite_count=Column(Integer)
    tweet_count=Column(Integer)
    user_lang=Column(String)

class UserToCand(Base):
    __tablename__ = 'user_candidate'
    link_id = Column(BigInteger, primary_key=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    candidate = Column(String)
    party = Column(String)

class TopicRepresentation(Base):
    __tablename__ = 'topics'
    record_id = Column(BigInteger, primary_key=True, nullable=False)
    topic0=Column(Float)
    topic1=Column(Float)
    topic2=Column(Float)
    topic3=Column(Float)
    topic4=Column(Float)
    topic5=Column(Float)
    topic6=Column(Float)
    topic7=Column(Float)
    topic8=Column(Float)
    topic9=Column(Float)
    topic10=Column(Float)
    topic11=Column(Float)
    topic12=Column(Float)
    topic13=Column(Float)
    topic14=Column(Float)
    topic15=Column(Float)
    topic16=Column(Float)
    topic17=Column(Float)
    topic18=Column(Float)
    topic19=Column(Float)
    topic20=Column(Float)
    topic21=Column(Float)
    topic22=Column(Float)
    topic23=Column(Float)
    topic24=Column(Float)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    users = relationship('User')


class UserTopicRepresentation(Base):
    __tablename__ = 'user_topics'
    record_id = Column(BigInteger, primary_key=True, nullable=False)
    topic0=Column(Float)
    topic1=Column(Float)
    topic2=Column(Float)
    topic3=Column(Float)
    topic4=Column(Float)
    topic5=Column(Float)
    topic6=Column(Float)
    topic7=Column(Float)
    topic8=Column(Float)
    topic9=Column(Float)
    topic10=Column(Float)
    topic11=Column(Float)
    topic12=Column(Float)
    topic13=Column(Float)
    topic14=Column(Float)
    topic15=Column(Float)
    topic16=Column(Float)
    topic17=Column(Float)
    topic18=Column(Float)
    topic19=Column(Float)
    topic20=Column(Float)
    topic21=Column(Float)
    topic22=Column(Float)
    topic23=Column(Float)
    topic24=Column(Float)
    topic25=Column(Float)
    topic26=Column(Float)
    topic27=Column(Float)
    topic28=Column(Float)
    topic29=Column(Float)
    topic30=Column(Float)
    topic31=Column(Float)
    topic32=Column(Float)
    topic33=Column(Float)
    topic34=Column(Float)
    topic35=Column(Float)
    topic36=Column(Float)
    topic37=Column(Float)
    topic38=Column(Float)
    topic39=Column(Float)
    topic40=Column(Float)
    topic41=Column(Float)
    topic42=Column(Float)
    topic43=Column(Float)
    topic44=Column(Float)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    users = relationship('User')

class Candidate(Base):
    __tablename__ = 'candidates'
    candidate_id = Column(BigInteger, primary_key=True, nullable=False)
    message_topic0=Column(Float)
    message_topic1=Column(Float)
    message_topic2=Column(Float)
    message_topic3=Column(Float)
    message_topic4=Column(Float)
    message_topic5=Column(Float)
    message_topic6=Column(Float)
    message_topic7=Column(Float)
    message_topic8=Column(Float)
    message_topic9=Column(Float)
    message_topic10=Column(Float)
    message_topic11=Column(Float)
    message_topic12=Column(Float)
    message_topic13=Column(Float)
    message_topic14=Column(Float)
    message_topic15=Column(Float)
    message_topic16=Column(Float)
    message_topic17=Column(Float)
    message_topic18=Column(Float)
    message_topic19=Column(Float)
    message_topic20=Column(Float)
    message_topic21=Column(Float)
    message_topic22=Column(Float)
    message_topic23=Column(Float)
    message_topic24=Column(Float)
    message_topic25=Column(Float)
    message_topic26=Column(Float)
    message_topic27=Column(Float)
    message_topic28=Column(Float)
    message_topic29=Column(Float)
    message_topic30=Column(Float)
    message_topic31=Column(Float)
    message_topic32=Column(Float)
    message_topic33=Column(Float)
    message_topic34=Column(Float)
    message_topic35=Column(Float)
    message_topic36=Column(Float)
    message_topic37=Column(Float)
    message_topic38=Column(Float)
    message_topic39=Column(Float)
    message_topic40=Column(Float)
    message_topic41=Column(Float)
    message_topic42=Column(Float)
    message_topic43=Column(Float)
    message_topic44=Column(Float)
    v_same_party_acc=Column(Float)
    v_same_party_prec=Column(Float)
    v_same_party_recall=Column(Float)
    v_same_party_f1=Column(Float)
    v_same_party_roc_auc=Column(Float)
    v_same_party_importances=Column(String)
    v_opp_party_acc=Column(Float)
    v_opp_party_prec=Column(Float)
    v_opp_party_recall=Column(Float)
    v_opp_party_f1=Column(Float)
    v_opp_party_roc_auc=Column(Float)
    v_opp_party_importances=Column(String)
    candidate = Column(String)


if __name__=="__main__":
    engine=create_engine(configuration.get_engine_string())

    #create the database
    if not database_exists(engine.url):
        create_database(engine.url)

    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

    #Make the tables
    Base.metadata.create_all(bind=engine)