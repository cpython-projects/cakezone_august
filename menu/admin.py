from django.contrib import admin
from .models import Category, Dish
from django.utils.safestring import mark_safe


class DishInline(admin.TabularInline):
    model = Dish
    fields = ('name', 'price', 'is_visible', 'sort')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (DishInline, )
    list_display = ('name', 'is_visible', 'sort')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category')

    list_editable = ('price', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'