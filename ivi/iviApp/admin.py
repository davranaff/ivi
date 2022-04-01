from django.contrib import admin
from .models import Video

# Register your models here.

class SlugAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Video)
