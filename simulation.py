# Correct use of slicing with lists
# Correct use of at least one function from itertools

import random
from city import City
import infection
import re


def simulation():
    # simulation_settings = initialize_city()
    # num_simulation_days = simulation_settings[0]
    # num_population = simulation_settings[1]
    # num_medical_staff = simulation_settings[2]
    # num_ppe = simulation_settings[3]

    # default numbers for testing instead of entering input everytime
    num_simulation_days = 100
    num_population = 100
    num_medical_staff = 5
    num_ppe = 200

    # instantiate city object using num_population
    vancouver = City(num_population, num_medical_staff, num_ppe)
    if num_simulation_days != -1:
        run_simulation(num_simulation_days, vancouver)
    else:
        run_full_simulation(vancouver)


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
            num_setting = input("{} (Enter a positive integer)\n".format(input_string[setting]))
            # num_setting = int(input("{} (Enter a positive integer)\n".format(input_string[setting])))
            if not bool(re.match(r"^\d+$", num_setting)):
                raise ValueError('This is not a valid input.')
        except ValueError:
            print("Error. Please enter a valid positive integer.")
    return num_setting


# def print_person_stats(person_obj):
#     print("HP:{}, Infected %: {:.2f}, Recovery %: {:.2f}, Infected?: {}, Recovered?: {}, Medical Assist?: {}".format(
#         person_obj.get_hp(), person_obj.get_prob_infected(), person_obj.get_prob_recovery(), person_obj.is_infected(),
#         person_obj.is_recovered(), person_obj.is_medical_assisted()))

def print_person_stats(city_obj):
    city_citizens_list = city_obj.get_citizens()
    # infected_list = [citizen for citizen in city_citizens_list if citizen.is_infected()]
    infected_list = [citizen for citizen in city_citizens_list]
    for person_obj in infected_list:
        print(
            "HP:{}, Infected %: {:.2f}, Recovery %: {:.2f}, Infected?: {}, Recovered?: {}, Medical Assist?: {}, "
            "Deceased: {}".format(
                person_obj.get_hp(), person_obj.get_prob_infected(), person_obj.get_prob_recovery(),
                person_obj.is_infected(),
                person_obj.is_recovered(), person_obj.is_medical_assisted(), person_obj.is_deceased()))


# FUNCTION DECORATOR
def multiple_iterations(func):
    def wrapper(num_iterations, *args, **kwargs):
        for i in range(num_iterations):
            func(i, *args, **kwargs)

    return wrapper


@multiple_iterations
def run_simulation(day_number, city):
    infection.medical_assist(city)
    change_recovered(city)
    change_infected(city)
    infection.calculate_hp(city)
    infection.calculate_ppe(city)
    stats = calculate_statistics(city)
    print("----- Day {} -----".format(day_number + 1))
    infection.print_statistics(stats)
    print_person_stats(city)


# lists for plotting
#     day_counter.append(day + 1)
#     daily_stats.append(stats[0])
# plot_statistics(day_counter, daily_stats)


def run_full_simulation(city_obj):
    num_days = 0
    while city_obj.num_deceased <= city_obj.num_population or city_obj.num_recovered <= city_obj.num_population:
        change_infected(city_obj)
        change_recovered(city_obj)
        infection.calculate_hp(city_obj)
        infection.calculate_ppe(city_obj)
        stats = calculate_statistics(city_obj)
        # infection.print_statistics(stats, num_days)
        num_days = num_days + 1


def change_infected(city_obj):
    general_infected_rate = round(random.uniform(0.0, 0.5), 2)
    city_citizens_list = city_obj.get_citizens()
    for citizen in city_citizens_list:
        if citizen.get_prob_infected() >= general_infected_rate:
            individual_infected_rate = round(random.uniform(0.0, 0.4), 2)
            if citizen.get_prob_infected() >= individual_infected_rate and not citizen.is_infected() \
                    and not citizen.is_recovered():
                citizen.set_infected()


def change_recovered(city_obj):
    general_recovered_rate = round(random.uniform(0.1, 1.0), 2)
    city_citizens_list = city_obj.get_citizens()
    for citizen in city_citizens_list:
        if citizen.is_infected() and not citizen.is_deceased() and citizen.get_prob_recovery() >= general_recovered_rate:
            individual_recovered_rate = round(random.uniform(0.1, 0.8), 2)
            if citizen.get_prob_recovery() >= individual_recovered_rate:
                citizen.set_recovered()


def calculate_statistics(city_obj):
    city_citizens_list = city_obj.get_citizens()
    count_infected = 0
    count_recovered = 0
    count_deceased = 0

    for citizen in city_citizens_list:
        if citizen.is_infected():
            count_infected = count_infected + 1
        elif citizen.is_recovered():
            count_recovered = count_recovered + 1
        elif citizen.is_deceased():
            count_deceased = count_deceased + 1

    count_healthy = city_obj.get_num_population() + city_obj.get_num_medical_staff() \
                    - count_deceased - count_recovered - count_infected

    return count_infected, count_recovered, count_deceased, count_healthy


def main():
    simulation()


if __name__ == "__main__":
    main()
