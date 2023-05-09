import re


def validate_jumin(jumin):
  pattern = r'\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])-[1-4]\d{6}'
  if re.match(pattern, jumin):
    print(f"{jumin} 주민등록번호는 형식에 맞지 않는 주민등록번호입니다.")
  else:
    print(f"{jumin} 주민등록번호는 형식에 맞지 않습니다.")


# 주민등록번호 유효성 검사
validate_jumin("830422-1234567")
validate_jumin("900101-9234567")
'''
주민등록번호 정규표현식 검출하는 코드
'''
