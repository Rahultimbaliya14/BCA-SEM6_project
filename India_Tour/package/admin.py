from django.contrib import admin
from .models import *


admin.site.register(Package)
admin.site.register(Book)
admin.site.register(Payment)