# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.views.generic.edit import CreateView
from contacts.models import Contacts
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail


class CreateMessage(CreateView):
    model = Contacts
    template_name = 'contacts.html'
    success_url=reverse_lazy('Contacts')

    def form_valid(self, form):
        obj = form.save()
        full_message = u'Достопочтенный и многоуважаемый ' + obj.recipient.name + ' ' + obj.recipient.surname + '! '
        full_message += u'Спешу уведомить Вас о неподобающем поведении студента '
        full_message += obj.victim.surname + u' (курса ' + unicode(obj.victim.courses.first()) + u'). \n'
        full_message += u'Дело в следующем. ' + obj.message
        full_message += u'\nС уважением, один из Ваших студентов.'
        send_mail(obj.subject, full_message, 'from@pybursa.com',
                  [obj.recipient.email], fail_silently=False)
        messages.success(self.request,'Message was send.')
        return super(CreateMessage, self).form_valid(form)
