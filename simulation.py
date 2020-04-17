import random
# import city

# Correct use of slicing with lists
# Syntactic sugar: at least one list comprehension and one dictionary comprehension

def simulation():
    # ask for user input
    simulation_settings = initialize_city()
    num_simulation_days = simulation_settings[0]
    num_population = simulation_settings[1]
    num_medical_staff = simulation_settings[2]
    num_ppe = simulation_settings[3]

    # instantiate city object using num_population
    vancouver = city.City(num_population, num_medical_staff, num_ppe)

    run_simulation(num_simulation_days, vancouver)


def initialize_city() -> (int, int, int, int):
    # ask for user input
    # num_simulation_days is a positive integer >= 1 or -1 if full simulation selected
    # handle exceptions for invalid num_simulation_days
    # handle exceptions for all inputs (values can't be negative and any other inputs that may be invalid)
    # returns tuple (num_simulation_days, num_population, num_medical_staff, num_ppe)

    num_simulation_days = input_simulation_days()
    num_population = input_settings("population")
    num_medical_staff = input_settings("staff")
    num_ppe = input_settings("ppe")
    return num_simulation_days, num_population, num_medical_staff, num_ppe


def input_simulation_days():
    simulation_type = input("Select the type of simulation:\n1) Simulation for a defined number of days\n2) Full "
                            "simulation until the end\n")
    while simulation_type.strip() != "1" and simulation_type.strip() != "2":
        simulation_type = input("Invalid selection. Select the type of simulation:\n1) Simulation for a defined number "
                                "of days\n2) Full simulation until the end\n")
    if simulation_type == "1":
        num_simulation_days = input_settings("days")
    else:
        num_simulation_days = -1
    return num_simulation_days


def input_settings(setting):
    input_string = {"days": "How many days to simulate? ",
     "population": "How many people live in the city? ",
     "staff": "How many medical staff members in the city? ",
     "ppe": "How many Personal Protective Equipment (PPE) in the city? "}
    num_setting = 0
    while num_setting <= 0:
        try:
            num_setting = int(input("{} (Enter a positive integer)\n".format(input_string[setting])))
        except ValueError:
            print("Error. Please enter a valid positive integer.")
    return num_setting

# def run_simulation(num_simulation_days, city):
#     # run simulation for X days
#     if num_simulation_days != -1:
#         for day in range(num_simulation_days):
#             change_infected(city)
#             change_recovered(city)
#             calculate_hp(city)
#             calculate_ppe(city)
#             stats = calculate_statistics(city)
#             print_statistics(stats, day)
#
#     # full simulation
#     else:
#         num_days = 0
#         while city.num_deceased <= city.num_population or city.num_recovered <= city.num_population:
#             change_infected(city)
#             change_recovered(city)
#             calculate_hp(city)
#             calculate_ppe(city)
#             stats = calculate_statistics(city)
#             print_statistics(stats, num_days)
#             num_days = num_days + 1
#
#
# def change_infected(city):
#     # generates a random number for comparing against prob_infected
#     # generates another random number - if both random numbers are higher than prob_infected, they are infected
#
#     general_infected_rate = random.randint(0, 100)  # I made up the numbers
#     city_citizens_list = city.getCitizens() # get list of person objects
#     for citizen in city_citizens_list:
#         if citizen.get_prob_infected <= general_infected_rate:
#             individual_infected_rate = random.randint(0, 100)  # I made up the numbers
#             if citizen.get_prob_infected <= individual_infected_rate:
#                 citizen.set_infected() # sets infected attribute - if already infected, do nothing, else change to True
#
# def change_recovered(city):
#     # very similar to change_infected
#
#     general_recovered_rate = random.randint(0, 100)
#     city_citizens_list = city.getCitizens()
#     for citizen in city_citizens_list:
#         if citizen.is_infected():
#             if citizen.get_prob_recovered <= general_recovered_rate:
#                 individual_recovered_rate = random.randint(0, 100)
#                 if citizen.get_prob_recovered <= individual_recovered_rate:
#                     citizen.set_recovered()
#
#
# def calculate_statistics(city):
#     city_citizens_list = city.getCitizens() # get list of person objects
#     count_infected = 0
#     count_recovered = 0
#     count_deceased = 0
#
#     for citizen in city_citizens_list:
#         if citizen.is_infected():
#             count_infected = count_infected + 1
#         if citizen.is_recovered():
#             count_recovered = count_recovered + 1
#         if citizen.is_deceased():
#             count_deceased = count_deceased + 1
#
#     return (count_infected, count_recovered, count_deceased)


def main():
    initialize_city()


if __name__ == "__main__":
    main()
