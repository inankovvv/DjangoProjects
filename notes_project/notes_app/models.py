from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Notes(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    note = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} {str(self.date)}'

    def update_done(self):
        if self.done:
            self.done = False
        else:
            self.done = True
        self.save()


class Comments(models.Model):
    comment_id = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Comment on #{self.comment_id}'

