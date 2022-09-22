import re

from django.db import models
from streamfield.fields import StreamField


# Create your models here.
# streamblocks/models.py

# one object
class RichText(models.Model):
    text = models.TextField(blank=True, null=True)
    block_template = "streamblocks/richtext.html"

    class Meta:
        # This will use as name of block in admin
        verbose_name = "Text"


class Quote(models.Model):
    text = models.TextField(blank=True, null=True)
    block_template = "streamblocks/blockquote.html"

    class Meta:
        # This will use as name of block in admin
        verbose_name = "Quote"


class CodeBlock(models.Model):
    code_type = models.CharField(max_length=20, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    block_template = "streamblocks/codeblock.html"

    class Meta:
        # This will use as name of block in admin
        verbose_name = "Code"

    def save(
            self, *args, **kwargs
    ):
        text = re.sub('<', '&lt;', self.text)
        self.text = re.sub('>', '&gt;', text)
        super(CodeBlock, self).save(*args, **kwargs)


# list of objects
class ImageWithText(models.Model):
    image = models.ImageField(upload_to="folder/")
    text = models.TextField(null=True, blank=True)

    # StreamField option for list of objects
    as_list = True

    class Meta:
        verbose_name = "Image with text"
        verbose_name_plural = "Images with text"

    def __str__(self):
        return self.image.url


# Register blocks for StreamField as list of models
STREAMBLOCKS_MODELS = [
    RichText,
    ImageWithText,
    CodeBlock,
    Quote,
]


class Page(models.Model):
    title = models.CharField(max_length=128)
    stream = StreamField(
        model_list=[
            RichText,
            ImageWithText,
            CodeBlock,
            Quote,
        ],
        verbose_name="Page blocks",
        popup_size=(1000, 500),
    )

    def __str__(self):
        return self.title
