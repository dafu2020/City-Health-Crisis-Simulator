import requests

import json


def get_canada_statistic() -> list:
    """Fetch the most up to date COVID-19 outbreak statistic from COVID 19 API in canada

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
    for i in range(-3, 0):
        date_list.append(outbreak_statistic[i]['Date'])

    confirmed_list = []
    for i in range(-3, 0):
        confirmed_list.append(outbreak_statistic[i]['Cases'])

    latest_three_indication = {k: v for k, v in zip(date_list, confirmed_list)}







