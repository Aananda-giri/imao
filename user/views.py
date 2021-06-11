from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProfilePicForm
from .models import ProfilePicModel, User
from jokes.models import WockaJokes
from jokes.views import index
from django.db.utils import DataError

from django.contrib.auth.decorators import login_required
import os

# Create your views here.

def UploadProfileView(request):
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            doc_to_save = request.FILES['image']
            filename = doc_to_save._get_name()
            return redirect(Profile)
            #return HttpResponse(filename)
 #       else:
#            return HttpResponse('Invalid Form')
    else:
        form = ProfilePicForm()
        return render(request, 'memes/index.html', {'form': form,'display_type':'/Upload/' })
#
def Profile(request):
    latest_profile_pic = ProfilePicModel.objects.order_by('-pub_date')[:1]
    for i in latest_profile_pic:
        latest_profile_pic = str(i.image).replace('user/static/','')
    

    #######////////////////// Change This to get real user detail \\\\\\\\\\\\\\\#########    

    user = User.objects.get(id=1)

    #######//////////////////Change This \\\\\\\\\\\\\\\#########
    
    
    return render(request, 'user/profile.html', {'profile_pic':latest_profile_pic,'user':user})

@login_required
def categoriesView(request):
    categories = [category['category'] for category in WockaJokes.objects.values('category').distinct()]
    #return HttpResponse(categories)
    if (request.user.is_authenticated):
        #return HttpResponse('HEllo' + request.user.username)
        username = request.user.username
    #try:
    user = User.objects.get(username=username)
    #Categories saved in user's database
    
    pre_selected_categories = user.preferred_categories
    if pre_selected_categories:
        unselected_categories=[i for i in categories if i not in pre_selected_categories]
    else:
        unselected_categories=categories
    if request.method == 'POST':
        #return HttpResponse('Purnika')
    #if form.is_valid():
        selected_categories = request.POST.get('selectedCategories')


        userSelectedCategories=[]
        for category in categories:
            #return HttpResponse(request.POST.get(category))
            if (request.POST.get(category)!=None):
                #return HttpResponse('Purnika')
                #return HttpResponse(str(category.value()))
                userSelectedCategories.append(str(category))
            #return HttpResponse('She is waiting. hurry up! ' + str(user))
        #    user = User(preferred_categories = userSelectedCategories)
        #    print(str(err))
        user.preferred_categories = userSelectedCategories
        user.save()
        #return HttpResponse('saved:\n\n'+str(userSelectedCategories))
        
        #user.save()
        #return HttpResponse(password)
        return redirect(index)
        #return render(request, 'jokes/index.html', {'message':'Account Created!'})

            #return render(request, 'jokes/login.html', {'RegisterErrorMessage':'Sorry! username already taken', 'authtype':'/Register/'})
    else:
        #return HttpResponse(str(unselected_categories))
        return render(request, 'user/pre_home_page.html',{'unselected_categories':unselected_categories,'pre_selected_categories':pre_selected_categories})



@login_required
def getUserDataView(request):
    if (request.user.is_authenticated):
        #return HttpResponse('HEllo' + request.user.username)
        username = request.user.username
    else:
        test=1
        #Code For Testing user is loggged in
        return HttpResponse('user/viwes.py line 102: Code For Testing user is loggged in')

    try:
        #Try because User table of logged in user is not created at first 
        user = User.objects.get(username=username)
        #return HttpResponse('Hello')
    except User.DoesNotExist as err:
        user = User(username=username)
        user.save()

    if request.method == 'POST':
        form = ProfilePicForm
        if form.is_valid():
            
        
        #return HttpResponse('Hello From Purnika!')
        #if form.is_valid():
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            relligion = request.POST.get('relligion')
            country = request.POST.get('country')
            user.first_name=first_name
            user.middle_name=middle_name
            user.last_name=last_name
            user.email=email
            user.phone_number=phone_number
            user.relligion = relligion
            user.her_country = country
            try:
                user.save()
            except DataError as err:
                #print(str(err))
                return render(request, 'user/pre_home_page.html',{'getUSerInfo':True,  'user':user,'message':'Please enter a valid phone number'})
            return redirect(categoriesView)
            
            #return HttpResponse('Saved: '+str(first_name)+str(middle_name)+str(last_name)+str(email)+str(phone_number)+str(relligion))
        
            #user.save()
            #return HttpResponse(password)
            #return render(request, 'jokes/mermaid.html', {'message':'Account Created!'})
            
                #return render(request, 'jokes/login.html', {'RegisterErrorMessage':'Sorry! username already taken', 'authtype':'/Register/'})
        else:
            #return HttpResponse('Purnika')
            return render(request, 'user/pre_home_page.html',{'getUSerInfo':True, 'user':user})
            
            







            #return HttpResponse('Purnika')
        
            '''
        
        
        
        
        
        
            if request.method == 'POST':
        upload_form = UploadMemeForm(request.POST, request.FILES)
        if upload_form.is_valid():
            meme=upload_form.save()
            #return HttpResponse(str(m.meme))
            doc_to_save = request.FILES['meme']
            #return HttpResponse(doc_to_save)
            filename = doc_to_save._get_name()
            #return HttpResponse(filename)
            client_id = '55d759dcb713183'
            client_secret = '3c2a1cf3af3422b25206ef718f191ea5a6ca8c82'
            print("\n\n\n Logging in ")
            client = ImgurClient(client_id, client_secret)
            print(" Logged in \n")
            album = None
            #return HttpResponse('memes/static/memes/images/'+str(filename))
            #meme = UploadMeme.objects.get(meme='memes/static/memes/images/'+str(filename))
            image_path = str(meme.meme)     #Because it returns FileField
            description ='test description'
            #name = str(meme.meme).split('/')[-1]
            config={
                "album":None,
                "name": filename,
                "title": request.POST.get('title'),
                "description": request.POST.get('description'),
            }
            print('\n\n\n Uploading \n\n\n' + str(meme))
            image=client.upload_from_path(image_path, config=config, anon=True)
            print(' path: ' + str(image['link']))
            
            meme.src=image['link']
            meme.save()
            os.remove(str(meme.meme))              #removing file from local directory
        
        
        '''
        
        
        
        
        
            
'''except Exception as ex:
            test=1
            #Code for testing What error has occoured
            return HttpResponse(str(ex)+'user/viwes.py line 118: Code For Testing user is loggged in')'''

        #return HttpResponse('Hello')
        #except 
