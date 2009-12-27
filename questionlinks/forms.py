from django import forms 
from questionlink_django.questionlinks.models import Question,Answer

class QuestionCreationForm(forms.ModelForm):
	question_text = forms.CharField()
	# user_id = forms.IntegerField()
	# question_date = forms.DateTimeField()
	class Meta:
		model = Question
		fields = ("question_text",)
	
	def save(self, commit=True):
		question = super(QuestionCreationForm, self).save(commit=False)
		question.user_id = 1
		if commit:
			question.save()
		return question


class AnswerCreationForm(forms.ModelForm):
	answer_text = forms.CharField()
	answer_link = forms.CharField()
	class Meta:
		model = Answer
		fields = ('answer_link',"answer_text",)
