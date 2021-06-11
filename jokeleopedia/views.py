from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls.exceptions import NoReverseMatch

from django.urls import reverse

from jokes.models import WockaJokes
from user.views import getUserDataView as user_info


def Join(request):
    if request.user.is_authenticated:
        feedback='User Logged in!'
    else:
        feedback='Not loggen in!'
    
    if request.method == 'POST':
    #if form.is_valid():
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            #return HttpResponse('NSaved')
            #django.contrib.auth.logout()
            #logout(request) # To logout is user already logged in before registration
            user = User.objects.create_user(username, email, password)
            #Lastname = request.POST.get('lastname')
            #if Lastname:
            #    user.last_name = Lastname
            user.save()
            #User created
            
            #Logging in user
            #u = User.objects.get(username=username)
            #u.set_password(password)
            #u.save()
            #return HttpResponse('Saved')
            #return HttpResponse(password)

            #print('\n\n\n\n\nHello! they are waiting')
            #return HttpResponseRedirect(reverse(user_info))
            #return render(request, 'registration/login.html', {'feed':feedback, 'authtype':'/Register/', 'feedback':'Register nascent view'})
            return redirect(user_info)
            #return render(request, 'jokes/index.html')
        except IntegrityError as err:
            return render(request, 'registration/login.html',{'authtype':'/Register/','feed':'Hello', 'ErrorMessage':'Sorry! Username already taken. Please choose another username.'})
        except NoReverseMatch as err:
            return render(request, 'registration/login.html',{'authtype':'/Register/','feed':'Hello', 'ErrorMessage':'Please Fill Username, Email, Password'})
    
    #else:
    #    return render(request, 'mermaid.html')
            #return render(request, 'jokes/login.html', {'RegisterErrorMessage':'Sorry! username already taken', 'authtype':'/Register/'})
    else:
        return render(request, 'registration/login.html',{'authtype':'/Register/','feed':feedback})


from django.contrib.auth import logout
from django.contrib import messages
def logout_request(request):
    logout(request)
    print('\n\n\n\n\LoggedOut')
    messages.info(request, "Logged out successfully!")
    return redirect("/show")


        
    
    
