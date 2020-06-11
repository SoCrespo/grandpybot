# coding: utf-8
import requests
import config as c


def get_map_url(address):
    '''
    Return url of a map centered on address,
    with a marker on address.
    '''

    url = c.GOOGLE_MAP_STATIC_API_URL
    payload = {
        "key": c.GOOGLE_API_KEY,
        "markers": address,
        "size": f'{c.IMG_HEIGHT}x{c.IMG_WIDTH}'
        }
    img = requests.get(url, params=payload)
    return img.url

