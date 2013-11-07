from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

def switch(request):
	if request.user.is_authenticated():
		if request.user.stype == 'P':
			return redirect('/sgceusr/')
		elif request.user.stype == 'R' or request.user.stype == 'O':
			return redirect('/sgceman/')
	return render_to_response('switch.html', RequestContext(request))
