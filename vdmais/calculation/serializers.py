from django.utils.translation import ugettext as _
from django.conf import settings

from rest_framework import serializers

from . import choices


class CalcSerializer(serializers.Serializer):
    name = serializers.CharField(label=_('Server name'), max_length=20)
    clients = serializers.IntegerField(label=_('Number power clients'), min_value=1, max_value=35)
    systems = serializers.IntegerField(label=_('Number of external systems'), min_value=50, max_value=1000)
    cores = serializers.ChoiceField(choices=choices.core_choices, label=_('Number of cores in processor / RAM'))

    def validate_systems(self, value):
        if value % 50 != 0:
            raise serializers.ValidationError(_('The number of external systems must be a multiple of 50'))
        return value

    def calc(self, data):
        total = 0
        amount_list = []

        for i in data:
            amount = settings.AMOUNT_MIN + 10 * (
                pow(i['systems'], 0.25) + 50 * pow(i['clients'], 0.5) + choices.power[i['cores']])

            amount = round(amount, 2)
            total += amount
            amount_list.append({'name': i['name'], 'amount': amount})

        return {'total': round(total, 2), 'amounts': amount_list}
