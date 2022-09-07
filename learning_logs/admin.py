from django.contrib import admin
from .models import Topic, Entry 


admin.site.register(Topic) # tells django to manage our model through admin site 
admin.site.register(Entry)
