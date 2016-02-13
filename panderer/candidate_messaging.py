import glob
import os
from gensim import models,corpora,matutils
import logging

import configuration

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def add_to_dict(doc_lda):
    messaging={}
    num_topics=45
    row=matutils.sparse2full(doc_lda,num_topics)
    for topic in range(0,num_topics):
        label="topic%s"%(topic)
        messaging[label]=row[topic].item()
    return messaging

def get_doc_lda(full_doc, dictionary, model):
    bow=dictionary.doc2bow(full_doc)
    doc_lda=model[bow]
    messaging=add_to_dict(doc_lda)
    return messaging

def get_candidate_messaging(candidate):
    logger.info("Assigning messaging")
    model=models.ldamodel.LdaModel.load(configuration.lda_dir + 'cand_lda_model',mmap='r')
    dictionary=corpora.Dictionary.load(configuration.lda_dir + 'cand_lda_dictionary',mmap='r')

    filelist=glob.glob(configuration.text_dir + 'CandidateMessaging/%s*tokenized.txt'%(candidate))
    full_doc=[]
    for filename in filelist:
        if os.stat(filename).st_size > 0:
            with open(filename,'r') as txtfile:
                doc=txtfile.read().split(' ')

            full_doc.extend(doc)

    messaging=get_doc_lda(full_doc, dictionary, model)
    return messaging