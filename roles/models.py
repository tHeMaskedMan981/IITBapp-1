"""Models for Roles, which define things a user can do."""
from uuid import uuid4
from django.db import models
from multiselectfield import MultiSelectField

PERMISSION_CHOICES = (
    ('AddE', 'Add Event'),
    ('UpdE', 'Update Event'),
    ('DelE', 'Delete Event'),
    ('UpdB', 'Update Body'),
    ('Role', 'Modify Roles'),
)

class BodyRole(models.Model):
    """A role for a bodywhich can be granted to multiple users."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    body = models.ForeignKey('bodies.Body', on_delete=models.CASCADE, related_name='roles')
    inheritable = models.BooleanField(default=False)
    permissions = MultiSelectField(choices=PERMISSION_CHOICES)

    class Meta:
        verbose_name = "Body Role"
        verbose_name_plural = "Body Roles"
        ordering = ("body__name",)

    def __str__(self):
        return self.body.name + " " + self.name


INSTITUTE_PERMISSION_CHOICES = (
    ('AddB', 'Add Body'),
    ('DelB', 'Delete Body'),
    ('BodyChild', 'Modify Body-Child Relations'),
    ('Location', 'Full control over locations'),
    ('Role', 'Modify Institute Roles'),
    ('RoleB', 'Modify roles for any body'),
)

class InstituteRole(models.Model):
    """An institute role which can be granted to multiple users."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    permissions = MultiSelectField(choices=INSTITUTE_PERMISSION_CHOICES)

    class Meta:
        verbose_name = "Institute Role"
        verbose_name_plural = "Institute Roles"

    def __str__(self):
        return self.name
