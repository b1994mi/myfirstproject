from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

# Register the form for User Model.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Register the form for Profile Model.
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['adrs', 'phon', 'lngd', 'latd']