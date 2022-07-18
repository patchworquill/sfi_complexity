import string
import nltk
import matplotlib.pyplot as plt
import networkx as nx
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_lg")

# Test example from https://medium.com/analytics-vidhya/named-entity-recognition-with-spacy-2ecfa4114162
doc = nlp("Manchester United Football Club is a professional football club based in Manchester, England established in 1978")

for ent in doc.ents:
    print(ent.text, ent.label_)

index = "index.csv"
df = pd.read_csv(index, header=0)


###############################################

#               INDEXES NER

###############################################
# Test example with Index Titles
entities = []
entity_types = []

for title in df["Title"].tolist():
    doc = nlp(title)
    ents = []
    for ent in doc.ents:
        print(ent.text, ent.label_)
        ents.append(ent.label_)

    entities.append(doc.ents)
    entity_types.append(ents)

df["Entities"] = entities
df["Entity_Types"] = entity_types

df.to_csv("index_entities.csv", index=None)


###############################################

#               TRANSCRIPTS NER

###############################################

# Run NER on the Markdown Podcast Transcripts
transcripts = os.listdir("data")
transcripts = [
    transcript for transcript in transcripts if transcript.__contains__(".md")]

entities = []
entity_types = []
ent_t_ignore = ["CARDINAL", "ORDINAL"]

for md in transcripts:
    fulltext = ""
    with open("data/"+md, "r") as file:
        for line in file:
            fulltext += line

    doc = nlp(fulltext)
    ents = []
    ents_t = []

    for ent in doc.ents:
        print(ent.text, ent.label_)
        if ent.label_ not in ent_t_ignore:
            ents.append(ent.text)
            ents_t.append(ent.label_)

    entities.append(ents)
    entity_types.append(ents_t)

    print(len(entities[0]))
    print(len(entity_types[0]))
    zipped = list(zip(entity_types[0], entities[0]))
    df2 = pd.DataFrame(zipped, columns = ["Type", "Entity"])
    df2.to_csv("data/"+md.replace(".md", "")+"_ENTITIES.csv", index=None)

spacy.displacy.serve(doc, style='ent')
spacy.displacy.serve(doc, style='dep')

