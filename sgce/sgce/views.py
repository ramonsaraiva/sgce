from django.shortcuts import redirect

def switch(request):
	if request.user.is_authenticated():
		if request.user.stype == 'P':
			return redirect('/sgceusr/')
		elif request.user.stype == 'R' or request.user.stype == 'O':
			return redirect('/sgceman/')
	return redirect('/person/login/')
