def merge_tmdb_omdb(tmdb_list, omdb_getter):
    result = []
    for movie in tmdb_list:
        omdb = omdb_getter(movie['title'])
        if omdb.get('Response') == 'True':
            movie_data = {
                "title": movie["title"],
                "release_date": movie.get("release_date"),
                "vote_average": movie.get("vote_average"),
                "runtime": omdb.get("Runtime"),
                "director": omdb.get("Director"),
                "imdb_rating": omdb.get("imdbRating")
            }
            result.append(movie_data)
    return result
