from nltk import FreqDist
import numpy as np
import re


def buildDict(docs):
  doc_tokens = []  # python list
  for doc in docs:
    delim = re.compile(r'[\s,.]+')
    tokens = delim.split(doc.lower())
    if tokens[-1] == '': tokens = tokens[:-1]
    doc_tokens.append(tokens)

  vocab = FreqDist(np.hstack(doc_tokens))
  vocab = vocab.most_common()
  word_to_id = {word[0]: id for id, word in enumerate(vocab)}
  id_to_word = {id: word[0] for id, word in enumerate(vocab)}
  return doc_tokens, vocab, word_to_id, id_to_word


from collections import Counter
import math
import numpy as np


def TFIDF(doc_tokens, id_to_word):
  tf_vectors = []
  idf = {}

  #TF 구하기
  for doc in doc_tokens:
    vec = [0.0 for _ in range((len(id_to_word)))]
    word_count = Counter(doc)
    for key, value in word_count.items():
      vec[word_to_id[key]] = value
      #vec[word_to_id[key]] = 1+ math.log2(value) #tf계산
    tf_vectors.append(vec)

  #IDF 구하기
  for id, _ in id_to_word.items():
    idf[id] = 0.0
    for doc in tf_vectors:
      if doc[id] > 0:
        idf[id] += 1
  N = len(tf_vectors)
  idf = {id: np.log((N + 1) / (val + 1)) + 1 for id, val in idf.items()}

  #TF-IDF 구하기
  idf_list = [val for _, val in idf.items()]
  tfidf = np.array([np.multiply(tf, idf_list) for tf in tf_vectors])

  return tf_vectors, idf, tfidf


docs = []
docs.append('Python is a high-level, general-purpose programming language.')
docs.append(
  'Its design philosophy emphasizes code readability with the use of significant indentation.'
)
docs.append(
  'Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small- and large-scale projects.'
)
docs.append('Python is dynamically-typed and garbage-collected.')
docs.append(
  'It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.'
)
docs.append(
  'It is often described as a "batteries included" language due to its comprehensive standard library.'
)
docs.append(
  'Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.'
)
docs.append(
  'Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.'
)
docs.append(
  'Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions.'
)
docs.append('Python 2 was discontinued with version 2.7.18 in 2020.')
docs.append(
  'Python consistently ranks as one of the most popular programming languages.'
)

doc_tokens, vocab, word_to_id, id_to_word = buildDict(docs)
tf_vectors, idf, tfidf = TFIDF(doc_tokens, id_to_word)
"""TFIDF Vector 정규화"""

import pandas as pd

pd.DataFrame(tfidf, columns=word_to_id.keys())

tfidf_l1 = np.array([vec / np.sum(vec) for vec in tfidf])
#l1 norm
pd.DataFrame(tfidf_l1, columns=word_to_id.keys())

tfidf_l2 = np.array([vec / (np.sum(vec**2)**0.5) for vec in tfidf])  #l2 norm
pd.DataFrame(tfidf_l2, columns=word_to_id.keys())

from numpy.linalg import norm

tfidf_l2 = np.array([np.divide(vec, norm(vec)) for vec in tfidf])  #l2 norm
pd.DataFrame(tfidf_l2, columns=word_to_id.keys())
"""코사인 유사도 계산 - 2. 문서 간 유사도 계산"""

cos_sim = np.array([np.dot(tfidf_l2, vector) for vector in tfidf_l2])
cos_sim
print(cos_sim)
# 행렬의 각 원소는 해당하는 두 문서 간의 유사도를 나타냅니다. 예를 들어, (1,2) 위치의 값은 첫 번째 문서와 두 번째 문서 간의 유사도를 나타냅니다.

#이 1로 표시된 것은 각 문서 자체와의 유사도입니다. 예를 들어, 첫 번째 문서와 첫 번째 문서는 완전히 동일하므로 자기 자신과의 유사도는 1입니다. 따라서 대각선 상에 위치한 값들이 모두 1
for i in range(len(docs)):
  for j in range(i + 1, len(docs)):
    cos_sim_val = cos_sim[i][j]
    print(f"{i+1}번째 문서와 {j+1}번째 문서의 유사도: {cos_sim_val:.4f}")
