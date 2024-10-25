#Python file for testing flow options
#Flow 1: Let's see if we can first give a number to interpolate and then select the options to what
#type of interpolation we want to visualize

from scipy.interpolate import Akima1DInterpolator

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [33, 30, 29, 30, 27, 28, 29, 32, 27, 28]

def get_incognito_hour():
    while True:
        try:
            incognito_hour = float(input("Enter an hour between 1 and 10: "))
            if 1 <= incognito_hour <= 10:
                return incognito_hour
            else:
                print("The hour must be between 1 and 10. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


print("Result:", get_incognito_hour())
# Call the function and store the value in incognito_hour
incognito_hour = get_incognito_hour()

def main():


 if __name__ == '__main__':
    main()