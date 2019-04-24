from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import subprocess

from .models import Greeting


p = subprocess.Popen(["python3", 'index.py'],
                     stdout = subprocess.PIPE,
                     stdin = subprocess.PIPE)

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def next(process):
    out = {}
    out['info'] = []
    print(process.poll())
    line = process.stdout.readline().decode("utf-8")[:-1]
    while line[0] != '#':
        out['info'].append(line[1:])
        line = process.stdout.readline().decode("utf-8")[:-1]
    out['msg'] = line[1:]

    print("returning")
    print(out)
    return out

def no(request):
    global p
    p.stdin.write('n\n'.encode())
    p.stdin.flush()
    return JsonResponse(next(p))

def yes(request):
    global p
    p.stdin.write('y\n'.encode())
    p.stdin.flush()
    return JsonResponse(next(p))

def login(request):
    username = request.POST['name']
    pw = request.POST['password']
    global p
    out = 'l#'+str(username)+","+str(pw)+"\n"
    p.stdin.write(out.encode())
    p.stdin.flush()
    return JsonResponse(next(p))

def message(request):
    msg = request.POST['msg']
    global p
    out = "m"+msg+"\n"
    p.stdin.write(out.encode())
    p.stdin.flush()
    return JsonResponse(next(p))

def start(request):
    global p
    p.stdin.write('s\n'.encode())
    p.stdin.flush()
    return JsonResponse(next(p))
