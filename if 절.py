weather = input("오늘 날씨가 어때요?")
if weather == "비" or weather== "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")

tempt = int(input("기온은 어떄요?"))
if 30 <= tempt:
    print("너무 더워요. 나가지 마세요.")
#elif 10 <= temp < 30 : 이리 해도 된다!!!
elif 10 <= tempt  and tempt < 30 :
    print("괜찮은 날씨에요")
elif 0 <= tempt <10 :
    print("외투를 챙기세요")
elif 0 > tempt :
    print("날씨가 너무 추비워요. 나가지 마세요.")