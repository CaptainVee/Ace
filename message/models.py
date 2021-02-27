from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from user.models import Profile
from django.urls import reverse

# Create your models here.


class Workspace(models.Model):
	title = models.CharField(max_length=150 )
	description = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	head = models.ForeignKey(User, on_delete= models.CASCADE)
	image = models.ImageField(default='default.jpg', null=True, blank=True)
	contributors = models.ManyToManyField(Profile, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('workspace-details', kwargs={'pk' : self.pk})

	def is_contributor(self):
		return self.contributors.all()


	@property
	def announcements(self):
		return self.announcement_set.all().order_by('-updated_at')


class Announcement(models.Model):
	"""model for Announcement"""
	# slug = models.SlugField(unique=True, null=False)
	title = models.CharField(max_length=150 )
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(Profile, on_delete= models.CASCADE)
	announced = models.BooleanField(default=False)
	approved = models.BooleanField(default=False)
	image = models.ImageField(default='defaulst.png', null=True, blank=True)
	workspace = models.ForeignKey(Workspace, on_delete= models.CASCADE)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('announcements', kwargs={'pk': self.workspace.pk })








