import pandas as pd
import xlrd

# Assign spreadsheet filename to `file`
file = 'excel_test.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: dfl
df1 = xl.parse('Tabelle1')

#print(df1)

#for i in df1:
#    print(df1[i])

#print(df1['Nummer'])

print(df1.get_value())
