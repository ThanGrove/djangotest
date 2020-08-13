from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    markup = '<html><head><title>New Catalog Django API Site</title></head>' \
             '<body><h1>New Django API For Catalogs</h1>' \
             '<p>This site is a test Django site to explore employing Saxon for XML transflrmations</p>' \
             '<ul><li><a href="/polls/">Polls</a></li>' \
             '<li><a href="/admin/">Admin</a> (Hint: admin / !!admin)</li></ul>' \
             '</body></html>'
    return HttpResponse(markup)
