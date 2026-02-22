from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>ICT12367 SPU")
def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา")
def form(request):
    return render(request, 'form.html')
def contact(request):
    return HttpResponse("<h1>รหัสนักศึกษา: 68052064 ชื่อ: นายณัฐวุฒิ ศัยกุล")