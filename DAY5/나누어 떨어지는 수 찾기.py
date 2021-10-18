#list들의 각 원소들 중 divisor로 나누어 떨어지는 값들을 새로운 list에 담아서 출력해주세요. 나누어 떨어지는 값이 하나도 없으면 -1을 담아주세요

#=======================================
list1 = [5,9,7,10]
divisor1 = 5

# 출력 : [5, 10]


for a in range(len(list1)):
    if list1[a]%divisor1==0:
        print(list1[a]," ",end="")
print("")


#=======================================
list2 = [2,36,1,3]
divisor2 = 1

# 출력: [2, 36, 1, 3]

for a in range(len(list2)):
    if list2[a]%divisor2==0:
        print(list2[a]," ",end="")
print("")
#=======================================
list3 = [3,2,6]
divisor3 = 10

# 출력: [-1]

for a in range(len(list3)):
    if list3[a]%divisor3==0:
        print(list3[a])
    else:
        list3.append(-1)
print(list3[-1])
    

