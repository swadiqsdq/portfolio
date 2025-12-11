from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header='Super Admin'
admin.site.site_title='super admin'
admin.site.index_title='Super Admin Dashboard' 

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Internship)
admin.site.register(Skill)
admin.site.register(Projects)
admin.site.register(Contact)