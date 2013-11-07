from dilla import spam
import names

@spam.strict_handler('sgce.Event.slug')
def blank_slug(record, field):
	return None

def gen_names(times):
	n = ''
	for i in range(times):
		n += names.get_full_name() + ' '
	return n

@spam.strict_handler('sgce.Event.name')
def event_name(record, field):
	return gen_names(1)

@spam.strict_handler('sgce.Event.description')
def event_description(record, field):
	return gen_names(10)

@spam.strict_handler('sgce.Activity.name')
def activity_name(record, field):
	return gen_names(1)

@spam.strict_handler('sgce.Activity.description')
def activity_description(record, field):
	return gen_names(10)
