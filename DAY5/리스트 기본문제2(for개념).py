# for문을 이용해 list이용하기
list1 = [10,22,33,44,55,66,77,88,99,100]

# 1. len 함수를 이용해 리스트의 길이를 구해주세요.
print(len(list1))
b=len(list1)
a=0
print("길이")
# 2. 구한 길이를 이용해 while문으로 모든 값을 출력해주세요.
print("while 출력")
while a<=b-1:
    print(list1[a])
    a+=1


# 3. 위 리스트를 for문을 이용해 출력해주세요.
print("for 출력")
for i in range(b):
    print(list1[i])
# 4. 위 리스트를 for문을 이용해 3의 배수만 출력해주세요.
print("for 3의 배수")
for j in range(b):
    if list1[j]%3==0:
        print(list1[j])
total=0
# 5. 위 리스트를 for문을 이용해 리스트의 모든 값들을 더한 값을 출력해주세요.
print("모든값 더하기")
for k in range(b):
    total+=list1[k]
    print(total)

# while 버전, for .. in 버전
