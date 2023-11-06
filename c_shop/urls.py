from django.urls import path

from . import views
from .apis import member, project, board

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("mypage", views.myPage, name="myPage"),
    path("shop", views.shop, name="shop"),
    
    path("project", views.project, name="project"),
    path("project/write", views.projectWrite, name="projectWrite"),
    path("project/detail/<int:id>", views.projectDetail, name="projectDetail"),
    path("project/edit/<int:id>", views.projectEdit, name="projectEdit"),
    
    path("project/create", project.create, name="projectCreate"),
    path("project/update", project.update, name="projectUpdate"),
    path("project/delete/<int:id>", project.delete, name="projectDelete"),
    
    
    path("community/edit", views.communityEdit, name="communityEdit"),
    path("community/list", views.communityList, name="communityList"),
    path("community/view/<int:id>", views.communityView, name="communityView"),
    path("community/write", views.communityWrite, name="communityWrite"),
    
    path("board/create", board.create, name="boardCreate"),
    path("board/delete/<int:id>", board.delete, name="boardDelete"),
    
    
    
    
    path("member/create", member.create, name="memberCreate"),
    path("member/login", member.login, name="memberLogin"),
    path("member/logout", member.logout, name="memberLogout"),
    path("member/update", member.update, name="memberUpdate"),
    
    
]