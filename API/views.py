from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from API.models import News
import json

# Create your views here.
@csrf_exempt
def main_index(request):
    if request.method == 'GET':
        return JsonResponse({
        "status":"ok",
        }, status=200)
    else:
        return JsonResponse({
        "request type":request.method ,
        }, status=404)


@csrf_exempt
def news_main(request):
    if request.method == 'GET':
        news_list = News.objects.all()
        news_arr = []
        for news in news_list:
            news_arr.append({
                'id':news.id,
                'title':news.title,
                'content':news.content
            })
        return JsonResponse(news_arr, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if 'title' in data and 'content' in data:
            news = News.objects.create(
                title=data.get('title'), 
                content=data.get('content')
            )
            print(news)
            return JsonResponse({
                'id':news.id,
                'title': news.title,
                'content': news.content
            }, status=201)

@csrf_exempt
def news_update(request, id):
    news = News.objects.filter(id=id).last()
    if news:
        if request.method == 'GET':
            return JsonResponse({
                'id':news.id,
                'title': news.title,
                'content': news.content
            }, status=200)
        elif request.method == 'PUT':
            data = json.loads(request.body.decode('utf-8'))
            news.title = data.get('title')
            news.content = data.get('content')
            news.save()
            return JsonResponse({
                'id':news.id,
                'title': news.title,
                'content': news.content
            }, status=201)
        elif request.method == 'DELETE':
            old_news = news
            news.delete()
            return JsonResponse({
                'id':old_news.id,
                'title': old_news.title,
                'content': old_news.content
            }, status=200)
    else:
        return JsonResponse({
            'error_message':'News is not found'
        }, status=404)