from nltk import FreqDist
import re
import numpy as np
import pandas as pd  # Shell에서 pip install pandas 하기


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

doc_vectors = []  #4개 문서의 벡터
for tokens in doc_tokens:
  doc_vector = []
  for token in tokens:
    one_hot_vector = [0 for _ in word_to_id]
    one_hot_vector[word_to_id[token]] = 1
    doc_vector.append(one_hot_vector)
  doc_vectors.append(doc_vector)

for doc, doc_vector in zip(docs, doc_vectors):
  #문서 별 벡터(행렬) 정보 출력
  df = pd.DataFrame(doc_vector, columns=id_to_word.values())
  print(doc)
  print(df)

for doc, doc_vector in zip(docs, doc_vectors):
  #문서 별 벡터(행렬) 정보 출력
  df = pd.DataFrame(doc_vector, columns=id_to_word.values())
  print(doc)
  print(df)
  # one-hot vector에서 원문 추출
  words = [id_to_word[np.argmax(one_hot)] for one_hot in doc_vector]
  text = " ".join(words)
  print("원문: ", text)
