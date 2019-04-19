#django rest framework
from rest_framework import viewsets
#models
from article.models import Article
#serializers
from article.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer