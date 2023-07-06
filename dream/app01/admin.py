from django.contrib import admin

# Register your models here.
from .models import Eq
admin.site.register(Eq)

from .models import Exercise
admin.site.register(Exercise)

from .models import Things
admin.site.register(Things)

from .models import Users
admin.site.register(Users)