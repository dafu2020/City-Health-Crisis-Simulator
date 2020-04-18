import random
import pprint
from person import Person


class City:
    def __init__(self, num_population: int, num_medical_staff: int, num_ppe: int) -> None:
        """
        Simulate a City, including population, medical staff, Personal Protective Equipment

        :param num_population: number of population, a positive int
        :param num_medical_staff: number of medical stuff, a positive int
        :param num_ppe: number of Personal Protective Equipment, a positive int
        :raise TypeError: arguments are not integers
        :raise ValueError: arguments are not positive
        :precondition: population, medical_stuff and PPE must be positive integers
        :postcondition: A object that represents the city
        """
        # Check Parameter, Raise an Error if they are not positive or not integer
        check_number(num_population)
        check_number(num_medical_staff)
        check_number(num_ppe)
        self.__num_population = num_population
        self.__medical_staff = num_medical_staff
        self.__num_ppe = num_ppe
        self.__num_infected = 0
        self.__num_deceased = 0
        self.__num_recovered = 0
        self.__city_citizens = []
        self.__daily_decay = random.randint(5, 10)
        # Add the names of all elements into a Set
        self.__all_element_set = set()
        self.update_set()
        # Add Medical Stuff and Person into city_citizens
        self.instantiate_medical_stuff()
        self.instantiate_person()
        # Update number of infected, deceased and recovered
        self.update_num_infected()
        self.update_num_deceased()
        self.update_num_recovered()

    def get_num_population(self) -> int:
        """
        Get Number of Population
        """
        return self.__num_population

    def get_num_medical_staff(self) -> int:
        """
        Get Number of Medical Stuff
        """
        return self.__medical_staff

    def get_num_ppe(self) -> int:
        """
        Get Number of Personal Protective Equipment
        """
        return self.__num_ppe

    def get_citizens(self) -> list:
        """
        Get Citizens
        """
        return self.__city_citizens

    def get_daily_decay(self) -> int:
        """
        Get Daily Decay
        """
        return self.__daily_decay

    def get_num_infected(self) -> int:
        """
        Get Number of Infected
        """
        return self.__num_infected

    def get_num_deceased(self) -> int:
        """
        Get Number of Deceased
        """
        return self.__daily_decay

    def get_num_recovered(self) -> int:
        """
        Get Number of Recovery
        """
        return self.__num_recovered

    def get_all_element_set(self) -> set:
        """
        Get the set that has all elements
        """
        return self.__all_element_set

    def set_num_population(self, new_population: int) -> None:
        """
        Set Number of Population
        """
        check_number(new_population)
        self.__num_population = new_population

    def set_num_medical_stuff(self, new_medical: int) -> None:
        """
        Set Number of Medical Stuff
        """
        check_number(new_medical)
        self.__medical_staff = new_medical

    def set_num_ppe(self, new_ppe: int) -> None:
        """
        Set Number of PPE
        """
        if new_ppe < 0:
            raise ValueError("PPE should be positive.")
        self.__num_ppe = new_ppe

    def set_num_deceased(self, new_deceased: int) -> None:
        """
        Set Number of Deceased
        """
        self.__num_deceased = new_deceased

    def set_num_recovered(self, new_recovered: int) -> None:
        """
        Set Number of Recovered
        """
        self.__num_recovered = new_recovered

    def set_daily_decay(self, new_decay: int) -> None:
        """
        Set Daily Decay
        """
        self.__daily_decay = new_decay

    def instantiate_person(self) -> None:
        """
        Instantiate the Person, and add citizen into 'citizens' list
        """
        for number_person in range(0, self.__num_population):
            # Set Attribute for every person
            person_attribute = generate_attribute()
            prob_infection = person_attribute['prob_infection']
            prob_recovery = person_attribute['prob_recovery']
            initial_hp = person_attribute['initial_hp']
            # Invoke Class Person by Attributes
            person_object = Person(prob_infection, prob_recovery, initial_hp, 'citizen')
            self.__city_citizens.append(person_object)

    def instantiate_medical_stuff(self) -> None:
        """
        Instantiate the Person, and add Medical Stuff into 'citizens' list
        """
        for number_person in range(0, self.__medical_staff):
            person_attribute = generate_attribute()
            prob_infection = person_attribute['prob_infection']
            prob_recovery = person_attribute['prob_recovery']
            initial_hp = person_attribute['initial_hp']
            person_object = Person(prob_infection, prob_recovery, initial_hp, 'medical')
            self.__city_citizens.append(person_object)

    def update_num_infected(self) -> None:
        """
        Update the number of deceased
        """
        for person_object in self.__city_citizens:
            if person_object.is_infected():
                self.__num_infected += 1

    def update_num_deceased(self) -> None:
        """
        Update the number of deceased
        """
        for person_object in self.__city_citizens:
            if person_object.is_deceased():
                self.__num_deceased += 1

    def update_num_recovered(self) -> None:
        """
        Update the number of recovered
        """
        for person_object in self.__city_citizens:
            if person_object.is_recovered():
                self.__num_recovered += 1

    def update_set(self) -> None:
        """
        Update the set that has all names
        """
        self.__all_element_set = {'num_population', 'num_medical_staff', 'num_ppe', 'num_infected', 'num_deceased',
                                  'num_recovered', 'city_citizens', 'daily_decay'}


def check_number(attribute) -> None:
    """
    A Helper function that checks the parameter of Class City

    :raise TypeError: attribute is not an integer
    :raise ValueError: attribute is not positive
    """
    if attribute <= 0:
        raise ValueError("Input should be positive.")


def generate_attribute() -> dict:
    """
    Generate Attribute for City

    Probability of Infection: 5% - 12%
    Probability of Recovery: 20% - 33% (Basing on the total recovery rate of Canada)
    Initial_hp: 80 - 100

    :return: The dict that represents the attributes of City
    """
    # To easily calculate, all float numbers round to 2 decimals
    prob_infection = round(random.uniform(0.05, 0.12), 2)
    prob_recovery = round(random.uniform(0.20, 0.33), 2)
    initial_hp = random.randint(80, 100)
    attribute = {'prob_infection': prob_infection, 'prob_recovery': prob_recovery, 'initial_hp': initial_hp}
    return attribute


def main() -> None:
    """
    Test the Class City
    """
    vancouver = City(10, 2, 1_000_000)
    pprint.pprint(vancouver.get_citizens())


if __name__ == '__main__':
    main()