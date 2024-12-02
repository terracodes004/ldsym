from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        try:
            send_mail("I HAVE A QUESTION FOR YOU", request.POST['message'], request.POST['email'], 'davidowolabi252@gmail.com')
            didit = 1
            did = 1
            return render(request, "index.html", {"didit": didit, "did": did})
        except:
            didit = 1
            did = 0
            return render(request, "index.html", {"didit": didit, "did": did})
    else:
        did = 1
        didit = 0
        return render(request, "index.html", {"didit": didit, "did": did})

def about(response):
    return render(response, "about.html")

def blogh(response):
    news = []
    for x  in News.objects.all():
        news.append(x)
    news.reverse()
    return render(response, "blog-home.html", {'news':news})

def blogp(response):
    if response.method == "POST":
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password']
        if User.objects.filter(username=username).exists():
            messages.add_message(response, messages.ERROR, "Username already exists.")
            return render(response, "blog-post.html")
        elif User.objects.filter(email=email).exists():
            messages.add_message(response, messages.ERROR, "Email has already been used")
            return render(response, "blog-post.html")
        else:
            messages.add_message(response, messages.INFO, "SIGNED UP DONE")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth.login(response, user)
            return redirect('blog-post.html')
    else:
        return render(response, "blog-post.html")

def contact(response):
    return render(response, "contact.html")

def faq(response):
    faq = []
    for q in Faq.objects.all():
        faq.append(q)
    faq.reverse()
    comment = []
    for xx in Comments.objects.all():
        if xx.data == 'faq':
            comment.append(xx)
    comment.reverse()
    return render(response, "faq.html", {"faq":faq, 'com':comment})

def pi(response):
    return render(response, "portfolio-item.html")

def po(response):
    return render(response, "portfolio-overview.html")

def lo(request):
    auth.logout(request)
    return redirect("blog-post.html")

def li(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('blog-post.html')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password is not correct')
                return render(request, "li.html")
        else:
            messages.add_message(request, messages.ERROR, 'Username or password is not correct')
            return render(request, "li.html")
    else:
        return render(request, "li.html")

def ask(request, typ):
    if typ == "ask":
        if request.method == 'POST':
            name = request.POST['name']
            title = request.POST['title']
            des = request.POST['content']
            file = request.FILES.get('file', None)
            if file:
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                faq = Faq(name=name, title=title, question=des, file=filename)
            else:
                faq = Faq(name=name, title=title, question=des)
            faq.save()
            return redirect('faq')
        else:
            return render(request, 'ask.html')
    
    elif typ == 'post':
        return render(request, 'post.html')
    
    elif typ == 'faq':
        if request.method == 'POST':
            name = request.POST['name']
            content = request.POST['content']
            post_id = request.POST.get('id', None)  # Use get to avoid KeyError
            comm = Comments(name=name, comment=content, data="faq", post_id=post_id)
            comm.save()
            return redirect('faq')
        else:
            return render(request, 'faq.html')
    
    else:
        return render(request, 'ask.html')

def post(request, num):
    varss = []
    for dd in News.objects.all():
        if dd.id == num:
            varss.append(dd)
    ggg = ''+varss[0].content
    ggg = ggg.replace('\n', '<br/>')
    neww = ggg

    varis = {
        'no' : num,
        'news' : varss,
        'neww' : neww
    }
    return render(request, 'pos.html', varis)