# from django.shortcuts import render
# from . import models
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = models.Movie.objects.all()

#     data = {
#         'movies': list(movies.values())
#         }

#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie = models.Movie.objects.get(pk=pk)
    
#     data  = {
#             'name': movie.name,
#             'description': movie.description,
#             'active': movie.active
#             }
    
#     return JsonResponse(data)