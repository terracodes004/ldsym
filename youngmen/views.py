from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from random import randint
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import Udetails, Post

def index(request):
    if request.method == "POST":
        try:
            send_mail("I HAVE A QUESTION FOR YOU", request.POST['message'], request.POST['email'],['kehinde0w0labi004@gmail.com'] )
            didit = 1
            did = 1
        except Exception as e:
            print(f"Error sending email: {e}")
            didit = 1
            did = 0
    else:
        did = 1
        didit = 0

    postt = []
    nn = 0
    bb = []
    for dr in Udetails.objects.all():
        bb.append(dr)
    for xx in Post.objects.all().reverse():
        if nn < 3 and xx.a_approval:
            postt.append(xx)
        nn += 1
    postt.reverse()
    
    return render(request, "index.html", {"didit": didit, "did": did, "postt": postt, 'dr': bb})

def about(response):
    return render(response, "about.html")

def blogh(response):
    news = []
    for x  in News.objects.all():
        news.append(x)
    news.reverse()
    postt = []
    nn = 0
    for xx in Post.objects.all():
        if nn < 3 and xx.a_approval:
            postt.append(xx)
        nn += 1
    postt.reverse()
    bb = []
    for dr in Udetails.objects.all():
        bb.append(dr)
    return render(response, "blog-home.html", {'news':news, 'postt': postt,'dr':bb})

def blogp(response):
    if response.method == "POST":
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password']
        num = response.POST['num']
        if User.objects.filter(username=username).exists():
            messages.add_message(response, messages.ERROR, "Username already exists.")
            return render(response, "blog-post.html")
        elif User.objects.filter(email=email).exists():
            messages.add_message(response, messages.ERROR, "Email has already been used")
            return render(response, "blog-post.html")
        else:
            messages.add_message(response, messages.INFO, "SIGNED UP DONE")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.last_name = num
            user.save()
            auth.login(response, user)
            return redirect('blog-post.html')
    else:
        ud = []
        for gg in Udetails.objects.all():
            if gg.user == response.user.username:
                ud.append(gg)
        
        if Udetails.objects.filter(user=response.user.username):
            dd = True
        else:
            dd = False
        bb = []
        comment = []
        for xx in Comments.objects.all():
            if xx.data == 'bp' and xx.toname == response.user.username:
                comment.append(xx)
        comment.reverse()
        for dr in Post.objects.all():
            if dr.username == response.user.username:
                bb.append(dr)
        bb.reverse()
        return render(response, "blog-post.html", {"ud":ud, "dd":dd,'news':bb, 'com': comment})

def contact(response):
    if response.method == "POST":
        name = response.POST['name']
        email = response.POST['email']
        phone = response.POST['phone']
        message = response.POST['message']
        try:
            send_mail("I HAVE A QUESTION FOR YOU", f"Name : {name}\n Phone : {phone} \n {message}", email,['kehinde0w0labi004@gmail.com'] )
            messages.add_message(response, messages.INFO, "SENT SUCCESSFUL")
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.add_message(response, messages.ERROR, f"Error occur {e}")
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
        if request.method == 'POST':
            username = request.user.username
            likes = 0
            hates = 0
            comment = ""
            a_approval = 0
            title = request.POST['title']
            description = request.POST['des']
            file = request.FILES.get('file', None)
            if file:
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                pos = Post(username=username, likes=likes, hate=hates, comment=comment, a_approval=a_approval, title=title, description=description, photos=filename)
            else:
                pos = Post(username=username, likes=likes, hate=hates, comment=comment, a_approval=a_approval, title=title, description=description)
            bad = ['fuck','ass', 'nigga', 'bitch', 'shit']
            for b in bad:
                if b in description:
                    good = False
                else:
                    good = True
            if good:
                pos.save()
            return redirect('/index.html')
        else:

            return render(request, 'post.html')
    
    elif typ == 'faq':
        if request.method == 'POST':
            name = request.POST['name']
            content = request.POST['content']
            post_id = request.POST.get('id', None)  # Use get to avoid KeyError
            comm = Comments(name=name, comment=content, data="faq", post_id=post_id)
            comm.save()
            return redirect('faq')
    elif typ == 'bp':
        if request.method == 'POST':
            name = request.POST['name']
            content = request.POST['content']
            post_id = request.POST.get('id', None)  # Use get to avoid KeyError
            comm = Comments(name=name,toname=request.user.username, comment=content, data="bp", post_id=post_id)
            comm.save()
            return redirect('/blog-post.html')
    elif typ == 'use':
        if request.method == 'POST':
            ty = request.POST['to']
            name = request.POST['name']
            content = request.POST['content']
            post_id = request.POST.get('id', None)  # Use get to avoid KeyError
            comm = Comments(name=name,toname=ty, comment=content, data="bp", post_id=post_id)
            comm.save()
            return redirect(f'/user/{ty}')
        else:
            return render(request, 'faq.html')
    elif typ=="details":
        if request.method == 'POST':
            user = request.user.username
            des = request.POST['des']
            tags = request.POST['tags']
            file = request.FILES.get('file', None)
            if file:
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                uu = Udetails(user=user, des=des, tags=tags, profile=filename, an_lds_ym=0)
            else:
                uu = Udetails(user=user, des=des, tags=tags, an_lds_ym=0)
            uu.save()
            return redirect('blog-post')
        return render(request, 'details.html')
        
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
def full(request):
    postt = []
    for xx in Post.objects.all():
        postt.append(xx)
    bb = []
    for dr in Udetails.objects.all():
        bb.append(dr)
    postt.reverse()
    return render(request, 'full.html', {'postt': postt,'dr':bb})
def fulll(request, pk):
    postt = []
    for dd in Post.objects.all():
        if dd.id == int(pk):
            postt.append(dd)
            
    ggg = f'{postt[0].description}'
    ggg = ggg.replace('\n', '<br/>')
    neww = ggg
    bb = []
    for dr in Udetails.objects.all():
        bb.append(dr)
    varis = {
        'no' : pk,
        'news' : postt,
        'neww' : neww,
        'dr':bb
    }
    
    
    return render(request, 'fulll.html', varis)
def uuser(request, username):
    use = []
    ud = []
    for gg in Udetails.objects.all():
        if gg.user == username:
            ud.append(gg)
    
    if Udetails.objects.get(user=username):
        dd = True
    else:
        dd = False
    bb = []
    comment = []

    for xx in Comments.objects.all():
        if xx.data == 'bp' and xx.toname == username:
            comment.append(xx)
    comment.reverse()
    for dr in Post.objects.all():
        if dr.username == username:
            bb.append(dr)
    
    
    return render(request, 'uuser.html',{'use':use,"ud":ud,"usee":username, "dd":dd,'news':bb, 'com': comment, "ff": User.objects.get(username=username).last_name})
def search(request, type, look):
    user_search = []
    uuse = []
    post_search = []
    faq_search = []

    for i in User.objects.all():
        if f'{look}'.lower() in f'{i.username}'.lower() or f'{look}'.lower() == f'{i.username}'.lower():
            user_search.append(i)
            for ff in Udetails.objects.all():
                if ff.user == i.username:
                    uuse.append(ff)
        else:
            pass
    for i in Faq.objects.all():
        if f'{look}'.lower() in f'{i.title}'.lower() or f'{look}'.lower() in f'{i.name}'.lower():
            faq_search.append(i)
        else:
            pass
    for i in Post.objects.all():
        if f'{look}'.lower() in f'{i.title}'.lower() or look in f'{i.username}'.lower() :
            post_search.append(i)
        else:
            pass
    post_search.reverse()
    user_search.reverse()
    uuse.reverse()
    faq_search.reverse()
    varr = {
        'use' : user_search,
        'usee' : uuse,
        'post' : post_search,
        'faq' : faq_search,
        'typ' : type,
        'sea' : look
    }
    return render(request, "search.html", varr)
def see(request):
    return redirect(f"/search/{request.GET['search']}/all")
def forr(request):
    ff = []
    email = request.POST['email']
    for hh in User.objects.all():
        if hh.email == email:
            ff.append(hh)
    numcode = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
    try:
        send_mail("Verification code for an lds Young man", numcode, "kehindeowolabi004@gmail.com", [email])
        return render(request, "forgot.html", {"num" : int(numcode), "use":ff, 'em':email})
    except Exception as e:
        print(f'Error sending the mail {e}')
        return redirect("/login")
    
def cha(request, email):
    dd = User.objects.get(email=email)
    dd.set_password(request.POST['pass'])
    dd.save()
    return redirect("/blog-post.html")