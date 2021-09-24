from django.shortcuts import render
from quotes.models import Quote, Author, Tag
from .serializers import QuoteSerializer, AuthorSerializer, TagSerializer
from rest_framework import viewsets

"""Model ViewSet"""


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
