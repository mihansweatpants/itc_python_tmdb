import urllib.request
import urllib.parse
import json
import core
import os


def get_movie_budget(movie_id, api_key):
    return core.make_tmdb_api_request(f'/movie/{movie_id}', api_key)['budget']


if __name__ == "__main__":
    print('Budget of "Saw II" is {}$'.format(
        get_movie_budget(215, os.environ.get('API_KEY'))))
