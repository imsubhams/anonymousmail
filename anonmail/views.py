from django.shortcuts import render, reverse
from django.http import HttpResponse
from anonmail.forms import sendEmailForm
from sendanonmail import sendEmail
from anonmail import models


def home(request):
    if(request.method == 'POST'):
        form = sendEmailForm(request.POST)
        if(form.is_valid()):
            messge = "Hi there,\n\nThis mail is on behalf of Team Anonymous Mail.Someone out there wants to convey the following words to you without revealing his/her identity.\n\n-----------------------\n" + form.cleaned_data['message'] + "\n-----------------------\nIf you wish to report this activity please reply to the same thread starting with @admin.\n\nOur services are free and always will be. We hope to see you again.\n\nRegards\nTeam Anonymous Mail\nhttps://anonymousmail.pythonanywhere.com\n"
            k = sendEmail(form.cleaned_data['to'], '[no-reply]'+form.cleaned_data['subject'], messge)
            # k = False
            if(k==True):
                instance = form.save(commit=False)
                instance.sent = True
                instance.save()
                content = {
                    'message': ' MESSAGE HAS BEEN DELIVERED SUCCESSFULLY!',
                }
            else:
                form.save()
                content = {
                    'message': ' SEEMS LIKE THERE IS SOME ERROR! \n ANYHOW WE GOT YOUR WORDS, \nWE WILL DELIVER IT SOON',
                }
            return render(request, 'home/message.html', content)



        else:
            form = form
    else:
        form = sendEmailForm()
    content = {
        'form': form,
    }
    return render(request, 'home/index.html', content)


def underconstruction(request):
    content = {
        'message' : 'Under Construction... ^_^'
    }
    return render(request, 'home/message.html', content)

