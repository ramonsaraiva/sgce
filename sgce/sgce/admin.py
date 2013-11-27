from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from sgce.models import Event, Activity, Enrollment

admin.site.unregister(Group)
admin.site.unregister(Site)

admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(Enrollment)
