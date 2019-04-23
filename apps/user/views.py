from django.shortcuts import render


# Create your views here.
def index(request):
    pass
    return render(request, 'topic/topics.html')


def login(request):
    pass
    return render(request, 'user/login.html')


def register(request):
    pass
    return render(request, 'user/register.html')


def nodes(request):
    pass
    return render(request, 'topic/nodes.html')

def members(request):
    pass
    return render(request, 'topic/members.html')

def colleges(request):
    pass
    return render(request, 'topic/colleges.html')

def members(request):
    pass
    return render(request, 'topic/members.html')

def create(request):
    pass
    return render(request, 'topic/create.html')

def view(request):
    pass
    return render(request, 'topic/view.html')

def colleges_topics(request):
    pass
    return render(request, 'topic/college_topics.html')

def profile(request):
    pass
    return render(request, 'topic/profile.html')
def node_topics(request):
    pass
    return render(request, 'topic/node_topics.html')