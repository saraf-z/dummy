#1. Corrected the main flow logic for clarity.
#2. Adjusted the clean_data function to properly return the cleaned DataFrame without printing incorrect messages inside the loop.
#3. Fixed column names and variable names for consistency.
#4. Corrected the access of DataFrame columns in the main function.
#5. Fixed printing format for some outputs for clarity.

import math
import numpy as np
import pandas as pd
from scipy.interpolate import Akima1DInterpolator
from math import log, exp

# Function to read a CSV file
def read_csv_file(file_path_csv):
    """ This function reads a CSV file using pandas and returns the DataFrame."""
    try:
        df = pd.read_csv(file_path_csv)
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path_csv} was not found.")
        return None


# Function to clean the data
def clean_data(df):
    """This function cleans unused data by removing rows where the value is less than or equal to 0."""
    # Extract columns 'Energy[keV]' and 'Fluence_rate [cm^-2s^-1]' from the DataFrame
    energy = df['Energy[keV]']
    values = df['Fluence_rate [cm^-2s^-1]']

    # Filter out rows where values are less than or equal to 0
    clean_df = df[(values > 0)].copy()
    clean_df.reset_index(drop=True, inplace=True)
    return clean_df


# Logarithmic transformation: calculate logarithmic values of energy and values
def take_logarithm(clean_energies, clean_values, interpolated_energy):
    """Calculate the logarithm of a set of values."""
    log_energy = [log(i) for i in clean_energies]
    log_values = [log(e) for e in clean_values]
    log_interpolated_energy = log(interpolated_energy)
    return log_energy, log_values, log_interpolated_energy


# Function to select the interpolation method
def select_interpolation():
    options = {
        1: "lineal",
        2: "Akima"
    }
    print("Select interpolation method")
    for key, value in options.items():
        print(f"{key}: {value}")
    while True:
        try:
            selected_method = int(input("Select method (1 or 2): "))
            if selected_method in options:
                print(f"Selected method: {options[selected_method]}")
                return options[selected_method]
            else:
                print("Unavailable method, try again")
        except ValueError:
            print("Invalid input, try again")


# Interpolation functions
def log_linear_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point."""
    log_interpolated_value = np.interp(log_interpolated_energy, log_energy, log_values)
    return log_interpolated_value


def log_akima_interpolation(log_energy, log_values, log_interpolated_energy):
    """Interpolate the value at the given energy point using Akima interpolation."""
    akima_interpolator = Akima1DInterpolator(log_energy, log_values)
    log_interpolated_value_akima = akima_interpolator(log_interpolated_energy)
    return log_interpolated_value_akima


# Function to convert logarithmic values back to original values
def log_to_value(log_interpolated_value, log_interpolated_value_akima):
    interpolated_value = math.exp(log_interpolated_value)
    interpolated_value_akima = math.exp(log_interpolated_value_akima)
    return interpolated_value, interpolated_value_akima


def main():
    print('Script interpolator_functions.py')

    # Step 1: Read file
    file_path = 'n60.csv'
    df = read_csv_file(file_path)

    # Step 2: Clean data
    if df is not None:
        print("CSV file read, cleaning data...")
        clean_df = clean_data(df)
        print("Cleaned data:")
        print(clean_df)
    else:
        print("Unable to read CSV file.")
        return

    # Step 3: Ask user for the value of the interpolated_energy
    while True:
        try:
            interpolated_energy = float(
                input("Enter the energy point you want to interpolate in a range of 20.0 to 400: "))
            if interpolated_energy < 20 or interpolated_energy > 400:
                print("Invalid input, interpolated energy must be between 20 and 400. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input, enter a numeric value.")

    # Step 4: Call the take_logarithm function with user input and clean data
    clean_energies = clean_df['Energy[keV]'].tolist()
    clean_values = clean_df['Fluence_rate [cm^-2s^-1]'].tolist()

    log_energy, log_values, log_interpolated_energy = take_logarithm(clean_energies, clean_values, interpolated_energy)
    print("Logarithmic values:", log_energy, log_values, log_interpolated_energy)

    # Step 5: Select interpolation method
    selected_method = select_interpolation()

    # Step 6: Perform interpolation based on the selected method
    if selected_method == "lineal":
        log_interpolated_value = log_linear_interpolation(log_energy, log_values, log_interpolated_energy)
        interpolated_value = math.exp(log_interpolated_value)
        print(f"Interpolated value using linear method: {interpolated_value}")
    elif selected_method == "Akima":
        log_interpolated_value_akima = log_akima_interpolation(log_energy, log_values, log_interpolated_energy)
        interpolated_value_akima = math.exp(log_interpolated_value_akima)
        print(f"Interpolated value using Akima method: {interpolated_value_akima}")


if __name__ == "__main__":
    main()