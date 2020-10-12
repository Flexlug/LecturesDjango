from .models import Lectures, Subject
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput, ModelChoiceField

class LecturesForm(ModelForm):
    class Meta:
        model = Lectures
        fields = ['subject', 'title', 'video', 'text', 'file', 'date']

        widgets = {

            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название лекции'
            }),
            'video': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код на видео'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Примечание'
            }),
            'file': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл лекции'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата лекции'
            }),
        }

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'slug']

        widgets = {

            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета'
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug (транслит без пробелов)'
            }),
        }