from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from mysite.utils import unique_slug_generator

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('post_detail', kwargs={'slug': self.slug})

    def get_post_edit_url(self):
        return reverse ('post_edit', kwargs={'slug': self.slug})

    def get_post_delete_url(self):
        return reverse ('post_delete', kwargs={'slug': self.slug})

# --- Slug ---
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)