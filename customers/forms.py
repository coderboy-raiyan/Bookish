from typing import Any
from django.contrib.auth.models import User
from .models import CustomerModel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import GENDER_TYPES


class UserSignUpForm(UserCreationForm):
    phone_no = forms.CharField(max_length=11)
    gender = forms.ChoiceField(choices=GENDER_TYPES)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email",
                  "phone_no", "gender", "street_address", "city"]

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
            phone_no = self.cleaned_data.get("phone_no")
            gender = self.cleaned_data.get("gender")
            street_address = self.cleaned_data.get("street_address")
            city = self.cleaned_data.get("city")

            CustomerModel.objects.create(
                phone_no=phone_no,
                gender=gender,
                street_address=street_address,
                city=city,
                user=user,
                customer_id=100000 + user.id
            )

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
