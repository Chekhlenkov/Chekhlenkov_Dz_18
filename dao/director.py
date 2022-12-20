from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Director).get(id)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, id):
        director = self.get_one(id)
        self.session.delete(director)
        self.session.commit()

    def update(self, id):
        director = self.get_one(id.get("id"))
        director.name = id.get("name")

        self.session.add(director)
        self.session.commit()

