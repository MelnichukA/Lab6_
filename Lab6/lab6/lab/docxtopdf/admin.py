from django.contrib import admin
from .models import PDFConverter
from .models import UserInfo

admin.site.register(PDFConverter)
admin.site.register(UserInfo)
# Register your models here.
