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
        self.__deceased = False

        # include getters and setters for all variables(object attributes)

    def is_infected(self) -> bool:
        """
        Verify whether a person is infected

        :precondition: A person must have a __infected attribute
        :postcondition: True if person is infected, else False
        :return: the boolean result
        """
        return True if self.__infected else False

    def is_recovered(self) -> bool:
        """
        Verify whether a person is recovered

        :precondition: A person must have a __recovered attribute
        :postcondition: True if person is recovered, else False
        :return: the boolean result
        """
        return True if self.__recovered else False

    # def set_infected()
    # sets infected attribute - if already infected, do nothing, else change to True

    # ... add more getters/setters
