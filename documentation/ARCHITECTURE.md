# Архитектура проекта "Мезонин"

## Модели данных
### Table (Столик)
- number: номер столика
- capacity: вместимость
- table_type: тип (vip, standard, family)
- is_active: доступен ли

### Booking (Бронирование)
- user: пользователь
- table: столик
- date: дата бронирования
- time: время
- guests: количество гостей
- status: статус (pending, confirmed, cancelled)

### User (Пользователь)
- Стандартная модель Django с доп. полями

## Views (Контроллеры)
### accounts.views
- register: регистрация
- login_view: вход
- profile: профиль

### bookings.views  
- booking_create: создание брони
- booking_list: список броней
- booking_detail: детали брони

### pages.views
- home: главная страница
- about: о ресторане

## URLs (Маршруты)
- / - главная
- /about/ - о нас
- /bookings/create/ - бронирование
- /bookings/ - мои брони
- /register/, /login/, /profile/ - пользователи
- /admin/ - админка
