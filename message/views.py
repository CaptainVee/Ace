from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect

from .models import Announcement, Workspace
from .forms import AnnouncementUpdateForm, ContributorForm
from user.models import Profile
# Create your views here.

def welcome(request):
	'''this function is to redirect from login page to workspace list passing the username 
	of the logged in user as a parameter'''
	username = request.user.username
	if username == '':
		return render(request, 'message/home.html', {'title': 'Home'})
	else:
		return redirect('user-workspace', username)


class WorkspaceCreateView(LoginRequiredMixin, CreateView):
	model = Workspace
	fields = ['title', 'description', 'image']
	
	def form_valid(self, form):
		print(self.kwargs)
		form.instance.head = self.request.user
		return super().form_valid(form)



class UserWorkspaceListView(ListView):
	model = Workspace
	template_name = 'message/welcome.html'
	context_object_name = 'workspaces'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Workspace.objects.filter(head=user).order_by('-updated_at')

class WorkspaceDetailView(DetailView):
	model = Workspace

class WorkspaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Workspace
	fields = ['title', 'description', 'image']

	def form_valid(self, form):
		form.instance.head = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		user = self.request.user
		if user == post.head:
			return True
		return False

class WorkspaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Workspace
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		user = self.request.user
		if user == post.head:
			return True
		return False


class AnnouncementListView(View):
	def get(self, request, pk, *args, **kwargs):
		form = AnnouncementUpdateForm()

		announcement = Announcement.objects.filter(workspace=pk)
		workspace = get_object_or_404(Workspace, pk=pk)
		context = {
		'pk':pk,
		'form':form,
		'objects':announcement,
		'workspace':workspace
		}
		for a in announcement:
			print(a.author.user)
		return render(self.request, "message/announcement_list.html", context)
	
	def post(self, request, pk, *args, **kwargs):
		announcement_qs = Announcement.objects.filter(workspace=pk)
		for announcement in announcement_qs:
			form = AnnouncementUpdateForm(self.request.POST)
			if form.is_valid():
				approved = form.cleaned_data.get('approved')
				announcement.approved = approved
				announcement.save()
				print(announcement.approved)
		messages.success(request, f'The Announcement has been updated!')
		return redirect('workspace-details', pk)


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
	model = Announcement
	fields = ['title', 'content', 'image']
	
	def form_valid(self, form,):
		form.instance.author = get_object_or_404(Profile, user=self.request.user)
		form.instance.workspace = get_object_or_404(Workspace, pk=self.kwargs.get('pk'))
		return super().form_valid(form)

class AnnouncementDetailView(DetailView):
	def get(self, request, pk, a_pk, *args, **kwargs):
		announcement = Announcement.objects.filter(workspace=pk, pk=a_pk)[0]
		context = {'object': announcement}
		return render(request, "message/announcement_detail.html", context)


class AnnouncementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Announcement
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = get_object_or_404(Profile, user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		user = get_object_or_404(Profile, user=self.request.user)
		if user == post.author:
			return True
		return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Announcement
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		user = get_object_or_404(Profile, user=self.request.user)
		if user == post.author:
			return True
		return False

def Approve(request, pk, a_pk):
	announcement = get_object_or_404(Announcement, pk=a_pk)
	announcement.approved = True
	announcement.save()
	messages.info(request, "You have approved this announcement")
	return redirect("announcements", pk)


def Unapprove(request, pk, a_pk):
	announcement = get_object_or_404(Announcement, pk=a_pk)
	announcement.approved = False
	announcement.save()
	messages.info(request, "You have unapproved this announcement")
	return redirect("announcements", pk)


class AddContributor(View):
	def get(self, request, pk, *args, **kwargs):
		form = ContributorForm()
		context = {
		'form':form,
		}
		return render(self.request, "message/contributor_form.html", context)

	def post(self, request, pk, *args, **kwargs):
		workspace =  get_object_or_404(Workspace, pk=self.kwargs.get('pk'))
		form = ContributorForm(self.request.POST or None)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			contributor = get_object_or_404(Profile, email= email)
			workspace.contributors.add(contributor)
			workspace.save()
			return redirect("workspace-details", pk)


class About(ListView):
	model = Workspace
	template_name = 'message/about.html'
	context_object_name = 'workspaces'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Workspace.objects.filter(head=user).order_by('-updated_at')