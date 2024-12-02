from django.contrib import admin
from .models import *

# Register your models with the admin site
admin.site.register(Post)
admin.site.register(Scriptures)
admin.site.register(Faq)
admin.site.register(News)
admin.site.register(Comments)