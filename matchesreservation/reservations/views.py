from django.shortcuts import render
from django.http import Http404
from .models import Match


def home(request):
    matches = Match.objects.all()
    return render(request, 'home.html', {'matches': matches})


def match_detail(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        raise Http404('Match not found')
    return render(request, 'match_detail.html', {'match': match} )