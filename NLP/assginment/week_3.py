import nltk
# Shell에서 pip install nltk 하기
from nltk.tokenize import TreebankWordTokenizer
#Natural Language Toolkit 패키지
nltk.download('punkt')
#NLTK 패키지에서 제공하는 구두점 데이터를 다운로드합니다. 이 데이터는 토큰화 시 구두점을 제대로 인식하기 위해 필요
docs = []
docs.append("I am going to go to the store.")
docs.append("The Science of today is the technology of tommorow.")
docs.append("You are using pip version 3.")
docs.append("Could not install packages due to an Error.")
#리스트 docs에  문자열을 추가

tokenizer = TreebankWordTokenizer()
tokenized_docs = []

# 각 문장을 토큰화하여 tokenized_docs 리스트에 추가
for doc in docs:
  tokenized_doc = tokenizer.tokenize(doc)
  tokenized_docs.append(tokenized_doc)

# tokenized_docs 리스트 출력

for doc in tokenized_docs:
  print(doc)
  print('\n')

# 실행 결과를 한 줄씩 출력하기 위해 개행문자('\n')를 이용합니다.