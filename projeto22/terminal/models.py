from django.db import models


class alunos(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	refeicao=models.TextField()
	
class manha(models.Model):
	aluno=models.CharField(max_length=50)
	refeicao=models.TextField()

class almoco(models.Model):
	aluno=models.CharField(max_length=50)
	refeicao=models.TextField()

class janta(models.Model):
	aluno=models.CharField(max_length=50)
	refeicao=models.TextField()
