from django.contrib import admin
from django.utils.html import format_html

from electronics_shop.models import Product, Supplier

# Register your models here.
admin.site.register(Product)


@admin.action(description="Clear debt")
def clear_debt(self, request, queryset):
    queryset.update(debt=0.00)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "level",
        "type",
        "title",
        "link_to_supplier",
        "debt",
        "created_at",
    )
    list_display_links = ("title",)
    list_filter = ("city",)
    search_fields = ("title",)
    actions = (clear_debt,)

    def link_to_supplier(self, obj):
        if obj.the_supplier:
            link = f"/admin/electronics_shop/supplier/{obj.the_supplier.id}/change/"
            return format_html(
                '<a href="{}">Supplier {}</a>', link, obj.the_supplier.title
            )
        return ""

    link_to_supplier.short_description = "Show supplier"
