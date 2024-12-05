from django.contrib import admin
from inside.models import Location_inform

@admin.register(Location_inform)
class Location_informAdmin(admin.ModelAdmin):
  list_display = ['l_no','l_name','l_description','l_location']