import os
from socket import fromshare
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def filename(self):
        return os.path.basename(self.file.name)