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
from scipy.interpolate import interp1d

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
#STEP 3 ------------------------------------------------------------------------
##3. ask user for type of interpolation
print("Select the interpolation type:")
print("1 - Linear")
print("2 - Quadratic")
print("3 - Cubic")
print("4 - Akima")
interpolation_type = input("Enter the number corresponding to the interpolation type: ")
 #Define interpolation function based on selection
def select_interpolation(interpolation_type, column1, column2):
 try:
     if interpolation_type == '1':
        interp_function = interp1d(column1, column2, kind='linear')
        print("Linear interpolation selected.")
     elif interpolation_type == '2':
        interp_function = interp1d(column1, column2, kind='quadratic')
        print("Quadratic interpolation selected.")
     elif interpolation_type == '3':
        interp_function = interp1d(column1, column2, kind='cubic')
        print("Cubic interpolation selected.")
     elif interpolation_type == '4':
         interp_function = interp1d(column1, column2, kind='Akima')
         print ("Akima interpolation selected.")
     else:
          print("Invalid selection. Please enter 1, 2, 3 or 4")
          exit()
 except Exception as e:
    print(f"An error occurred: {e}")

#STEP 4 ---------------------------------------------------------------------------------------------------
###4. ask user for interpolation data input
while True:
    try:
        x_value = float(input("Enter an X value between 1 and 5 for interpolation: "))
        if 1 <= x_value <= 5:
            break
        else:
                print("Please enter a value between 1 and 5.")
    except ValueError:
     print("Invalid input. Please enter a numeric value.")

print (f'interpolated_energy: {x_value}')
#Value to interpolate will be stored in x_value variable

# Clean data



#STEP 5 -------------------------------------------------------------------------------
#5. convert data to interpolate into logartithms
