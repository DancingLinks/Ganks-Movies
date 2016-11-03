import json
import os
import urllib
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
import requests
from app.me.utils import Utils
from app.me.urls import Urls


def test(request):
    return render(request, 'test.html')


def home(request):
    return HttpResponseRedirect("/index")


def index(request):
    data = Utils.get_json_response(Urls.get_date_all())['results'][0]
    date = data.split('-')
    year, month, day = date[0], date[1], date[2]
    data = Utils.get_json_response(Urls.get_day_ganks(year, month, day))
    dict = Utils.json_to_dict(data)
    dict['title'] = '\u4eca\u65e5\u5e72\u8d27'
    return render(request, 'index.html', dict)


def day_ganks(request, id):
    data = Utils.get_json_response(Urls.get_date_all())['results'][int(id)-1]
    date = data.split('-')
    year, month, day = date[0], date[1], date[2]
    data = Utils.get_json_response(Urls.get_day_ganks(year, month, day))
    dict = Utils.json_to_dict(data)
    dict['title'] = 'Ganks (' + year + '-' + month + '-' + day + ')'
    return render(request, 'day_ganks.html', dict)


def android_ganks(request, id):
    response = requests.get(Urls.get_android_all(10, id))
    ganks = json.loads(response.text)['results']
    print(ganks)
    return render(request, 'android_ganks.html', {'title': 'Android Ganks', 'ganks': ganks})


def ios_ganks(request, id):
    response = requests.get(Urls.get_ios_all(10, id))
    ganks = json.loads(response.text)['results']
    return render(request, 'ios_ganks.html', {'title': 'iOS Ganks', 'ganks': ganks})


def front_ganks(request, id):
    response = requests.get(Urls.get_front_all(10, id))
    ganks = json.loads(response.text)['results']
    return render(request, 'front_ganks.html', {'title': 'Front Ganks', 'ganks': ganks})


def app_ganks(request, id):
    response = requests.get(Urls.get_app_all(10, id))
    ganks = json.loads(response.text)['results']
    return render(request, 'app_ganks.html', {'title': 'App Ganks', 'ganks': ganks})


def xiatuijian_ganks(request, id):
    response = requests.get(Urls.get_xiatuijian_all(10, id))
    ganks = json.loads(response.text)['results']
    return render(request, 'xiatuijian_ganks.html', {'title': 'Recommend Ganks', 'ganks': ganks})


def movie_ganks(request):
    ganks = {}
    return render(request, 'movie_ganks.html', {'title': 'Movie Ganks', 'ganks': ganks})


@csrf_exempt
def search_movie(request):
    title = request.POST.get('title', '')
    year = request.POST.get('year', '')
    plot = request.POST.get('plot', '')
    data = requests.get(Urls.get_movie(title, year, plot))
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    root = ET.fromstring(data.content.decode())
    ganks = []
    find = False
    for movie in root.findall('movie'):
        find = True
        movie_dict = {}
        movie_dict['title'] = movie.get('title')
        movie_dict['year'] = movie.get('year')
        movie_dict['released'] = movie.get('released')
        movie_dict['runtime'] = movie.get('runtime')
        movie_dict['genre'] = movie.get('genre')
        movie_dict['director'] = movie.get('director')
        movie_dict['writer'] = movie.get('writer')
        movie_dict['actors'] = movie.get('actors')
        movie_dict['plot'] = movie.get('plot')
        movie_dict['language'] = movie.get('language')
        movie_dict['country'] = movie.get('country')
        movie_dict['awards'] = movie.get('awards')
        movie_dict['poster'] = movie.get('poster')
        movie_dict['metascore'] = movie.get('metascore')
        movie_dict['imdbRating'] = movie.get('imdbRating')
        ganks.append(movie_dict)
    return render(request, 'movie_ganks.html', {'title': 'Movie Ganks', 'find': find, 'ganks': ganks})


@csrf_exempt
def download(request):
    url = request.POST.get('url', '')
    path = os.getcwd()
    name = url.split('/')[3].split('?')[0]
    path_name = path + '\\static\\images\\' + name
    if os.path.exists(path_name):
        result_dict = {'url': '..\\static\\images\\' + name }
        return JsonResponse(result_dict)
    else:
        r = requests.get(url, stream=True)
        with open(path_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
    result_dict = {'url': '..\\static\\images\\' + name }
    return JsonResponse(result_dict)
