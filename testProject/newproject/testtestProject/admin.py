from django.contrib import admin
from .models import Person
from .models import Mechanism
from .models import AllRange
from .models import Preferences
from .models import Spot

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=('name','lastname')

admin.site.register(Person, PersonAdmin)
admin.site.register(AllRange)
admin.site.register(Preferences)
admin.site.register(Spot)
admin.site.register(Mechanism)

