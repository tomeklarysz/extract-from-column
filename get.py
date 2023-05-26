import pandas as pd

data = pd.read_excel('Employee Sample Data.xlsx') # reading excel file which has one sheet,
# if your file has more than one, put in brackets ('Employee Sample Data.xlsx', sheet_name = ) and after equal sign number of the sheet

df = pd.DataFrame(data) # data frame

# if you want to see all columns in data sheet
'''for col in data.columns:
    print(col)'''

# important!! -> it's case sensitive, type carefully with big letters 
name = input("Enter full name: ") # which guy we want to check
column = input("What information do you want: ") # which thing of this guy we want to check

df2 = df.loc[df["Full Name"] == name, column] # second data frame with things we are interested in
#print(df2)
print(df2.item()) # exact thing we wanted
