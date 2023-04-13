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


docs = []
docs.append('To do is to be. To be is to do.')
docs.append('To be or not to be. I am what I am')
docs.append('I think therefore I am. Do be do be do.')
docs.append('Do do do da da da. Let it be let it be.')

doc_tokens, vocab, word_to_id, id_to_word = buildDict(docs)

from collections import Counter
import math

tf_vectors = []
for doc in doc_tokens:
  vec = [0.0 for _ in range((len(word_to_id)))]  #사전 길이 리스트
  word_count = Counter(doc)  #단어별 문서 내 출현빈도
  for key, value in word_count.items():
    vec[word_to_id[key]] = 1 + math.log2(value)  #tf계산
  tf_vectors.append(vec)

import pandas as pd

df = pd.DataFrame(tf_vectors, columns=id_to_word.values())
#print(df)
#각 문서에서의 단어별 출현 빈도를 나타내는 문서-단어 행렬이 출력

idf = {}
for id, _ in id_to_word.items():
  idf[id] = 0.0
  for doc in tf_vectors:
    if doc[id] > 0:
      idf[id] += 1

N = len(tf_vectors)
idf = {id: math.log2(N / val) for id, val in idf.items()}

df = pd.Series(idf.values(), index=idf.keys())
#print(df)
#출력 결과는 단어들의 idf 값

import numpy as np

idf_list = [val for _, val in idf.items()]
#각 단어의 IDF 값으로 이루어진 리스트를 생성
tfidf = np.array([np.multiply(tf, idf_list) for tf in tf_vectors])
# multiply로 배열 간의 요소별 곱셈을 수행

df = pd.DataFrame(tfidf, columns=id_to_word.values())
df  #TF-IDF 가중치를 계산한 결과

print(df.T)
