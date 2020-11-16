# establishing environment
import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd


def basic_clean(s):
    """
    Accepts string and returns with only lowercase, normalized unicode characters. 
    Removes anything that is not a letter, number, whitespace or a single quote.
    """
    # convert string to lower case
    s = s.lower()
    # normalize text
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # remove anything that is not a character specified in docstring
    s = re.sub(r"[^a-z0-9'\s]", '', s)
    # returning string
    return s

def tokenize(s):
    """
    Accepts a string and returns it tokenized.
    Breaks down words and any punctuation left over into discrete units.
    """
    # save tokenizer to variable
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # use tokenize on string and return
    return tokenizer.tokenize(s, return_str=True)

def stem(s):
    """
    Accepts string. Returns string after stemming it.
    """
    # saving stemmer to variable
    ps = nltk.porter.PorterStemmer()
    # applying stemmer to each word in string
    stems = [ps.stem(word) for word in s.split()]
    # joining words together
    article_stemmed = ' '.join(stems)
    # returning string
    return article_stemmed

def lemmatize(s):
    """
    Accepts string. Returns string after lemmatizing it.
    """
    # saving lemmatizer to variable
    wnl = nltk.stem.WordNetLemmatizer()
    # applying lemmatizer to each word in string
    lemmas = [wnl.lemmatize(word) for word in s.split()]
    # rejoining words
    article_lemmatized = ' '.join(lemmas)
    # returning string
    return article_lemmatized

def remove_stopwords(s):
    """
    Accepts string and return with stopwords removed.
    """
    # importing list of stopwords
    stopword_list = stopwords.words('english')
    # removing no and not from stopword list
    stopword_list.remove('no')
    stopword_list.remove('not')
    # splitting provided string
    words = s.split()
    # filtering out stop words
    filtered_words = [w for w in words if w not in stopword_list]
    # joining strings that are not stopwords
    article_without_stopwords = ' '.join(filtered_words)
    # returning string
    return article_without_stopwords