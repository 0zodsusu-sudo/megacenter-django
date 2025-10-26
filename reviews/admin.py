from django.contrib import admin
from .models import Floor, FloorImage, Review, Profile

class FloorImageInline(admin.TabularInline):
    model = FloorImage
    extra = 1

class FloorAdmin(admin.ModelAdmin):
    inlines = [FloorImageInline]

admin.site.register(Floor, FloorAdmin)
admin.site.register(Review)
admin.site.register(Profile)