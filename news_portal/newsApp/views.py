from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
# --------------Authentication-------------------->
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('home')

# ---------------CRUD--------------------------->
def home(request):
    return render(request, 'home.html')
def addNews(request):
    return render(request, 'addNews.html')
def editNews(request):
    return render(request, 'editNews.html')
def viewNews(request):
    return render(request, 'viewNews.html')
def deleteNews(request):
    return render(request, 'deleteNews.html')