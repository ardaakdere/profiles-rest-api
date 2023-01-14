from watchlist_app import models
from rest_framework.response import Response
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = models.Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie = models.Movie.objects.get(pk = pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        movie = models.Movie.objects.get(pk = pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error_messages)

    elif request.method == 'DELETE':
        movie = models.Movie.objects.get(pk = pk)
        movie.delete()
        return Response(200)