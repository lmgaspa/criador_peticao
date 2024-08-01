from django import forms

class ContratoForm(forms.Form):
    genero = forms.ChoiceField(choices=[('Homem', 'Homem'), ('Mulher', 'Mulher')], required=True)
    contratante = forms.CharField(max_length=18, required=True)  # CNPJ
    adm = forms.CharField(max_length=100, required=True)
    cpf = forms.CharField(max_length=14, required=True)
    cnpj = forms.CharField(max_length=18, required=True)
    email = forms.EmailField(required=True)
    cep = forms.CharField(max_length=9, required=True)
    rua = forms.CharField(max_length=100, required=True)
    cidade = forms.CharField(max_length=100, required=True)
    estado = forms.CharField(max_length=2, required=True)
    testemunha_nome1 = forms.CharField(max_length=100, required=False)
    testemunha_cpf1 = forms.CharField(max_length=14, required=False)
    testemunha_nome2 = forms.CharField(max_length=100, required=False)
    testemunha_cpf2 = forms.CharField(max_length=14, required=False)

