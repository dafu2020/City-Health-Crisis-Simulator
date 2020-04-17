import random
from person import Person


class City:
    def __init__(self, num_population: int, num_medical_staff: int, num_ppe: int) -> None:
        """
        Simulate a City, including population, medical staff, Personal Protective Equipment

        :param num_population: number of population, an int
        :param num_medical_staff: number of medical stuff, an int
        :param num_ppe: number of Personal Protective Equipment, an int
        """
        self.__num_population = num_population
        self.__medical_staff = num_medical_staff
        self.__num_ppe = num_ppe
        self.__num_deceased = 0
        self.__num_recovered = 0
        self.__city_citizens = []
        self.__daily_decay = 5

    def get_num_population(self) -> int:
        return self.__num_population

    def get_num_medical_staff(self) -> int:
        return self.__medical_staff

    def get_num_ppe(self) -> int:
        return self.__num_ppe

    def set_num_population(self, new_population: int) -> None:
        self.__num_population = new_population

    def set_num_medical_stuff(self, new_medical: int) -> None:
        self.__medical_staff = new_medical

    def set_num_ppe(self, new_ppe: int) -> None:
        self.__num_ppe = new_ppe

    def instantiate_person(self) -> None:
        for number_person in range(0, self.__num_population):
            person_attribute = generate_attribute()
            prob_infection = person_attribute['prob_infection']
            prob_recovery = person_attribute['prob_recovery']
            initial_hp = person_attribute['initial_hp']
            person_object = Person(prob_infection, prob_recovery, initial_hp, 'citizen')
            self.__city_citizens.append(person_object)

    def instantiate_medical_stuff(self) -> None:
        for number_person in range(0, self.__medical_staff):
            person_attribute = generate_attribute()
            prob_infection = person_attribute['prob_infection']
            prob_recovery = person_attribute['prob_recovery']
            initial_hp = person_attribute['initial_hp']
            person_object = Person(prob_infection, prob_recovery, initial_hp, 'medical')
            self.__city_citizens.append(person_object)


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


def main():
    print(generate_attribute())


if __name__ == '__main__':
    main()