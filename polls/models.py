from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    class Meta:
        ordering = ['choice_text']

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
