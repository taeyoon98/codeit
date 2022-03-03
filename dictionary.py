cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

#.get()을 쓰면 값이 없어 오류가떠도 none이라고 표시되고 프로그램은 계속 진행 반면 []쓰면 바로 종료된다. 그래서 cabinet.get(5,"사용 가능")하면 5
#라는 값이 없으면 사용가능이라고 표시된다

print(3 in cabinet) # true
print(5 in cabinet) # false

# 새 손님
print(cabinet)
cabinet[5] = "김태윤"
cabinet[3] = "전소민"
print(cabinet)

#간 손님
del cabinet[100]
print(cabinet)

#key 들만 출력
print(cabinet.keys())
#value 들만 출력
print(cabinet.values())
#key value 쌍으로 출력
print(cabinet.items())

#모든 값 제거
cabinet.clear()
print(cabinet)







