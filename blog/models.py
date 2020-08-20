import hashlib
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    def get_absolute_url(self):
        kwargs = {
            "year": self.created_at.year,
            "month": self.created_at.month,
            "day": self.created_at.day,
            "slug": self.slug,
            "pk": self.pk,
        }
        return reverse("entry_detail", kwargs=kwargs)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Entries"


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body

    def gravatar_url(self):
        # Get the md5 hash of the email address
        md5 = hashlib.md5(self.email.encode())
        digest = md5.hexdigest()
        return 'http://www.gravatar.com/avatar/{}'.format(digest)
