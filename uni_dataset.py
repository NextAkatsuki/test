import pandas as pd

data = pd.read_csv('gpascore.csv')
#만약만약에 중단에 있어야하는 값이 공백으로 있어서 찾고싶다
#print(data.isnull().sum())             #값이 빠져있는 부분 체크
data = data.dropna()                    #NAN/빈값있는 행 제거
#data.fillna(100)                       #빈값을 100으로 채운다

# x데이터 예시 인풋 [[380,3.21,3], [660,3.67,3], [], [], []]
x_data=[]
for i,rows in data.iterrows():
    x_data.append([rows['gre'],rows['gpa'],rows['rank']])

# y데이터 인풋 [[0], [1], [0], [0], [1]....]
y_data = data['admit'].values