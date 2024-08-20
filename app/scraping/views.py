from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    """
    Index view for scraping app.

    Args:
        request (HttpRequest): Request object.

    Returns:
        HttpResponse: JSON response.
    """
    return JsonResponse({"message": "Hello, world!"})
