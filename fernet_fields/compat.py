import django

from django.utils import encoding

# Support deprecation of force_text in django 4
if django.VERSION < (3, 0):
    force_text = encoding.force_text
else:
    force_text = encoding.force_str

