import spacy
from spacy.language import Language

nlp = spacy.load("en_core_web_sm")

s1 = "This is a sentence. This is second sentence. This is last sentence."
s2 = "This is a sentence; This is second sentence; This is last sentence."
s3 = "This is a sentence. This is second U.K. sentence. This is last sentence."


doc1 = nlp(s1)
print(" --- Here we go with doc1 sentences now --- ")

for sent in doc1.sents:
    print(sent.text)

doc3 = nlp(s3)
print(" --- Here we go with doc3 sentences now --- ")

for sent in doc3.sents:
    print(sent)


'''
Let's take a s2 because there's 3 sentences with compound statement so how can we handle this now we have to look into this
'''
doc2 = nlp(s2)
print(" --- Here we go with doc2 sentences now --- ")

'''
It's not segment it according to the ; semicolon so here we can see
'''
for sent in doc2.sents:
    print(sent)
'''
Now write down the custom boundaries that split the sentence according to ;
'''

@Language.component("custom_boundaries")  # Registering the function
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ";":
            # print(token.i)
            doc[token.i + 1].is_sent_start = True
    return doc

print("Call the custom function and check how it works")

print(nlp.pipe_names)  # Check pipeline before adding e.g. ['tok2vec', 'tagger', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']

# Add the component using its registered name
nlp.add_pipe("custom_boundaries", before="parser")  

print(nlp.pipe_names)  # Check pipeline after adding

print("-- let's test after adding new pipeline --")
doc_2 = nlp(s2)
for sent in doc_2.sents:
    print(sent)
