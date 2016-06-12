#! coding: utf-8
from django.db import models
from django.forms import ModelForm, Textarea, TextInput
#
#
class Contact(models.Model):
    product_name = models.CharField(max_length=250)
    quarter = models.DecimalField('Квартал:', max_digits=8, decimal_places=2)
    num_contract = models.DecimalField('Номер контракта:', max_digits=12, decimal_places=2)
    contract_date = models.CharField(max_length=250)
    name_provider = models.TextField('Наименование поставщика')
    boss_provider = models.CharField('Представитель поставщика', max_length=250)
    provider_const = models.CharField('Основание представителя', max_length=250)
    sum_contract = models.DecimalField('Сумма контракта:', max_digits=12, decimal_places=2)
    accepted_sum = models.DecimalField('Принят на сумму:', max_digits=12, decimal_places=2)
    sum_cancel = models.DecimalField('Расторгается на сумму:', max_digits=12, decimal_places=2)
#
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
#
    def __unicode__(self):
        return '%s' % self.product_name
#
#
class ContactForm(ModelForm):

#
    class Meta:
        model = Contact
        exclude = []
        widgets = {
            'product_name': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Название товара'}),
            'quarter': TextInput(attrs={
        'id': 'subjectstyle','placeholder' : 'Квартал'}),
            'num_contract': TextInput(attrs={
        'id': 'tellstyle', 'placeholder' : 'Номер контракта'}),
            'contract_date': TextInput(attrs={
        'id': 'messagestyle', 'placeholder' : 'Дата контракта'}),
            'name_provider': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Наименование поставщика'}),
            'boss_provider': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Представитель поставщика'}),
            'provider_const': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Основание поставщика'}),
            'sum_contract': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Сумма контракта'}),
            'accepted_sum': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Принято на сумму'}),
            'sum_cancel': TextInput(attrs={
        'id': 'namestyle', 'placeholder' : 'Расторгаем на сумму'}),
        }
