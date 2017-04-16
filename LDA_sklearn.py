import nltk
from time import time
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
# import lda
# import lda.datasets


print("Loading dataset...")
t0 = time()
dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                             remove=('headers', 'footers', 'quotes'))
data_samples = dataset.data[:100]
print("done in %0.3fs." % (time() - t0))
#nltk.word_tokenize(sentence)
#word_list = twitter_samples.tokenized('tweets.20150430-223406.json')
word_list = twitter_samples.strings('tweets.20150430-223406.json')

# filtered_word_list = word_list[:] #make a copy of the word_list
# # iterate over word_list
# for word in word_list:
#     if word in stopwords.words('english'): 
#         filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword

#filtered_word_list.save

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()

vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
X = vectorizer.fit_transform(word_list)
model_ = LatentDirichletAllocation(n_topics=15, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
# model = lda.LDA(n_topics=20, n_iter=500, random_state=1)
# model.fit(X)
model_.fit(X)
# topic_word = model.topic_word_
# print("type(topic_word): {}".format(type(topic_word)))
# print("shape: {}".format(topic_word.shape))

# print("\nTopics in LDA model:")
# feature_names = vectorizer.get_feature_names()
# print_top_words(model, feature_names, 7)

# doc_topic = model.doc_topic_
# print("type(doc_topic): {}".format(type(doc_topic)))
# print("shape: {}".format(doc_topic.shape))

# for n in range(10):
#     topic_most_pr = doc_topic[n].argmax()
#     print("doc: {} topic: {}".format(n, topic_most_pr))
print("done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
tf_feature_names = vectorizer.get_feature_names()
print_top_words(model_, tf_feature_names, 7)

print 1