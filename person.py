import doctest


class Person:
    def __init__(self, prob_infection: float, prob_recovery: float, initial_hp: int, role: str):
        """
        Initialize a new Person

        :param prob_infection: a float
        :param prob_recovery:  a float
        :param initial_hp: an integer
        :param role: a string
        :precondition: prob_infection must be a float representing the chance of a person getting infected;
                       prob_recovery must be a float representing the chance of a person will recover;
                       initial_hp must be an positive integer representing the initial HP of a person;
                       role must be a string representing the occupational role of a person.
        :postcondition: initialized Person as an object

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')

        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        """
        # make sure person's initial HP is a positive number
        if initial_hp > 0:
            self.__hp = initial_hp
        else:
            raise ValueError("Person HP have to be bigger than zero!!")

        # set the probability of this person getting infected with the virus
        # and the probability of this person recovered
        self.__prob_recovery = prob_recovery
        self.__prob_infection = prob_infection

        # set the occupational role of this person
        self.__role = role

        # the default states of a person, assuming no one gets the virus on day 1
        self.__infected = False
        self.__recovered = False
        self.__medical_assist = False
        self.__ppe = False

    # getters for Person attributes
    def get_hp(self) -> int:
        """
        Get the HP of a person

        :precondition: Person must have an __hp attribute
        :postcondition: get the hp of the Person
        :return: the HP of the Person as an integer

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.get_hp()
        80
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.get_hp()
        92
        """
        return self.__hp

    def get_prob_recovery(self) -> float:
        """
        Get the probability of recovery of a person

        :precondition: Person must have an __prob_recovery attribute
        :postcondition: get the probability of recovery of the Person
        :return: the probability of recovery of the Person as an float

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.get_prob_recovery()
        0.01
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.get_prob_recovery()
        0.15
        """
        return self.__prob_recovery

    def get_prob_infected(self) -> float:
        """
        Get the probability of getting virus infection of a person

        :precondition: Person must have an __prob_infection attribute
        :postcondition: get the probability of getting virus infection of the Person
        :return: the probability of getting virus infection of the Person as an float

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.get_prob_infected()
        0.02
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.get_prob_infected()
        0.03
        """
        return self.__prob_infection

    def get_role(self) -> str:
        """
        Get the occupational role of this person

        :precondition: Person must have an __role attribute
        :postcondition: get the occupational role of the Person
        :return: the occupational role of the Person as a str

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.get_role()
        'citizen'
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.get_role()
        'medical'
        """
        return self.__role

    def is_infected(self) -> bool:
        """
        Verify whether a person is infected

        :precondition: A person must have a __infected attribute
        :postcondition: True if person is infected, else False
        :return: the boolean result

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.is_infected()
        False
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.is_infected()
        False
        """
        return self.__infected

    def is_recovered(self) -> bool:
        """
        Verify whether a person is recovered

        :precondition: A person must have a __recovered attribute
        :postcondition: True if person is recovered, else False
        :return: the boolean result

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.is_recovered()
        False
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.is_recovered()
        False
        """
        return self.__recovered

    def is_medical_assisted(self) -> bool:
        """
        Verify whether a person gets medical assist

        :precondition: A person must have a __medical_assist attribute
        :postcondition: True if person is being assisted, else False
        :return: the boolean result

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.is_medical_assisted()
        False
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.is_medical_assisted()
        False
        """
        return self.__medical_assist

    def is_ppe_equipped(self) -> bool:
        """
        Verify whether a person is equipped with PPE (Personal Protective Equipment)

        :precondition: A person must have a __ppe attribute
        :postcondition: True if person is being equipped, else False

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.is_ppe_equipped()
        False
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.is_ppe_equipped()
        False
        """
        return self.__ppe

    def is_deceased(self) -> bool:
        """
        Verify whether a person is alive

        :precondition: A person must have a __hp attribute
        :postcondition: True if person is alive(__hp > 0), else False
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.is_deceased()
        False
        >>> person2 = Person(0.03, 0.15, 90, 'medical')
        >>> person2.is_deceased()
        False
        """
        return self.__hp <= 0

    # setters for Person class
    def update_hp(self, new_hp: int) -> None:
        """
        Update the HP of a person

        :param new_hp: an integer
        :precondition: new_hp must be a positive integer;
                        Person must have an __hp attribute
        :postcondition: update the hp of the Person;
                        raise ValueError if the new hp is a negative number

        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> hp_update = 70
        >>> person1.update_hp(hp_update)
        >>> person1.get_hp()
        70
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> hp_update = 94
        >>> person2.update_hp(hp_update)
        >>> person2.get_hp()
        94

        """
        if new_hp >= 0:
            self.__hp = new_hp
        else:
            raise ValueError("Person HP cannot be negative")

    def update_prob_recovery(self, new_prob_recovery: float) -> None:
        """
        Update the probability of recovery of a person

        :param new_prob_recovery: a float
        :precondition:new_prob_recovery must be a float;
                        Person must have an __prob_recovery attribute
        :postcondition: update the probability of recovery of the Person


        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> prob_recovery_update = 0.12
        >>> person1.update_prob_recovery(prob_recovery_update)
        >>> person1.get_prob_recovery()
        0.12
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> prob_recovery_update = 0.12
        >>> person2.update_prob_recovery(prob_recovery_update)
        >>> person2.get_prob_recovery()
        0.12
        """
        self.__prob_recovery = new_prob_recovery

    def update_prob_infected(self, new_prob_infected: int) -> None:
        """
        Update the probability of getting virus infection of a person

        :precondition: Person must have an __prob_recovery attribute
        :postcondition: update the probability of getting virus infection of the Person
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> prob_infected_update =0.08
        >>> person1.update_prob_infected(prob_infected_update)
        >>> person1.get_prob_infected()
        0.08
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> prob_infected_update = 0.23
        >>> person2.update_prob_infected(prob_infected_update)
        >>> person2.get_prob_infected()
        0.23
        """
        self.__prob_infection = new_prob_infected

    # is infected mutator = set_infected
    def set_infected(self) -> None:
        """
        Virus infect a person

        :precondition: A person must have a __infected attribute
        :postcondition: if a person is already infected, do nothing; else, changed the __infected to True
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.set_infected()
        >>> person1.is_infected()
        True
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.set_infected()
        >>> person2.is_infected()
        True
        """
        if not self.__infected:
            self.__infected = True
            self.__recovered = False

    def set_recovered(self) -> None:
        """
        A person has recovered from COVID-19

        :precondition:  A person must have a __recovered attribute
        :postcondition: if a person is already recovered, do nothing; else, changed the __recovered to True
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.set_recovered()
        >>> person1.is_recovered()
        True
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.set_recovered()
        >>> person2.is_recovered()
        True
        """
        if not self.__recovered:
            self.__recovered = True
            self.__infected = False

    def set_medical_assist(self) -> None:
        """
        A person has been assisted by the medical staff

        :precondition: A person must have a __medical_assist attribute
        :postcondition: if a person is already been assisted, do nothing; else, changed the __recovered to True
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.set_medical_assist()
        >>> person1.is_medical_assisted()
        True
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.set_medical_assist()
        >>> person2.is_medical_assisted()
        True
        """
        if not self.__medical_assist:
            self.__medical_assist = True

    def set_ppe_equipped(self) -> None:
        """
        Equipped a Person with PPE

        :precondition: A person must have a __ppe attribute
        :postcondition: if a person is already been equipped with PPE, do nothing; else, changed the __ppe to True
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.set_ppe_equipped()
        >>> person1.is_ppe_equipped()
        True
        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.set_ppe_equipped()
        >>> person2.is_ppe_equipped()
        True
        """
        if not self.__ppe:
            self.__ppe = True

    def set_deceased(self) -> None:
        """
        Call the death of a Person

        :precondition: A person must have a __infected attribute; A person must have a __recovered attribute;
        :postcondition: if a person is dead, then this person will no longer recovered, and infected
        >>> person1 = Person(0.02, 0.01, 80, 'citizen')
        >>> person1.set_deceased()
        >>> person1.is_infected()
        False
        >>> person1.is_recovered()
        False

        >>> person2 = Person(0.03, 0.15, 92, 'medical')
        >>> person2.set_deceased()
        >>> person2.is_infected()
        False
        >>> person2.is_recovered()
        False
        """
        self.__infected = False
        self.__recovered = False


def main():
    """
    Drive the program
    """
    doctest.testmod()


if __name__ == "__main__":
    main()
