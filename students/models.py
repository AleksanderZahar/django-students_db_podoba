# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class Student(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"
        ordering = ['last_name']

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище"
    )

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Ім\'я'
    )

    middle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"По-батькові",
        default=""
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True
        # null=True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Студ. квиток"
    )

    student_group = models.ForeignKey(
        'Group',
        blank=False,
        verbose_name=u'Група',
        null=True,
        on_delete=models.PROTECT
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові відомості"
    )

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"
        ordering = ['title']

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва групи"
    )

    leader = models.OneToOneField(
        'Student',
        blank=True,
        verbose_name=u'Староста',
        null=True,
        on_delete=models.SET_NULL
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові відомості"
    )

    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s" % (self.title,)
