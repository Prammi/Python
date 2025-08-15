import pandas as pd
import numpy as np

person=pd.read_json('./Pandas/Data/personsData.json')
country=pd.read_json('./Pandas/Data/countryCodes.json')

# print(person)
# print(country)

print("*"*50 + " GROUP By " + "*"*50 )
temp =pd.merge(person,country ,left_on="countryCode",right_on="countryCode",how="inner",sort=["firstName","lastName"])
print(temp)

pivot=temp.pivot(columns="countryName",index="firstName",values="sports")
print(pivot)
