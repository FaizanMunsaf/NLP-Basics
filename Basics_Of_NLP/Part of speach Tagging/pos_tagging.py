import spacy
import spacy.attrs

nlp = spacy.load("en_core_web_md")

s1 = "Apple is looking at buying U.K. startup for $1 billion"

doc = nlp(s1)

for token in doc:
    print(token.text, " POS -> " + token.pos_, " TAG -> " + token.tag_, " Explain -> " + spacy.explain(token.tag_)) # type: ignore

print("find the document before checking the occurance : ", doc.count_by(spacy.attrs.POS))

for key, val in doc.count_by(spacy.attrs.POS).items():
    print(key, doc.vocab[key].text, val)

from spacy import displacy
from pathlib import Path

svg = displacy.render(docs=doc, style="dep")

output_path = Path("./dependency_plot.svg") # you can keep there only "dependency_plot.svg" if you want to save it in the same folder where you run the script 
output_path.open("w", encoding="utf-8").write(svg)

