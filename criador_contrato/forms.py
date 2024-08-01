# forms.py
from django import forms

class ContratoForm(forms.Form):
    tipo_pessoa = forms.ChoiceField(choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ')], required=True)
    genero = forms.ChoiceField(choices=[('Homem', 'Homem'), ('Mulher', 'Mulher')], required=False)
    contratante = forms.CharField(max_length=100, required=True)
    nacionalidade = forms.CharField(max_length=100, required=False)
    cpf = forms.CharField(max_length=14, required=False)
    cnpj = forms.CharField(max_length=18, required=False)
    profissao = forms.CharField(max_length=100, required=False)
    cep = forms.CharField(max_length=9, required=True)
    rua = forms.CharField(max_length=100, required=True)
    cidade = forms.CharField(max_length=100, required=True)
    estado = forms.CharField(max_length=2, required=True)
    data_atual = forms.CharField(max_length=10, required=True)
    testemunha_nome1 = forms.CharField(max_length=100, required=False)
    testemunha_cpf1 = forms.CharField(max_length=14, required=False)
    testemunha_nome2 = forms.CharField(max_length=100, required=False)
    testemunha_cpf2 = forms.CharField(max_length=14, required=False)
