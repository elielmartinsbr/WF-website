from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from subscription.models import Subscription

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # source: https://testdriven.io/blog/django-custom-user-model/
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []  # type: ignore

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = UserManager()

    subscriptions: models.QuerySet[Subscription]

    def __str__(self) -> str:
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_subscriber(self) -> bool:
        """Check whether user has active subscription."""
        if not hasattr(self, "subscription"):
            return False

        return self.subscription.is_active
