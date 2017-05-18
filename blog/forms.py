from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

'''
We need to import Django forms first (from django import forms) and, obviously, 
our Post model (from .models import Post).

PostForm, as you probably suspect, is the name of our form. 
We need to tell Django that this form is a ModelForm
(so Django will do some magic for us) – forms.ModelForm is responsible for that.

Next, we have class Meta, where we tell Django which model should be 
used to create this form (model = Post).

Finally, we can say which field(s) should end up in our form. 
In this scenario we want only title and text to be exposed – author should be the 
person who is currently logged in (you!) and created_date should be automatically 
set when we create a post (i.e. in the code), right?
'''
