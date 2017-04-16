from itertools import chain

import gensim
from corpora import corpus

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word = dictionary, passes=passes, minimum_probability=0)

# Assinging the topics to the document in corpus
lda_corpus = ldamodel[corpus]

# Find the threshold, let's set the threshold to be 1/#clusters,
# To prove that the threshold is sane, we average the sum of all probabilities:
scores = list(chain(*[[score for topic_id,score in topic] \
                     for topic in [doc for doc in lda_corpus]]))

threshold = sum(scores)/len(scores)
print(threshold)

for t in range(len(topic_tuple)):
    key_words.append([topic_tuple[t][j][0] for j in range(num_words)])
    df_key_words = pd.DataFrame({'key_words' : key_words})

    documents_corpus.append([j for i,j in zip(lda_corpus,doc_set) if i[t][1] > threshold])
    df_documents_corpus = pd.DataFrame({'documents_corpus' : documents_corpus})

    documents_corpus_id.append([i for d,i in zip(lda_corpus, doc_set_id) if d[t][1] > threshold])
    df_documents_corpus_id = pd.DataFrame({'documents_corpus_id' : documents_corpus_id})


result.append(pd.concat([df_key_words, df_documents_corpus, df_documents_corpus_id ], axis=1))