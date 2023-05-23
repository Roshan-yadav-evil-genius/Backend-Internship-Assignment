from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField("Category", max_length=50)

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE)
    name = models.CharField("Sub Category", max_length=50)

    def __str__(self) -> str:
        return f"{self.category} > {self.name}"


class Event(models.Model):
    event_type = models.CharField("Event type", max_length=50)
    name = models.CharField("Name of Event", max_length=50)
    tagline = models.CharField("Tag line of event", max_length=50)
    schedule = models.DateTimeField(
        "Schedule", auto_now=False, auto_now_add=False)
    description = models.TextField("Description of Event")
    file = models.ImageField("Event Image", upload_to="Event/Files")
    user = models.ForeignKey(
        User, verbose_name="Created By", on_delete=models.CASCADE)
    Category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE)
    Subcategory = models.ForeignKey(
        Subcategory, verbose_name="SubCategory", on_delete=models.CASCADE)
    rigor_rank = models.IntegerField("Rigor Rank")
    attendees = models.CharField("Attendees", max_length=50)

    created_at=models.DateTimeField("Created At", auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.user} > {self.name}"
