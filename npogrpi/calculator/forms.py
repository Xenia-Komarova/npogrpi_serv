from django import forms

from website.models import (DiameterColumn, DiameterOpenBorehole,
                            DiameterShank, Type)

from .models import ContactSearch


class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = ContactSearch
        fields = ['name', 'phone_number', 'email', 'company', 'type', 'diameter_column', 'diameter_shank', 'diameter_open_borehole']

    type = forms.ModelChoiceField(queryset=Type.objects.filter(incalc__in=[True]), label='Тип оборудования')
    diameter_column = forms.ModelChoiceField(queryset=DiameterColumn.objects.all(), label='Условный диаметр колонны')
    diameter_shank = forms.ModelChoiceField(queryset=DiameterShank.objects.all(), label='Условный диаметр хвостовика')
    diameter_open_borehole = forms.ModelChoiceField(queryset=DiameterOpenBorehole.objects.all(), label='Диаметр открытого ствола')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['diameter_column'].queryset = DiameterColumn.objects.all()
        self.fields['diameter_shank'].queryset = DiameterShank.objects.all()
        self.fields['diameter_open_borehole'].queryset = DiameterOpenBorehole.objects.all()

        #if 'type' in self.data:
            #try:
                #type_id = int(self.data.get('type'))
                #self.fields['diameter_column'].queryset = DiameterColumn.objects.filter(type_id=type_id)
                #self.fields['diameter_shank'].queryset = DiameterShank.objects.filter(type_id=type_id)
                #self.fields['diameter_open_borehole'].queryset = DiameterOpenBorehole.objects.filter(type_id=type_id)
           # except (ValueError, TypeError):
                #pass

class ProductSelectionForm(forms.ModelForm):
    class Meta:
        model = ContactSearch
        fields = ['name', 'phone_number', 'email', 'company', 'diameter_column', 'diameter_shank', 'diameter_open_borehole', 'stages_quantity']
    type_choices = [(type.slug, type.name) for type in Type.objects.filter(inmgrp__in=[True])]
    diameter_column = forms.ModelChoiceField(queryset=DiameterColumn.objects.all(), label='Условный диаметр колонны')
    diameter_shank = forms.ModelChoiceField(queryset=DiameterShank.objects.all(), label='Условный диаметр хвостовика')
    diameter_open_borehole = forms.ModelChoiceField(queryset=DiameterOpenBorehole.objects.all(), label='Диаметр открытого ствола')
    stages_quantity = forms.IntegerField(label='Количество стадий')

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['type'].choices = [(type.slug, type.name) for type in Type.objects.filter(inmgrp=True)]


    def clean(self):
        cleaned_data = super().clean()
        stages_quantity = cleaned_data.get('stages_quantity')
        if stages_quantity is not None and stages_quantity <= 0:
            raise forms.ValidationError('Количество стадий должно быть положительным числом')
        return cleaned_data
