from django.forms import ModelForm, TextInput, Select, NumberInput
from datetime import date
from .models import Record,Category

class RecordForm(ModelForm):

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model   = Record
        fields  = ['date','description','category','cash','balance_type']
        widgets = {
            'date': TextInput(attrs={\
                        'id':'datepicker',\
                        'value':date.today().strftime('%Y-%m-%d'),\
                        'class':"form-control", 'style':"font-size:.875rem"                      
                    }),
            'description': TextInput(attrs={'class':"form-control", 'style':"font-size:.875rem"}),
            'category': Select(attrs={'class':"form-control", 'style':"font-size:.875rem"}),
            'cash': NumberInput(attrs={'class':"form-control", 'style':"font-size:.875rem"}),
            'balance_type': Select(attrs={'class':"form-control", 'style':"font-size:.875rem"}),
        }

