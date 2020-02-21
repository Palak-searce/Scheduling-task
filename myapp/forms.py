from django import forms
import datetime

def check_valid_date(value):
    try:
        y,m,d=map(int,value.split("-"))
    except ValueError:
        raise forms.ValidationError("Incorrect data format, should be YYYY-MM-DD")

    try:
        s=datetime.date(y,m,d)
        print("Date is valid.")
    except ValueError:
        raise forms.ValidationError("Invalid date !!")


class my_form(forms.Form):
    user = forms.CharField(label='Enter username')
    profile = forms.CharField(label='Enter user profile')
    s_date = forms.CharField(label='Enter StartDate',validators = [check_valid_date])
    e_date = forms.CharField(label='Enter EndDate',validators = [check_valid_date])
