from django.shortcuts import render
from django.http import HttpResponse
from .apis import member as MemberAPI
from django.shortcuts import redirect, get_object_or_404
from django.core import serializers
from c_shop.models import Member, Board, Company, Project, ProjectImages
from django.core.paginator import Paginator
import random
from datetime import datetime, timedelta

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




def communityList(request):
    
    onWrite = True
    boardtype = -1
    
    if 'type' in request.GET:
        boardtype = int(request.GET['type'] or 0)
        
    if boardtype != -1:
        boards = Board.objects.filter(category=boardtype)
        if boardtype > 4:
            onWrite = False
    else:      
        boards = Board.objects.all()    
    boardcnt = boards.count()
    data = list(boards.order_by('-id'))  
        
        
    if 'page' in request.GET:
        page_num = int(request.GET['page'] or 1)
    else:
        page_num = 1 
    proj_per_page = 10
    paginator = Paginator(data, proj_per_page) # page별 분리
    page = paginator.page(page_num) # 해당 페이지 가져오기  
    
    result = {
        'data': page, 
        'pagenum': {
            'total': boardcnt,
            'start_index': (proj_per_page * (page_num-1)),
        },
        'onWrite': onWrite,
        'type': boardtype,
        'currentPage': page_num, 
        'totalPages': paginator.page_range
    }
    return render(request, "community/list.html", result)




def communityView(request, id):
    
    boardnum = request.GET['bn']
    board_obj = get_object_or_404(Board, pk=id)
    
    cookie_name = f'board_' + str(id)
    if cookie_name not in request.COOKIES:
        board_obj.views += 1
        board_obj.save()
        expires = datetime.utcnow() + timedelta(days=1)
        expires = expires.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
        response = HttpResponse(render(request, "community/view.html", { 'data' : board_obj, 'boardnum' : boardnum }))
        response.set_cookie(cookie_name, 'true', expires=expires)
        return response
    
    return render(request, "community/view.html", { 'data' : board_obj, 'boardnum' : boardnum, "writer": board_obj.user._id })


def communityWrite(request):   
    boardtype = 0
    if 'type' in request.GET:
        boardtype = int(request.GET['type'] or 0)
    return render(request, "community/write.html", {'type': boardtype})

def communityEdit(request):
    return render(request, "community/edit.html")


    