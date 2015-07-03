from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    
    # The function name which used to validate values must be clean_message
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())

        if num_words < 4:
            errors = ["Not enough words!","Not enough words2!"]
            raise forms.ValidationError(errors)
        return message