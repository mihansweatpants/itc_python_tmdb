import urllib.request
import urllib.parse
import json
import random
import core


def get_the_latest_movie_id(api_key):
    return core.make_tmdb_api_request('/movie/latest', api_key)['id']


def generate_movie_collection(collection_length):
    collection = []
    while len(collection) != collection_length:
        try:
            collection.append(core.make_tmdb_api_request(f'/movie/{random.randint(1, max_range)}', api_key))
        except urllib.error.HTTPError as err:
            if err.code == 404:
                continue
    return collection


if __name__ == "__main__":
    max_range = get_the_latest_movie_id(os.environ.get('API_KEY'))
    movie_collection = generate_movie_collection(input('Size of collection: '))
    core.write_to_json_file('./', input('Name of collection: '), movie_collection)
