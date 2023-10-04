from flask import make_response
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import thai_stopwords
from pythainlp.summarize.keybert import KeyBERT
import thaispellcheck

def cleansing(data): 
    text = data['text']
    correct_words = thaispellcheck.check(text, autocorrect=True)
    words = word_tokenize(correct_words, engine="newmm", keep_whitespace=False)
    stopwords = list(thai_stopwords())
    list_word_not_stopwords = [i for i in words if i not in stopwords]
    return make_response({'tokens': list_word_not_stopwords, 'result' : 'succes'}, 200)   

def find_keywords(data): 
    text = data['text']
    kb = KeyBERT()
    keywords = kb.extract_keywords(text)
    return make_response({'tokens': keywords, 'result' : 'succes'}, 200)   

