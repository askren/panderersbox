import os
import json

config_path=os.path.abspath(os.path.join(os.path.dirname(__file__), 'configuration.json'))

_config_dict={}

if os.path.isfile(config_path):
    with open(config_path) as f:
        _config_dict=json.load(f)
else:
    _config_dict=os.environ

twitter_consumer_key=_config_dict['TWITTER_CONSUMER_KEY']
twitter_consumer_secret=_config_dict['TWITTER_CONSUMER_SECRET']
twitter_key=_config_dict['TWITTER_KEY']
twitter_secret=_config_dict['TWITTER_SECRET']
text_dir=_config_dict['TEXT_DIR']
java_home=_config_dict['JAVA_HOME']
lda_dir=_config_dict['LDA_DIR']

def get_engine_string():
    if _config_dict.get('RDS_PASSWORD'):
        return 'postgres://%s:%s@%s/twitter_candidates_and_followers_db'%(_config_dict['RDS_USERNAME'], _config_dict['RDS_PASSWORD'], _config_dict['RDS_HOSTNAME'])
    return 'postgres://%s@%s/twitter_candidates_and_followers_db'%(_config_dict['RDS_USERNAME'], _config_dict['RDS_HOSTNAME'])

def get_conn_dict():
    conn_dict={'database':'twitter_candidates_and_followers_db', 'user': _config_dict['RDS_USERNAME']}
    if _config_dict['RDS_HOSTNAME'] != 'localhost':
        conn_dict['host'] = _config_dict['RDS_HOSTNAME']
    if _config_dict.get('RDS_PASSWORD'):
        conn_dict['password']= _config_dict['RDS_PASSWORD']
    return conn_dict




