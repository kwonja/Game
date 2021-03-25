#예제
# 1부터 5까지 반복 프린트
#for i in range(1,6,1):
#    print(i,end=" ")

#10부터 1까지 역순 반복
#for i in range(10,0,-1):
#    print(i,end=" ")

#p167_.py     1부터 n까지 합 구하기

#sum=0
#n=10
#for i in range(1,n+1):
#    sum=sum+i
#print("합=",sum)

# 구구단 1부터 5까지 출력

#for i in range(1,6):
#    print("9 *",i,"=",9*i)

#lab:팩토리얼 계산하기
#sum=1
#n=int(input("정수를 입력하시오: "))
#for i in range(1,n+1,1):
#    sum=sum*i
#print(n,"!은",sum,"이다.")

#lab: n-각형 그리기:shape1_py
#import turtle
#t = turtle.Turtle()
#t.shape("turtle")
#s = turtle.textinput("", "몇각형을 원하시나요?:")
#n=int(s)
#for i in range(n):
#    t.forward(100)
#    t.left(360/n)
#turtle.mainloop()
#turtle.bye()

#lab: 방정식의 해 구하기:root_.py
#COUNT = 100
#START = 1.0
#END = 2.0
#for i in range(COUNT):
#     x = START + i*((END-START)/COUNT)
#     f = (x**2 -x -1)
#     if abs(f-0.0) < 0.01 :
#        print("방정식의 해는 ", x)


#sum_py  제어 변수 선언(while 루프 사용)

#i=0
#sum=0
#while i<= 10:
#    sum=sum+i
#    i=i+1
#print("합계는",sum)

#else 가 있는 while 루프

#i=0
#while i<3:
#    print("루프 안쪽")
#    i=i+1
#else:
#    print("else 부분")

#무한반복 오류

#i=0;
#while(i<10):
#    print("hello")

#lab : 구구단 출력

#단=int(input("원하는 단은: "))
#i=1

#while i<=9:
#    print("%d * %d=%d" %(단,i,단))
#    i=i+1

#lab : 숫자 맞추기 게임

#import random
#tries = 0 # 시도 횟수
#guess = 0 # 사용자의 추측값
#answer = random.randint(1, 100) # 1과 100사이의 난수
#print("1부터 100 사이의 숫자를 맞추시오")
#while guess != answer :
#     guess = int(input("숫자를 입력하시오: "))
#     tries = tries + 1
#     if guess < answer:
#         print("너무 낮음!")
#     elif guess > answer:
#         print("너무 높음!")
#         
#if guess == answer:
#    print("축하합니다. 시도횟수=", tries)
#else:
#    print("정답은 ", answer)


#lab 초등생을 위한 산수 문제 발생기

#import random
#flag = True
#while flag:
#  x = random.randint(1, 100)
#  y = random.randint(1, 100)
#  answer = int(input("%d+%d ="%(x,y)))
#  if answer == x + y:
#     print("잘했어요!!")
#  else:
#    print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
#  flag = False

#lab 로그인 프로그램

#암호가 pythonisfun 이면 로그인 성공
#password = ""
#while password != "pythonisfun":
#     password = input("암호를 입력하시오: ")
     
#print("로그인 성공")

#중첩 반복문

#예제1
#for y in range(5) :
#    for x in range(10) :
#       print("*", end="" )
#    print("")  

#예제2

#for y in range(1,6):
#    for x in  range(1,y):
#        print("*",end=" ")
#    print("*")


#예제3

#adj=["small","medium","large"]
#non=["apple","banana","grape"]
#for x in adj:
#    for y in non:
#        print(x,y)

#lab : 주사위 합이 6이 되는 경우
#for a in range(1,7):
#    for b in range(1,7):
#        if a+b ==6:
#            print("첫번째 주사위=%d"%(a),"두번째 주사위=%d"%(b))

#lab : 모든 조합 출력하기

#persons = [ "Kim" , "Park" , "Lee"]
#restaurants = [ "Korean" , "American" , "French"]
#for person in persons:
#     for restaurant in restaurants:
#         print(person + "이 " + restaurant+" 식당을 방문")


#조건문 반복문

#예제 1
#while True:
#  light = input("신호등 색상을 입력하시오 ")
#  if light == "green":
#        break
#print(" 전진!! ")
#예제2 3의 배수면 출력x
#for i in range(1, 11):
#     if i%3 == 0 :
#          continue
#     print(i, end=" ") 


#lab 소수찾기
#N_PRIMES = 50 # 찾아야 하는 소수의 개수
#number = 2 # 2부터 시작한다.
#count = 0
#while count < N_PRIMES :
#      divisor = 2 # 나누는 수는 2부터 시작하여 하나씩 증가한다.
#      prime = True
#      while divisor < number :
#          if number % divisor == 0: # 나누어지면 소수가 아니다.
#                 prime = False
#                 break;
#          divisor += 1
#      if prime: # 소수이면 소수 개수를 증가하고 출력한다.
#           count += 1
#           print(number, end=" ")
#      number += 1 # 다음 수로 간다.

#lab 파이 계산하기
#divisor = 1.0
#divident = 4.0
#sum = 0.0
#loop_count = int(input("반복횟수:"))
#while(loop_count > 0):
#   sum = sum + divident / divisor
#   divident = -1.0 * divident
#   divisor = divisor + 2
#   loop_count = loop_count - 1
#print("Pi = %f" % sum)

#lab 거북이 랜덤 워크
#import turtle
#import random
#t = turtle.Turtle()
#t.shape("turtle")
#for i in range(30):
#  length = random.randint(1, 100)
#  t.forward(length)
#  angle = random.randint(-180, 180)
#  t.right(angle)
  
#turtle.mainloop()
#turtle.bye()

#스파이럴 그리기
#import turtle
#t = turtle.Turtle()
#t.shape("turtle")
#for i in range(200):
#  t.forward(2+i/4) 
#  t.left(30-i/12) 

#turtle.mainloop()
#turtle.bye()

#도박상의 확률
#import random
#initial_money = 50
#goal = 250
#wins = 0
#for i in range(100) : # 라스베가스에 100번 간다.
#      cash = initial_money
#      while cash > 0 and cash < goal : # 돈이 0이거나 250불을 따면 반복 중단
#         number = random.randint(1, 2)
#         if number == 1 :
#             cash = cash + 1 # $1을 딴다.
#         else :
#            cash = cash - 1 # $1을 잃는다.
#      if cash == goal : wins = wins + 1
#      
#print("초기 금액 $%d" % initial_money)
#print("목표 금액 $%d" % goal)
#print("100번 중에서 %d번 성공" % wins)




    