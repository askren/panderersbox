
from gensim import corpora
import glob
import gensim
import pyLDAvis.gensim
import pyLDAvis
import logging
from panderer.build_database_model import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import configuration
import stopwords

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

engine=create_engine(configuration.get_engine_string())

db_session = scoped_session(sessionmaker(bind=engine))


def get_vis(model,corpus,dictionary):
    vis=pyLDAvis.gensim.prepare(model,corpus,dictionary)
    pyLDAvis.display(vis)
    pyLDAvis.save_html(vis,configuration.lda_dir + 'lda_visualization_test.html')

def lda(candidate_docs):
    logger.info("Turning documents into dictionary and corpus")
    cand_dictionary=corpora.Dictionary(candidate_docs)
    cand_dictionary.filter_extremes(no_below=5, no_above=0.70, keep_n=100000)
    cand_corpus = [cand_dictionary.doc2bow(cand_text) for cand_text in candidate_docs]
    num_topics=45
    logger.info("Running the LDA model")
    cand_model = gensim.models.ldamodel.LdaModel(cand_corpus, alpha=0.0075, num_topics=num_topics, id2word = cand_dictionary, passes=50)
    cand_model.save(configuration.lda_dir + 'cand_lda_model_test')
    cand_dictionary.save(configuration.lda_dir + 'cand_lda_dictionary_test')
    corpora.MmCorpus.serialize(configuration.lda_dir + 'cand_corpus_test.mm', cand_corpus)
    cand_model.show_topics(num_topics=-1, num_words=30, log=True, formatted=True)
    logger.info("Getting the visualization")
    get_vis(cand_model,cand_corpus,cand_dictionary)


def main():
    candidate_docs=[]
    logger.info("Processing input files")

    for user in db_session.query(User):
        doc=user.user_content
        if doc:
            new_doc=doc[1:-1].split(',')
            candidate_docs.append(new_doc)
    lda(candidate_docs)

if __name__ == "__main__":
    main()

