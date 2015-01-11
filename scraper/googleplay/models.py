__author__ = 'can'

from django.db import models

class GooglePlayTopFreeApps(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=250, null=False, blank=False)
    star_count = models.FloatField(null=True, default=0)
    review_count = models.BigIntegerField(null=True, default=0)
    release_date = models.DateField(null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'googleplay_top_free_apps'
        ordering = ('id',)