# To Do:
##  adjust wockajokes funney range (0 to 5.0)

from django.db import models
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from user.models import User
import random
import string

#python3 manage.py migrate --database=jokes
#python3 manage.py migrate --fake
class Jokes(models.Model):
    #temporary_id = ...
    id = models.AutoField(primary_key=True)
    #id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))    # ascii_letters -> ascii_lowercase + ascii_uppercase
    
    #id = models.CharField(unique=True, primary_key=True, default=StringKeyGenerator(), editable=False)
    '''class StringKeyGenerator(object):
    def __init__(self, len=16):
        self.lenght = len
    def __call__(self):
        return ''.join(random.choice(string.letters + string.digits) for x in range(self.lenght))'''
    
    # Id assigned to joke in it's source website
    source = models.CharField(max_length = 100, default=None, null=True)
    source_id = models.IntegerField(default = None, null=True)
    
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=65000)
    author = models.CharField(max_length=100, default = None, null=True)
    loves = models.IntegerField(default=0)
    
    # To determine funneyness/average_rating of a joke [funney in wocka jokes website]
    rating = models.FloatField(default = None)
    
    rating_letters_points = models.FloatField(default=0)
    # (rating in wocka jokes website)
    #To determing the adult, child, .....  of a joke
    
    rating_letters = models.CharField(max_length = 5)
    
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    
    #extract tags
    tags = ArrayField(models.CharField(max_length=150, blank=True), default=None, null=True)
    category = models.CharField(max_length=100,default=None, null=True)
    joke_type = ArrayField(models.CharField(max_length=150, blank=True), default=None, null=True)
    #'qa -> questsion_answer, n-> joke (normal_joke), q->quoet, one_liner'
    
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # 'http://www.wocka.com/'                         ids:  00000 - 10018     max.rating: 5.54
    # 'Absurdly Big Adult Joke Book.epub'             ids:  10019 - 11706     max.rating: 0.0
    # 'stupidstuff'                                   ids:  11707 - 15479     max.rating: 5.0       joke:3773   (vaccent from deleted_ids position)
    # 'The Best Joke Book'                            ids:  15480 - 16064     max.rating: 5.0       joke:585
    # 'The Best Joke Book Hundreds of the Funniest, Silliest, Most Ridiculous Jokes Ever'
    
    #           Total: 15484
'''#<<<<<<< HEAD
    def deleted_ids(self):
        return([214, 14936, 15003, 15025, 15026, 15027, 15028, 791, 15029, 15030, 15031, 15178, 15235, 1289, 15236, 14679, 14680, 14681, 14682, 14683, 14684, 14685, 1677, 14686, 14687, 14688, 14689, 14690, 14691, 14692, 14693, 14694, 2057, 14695, 14696, 14697, 2358, 14698, 14699, 2458, 2468, 14700, 14701, 14702, 14703, 14704, 14705, 14706, 14707, 14708, 14709, 14710, 14711, 14712, 14713, 15237, 15238, 15239, 15240, 15241, 15242, 15244, 15245, 15246, 15247, 15248, 15249, 15250, 15251, 15252, 15253, 15254, 15299, 15300, 15356, 15416, 15417, 15418, 15445, 15446, 13435, 13644, 14940, 14715, 14716, 14941, 14942, 14674, 14675, 14677, 14656, 14659, 14660, 14662, 14664, 14667, 14668, 14669, 14670, 14720, 14721, 14722, 14724, 14726, 14727, 14728, 14729, 14731, 14732, 14733, 14735, 14736, 14738, 14739, 14765, 14943, 14743, 14744, 14745, 14746, 14747, 14750, 14751, 14753, 14754, 14755, 14756, 14757, 14758, 14759, 14761, 14762, 14763, 14805, 14998, 14999, 15000, 15001, 14767, 14769, 14770, 14773, 14774, 14775, 14776, 14777, 14780, 14781, 14782, 14783, 14784, 14785, 14786, 14787, 14788, 14790, 14791, 14792, 14794, 14795, 14796, 14797, 14798, 14800, 14801, 14802, 14803, 14807, 14809, 14811, 14818, 14819, 14820, 14821, 14822, 14823, 14874, 14875, 14876, 14877, 14826, 14828, 14829, 14830, 14831, 14832, 14833, 14834, 14836, 14837, 14838, 14840, 14841, 14842, 14879, 14880, 14881, 14882, 14883, 14884, 14885, 15002, 14844, 14847, 14848, 14849, 14850, 14851, 14852, 14853, 14855, 14856, 14857, 14859, 14860, 14861, 14863, 14864, 14865, 14867, 14869, 14870, 14872, 14919, 14887, 14888, 14889, 14890, 14891, 14893, 14894, 14895, 14896, 14898, 14900, 14901, 14902, 14903, 14904, 14905, 14906, 14908, 14909, 14912, 14913, 14914, 14915, 14917, 14918, 14921, 14924, 14925, 14927, 14928, 14930, 14931, 14933, 14934, 14945, 14946, 14947, 14949, 14950, 14951, 14952, 14953, 14954, 14955, 14956, 14958, 14959, 14961, 14962, 14963, 14964, 14965, 14966, 14967, 14968, 14969, 14970, 14975, 14976, 14977, 14978, 14980, 14982, 14983, 14984, 14986, 14987, 14989, 14990, 14991, 14992, 14993, 14994, 14995, 14996, 14997, 15005, 15007, 15011, 15012, 15013, 15015, 15016, 15021, 15022, 15023, 15035, 15036, 15040, 15042, 15047, 15048, 15051, 15052, 15053, 15054, 15055, 15056, 15057, 15061, 15063, 15064, 15066, 15068, 15070, 15071, 15073, 15075, 15077, 15079, 15082, 15083, 15084, 15085, 15144, 15146, 15088, 15090, 15091, 15092, 15093, 15094, 15095, 15096, 15097, 15098, 15099, 15100, 15101, 15103, 15104, 15105, 15106, 15107, 15111, 15112, 15114, 15115, 15116, 15117, 15118, 15121, 15122, 15123, 15124, 15125, 15127, 15128, 15129, 15130, 15131, 15132, 15134, 15135, 15137, 15139, 15140, 15141, 15142, 15143, 15148, 15149, 15150, 15151, 15153, 15154, 15157, 15158, 15159, 15160, 15161, 15162, 15163, 15165, 15166, 15167, 15168, 15169, 15170, 15171, 15172, 15173, 15174, 15176, 15177, 15181, 15182, 15184, 15186, 15188, 15189, 15190, 15191, 15193, 15194, 15195, 15196, 15197, 15198, 15199, 15200, 15201, 15203, 15205, 15206, 15207, 15208, 15209, 15210, 15211, 15212, 15213, 15214, 15216, 15217, 15218, 15220, 15221, 15222, 15225, 15226, 15227, 15228, 15230, 15231, 15232, 15233, 15234, 15256, 15258, 15259, 15261, 15262, 15263, 15264, 15265, 15266, 15267, 15269, 15270, 15271, 15272, 15273, 15274, 15275, 15276, 15277, 15278, 15282, 15286, 15288, 15289, 15292, 15293, 15294, 15295, 15296, 15303, 15304, 15307, 15308, 15310, 15311, 15312, 15313, 15316, 15317, 15321, 15322, 15323, 15324, 15326, 15328, 15330, 15331, 15341, 15342, 15345, 15346, 15347, 15348, 15349, 15351, 15352, 15353, 15354, 15355, 15359, 15360, 15362, 15364, 15365, 15367, 15368, 15369, 15370, 15371, 15372, 15373, 15374, 15375, 15376, 15377, 15379, 15380, 15381, 15382, 15384, 15386, 15387, 15389, 15390, 15393, 15395, 15398, 15399, 15400, 15404, 15405, 15406, 15408, 15409, 15410, 15413, 15422, 15424, 15426, 15427, 15428, 15429, 15430, 15431, 15433, 15434, 15435, 15437, 15441, 15442, 15444, 15448, 15449, 15451, 15455, 15458, 15459, 15460, 15463, 15464, 15465, 15466, 15467, 15468, 15470, 15473, 15474, 15475, 15477])
        
=======

>>>>>>> 300a3cceb61c35f7beffcf7327c6477d0fadfe7d
'''

# Create your models here.
#@login_required
class WockaJokes(models.Model):
    id = models. AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=65000)
    author = models.CharField(max_length=100)
    loves = models.IntegerField(default=0)
    funney = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    rating_letters = models.CharField(max_length = 5)
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    category = models.CharField(max_length=100)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class StupidStuffJokes(models.Model):
    id = models. AutoField(primary_key=True)
    body = models.CharField(max_length=65000, default='')
    category = models.CharField(max_length=100, default='')
    rating = models.FloatField(default=0)
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    loves = models.IntegerField(default=0)
    rating_letters = models.CharField(max_length = 5, default='' )
        #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class RedditJokes(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    body = models.CharField(max_length=50000, default='')
    #category = models.CharField(max_length=100, default='')
    score = models.FloatField(default=0)
    title = models.CharField(max_length=350, default='')
    #author = models.CharField(max_length=100, default='')
    loves = models.IntegerField(default=0)
    #rating_letters = models.CharField(max_length = 5, default='' )
        #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return (str(self.title) + '  \n' +  str(self.body))
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class UploadJokes(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    category = models.CharField(max_length=100, default=None, null=True)
    votes = models.IntegerField(default=0)
    #rating = models.FloatField(default=0)
    tag = models.CharField(max_length=100, default=None, null=True)
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return(self.title + ':\n\t' + self.body)
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class SearchModel(models.Model):
    search_term = models.CharField(max_length=100)

'''class RedditJokes(models.Model):

    joke_title = models.CharField(max_length=100)
    def __str__(self):
        return self.joke_title'''


class Comments(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    
    # UploadJokes as foreign Key for real Implications
    wockajokes = models.ForeignKey(WockaJokes, on_delete=models.CASCADE)
    
    body = models.CharField(max_length=150, default = None)
    loves = models.IntegerField(default=0)
    
    def __str__(self):
        return self.body
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def appendReadIds():
        print('I want')

    def incrementCommentVote(id):
        print('I want')

    def incrementCommentVote(id):
        print('I want')

    

class ShortedList(models.Model):
    category = models.CharField(max_length=100, primary_key = True)
    shortedids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
#ArrayField(models.CharField(max_length=250, blank=True), default=None, null=True)

class AbsurdlyBigJokes(models.Model):
    id = models. AutoField(primary_key=True)
    category = models.CharField(max_length=100, default = '')
    title = models.CharField(max_length=100, default = '')
    body = models.CharField(max_length = 2500)
    author = models.CharField(max_length=100, default = '')
    loves = models.IntegerField(default=0)
    funney = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    rating_letters = models.CharField(max_length = 5)
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#python3 manage.py migrate --database=feedbacks
class Feedbacks(models.Model):
    username = models.CharField(max_length=50, default = None, null=True)
    body = models.CharField(max_length=500, default = None)
    loves = models.IntegerField(default=0)    
    email = models.EmailField(default = None,)
    
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):
        return('Username: {}, Body:{}, email:{}'.format(self.username, self.body, self.email))
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# Python3 manage.py migrate --database='feedbacks'
class JokeComments(models.Model):
    #user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    
    #UploadJokes as foreign Key for real Implications
    username = models.CharField(max_length=50, default = '')
    jokes = models.ForeignKey(Jokes, on_delete=models.CASCADE)
    
    body = models.CharField(max_length=150, default = None)
    loves = models.IntegerField(default=0)
    email  = models.EmailField(blank=True)
    
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return self.body
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



