from random import randint


def calculate_hp(city: object) -> None:
    """
    Calculate HP.

    Decays the HP of infected citizens by a fixed amount.

    :param city: the City object
    :precondition: city is a valid instance of City
    """

    for citizen in city.get_citizens():
        if citizen.is_infected() and not citizen.is_recovered():
            new_hp = citizen.get_hp() - city.get_daily_decay()
            citizen.update_hp(max(new_hp, 0))


def calculate_ppe(city: object) -> None:
    """
    Calculate personal protective equipment.

    Consumes one PPE per medical worker and protects them from infection.

    :param city: the City object
    :precondition: city is a valid instance of City
    """

    num_ppe = city.get_num_ppe()

    for citizen in city.get_citizens():
        if citizen.get_role() == 'medical':
            if num_ppe > 0:
                num_ppe -= 1
                citizen.set_prob_infection(0)
            elif citizen.get_prob_infection() == 0:
                citizen.set_prob_infection(randint(1, 100))

    city.set_num_ppe(num_ppe)


def medical_assist(city: object) -> None:
    """
    Calculate medical assistances.

    Lets healthy medical workers assist others and increase their recovery probability.

    :param city: the City object
    :precondition: city is a valid instance of City
    """

    patients_per_doctor = 5
    patient_prob_recovery_increase = 8

    citizens = city.get_citizens()
    needs_assistance = [citizen for citizen in citizens if citizen.is_infected()]

    for citizen in citizens:
        if citizen.get_role() == 'medical' and not citizen.is_infected():
            for i in range(patients_per_doctor):
                if len(needs_assistance) == 0:
                    return
                patient = needs_assistance.pop()
                new_prob_recovery = patient.get_prob_recovery() + patient_prob_recovery_increase
                patient.set_prob_recovery(min(100, new_prob_recovery))


def print_statistics(statistics: (int, int, int)) -> None:
    """
    Pretty print statistics.

    :param statistics: tuple of statistics (num_infected, num_recovered, num_deceased)
    :precondition: statistics is a tuple of 3 ints
    :postcondition: the printed text will be accurate and helpful
    """

    num_infected, num_recovered, num_deceased = statistics
    print(f'⚠️ Infected: {num_infected}')
    print(f'✅ Recovered: {num_recovered}')
    print(f'❌ Deceased: {num_deceased}')
