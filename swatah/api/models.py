from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=250)
  completed = models.BooleanField(default=False, blank=True)

  def __str__(self):
      return self.title
  
class Item(models.Model):
	category = models.CharField(max_length=250)
	subcategory = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	amount = models.PositiveIntegerField()

	def __str__(self) -> str:
		return self.name

  
