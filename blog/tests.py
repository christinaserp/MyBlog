from django.test import TestCase
from .models import Article
# Create your tests here.

all_articles = Article.objects.all()
print(all_articles)
