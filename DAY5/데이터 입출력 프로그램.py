'''
명령어를 입력해주세요: help (입력)

add : 데이터 추가
list : 데이터 조회
update : 데이터 수정
delete : 데이터 삭제

명령어를 입력해주세요 : add (입력)
저장할 값을 입력해주세요 : 10 (입력)
10을 저장했습니다. (출력)

명령어를 입력해주세요 : list (입력)
['10']

명령어를 입력해주세요 : add
저장할 값을 입력해주세요 : 20
20을 저장했습니다.

명령어를 입력해주세요 : list
['10', '20']

명령어를 입력해주세요 : update
몇번째 값을 수정하시겠습니까 : 1
어떤 값으로 수정하시겠습니까 : 100
1번째 값이 100으로 수정되었습니다.

명령어를 입력해주세요 : list
['100', '20']

명령어를 입력해주세요 : delete
몇번째 값을 삭제하시겠습니까 : 1
1번째 값을 삭제했습니다.

명령어를 입력해주세요 : list
['20']

명령어를 입력해주세요 : exit
프로그램을 종료합니다.

'''
list1=[]
print("====== help(도움말) ======")
while True:
    print("")
    command=input("명령어를 입력해주세요 :")
    print("")
    if command=="help":
        print("add : 데이터 추가")
        print("list : 데이터 조회")
        print("update : 데이터 수정")
        print("delete : 데이터 삭제")
    elif command=="add":
        add=int(input("저장할 값을 입력해주세요 : "))
        list1.append(add)
        print("{}을 저장했습니다.".format(add))
    elif command=="list":
        print(list1)
    elif command=="update":
        modify=int(input("몇번째 값을 수정하시겠습니까 :"))
        update=int(input("어떤 값으로 수정하시겠습니까 :"))
        list1[modify]=update
        print("{}째 값이 {}으로 수정되었습니다.".format(modify,update))
    elif command=="delete":
        delete=int(input("몇번째 값을 삭제하시겠습니까 :"))
        del list1[delete]
    elif command=="exit":
        break
print("프로그램을 종료합니다.")
