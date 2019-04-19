#django rest framework
from rest_framework import serializers
#models
from article.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer."""
    class Meta:
        model = Article
        fields = '__all__'