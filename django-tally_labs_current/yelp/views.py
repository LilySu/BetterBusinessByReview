from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
<<<<<<< HEAD
from .serializers import YelpYelpScrapingSerializer
from .models import YelpYelpScraping
from tallylib.scattertext import getYelpWords, getYelp3Words
from tallylib.no_nlp_long_phrases import getYelpPhrases
from tallylib.scraper import yelpScraper
=======
from .models import YelpYelpScraping
from .serializers import YelpYelpScrapingSerializer
from tallylib.scraper import yelpScraper
from tallylib.textrank import yelpTrendyPhrases
>>>>>>> origin/master

import requests
import json


<<<<<<< HEAD
def index(request):
    return HttpResponse("Hello, world. You're at the Yelp Scraping app index page.")

def getPosNegPhrases(request, business_id):
    yelpScraperResult = yelpScraper(business_id)
    # result = json.dumps(getYelpWords(yelpScraperResult))
    result = json.dumps(getYelpPhrases(yelpScraperResult))
    # result = json.dumps(getYelp3Words(yelpScraperResult))
=======
def home(request, business_id):
    result = "This is Yelp Analytics home page."
    viztype = request.GET.get('viztype')
    if viztype == '1':
        result = "this is a line chart."
    else:
        result = json.dumps(yelpScraper(business_id))
>>>>>>> origin/master
    return HttpResponse(result)


class YelpYelpScrapingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class YelpYelpScrapingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
<<<<<<< HEAD

    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer
=======
    queryset = YelpYelpScraping.objects.all()
    serializer_class = YelpYelpScrapingSerializer

>>>>>>> origin/master
