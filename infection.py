from random import randint


def calculate_hp(city: object) -> None:
    for citizen in city.get_citizens():
        if citizen.is_infected() and not citizen.is_recovered():
            new_hp = citizen.get_hp() - city.get_daily_decay()
            citizen.set_hp(max(new_hp, 0))


def calculate_ppe(city: object) -> None:
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
    num_infected, num_recovered, num_deceased = statistics
    print(f'⚠️ Infected: {num_infected}')
    print(f'✅ Recovered: {num_recovered}')
    print(f'❌ Deceased: {num_deceased}')
