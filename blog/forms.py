# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:46:12 2023

@author: PC
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)