import urllib.request
import urllib.parse
import json
import random
import re


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'eng',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def write_to_json_file(path, file_name, data):
    file_path = f'{path}{file_name}.json'
    with open(file_path, 'w') as fp:
        json.dump(data, fp, indent=4)


def open_movie_collection(path):
        with open(path) as json_data:
            return json.load(json_data)