from django.db import models



class Group(models.Model):
    '''
    '''
    
    edu_lvl = models.BooleanField()
    faculty = models.CharField(max_length=64)
    profile = models.CharField(max_length=64)
    edu_form = models.CharField(max_length=64)
    course = models.IntegerField()
    stream = models.IntegerField()
    group = models.IntegerField()
    group_code = models.CharField(
        max_length = 256,
        )

    def __str__(self):
        return self.group_code

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

# class Schedule(models.Model):
#     '''
#     '''

#     group_code = models.ForeignKey()
#     schedule = models.JSONField()

#     class Meta:
#         verbose_name = 'Schedule'
#         verbose_name_plural = 'Schedules'
