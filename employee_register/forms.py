from django import forms
from .models import Employee


class EmployeeForm (forms.ModelForm):
    
    class Meta:
        model= Employee
        # fields='__all__'
        fields=('fullname','mobile','emp_code','position',)   # ingane cheythal nammak fields nte order okke ishtamulla pole change cheyyam
        
        #updating label texts 
        
        labels = {
            'fullname' : 'Fulll Name',
            'emp_code' : 'EMP .Code',
            'mobile' : 'Mobile',
            'position': 'Position',
                
            
        }
        
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = "select"
        self.fields['emp_code'].required = False



