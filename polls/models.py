import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(verbose_name='Вопрос', max_length=200)
	pub_date      = models.DateTimeField(verbose_name='Дата публикации', default = timezone.now())
	final_date    = models.DateTimeField(verbose_name='Дата окончания',
						blank=True, default = timezone.now()+datetime.timedelta(days=1))
	win_vote      = models.IntegerField(verbose_name='Досрочная победа с ', default=0)
	completed     = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return self.question_text

	def was_completed(self):
		if timezone.now() >= self.final_date: return True
		elif self.win_vote != 0:
			winner = False
			for pers in self.choice_set.all():
				winner = pers.votes >= self.win_vote
				if winner: return winner
			else: return False
		else: return False


	was_completed.admin_order_field = 'final_date'
	was_completed.boolean = True
	was_completed.short_description = 'Завершено'

	
class Choice(models.Model):
	YEARS_OLD=[(x,str(x)) for x in range(100)]

	question_id  = models.ForeignKey('Question', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Вопрос', help_text='Укажите, в каком опросе нужно участвовать')
	votes        = models.IntegerField(verbose_name='Количество голосов', default=0)
	first_name   = models.CharField(verbose_name='Имя', max_length=100, blank=True, null=True)
	last_name    = models.CharField(verbose_name='Фамилия', max_length=100, blank=True, null=True)
	age          = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=True, null=True, choices=YEARS_OLD)
	photo_person = models.ImageField(upload_to='polls/person/photos/', blank=True)
	bio_person   = models.TextField(max_length=500, help_text='Кратко об участнике',
						verbose_name='Краткая биография' )

	class Meta:
		ordering = ["-votes"]

	def __str__(self):
		return '{1} {0}'.format(self.last_name, self.first_name)

	def get_absolute_url(self):
		return reverse('polls:choice-detail', args=[str(self.id)])
