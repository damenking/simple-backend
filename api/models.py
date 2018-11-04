from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question