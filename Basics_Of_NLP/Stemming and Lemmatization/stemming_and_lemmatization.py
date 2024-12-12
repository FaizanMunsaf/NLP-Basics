'''
Playing 
Play
Played
=> Play
'''
import spacy
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

words = ['run','runner','running','ran','runs','easily','fairly']

# Stemmers

p_stemmer = PorterStemmer()
s_stemmer = SnowballStemmer(language="english")

for word in words:
    print("Actual Word : " + word + " : PostStemmer : " + p_stemmer.stem(word) + " : SnowBall Stemmer : " + s_stemmer.stem(word) )


# Lemmatization 
nlp = spacy.load("en_core_web_md")

doc1 = nlp("The striped bats are hanging on their feet for best")

for token in doc1:
    print(token.text, "\t", token.lemma_, "\t" ,token.lemma)

# Testing Stemming on same string why Lemmatization is good because Lemma always choose from dictionary words
s1 = "The striped bats are hanging on their feet for best"
for word in s1.split():
    print(word + " postemmer :  " + p_stemmer.stem(word))
