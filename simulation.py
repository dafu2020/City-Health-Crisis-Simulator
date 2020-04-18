import random
from city import City
import infection
import re
import itertools
import api


def simulation():
    """ Run the simulation program.

    :precondition: no precondition
    :postcondition: the simulation is executed properly
    """
    simulation_settings = initialize_city()
    num_simulation_days = simulation_settings[0]
    num_population = simulation_settings[1]
    num_medical_staff = simulation_settings[2]
    num_ppe = simulation_settings[3]

    # instantiate city object using num_population
    vancouver = City(num_population, num_medical_staff, num_ppe)
    if num_simulation_days != -1:
        run_simulation(num_simulation_days, vancouver)
    else:
        run_full_simulation(vancouver)
    confirmed_cases_in_canada = api.get_canada_statistic()
    api.get_latest_statistic(confirmed_cases_in_canada)


def initialize_city() -> (int, int, int, int):
    """ Get the user's input in order to initialize the city.

    :precondition: no precondition
    :postcondition: the values entered by the user are returned as integers
    :return: tuple of 4 integers representing the number of simulated days, population, medical staff size, and number
    of ppe
    """
    num_simulation_days = input_simulation_days()
    num_population = input_settings("population")
    num_medical_staff = input_settings("staff")
    num_ppe = input_settings("ppe")
    return num_simulation_days, num_population, num_medical_staff, num_ppe


def input_simulation_days() -> int:
    """ Get the user's input for the simulation type and the amount of days to simulate.

    :precondition: no precondition
    :postcondition: the user's input is validated and returned correctly as an integer
    :return: an integer representing the number of days to simulate
    """
    print("Welcome to the City Health Crisis Simulator. The program attempts to model the operation of a hospital "
          "during the COVID-19 crisis and evaluates the number of people that will become infected over time.")
    simulation_type = input("To begin, select the type of simulation:\n1) Simulation for a defined number of days\n"
                            "2) Full simulation until the end\n")
    while simulation_type.strip() != "1" and simulation_type.strip() != "2":
        simulation_type = input("Invalid selection. Select the type of simulation:\n1) Simulation for a defined number "
                                "of days\n2) Full simulation until the end\n")
    if simulation_type == "1":
        num_simulation_days = input_settings("days")
    else:
        # use -1 to signify that a full simulation is requested
        num_simulation_days = -1
    return num_simulation_days


def input_settings(setting: str) -> int:
    """ Get the user's input for the setting.

    :param setting: a string representing the setting
    :precondition: setting is a string that is either "days", "population", "staff", or "ppe"
    :postcondition: the setting is validated and the user's input is returned as an integer
    :return: an integer
    """
    input_string = {"days": "How many days to simulate? ",
                    "population": "How many people live in the city? ",
                    "staff": "In addition to the population, how many medical staff members in the city? ",
                    "ppe": "How many Personal Protective Equipment (PPE) in the city? "}
    num_setting = 0
    while num_setting <= 0:
        try:
            num_setting = int(input("{} (Enter a positive integer)\n".format(input_string[setting])))
            # USE OF AT LEAST ONE REGULAR EXPRESSION, for pure numbers only
            if not bool(re.match(r"^\d+$", str(num_setting))):
                print('Invalid input. Please try again.')
        except ValueError:
            print("Error. Please enter a valid positive integer.")
    return num_setting


def print_person_stats(city_obj: object):
    """ Print the statistics of the city's people in critical condition.

    :param city_obj: a city object
    :precondition: city_obj is a well-formed city object
    :postcondition: the statistics are properly printed
    """
    city_citizens_list = city_obj.get_citizens()
    infected_list = [citizen for citizen in city_citizens_list if citizen.is_infected() and citizen.get_hp() < 3]
    if infected_list:
        print("People in critical condition:")
        # ENUMERATE FUNCTION
        for index, person_obj in enumerate(infected_list, 1):
            print(
                "{}: HP:{}, Medical Assist?: {}, Deceased: {}".format(
                    index, person_obj.get_hp(), person_obj.is_medical_assisted(), person_obj.is_deceased()))


# FUNCTION DECORATOR
def multiple_iterations(func):
    """ Decorate the run_simulation function.

    :param func: the function to decorate
    :precondition: run_simulation is the function passed to this function
    :postcondition: the wrapper is sucessfully returned
    :return: the function wrapper to iterate
    """
    def wrapper(num_iterations, *args, **kwargs):
        # ITERTOOLS FUNCTION
        for i in itertools.count(0):
            func(i, *args, **kwargs)
            if i >= num_iterations - 1:
                break
    return wrapper


@multiple_iterations
def run_simulation(day_number: int, city: object):
    """ Run the simulation for day_number amount of days.

    :param day_number: a number of days to simulate
    :param city: a city object
    :precondition: day_number is a positive integer and city is a well-formed city object
    :postcondition: the simulation is properly run for the day_number amount of days
    """
    daily_calculations(city)
    stats = calculate_statistics(city)
    print("----- Day {} -----".format(day_number + 1))
    infection.print_statistics(stats)
    print_person_stats(city)


def daily_calculations(city_obj: object):
    """ Calculate the daily change of infected and recovered.

    :param city_obj: a city object
    :precondition: city_obj is a well-formed city object
    :postcondition: the daily calculations are properly executed
    """
    infection.medical_assist(city_obj)
    change_recovered(city_obj)
    change_infected(city_obj)
    infection.calculate_hp(city_obj)
    infection.calculate_ppe(city_obj)


def run_full_simulation(city_obj: object):
    """ Run a full simulation of the infection.

    :param city_obj: a city object
    :precondition: city_obj is a well-formed city object
    :postcondition: a full simulation is properly executed
    """
    num_days = 1
    num_recovered = calculate_statistics(city_obj)[1]
    num_deceased = calculate_statistics(city_obj)[2]
    num_healthy = calculate_statistics(city_obj)[3]
    while num_recovered + num_deceased < city_obj.get_num_total_population():
        # if there is just one healthy person left, there is nobody to infect them
        if num_healthy == 1 and num_recovered + num_deceased == city_obj.get_num_total_population():
            break
        daily_calculations(city_obj)
        stats = calculate_statistics(city_obj)
        print("----- Day {} -----".format(num_days + 1))
        infection.print_statistics(stats)
        num_days = num_days + 1
        num_recovered = calculate_statistics(city_obj)[1]
        num_deceased = calculate_statistics(city_obj)[2]
        num_healthy = calculate_statistics(city_obj)[3]


def change_infected(city_obj: object):
    """ Execute the daily change of infected population.

    :param city_obj: a city object
    :precondition: city_obj is a well-formed city object
    :postcondition: the daily change of infected is properly calculated
    """
    general_infected_rate = round(random.uniform(0.0, 0.5), 2)
    city_citizens_list = city_obj.get_citizens()
    for citizen in city_citizens_list:
        if citizen.get_prob_infected() >= general_infected_rate:
            individual_infected_rate = round(random.uniform(0.0, 0.4), 2)
            if citizen.get_prob_infected() >= individual_infected_rate and not citizen.is_infected() \
                    and not citizen.is_recovered():
                citizen.set_infected()


def change_recovered(city_obj: object):
    """ Execute the daily change of recovered population.

    :param city_obj: a city object
    :precondition: city_obj is a well-formed city object
    :postcondition: the daily change of recovered is properly calculated
    """
    general_recovered_rate = round(random.uniform(0.1, 1.0), 2)
    city_citizens_list = city_obj.get_citizens()
    for citizen in city_citizens_list:
        if citizen.is_infected() and not citizen.is_deceased() and \
                citizen.get_prob_recovery() >= general_recovered_rate:
            individual_recovered_rate = round(random.uniform(0.1, 0.8), 2)
            if citizen.get_prob_recovery() >= individual_recovered_rate:
                citizen.set_recovered()


def calculate_statistics(city_obj: object) -> (int, int, int, int):
    """ Calculate the city's statistics.

    :param city_obj: a city object
    :precondition: city_object is a well-formed city object
    :postcondition: the statistics are properly calculated and returned
    :return: a tuple containing four integers representing the number of infected, recovered, deceased, and healthy
    people in the city
    """
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
    count_healthy = city_obj.get_num_total_population() - count_deceased - count_recovered - count_infected
    return count_infected, count_recovered, count_deceased, count_healthy


def main():
    """
    Drive the program.
    """
    simulation()


if __name__ == "__main__":
    main()
