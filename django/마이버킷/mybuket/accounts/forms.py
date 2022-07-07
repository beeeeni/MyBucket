from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustommUserChangeForm(UserChangeForm):
    class Meta:
    	model = get_user_model()
        # fields = ('username','first_name','email')