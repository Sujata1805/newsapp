from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsArticle
from .serializers import NewsArticleSerializer



# Create your views here.

class NewsAPIView(APIView):
    def get(self, request):
        articles = NewsArticle.objects.all()
        serializer = NewsArticleSerializer(articles, many=True)
        return render(request,'articles/news.html',{'news_articles':serializer.data})

