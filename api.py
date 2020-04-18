import requests
import time
import json


# USING COVID-19 API
def get_canada_statistic() -> list:
    """ Fetch the number of COVID-19 confirmed case in Canada

    Fetch the general COVID-19 outbreak data statistics of confirmed cases in Canada
    :precondition: fetch Canadian COVID-19 outbreak statistics in json objects for each day,
                    and store them together in a list
    :postcondition: the fetched information in json objects stored together as a list
    """
    url = 'https://api.covid19api.com/total/country/canada/status/confirmed'
    response = requests.get(url)
    response.raise_for_status()
    canada_info = json.loads(response.text)
    return canada_info


def get_latest_statistic(outbreak_statistic: list) -> None:
    """Get the number of confirmed COVID-19 cases in Canada from the latest three report

    :param outbreak_statistic: a list
    :precondition: outbreak_statistic must be a list containing the date and the corresponding number of confirmed
                    COVID-19 cases in Canada from January to present.
    :postcondition: print out the date and the corresponding number of confirmed COVID-19 cases
                    from the latest three report
    """
    date_list = []
    # USING LIST SLICING
    for i in outbreak_statistic[-3:]:
        date_list.append(i['Date'])

    confirmed_list = []
    for i in range(-3, 0):
        confirmed_list.append(outbreak_statistic[i]['Cases'])

    # USING DICTIONARY COMPREHENSION
    latest_three_indication = {date: case_number for date, case_number in zip(date_list, confirmed_list)}

    print_outbreak_data(latest_three_indication)


def print_outbreak_data(outbreak_data_dictionary: dict) -> None:
    """Print the date and the corresponding confirmed cases

    :param outbreak_data_dictionary: a dictionary
    :precondition: outbreak_data_dictionary must be a dictionary
    :postcondition: print out the date and the corresponding number of confirmed COVID-19 cases;
                    print out a educational message telling people to stay at home
    """
    print(f'\nLet\'s take a look of what is happening in Canada:\n')
    time.sleep(2)

    for date, case_number in outbreak_data_dictionary.items():
        print(f'On day {date}, we have {case_number} confirmed case for COVID-19')
    time.sleep(2)
    print(f'\nThe time has now come for us all to do more, you must stay at home. \n'
          f'This is the critical thing we must do to stop the disease spreading. \n'
          f'Please only leave your house when necessary and for the very limited purposes.\n'
          f'Please respect the work from our medical staff, together, we can flatten that curve!\n')


def main():
    """
    Drive the program
    """
    confirmed_cases_in_canada = get_canada_statistic()
    get_latest_statistic(confirmed_cases_in_canada)


if __name__ == "__main__":
    main()
