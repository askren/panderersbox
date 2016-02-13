from nltk.stem import WordNetLemmatizer

import configuration
from panderer import stopwords
import os


_wnl = WordNetLemmatizer()
_tagger=None

def get_tagger():
    global _tagger
    if _tagger is None:

        import jnius_config
        import os

        os.environ['JAVA_HOME'] = configuration.java_home
        jnius_config.add_options('-Xrs', '-Xmx128M')

        jnius_config.set_classpath(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/ark-tweet-nlp-0.3.2/ark-tweet-nlp-0.3.2.jar')))

        from jnius import autoclass


        _Tagger = autoclass('cmu.arktweetnlp.Tagger')
        _tagger=_Tagger()
        _tagger.loadModel('/cmu/arktweetnlp/model.20120919')

    return _tagger

def _remove_tag(arg):
    if arg[0]=='#':
        arg=arg[1:]
        is_hash=True
    else:
        is_hash=False
    return (arg,is_hash)

def _posessive(arg):
    return (arg).rsplit("'",1)[0]

def _proper(arg):
    return (arg).title()

def _verb(arg):
    return (arg.lower(), 'v')

def _noun(arg):
    return (arg.lower(), 'n')

def _prop_noun(arg):
    return (_proper(arg), 'n')

def _prop_pos_noun(arg):
    return (_proper(_posessive(arg)), 'n')

def _pos_noun(arg):
    return (_posessive(arg), 'n')

def _adverb(arg):
    return (arg.lower(), 'r')

def _adjective(arg):
    return (arg.lower(), 'j')


def lem_tweet_tokens(text):

    kept_tags={'V':_verb,'N':_noun,'^':_prop_noun,'S':_pos_noun,'Z':_prop_pos_noun, 'J':_adjective, 'R':_adverb}

    taggedTokens = get_tagger().tokenizeAndTag(text)

    lem_tokens=[]
    lem_hashtags=[]

    for i in range(taggedTokens.size()):
        token=taggedTokens.get(i)
        if token.tag in kept_tags:
            cleaned_token=token.token.decode('ascii','ignore')
            if cleaned_token:
                untagged_token,is_hash=_remove_tag(cleaned_token)
                lem_token=_wnl.lemmatize(*kept_tags[token.tag](untagged_token))

                if lem_token.lower() not in stopwords.stopset:
                    lem_tokens.append(lem_token.lower())

                if is_hash:
                    lem_hashtags.append(lem_token.lower())

    return (lem_tokens,lem_hashtags)
