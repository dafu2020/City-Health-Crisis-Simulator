# Correct use of slicing with lists
# Correct use of at least one function from itertools

import random
import city
import infection


def simulation():
    # simulation_settings = initialize_city()
    # num_simulation_days = simulation_settings[0]
    # num_population = simulation_settings[1]
    # num_medical_staff = simulation_settings[2]
    # num_ppe = simulation_settings[3]

    # default numbers for testing instead of entering input everytime
    num_simulation_days = 5
    num_population = 10
    num_medical_staff = 3
    num_ppe = 200

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


def run_simulation(num_simulation_days, city_obj):
    # run simulation for X days
    if num_simulation_days != -1:
        for day in range(num_simulation_days):
            change_infected(city_obj)
            # change_recovered(city_obj)
            # infection.calculate_hp(city_obj)
            # infection.calculate_ppe(city_obj)
            # stats = calculate_statistics(city_obj)
            # infection.print_statistics(stats, day)

    # full simulation
    # else:
    #     num_days = 0
    #     while city_obj.num_deceased <= city_obj.num_population or city_obj.num_recovered <= city_obj.num_population:
    #         change_infected(city_obj)
    #         change_recovered(city_obj)
    #         infection.calculate_hp(city_obj)
    #         infection.calculate_ppe(city_obj)
    #         stats = calculate_statistics(city_obj)
    #         # infection.print_statistics(stats, num_days)
    #         num_days = num_days + 1


def change_infected(city_obj):
    # generates a random number for comparing against prob_infected
    # generates another random number - if both random numbers are higher than prob_infected, they are infected

    general_infected_rate = round(random.uniform(0.0, 1.0), 2)
    print("general infected rate:", general_infected_rate)
    # get list of person objects
    city_citizens_list = city_obj.get_citizens()
    print(len(city_citizens_list))
    for citizen in city_citizens_list:
        if citizen.get_prob_infected() <= general_infected_rate:
            individual_infected_rate = round(random.uniform(0.0, 1.0), 2)
            if citizen.get_prob_infected() <= individual_infected_rate and not citizen.is_infected() \
                    and not citizen.is_recovered():
                citizen.health_shifter()


def change_recovered(city_obj):
    # very similar to change_infected

    general_recovered_rate = random.randint(0, 100)
    city_citizens_list = city_obj.get_citizens()
    for citizen in city_citizens_list:
        if citizen.is_infected():
            if citizen.get_prob_recovered() <= general_recovered_rate:
                individual_recovered_rate = random.randint(0, 100)
                if citizen.get_prob_recovered() <= individual_recovered_rate:
                    citizen.set_recovered()


def calculate_statistics(city_obj):
    city_citizens_list = city_obj.get_citizens() # get list of person objects
    count_infected = 0
    count_recovered = 0
    count_deceased = 0

    for citizen in city_citizens_list:
        if citizen.is_infected():
            count_infected = count_infected + 1
        if citizen.is_recovered():
            count_recovered = count_recovered + 1
        if citizen.is_deceased():
            count_deceased = count_deceased + 1

    return count_infected, count_recovered, count_deceased


def main():
    simulation()


if __name__ == "__main__":
    main()
