# -*- coding: utf-8 -*-  

from django.utils.translation import ugettext as _
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.http import urlquote


class Shequ(models.Model):
    '''
    社区名称
    '''
    name = models.CharField(_(u'社区'),unique=True,max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'社区列表'
        verbose_name_plural = u'社区'

class ZhiBu(models.Model):
    '''
    支部名称
    '''
    name = models.CharField(_(u'支部'),max_length=50)
    shequ = models.ForeignKey(Shequ,verbose_name=_(u'社区'))
    is_display = models.BooleanField(default=True)
    sort = models.IntegerField(_(u'排序'),default=0) 
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'支部列表'
        verbose_name_plural = u'支部'
        ordering = ('-sort',)


class Mobile(models.Model):
    '''
    联系方式
    '''
    name = models.CharField(_(u'联系人'),max_length=50)
    zhibu = models.ManyToManyField(ZhiBu,verbose_name=_(u'支部'))
    mobile = models.CharField(_(u'手机号码'),max_length=50, blank=True)
    phone = models.CharField(_(u'座机号码'),max_length=50, blank=True)
    sort = models.IntegerField(_(u'排序'),default=0) 
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'联系人列表'
        verbose_name_plural = u'联系人'
        ordering = ('-sort',)




