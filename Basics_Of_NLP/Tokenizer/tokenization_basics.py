import spacy

s1 = 'Apple is looking at buying U.K. startup for $1 billion !'
s2 = 'Hello all, We are here to help you! email support@udemy.com or visit us at http://www.udemy.com!'
s3 = '10km cab ride almost costs $20 in NYC'
s4 = "Let's watch a movie together."

nlp = spacy.load(name = 'en_core_web_sm')

# python -m spacy  en_core_web_md # for download the model in spacy
# nlp_1 = spacy.load(name = 'en_core_web_md')

doc1 = nlp(s1)
for token in doc1:
    print("docs 1 ------- ", token)

doc2 = nlp(s2)
for token in doc2:
    print(token)

doc2 = nlp(s2)
for token in doc2:
    print("docs 2 ------- ", token)

doc3= nlp(s3)
for token in doc3:
    print("docs 3 ------- ", token)

doc4= nlp(s4)
for token in doc4:
    print("docs 4 ------- ", token)

# type of spacy tokens
print("type of tokens ---- : ", type(doc4)) #  <class 'spacy.tokens.doc.Doc'>

# Length of string in spacy similar like basics
print("spacy basics strings ----- : ", len(doc4))

# slicing in spacy similar like array even negative token but i can't update the any specific spacy doc
print("Slicing in spacy ----- : ", doc4[2:5])