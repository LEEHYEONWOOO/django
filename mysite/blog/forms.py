from django import forms
from .models import Board1

class Board1Form(forms.ModelForm):
    class Meta:
        model = Board1
        fields = ['num','writer','pass_field','title','content','file1','boardid','regdate','readcnt','grp','grplevel','grpstep']


        