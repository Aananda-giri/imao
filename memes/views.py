from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from user.models import User
from .forms import UploadMemeForm
from .models import UploadMeme, Meme, MemesComments, Feedbacks
from .models import ImgflipMemes as ImgflipMemesModel

from django.urls import reverse

from imgurpython import ImgurClient
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.core import serializers

import json
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UploadMemeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            doc_to_save = request.FILES['meme']
            filename = doc_to_save._get_name()
            return HttpResponse(filename)
    else:
        form = UploadMemeForm()
        return render(request, 'memes/index.html', {'form': form})

'''Reference: https://stackoverflow.com/questions/22831576/django-raises-multivaluedictkeyerror-in-file-upload/22832271'''
import os
def viewMemes(request):
    memes_list = UploadMeme.objects.all()
    memes=[]
    for meme in memes_list:
        memes.append(str(meme.meme).replace('memes/static/',''))
    context = {'memes_list':memes}
    print('Directory:'+str(os.getcwd()))
    return render(request, 'memes/MemeHome.html', context)


def toImagur(request):
    client_id = '55d759dcb713183'
    client_secret = '3c2a1cf3af3422b25206ef718f191ea5a6ca8c82'
    print("\n\n\n Logging in \n\n\n")
    client = ImgurClient(client_id, client_secret)
    memes_list = UploadMeme.objects.all()
    memes=[]
    for meme in memes_list:
        #memes.append(str(meme.meme).replace('memes/static/',''))
    #context = {'memes_list':memes}
    #return render(request, 'memes/MemeHome.html', context)
        album = None
        image_path = str(meme.meme)
        description ='test description'
        name = str(meme.meme).split('/')[-1]
        config={
            "album":album,
            "name": name,
            "title": "image title",
            "description": description,
        }
        print('\n\n\n Uploading \n\n\n' + str(meme))
        image=client.upload_from_path(image_path, config=config, anon=True)
        meme.src=image['link']
        meme.save()
        #removing file from local directory
        os.remove(str(memes_list[0].meme))
        print(' path: ' + str(image['link']))
    return HttpResponseRedirect(reverse(viewMemes))

def memes(request):
    form = UploadMemeForm()
    #return render(request, 'memes/MemeHome.html', {'upload_form': form})
    memes_list = UploadMeme.objects.all()
    context = {'memes_list':memes_list, 'upload_form': form}
    return render(request, 'memes/MemeHome.html', context)

@login_required
def upload(request):
    if request.method == 'POST':
        #return HttpResponse('I want Her')
        upload_form = UploadMemeForm(request.POST, request.FILES)
        if upload_form.is_valid():
            meme=upload_form.save()
            username = request.user.username
            meme.user_id = username
            meme.save()
            if request.POST.get('is_profile'):
                m=User.objects.get(username=username)
                m.profile_url = str(meme.meme)
                
            
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
            
            meme.url=image['link']
            meme.save()
            os.remove(str(meme.meme))              #removing file from local directory
            return HttpResponseRedirect(reverse(memes))
    else:
        return HttpResponse('I really want Her')

    
'''
https://i.imgur.com/gkvlh3L.jpg
'''
#client_id:55d759dcb713183
#client_seret:3c2a1cf3af3422b25206ef718f191ea5a6ca8c82

def ImgflipMemes(request):
    logged_in = False
    if (request.user.is_authenticated):
        logged_in = True
    memes_list=[]
    with open('imgflip.json', 'r') as f:
        memes_list = json.load(f)
        
    #for meme in Meme.objects.using('imgflip_memes').all().order_by('-imgflip_img_votes')[:15]:
    #    memes_list.append(meme)
    return render(request, 'memes/index.html', {'memes_list':memes_list[:15],'logged_in':logged_in})


def getMeme(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        newMax = request.GET.get("last_meme_id", None)
        #category = request.GET.get('category');
        #print('\n\n'+str(category) + str(type(category)))
    print('\n\n New Max' + str(newMax))
    
    memes_list = []
    
    with open('imgflip.json', 'r') as f:
        memes_list = json.load(f)
    #print(memes_list[(int(newMax)): (int(newMax)+10)])
    
    #memes = serializers.serialize('json', memes_list[(int(newMax)): (int(newMax)+10)], )
    memes = json.dumps(memes_list[(int(newMax)): (int(newMax)+50)])
    return JsonResponse({'memes_list' : memes}, status = 200)

@login_required
def vote(request):
    print('\n\n\nvoting\n\n\n')
    message=''
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        meme_id = request.GET.get("meme_id", None);
        vote = request.GET.get("vote", None)
    print('\n\n\nmeme_id:' + str(meme_id))
    '''if bool(vote):
        #print('category:{} {}'.format(category, str(category)=='Adult'))
        if str(category) == 'Adult':
            db = AbsurdlyBigJokes
        else:
            db = WockaJokes
            #return JsonResponse({'message':message }, status = 200)

        try:
            joke = db.objects.get(id= int(joke_id))
            print('\n\njoke:'+str(joke.body))
        except (KeyError, db.DoesNotExist):
            pass
            # Redisplay the question voting form.
            #return render(request, 'polls/detail.html', {
            #    'question': question,
            #    'error_message': "You didn't select a choice.",
            #})
        else:
            if user_have_not_voted_joke:'''
    if (request.user.is_authenticated):
        #return HttpResponse('Ill make ai')
        username = request.user.username
        '''print(username)
        meme = ImgflipMemesModel.objects.create(id=int(meme_id), user = User.objects.get(username=username), )
        meme = ImgflipMemesModel.objects.create(id=int(meme_id), user=username)
        meme.loves += 1
        meme.save(using='imgflip_memes')
        message = str(meme_id) + 'voted successfully.'
        print('\n\nCreating and Fucking voting meme freely'+str(type(int(meme_id))) + str(int(meme_id)+1))'''
    else:
        return HttpResponseRedirect(reverse(login))
    if bool(vote):
        #For upvotes
        try:
            print('\n\n\ntry blockk')
            #meme = ImgflipMemesModel.objects.get(id=int(meme_id), user = User.objects.get(username=username), )
            meme = ImgflipMemesModel.objects.get(id=int(meme_id))
            meme.loves += 1
            meme.save()
            print('\n\nFucking voting meme freely'+str(type(int(meme_id))) + str(int(meme_id)+1))
        except:
            #meme = ImgflipMemesModel.objects.create(id=int(meme_id), user = User.objects.get(username=username), )
            print('\n\n\n except blockk\n\n\n')
            meme = ImgflipMemesModel(id=int(meme_id), user = User.objects.using('default').get(username=username))
            meme.loves += 1
            
            #meme.save(using='imgflip_memes')
            meme.save()
            
            print('\n\n\n'+str(meme.loves)+'\n\n\n')
            message = str(meme_id) + 'voted successfully.'
            print('\n\nCreating and Fucking voting meme freely'+str(type(int(meme_id))) + str(int(meme_id)+1))
    else:
        #for downvotes
        print('\n\n\n else block')
        #meme = ImgflipMemesModel.objects.get(id=int(meme_id), user = User.objects.get(username=username))
        meme = ImgflipMemesModel.objects.get(id=int(meme_id))
        meme.loves -= 1
        meme.save()
        
        message = str(meme_id) + 'unvoted meme successfully.'
        print('\n\n unVoting:' + str(meme_id))
            
    #print('Loves : ' + str(db.objects.get(id=int(joke_id)).loves))
    #print(str(vote) +' of type'+ str(type(vote)))
    return JsonResponse({'message':message }, status = 200)

def getComments(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        meme_id = request.GET.get("meme_id", None);
        #return HttpResponse('hi')
    #print('\n\njoke_id:' + str(int(joke_id)))
    comments = ImgflipMemesModel.objects.get(id=int(meme_id)).memescomments_set.all()
    print(comments)
    comments = serializers.serialize('json', comments, )
    
    return JsonResponse({'comments':comments},status=200)

@login_required
def saveComment(request):
    
    if request.is_ajax and request.method == "POST":
        # get the nick name from the client side.
        comment = request.POST.get("comment", None);
        meme_id = request.POST.get("meme_id", None);
        
        #category = request.GET.get("category", None)
        print('\n\n\nComment : '+comment+'\n\n\n')
    if (request.user.is_authenticated):
        #return HttpResponse('Ill make ai')
        username = request.user.username
    else:
        return HttpResponseRedirect(reverse(login))
        
    if not str(comment).strip()=='':
        MemesComments.objects.create(body=str(comment), user_id=str(username), meme=ImgflipMemesModel.objects.get(id=int(meme_id)))
    return HttpResponse('Successfully commented')

def sitemap(request):
    return render(request, 'memes/sitemap(1).xml',)



def feedback(request):
    
    body=''
    if request.is_ajax and request.method == "POST":
        
        username = request.POST.get('username','')
        body = request.POST.get('feedback','')
        #summary = request.POST.get('summary')
        email = request.POST.get('email')
        
        print('\nbody:{} username:{} email:{}'.format(body, username, email))
    
    if (body!='' and username!=''):
        Feedbacks.objects.using('feedbacks').create(username=username, body=body, email=email)
        
        print('feedback saved')
        feedbacks = list(Feedbacks.objects.using('feedbacks').all().values_list('username', 'body'))[-1:]#serializers.serialize('json', list(Feedback.objects.all().values_list('username', 'body'))[-1:], )
        return JsonResponse({"Saved":True,'feedbacks':feedbacks}, status = 200)
    
    
    else:
        feedbacks = Feedbacks.objects.using('feedbacks').all().order_by('-pub_date').values_list('username', 'body')
        #print(feedbacks)
        return render(request, 'memes/feedbacks.html', {'feedbacks' : feedbacks})
