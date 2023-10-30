from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI
from django.shortcuts import redirect, get_object_or_404
from django.core import serializers
from c_shop.models import Member, Board, Company, Project, ProjectImages
from django.core.paginator import Paginator
import random

def index(request):
    # if(request.session.get('id')):
    #     request.session['id'] = None
    
    return render(request, "index.html")

def login(request):
    if(request.session.get('id')):
        return redirect('/')
    return render(request, "login.html")

def myPage(request):
    if(not request.session.get('id')):
        return redirect('/login/')
    user = get_object_or_404(Member, pk=request.session.get('id'))
    myBoard = Board.objects.filter(user=user).count()
    myProject = Project.objects.filter(user=user).count()
    # return render(request, "mypage.html", {"data":user,"myBoard":myBoard,"myProject":myProject ,"plantExp":user.plantExp%700})
    return render(request, "mypage.html", {"data":user,"myBoard":myBoard,"myProject":myProject ,"plantExp":user.plantExp})

def shop(request):
    data = list(Company.objects.all())
    # data = random.shuffle(data*5)
    return render(request, "shop.html",{"data":data*4})



def project(request):       
    
    if 'page' in request.GET:
        page_num = int(request.GET['page'] or 1)
    else:
        page_num = 1        
    proj_per_page = 12
    data = list(Project.objects.all().order_by('-id'))
    paginator = Paginator(data, proj_per_page) # page별 분리
    page = paginator.page(page_num) # 해당 페이지 가져오기    
    
    result = []
    for obj in page:
        img = "default/no_image.png"
        if ProjectImages.objects.filter(project=obj).exists():
            img = get_object_or_404(ProjectImages, project=obj).photo
        datain = {
            "id": obj.id, 
            "user": obj.user, 
            "title": obj.title, 
            "summary": obj.summary, 
            "team": obj.team,
            "teammate": obj.teammate,
            "category": obj.category,
            "created_at": obj.created_at,
            "image": str(img)
        }
        result.append(datain)   
    return render(request, "project/list.html", {"data": result,'currentPage': page_num, 'totalPages': paginator.page_range})

def projectDetail(request, id):   
    data = get_object_or_404(Project, pk=id)
    img = "default/no_image.png"
    if ProjectImages.objects.filter(project=id).exists():
        img = get_object_or_404(ProjectImages, project=id).photo           
    return render(request, "project/detail.html", {"data": data, "writer": data.user._id, "image": str(img)})

def projectWrite(request):
    if(not request.session.get('id')):
        return redirect('/login/')
    user = get_object_or_404(Member, pk=request.session.get('id')) 
    return render(request, "project/write.html")

def projectEdit(request, id):
    if(not request.session.get('id')):
        return redirect('/login/')
    user = get_object_or_404(Member, pk=request.session.get('id'))    
    data = get_object_or_404(Project, pk=id, user=user)
    img = "default/no_image.png"
    return render(request, "project/edit.html", {"data": data, "writer": data.user._id, "image": str(img)})



def communityEdit(request):
    return render(request, "community/edit.html")
def communityList(request):
    return render(request, "community/list.html")
def communityView(request, id):
    return render(request, "community/view.html")
def communityWrite(request):
    return render(request, "community/write.html")



    