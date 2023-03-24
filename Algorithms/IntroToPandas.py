import pandas as pd

income = pd.read_csv(r"c:\Users\Administrator\Downloads\income.csv")
income.Y2008 = income.Y2008.astype(float)
#income.columns = income.columns.str.replace('Y' , 'Year ')
income.set_index("Index",inplace = True)
income.reset_index(inplace=True)
#print(income.loc[:,"Index":"Y2008"])

data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"],
                     "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
data.columns = ['Names','Zodiac Signs']
data.rename(columns = {"Names":"Cust_Name"},inplace = True)
#print(income.drop('Index', axis = 1))
print(income[income.Index == "A"])
#print(income)

