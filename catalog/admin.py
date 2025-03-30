from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Book

class BookStatusFilter(admin.SimpleListFilter):
    title = _("status")
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return (("Borrowed", _("Borrowed")), ("Available", _("Available")))

    def queryset(self, request, queryset):
        if self.value() == "Borrowed":
            return queryset.filter(borrowed_by__isnull=False)
        if self.value() == "Available":
            return queryset.filter(borrowed_by__isnull=True)


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'borrowed_by']
    list_filter = [BookStatusFilter]
    list_display = ["title", "author", "status", "borrowed_by"]
    readonly_fields = ["status"]


admin.site.register(Book, BookAdmin)
