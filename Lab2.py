def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

   
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calculate_average_temperature(temperatures):
    if not temperatures:
        return None  # Return None if the list is empty
    total_temperature = sum(temperatures)
    average_temperature = total_temperature / len(temperatures)
    return float(average_temperature)  # Ensure average_temperature is a float
          
def get_user_input():
    user_input = input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    numbers = list(map(float, user_input.split(",")))
    return numbers

def find_min_max_temperature():
    temperature = input("Enter temperature separated by commas: ")
    temperature_list = [float(temperature) for temperature in temperature.split(",")]
    return min(temperature_list), max(temperature_list)


def sort_temperatures(temperatures):
    sorted_temperatures = sorted(temperatures)
    return sorted_temperatures

def calc_median_temperature():
    sorted_temperatures = sorted(temperatures)
    n = len(sorted_temperatures)
    
    if n == 0:
        return None  # Return None if the list is empty

    if n % 2 == 1:
        # If the number of temperatures is odd
        median_index = n // 2
        median_temperature = sorted_temperatures[median_index]
    else:
        # If the number of temperatures is even
        upper_median_index = n // 2
        lower_median_index = upper_median_index - 1
        median_temperature = (sorted_temperatures[lower_median_index] + sorted_temperatures[upper_median_index]) / 2
    
    return median_temperature
    
if __name__ == "__main__":
        main()
