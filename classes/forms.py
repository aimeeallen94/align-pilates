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

#def prevent_double_bookings(Class_Type, class_type_id):
    """
    Check if the user has already booked a class at the same time.
    """
#    class_type = get_object_or_404(Class_Type, pk=class_type_id)
#    existing_bookings = Class_Type.objects.filter( class_type__day=class_type.day, class_type__time=class_type.time)
#    for Class_Type in existing_bookings:
#        if class_type.time() == booking.class_type.time():
#            messages.error("You have already booked a class at this time.")