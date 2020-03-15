import graphene
from graphene_django import DjangoObjectType

from .models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(graphene.ObjectType):
    movies = graphene.List(MovieType)

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()

class CreateMovie(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        movie = Movie(title=title)
        movie.save()

        return CreateMovie(
            id=movie.id,
            title=movie.title,
        )


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()