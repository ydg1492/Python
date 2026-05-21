#모듈: 하나의 py 파일에 모든 코드를 작성하면 기능별로 관리하거나 재사용하기 어려움

#모듈은 여러변수와 함수를 가지고 있는 코드 파일의 집합체

#모듈의 종류
#1) 표준모듈: 파이썬에 기본으로 내장되어 있어서 별도의 다운로드 설치 필요없이 import만 하면 사용가능(표준함수는 아님.) 즉 import을 선언함
#2) 외부모듈: 파이썬 설치 할때 같이 설치한 pip(CLI 패키지 인스톨러 프로그램)으로 다운로드 설치 후 import 하여 사용 - Package Installer for Python

#먼저 표준모듈 중 활용이 많이 모듈들...

#1.math 모듈: 수학적 연산기능(함수)을 모아놓은 모듈 - ML에서 많이 활용

import math

print(math.sin(1))
print(math.cos(1))
print(math.log(100,10))
print(math.log(8,2))
print(math.floor(3.7)) #소수점제거
print(math.ceil(3.7)) #소수점올림

#반올림은 math모듈을 사용하지 않고.. 표준함수 round() 이용
print(round(3.7))
print(round(3.2))

#함수가 아닌 값을 가진 변수도 모듈안에 존재함
print(math.pi)
#---------------

#1.1 모듈의 기능을 사용할때 마다 math라는 모델명을 쓰고..함수명을 쓰기에..좀 번거로움
#모듈명이 길면..
#그래서 import하면서 module명을 다르기 바꿔 부를 수 있음.

import math as m
print(m.pow(4,2)) #4의 2제곱

#1.2 모듈안에 있는 중에서 매우 자주 사용하는 기능이 있다면.. 모듈명을 쓰는것 조차 번거로움
#import 할때.. 표준함수처럼.. 함수명만 쓰면 되도록..모듈전체가 아닌 함수만 import 할수 있음.

from math import floor
print(floor(3.7))
print()
#----------------------------------

#2. random 모듈: 랜덤값 제공 기능을 가진 모듈
import random
print(random.random()*10) #0.0 ~0.999999999999999
print(random.randrange(10)) #0~9 까지 정수 중 랜덤
print(random.randrange(5,16)) #5~15까지 정수 중 랜덤

#리스트 요소 중 랜덤하게 값을 선택...
aaa= [10,20,30,40,50]
print(random.choice(aaa)) #1개 선택
print(random.sample(aaa,3)) #3개 선택 ~리스트로 결과를 줌

#[예] 로또 번호 추천..........
lotto= list(range(1,46))
print(lotto)

#로또 번호 45개중 6개를 랜덤하게 선택
nums= random.sample(lotto,6)
print(nums)

#낮은 번호 순으로..정렬
nums.sort()
print(nums)

#3. os 모듈: 운영체제와 관련된 기능 모듈
import os
print('현재 작업폴더:', os.getcwd()) #current wworking directory
print('현재 폴더목록:', os.listdir()) #현재폴더의 파일 및 폴더 목록

#폴더 만들기
#os.mkdir('image')
#존재하는 폴더명을 다시 만들려고 하면 에러!! 그래서 존재하지 않을때만 만들도록..
if not os.path.isdir('image'):
    os.mkdir('image')

#폴더 삭제하기
if os.path.isdir('image'):
    os.rmdir('image')

#파일명 변경해보기
if os.path.exists('aaa.txt'):
    os.rename('aaa.txt','newname.txt')

#폴더 위치 이동
print('현재 폴더위치:', os.getcwd())
os.chdir('..') #상위폴더로..
print('현재 폴더위치:', os.getcwd())
os.chdir('Python')
print('현재 폴더위치:', os.getcwd())

#cmnd 나 터미널 창에서 작성했던 대부분의 명령어들은 파이썬코드로 실행할수 있음
#os.system('dir') #터미널에 dir 명령어를 쓰는 것과 같은 기능

#함수를 사용하는 취소선같은 것이 보인다면..더이상 사용을 권장하지 않는 다는 뜻. deprecated되었다고 함.
# import subprocess
# subprocess.run('dir', shell=True)
# os.chdir('Projects')
# subprocess.run('ex01_print.py', shell=True)
# os.chdir('..')
print('-'*30)
print()
#-------------------------------------

#4 datetime 모듈: 날짜와 시간 관련 기능 제공 모듈
import datetime

#현재 날짜와 시간 얻어오기
now= datetime.datetime.now()
print(now.strftime("%Y년-%m월-%d일 %H시:%M분:%S초"))
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print()

#특정 시간 변경 기능
future= now.replace(year=(now.year+1))
print(now)
print(future)

#경과시간 같은 것을 계산해야 하는 경우가 있음..
#경과시간을 계산하기 편하게 ... 시간의 기록을 카운팅한 값이 존재함.
print(now.timestamp()) #... 1970-01-01 0:0:0 초부터 밀리센컨드 마다 카운팅된 값
print()

#타임스탬프로 기록값 숫자를 통해 특정 작업이 얼마나 시간이 소요되었는지 확인 가능

start= datetime.datetime.now() #이 순간의 시간...
#특정작업!!
for n in range(10000):
    print(n, end='') 
print()
end= datetime.datetime.now()#아 순간의 시간...

#경과시간 계산.. 종료시간 - 시작시간
ellipsed_time= end-start
print('경과시간:',ellipsed_time)
print()

#날짜 계산 프로그램 만들기
a_day= datetime.datetime(2026, 4, 29)
today= datetime.datetime.now()
print('개강일 부터:', today-a_day)
print('개강일 부터:', (today-a_day).days, "일 경과")

#5 time모듈
import time

# print('3초간 프로그램을 정지하기..잠시만 기다려 주세요..')
# time.sleep(3)
# print('프로그램이 다시 시작됩니다.')

#타임스탬프로..더 간단하게
print(time.time())
print(time.time_ns())

# #6 urllib 모듈:URL(Uniform Resource Location) 관련 기능 제공 모듈
# from urllib import request

# url= request.urlopen("https://wwww.naver.com")
# data= url.read()
# print(data)
