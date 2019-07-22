from django.db import models

# Create your models here.
# Database created for PDF file
class pdf_file(models.Model):
    name = models.CharField(max_length=100)
    pdffile = models.FileField()

    def __str__(self):
        return self.name
		
# Database created for Teacher info
class TeachersInfo(models.Model):
