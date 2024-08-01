import pytest
from django.urls import reverse
from django.test import Client
from django.http import JsonResponse

@pytest.mark.django_db
def test_gerar_contrato_post():
    client = Client()

    url = reverse('gerar_contrato')
    data = {
        'genero': 'Homem',
        'contratante': '13.273.587/0001-54',
        'cnpj': '13.273.587/0001-54',
        'adm': 'Luiz',
        'cpf': '044.444.444-44',
        'email': 'luiz@example.com',
        'cep': '45600-730',
        'rua': 'Rua Zildo Pedro Guimarães Júnior',
        'cidade': 'Itabuna',
        'estado': 'BA',
        'testemunha_nome1': 'Agenor',
        'testemunha_cpf1': '040.404.040-40',
        'testemunha_nome2': 'Irene',
        'testemunha_cpf2': '404.004.044-00'
    }

    response = client.post(url, data)

    if response.status_code != 200:
        print(response.content.decode())  # Imprime o conteúdo da resposta para depuração

    assert response.status_code == 200, "Verifique a view gerar_contrato para aceitar POST requests"
    # Verifique se a resposta é um documento
    assert response['Content-Type'] == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', "O tipo de conteúdo deve ser um documento Word"

@pytest.mark.django_db
def test_consultar_cep_get():
    client = Client()

    url = reverse('consultar_cep')
    response = client.get(url, {'cep': '45600-730'})

    assert response.status_code == 200, "A view consultar_cep deve retornar status 200"
    assert isinstance(response, JsonResponse), "A resposta deve ser um JsonResponse"
    data = response.json()
    assert 'rua' in data and 'cidade' in data and 'estado' in data, "A resposta deve conter rua, cidade e estado"
