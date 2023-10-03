"""
This module will work only if no permission is needed to get the web-page
"""
import re
import requests


def scrap(url: str) -> list[str]:
    """
    Scrapping a RU phone numbers on web-page
    :param url: string of full url path to source
    :return: list of found phone numbers, return [] if none or hidden(by frontend framework event listeners for ex.).
    """
    # Masking to regular browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Accept': 'text/html',
      }
    r = requests.get(url, headers=headers)

    mass = re.findall(r'([+7,8][-, ]?[(]?\d{3}[)]?[-, ]?\d{3}[-, ]?\d{2}[-, ]?\d{2})', r.content.decode('utf-8'))

    # Filtering to unique items
    result = []
    for item in mass:
        if item not in result:
            result.append(item)
    return result
