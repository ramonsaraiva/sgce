from django import template
from sgce.models import Enrollment

register = template.Library()

@register.filter
def enrolled_in_activity(user, activity):
	enrollments = Enrollment.objects.filter(person=user, activities=activity)
	if enrollments:
		return True
	return False

