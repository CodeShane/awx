# Copyright (c) 2013 AnsibleWorks, Inc.
# All Rights Reserved.


from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

__all__ = ['ActivityStream']


class ActivityStream(models.Model):
    '''
    Model used to describe activity stream (audit) events
    '''

    class Meta:
        app_label = 'main'

    OPERATION_CHOICES = [
        ('create', _('Entity Created')),
        ('update', _("Entity Updated")),
        ('delete', _("Entity Deleted")),
        ('associate', _("Entity Associated with another Entity")),
        ('disassociate', _("Entity was Disassociated with another Entity"))
    ]

    actor = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, related_name='activity_stream')
    operation = models.CharField(max_length=13, choices=OPERATION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    changes = models.TextField(blank=True)

    object_relationship_type = models.TextField(blank=True)
    object1 = models.TextField()
    object2 = models.TextField()

    user = models.ManyToManyField("auth.User", blank=True)
    organization = models.ManyToManyField("Organization", blank=True)
    inventory = models.ManyToManyField("Inventory", blank=True)
    host = models.ManyToManyField("Host", blank=True)
    group = models.ManyToManyField("Group", blank=True)
    inventory_source = models.ManyToManyField("InventorySource", blank=True)
    inventory_update = models.ManyToManyField("InventoryUpdate", blank=True)
    credential = models.ManyToManyField("Credential", blank=True)
    team = models.ManyToManyField("Team", blank=True)
    project = models.ManyToManyField("Project", blank=True)
    project_update = models.ManyToManyField("ProjectUpdate", blank=True)
    permission = models.ManyToManyField("Permission", blank=True)
    job_template = models.ManyToManyField("JobTemplate", blank=True)
    job = models.ManyToManyField("Job", blank=True)

    def get_absolute_url(self):
        return reverse('api:activity_stream_detail', args=(self.pk,))
