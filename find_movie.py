import json
import re
import core


def find_movie(collection, title):
    matches = []
    for movie in range(len(collection)):
        if re.search(title, collection[movie]['title'], re.IGNORECASE) is not None:
            matches.append(collection[movie]['title'])
    return matches


if __name__ == "__main__":
    collection = core.open_movie_collection(input('Path to your movie collection: '))
    result = find_movie(collection, input('Search for a movie: '))
    print(f'{len(result)} movies found:')
    for movie in result:
        print(f'-{movie}')
