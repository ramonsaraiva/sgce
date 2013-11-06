from dilla import spam

@spam.strict_handler('sgce.Event.slug')
def blank_slug(record, field):
	return None
