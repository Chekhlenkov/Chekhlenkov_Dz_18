from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace("genres")

@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200

@genres_ns.route("/<int:id>")
class GenreView(Resource):
    def get(self, id):
        genre = genre_service.get_one(id)
        return GenreSchema().dump(genre), 200