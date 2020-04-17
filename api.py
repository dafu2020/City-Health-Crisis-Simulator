import requests
import time
import json

# USING COVID-19 API
def get_canada_statistic() -> list:
    """Fetch the most up to date COVID-19 outbreak statistic from COVID 19 API in Canada

    """
    url = 'https://api.covid19api.com/total/country/canada/status/confirmed'
    response = requests.get(url)
    response.raise_for_status()
    canada_info = json.loads(response.text)
    return canada_info


def get_latest_statistic(outbreak_statistic: list) -> None:
    """Get the last three day's number confirmed Covid-19 cases in Canada
    """
    date_list = []
    for i in outbreak_statistic[-3:]:   # USING LIST SLICING
        date_list.append(i['Date'])

    confirmed_list = []
    for i in range(-3, 0):
        confirmed_list.append(outbreak_statistic[i]['Cases'])

    # USING LIST COMPREHENSION
    latest_three_indication = {date: case_number for date, case_number in zip(date_list, confirmed_list)}

    print_outbreak_data(latest_three_indication)


def print_outbreak_data(outbreak_data_dictionary: dict) -> None:
    """Print the date and the corresponding confirmed cases

    :param outbreak_data_dictionary:
    :return:
    """
    print(f'\nLet\'s take a look of what is happening in Canada:\n')
    time.sleep(3)

    for date, case_number in outbreak_data_dictionary.items():
        print(f'On day {date}, we have {case_number} confirmed case for COVID-19')
    time.sleep(3)
    print(f'\nThe time has now come for us all to do more, you must stay at home. \n'
          f'This is the critical thing we must do to stop the disease spreading. \n'
          f'Please only leave your house when necessary and for the very limited purposes.\n'
          f'Please respect the work from our medical staff, together, we can flatten tht curve!\n')


get_latest_statistic(get_canada_statistic())
