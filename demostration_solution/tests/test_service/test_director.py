from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService
from demostration_solution.setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    jonh_evan = Director(id=1, name='jonh_evan')
    kate_mody = Director(id=2, name='kate_mody')
    max_harden = Director(id=3, name='max_harden')

    director_dao.get_one = MagicMock(return_value=jonh_evan)
    director_dao.get_all = MagicMock(return_value=[jonh_evan, kate_mody, max_harden])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None
        assert director.id != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {

            "name": "Johny",
        }
        director = self.director_service.create(director_d)
        assert director.id != None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Johny"
        }
        self.director_service.update(director_d)
