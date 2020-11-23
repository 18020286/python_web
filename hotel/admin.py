from django.contrib import admin

from hotel.models import Room, HotelInfo


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'price', 'num_room')
    search_fields = ('room_type',)


class Hotel(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')


admin.site.register(Room, RoomAdmin)
admin.site.register(HotelInfo, Hotel)


