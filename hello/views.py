from django.shortcuts import render
from django.http import HttpResponse
import subprocess

from .models import Greeting


p = subprocess.Popen(["python", 'index.py'],
                     stdout = subprocess.PIPE,
                     stdin = subprocess.PIPE)

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def next(process):
    out = {}
    out['info'] = []
    line = process.stdout.readline()[-1]
    while line[0] != '#':
        out['info'].append(line[1:])
    out['msg'] = line[1:]
    return out

def no(request):
    global p
    p.stdin.write('n')
    return next(p)

def yes(request):
    global p
    p.stdin.write('y')
    return next(p)

def login(request):
    username = request.POST['name']
    pw = request.POST['password']
    global p
    p.stdin.write('l#'+username+","+pw)
    return "Wait a sec"

def message(request):
    msg = request.POST['msg']
    global p
    p.stdin.write('m'+msg)
    return "Ok"

def start(request):
    global p
    p.stdin.write('s')
    return next(p)