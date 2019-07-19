from django.contrib import admin
from .models import *
import copy

# admin.site.register(TypeComponents)
# admin.site.register(CompItems)
admin.site.register(Country)
# admin.site.register(Quantity)
admin.site.register(Part)


# @admin.register(Quantity)
# class QuantityAdmin(admin.ModelAdmin):
#     list_display = ('kol',)

@admin.register(TypeComponents)
class TypeComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_type')



@admin.register(Pki)
class PkiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_type', 'part_name',  'serial_number', 'country', 'date_of_arrival')
    list_filter = ('name', 'name_type', 'part_name', 'serial_number', 'date_of_arrival')


@admin.register(CompItems)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('comp', 'items', 'quantity')
    list_filter = ('comp', 'items')


def rename_serial(numb):
    a = numb.split('-')
    b = a[:len(a)-1]
    b.append(str(int(a[-1]) + 1).zfill(len(a[-1])))
    return '-'.join(b)


@admin.register(Comp)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'part', 'get_items')
    list_filter = ('serial_number', 'part')
    actions = ['make_copy']

    # Копирование компьютера
    def make_copy(self, request, queryset):
        for obj in queryset:
            obj_copy = copy.copy(obj)
            obj_copy.id = None
            sn = obj_copy.serial_number
            obj_copy.serial_number = rename_serial(obj_copy.serial_number)
            obj_copy.save()

    #  Копирование компонентов компьютера
            for item in obj.items.all():
                obj_copy.items.add(item)
            obj_copy.save()

    # Копирование количества компонентов компьютера
            for ob in CompItems.objects.filter(comp__serial_number=obj_copy.serial_number):
                ob.quantity = [i.quantity for i in CompItems.objects.filter(
                    comp__serial_number=sn).filter(items__name_type=ob.items)][0]
                ob.save()

    make_copy.short_description = "Создать копию"