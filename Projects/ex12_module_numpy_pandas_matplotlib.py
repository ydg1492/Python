#데이터를 수집했다면.. 분석
#데이터분석을 쉽게 해주는 대표적인 외부 모듈:numpy,pandas
#보기편하게 시각화(그래프)해주는 외부 모듈:matplotlib

#외부모듈 설치

#1)numpy(numberic python):배열같은 대량의 데이털르 행렬 수학계산 해주는 기능모듈

#1.일반적인 파이썬의 배열(리스트)
aaa= [10,20,30]
bbb= [4,5,6]

#파이썬의 배열(리스트)는 덧셈을 하면 산수덧셈이 아니라, concat()이 되어 요소가 추가됨.
# ccc= aaa+bbb
# print(ccc)

#2.numpy 배열로 만들어서.. 산술덧셈을 수행
import numpy as np
aa= np.array([10,20,30]) #리스트를 numpy용 배열자료행으로 만들기
bb= np.array([4,5,6])

#배열끼리 산술 덧셈
cc= aa+bb
print(cc)

#사칙연산 모두 가능
print(aa-bb)
print(aa*bb)
print(aa/bb)

#사칙연산 말고도 많은 수학적 기능을 가지고 있지만...2부 수업에서 정식 소개
print()
#-------------------------------------------------------------

#2)panda: 엑셀이나, csv처럼 표형태의 데이터를 실제 표처럼 쉽게 다를수 있도록 해주는 모듈
import pandas as pd

#csv파일을 읽어와서 행열 표형태(DataFrame이라고 부름)로 만들어 줌
aa= pd.read_csv('Projects/file/scores.csv')
print(aa)

print(aa.head()) #상위 5개만 추출
print(aa.tail()) #하위 5개만 추출
print(aa.head(n=2)) #상위 2개만 추출
print(aa.shape) #행렬 모양(개수 확인)

#국어성적만..확인
print(aa['국어'])

#한 제목들 확인
print(aa.columns)

#데이터분석에 필요한 기초 계산을 해줌(집계함수)
print("korean average:",aa['국어'].mean())
print("korean average:",aa['영어'].max())

#기초 계산들을 모두 해주는 기능(평균,최대값,중위값..25%해당 값 등..을 모두 알려줌)
print(aa.describe())

#특정 학생의 성적들 추출(특정 행(줄:row))
rows= aa.loc[1:3] #1~3까지
print(rows)
print()

rows= aa.loc[2:,['이름','수학']]
print(rows)
print()
#----------------------------

#꽤 많은 회사에서 데이터들을 엑셀파일로 가지고 있는 경우가 많음
#원래 엑셀을 꽤 읽기 어려움...
#다행히 엑셀파일을 파이썬에서 쉽게 읽어오는 외부모듈이 존재함[openpyxl]
#[설치] pip install openpyxl

#pandas가 엑셀파일을 읽어들일때..openxl 모듈을 사용함..
bb= pd.read_excel('Projects/file/student_scores.xlsx')
print(bb)
print()
#분석하는 방법은 위 csv 때와 똑같이 수행가능.
print(bb.describe())
print()
#------------------------------------------------------------------

#3)matplotlib: 파이썬에서 데이터를 눈으로 보기 쉽게 시각화하는 모듈
# 숫자가 있는 모든 데이터 표현 가능 [선그래프,막대그래프,원그래프]

#1.모듈 사용
import matplotlib.pyplot as plt

#그래프에 한글이 깨지지 않도록..한글글꼴을 지정
plt.rcParams['font.family'] = 'Malgun Gothic'
#[1]하루동안의 온도변화 그래프 -------------------------------------
#2.데이터 준비
#시간별 온도
hours= [6,9,12,15,18,21,24] #그래프의 x축 데이터:
temperature= [10,14,18,20,17,13,11] #그래프의 y축 데이터:

#3.그래프 그리기
plt.plot(hours, temperature, marker='o', linestyle='--', color='orange')
#plt.plot(hours, temperature, marker='x')

#그래프 꾸미기
plt.title('하루 동안의 온도변화') #한글은 깨짐
plt.xlabel('시간')
plt.ylabel('온도', rotation=0)
plt.grid(True)
#4.그래프 표시
#plt.show()
#--------------------------------------------------------------------------------------

#예제2)
# 1. 롯데리아 월별 매출 데이터 준비 (가상)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

#위 dict를 판다스로 아주 쉽게 표로 만들 수 있음
ee= pd.DataFrame(data)
print(ee)

#그래프로 시각화 하기
plt.figure(figsize=(11,7)) #도화지 사이즈 -- 가로가 긴 그래프
#산점도 그래프 표시
plt.scatter(ee['월'],ee['매출액(만원)'],marker='o',color='tomato') #x축, y축

#그래프 꾸미기
plt.title('롯데리아 2026년 월별 매출 변화')
plt.xlabel('월')
plt.ylabel('매출액 (만원)', rotation=0)
plt.grid(True)

# x축 간격
plt.xticks(range(0, 13, 1))

# y축 간격
plt.yticks(range(4000, 8000, 200))

#각 점마다 매출액 값 표시하기
for idx, value in enumerate(ee['매출액(만원)']):
    plt.text(idx,value +50,f"{value}",ha='center', fontsize=9)
    plt.plot(ee['월'],ee['매출액(만원)'])
#그래프 출력
plt.show()

