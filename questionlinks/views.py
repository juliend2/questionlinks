from django import forms 
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render_to_response
from questionlink_django.questionlinks.forms import QuestionCreationForm
from questionlink_django.questionlinks.models import Question


def login(request): 
	if request.method == 'POST': 
		username = request.POST.get('username', '') 
		password = request.POST.get('password', '') 
		user = auth.authenticate(username=username, password=password) 
		if user is not None and user.is_active: 
			# Correct password, and the user is marked "active" 
			auth.login(request, user) 
			# Redirect to a success page. 
			return HttpResponseRedirect("/questions") 
		else: 
			# Show an error page 
			return HttpResponseRedirect("/login/") 
	else:
		form = UserCreationForm() 
		return render_to_response('login.html', {
			'form':form,
		})

def register(request): 
	if request.method == 'POST': 
		form = UserCreationForm(request.POST) 
		if form.is_valid(): 
			new_user = form.save() 
			return HttpResponseRedirect("/questions/") 
	else: 
		form = UserCreationForm() 
	return render_to_response("register.html", { 
		'form': form, 
	}) 

@login_required()
def questions(request):
	if request.method == 'POST': 
		form = QuestionCreationForm(request.POST) 
		form.user_id = 1
		if form.is_valid():
			new_question = form.save(commit=False) # Create, but don't save the new author instance.
			new_question.user_id = request.user.id # put the correct user id HERE
			new_question.save()
			return HttpResponseRedirect("/questions/") 
	else: 
		form = QuestionCreationForm() 
		questions = Question.objects.filter(user=request.user.id)
		return render_to_response("questions.html", { 
			'form': form, 
			'questions':questions,
		})

def logout(request): 
	auth.logout(request) 
	# Redirect to a success page. 
	return HttpResponseRedirect("/login/")
	
