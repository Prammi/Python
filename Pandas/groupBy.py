import pandas as pd
import numpy as np

person=pd.read_json('./Pandas/Data/personsData.json')
country=pd.read_json('./Pandas/Data/countryCodes.json')

# print(person)
# print(country)

print("*"*50 + " GROUP By " + "*"*50 )
temp =pd.merge(person,country ,left_on="countryCode",right_on="countryCode",how="inner",sort=["firstName","lastName"])
result1=temp.groupby(temp["countryName"])["weight"].sum()
print(result1)
print("\n")

result2=temp.groupby(temp["countryName"])["weight"].mean()
print(result2)
print("\n")


result3=temp.groupby(["countryName"]).agg({'weight':'mean','height':'sum'})
print(result3)
print("\n")
# basically same 
resultss=temp.groupby(temp["countryName"]).agg({'weight':'mean','height':'sum'})
print(resultss)
print("\n")



result4=temp.groupby(["countryName","firstName"]).agg({'weight':'mean','height':'sum'})
print(result4)
print("\n")
