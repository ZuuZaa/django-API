from django.urls import path
from API.views import main_index, news_main, news_update

urlpatterns = [
    path('', main_index, name='main_index'),
    path('news', news_main, name='news_main'),
    path('news/<int:id>', news_update, name='news_update'),

]
