from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("genre_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("year"))
        elif filters.get("year_id") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()

        return movies

    def create(self, id):
        return self.dao.create(id)

    def update(self, id):
        self.dao.udate(id)
        return self.dao

    def delete(self, id):
        self.dao.delete(id)
