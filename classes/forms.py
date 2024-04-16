from django import forms
from .models import Class_Type, Level


class ClassTypeForm(forms.ModelForm):

    class Meta:
        model = Class_Type
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        level = Level.objects.all()
        friendly_names = [(l.id, l.get_friendly_name()) for l in level]

        self.fields['level'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

#class ClassBookingForm(forms.ModelForm):
#    class Meta:
#        model = Class_Type
#        fields = ['day', 'time']

#    def clean(self):
#        cleaned_data = super().clean()
#        date = cleaned_data.get('day')
#        time = cleaned_data.get('time')

        # Check if a class is already scheduled at the same time
#        if Class_Type.objects.filter(day=day, time=time).exists():
#            self.add_error('time', 'A class is already scheduled at this time.')