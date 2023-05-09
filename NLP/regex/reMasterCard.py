import re

pattern = r'^5[1-5][0-9]{14}$'
test_cases = [
  '5123456789012346', '4123456789012346', '5623456789012346',
  '5111111111111111'
]

for tc in test_cases:
  if re.match(pattern, tc):
    print(f"{tc} is a valid MasterCard number.")
  else:
    print(f"{tc} is not a valid MasterCard number.")
'''
마스터카드 정규표현식 검출하는 코드
'''
