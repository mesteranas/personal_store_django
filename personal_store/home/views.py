from django.shortcuts import render,redirect,get_object_or_404
from django.utils.translation import gettext_lazy as _,activate
from . import forms,models,currencyConverter
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models import Q
# Create your views here.
def home_(r,category="all",sort="date"):
    if r.method=="POST":
        form=forms.Items(r.POST)
        if form.is_valid():
            return redirect("Items",category=form.cleaned_data["category"],sort=form.cleaned_data["sort"])
    if category=="all":
        items=models.item.objects.all().order_by("-" + sort)
    else:
        items=models.item.objects.filter(category=category).order_by("-" + sort)
    form=forms.Items({"category":category,"sort":sort})
    return render(r,"home.html",{"items":items,"form":form})
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def changeLanguage(r):
    if r.method=="POST":
        language=r.POST["language"]
        activate(language)
        return redirect("homePage")
    return render(r,"changeLanguage.html")
def newaccound(r):
    if r.method=="POST":
        frm=forms.new_accound(r.POST)
        if frm.is_valid():
            fristName=frm.cleaned_data["frist_name"]
            lastName=frm.cleaned_data['last_name']
            email=frm.cleaned_data["email"]
            userName=frm.cleaned_data["user_name"]
            gender=frm.cleaned_data["gender"]
            password=frm.cleaned_data["password"]
            confpassword=frm.cleaned_data["confpassword"]
            currency=frm.cleaned_data["currency"]
            country=frm.cleaned_data["country"]
            address=frm.cleaned_data["address"]
            if not User.objects.filter(username=userName).exists():
                if password==confpassword:
                    user=User.objects.create_user(userName,email,password,first_name=fristName,last_name=lastName)
                    profile=models.Profile(user=user,gender=gender,country=country,currency=currency,address=address)
                    profile.save()
                    auth.login(r,user)
                    return redirect("homePage")

    frm=forms.new_accound()
    return render(r,"new-user.html",{"form":frm})
def login(r):
    if r.method=="POST":
        frm=forms.login(r.POST)
        if frm.is_valid():
            user_name=frm.cleaned_data["user_name"]
            password=frm.cleaned_data["password"]
            user=auth.authenticate(username=user_name,password=password)
            if user:
                auth.login(r,user)
                return redirect("homePage")
    frm=forms.login()
    return render(r,"login.html",{"form":frm})
@login_required
def logout(r):
    auth.logout(r)
    return redirect("homePage")
@login_required
def settings(r):
    return render(r,"profile.html")
@login_required
def deletacc(r):
    if r.method=="POST":
        frm=forms.delete(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["password"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                User.delete(user1)
                return redirect("homePage")
    frm=forms.delete()
    return render(r,"deleteAccount.html",{"form":frm})
@login_required
def changePassword(r):
    if r.method=="POST":
        frm=forms.ChangePassword(r.POST)
        if frm.is_valid():
            password=frm.cleaned_data["currentPassword"]
            newpassword=frm.cleaned_data["newPassword"]
            confnewpassword=frm.cleaned_data["confNewPassword"]
            user1=User.objects.get(username=r.user)
            if user1.check_password(password):
                if newpassword==confnewpassword:
                    user1.set_password(newpassword)
                    user1.save()
                    auth.login(r,user1)
                    return redirect("homePage")
    frm=forms.ChangePassword()
    return render(r,"change_password.html",{"form":frm})
@login_required
def changeProfiel(r):
    user1=User.objects.get(username=r.user)
    profile=models.Profile.objects.get(user=user1)
    if r.method=="POST":
        frm=forms.editProfile(r.POST)
        if frm.is_valid():
            firstname=frm.cleaned_data["first_name"]
            lastname=frm.cleaned_data["last_name"]
            email=frm.cleaned_data["email"]
            country=frm.cleaned_data["country"]
            currency=frm.cleaned_data["currency"]
            address=frm.cleaned_data["address"]
            user1.first_name=firstname
            user1.last_name=lastname
            user1.email=email
            user1.save()
            profile.currency=currency
            profile.country=country
            profile.address=address
            profile.save()
    frm=forms.editProfile({"first_name":user1.first_name,"last_name":user1.last_name,"email":user1.email,"country":profile.country,"currency":profile.currency,"address":profile.address})
    return render(r,"change_profile.html",{"form":frm})
def viewItem(r,pk):
    item=get_object_or_404(models.item,pk=pk)
    if r.user.is_authenticated:
        user=get_object_or_404(User,username=r.user)
        profile=get_object_or_404(models.Profile,user=user)
        currencyValue=str(currencyConverter.convert("USD",profile.currency,item.price))+profile.currency
    else:
        currencyValue="please login firstly to able to convert to your currency"
    
    return render(r,"viewItem.html",{"item":item,"currencyValue":currencyValue})
def comment(r,pk):
    item=get_object_or_404(models.item,pk=pk)
    comments=models.comment.objects.filter(Item=item).order_by("-date")
    if r.method=="POST":
        user=get_object_or_404(User,username=r.user)
        frm=forms.Comment(r.POST)
        if frm.is_valid():
            content=frm.cleaned_data["content"]
            NewComment=models.comment(user=user,Item=item,content=content)
            NewComment.save()
    frm=forms.Comment()
    return render(r,"comments.html",{"comments":comments,"form":frm})
@login_required
def deleteComment(r,itemPk,commentPk):
    user=get_object_or_404(User,username=r.user)
    item=get_object_or_404(models.item,pk=itemPk)
    comment=get_object_or_404(models.comment,pk=commentPk)
    if comment.user!=user:
        return Http404("you can't delete this comment")
    if r.method=="POST":
        comment.delete()
        return redirect("homePage")
    return render(r,"deleteComment.html")
def search(r):
    results=[]
    if r.method=="POST":
        results=models.item.objects.filter(Q(name__icontains=r.POST["search"])).order_by("-date")
    return render(r,"search.html",{"results":results})
def buy(r,pk):
    frm=forms.Card()
    return render(r,"buy.html",{"form":frm})