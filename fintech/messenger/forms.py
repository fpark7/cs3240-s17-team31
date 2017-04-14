# importing forms
from django import forms
from messenger.models import Message

class MessageForm(forms.ModelForm):

    OPTIONS = (('Y', 'Yes'),
               ('N', 'No'),)

    is_encrypted = forms.ChoiceField(required=True, choices=OPTIONS, help_text="Encrypt this message?")
    message_title = forms.CharField(required=True, help_text="Subject")
    message_content = forms.CharField(required=True, help_text="Message Content", widget=forms.Textarea(attrs={'rows':6, 'cols': 20}))
    message_to = forms.CharField(required=True, help_text="Message Recipient")

    class Meta:
        model = Message
        fields = ("message_to", "message_title", "is_encrypted", "message_content")
