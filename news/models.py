import uuid
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import datetime
from django.conf import settings
from django.utils.text import slugify


def image_upload(instance, filename):
    # Set a file name as date and time
    today = datetime.now()
    year = today.year
    month = today.strftime('%B')
    time = today.time()
    title = title = f'{year}_{month}_{time}'
    title1 = title.replace(':', '_')[:-7]

    # Change file name
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.author, title1, ext)

    return f'news/{year}/{month}/{filename}'


class News(models.Model):
    title = models.CharField(max_length=100, null=False)
    subtitle = models.CharField(max_length=100, null=False)
    description = RichTextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, limit_choices_to={'is_staff': True}, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    image = models.ImageField(upload_to=image_upload, default='news.jpg')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=200,
                            editable=False, allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-create_at', 'title']

    def __str__(self):
        return self.title
