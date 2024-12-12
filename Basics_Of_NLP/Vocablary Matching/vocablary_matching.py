"""
There's two kind of matching in spacy
1. Rule based matching
    - How we can define the rule based matching to create best pattern
    - I want to search something  e.g. which is Digit or not based
    Is_DIGIT or not for example in whole text it will pick the digits and return to us but if 234was like together he will count this string
    - Take another example like Entity type for example any comapny name like Google we most probably use ENT_TYPE
    ENT_TYPE and ORG is GOOGLE or not or any other company name it will return to us.
    - LEMMA - be so it will found grammatically be possible such as is, are, be e.t.c.
    - IS_STOP find to stop word or not
    - LOWER - searching for small wooden in whole paragraph even it's capital letter if it's together it will find and return to us. 
2. Phras based matching
"""

# Rule Based Matching
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

'''
spacy.vocab to access a central lookup table that stores information about all the words (tokens) encountered during text processing
'''
print("=============================================")
print("NLP VOCAB : ", nlp.vocab)
print("=============================================")

matcher = Matcher(nlp.vocab)

print("=============================================")
print("Matcher : ", matcher)
print("=============================================")

# create a list, and inside that list add series of dictionary

# Hello World can appear in the following ways, 
# 1) Hello World | hello world | Hello WORLD
# 2) Hello-World 

pattern_1 = [
    {"LOWER": "hello"},
    {"LOWER": "world"}
    ]

pattern_2 = [
    {"LOWER": "hello"},
    {"IS_PUNCT": True},
    {"LOWER": "world"}
    ]

'''
LOWER, IS_PUNCT are the attributes 
They has to be written in that way only
'''

'''
============================================================
Add Patterns to matcher object
============================================================

Add a match rule to matcher, A match rule consists of,
1) An ID key
2) one or more patterns list
3) an on_match callback
'''
matcher.add("Hello World", patterns=[pattern_1,pattern_2])

doc = nlp(" 'Hello World' are the first two print printed words for most of the programmers, printing 'Hello-World'  is the most common for the beginners")
print("Doc : ", doc)

find_matches = matcher(doc)

'''
It returns output list of tuples
string ID, index start and index end
'''
print("Finding the match from the Doc : ", find_matches)

for match_id, start, end in find_matches:
    string_id = nlp.vocab.strings[match_id] #  get string representation
    span = doc[start:end] # get the match spanned
    print(match_id, string_id, start, end, span.text)


'''
How to remove the matches
'''
# matcher.remove("Hello World")

'''
Redefine the patterns: 
'OP:*' -> is going to allow this pattern to match zero or more times for any punctuation
'''
pattern_3 = [
    {"LOWER": "hello"},
    {"LOWER": "world"}
    ]

pattern_4 = [
    {"LOWER": "hello"},
    {"IS_PUNCT": True, "OP":"*"},
    {"LOWER": "world"}
    ]

matcher.add("Hello World", patterns=[pattern_3, pattern_4])

doc_2 = nlp("You can print Hello World or hello world or Hello-World")
find_matches = matcher(doc_2)
print("Doc2 : ", find_matches)



# Phrase Based Matching please before run this to comment upper code rule based only
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

phrase_list = ["Barack Obama", "Angela Merkel", "Washington, D.C."]

# conver each phrase to a document
phrase_patterns = [nlp(text) for text in phrase_list] # I am using list comprehension here

print("Phrase Patterns : ----- : ", phrase_patterns, "Type : ", type(phrase_patterns[0]))
matcher.add("TerminologyList", phrase_patterns)

doc_3 = nlp("German Chancellor Angela Merkel and US President Barack Obama " 
            "converse in the Oval Office inside the White House in Washington, D.C.")

find_matches = matcher(doc_3)
print("Doc3 : ", find_matches)

for match_id, start, end in find_matches:
    string_id = nlp.vocab.strings[match_id] #  get string representation
    span = doc[start:end] # get the match spanned
    print(match_id, string_id, start, end, span.text)

