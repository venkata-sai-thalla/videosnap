from accounts.models import Skills
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Achievements)
admin.site.register(Experience)
admin.site.register(Certificates)
admin.site.register(Projects)
admin.site.register(Internship)
admin.site.register(Award)
admin.site.register(Publication)
admin.site.register(Resume)
