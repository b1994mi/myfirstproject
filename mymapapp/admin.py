from django.contrib import admin
from .models import Profile, Logger
# Only register the Profile Model and Logger, no customization to the admin page.
admin.site.register(Profile)
admin.site.register(Logger)