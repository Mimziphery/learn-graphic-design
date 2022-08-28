import os
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def filename(self):
        return os.path.basename(self.file.name)