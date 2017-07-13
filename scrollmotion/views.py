from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


@login_required
def dashboard(request):
	return render(request, 'dashboard/dashboard.html', {})


class Register(View):

	def get(self, request):
		form = UserCreationForm()
		return render(request, 'registration/register.html', {'form': form})

	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			error = form.errors.values()[0]
			return render(request, 'registration/register.html', {'form': form, 'error': error})
