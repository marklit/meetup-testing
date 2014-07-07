from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    photo = models.FileField(upload_to='candidate-photos')
