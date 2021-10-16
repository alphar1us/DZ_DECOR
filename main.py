from loggers import logger, logger_with_path
import requests
import time


@logger
def get_questions(start_date, end_date, tags):
    url = 'https://api.stackexchange.com/2.2/questions'

    params = {'fromdate': str(start_date), 'todate': str(end_date), 'tagged': tags, 'site': 'stackoverflow'}

    response = requests.get(url, params)
    response.raise_for_status()

    questions = []

    for items in response.json()['items']:
        questions += [items['title']]

    return questions


if __name__ == '__main__':
    days = 2
    end_date = round(time.time())
    start_date = end_date - 86400 * days
    tags = 'Python'

    get_questions(start_date, end_date, tags)