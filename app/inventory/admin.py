from django.contrib import admin

from .models import (
    Category,
    Order,
    OrderProduct,
    Product,
    ProductPromotionEvent,
    PromotionEvent,
    StockManagement,
    User,
)


# Inline for Product Promotions in Product Admin
class ProductPromotionInline(admin.TabularInline):
    model = ProductPromotionEvent
    extra = 1


# Inline for Order Products in Order Admin
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "level")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "is_active",
        "is_digital",
        "created_at",
    )
    list_filter = ("is_active", "is_digital", "category")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductPromotionInline]


@admin.register(StockManagement)
class StockManagementAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "last_checked_at")
    search_fields = ("product__name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "updated_at")
    list_filter = ("created_at",)
    inlines = [OrderProductInline]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    search_fields = ("order__id", "product__name")


@admin.register(PromotionEvent)
class PromotionEventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "price_reduction")
    search_fields = ("name",)


admin.site.register(ProductPromotionEvent)