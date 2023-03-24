import numpy as np
import pandas as pd
mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
        'Yield': [1010, 1025.2, 1404.2, 1251.7],
        'cost' : [102, np.nan, 20, 68] }
crops = pd.DataFrame(mydata)
crops.isnull() 

#print(mydata)
#print()
crops = crops['cost'].fillna(value = "UNKNOWN",inplace = True)
#print(crops)

data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], "Price" : [10000,50000,20000,10000,10000,40000]})
#print(data.loc[data.duplicated(keep = "all"),:])


iris = pd.read_csv(r"C:\Users\Administrator\Downloads\iris.csv")
iris["setosa"] = iris.Species.map({"setosa" : 1,"versicolor":0, "virginica" : 0})
#print(pd.get_dummies(iris.Species,prefix = "Species"))
#iris['cum_sum'] = iris["Sepal.Length"].cumsum()
#iris = pd.concat(iris, iris['cum sum'], axis=1)
students = pd.DataFrame({'Names': ['John','Mary','Henry','Augustus','Kenny'],
                         'Zodiac Signs': ['Aquarius','Libra','Gemini','Pisces','Virgo']})

students['flag'] = np.where(students['Names'].isin(['John','Henry']), 'yes', 'no')
iris = iris._get_numeric_data()
print(iris.head(3))

