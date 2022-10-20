from audioop import add
import email
from email.message import Message
from multiprocessing import context
from os import remove
from xml.etree.ElementTree import Comment
from django.forms import PasswordInput
from django.shortcuts import render ,redirect
from django.contrib import messages
import bcrypt

from treeapp.models import Tree, User


def main_page(request):
    return render(request,"index.html")

def success(request):
    if "user_id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'trees':Tree.objects.all()
    }
    return render(request,"success.html",context)

def registration(request):
    form =request.POST
    errors=User.objects.basic_validator(form)
    if len(errors)>0:
        for key , val in errors.items():
            messages.error(request,val)
        return redirect('/')
    user = User.objects.create(first_name=form['first_name'],last_name=form['last_name']
    ,email=form['email'],password=bcrypt.hashpw(form['password'].encode(),bcrypt.gensalt()).decode())
    request.session["user_id"]= user.id
    return redirect('/dashboard')

def login(request):
    form =request.POST
    try:
        user=User.objects.get(email=form['email'])
    except:
        messages.error(request,'check youre email and password!')
        return redirect('/')
    if bcrypt.checkpw(form['password'].encode(),user.password.encode()):
        request.session['user_id']= user.id
        request.session['first_name'] = user.first_name
        return redirect('/dashboard')
    messages.error(request,'check youre email and password!')
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/') 

def add_tree_page(request):
    
    return render(request,'add_tree.html')

def add_tree(request):
    form =request.POST
    errors=Tree.objects.tree_validator(form)
    if len(errors)>0:
        for key , val in errors.items():
            messages.error(request,val)
        return redirect('/newTree')
    Tree.objects.create(
        species = request.POST['species'],
        location=request.POST['location'],
        reason = request.POST['reason'],
        planted_by = User.objects.get(id=request.session.get('user_id')),
        planted_at=request.POST["date"],
    )
    return redirect('/dashboard')

def details_page(request,tree_id):
    context={
        "tree":Tree.objects.get(id=tree_id)
    }
    return render(request,"details.html",context)

def account_page(request):
    user = User.objects.get(id=request.session['user_id'])
    context={
        'trees':Tree.objects.all(),
        'user':user,
    }
    return render(request,"account.html",context)

def delete(request,id):
    tree=Tree.objects.get(id=id)
    tree.delete()
    return redirect('/user/account')

def Update_page(request,id):
    context = {
        "tree": Tree.objects.get(id=id),
    }
    return render (request,"Update.html",context)

def edit(request,id):
    tree = Tree.objects.get(id=id)

    tree.species=request.POST['species']
    tree.location=request.POST['location']
    tree.reason=request.POST['reason']
    tree.created_at=request.POST['date']
    tree.save()
    return redirect(f'/edit/{id}')
    



