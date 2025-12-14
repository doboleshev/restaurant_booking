# 📋 Полный список файлов проекта

## Основные файлы Django
- `manage.py` - Точка входа Django
- `requirements.txt` - Зависимости Python

## Приложения Django
### accounts/ - Пользователи
- `accounts/views.py` - Контроллеры аутентификации
- `accounts/forms.py` - Формы регистрации/входа
- `accounts/models.py` - Модели пользователей
- `accounts/templates/` - Шаблоны: login.html, register.html, profile.html

### bookings/ - Бронирование
- `bookings/models.py` - Table и Booking модели
- `bookings/views.py` - Логика бронирования
- `bookings/forms.py` - Форма бронирования
- `bookings/templates/` - booking_create.html, booking_list.html

### pages/ - Статические страницы
- `pages/views.py` - Главная и "О нас"
- `pages/templates/` - home.html, about.html

### contacts/ - Обратная связь
- `contacts/models.py` - ContactMessage модель

## Шаблоны
- `templates/base.html` - Основной шаблон с Bootstrap 5
- `templates/accounts/`, `templates/bookings/`, `templates/pages/`

## Настройки
- `restaurant_booking/settings.py` - Конфигурация Django
- `restaurant_booking/urls.py` - Маршруты URL
