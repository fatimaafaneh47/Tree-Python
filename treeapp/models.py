from unittest import defaultTestLoader
from django.db import models
from distutils.log import error
from typing import Text
from django.db import models
import re 
from django.core.validators import validate_email

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors={}
        if len(post_data['first_name'])<1:
            errors['first_name']='please enter youre first name'
        if len(post_data['last_name'])<1:
            errors['last_name']='please enter youre last name'
        if len(post_data['first_name'])<2:
            errors['first_name']='first name should be at least 2 chcechtors'
        if len(post_data['last_name'])<2:
            errors['last_name']='first name should be at least 2 chcechtors'
        if len(post_data['password'])<2:
            errors['password']='first name should be at least 8 chcechtors'
        try: 
             validate_email(post_data['email'])
        except:
             errors['email']='please enter a valid email'
        if len(post_data['password'])<1:
            errors['password']='please enter a password'
        if post_data['password'] !=post_data['confirm_pw']:
            errors['confirm_pw'] ='youre password didnt match'
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    confirm_pw = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager() 

class TreeManager(models.Manager):
    
    def tree_validator(self, posted_data):
        errors = {}
        if len(posted_data['species']) < 5:
            errors['species'] = "Species must be at least 5 characters length!"
        if len(posted_data['location']) < 2:
            errors['location'] = "Location must be at least 2 characters length!"
        if len(posted_data['reason']) > 50:
            errors['reason'] = "Reason must be at most 50 characters length!"       
        return errors


class Tree(models.Model):
    species = models.CharField(max_length=255,default="Tree")
    location = models.CharField(max_length =255,null=True)
    reason = models.CharField(max_length=255,null=True)
    planted_by = models.ForeignKey(User, related_name="trees", on_delete = models.CASCADE,null=True)
    planted_at = models.DateField(null=True) 
    created_at=models.DateTimeField(auto_now_add=True,null =True)
    updated_at=models.DateTimeField(auto_now=True,null =True)
    objects = TreeManager() 
    


