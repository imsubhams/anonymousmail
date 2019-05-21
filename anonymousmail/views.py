
from django.shortcuts import render

def handler404(request):
    content = {
        'message' : 'Looks Like You Are Lost...'
    }
    return render(request, 'home/messageerror.html', content)