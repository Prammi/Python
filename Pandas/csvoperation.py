import pandas as pd
import numpy as np

print("*"*50 + " CSV " + "*"*50 )
df = pd.read_csv("./Pandas/Data/customers.csv")
print(df.columns)
print(df.describe())
# print(df.info())
print(df.size)
print(df.head())

print("*"*50 + " PARQUET " + "*"*50 )
results =pd.read_parquet("./Pandas/Data/results.parquet")
print(results.columns)
print(results.describe())
# print(results.info())
print(results.size) #None
print(results.head())

print("*"*50 + " JSON " + "*"*50 )
results =pd.read_json("./Pandas/Data/sampleJson.json")
print(results.columns)
print(results.describe())
# print(results.info())
print(results.size)
print(results.head())


# print("*"*50 + " EXCEL " + "*"*50 )
# results =pd.read_excel("./Pandas/Data/olympics-data.xlsx",sheet_name="results")
# print(results.columns)
# print(results.describe())
# # print(results.info())
# print(results.size)
# print(results)
# print(results.head())


print("*"*50 + " CSV " + "*"*50 )
df = pd.read_csv("./Pandas/Data/customers.csv")
print(df.columns)
print(df.describe())
print(df.size)
print(df)
print(df.sample(5))


# LOC example 
print(df.loc[0]) #loq[] single row
print(df.loc[[0,1,2]])#multiple row
print(df.loc[[0,1,2],["Customer Id"]]) #multiple row with columns 
print(df.loc[0:10,["Customer Id","First Name"]])#multiple rows and cols 

df.loc[0,"First Name"]="Pramod Raikal"

#ILOC - colums are based on index 
print(df.iloc[0:10,[0,1,2]])#multiple rows and cols  

print(df["First Name"])
# iloc [a,b ] b is exclusive 
#loc [a,b ] b is inclusive

print(df.sort_values(["First Name","Last Name"],ascending=True))
print(df.sort_values(["First Name","Last Name"],ascending=[0,1]))
print(df.sort_values(["First Name","Last Name","Email"],ascending=[0,1,1]))


for i,row in df.iterrows():
    print(f"index is {i}- the first name is {row["First Name"]}; email is {row["Email"]}")
    
    
    
print("*"*50 + " FILETRING DATA " + "*"*50 )
results =pd.read_json("./Pandas/Data/sampleJson.json")
print(results)
print(results.loc[[0,1,2],["Name","Department"]]) # traditional Loc
print(results.loc[results["Salary"]>75000])
print(results.loc[results["Salary"]<75000,["Name","Department"]])
print(results.loc[(results["Salary"]<75000) &(results["EmployeeID"]<125),["Name","Department","Salary","EmployeeID"]])
print(results.loc[(results["Salary"]<75000) &(results["EmployeeID"]<125)& (results["Department"].str.contains("Human")),["Name","Department","Salary","EmployeeID"]])
print(results.loc[(results["Salary"]<75000) &(results["EmployeeID"]<125)& (results["Department"].str.contains("Human",case=False) ),["Name","Department","Salary","EmployeeID"]])
print(results.loc[(results["Salary"]<75000) &(results["EmployeeID"]<125)& (results["Department"].str.contains("Human|Finance",case=False) ),["Name","Department","Salary","EmployeeID"]])

print(results.loc[results["Department"].isin(["Finance","Sales"]),["Name","Department","Salary","EmployeeID"]])


print("*"*50 + " QUERYING " + "*"*50 )

print(results.query("EmployeeID<125  and Department.str.contains('Human|Sales')",engine="python")[["Name","Department","Salary","EmployeeID"]])
#or
temp=results.query("EmployeeID<125  and Department.str.contains('Human|Sales')",engine="python")
print(temp.filter(items=["Name","Department","Salary","EmployeeID"]))


# or
mask_salary = results["Salary"] < 75000
mask_id = results["EmployeeID"] < 125
mask_dept_human = results["Department"].str.contains("Human", case=False)
mask_dept_human_finance = results["Department"].str.contains("Human|Finance", case=False)

# Apply masks
print(results.loc[mask_salary & mask_id & mask_dept_human_finance, ["Name", "Department", "Salary", "EmployeeID"]])   


print("*"*50 + " ADDING  REMOVING COL " + "*"*50 )
condition = results["EmployeeID"] % 2 == 0
temp = np.where(
    condition,
    np.random.randint(10000, 50000, size=condition.shape[0]),
    np.random.randint(1000, 10000, size=condition.shape[0])
)

# temp=np.where(results["EmployeeID"]%2==0,np.random.randint(10000,50000),np.random.randint(1000,10000))
results["NewSalary"]=temp
print(results)    

# results1=results.drop(columns=["Salary"]) 
# or
results.drop(columns=["Salary"],inplace=True)  
print(results)

results["Tax"]=results["NewSalary"]*.30
print(results)

results.rename(columns={    'NewSalary':'Salary'},inplace=True)
print(results)

results["First Name"]=results["Name"].str.split(" ").str[0]
results["Last Name"]=results["Name"].str.split(" ").str[1]
print(results)

# print(results.query("`First Name`.str.contains('Sneha|Raj',case=False)",engine="python"))

# results["Year"]=results["JoiningDate"].str.split("-").str[0].astype(np.int16)
# results["Month"]=results["JoiningDate"].str.split("-").str[1].astype(np.int16)  
# print(results.query("`Year` >2020 and `Month`<10",engine="python"))

# or

results["JoiningDate"]=pd.to_datetime(results["JoiningDate"])
results["Year"]=results["JoiningDate"].dt.year
results["Month"]=results["JoiningDate"].dt.month
print(results.query("`Year` >2020 and `Month`<10",engine="python"))


print("*"*50 + " CLASSIFYING  " + "*"*50 )
results["Range"]=results["Salary"].apply(lambda x: "Low Paid" if x <10000 else ("Average Paid" if x<25000 else "OverPaid" ))
results["TaxRange"]=results["Tax"].apply(lambda x: "Low Tax" if x <10000 else "High Tax")

print(results.filter(items=["Name","Tax","TaxRange"]) )


# or 
def TaxRange(row):
    if row["Tax"]<10000:
        return "Low Taz"
    else:
        return "High Taz"

results["AltTaxRange"]=results.apply(TaxRange,axis=1)
print(results)