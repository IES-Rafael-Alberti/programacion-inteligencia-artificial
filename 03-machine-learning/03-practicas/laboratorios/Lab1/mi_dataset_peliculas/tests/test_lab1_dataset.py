import sys
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from mi_dataset_peliculas.merge import merge_tmdb_omdb
from mi_dataset_peliculas.omdb import get_omdb_data
from mi_dataset_peliculas.tmdb import get_popular_movies


class Lab1DatasetContractTests(unittest.TestCase):
    @patch("mi_dataset_peliculas.tmdb.get_api_keys", return_value=("tmdb-key", "omdb-key"))
    def test_popular_movies_keeps_the_lab1_function_contract(self, _keys):
        response = Mock()
        response.json.return_value = {"results": [{"title": "Arrival"}]}
        response.raise_for_status.return_value = None
        session = Mock()
        session.get.return_value = response

        result = get_popular_movies(page=2, session=session)

        self.assertEqual(result, [{"title": "Arrival"}])
        session.get.assert_called_once_with(
            "https://api.themoviedb.org/3/movie/popular",
            params={"api_key": "tmdb-key", "language": "es-ES", "page": 2},
            timeout=30,
        )

    @patch("mi_dataset_peliculas.omdb.get_api_keys", return_value=("tmdb-key", "omdb-key"))
    def test_omdb_lookup_keeps_the_lab1_title_contract(self, _keys):
        response = Mock()
        response.json.return_value = {"Response": "True", "Title": "Arrival"}
        response.raise_for_status.return_value = None
        session = Mock()
        session.get.return_value = response

        result = get_omdb_data("Arrival", session=session)

        self.assertEqual(result["Title"], "Arrival")
        session.get.assert_called_once_with(
            "https://www.omdbapi.com/",
            params={"apikey": "omdb-key", "t": "Arrival", "type": "movie"},
            timeout=30,
        )

    def test_merge_keeps_the_lab1_teaching_schema(self):
        movies = [{"title": "Arrival", "release_date": "2016-11-11", "vote_average": 7.6}]
        omdb_getter = Mock(return_value={
            "Response": "True",
            "Runtime": "116 min",
            "Director": "Denis Villeneuve",
            "imdbRating": "7.9",
        })

        result = merge_tmdb_omdb(movies, omdb_getter)

        self.assertEqual(result, [{
            "title": "Arrival",
            "release_date": "2016-11-11",
            "vote_average": 7.6,
            "runtime": "116 min",
            "director": "Denis Villeneuve",
            "imdb_rating": "7.9",
        }])
        omdb_getter.assert_called_once_with("Arrival")


if __name__ == "__main__":
    unittest.main()
