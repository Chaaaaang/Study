# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 21:01:19 2019

@author: User
"""

# 2. 데이터의 이해

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = r'D:\graduated_school\Study\Data_Mining\data\Titanic/'

train_data = pd.read_csv(data_path+'train.csv')

# 2.1 데이터 객체와 속성 유형
train_data.head()
train_data.info()

"""
2.1.1 명목속성 
- 수학적 연산의 의미 x. 유의미한 순서나 정량적 값을 갖고 있지 않음.
- 출현 빈도 등에 대해서 고려 가능.
- 필드 : PassengerID, Survived, Pclass, Name, Ticket, Cabin, Embarked 속성

2.1.2 이진 속성
- 0과 1의 속성을 가짐
- 상태값 두 개가 동등한 가치와 중요도를 가지지 않을 때 씀.
- 필드 : Sex, Survived

2.1.3 순서 속성
- 유의미한 순서나 순위를 값으로 갖는 속성.
- SibSp, Parch 등
- 최빈수, 중위수 등이 의미 있음.

2.1.4 숫자 속성
- 간격 척도 속성 : 절대 영점이 없음. 즉, 5도와 10도가 2배 차이가 아님.
 -> 비율 계산 불가능
- 비율 척도 속성 : 비율까지 가능.
- 평균, 중위수, 최빈수 계산 가능
"""

# 2.2 데이터에 대한 기술 통계
"""
2.2.1 중심 경향 측정 : 평균, 중위수, 최빈값
- 평균
 ○ 이상치에 민감함
 ○ 높고 낮은 극단의 값을 버린 후 평균 계산하기도 함.
  -> 정보 손실의 문제가 발생 할 수 있으므로 계산시 너무 많이 제거 안하는 것이 좋음.

- 중위값
 ○ 비대칭 데이터에서 평균보다 중심 측정 단위가 될 수 있음.
 ○ 순서도 고려하게 됨
 ○ 많은 양의 관측치는 계산자원이 많이 필요 할 수도 있음.

- 최빈값
 ○ 가장 빈번히 발생하는 값
 ○ 여러 값들이 최빈 값을 가진 경우 1개, 2개, 3개에 대해 유니모달, 바이모달, 트라이모달이라 함

- 대칭성을 가진 데이터 : 평균 = 중위수 = 최빈값
- 좌측으로 치우친 데이터(좌측에 데이터 많은 경우) : 최빈값 < 중위수 < 평균
- 우측으로 치우친 데이터(좌측에 데이터 많은 경우) : 평균 > 중위수 > 최빈값


2.2.2 데이터 분포 측정
- 데이터가 오름차순으로 정렬되어 있다고 가정함.
- 범위 : 최대값과 최소값의 차이값
- 사분위수 : 25%분위수, 50%분위수, 75%분위수를 기준으로 4개의 영역으로 데이터를 나누는 것을 말함.
 ○ IQR(사분위 범위) : 1번째 사분위수와 3번째 사분위수 사이의 거리. -> Q3 - Q1
- 박스플롯
 ○ 박스의 길이는 사분위수 범위. 중위수(25% ~ 75%)는 상자 내부의 선 사이 값.
 ○ 중위수는 상자내부의 선
 ○ 박스 외부의 두 개의 줄은 수염으로 1.5*IQR값임. 여기 넘어가는 점은 선이 아닌 점으로 표시함.(극단적 이상치)
- 분산과 표준편차 : 데이터 산포에 대한 측정값.
 ○ 표준편차는 평균에 대한 분산을 측정하여 평균을 중심 척도로 선택한 경우에만 고려함.
 ○ 관찰값은 평균으로부터 표준편차의 몇 배수 이상으로 떨어져 있을 가능성이 낮음.


2.2.3 기본 기술 통계값의 가시화
- 분위수플롯 : x는 분위수, y는 실제값임.
- 분위수대조플롯 : x, y를 같은 값으로 축을 놓고 같은 값을 선으로 연결한 후 실제 데이터를
점으로 나타내 봄 -> 많이 치우쳐 있으면 한 쪽으로 편향 된 것임.
- 히스토그램
 ○ 히스토는 '막대', 그램은 '차트'를 의미함
 ○ X는 값, Y는 X값의 빈도
 ○ X가 숫자값이면 히스토그램에 적합.
 ○ X의 넓이 : Bucket이라고 함(X값의 범위)
- 산점도
 ○ 2변량 데이터에 군집, 이상치, 상관관계를 살펴봄.
"""


# 
 


# Age의 평균값, 중위값
age = train_data['Age']
age.dropna(inplace=True)
np.mean(age)
np.median(age)

# Parch의 최빈값
parch = train_data['Parch']
parch.value_counts()[0]

# Survived의 최빈값
survived = train_data['Survived']
survived.value_counts()[0]


# Age의 범위
max(age) - min(age)

# Age의 사분위수
    # 1사분위수
np.percentile(age, 25) 

    # 2사분위수
np.percentile(age, 50) 
    
    # 3사분위수
np.percentile(age, 75) 

# Age의 분산
np.var(age)

# Age의 표준편차
np.std(age)

# 기술통계량 한번에 다 보기
age.describe()


# Age의 박스플롯
plt.boxplot(age)

# (Option) Q-Q plot
"""
Q-Q(Quantile-Quantile) plot
- 분석하고자 하는 샘플의 분포과 정규 분포의 분포 형태를 비교하는 시각적 도구. 
- 동일 분위수에 해당하는 정상 분포의 값과 주어진 분포의 값을 한 쌍으로 만들어 스캐터 플롯(scatter plot)으로 그린 것. 
- 그리는 방법

대상 샘플을 크기에 따라 정렬(sort)한다.
각 샘플의 분위수(quantile number)를 구한다.
각 샘플의 분위수와 일치하는 분위수를 가지는 정규 분포 값을 구한다.
대상 샘플과 정규 분포 값을 하나의 쌍으로 생각하여 2차원 공간에 하나의 점(point)으로 그린다.
모든 샘플에 대해 2부터 4까지의 과정을 반복하여 스캐터 플롯과 유사한 형태의 플롯을 완성한다.
비교를 위한 45도 직선을 그린다.
"""
import scipy.stats as stats
stats.probplot(age, plot=plt)
plt.axis("equal")
plt.show()


# Age의 히스토그램
age.hist()

# Age와 Fare의 산점도
data = train_data.dropna()
plt.scatter(data['Age'], data['Fare'])

import statsmodels.api as sm

X = data['Age']
Y = data['Fare']

results = sm.OLS(Y,sm.add_constant(X)).fit()

plt.scatter(X,Y)
X_plot = np.linspace(min(X),max(X),100)
plt.plot(X_plot, X_plot*results.params[0] + results.params[1])

plt.show()


# 수치형 데이터의 유사도 측정(유클리디안) : Age 데이터만 측정해봄
from sklearn.metrics.pairwise import euclidean_distances
euclidean_distances(X.values.reshape(-1,1), X.values.reshape(-1,1))
