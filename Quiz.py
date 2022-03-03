url= "https://naver.com"
my_str= url.replace("https://","")
my_str=my_str[:my_str.index(".")]
password=my_str[0:3]+ str(len(my_str))+ str(my_str.count("n"))+"!"
print("{0}의 비밀번호는 {1}입니다. "    .format(url,password))



print(my_str[0:3]+ str(len(my_str))+ str(my_str.count("n"))+"!")
