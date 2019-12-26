from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(AboutPage)
@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields = ('title', 'description',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    list_display = ('title', 'description',)
    # readonly_fields = ('title', 'description') #in order to make field read-only
    ordering = ('-created_at',)

@admin.register(NavLinks)
class NavLinksAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'active',)
    search_fields = ('active',)
    list_display = ('title', 'url', 'active',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'subject', 'message',)
    list_filter = ('sent_at',) #-create_at if from olf to new
    list_display = ('name', 'email', 'subject',)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ('title','image', 'description', 'category', 'owner')
    list_display = ('title', 'category',)
    list_filter = ('created_at',)
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'image',)
    list_display = ('title',)
    search_field = ('title',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('title','image', 'description', 'category', 'long_description')
    list_display = ('title', 'category',)
    list_filter = ('created_at',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'story')