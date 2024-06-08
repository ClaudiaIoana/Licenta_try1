from django.db import models

from regular_user.models import RegularUser


class Category(models.Model):
    name = models.CharField(max_length=700)
    creator = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)


class Domain(models.Model):
    name = models.CharField(max_length=700)
    creator = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)


class Flashcards(models.Model):
    front = models.TextField()
    back = models.TextField()
    creator = models.ForeignKey(RegularUser, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    domain_cards = models.ManyToManyField(Domain, through="DomainCards")
    category_cards = models.ManyToManyField(Category, through="CategoryCard")

    class Meta:
        app_label = 'flashcards'


class DomainCards(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    card = models.ForeignKey(Flashcards, on_delete=models.CASCADE)


class CategoryCard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    card = models.ForeignKey(Flashcards, on_delete=models.CASCADE)

