from django import forms
from . import dictionarys
class new_accound (forms.Form):
    frist_name=forms.CharField(label="frist name")
    last_name=forms.CharField(label="last name")
    email=forms.CharField(label="email",widget=forms.EmailInput())
    user_name=forms.CharField(label="user name")
    gender=forms.ChoiceField(label="gender",choices=[("male","male"),("female","female")],required=True)
    country=forms.ChoiceField(label="country",choices=dictionarys.countries,required=True)
    currency=forms.ChoiceField(label="currency",choices=dictionarys.currencies,required=True)

    password=forms.CharField(label="password",min_length=8,widget=forms.PasswordInput())
    confpassword=forms.CharField(label="confirm password",min_length=8,widget=forms.PasswordInput())
class login(forms.Form):
    user_name=forms.CharField(label="user name")
    password=forms.CharField(label="password",widget=forms.PasswordInput())
class delete(forms.Form):
    password=forms.CharField(label="confirm password to delete account",widget=forms.PasswordInput())
class ChangePassword(forms.Form):
    currentPassword=forms.CharField(label="current password",widget=forms.PasswordInput())
    newPassword=forms.CharField(min_length=8,label="new password",widget=forms.PasswordInput())
    confNewPassword=forms.CharField(min_length=8,label="confirm new password",widget=forms.PasswordInput())
class editProfile(forms.Form):
    first_name=forms.CharField(label="first name")
    last_name=forms.CharField(label="last name")
    email=forms.CharField(label="email",widget=forms.EmailInput())
    country=forms.ChoiceField(label="country",choices=dictionarys.countries,required=True)
    currency=forms.ChoiceField(label="currency",choices=dictionarys.currencies,required=True)
class Comment(forms.Form):
    content=forms.CharField(label="add comment ...",widget=forms.Textarea())