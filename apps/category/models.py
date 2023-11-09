from django.db import models

class Category(models.Model):
    GENDER_CHOICES = (
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('niño', 'Niño'),
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='H')

    def __str__(self):
        return self.name

