from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking , ContactMessage
from datetime import date , timedelta


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date' , 'time' , 'guests' , 'duration' , 'special_requests']
        widgets = {'date': forms.DateInput(attrs={'type': 'date' , 'min': date.today()}) ,
                   'time': forms.TimeInput(attrs={'type': 'time'}) ,
                   'special_requests': forms.Textarea(attrs={'rows': 4}) , }

    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        # Устанавливаем минимальную дату - сегодня
        self.fields['date'].widget.attrs['min'] = date.today().isoformat()
        # Максимальная дата - через 3 месяца
        self.fields['date'].widget.attrs['max'] = (date.today() + timedelta(days=90)).isoformat()


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name' , 'email' , 'phone' , 'subject' , 'message']
        widgets = {'message': forms.Textarea(attrs={'rows': 5}) , }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
