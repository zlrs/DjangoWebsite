from django.forms import ModelForm
from creditessential.models import CoursesFinished

class CoursesFinishedForm(ModelForm):
    class Meta:
        model = CoursesFinished
        fields = '__all__'