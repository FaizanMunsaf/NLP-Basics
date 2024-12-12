'''
a an the always (this is meaning less in analytics we need to remove this) 
'''

import spacy
nlp = spacy.load("en_core_web_md")

print("========= Spacy default stop words ==========")
print(nlp.Defaults.stop_words)
print("=============================================")

print("By default spacy stop words length is : ", len(nlp.Defaults.stop_words))

print("Check always is a stop word or not : ", nlp.vocab["always"].is_stop)

print("Check finance is a stop word or not : ", nlp.vocab["finance"].is_stop)

print("Check asdf is a stop word or not : ", nlp.vocab["asdf"].is_stop)

nlp.Defaults.stop_words.add("asdf")
nlp.vocab["asdf"].is_stop = True
print("After add a new stop words and Check asdf is a stop word or not : ", nlp.vocab["asdf"].is_stop)

print("After add a new stop words and By default spacy stop words length is : ", len(nlp.Defaults.stop_words))

print("Check the no is stop word or not : ", nlp.vocab["no"].is_stop)
nlp.vocab["no"].is_stop = False
print("========= Spacy default stop words but there's not no any more ==========")
nlp.Defaults.stop_words.remove("no")
print(nlp.Defaults.stop_words, len(nlp.Defaults.stop_words))
print("=========================================================================")
