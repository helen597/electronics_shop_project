from django.contrib import admin
from electronics_shop.models import Product, Supplier
from django.utils.html import format_html

# Register your models here.
admin.site.register(Product)


@admin.action(description="Clear debt")
def clear_debt(queryset):
    queryset.update(debt=0.00)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
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
            link = f"/admin/electronics_shop/supplier/1/change/"
            return format_html(
                '<a href="{}">Supplier {}</a>', link, obj.the_supplier.title
            )
        return ""

    link_to_supplier.short_description = "Show supplier"
