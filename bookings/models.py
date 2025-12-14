from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator


class Table (models.Model):
    """Модель столика"""
    TABLE_TYPES = [('standard' , 'Стандарт'), ('vip' , 'VIP'), ('family' , 'Семейный'), ('bar' , 'Барная стойка'),]

    number = models.PositiveIntegerField(unique=True , verbose_name="Номер столика")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")
    table_type = models.CharField(max_length=20 , choices=TABLE_TYPES , verbose_name="Тип столика")
    is_active = models.BooleanField(default=True , verbose_name="Доступен")
    description = models.TextField(blank=True , verbose_name="Описание")
    image = models.ImageField(upload_to='tables/' , blank=True , null=True , verbose_name="Фото")

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"

    def __str__(self):
        return f"Столик №{self.number} ({self.capacity} персон)"


class Booking (models.Model):
    """Модель бронирования"""
    STATUS_CHOICES = [('pending', 'Ожидает подтверждения'), ('confirmed', 'Подтверждено') ,
                      ('cancelled', 'Отменено') , ('completed', 'Завершено') ,]

    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="Пользователь")
    table = models.ForeignKey(Table , on_delete=models.CASCADE , verbose_name="Столик")
    date = models.DateField(verbose_name="Дата бронирования")
    time = models.TimeField(verbose_name="Время бронирования")
    duration = models.PositiveIntegerField(default=2 , validators=[MinValueValidator(1) , MaxValueValidator(6)] ,
                                           verbose_name="Продолжительность (часы)")
    guests = models.PositiveIntegerField(default=2 , validators=[MinValueValidator(1) , MaxValueValidator(20)] ,
                                         verbose_name="Количество гостей")
    special_requests = models.TextField(blank=True , verbose_name="Особые пожелания")
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ['-date' , '-time']

    def __str__(self):
        return f"Бронирование #{self.id} - {self.user.username}"
