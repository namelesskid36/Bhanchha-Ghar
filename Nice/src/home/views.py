from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout ,  update_session_auth_hash
from django.http import JsonResponse
from . models import *
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def show_contactus(request):
    return render(request, 'home/ContactUs.html')
def show_successLogin(request):
    return render(request, 'home/LoginSuccess.html')

def show_selectRegister(request):
    return render(request, 'home/Register.html')

def recipie(request):
    return render(request, 'home/Recipes.html')

def show_login(request):

    if request.method =='POST':
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        if not email or not password:
            return HttpResponse("Please fill in all fields. Some fields are empty or only contain spaces.")
        try:
            user_profileEmail = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return HttpResponse("No user with this email address exists.")
        user = authenticate(request, username=user_profileEmail.user , password=password)
        if user is not None:
            login(request,user)
            user_profile = UserProfile.objects.get(user=user) 
            if user_profile.accountType == "regular":
                return redirect("/Users")
            if user_profile.accountType == "broker":
                return redirect("/Chefs")
            else:
                return HttpResponse("Error login")
        else:
            return HttpResponse("Email or Password Incorrect")
    return render(request, 'home/login.html')

def show_logout(request):
    logout(request)
    return redirect('/')


def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email(email, code, username):
    subject = "Welcome to BhanchaGhar - Verify Your Email"
    message = (
        f"Dear {username},\n\n"
        "Greetings from BhanchaGhar! We are thrilled to welcome you to our community, where you can discover a plethora of culinary delights and connect with professional chefs to elevate your dining experience.\n\n"
        "Once your email is verified, you will gain access to a comprehensive range of features, including:\n"
        "1. Extensive Recipe Search: Explore a vast collection of recipes tailored to your preferences and dietary needs.\n"
        "2. Chef Profiles: Browse and hire top chefs, view their profiles, and read reviews from other users.\n"
        "3. Ordering Services: Place orders directly with chefs for personalized culinary experiences.\n\n"
        f"Your Verification Code: {code}\n\n"
        "Thank you for choosing BhanchaGhar. We look forward to helping you discover new recipes and connect with exceptional culinary talents.\n\n"
        "Warm regards,\n"
        "The BhanchaGhar Team"
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def show_registerBroker(request):
    if request.method == 'POST':
        uname = request.POST.get("username").strip()
        contact_number = request.POST.get("contactnumber").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        confirm_password = request.POST.get("confirm-password").strip()
        gender = request.POST.get("gender").strip()
        profile_picture = request.FILES.get('profile-picture')
        resume = request.FILES.get('resume')
        accountType = "broker"

        if not uname or not contact_number or not email or not password or not confirm_password:
            return HttpResponse("Please fill in all fields. Some fields are empty or only contain spaces.")

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists. Please choose a different email.")

        if UserProfile.objects.filter(contact_number=contact_number).exists():
            return HttpResponse("Contact number already exists. Please choose a different contact number.")

        if password != confirm_password:
            return HttpResponse("Your password and confirm password must be the same.")

        if profile_picture:
            file_extension = profile_picture.name.split('.')[-1].lower()
            if file_extension not in ["jpg", "jpeg", "png", "gif"]:
                return HttpResponse("Please upload only image files (jpg, jpeg, png, gif).")
            profile_picture_name = profile_picture.name
        else:
            profile_picture_name = None

        if resume:
            file_extension = resume.name.split('.')[-1].lower()
            if file_extension not in ["jpg", "jpeg", "png", "gif", "pdf"]:
                return HttpResponse("Please upload only valid files (jpg, jpeg, png, gif, pdf).")
            resume_name = resume.name
        else:
            resume_name = None

        verification_code = generate_verification_code()
        send_verification_email(email, verification_code, uname)

        request.session['registration_data'] = {
            'username': uname,
            'contact_number': contact_number,
            'email': email,
            'gender': gender,
            'profile_picture_name': profile_picture_name,
            'resume_name': resume_name,
            'password': password,
            'accountType': accountType,
            'verification_code': verification_code,
        }

        return redirect('/EMVChefs')

    return render(request, 'home/ChefsRegister.html')

from django.db import IntegrityError


def verify_emailbroker(request):
    if request.method == 'POST':
        input_code = request.POST.get("verification_code").strip()
        registration_data = request.session.get('registration_data')

        if not registration_data:
            return HttpResponse("Session expired. Please register again.")

        if input_code == registration_data['verification_code']:
            try:
                user = User.objects.create_user(
                    registration_data['username'],
                    registration_data['email'],
                    registration_data['password']
                )
                user.save()
            except IntegrityError:
                return HttpResponse("Username already exists. Please choose a different username.")

            profile_picture_name = registration_data.get('profile_picture_name')
            resume_name = registration_data.get('resume_name')

            profile = UserProfile(
                user=user,
                contact_number=registration_data['contact_number'],
                email=registration_data['email'],
                gender=registration_data['gender'],
                profile=f'static/pfps/{profile_picture_name}' if profile_picture_name else None,
                resume=f'static/Resumes/{resume_name}' if resume_name else None,
                accountType=registration_data['accountType']
            )
            profile.save()

            del request.session['registration_data']

            return redirect('/LoginSuccess')
        else:
            return HttpResponse("Invalid verification code.")

    return render(request, 'home/EMVChefs.html')

def show_registerRegular(request):
    if request.method == 'POST':
        uname = request.POST.get("username").strip()
        contact_number = request.POST.get("contactnumber").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        confirm_password = request.POST.get("confirm-password").strip()
        gender = request.POST.getlist("gender")
        profile = request.FILES.get('profile-picture')
        accountType = "regular"

        if not uname or not contact_number or not email or not password or not confirm_password:
            return HttpResponse("Please fill in all fields. Some fields are empty or only contain spaces.")
        
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists. Please choose a different username.")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists. Please choose a different email.")

        if UserProfile.objects.filter(contact_number=contact_number).exists():
            return HttpResponse("Contact number already exists. Please choose a different contact number.")

        if password != confirm_password:
            return HttpResponse("Your password and confirm password must be the same.")

        if profile:
            file_extension = profile.name.split('.')[-1].lower()
            if file_extension not in ["jpg", "jpeg", "png", "gif"]:
                return HttpResponse("Please upload only image files (jpg, jpeg, png, gif).")

        # Generate verification code and send email
        verification_code = generate_verification_code()
        send_verification_email(email, verification_code, uname)

        # Temporarily store the user data in session
        request.session['registration_data'] = {
            'username': uname,
            'contact_number': contact_number,
            'email': email,
            'gender': gender,
            'profile': profile.name if profile else None,
            'password':password,
            'accountType': accountType,
            'verification_code': verification_code,
        }

        # Redirect to verification page
        return redirect('/EMVUsers')
        

    return render(request, 'home/UsersRegister.html')

def verify_emailregular(request):
    if request.method == 'POST':
        input_code = request.POST.get("verification_code").strip()
        registration_data = request.session.get('registration_data')

        if not registration_data:
            return HttpResponse("Session expired. Please register again.")

        if input_code == registration_data['verification_code']:
            # Create the user account and save the data to the database
            user = User.objects.create_user(
                registration_data['username'],
                registration_data['email'],
                registration_data['password']
            )
            user.save()

            profile = UserProfile(
                user=user,
                contact_number=registration_data['contact_number'],
                email=registration_data['email'],
                gender=registration_data['gender'],
                profile=registration_data['profile'],
                accountType=registration_data['accountType']
            )
            profile.save()

            # Clear the session data
            del request.session['registration_data']

            return redirect('/LoginSuccess')
        else:
            return HttpResponse("Invalid verification code.")

    return render(request, 'home/EMVUsers.html')

def show_product(request):
    return render(request, 'home/Users.html')

from django.urls import reverse

def some_view(request):
    return redirect(reverse('ChefsProfile'))

def show_Food(request):
    chefs = Chef.objects.all()
    return render(request, 'home/ChefsProfiles.html', {'chefs': chefs})

def show_productBroker(request,):
    return render(request, 'home/Chefs.html')

@login_required
def show_AddProduct(request):
    if request.method == 'POST':
        title = request.POST.get("title").strip()
        price = request.POST.get("price").strip()
        location = request.POST.get("location").strip()
        description = request.POST.get("description").strip()
        img = request.FILES.get('profile-picture')
        user = request.user  # Use the User instance directly

        if not title or not price or not location or not description:
            return HttpResponse("Please fill in all fields. Some fields are empty or only contain spaces.")
        
        if img:
            file_extension = img.name.split('.')[-1].lower()
            if file_extension not in ["jpg", "jpeg", "png", "gif"]:
                return HttpResponse("Please upload only image files (jpg, jpeg, png, gif).")
            
        chef = Chef.objects.create(
            user=user,
            title=title,
            price=price,
            location=location,
            description=description,
            img=img
        )
        chef.save()
        messages.add_message(request, messages.SUCCESS, 'Chef Profile Added successfully')
        return redirect('Foods')  # Ensure this matches your URL name
    
    return render(request, 'home/AddProfiles.html')


@login_required
def show_MyProduct(request):
    chefs = Chef.objects.filter(user=request.user)
    return render(request, 'home/MyProfile.html', {'chefs': chefs})



@login_required
def show_updateProduct(request, chef_id):
    instance = get_object_or_404(Chef, id=chef_id)

    if request.method == "POST":
        title = request.POST.get("title").strip()
        price = request.POST.get("price").strip()
        location = request.POST.get("location").strip()
        description = request.POST.get("description").strip()
        img = request.FILES.get('room-picture')

        if not title or not price or not location or not description:
            messages.add_message(request, messages.ERROR, "Please fill in all fields. Some fields are empty or only contain spaces.")
        else:
            instance.title = title
            instance.price = price
            instance.location = location
            instance.description = description

            if img:
                file_extension = img.name.split('.')[-1].lower()
                if file_extension in ["jpg", "jpeg", "png", "gif"]:
                    instance.img = img
                else:
                    messages.add_message(request, messages.ERROR, "Please upload only image files (jpg, jpeg, png, gif).")
                    return render(request, 'home/UpdateChefProfiles.html', {'chef': instance})
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Chef Profile updated successfully')
            return redirect('MyProduct')

    return render(request, 'home/UpdateChefProfiles.html', {'chef': instance})


@login_required
def show_deleteProduct(request, chef_id):
    instance = get_object_or_404(Chef, id=chef_id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "Product Deleted successfully")
    return redirect('MyProduct')


def product_detail(request, chef_id):
    chef = get_object_or_404(Chef, id=chef_id)
    return render(request, 'home/ChefsProfileDetails.html', {'chef': chef})


def show_profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

        context = {
            'user_profile': user_profile,
        }

        return render(request, 'home/Profile.html', context)
    
    return render(request, 'home/Profile.html', {})



@login_required
def update_profile(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new-password')
        confirm_new_password = request.POST.get('confirm-new-password')
        contact_number = request.POST.get('contactnumber')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        profile = request.FILES.get('profile-picture')

        user = request.user

        # Check if the provided password is correct
        if not user.check_password(password):
            messages.error(request, 'Incorrect password. Please try again.')
            return redirect('update_profile')  # Redirect back to update profile page

        try:
            # Retrieve UserProfile associated with the User
            user_profile = user.userprofile
        except UserProfile.DoesNotExist:
            messages.error(request, 'User profile does not exist.')
            return redirect('update_profile')  # Redirect back to update profile page

        # Update UserProfile fields
        user_profile.contact_number = contact_number
        user_profile.gender = gender
        if profile:
            user_profile.profile = profile
        user_profile.save()

        # Update User email if changed
        if user.email != email:
            user.email = email
            user.save()

        # Change password if new password is provided
        if new_password:
            if new_password != confirm_new_password:
                messages.error(request, 'New passwords do not match. Please try again.')
                return redirect('updateprofile')  # Redirect back to update profile page
            
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Update session with new password hash

        messages.success(request, 'Profile updated successfully.')
        return redirect('Profile')  # Redirect to profile view or home after successful update

    return render(request, 'home/UpdateProfile.html', {'user': request.user})
