from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from urus_sosh1.models import doc
from django.forms import ModelForm
class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class zagruzka(ModelForm):
    class Meta:
        model = doc
        fields = '__all__'


