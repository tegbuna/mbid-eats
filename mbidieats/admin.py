# (To be able to edit recipes we edit here:)
from django.contrib import admin
# import models
from .models import Topic, Recipe

# Register your models here.
admin.site.register(Topic)
admin.site.register(Recipe)





