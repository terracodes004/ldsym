from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('about.html', about, name='about'),
    path('blog-home.html', blogh, name='blog-home'),
    path('blog-post.html', blogp, name='blog-post'),
    path('contact.html', contact, name='contact'),
    path('faq.html', faq, name='faq'),  # Ensure this line has the correct name
    path('portfolio-item.html', pi, name='portfolio-item'),
    path('portfolio-overview.html', po, name='portfolio-overview'),
    path("logout", lo, name='logout'),
    path("login", li, name='login'),
    path('form/<str:typ>', ask, name='ask'),
    path("full", full),
    path("full/<str:pk>", fulll),
    path("search/<str:look>/<str:type>", search),
    path("see", see),
    path("user/<str:username>", uuser),
    path("forget.html", forr),
    path("change/<str:email>", cha),
    path('post/<int:num>', post)
]

from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
