from django.contrib import admin
from django.urls import path, include

from .views import (
welcome,
Approve,
Unapprove,
AnnouncementListView,
AnnouncementCreateView,
AnnouncementDeleteView,
AnnouncementUpdateView,
AnnouncementDetailView,
WorkspaceCreateView,
UserWorkspaceListView,
WorkspaceDetailView,
WorkspaceUpdateView,
WorkspaceDeleteView,
AddContributor,
About)

urlpatterns = [
	path('', welcome, name='welcome'),
	path('approve/<int:pk>/<int:a_pk>/', Approve, name='approve'),
	path('unapprove/<int:pk>/<int:a_pk>/', Unapprove, name='unapprove'),
	path('annoucement/<int:pk>/', AnnouncementListView.as_view(), name='announcements'),
	path('message/<int:pk>/new/', AnnouncementCreateView.as_view(), name='message'),
	path('message/<int:pk>/',AnnouncementDetailView.as_view(), name='message-details'),
	path('message/<int:pk>/update', AnnouncementUpdateView.as_view(), name='message-update'),
	path('message/<int:pk>/delete', AnnouncementDeleteView.as_view(), name='message-delete'),
	path('workspace/new/', WorkspaceCreateView.as_view(), name='create-workspace'),
	path('workspace/<int:pk>/update', WorkspaceUpdateView.as_view(), name='workspace-update'),
	path('workspace/<int:pk>/delete', WorkspaceDeleteView.as_view(), name='workspace-delete'),
	path('user/<str:username>/', UserWorkspaceListView.as_view(), name='user-workspace'),
	path('workspace/<int:pk>/', WorkspaceDetailView.as_view(), name='workspace-details'),
	path('workspace/<int:pk>/contributor/', AddContributor.as_view(), name='add-contributor'),
	path('about/', About, name='about'), 

]
