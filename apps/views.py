from django.shortcuts import render

from apps.models import Friend


def index_view(request):
    friends = Friend.objects.all()
    context = {
        'friends': friends
    }
    return render(request, 'apps/index.html', context)