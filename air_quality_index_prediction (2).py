# -*- coding: utf-8 -*-
"""Air Quality Index Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wvwEul636mpgIgtlfyvEt3VzWBrivl6U

# **WEEK 1 TASK**
"""

!pip install numpy pandas matplotlib seaborn scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/air quality data.csv')
df.head()

# @title PM10 vs NO

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='PM10', y='NO', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df.shape

df.info()

df.duplicated().sum()

df.isnull().sum()

df.dropna(subset=['AQI'],inplace = True)

df.isnull().sum().sort_values(ascending = False)

df.describe().T

null_values_percentage = (df.isnull().sum()/df.isnull().count()*100).sort_values(ascending = False)
null_values_percentage

"""# **WEEK 2 TASK**"""

df['Xylene'].plot(kind = 'hist', figsize=(10,5))
plt.legend
plt.show()

df['PM10'].plot(kind = 'hist', figsize=(15,5))
plt.legend
plt.show()

df['NH3'].plot(kind = 'hist', figsize=(10,5))
plt.legend
plt.show()

df['Toluene'].plot(kind = 'hist', figsize=(10,5))
plt.legend
plt.show()

df['Benzene'].plot(kind = 'hist', figsize=(10,5))
plt.legend
plt.show()

df['SO2'].plot(kind = 'hist', figsize=(10,5))
plt.legend
plt.show()

sns.displot(df,x='AQI',color='black')
plt.show()

sns.set_theme(style="darkgrid")
graph = sns.catplot(x="City", kind="count", data=df,height = 5,aspect = 3)
graph.set_xticklabels(rotation=90)

sns.set_theme(style="darkgrid")
graph = sns.catplot(x="City", kind="count", data=df, col="AQI_Bucket", col_wrap=2, height=3.5, aspect=3) # Changed col_warp to col_wrap
graph.set_xticklabels(rotation=90)

graph1 = sns.catplot(x='City',y='PM2.5',kind='box',data=df,height=5,aspect=3) # Changed 'ascept' to 'aspect'
graph1.set_xticklabels(rotation=90)

graph1 = sns.catplot(x='City',y='NO2',kind='box',data=df,height=5,aspect=3) # Changed 'ascept' to 'aspect'
graph1.set_xticklabels(rotation=90)

graph1 = sns.catplot(x='City',y='O3',kind='box',data=df,height=5,aspect=3) # Changed 'ascept' to 'aspect'
graph1.set_xticklabels(rotation=90)

graph1 = sns.catplot(x='City',y='SO2',kind='box',data=df,height=5,aspect=3) # Changed 'ascept' to 'aspect'
graph1.set_xticklabels(rotation=90)

graph5 =sns.catplot(x='AQI_Bucket',kind='count',data=df,height=5,aspect=3)
graph5.set_xticklabels(rotation=90)

df.isnull().sum().sort_values(ascending=False)

df.describe().loc['mean']

df = df.replace({
    "PM2.5" : {np.nan:67.476613},
    "PM10" : {np.nan : 118.454435},
    "NO" : {np.nan : 17.622421},
    "NO2" : {np.nan:	28.978391},
    "NOx" : {np.nan:	32.289012},
    "NH3" : {np.nan :	23.848366},
    "CO" :{np.nan:	2.345267},
    "SO2" : {np.nan:	14.362933},
    "O3" : {np.nan :	34.912885},
    "Benzene" : {np.nan:	3.458668},
    "Toluene" : {np.nan :	9.525714},
    "Xylene":{np.nan:	3.588683}

})

df.isnull().sum()

df = df.drop(['AQI_Bucket'],axis = 1)

df.head()

sns.boxplot(data=df[['PM2.5','PM10']])
plt.show()

sns.boxplot(data=df[['NO2','NO','NOx',"NH3"]])
plt.show()

sns.boxplot(data=df[['SO2','O3']])
plt.show()

def replace_outliers(df):
  for column in df.select_dtypes(include=['number']).columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = df[column].apply(
        lambda x: Q1 if x < lower_bound else (Q3 if x > upper_bound else x)
    )
  return df

df = replace_outliers(df)

df.describe()

sns.boxplot(data=df[['PM2.5','PM10']])

sns.boxplot(data=df[['O3','SO2']])

sns.boxplot(data=df[['NO','NO2','NOx']])

sns.displot(df,x='AQI',color = 'grey')
plt.show()

df1 = df.drop(columns=['City'])

plt.figure(figsize=(12,8))
sns.heatmap(df1.drop(columns=['Date']).corr(), annot=True)
plt.show()

"""# **WEEK 3 Task**"""

df.drop(['Date','City'],axis = 1,inplace = True)
df.head()

from sklearn.preprocessing import StandardScaler
df1 = StandardScaler().fit_transform(df)
df1

df = pd.DataFrame(df1,columns=df.columns)
df.head()

from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error,r2_score

df.columns

X = df[['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']]
y = df['AQI']

X.head()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print('Shape of X train',X_train.shape)
print('Shape of X test',X_test.shape)
print('Shape of y train',y_train.shape)
print('Shape of y test',y_test.shape)

LR = linear_model.LinearRegression()
LR.fit(X_train,y_train)

train_pred = LR.predict(X_train)
test_pred = LR.predict(X_test)

RMSE_train = np.sqrt(mean_squared_error(y_train,train_pred))
RMSE_test = np.sqrt(mean_squared_error(y_test,test_pred))
print('RMSE for train data',str(RMSE_train))
print('RMSE for test data',str(RMSE_test))
print('_'*60)
print('R Squared value for Train',LR.score(X_train,y_train))
print('R Squared value for Test',LR.score(X_test,y_test))

knn = KNeighborsRegressor()
knn.fit(X_train,y_train)

train_pred = knn.predict(X_train)
test_pred = knn.predict(X_test)
RMSE_train = np.sqrt(mean_squared_error(y_train,train_pred))
RMSE_test = np.sqrt(mean_squared_error(y_test,test_pred))
print('RMSE for train data',str(RMSE_train))
print('RMSE for test data',str(RMSE_test))
print('_'*60)
print('R Squared value for Train',knn.score(X_train,y_train))
print('R Squared value for Test',knn.score(X_test,y_test))

dtr = DecisionTreeRegressor()
dtr.fit(X_train,y_train)

train_pred = knn.predict(X_train)
test_pred = knn.predict(X_test)
RMSE_train = np.sqrt(mean_squared_error(y_train,train_pred))
RMSE_test = np.sqrt(mean_squared_error(y_test,test_pred))
print('RMSE for train data',str(RMSE_train))
print('RMSE for test data',str(RMSE_test))
print('_'*60)
print('R Squared value for Train',dtr.score(X_train,y_train))
print('R Squared value for Test',dtr.score(X_test,y_test))

rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)

train_pred = knn.predict(X_train)
test_pred = knn.predict(X_test)
RMSE_train = np.sqrt(mean_squared_error(y_train,train_pred))
RMSE_test = np.sqrt(mean_squared_error(y_test,test_pred))
print('RMSE for train data',str(RMSE_train))
print('RMSE for test data',str(RMSE_test))
print('_'*60)
print('R Squared value for Train',rfr.score(X_train,y_train))
print('R Squared value for Test',rfr.score(X_test,y_test))