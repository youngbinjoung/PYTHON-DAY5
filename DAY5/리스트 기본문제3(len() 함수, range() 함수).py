list1 = [2,5,9,11,23,51,26,38,41,93,101]

# range 함수를 이용해 1 ~ 100 까지 출력해주세요.
for a in range(len(list1)):
    print(list1[a])
# range 함수를 이용해 위 리스트의 '홀수번째' 값만 출력해주세요.
for b in range(len(list1)):
    if list1[b]%2==1:
        print(list1[b])
# range 함수를 이용해 위 리스트의 '짝수값'만 출력해주세요. 
for c in range(len(list1)):
    if list1[c]%2==0:
        print(list1[c])
# range 함수를 이용해 구구단을 출력해주세요.
for gugu in range(2,10):
    print("== {}단 ==".format(gugu))
    for dan in range(2,10):
        print("{} x {} = {}".format(gugu,dan,gugu*dan))
               
