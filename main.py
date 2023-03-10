import random

#1에서 100사이의 임의의 수를 100개 생성하여 리스트를 만든다
a_list = [random.randrange(1, 100) for _ in range(0,100)]

#리스트 전체 출력
print('a_list : {}'.format(a_list))

#리스트 값을 [index] : value 형식으로 한 줄에 5개씩 출력
for i, v in enumerate(a_list):
    print('[{:2d}] : {:2d}'.format(i, v), end=' ')
    if (i+1) % 5 == 0:
        print(' ')

#리스트 값을 처음부터 10개씩 나누어 슬라이싱한 것을 출력
start, step = 0, 10        
for i in range(0, len(a_list), step):
    end = i+step
    print('{}'.format(a_list[start:end]))
    start = end
  
    
'''
다음 문제를 연습해보시기 바랍니다.
리스트 안에서 원하는 값들만 뽑아서 리스트를 다시 만들어 보는것을 연습해보기 위해 문제를 제출합니다.
리스트 안의 값 중 30 이상이고 60 이하인 숫자들의 갯수와 모두 더한 평균을 출력해보세요.
'''
count = 0
for num in a_list:
    if 30 <= num <= 60:
        count += 1

print("30 이상이고 60 이하인 숫자의 갯수: {}".format(count))

total = 0
for num in a_list:
    if 30 <= num <= 60:
        total += num

if count > 0:
    average = total / count
    print("30 이상이고 60 이하인 숫자들의 평균: {:.2f}".format(average))
else:
    print("30 이상이고 60 이하인 숫자가 없습니다.")