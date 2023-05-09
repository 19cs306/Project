from django.forms import ModelForm, FileField, ValidationError
from .models import MyModel
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # get the file extension
    valid_extensions = ['.txt', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .txt and .docx files are allowed.')

class MyModelForm(ModelForm):
    file = FileField(validators=[validate_file_extension])

    class Meta:
        model = MyModel
        fields = ['file']
