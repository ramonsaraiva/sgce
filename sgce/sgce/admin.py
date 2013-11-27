from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from sgce.models import Event, Activity, Enrollment, Payment, Voucher

admin.site.unregister(Group)
admin.site.unregister(Site)

class EventModelAdmin(admin.ModelAdmin):
	filter_horizontal = ('activities', 'enrollments', 'vouchers')

class EnrollmentModelAdmin(admin.ModelAdmin):
	filter_horizontal = ('activities',)

admin.site.register(Event, EventModelAdmin)
admin.site.register(Activity)
admin.site.register(Enrollment, EnrollmentModelAdmin)
admin.site.register(Payment)
admin.site.register(Voucher)
