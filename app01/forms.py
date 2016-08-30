from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(request = False,label = 'You e-mail address')
    message = forms.CharField(widgegt = forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Please enter more words")
        return message
    
    