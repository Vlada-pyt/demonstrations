from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService
from demostration_solution.setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    castle = Movie(id=1,
            title="The castle",
            description="The very interesting story about magic castle",
            trailer="https://www.youtube.com/watch?v=VniIjDq3UtA",
            year=2007,
            rating=2.5,
            genre_id=4,
            director_id=4)

    musical = Movie(id=2,
                    title="The musical",
                   description="This film about music around us",
                   trailer="https://www.youtube.com/watch?v=CIjDqdfsd",
                   year=2013,
                   rating=3.5,
                   genre_id=5,
                   director_id=5)


    movie_dao.get_one = MagicMock(return_value=castle)
    movie_dao.get_all = MagicMock(return_value=[castle, musical])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "The castle",
            "description": "The very interesting story about magic castle",
            "trailer": "https://www.youtube.com/watch?v=VniIjDq3UtA",
            "year": 2007,
            "rating": 2.5,
            "genre_id": 4,
            "director_id": 4
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 2,
            "title": "The castle",
            "description": "The very interesting story about magic castle",
            "trailer": "https://www.youtube.com/watch?v=VniIjDq3UtA",
            "year": 2007,
            "rating": 2.5,
            "genre_id": 4,
            "director_id": 4
        }
        self.movie_service.update(movie_d)
