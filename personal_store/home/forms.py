from django import forms
from . import dictionarys,models
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
class Items(forms.Form):
    def getCategory():
        categories=[("all","all")]
        for item in models.item.objects.all().order_by("-date"):
            List=(item.category,item.category)
            if List in categories:
                continue
            categories.append(List)
        return categories

    category=forms.ChoiceField(choices=getCategory(),label="category")
    sort=forms.ChoiceField(choices={"date":"date","itemsCount":"available items","price":"price"},label="sort by")

class Card(forms.Form):
    cardNumber=forms.CharField(label="card number",widget=forms.NumberInput())
    mmyy=forms.CharField(label="MM/YY",widget=forms.NumberInput())
    cvc=forms.CharField(label="cvc",widget=forms.NumberInput())