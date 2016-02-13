import glob
from panderer import tweet_parser
import logging
import os
from panderer import stopwords

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

def parse_text(text):
    text_tokens=[]
    for sentence in text:
        if sentence:
            if not sentence.isspace():
                sentence_content, hashtag_content = tweet_parser.lem_tweet_tokens(sentence)
                if sentence_content:
                    modified_content=[]
                    for token in sentence_content:
                        if token not in stopwords.stopset:
                            modified_content.append(token)
                    text_tokens.extend(modified_content)
    return(text_tokens)


def main():
    for filename in glob.glob('/var/local/InsightData/CandidateMessaging/*.txt'):
        logger.info("Working on filename:%s",filename)
        with open(filename,'r') as speechfile:
            text=speechfile.read().replace('\n','').split('.')
            text_tokens=parse_text(text)
        origname=os.path.splitext(filename)[0]
        with open((origname+'_tokenized.txt'),'w') as f:
            f.write(' '.join(text_tokens))

if __name__ == "__main__":
    main()