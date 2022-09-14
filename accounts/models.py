from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid_no = models.CharField(max_length=100,blank=True, null=True,verbose_name="UID No.")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    linked_upa = models.ManyToManyField(User,related_name="linked_upa",blank=True)

    left_branch = models.BooleanField(default=False)
    left_upa = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name="left_branch")
    middle_branch = models.BooleanField(default=False)
    middle_upa = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name="middle_branch")
    right_branch = models.BooleanField(default=False)
    right_upa = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name="right_branch")
    initial_form_status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # instance.profile.save()

'''
def random_string_generator(size=10,chars = string.ascii.lowecase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
'''