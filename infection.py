def calculate_hp(city: object) -> None:
    for citizen in city.get_citizens():
        if citizen.is_infected() and not citizen.is_recovered():
            new_hp = citizen.get_hp() - city.get_daily_decay()
            citizen.set_hp(max(new_hp, 0))
