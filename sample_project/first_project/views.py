from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def home(request):
    
    now = datetime.datetime.now()
    other_date = datetime.datetime(2011, 9, 1)
    dir = {'val' : 6 , 'str' :  "I'm Jai" , 'name' : 'rakib' , 'spaceString' : 'Rakibul Hasan',

            'date' : datetime.datetime.now(), 'empty' : "",
            'lst': [
                    {'name': 'bed', 'age': 19},
                    {'name': 'kmy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                    ],

            'number' : 21, 'es' : "<p>You are <em>pretty</em> smart!</p>",
            'fileValue' : "123456789", 'arr' : ['a','b','c'], 'txtNum' : 'One',
            'courseName' :'Phitron is best', 'tit' : 'Django rest framework',
            'Date' : now, 'other_date' : other_date,
            'unorder' : ['states',['kansas',['lawrence','topeka'],'illinois']],
            'description' : 'My name is Rakibul Hasan. I am a student.',
            'string' : '<b>I</b> <button>love</button> <span>dogs</span> ',
            'str': 'You can build web apps with python and Django',
            'num_messages' : 4, 
            'longdescription' : "I remember as a child, and as a young budding naturalist, spending \
        all my time observing and testing the world around me—moving pieces, \
        altering the flow of things, and documenting ways the world responded \
        to me. Now, as an adult and a professional naturalist, I've approached \
        language in the same way, not from an academic point of view but as a \
        curious child still building little mud dams in creeks and chasing after \
        frogs. So this book is an odd thing: it is a naturalist's walk through the \
        language-making landscape of the English language, and following in \
        the naturalist's tradition it combines observation, experimentation, \
        speculation, and documentation—activities we don't normally \
        associate with language.",

           }
    return render(request,'home.html',context=dir)
