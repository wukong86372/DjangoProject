from django.contrib import admin
from board.models import Message,Account,Like

# Register your models here.
admin.site.register(Message)
admin.site.register(Account)
admin.site.register(Like)
