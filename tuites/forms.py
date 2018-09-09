from django import forms
from tuites.models import Tuite


class PostTuiteForm(forms.ModelForm):
    class Meta:
        model = Tuite
        fields = ('content', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widget = forms.HiddenInput()
        self.fields['content'].help_text='Digite o que você está pensando'
        self.fields['content'].widget = forms.Textarea()
        #self.fields['content'].widget = forms.TextInput(attrs={'class': 'post-tuite-input'}) #Para adicionar classe em um field

    # def clean_content(self): #Clean content é específico
    #     content = self.cleaned_data.get('content')
    #     if 'Temer' in content:
    #         raise forms.ValidationError (
    #             'FORA TEMER'
    #         )
    #     return cleaned_data

    def clean(self): #Clean é geral
        cleaned_data = super().clean()
        
        content = self.cleaned_data.get('content')
        if 'Temer' in content:
            raise forms.ValidationError (
                'FORA TEMER'
            )
        if not self.initial.get('user') == cleaned_data.get('author'):
            raise forms.ValidationError('Não tente burlar o sistema!')
        return cleaned_data