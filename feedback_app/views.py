#! coding: utf-8
from django.conf import settings
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.utils.translation import activate
activate('en')
from django.template import Context
import webodt
from webodt.converters import converter
conv = converter()
#
from feedback_app.models import Contact, ContactForm
import num2t4ru
from num2t4ru import num2text
#
#

class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'feedback_app/form.html'
    success_url = '/thanks/'
#
    def form_valid(self, form):
        message = '{product_name} / {quarter} написал: '.format(
            product_name=form.cleaned_data.get('product_name').encode('utf-8'),
            quarter=form.cleaned_data.get('quarter'),
            num_contract=form.cleaned_data.get('num_contract'),
            contract_date=form.cleaned_data.get('contract_date').encode('utf-8'),
            name_provider=form.cleaned_data.get('name_provider').encode('utf-8'),
            boss_provider=form.cleaned_data.get('boss_provider').encode('utf-8'),
            provider_const=form.cleaned_data.get('provider_const').encode('utf-8'),
            sum_contract=form.cleaned_data.get('sum_contract'),
            accepted_sum=form.cleaned_data.get('accepted_sum'),
            sum_cancel=form.cleaned_data.get('sum_cancel'))
        message += "\n\n{0}".format(form.cleaned_data.get('contract_date'))
        template = webodt.ODFTemplate('test.odt')
        context = dict(product_name=form.cleaned_data.get('product_name'),
        quarter=form.cleaned_data.get('quarter'),
        num_contract=form.cleaned_data.get('num_contract'),
        contract_date=form.cleaned_data.get('contract_date'),
        name_provider=form.cleaned_data.get('name_provider'),
        boss_provider=form.cleaned_data.get('boss_provider'),
        provider_const=form.cleaned_data.get('provider_const'),
        sum_contract=form.cleaned_data.get('sum_contract'),
        accepted_sum=form.cleaned_data.get('accepted_sum'),
        sum_cancel=form.cleaned_data.get('sum_cancel'),
        accepted_sum_word=num2text(form.cleaned_data.get('accepted_sum')))
        #balance=num2text(form.cleaned_data.get('phone')-form.cleaned_data.get('name')))
        document = template.render(Context(context))
        docx = conv.convert(document, format='docx')
        document.close()
        return super(ContactCreateView, self).form_valid(form)
