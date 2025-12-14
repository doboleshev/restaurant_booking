from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime


@login_required
def booking_list(request):
    return render(request , 'bookings/booking_list.html')


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
        except ValueError:
            messages.error(request , 'Некорректный формат даты')
            return render(request , 'bookings/booking_create.html' ,
                          {'today': datetime.now().date().isoformat()})

        # Здесь будет логика сохранения бронирования в базу данных
        # Пока просто показываем сообщение об успехе

        messages.success(request , f'Столик успешно забронирован на {date} в {time} для {guests} гостей!')
        return redirect('booking_list')

    # GET запрос - показываем форму
    return render(request , 'bookings/booking_create.html' ,
                  {'today': datetime.now().date().isoformat()})
