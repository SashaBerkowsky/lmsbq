from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'borrowed_by')
    list_filter = ('status',) 

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

admin.site.register(Book, BookAdmin)
