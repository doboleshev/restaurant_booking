from django.db import models


class ContactMessage (models.Model):
    """Модель сообщений обратной связи"""
    name = models.CharField(max_length=100 , verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20 , blank=True , verbose_name="Телефон")
    subject = models.CharField(max_length=200 , verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
