import numpy as np
import pandas as pd

train = pd.read_csv(r"C:\Users\Administrator\Downloads\datafiles19cdaf8\train.csv")
test = pd.read_csv(r"C:\Users\Administrator\Downloads\datafiles19cdaf8\test.csv")
train.info()
print("\n")
print ("The train data has",train.shape)
print ("The test data has",test.shape)
print("\n")
print(train)
print("\n")
nans = train.shape[0] - train.dropna().shape[0]
print ("%d rows have missing values in the train data" %nans)
nand = test.shape[0] - test.dropna().shape[0]
print("%d rows have missing values in the test data" %nand)
print(train.isnull().sum())
#Education
train.workclass.value_counts(sort=True)
train.workclass.fillna('Private',inplace=True)


#Occupation
train.occupation.value_counts(sort=True)
train.occupation.fillna('Prof-specialty',inplace=True)


#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna('United-States',inplace=True)

print(train)
print(train.isnull().sum())

print("\n")
print(train.target.value_counts())
print(train.shape[0])
print(train.target.value_counts()/train.shape[0])
print(pd.crosstab(train.education, train.target,margins=True)/train.shape[0])
