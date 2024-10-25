##file to store parts of code when code starts failing

def akima_interpolation(incognito_hour):
    interpolator = Akima1DInterpolator(incognito_hour, temperature)
    interpolated_value = interpolator(incognito_hour)
    return f"Akima interpolation result for hour {incognito_hour}:{interpolated_value}"

def linear_interpolation():
    # Placeholder for linear interpolation logic
    return "Linear interpolation selected."

#------------------------------------------------------------
def akima_interpolation():
    return f"Akima interpolation result for hour"


def choose_interpolation():
    while True:
        print("Choose an interpolation method:")
        print("1. Akima Interpolation")
        print("2. Linear Interpolation")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return akima_interpolation(get_incognito_hour)
        elif choice == "2":
            return linear_interpolation()
        else:
            print("Invalid choice. Please enter 1 or 2.")
result = choose_interpolation()


print("The incognito hour is:", incognito_hour)
result = akima_interpolation(incognito_hour)
