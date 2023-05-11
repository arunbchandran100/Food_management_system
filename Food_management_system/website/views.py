from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User#, UserChangeForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .helpers import send_forget_password_mail
#import passlib.pwd  
from website.models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.shortcuts import render


# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'doner/index.html')

from django.contrib.auth import authenticate, login


def SignupPage(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        user_type = request.POST.get('user_type')
        print("First name:", fname)
        
        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            try:
                validate_password(pass1)
            except ValidationError as e:
                return HttpResponse("Password validation failed: " + str(e))
            
            
            my_user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=pass1)
            
            # Create profile object
            profile = Profile.objects.create(user=my_user, mobile=mobile,user_type=user_type)
            # Save user and profile objects
            my_user.save()
            profile.save()
            
            user = authenticate(request, username=email, password=pass1)
            login(request, user)
            return redirect('index')
    return render(request,'registeration/signup.html')


"""
class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'registeration//edit_profile.html'
    success_url = reverse_lazy('home')"""
    

@login_required(login_url='login')
def profile(request):
  if request.method == 'POST':
    return redirect(reverse('eprofile'))

  return render(request, 'registeration/view_profile.html')

"""
@login_required
def editprofile(request):
  if request.method == 'POST':
    # Get the data that the user submitted from the form.
    print("Test")
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    
    print("hi")
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Email:", email)
    
    #mobile = request.POST.get('mobile')
    #user_type = request.POST.get('user_type')

    # Validate the data and make sure that it is all correct.
    if not first_name:
      return render(request, 'edit_profile.html', {'error': 'First name is required'})
    if not last_name:
      return render(request, 'edit_profile.html', {'error': 'Last name is required'})
    if not email:
      return render(request, 'edit_profile.html', {'error': 'Email is required'})
    #if not mobile:
      #return render(request, 'edit_profile.html', {'error': 'Mobile number is required'})



    # Get the updated user object from the database

    # Update the user's profile details in the database


    # Save the updated user object to the database


    # Refresh the request user object with the updated data from the database




    # Update the user's profile details in the database.
    # Update the user's profile details in the database.
    my_user = User.objects.get(username=request.user.username)
    my_user.first_name = first_name
    my_user.last_name = last_name
    my_user.email = email
    my_user.save()
    #my_user.profile.mobile = mobile
    request.user = my_user
    #my_user.profile.save()
    #print first_name

    # Redirect the user back to the profile page.
    return redirect('vprofile')

  else:
    return render(request, 'registeration/edit_profile.html')
"""

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Get the data that the user submitted from the form.
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        user_type = request.POST.get('user_type')

        print("last name:", last_name)
        print("mobile:", mobile)

        # Update the user's profile details in the database.
        my_user = request.user
        my_user.first_name = first_name
        my_user.last_name = last_name
        my_user.email = email
        my_user.save()

        profile = Profile.objects.get(user=my_user)
        profile.mobile = mobile
        profile.user_type = user_type
        profile.save()
        

        # Redirect the user to the vprofile page.
        return redirect('vprofile')

    else:
        # If the request method is not POST, render the edit profile page.
        return render(request, 'registeration/edit_profile.html')


def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        user=authenticate(request,username=email,password=pass1)
        

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("email or Password is incorrect!!!")

    return render (request,'registeration/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def ChangePassword(request, token):
    context = {}
    
    
    try:
        user_obj = User.objects.filter(forget_password_token = token).first()
        context = {'user_id' : user_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change_password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'registeration/change_password.html' , context)


import uuid
def ForgetPassword(request,token):
    try:
        if request.method == 'POST':
            phone = request.POST.get('username')
            
            if not User.objects.filter(phone=phone).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget_password/')
            
            user_obj = User.objects.get(phone = phone)
            token = str(uuid.uuid4())
            user_obj= User.objects.get(user = user_obj)
            user_obj.forget_password_token = token
            user_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget_password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'registeration/forget_password.html')