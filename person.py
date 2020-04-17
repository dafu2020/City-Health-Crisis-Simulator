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
        """
        return self.__hp

    def get_prob_recovery(self) -> float:
        """
        Get the probability of recovery of a person

        :precondition: Person must have an __prob_recovery attribute
        :postcondition: get the probability of recovery of the Person
        :return: the probability of recovery of the Person as an float
        """
        return self.__prob_recovery

    def get_prob_infected(self) -> float:
        """
        Get the probability of getting virus infection of a person

        :precondition: Person must have an __prob_infection attribute
        :postcondition: get the probability of getting virus infection of the Person
        :return: the probability of getting virus infection of the Person as an float
        """
        return self.__prob_infection

    def get_role(self) -> str:
        """
        Get the occupational role of this person

        :precondition: Person must have an __role attribute
        :postcondition: get the occupational role of the Person
        :return: the occupational role of the Person as a str
        """
        return self.__role

    def is_infected(self) -> bool:
        """
        Verify whether a person is infected

        :precondition: A person must have a __infected attribute
        :postcondition: True if person is infected, else False
        :return: the boolean result
        """
        return self.__infected

    def is_recovered(self) -> bool:
        """
        Verify whether a person is recovered

        :precondition: A person must have a __recovered attribute
        :postcondition: True if person is recovered, else False
        :return: the boolean result
        """
        return self.__recovered

    def is_medical_assisted(self) -> bool:
        """
        Verify whether a person gets medical assist

        :precondition: A person must have a __medical_assist attribute
        :postcondition: True if person is being assisted, else False
        :return: the boolean result
        """
        return self.__medical_assist

    def is_ppe_equipped(self) -> bool:
        """
        Verify whether a person is equipped with PPE (Personal Protective Equipment)

        :precondition: A person must have a __ppe attribute
        :postcondition: True if person is being equipped, else False
        """
        return self.__ppe

    def is_deceased(self) -> bool:
        """
        Verify whether a person is alive

        :precondition: A person must have a __deceased attribute
        :postcondition: True if person is alive, else False
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
        """
        self.__prob_recovery = new_prob_recovery

    def update_prob_infected(self, new_prob_infected: int) -> None:
        """
        Update the probability of getting virus infection of a person

        :precondition: Person must have an __prob_recovery attribute
        :postcondition: update the probability of getting virus infection of the Person
        """
        self.__prob_infection = new_prob_infected

    # is infected mutator = set_infected
    def set_infected(self) -> None:
        """
        Virus infect a person

        :precondition: A person must have a __infected attribute
        :postcondition: if a person is already infected, do nothing; else, changed the __infected to True
        """
        if not self.__infected:
            self.__infected = True

    def set_recovered(self) -> None:
        """
        A person has recovered from COVID-19

        :precondition:  A person must have a __recovered attribute
        :postcondition: if a person is already recovered, do nothing; else, changed the __recovered to True
        """
        if not self.__recovered:
            self.__recovered = True
            self.__infected = False

    def set_medical_assist(self) -> None:
        """
        A person has been assisted by the medical staff

        :precondition: A person must have a __medical_assist attribute
        :postcondition: if a person is already been assisted, do nothing; else, changed the __recovered to True
        """
        if not self.__medical_assist:
            self.__medical_assist = True

    def set_ppe_equipped(self) -> None:
        """
        Equipped a Person with PPE

        :precondition: A person must have a __ppe attribute
        :postcondition: if a person is already been equipped with PPE, do nothing; else, changed the __ppe to True
        """
        if not self.__ppe:
            self.__ppe = True
