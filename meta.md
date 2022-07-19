# Meta

# Build Log

## 2022-07-17
- Told Alli about this. Located the Google [Colab notebook](https://colab.research.google.com/drive/1z6rotg6Z7KTpjJtkp5tHTsIq06oNMDhi?usp=sharing) where I had been writing doing the analysis previously (because my python environment was a superfund site).
- [x] Parse out the index into a CSV
- [x] Perform NER on the Titles
- [x] Perform a Named Entity Recognition (NER) to get the names of
  - [ ] Episodes
  - [ ] Speakers
  - [ ] Papers Referenced

- In order to perform the NER, I need to install spacy. Previously my venv was python 3.7.0, but theres an error so I have to update. Going to try 3.9. So I use `python3.9 -m venv nlp-env-9` and `source nlp-env-9/bin/activate` to enter it. My VSCode workspace recognizes the config change and sets that as a the new default python for the workspace. 
  - New python is 3.9.13
  - Follow the official spacy install instructions: https://spacy.io/usage
    - pip install -U pip setuptools wheel
    - pip install -U spacy
    - python -m spacy download en_core_web_sm en_code_web_lg
    - pip install pandas gensim pyldavis

- Following [this tutorial](https://analyticsindiamag.com/hands-on-guide-to-building-knowledge-graph-for-named-entity-recognition/) to create a Knowledge Graph from the Named Entities
  - Now I'm also following [this tutorial](https://analyticsindiamag.com/complete-guide-to-implement-knowledge-graph-using-python/) and using the code therein
  - [x] Start with Titles Only
  - [x] Perform NER on all transcripts
    - How should I clean the entities and link them so "Stefani Crabtree" and "Stefani" are the same entity?
      - This task is called NED, Named Entity Disambiguation, and an article on Towards Data Science uses [DGL-KE](https://github.com/awslabs/dgl-ke), trained on Wikipedia, to perform the disambiguation. [.](\w) -> . $1 && [?](\w) -> ,? $1 in files into clude data/*.md
## 2022-06-28
- Told Kene about this, and it made me want to re-examine the work I did here, what I learned and consider next steps.

- Next steps:
  - Obviously, it would be good to clean the files
    - Newline by speaker. Segment into a call-and-response format
  - Add named entities. Entities:
    - Other episodes of this podcast
    - Names, Places, proper nouns
    - Concepts

## 2021-12-13
- Generated and downloaded all the wordclouds from a colab notebook, which I have yet to add to this

- Next up: 
  - TODO: split into messages on speaker / timecode
  - TODO: Parse out the SHOWNOTES / LINKS section
  - TODO: LDA topic analysis
## 2021-12-12
- Finally got the scraper working and downloaded the 'corpora' I'll be working with:
  - class="sc-episode-details-title"
  - class="sc-episode-details-time"
  - class="sc-episode-details-body"
- Had to use a selenium automation after all, since it is a javascript web-app. There's probably some way to trigger the javascript programmatically, but I don't know much about JavaScript, so I did it with selenium. `scraper.py` 
- Public Colab Notebook Link: https://colab.research.google.com/drive/1z6rotg6Z7KTpjJtkp5tHTsIq06oNMDhi?usp=sharing