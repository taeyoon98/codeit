from random import*
# 내가푼 풀이법 3.9 버전 이후부터는 set에서 셔플 안됨
#st1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#shuffle(st1)
#st1=set(st1)
#sample1=sample(st1,1)
#sample2=sample(st1 - set(sample1) ,3)
#print("-- 당첨자 발표 --")
#print("치킨 당첨자 :"+str(sample1))
#print("커피 당첨자 :"+str(sample2))
#print("-- 축하합니다 --")


# 답안
users= range(1,21)
users = list(users)

shuffle(users)
winners=sample(users,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :{0}".format(winners[0]))
print("커피 당첨자 :{0}".format(winners[1:]))
print("-- 축하합니다 --")





