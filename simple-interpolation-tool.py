#Python file created as a beta version for the interpolation tool
#1. Upload csv- excell file
#2. Read and format excell file
#3. ask user for type of interpolation
#4. ask user for interpolation data input
#5. convert data to interpolate into logartithms
#6. operate !
#7. convert data to exp scale
#8. create graph
#9. show data and graph

#Imports
import pandas as pd

#testing
print('Script interpolator_script.py')

#STEPS 1 AND 2 -------------------------------------------------------------------------------
#Upload excel file
file_path_excel =r"C:\Users\VPECOS\Desktop\documentos sara\PRACTICAS\datos.xlsx"
df_excel = pd.read_excel(file_path_excel)#call to excel file
print(df_excel.head)
#Upload csv file
file_path_csv = r'C:\Users\VPECOS\Desktop\documentos sara\PRACTICAS\datos.csv' ####REMEMBER TO UPLOAD CORRECT CSV FILE
df = pd.read_csv(file_path_csv)
print("CSV file loaded successfully.")
print(df.head())
# PRINT data in list format
column1 = list(df['X'])
column2 = list(df['Y'])
#test the script
energy = column1  # Energy values of the distribution
values = column2  # Variable values of the distribution
#print results
print(f'Energy: {energy}')
print (f'Values: {values}')
# Data Read and listed --------------------------------------------------------------------------------------



