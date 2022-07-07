from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def bucket_log(request):
    return render(request, 'bucket_log.html')

def mypage(request):
    return render(request, 'mypage.html')

def change_info(request):
    return render(request, 'change_info.html')

def mywriting(request):
    return render(request, 'mywriting.html')

def show_following1(request):
        return render(request, 'show_following1.html')
def scrap(request):
    return render(request, 'scrap.html')
