from dao.genre import GenreDAO

class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, id):
        return self.dao.create(id)

    def update(self, id):
        self.dao.udate(id)
        return self.dao

    def delete(self, id):
        self.dao.delete(id)
