from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ContratoForm
from docx import Document
import os
import brazilcep

def index(request):
    form = ContratoForm()
    return render(request, 'index.html', {'form': form})

def gerar_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            print("Dados recebidos do formulário:", dados)  # Log para depuração

            # Monta o endereço completo
            endereco_completo = f"{dados['rua']}, {dados['cidade']}, {dados['estado']}, CEP: {dados['cep']}"

            # Ajusta os dados conforme o tipo de pessoa
            if dados['tipo_pessoa'] == 'CNPJ':
                dados['nacionalidade'] = ''
                dados['portador'] = ''
                dados['endereco'] = 'com endereço profissional na ' + endereco_completo
            else:
                genero = dados['genero']
                dados['nacionalidade'] = 'brasileiro' if genero == 'Homem' else 'brasileira'
                dados['portador'] = 'Portador' if genero == 'Homem' else 'Portadora'
                dados['endereco'] = 'residente e domiciliado na ' + endereco_completo

            # Substitui os placeholders pelos dados do formulário
            doc_path = os.path.join(os.path.dirname(__file__), 'modelo_contrato.docx')
            doc = Document(doc_path)

            for paragrafo in doc.paragraphs:
                for chave, valor in dados.items():
                    if f'{{{{ {chave} }}}}' in paragrafo.text:
                        paragrafo.text = paragrafo.text.replace(f'{{{{ {chave} }}}}', valor)
                for run in paragrafo.runs:
                    for chave, valor in dados.items():
                        if f'{{{{ {chave} }}}}' in run.text:
                            run.text = run.text.replace(f'{{{{ {chave} }}}}', valor)

            # Prepara a resposta com o documento gerado
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=contrato_gerado.docx'
            doc.save(response)

            return response

    return HttpResponse("Método não permitido.", status=405)

def consultar_cep(request):
    cep = request.GET.get('cep')
    if cep:
        try:
            endereco = brazilcep.get_address_from_cep(cep)
            return JsonResponse({
                'rua': endereco.get('street'),
                'cidade': endereco.get('city'),
                'estado': endereco.get('uf')
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'CEP não fornecido'}, status=400)
