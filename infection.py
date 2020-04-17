from random import randint


def calculate_hp(city: object) -> None:
    for citizen in city.get_citizens():
        if citizen.is_infected() and not citizen.is_recovered():
            new_hp = citizen.get_hp() - city.get_daily_decay()
            citizen.set_hp(max(new_hp, 0))


def calculate_ppe(city: object) -> None:
    num_ppe = city.get_num_ppe()

    for citizen in city.get_citizens():
        if citizen.get_role == 'medical':
            if num_ppe > 0:
                num_ppe -= 1
                citizen.set_prob_infection(0)
            elif citizen.get_prob_infection() == 0:
                citizen.set_prob_infection(randint(1, 100))

    city.set_num_ppe(num_ppe)
