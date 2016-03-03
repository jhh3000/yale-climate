from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Climate(models.Model):

	name = models.CharField(
		blank=True,
		null=True,
		max_length=250,
	)

	year = models.IntegerField(
		blank=True,
		null=True,
	)

	sevoflurane = models.IntegerField(
		blank=True,
		null=True,
	)

	isofluroane = models.IntegerField(
		blank=True,
		null=True,
	)

	desflurane = models.IntegerField(
		blank=True,
		null=True,
	)

	n2o = models.IntegerField(
		blank=True,
		null=True,
	)
