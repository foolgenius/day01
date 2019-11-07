from django.forms import forms

from UserApp.models import Profile, User_module


class UsermoduleForm(forms.ModelForm):
    class Meta:
        model = User_module
        fields = ('u_sex', 'u_birthday', 'u_location', 'u_name', 'u_avatar')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        cleaned = super().clean()
        if cleaned['max_distance'] < cleaned['min_distance']:
            raise forms.ValidationError('max_distance must gt min_distance ')
        else:
            return cleaned['max_distance']

    def clean_max_dating_age(self):
        cleaned = super().clean()
        if cleaned['max_dating_age'] < cleaned['mix_dating_age']:
            raise forms.ValidationError('max_dating_age must gt min_dating_age')
        else:
            return cleaned['max_dating_age']
