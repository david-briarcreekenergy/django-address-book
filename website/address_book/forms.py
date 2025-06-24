from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User


class UpdateUserPasswordForm(SetPasswordForm):

    class Meta:
        model = User
        fields = "new_password1, new_password2"

    def __init__(self, *args, **kwargs):
        super(UpdateUserPasswordForm, self).__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password1"].widget.attrs["placeholder"] = "New Password"
        self.fields["new_password1"].label = ""
        self.fields["new_password1"].help_text = (
            '<span class="form-text text-muted"><small>Required. 8 characters or more. Letters, digits and @/./+/-/_ only.</small></span>'
        )
        self.fields["new_password2"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs[
            "placeholder"
        ] = "Confirm New Password"
        self.fields["new_password2"].label = ""
        self.fields["new_password2"].help_text = (
            '<span class="form-text text-muted"><small>Required. 8 characters or more. Letters, digits and @/./+/-/_ only.</small></span>'
        )


class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
        required=False,
    )
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
        required=False,
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
        required=False,
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )


class UpdateContact(forms.ModelForm):
    # attrs here are bootstrap classes
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
        required=False,
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
        required=False,
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address"}
        ),
        required=False,
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
        required=False,
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}),
        required=False,
    )
    zipcode = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Zip Code"}
        ),
        required=False,
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Country"}
        ),
        required=False,
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "email",
            "address",
            "city",
            "state",
            "zipcode",
            "country",
            "image",
        )


class SignUpForm(UserCreationForm):
    # attrs here are bootstrap classes
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last name"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )

    class Meta:
        model = User
        fields = (
            "username",
            "last_name",
            "first_name",
            "email",
            "password1",
            "password2",
        )

    # this is for removing the labels and adding placeholders
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )
