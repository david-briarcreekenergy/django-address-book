from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.contrib import messages
from .forms import UpdateContact, SignUpForm, UpdateUserForm, UpdateUserPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.error(request, "Error logging in")
            return render(request, "login.html", {})
    else:
        return render(request, "login.html", {})


def register_user(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)

            login(request, user)

            messages.success(request, "Login successful.  Welcome!")

            return redirect("home")
        else:
            messages.error(
                request,
                "Something went wrong with your registration. Please try again.",
            )
            return redirect("register")

    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.filter(user=request.user).order_by(
            "last_name", "first_name"
        )
        return render(request, "home.html", {"contacts": contacts})
    else:
        return redirect("login")


def about(request):
    return render(request, "about.html", {})


# pk - primary key
@login_required()
def contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)

    if request.user == contact.user:
        # this form is for updating the contact and uploading the image
        # request.FILES is for uploading the image
        form = UpdateContact(
            request.POST or None, request.FILES or None, instance=contact
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Contact Successfully Updated")

        return render(request, "contact.html", {"contact": contact, "form": form})

    else:
        messages.error(request, "You are not authorized to edit this contact")
        return redirect("home")

    # return render(request, "contact.html", {"contact": contact, "form": form})


@login_required()
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)

    if request.user == contact.user:
        contact.delete()
        messages.success(request, "Contact has been deleted")
        return redirect("home")
    else:
        messages.error(request, "You are not authorized to delete this contact")
        return redirect("home")


@login_required()
def add_contact(request):
    # this form is for adding a new contact and uploading the image
    # request.FILES is for uploading the image
    form = UpdateContact(request.POST or None, request.FILES or None)

    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.user = request.user
        new_contact.save()
        messages.success(request, "Contact Added")
        return redirect("contact", pk=new_contact.id)

    return render(request, "add_contact.html", {"form": form})


def update_user(request):

    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            # django logs user out after updated
            login(request, current_user)
            messages.success(request, "User successfully updated")
        # else:
        #     messages.error(request, "Error attempting to update user")

        return render(request, "update_user.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to update your information")
        return redirect("login")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == "POST":
            form = UpdateUserPasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, current_user)
                messages.success(request, "Password Updated")
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect("update_password")
        else:
            form = UpdateUserPasswordForm(current_user)
            return render(request, "update_password.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to update the user password")
        return redirect("login")
