from django.contrib import admin
from .models import Table , Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number' , 'capacity' , 'table_type' , 'is_active')
    list_filter = ('table_type' , 'is_active')
    search_fields = ('number' , 'description')
    list_editable = ('is_active' ,)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user' , 'table' , 'date' , 'time' , 'guests' , 'status')
    list_filter = ('status' , 'date' , 'table__table_type')
    search_fields = ('user__username' , 'table__number')
    readonly_fields = ('created_at' , 'updated_at')
    date_hierarchy = 'date'
    actions = ['confirm_bookings' , 'cancel_bookings']

    def confirm_bookings(self , request , queryset):
        queryset.update(status='confirmed')
        self.message_user(request , f"{queryset.count()} бронирований подтверждено")

    confirm_bookings.short_description = "Подтвердить выбранные бронирования"

    def cancel_bookings(self , request , queryset):
        queryset.update(status='cancelled')
        self.message_user(request , f"{queryset.count()} бронирований отменено")

    cancel_bookings.short_description = "Отменить выбранные бронирования"
