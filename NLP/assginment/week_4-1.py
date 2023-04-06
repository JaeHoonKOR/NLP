from nltk import FreqDist
import re
import numpy as np
import pandas as pd


# buildDict 함수 구현
def buildDict(docs):
  doc_tokens = []
  for doc in docs:
    delim = re.compile(r'[\s,.]+')
    tokens = delim.split(doc.lower())
    if tokens[-1] == '':
      tokens = tokens[:-1]
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

# doc_vectors 생성
doc_vectors = []
for tokens in doc_tokens:
  doc_vector = [0 for _ in word_to_id]
  for token in tokens:
    if token in word_to_id:
      doc_vector[word_to_id[token]] = 1
  doc_vectors.append(doc_vector)

# doc_vectors를 numpy array로 변환하여 전치행렬 구하기
doc_array = np.array(doc_vectors)
doc_T = doc_array.T

# 검색어 입력받기
keyword = input("검색어를 입력하세요: ").lower()

# 검색어가 등장한 문서 검색
doc_idx_list = np.where(doc_T[word_to_id[keyword]] == 1)[0]
if len(doc_idx_list) == 0:
  print("해당 검색어가 포함된 문서가 없습니다.")
else:
  for doc_idx in doc_idx_list:
    doc = docs[doc_idx]
    print(f"[{doc_idx+1}번 문서] {doc}")
