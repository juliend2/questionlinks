from datetime import datetime
from django.db import models
from django.contrib.auth import models as umodels

def getnow():
	now = datetime.today()
	str_now = now.date().isoformat()
	return str_now

class Question(models.Model):
	user = models.ForeignKey(umodels.User)
	question_text = models.TextField(default='')
	question_date = models.DateTimeField('date created', default=getnow())
	sorting = models.IntegerField(default=0)
	
class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_link = models.URLField(verify_exists=False, max_length=200)
	answer_text = models.TextField(default='')
	answer_date = models.DateTimeField('date created', default=getnow())
	sorting = models.IntegerField(default=0)
	