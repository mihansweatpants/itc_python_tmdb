import core


def get_recommendation(collection, title):
    recommendations = []
    genres = []
    for movie in collection:
        if movie['title'] == title:
            movie_of_choice = movie
            for genre_num in range(len(movie_of_choice['genres'])):
                genres.append(movie_of_choice['genres'][genre_num])
        for genre in genres:
            if genre in movie['genres'] and movie['title'] != movie_of_choice['title']:
                recommendations.append(movie['title'])
    return set(recommendations) 


if __name__ == "__main__":
    collection = core.open_movie_collection(input('Path to your movie collection: '))
    recommnded_movies = get_recommendation(collection, input('Title of the movie you like: '))
    print("You'd also (probably) like to see:")
    for movie in recommnded_movies:
        print(f'-{movie}')