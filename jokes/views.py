from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import WockaJokes, UploadJokes, Feedbacks, Jokes, JokeComments
from django.template import loader

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import WockaJokes, Comments, ShortedList, AbsurdlyBigJokes
from user.models import User
#from user.views import categoriesView
from .forms import UploadJokeForm, SearchForm, sendMailForm

from rest_framework.decorators import api_view
import json
import random

from django.http import JsonResponse
from django.core import serializers

#from .forms import NameForm, ProductForm

# Create your views here.

def bubbleSort(arr): 
#"Bubble Short" to short joke_list on jokes based on funney
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j].funney > arr[j+1].funney : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(list(set(arr)))



'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
def anonIndex(request):
    categories = [category['category'] for category in WockaJokes.objects.values('category').distinct()]
    if request.method == 'POST':
        if request.POST.get('category'):
            return HttpResponse(request.POST.get('category'))
            Comments.appendReadIds()
        search_form = SearchForm(request.POST)
        '''comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment=request.POST.get('comment')'''
    #return HttpResponseRedirect(reverse(index))
    return HttpResponse('I am independent & want her')
    
#@login_required
def index(request, joke_id=-1):
    category='none'
    #updateShortedList()
    form = UploadJokeForm()
    search_form = SearchForm()
    latest_joke_list=[]
    categories = [category['category'] for category in WockaJokes.objects.values('category').distinct()]
    categories.append('Adult')
    
    logged_in = False
    if (request.user.is_authenticated):
        #return HttpResponse('Ill make ai')
        username = request.user.username
        logged_in = True
                
    if request.method == 'POST':
        #############################################
        ###********For Comment Operation*********###
        ############################################
        search_form = SearchForm(request.POST)
        if request.POST.get('comment'):
            Comments.appendReadIds()
            

            #return HttpResponse('Ill make ai')
            joke_id=request.POST.get('joke_id')
            comment=request.POST.get('comment')
            #return HttpResponse(username)
            #return HttpResponse(str(joke_id)+'\n\n'+str(comment))
            if not str(comment).strip()=='':
                Comments.objects.create(body=comment, user_id=username,wockajokes_id=joke_id)
            return HttpResponseRedirect(reverse(index))
        
        #############################################
        ###********For Search operation*********###
        ############################################

        elif search_form.is_valid():
            #return HttpResponse('OK!')
            #return HttpResponse(request.POST.get('search_term'))
            
            '''comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
            comment=request.POST.get('comment')'''
            
            
            latest_joke_list = WockaJokes.objects.annotate(
                search=SearchVector('title','body','author'),
            ).filter(search=request.POST.get('search_term')).order_by('-funney')
            #id_set=[1,2,3]
            #latest_joke_list = WockaJokes.objects.filter(id__in =id_set)
            #search_form.save()
            #return HttpResponse(latest_joke_list)
            #latest_joke_list=bubbleSort(latest_joke_list)
            #print('\n\n\n\n\n'+str(type(latest_joke_list)))
            
            #return render(request, 'jokes/index.html', context)
            #return HttpResponse(latest_joke_list)
            #context = {'latest_joke_list': latest_joke_list, 'form':form,'search_form':search_form}
            #return render(request, 'jokes/index.html', context)
        
        #############################################
        ###******** For category selection *********###
        ############################################
        elif request.POST.get('category'):
            category = request.POST.get('category')
            if category == 'Adult':
                latest_joke_list = AbsurdlyBigJokes.objects.all()[:15]
                #total_jokes = int(WockaJokes.objects.all().order_by("-id")[0].id) + int(UploadJokes.objects.all().order_by("-id")[0].id)
                context = {'latest_joke_list': latest_joke_list, 'form':form,'search_form':search_form, 'categories':categories, 'category':category, 'logged_in': logged_in}
                return render(request, 'jokes/index.html', context)
                
                
                
                
                
                
                
                
                
                
            else:
                ids_list = ShortedList.objects.filter(category=category)[0].shortedids[:15]
                latest_joke_list = WockaJokes.objects.filter(id__in=ids_list)
            
            ''' gets first 15 jokes from selected categories '''
            
                        
            #return HttpResponse(latest_joke_list[0])
    elif request.user.is_authenticated:
#    latest_joke_list = WockaJokes.objects.order_by('-pub_date')[:5]
        #latest_joke_list = WockaJokes.objects.order_by('-funney')[:50]
        jokes=[]
        #preferred_categories =[]
        preferred_categories_raw=User.objects.values('preferred_categories')#['Other / Misc']
        preferred_categories = [a['preferred_categories'] for a in preferred_categories_raw if a['preferred_categories']!=None]
        try:
            preferred_categories = preferred_categories[0]
        except IndexError:
            preferred_categories = []
            #redirect(categoriesView)
        
        for categ in preferred_categories:
            jokes = WockaJokes.objects.filter(category = categ).order_by('-funney')
            for joke in jokes:
                latest_joke_list.append(joke)
        #"Bubble Short" to short joke on jokes based on funney
        latest_joke_list=bubbleSort(latest_joke_list)[:25]
        #jokes=jokes.order_by('-funney')
        #******************************************************
        ################## Optimize for website ##############
        #******************************************************
                

        #context = {'latest_joke_list': latest_joke_list, 'form':form,'search_form':search_form}


    #return render(request, 'jokes/index.html', context,{'form':form})
        #return render(request, 'jokes/index.html', context)
        #form = AddJokeForm()
        #return render(request, 'jokes/index.html', {'form':form})
    
    else:
        favourite_ids=[]
        #print('\n\n\n\n\n\nHello\n\n\n\n\n')
        with open('jokes/wockaFavList.json', 'r') as f:
            favourite_ids=json.load(f)
        
        latest_joke_list = WockaJokes.objects.filter(id__in=favourite_ids[0:15])
    try:
        total_jokes = int(WockaJokes.objects.all().order_by("-id")[0].id) + int(UploadJokes.objects.all().order_by("-id")[0].id)
    except:
        total_jokes=[]
    context = {'latest_joke_list': latest_joke_list, 'form':form,'search_form':search_form, 'categories':categories, 'total_jokes':total_jokes, 'category':category, 'logged_in':logged_in}
    '''
    category : category for returning category_name to view[getJoke()] from index.html with ajax for appending jokes at bottom of the page 
    '''
    template_name = 'jokes/index.html'
    return render(request, template_name, context)

    
    '''latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
    jokes=''
    for joke in latest_joke_list:
        temp = joke.joke_title + '<br>' + joke.joke_statement + '<br><br>'
        jokes += temp
    return HttpResponse(jokes)'''
    #    return HttpResponse(jokee.joke_statement)
    '''#given:
    latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.joke_statement for q in latest_joke_list])
    return HttpResponse(output)'''
# Leave the rest of the views (detail, results, vote) unchanged

#To update shorted list of jokes for each category
#Recall Perodically
def updateShortedList():
    categories = [category['category'] for category in WockaJokes.objects.values('category').distinct()]
    
    print('Obtained Categories')
    for category in categories:
        
        try:
            shorted = ShortedList.objects.create(category=category)
        except Exception as ex:
            shorted = ShortedList.objects.get(category=category)
        
        print('Gettind data for category:  ' + str(category))
        shorted.shortedids = [j.id for j in  WockaJokes.objects.filter(category=category).order_by('-funney')]
        shorted.save()
        print('Updated   category:'+str(category))
        
        #To update favourites from local wockaFavList.json file
        favourite_ids=[]
        with open('jokes/wockaFavList.json', 'r') as f:
            favourite_ids=json.load(f)
        try:
            shorted = ShortedList.objects.create(category='WockaFavourites')
        except Exception as ex:
            shorted = ShortedList.objects.get(category='WockaFavourites')
        
        shorted.shortedids = [j.id for j in  WockaJokes.objects.filter(category='WockaFavourites').order_by('-funney')]
        shorted.save()
        print('Updated   Favourites:')
        
        
        
def stupidstuff(request):
    latest_joke_list = StupidStuffJokes.objects.order_by('rating')[:15]
    context = {'latest_joke_list': latest_joke_list}
    return render(request, 'jokes/stupidstuff.html', context)



def results(request, joke_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % joke_id)

def vote(request):
    #return HttpResponse(request.POST['choice'])
    joke = get_object_or_404(WockaJokes, id=request.POST['choice'])
    joke.love += 1
    joke.save()
    return HttpResponseRedirect(reverse(index))
    #return HttpResponse("You're voting on question %s." % joke.id)

def test(request):
    latest_joke_list = Joke.objects.order_by('-pub_date')[:5]
    context = {'latest_joke_list': latest_joke_list}
    return render(request, 'jokes/test.html', context)
    
def taste(request):
	return render(request, 'jokes/taste.html',)


def ttaste(request):
	return render(request, 'jokes/ttaste.html',)

@login_required
def uploadJokeView(request):
    if request.method == 'POST':
        form = UploadJokeForm(request.POST)
        if form.is_valid():
        
            UploadJokeObj= form.save()
            UploadJokeObj.save(using='user_uploaded')
            print('\n\n\n\nSaving:',form)

            #return render(request, 'jokes/index.html', context)
            return HttpResponse('Congratulations You have successfully added a joke!')
    else:
        form = AddJokeForm()
        return render(request, 'jokes/index.html', {'form':form})
    
#For Sending Mail
from django.core.mail import send_mail
def SendMail(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            if send_mail(
                'request.POST.get("subject")',
                'request.POST.get("message")',
                'amaryesh123456@gmail.com',
                ['request.POST.get("recepients")'],
                fail_silently=False,):
                feedback=''
                context={'feedback':'Message sent successfully!','form':MailForm()}
            else:
                context={'feedback':'Sorry Error occured','form':MailForm()}
    else:
        return render(request, 'jokes/mail.html',{'form':form})
	

        form = CommentForm()
    return render(request, 'jokes/name.html', {'form': MailForm()})


from django.core.mail import send_mail
#@login_required
def sendMail(request):
    if request.method == 'POST':
        mailForm = sendMailForm(request.POST)
        if mailForm.is_valid():
            mailfrom = 'amaryesh123456@gmail.com'
            mailto = 'jokeleopedia@gmail.com'
            #mailto = request.POST.get('mailto')
            message = request.POST.get('message')
            subject = request.POST.get('summary')
            sender = request.POST.get('Your_email_address')
            subject = str(subject) + '-from:' + str(sender)
        #return HttpResponse(str(mailto))
        if send_mail(
            subject,
            message,
            mailfrom,
            [mailto],
        fail_silently=False,
        ):
            return HttpResponseRedirect(reverse(index))
        else:
            return HttpResponse('Mail not sent')
    else:
        return render(request, 'jokes/feedback.html', {'form':sendMailForm()})

def getJoke(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        newMax = request.GET.get("last_joke_id", None)
        category = request.GET.get('category');
        #print('\n\n'+str(category) + str(type(category)))
        
        if category=='none':
            with open('jokes/wockaFavList.json', 'r') as f:
                ids_list = json.load(f)
        
        elif category == 'Adult':
            #ids_list = ShortedList.objects.filter(category=category)[0].shortedids[:]
            latest_joke_list = list(AbsurdlyBigJokes.objects.all()[(int(newMax)): (int(newMax)+10)])
            latest_joke_list = serializers.serialize('json', latest_joke_list, )
            return JsonResponse({"valid":False,'jokes':latest_joke_list}, status = 200)
        
        else:
            ids_list = ShortedList.objects.filter(category=category)[0].shortedids[:]
            #latest_joke_list=WockaJokes.objects.filter(id__in=ids_list)
    
        #print('\n\n'+str(newMax) + str(type(newMax)))
        
        #ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
    #print('\n\n'+ str(type(int(newMax))) + '\n\n\n' + str(newMax) + '\n\n\n' )
    
    #temp++
    #if(temp < newMax):
        #temp=newMax
    #if(temp >= int(newMax)):
    #    return JsonResponse({'repeat':True})
    
    
        
    #newMax = 5 + int(newMax)
    latest_joke_list = list(WockaJokes.objects.filter(id__in = ids_list[(int(newMax)): (int(newMax)+10)]))
    #context = {'latest_joke_list': latest_joke_list}
            
    #instance = latest_joke_list
    latest_joke_list = serializers.serialize('json', latest_joke_list, )
    #return JsonResponse({"instance": ser_instance}, status=200)
    return JsonResponse({"valid":False,'jokes':latest_joke_list}, status = 200)
    #return JsonResponse({'repeat':True})
    '''    for count, joke in enumerate(latest_joke_list):
        return HttpResponse(joke.id)
        jokes[newMax+count] = {'id':joke.id, 'title':joke.title, 'body':joke.body, author:'joke.author' } #Add funney, rating, ............
    jk = serializers.serialize('json', [ jokes, ])'''
    
    '''    else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occured
    return JsonResponse({"error": ""}, status=400)'''

def vote(request):
    message=''
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        joke_id = request.GET.get("joke_id", None);
        vote = request.GET.get("vote", None)
        category = request.GET.get("category", None)
        #if bool(vote):
        print('category:{} {}'.format(category, str(category) == 'Adult'))
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
            #if user_have_not_voted_joke:
            if bool(vote):
                #For upvotes
                joke.loves+=1;
                message = str(joke_id) + 'voted successfully.'
                print('\n\nFucking voting freely'+str(type(int(joke_id))) + str(int(joke_id)+1))
            else:
                #for downvotes
                joke.loves -= 1;
                message = str(joke_id) + 'unvoted successfully.'
                print('\n\n unVoting:' + str(joke_id))
            joke.save()
            
    print('Loves : ' + str(db.objects.get(id=int(joke_id)).loves))
    #print(str(vote) +' of type'+ str(type(vote)))
    return JsonResponse({'message':message }, status = 200)

def getComments(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        joke_id = request.GET.get("joke_id", None);
        category = request.GET.get("category", None)
        which_jokes = request.GET.get("which_jokes", None)
        
        print('For Comments: joke_id:{}  category:{}  which_joke:{}'.format(joke_id, category, which_jokes))
        
        if (str(which_jokes)=='jokes'):
            #db = Jokes
            #db_name = 'jokes'
            comments = Jokes.objects.using('jokes').get(id=joke_id).jokecomments_set.all()
            print('\nDB: Jokes  id: {}'.format(id))
            
        else:
            if str(category) == 'Adult':
                db = AbsurdlyBigJokes
                db_name = 'default'
                print('\nDB: AbsurdlyBigJokes')
            else:
                db = WockaJokes
                db_name = 'default'
                print('\nDB: WockaJokes')
            
            comments = db.objects.using(db_name).get(id=int(joke_id)).comments_set.all()
    #print('\n\njoke_id:' + str(int(joke_id)))
    
    print('\n\nComments:\t {}\n'.format(comments))
    comments = serializers.serialize('json', comments, )
    
    return JsonResponse({'comments':comments},status=200)


@login_required
def saveComment(request):
    
    if request.is_ajax and request.method == "POST":
        # get the nick name from the client side.
        comment = request.POST.get("comment", None);
        joke_id = request.POST.get("joke_id", None);
        
        category = request.POST.get("category", None)
        
    if (request.user.is_authenticated):
        #return HttpResponse('Ill make ai')
        username = request.user.username
    #print('\n\ncomment:{}  id:{} username:{}'.format(comment, joke_id, username))
    if not str(comment).strip()=='':
        #pass
        if str(category) == 'Adult':
            Comments.objects.create(body=str(comment), user_id=str(username),AbsurdlyBigJokes=int(joke_id))
            #db = AbsurdlyBigJokes
            print('\n\n\n' + str(True))
        else:
            Comments.objects.create(body=str(comment), user_id=str(username),wockajokes_id=int(joke_id))
    return HttpResponse('Successfully commented')

def saveNewJokesComment(request):
    if request.is_ajax and request.method == "POST":
        # get the nick name from the client side.
        username = request.POST.get("username", None);
        comment = request.POST.get("comment", None);
        joke_id = request.POST.get("joke_id", None);
        email = request.POST.get("email", None);
        
    if not str(comment).strip()=='':
        JokeComments.objects.using('jokes').create(body=str(comment), jokes_id = int(joke_id), email = email, username = username)
        return HttpResponse('Successfully commented')
    
    else:
        return HttpResponse('Comment is empty')


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
        return render(request, 'jokes/feedback.html', {'feedbacks':feedbacks})

def each_joke(request, joke_id = 1):
    print('\n\n\n'+str(joke_id) + '\n\n\n')
    #jokes = WockaJokes.objects.all()[0]
    if request.method == 'GET':
        joke_id = request.GET.get('joke_id', joke_id)
    
    if joke_id != None:
        jokes = Jokes.objects.using('jokes').filter( id = int(joke_id) )[0]
        
        random_joke = False
    else:
        print('\nfirst_template: getting random joke \n')
        jokes = Jokes.objects.using('jokes').all().order_by('-loves')[0]
        random_joke=True
    
    # print(jokes)
    print('\n\n\n'+str(jokes))
    
    categories = list(Jokes.objects.using('jokes').values('category').distinct())
    #categories = [category['category'] for category in  Jokes.objects.using('jokes').values('category').distinct()]
    template_1 = 'jokes/template.html'
    print('Returning By render joke_id = '+str(joke_id) + '\t' + str(jokes))
    return render(request, template_1, { 'jokes' : [jokes], 'random_joke' : random_joke, 'categories':categories })

'''        favourite_ids=[]
        #print('\n\n\n\n\n\nHello\n\n\n\n\n')
        with open('jokes/wockaFavList.json', 'r') as f:
            favourite_ids=json.load(f)
        
        latest_joke_list = WockaJokes.objects.filter(id__in=favourite_ids[0:15])'''

def get_category(request, category=None):
    
    #To get category if requested via AJAX
    if request.is_ajax and request.method == "GET":
        
        category = request.GET.get("category", category)
    
    print('\n\ncategory:{}\n'.format(category))
    
    if (category=='general' or category==None):
        #order_by('-loves') once enough loves are given
        
        #jokes = list(Jokes.objects.using('jokes').all().order_by('-rating')[:100])
        #jokes = Jokes.objects.using('jokes').all().order_by('-rating')[:100]
        favourite_ids=[]
        with open('jokes/wockaFavList.json', 'r') as f:
            favourite_ids=json.load(f)
        
        jokes = Jokes.objects.using('jokes').filter(source_id__in=favourite_ids[:300], source='http://www.wocka.com/').order_by('-rating')
        category = 'general'
    
    else:
        #order_by('-loves') once enough loves are given
        jokes = list(Jokes.objects.using('jokes').filter(category=category).order_by('-rating'))
        jokes = Jokes.objects.using('jokes').filter(category=category).order_by('-rating')
    
    #comments = db.objects.get(id=int(joke_id)).comments_set.all()
    if category!=None:
    #return HttpResponse('\n Received via Json. \n')
        jokes = serializers.serialize('json', jokes, )
        #print(serializers.serialize('json', [jokes[0]], ))
        return JsonResponse({'jokes':jokes, 'category':category}, status=200)
    
    else:
        #return HttpResponse('\n Received via URL. \n')
        
        template = 'jokes/temaplate.html'
        return render(request, template, {'jokes':jokes, 'category':category})


@api_view(["GET"])
def random_joke_api(request):
    try:
        joke = Jokes.objects.using('jokes').all().order_by('-rating')[random.randint(0,10000)]
        title = joke.title
        if title.strip()=='':
            title = joke.category
        return JsonResponse({'title':title, 'body':joke.body, 'author':joke.author}, status=200)
    except ValueError as e:
        return Response(e.argss[0], status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def list_jokes_api(request, no_of_jokes):
    if int(no_of_jokes) < 10:
        no_of_jokes = int(no_of_jokes)
    else:
        no_of_jokes = 10
    
    try:
        jokes = Jokes.objects.using('jokes').all().order_by('-rating')[:no_of_jokes]
        j2=[]
        for joke in jokes:
            title = joke.title
            if title.strip()=='':
                title = joke.category
            j2.append({'title':joke.title, 'body':joke.body, 'author':joke.author})
        #jokes = serializers.serialize('json', j2, )
        return JsonResponse({'jokes':j2}, status=200)
    except ValueError as e:
        return Response(e.argss[0], status.HTTP_400_BAD_REQUEST)

def api_view(request):
    return render(request, 'jokes/api_template.html')
