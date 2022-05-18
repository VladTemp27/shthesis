from django.forms import ModelForm
from dashboard.models import Document

class uploadDocument(ModelForm):
    class Meta:
        model = Document
        exclude = ('uploaderID',)
        fields = ['document','uploaderID']


