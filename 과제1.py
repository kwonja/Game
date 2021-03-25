#011
#삼성전자=50000
#print(삼성전자*10)
#012
#print("항목","     값")
#money=input("시가총액     ")
#nowprice=input("현재가     ")
#per=input("PER     ")

#013
#s="hello"
#t="pyton"
#print(s+"! "+t)

#014
#print(2+2*3)

#015
#a=128
#print(type(a))

#016
#num_str="720"
#print(type(num_str))
#num_str=int(num_str)
#print(type(num_str))

#017
#num=100
#print(type(num))
#num=str(num)
#print(type(num))

#018
#num="15.79"
#num=float(num)
#print(type(num))

#019
#year="2020"
#year=int(year)
#print(year-1)
#print(year-2)
#print(year-3)

#020
#price=48584
#rate=36
#print(price*36)
#################

#101
#a=100>20
#type(a)    #인터프리터에 bool이라고 나옴

#102
#print(3==5) #false

#103
#print(3<5) # true

#104
#x=4
#print(1<x<5) true

#105
#print(3==3 and 4!=3) #true

#106

#107
#if 4<3:
#    print("hello world")   출력이 이뤄지지 않음

#108
#if 4 < 3:
#    print("Hello World.")
#else:
#    print("Hi, there.")     # 이부분이 출력

#109
#if True :
#    print ("1")
#    print ("2")
#else :
#    print("3")
#print("4")                #1,2,4, 출력

#110
#if True :
#    if False:
#        print("1")
#       print("2")
#    else:
#        print("3")
#else :
#    print("4")
#print("5")               # 3, 5 출력

#111
#a="안녕하세요"
#print(a*2)

#112
#x=int(input("숫자를 입력하세요: "))
#print(x+10)

#113
#x=int(input())
#if x%2==0:
#    print("짝수")
#else :
#    print("홀수")

#114
#x=int(input("입력값: "))
#if(x+20>255):
#    print("출력값: 255")
#else:
#    print("출력값:", x+20)

#115
#x=int(input("입력값: "))
#if(0<=(x-20)<=255):
#    print("출력값: ",x-20)
#else :
#    if(x-20<0):
#        print("출력값: 0")
#    else:
#        print("출력값: 255")

#116
#x=input("현재시간:")
#if(x[3]=="0" and x[4]=="0"):
#    print("정각 입니다.")
#else :
#    print("정각이 아닙니다")

#117
#x=input("종아하는 과일은? ")
#if(x=="사과" or x=="포도" or x=="홍시"):
#    print("정답입니다")
#else:
#    print("오답입니다")

#118
#x=input("투자종목: ")
#if(x=="Microsoft"or x=="Google"or x
#   =="Naver"or x=="Kakao"or x=="SAMSUNG" or x=="LG"):
#    print("투자 경고 종목입니다")
#else:
#    print("투자경고 종목이 아닙니다")

#119           -> 질문
#fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
#user = input("제가좋아하는계절은: ")
#if user in fruit.keys():
#    print("정답입니다.")
#else:
#    print("오답입니다.")

#120
#fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
#x=input("제가 좋아하는과일은? ")
#if x in fruit.values():
#     print("정답입니다.")
#else:
#     print("오답입니다.")

#121
#a=input("문자: ")
#if a.islower():
#    print(a.upper())
#else:
#    print(a.lower())     

#122
#score = input("score: ")
#score = int(score)
#if 81 <= score <= 100:
#    print("grade is A")
#elif 61 <= score <= 80:
#    print("grade is B")
#elif 41 <= score <= 60:
#    print("grade is C")
#elif 21 <= score <= 40:
#    print("grade is D")
#else:
#    print("grade is E")

#123
#환율 = {"달러": 1167, 
#      "엔": 1.096, 
#      "유로": 1268, 
#      "위안": 171}
#user = input("입력: ")
#num, currency = user.split()
#print(float(num) * 환율[currency], "원")

#124
#num1 = int(input("input number1: "))
#num2 = int(input("input number2: "))
#num3 = int(input("input number3: "))
#if num1 > num2 and num1 > num3:
#    print(num1)
#elif num2 > num1 and num2 > num3:
#    print(num2)
#else:
#    print(num3)

#125
#x=input("휴대전화 번호 입력: ")
#a,b,c=x.split("-")
#통신사={"011":"SKT","016":"KT","019":"LGU","010":"알수없음"}
#if a in 통신사:
#    print("당신은",통신사[a],"사용자입니다")

#126
#x = input("우편번호: ")
#x = x[:3]
#if x in ["010", "011", "012"]:
#    print("강북구")
#elif x in ["014", "015", "016"]:
#    print("도봉구")
#else:
#    print("노원구")

#127
#x=input("주민등록번호: " )
#if x[7]=="1" or x[7]== "3":
#    print("남자")
#elif x[7]=="2" or x[7]=="4":
#     print("여자")

#128
#x = input("주민등록번호: ")
#y = x.split("-")[1]
#if 0 <= int(y[1:3]) <= 8:
#    print("서울입니다.")
#else:
#    print("서울이 아닙니다.")

#129

#num = input("주민등록번호: ")
#계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#        int(num[11])* 4 + int(num[12]) * 5
#계산2 = 11 - (계산1 % 11)
#계산3 = str(계산2)

#if num[-1] == 계산3[-1]:
#    print("유효한 주민등록번호입니다.")
#else:
#    print("유효하지 않은 주민등록번호입니다.")

#130

#import requests
#btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#시가=float(btc["opening_price"])
#변동폭=float(btc["max_price"]) - float(btc["min_price"])
#if (시가+변동폭) > float(btc["max_price"]):
#    print("상승장")
#else:
#    print("하락장")




