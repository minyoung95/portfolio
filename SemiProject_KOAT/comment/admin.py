from django.contrib import admin
from comment.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['c_no','c_content','c_date']