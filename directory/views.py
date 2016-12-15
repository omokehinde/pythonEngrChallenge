from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NameNEmail
from django.core.urlresolvers import reverse
from directory.forms import EmailNameForm

def index(request):
	return render(request, 'directory/index.html')

def list(request):
	directory_list = NameNEmail.objects.all()
	context = {
		'directory_list': directory_list
	}
	return render(request, 'directory/list.html', context)

def add(request):
	
	if request.method == 'POST':
		form = EmailNameForm(request.POST)
		if form.is_valid:
			
			user_input = form.save(commit=False)

			# clean (normalized) data
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			user_input.save()

			return HttpResponseRedirect('/list')
	else:
			form = EmailNameForm() # This returns the user to the form 
		#return render(request, 'info/list.html')
	return render(request, 'directory/add.html', {'form': form})


	