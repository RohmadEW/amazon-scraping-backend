from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from bson.json_util import dumps


def index(request):
    """
    Index view for scraping app.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: JSON response.
    """
    collection = settings.MONGO_DB["reviews"]
    documents = list(collection.find())
    json_documents = dumps(documents)

    return JsonResponse(json_documents, safe=False)


@csrf_exempt
@require_POST
def insert_reviews(request):
    """
    Insert reviews

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: JSON response.
    """
    data = json.loads(request.body)
    reviews = data.get("reviews")

    collection = settings.MONGO_DB["reviews"]
    collection.insert_many(reviews)

    return JsonResponse({"message": "Data inserted successfully!"})
