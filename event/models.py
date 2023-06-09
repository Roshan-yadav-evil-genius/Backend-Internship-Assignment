from django.db import models

# Create your models here.


class Event(models.Model):
    event_type = models.CharField("Event type", max_length=50)
    name = models.CharField("Name of Event", max_length=50)
    tagline = models.CharField("Tag line of event", max_length=50)
    schedule = models.DateTimeField(
        "Schedule", auto_now=False, auto_now_add=False)
    description = models.TextField("Description of Event")
    file = models.ImageField("Event Image", upload_to="Event/Files")
    user = models.CharField("User", max_length=50)
    Category = models.CharField("Category", max_length=50)
    Subcategory = models.CharField("Subcategory", max_length=50)
    rigor_rank = models.IntegerField("Rigor Rank")
    attendees = models.CharField("Attendees", max_length=50)

    created_at=models.DateTimeField("Created At", auto_now=False, editable=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} > {self.name}"
