from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (AbstractBaseUser, )
from .manager import UserManager


class AbstractCustomUser(AbstractBaseUser):
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
    username = models.CharField(max_length=50, db_index=True,
                                validators=[alphanumeric])
    email = models.EmailField(_('email address'), max_length=255,
                              unique=True, db_index=True)
    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designates whether this users should be treated as '
        'active. Unselect this instead of deleting profiles.'))
    date_joined = models.DateTimeField(_('date joined'), auto_now=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('users')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.username

    def get_short_name(self):
        """ Return the email."""
        return self.username

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class User(AbstractCustomUser):
    class Meta(AbstractCustomUser.Meta):
        swappable = 'AUTH_USER_MODEL'

@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nro_documento = models.CharField(max_length=12, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profiles/uploads", blank=True, null=True,
        default="/static/images/default_user_default.png")

    def __str__(self):
        return "{0} {1} {2}".format(
            self.nombres, self.primer_apellido, self.segundo_apellido)

    @models.permalink
    def get_absolute_url(self):
        #from django.core.urlresolvers import reverse
        #return reverse('app1.views.details', args=[str(self.id)])
        return ('apps:test1_app:index')

    @models.permalink
    def get_update_url(self):
        #from django.core.urlresolvers import reverse
        #return reverse('app1.views.details', args=[str(self.id)])
        return ('apps:test1_app:index', [self.pk])

    @models.permalink
    def get_delete_url(self):
        #from django.core.urlresolvers import reverse
        #return reverse('app1.views.details', args=[str(self.id)])
        return ('apps:test1_app:index', [self.pk])