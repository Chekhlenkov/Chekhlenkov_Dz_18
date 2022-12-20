from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Genre).get(id)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, id):
        genre = self.get_one(id)
        self.session.delete(genre)
        self.session.commit()

    def update(self, id):
        genre = self.get_one(id.get("id"))
        genre.name = id.get("name")

        self.session.add(genre)
        self.session.commit()
