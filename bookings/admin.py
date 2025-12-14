from django.contrib import admin
from .models import Table , Booking
from contacts.models import ContactMessage


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


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'subject' , 'created_at' , 'is_read')
    list_filter = ('is_read' , 'created_at')
    search_fields = ('name' , 'email' , 'subject' , 'message')
    readonly_fields = ('created_at' ,)
    actions = ['mark_as_read']

    def mark_as_read(self , request , queryset):
        queryset.update(is_read=True)
        self.message_user(request , f"{queryset.count()} сообщений отмечены как прочитанные")

    mark_as_read.short_description = "Отметить как прочитанные"
