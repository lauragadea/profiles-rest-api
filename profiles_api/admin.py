from django.contrib import admin

from profiles_api import models


# this tells the django admin to register our UserProfile model with the admin site
# so it is accesible by the admin interface
admin.site.register(models.UserProfile)
