from django.db import models

class UserInfo(models.Model):
	name = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.name

# Create your models here.
class PDFConverter(models.Model):
	name = models.CharField(max_length = 100)
	time = models.TimeField(auto_now = True)
	size = models.IntegerField()
	regDate = models.DateField(auto_now = True)
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	uploadCount = models.IntegerField()
	
	def __str__(self):
		return self.name