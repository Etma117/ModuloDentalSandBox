from django import forms
from django.utils.dateparse import parse_datetime
from django.forms.widgets import DateInput, TimeInput, Select

class SplitDateTimeWidgetCustom(forms.MultiWidget):
    def __init__(self, attrs=None):
        date_attrs = {'type': 'date', 'class': 'form-control'}
        time_attrs = {'class': 'form-control'}

        # Crear opciones para cada hora del día (24 horas)
        hour_options = [(str(i), f'{i:02d}:00') for i in range(24)]

        widgets = (
            DateInput(attrs=date_attrs),
            Select(attrs=time_attrs, choices=[('', 'Seleciona una hora')] + hour_options),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            # Parseamos el valor a datetime para asegurar que sea una instancia de datetime.datetime
            return [parse_datetime(str(value))]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        date_value, time_value = super().value_from_datadict(data, files, name)
        if date_value and time_value:
            return f"{date_value} {time_value}"
        return None
