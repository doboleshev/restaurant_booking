from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Booking, Table


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    context = {
        'bookings': bookings,
        'upcoming_bookings': bookings.filter(date__gte=datetime.now().date()),
        'past_bookings': bookings.filter(date__lt=datetime.now().date())
    }
    return render(request , 'bookings/booking_list.html', context)


@login_required
def booking_create(request):
    if request.method == 'POST':
        # Получаем данные из формы
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        duration = request.POST.get('duration')
        special_requests = request.POST.get('special_requests')
        table_type = request.POST.get('table_type')

        # Валидация данных
        if not all([ date , time , guests ]):
            messages.error(request , 'Пожалуйста, заполните все обязательные поля')
            return render(request , 'bookings/booking_create.html' ,
                          {'today': datetime.now().date().isoformat()})

        try:
            # Проверяем, что дата в будущем
            booking_date = datetime.strptime(date , '%Y-%m-%d').date()
            if booking_date < datetime.now().date():
                messages.error(request , 'Дата бронирования не может быть в прошлом')
                return render(request , 'bookings/booking_create.html' ,
                              {'today': datetime.now().date().isoformat()})
            
            # Парсим время
            booking_time = datetime.strptime(time , '%H:%M').time()
            
            # Валидация количества гостей
            guests_count = int(guests)
            if guests_count < 1 or guests_count > 20:
                messages.error(request , 'Количество гостей должно быть от 1 до 20')
                return render(request , 'bookings/booking_create.html' ,
                              {'today': datetime.now().date().isoformat()})
            
            # Валидация продолжительности
            duration_hours = int(duration) if duration else 2
            if duration_hours < 1 or duration_hours > 6:
                messages.error(request , 'Продолжительность должна быть от 1 до 6 часов')
                return render(request , 'bookings/booking_create.html' ,
                              {'today': datetime.now().date().isoformat()})
            
            # Находим или создаем подходящий столик
            # Сначала пытаемся найти столик по типу и вместимости
            table = Table.objects.filter(
                table_type=table_type or 'standard',
                capacity__gte=guests_count,
                is_active=True
            ).first()
            
            # Если не нашли подходящий столик, берем любой доступный
            if not table:
                table = Table.objects.filter(
                    capacity__gte=guests_count,
                    is_active=True
                ).first()
            
            # Если все еще нет столика, создаем временный (для демонстрации)
            # В реальном приложении здесь должна быть логика создания столика или сообщение об ошибке
            if not table:
                messages.error(request , 'К сожалению, нет доступных столиков на выбранную дату и время')
                return render(request , 'bookings/booking_create.html' ,
                              {'today': datetime.now().date().isoformat()})
            
            # Создаем бронирование
            booking = Booking.objects.create(
                user=request.user,
                table=table,
                date=booking_date,
                time=booking_time,
                duration=duration_hours,
                guests=guests_count,
                special_requests=special_requests or '',
                status='pending'
            )
            
            messages.success(request , f'Столик успешно забронирован на {date} в {time} для {guests} гостей!')
            return redirect('booking_list')
            
        except ValueError as e:
            messages.error(request , f'Некорректный формат данных: {str(e)}')
            return render(request , 'bookings/booking_create.html' ,
                          {'today': datetime.now().date().isoformat()})
        except Exception as e:
            messages.error(request , f'Произошла ошибка при создании бронирования: {str(e)}')
            return render(request , 'bookings/booking_create.html' ,
                          {'today': datetime.now().date().isoformat()})

    # GET запрос - показываем форму
    return render(request , 'bookings/booking_create.html' ,
                  {'today': datetime.now().date().isoformat()})
