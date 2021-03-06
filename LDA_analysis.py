# -*- coding: utf-8 -*-
"""Complexity Podcast LDA Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z6rotg6Z7KTpjJtkp5tHTsIq06oNMDhi

# Topic models with Gensim

Gensim is a popular library for topic modeling. Here we'll see how it stacks up to scikit-learn.

<p class="reading-options">
  <a class="btn" href="/text-analysis/topic-models-with-gensim">
    <i class="fa fa-sm fa-book"></i>
    Read online
  </a>
  <a class="btn" href="/text-analysis/notebooks/Topic models with Gensim.ipynb">
    <i class="fa fa-sm fa-download"></i>
    Download notebook
  </a>
  <a class="btn" href="https://colab.research.google.com/github/littlecolumns/ds4j-notebooks/blob/master/text-analysis/notebooks/Topic models with Gensim.ipynb" target="_new">
    <i class="fa fa-sm fa-laptop"></i>
    Interactive version
  </a>
</p>

### Prep work: Downloading necessary files
Before we get started, we need to download all of the data we'll be using.
* **recipes.csv:** recipes - a list of recipes (but only with ingredient names)
* **state-of-the-union.csv:** State of the Union addresses - each presidential address from 1970 to 2012
"""

# Make data directory if it doesn't exist
!mkdir -p data
!wget -nc https://raw.githubusercontent.com/patchworquill/sfi_complexity/master/merged.csv

import pandas as pd

df = pd.read_csv("merged.csv",sep="\t", names=["episodes", "content"], error_bad_lines=False, engine="python") # Skip the offending lines

df.head()

# from wordcloud import WordCloud

# total_string=""

# for i in range(0,69):
#   total_string += df.iat[i,1]

# wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
#   # Generate a word cloud
# wordcloud.generate(total_string)
# # Visualize the word cloud
# im = wordcloud.to_image()

# fp = "main-wordcloud.png"
# im.save(fp, format="png")

# total_string += df.iat[i,1]
#   # Create a WordCloud object

# wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
# # Generate a word cloud
# wordcloud.generate(long_string)
# # Visualize the word cloud
# im = wordcloud.to_image()

# fp = str(i)+"-wordcloud.png"
# im.save(fp, format="png")

# !zip -r /content/file.zip /content/wordcloud

"""## Using Gensim"""

#!pip install --upgrade gensim

from gensim.utils import simple_preprocess

texts = df.content.apply(simple_preprocess)

from gensim import corpora

dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=5, no_above=0.5)

corpus = [dictionary.doc2bow(text) for text in texts]

from gensim import models

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

n_topics = 70

# Build an LSI model
lsi_model = models.LsiModel(corpus_tfidf,
                            id2word=dictionary,
                            num_topics=n_topics)

lsi_model.print_topics()

"""Gensim is all about how important each word is to the category. Why not visualize it? First we'll make a dataframe that shows each topic, its top five words, and its values."""

n_words = 10

topic_words = pd.DataFrame({})

for i, topic in enumerate(lsi_model.get_topics()):
    top_feature_ids = topic.argsort()[-n_words:][::-1]
    feature_values = topic[top_feature_ids]
    words = [dictionary[id] for id in top_feature_ids]
    topic_df = pd.DataFrame({'value': feature_values, 'word': words, 'topic': i})
    topic_words = pd.concat([topic_words, topic_df], ignore_index=True)

topic_words.head()

"""Then we'll use seaborn to visualize it."""

import seaborn as sns
import matplotlib.pyplot as plt

g = sns.FacetGrid(topic_words, col="topic", col_wrap=3, sharey=False)
g.map(plt.barh, "word", "value")

"""## Using LDA with Gensim

Now we'll use LDA.
"""

from gensim.utils import simple_preprocess

texts = df.content.apply(simple_preprocess)

from gensim import corpora

dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=2000)
corpus = [dictionary.doc2bow(text) for text in texts]

from gensim import models

n_topics = 70

lda_model = models.LdaModel(corpus=corpus, num_topics=n_topics)

lda_model.print_topics()

!pip install pyLDAvis
!pip install --upgrade pandas==1.2

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

print(pyLDAvis.__version__)

pyLDAvis.enable_notebook()
lda_viz = gensimvis.prepare(lda_model, corpus, dictionary)
lda_viz

import pickle
pickle.dump( lda_viz, open( "lda_vis.p", "wb" ))

