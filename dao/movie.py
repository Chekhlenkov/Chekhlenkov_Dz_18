from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, id):
        movie = self.get_one(id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, id):
        movie = self.get_one(id.get("id"))
        movie.title = id.get("title")
        movie.description = id.get("description")
        movie.trailer = id.get("trailer")
        movie.year = id.get("year")
        movie.rating = id.get("rating")
        movie.genre_id = id.get("genre_id")
        movie.director_id = id.get("director_id")

        self.session.add(movie)
        self.session.commit()
