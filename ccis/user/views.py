from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.


class TestIndexView(View):
    def get(self, request, year):
        if request.method == 'GET':
            print(request.path_info)
            print(request.path)
            print(request.GET)
            print(year)
            # month = request.GET.get('month')
            return HttpResponse(year)
