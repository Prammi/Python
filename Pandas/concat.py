import pandas as pd
import numpy as np

person=pd.read_json('./Pandas/Data/personsData.json')
country=pd.read_json('./Pandas/Data/countryCodes.json')

# print(person)
# print(country)

print("*"*50 + " MERGE " + "*"*50 )
temp =pd.merge(person,country ,left_on="countryCode",right_on="countryCode",how="inner",sort=["firstName","lastName"])
# print(temp) # check the col names
print(temp.loc[:,["firstName","lastName","countryName"]])
print("\n")
temp=pd.merge(person,country,on="countryCode",how="inner").loc[:,["firstName","lastName","countryName"]]
print(temp)

print("*"*50 + " CONCAT " + "*"*50 )
print("\n")

india=person.query("`countryCode`=='IN'")
australia=person.query("`countryCode`=='AU'")
print(pd.concat([india,australia]))

print("*"*50 + " ISNAN " + "*"*50 )
print("\n")
temp =pd.merge(person,country ,left_on="countryCode",right_on="countryCode",how="inner",sort=["firstName","lastName"])
temp.loc[[0,1,3],"height"]=np.nan
print(temp)
print("\n")
temp["height"]=temp["height"].fillna(temp["height"].mean())
print(temp)
print("\n")
temp.loc[[0,1,3],"height"]=np.nan
temp["height"]=temp["height"].interpolate(limit_direction='both')
print(temp)
print("\n")

temp.loc[[0,1,3],"height"]=np.nan
print(temp["height"].isna())
print(temp[temp["height"].isna()])
print("\n")
print(temp[temp["height"].notna()])
print("\n")

print("*"*50 + " VALUE COUNTS " + "*"*50 )
print(temp["countryName"].value_counts())
temp2=temp.query("countryName =='India'")[["weight"]]
print(temp2.value_counts())







