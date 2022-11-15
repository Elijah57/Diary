from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    pass
    moods = [
        ("happy", "happy"),
        ("numb", "numb"),
        ("angry", "angry")

    ]
    date = models.DateTimeField(primary_key= False, blank=False)
    story = models.TextField(blank=False, primary_key= False)
    title = models.CharField(max_length=250)
    mood = models.CharField(max_length=15, choices=moods,default="numb", blank=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-date"]

# CREATE TABLE "Diary_journal" 
# ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#  "date" datetime NOT NULL,
#   "story" text NOT NULL,
#    "title" varchar(250) NOT NULL,
#     "mood" varchar(15) NOT NULL);
# COMMIT;
#python manage.py makemigrations    python manage.py runserver  
