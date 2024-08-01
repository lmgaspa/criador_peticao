$(document).ready(function() {
    // Aplica máscara aos campos
    function aplicarMascara() {
      const tipoPessoa = $('input[name="tipo_pessoa"]:checked').val();
      if (tipoPessoa === 'CPF') {
        $('#cpf_cnpj').unmask().mask('000.000.000-00', {reverse: true});
      } else if (tipoPessoa === 'CNPJ') {
        $('#cpf_cnpj').unmask().mask('00.000.000/0000-00', {reverse: true});
      }
  
      // Máscaras para as testemunhas
      $('#testemunha_cpf1').unmask().mask('000.000.000-00', {reverse: true});
      $('#testemunha_cpf2').unmask().mask('000.000.000-00', {reverse: true});
      
      // Máscara para o CEP
      $('#cep').unmask().mask('00000-000', {reverse: true});
    }
  
    // Marca o tipo de pessoa padrão como CPF e ajusta os campos
    $('input[name="tipo_pessoa"][value="CPF"]').prop('checked', true);
    aplicarMascara();
    toggleFields();
  
    // Atualiza as máscaras e os campos ao mudar o tipo de pessoa
    $('input[name="tipo_pessoa"]').change(function() {
      aplicarMascara();
      toggleFields();
    });
  
    // Consulta o CEP e preenche os campos
    $('#consultar_cep').click(function() {
      const cep = $('#cep').val();
      if (cep) {
        $.ajax({
          url: consultarCepUrl,
          data: {'cep': cep},
          success: function(data) {
            if (data.error) {
              alert(data.error);
            } else {
              $('#rua').val(data.rua);
              $('#cidade').val(data.cidade);
              $('#estado').val(data.estado);
            }
          },
          error: function() {
            alert('Erro ao consultar o CEP.');
          }
        });
      }
    });
  
    // Alterna a exibição de campos com base no tipo de pessoa
    function toggleFields() {
      const tipoPessoa = $('input[name="tipo_pessoa"]:checked').val();
      const isCpf = tipoPessoa === 'CPF';
  
      $('#genero_field').toggle(isCpf);
      $('#nacionalidade_field').toggle(isCpf);
      $('#profissao_field').toggle(isCpf);
      
      $('#cpf_cnpj_label').text(isCpf ? 'CPF:' : 'CNPJ');
      $('#cpf_cnpj').val('');
      
      $('#endereco_label').text('Endereço:');
      $('#endereco').attr('placeholder', isCpf ? 'residente e domiciliado na...' : 'com endereço profissional na...');
      
      if (isCpf) {
        updateEndereco();
      } else {
        $('#nacionalidade').val('');
        $('#endereco').val('com endereço profissional na');
      }
    }
  
    // Atualiza o campo de endereço e nacionalidade com base no gênero
    function updateEndereco() {
      const genero = $('input[name="genero"]:checked').val();
      const nacionalidade = $('#nacionalidade');
      const endereco = $('#endereco');
  
      if (genero) {
        if (genero === 'Homem') {
          nacionalidade.val('Brasileiro');
          endereco.val('residente e domiciliado na');
        } else {
          nacionalidade.val('Brasileira');
          endereco.val('residente e domiciliada na');
        }
      } else {
        console.error('Erro: Gênero não selecionado.');
      }
    }
  
    // Configura o evento de mudança para atualizar os campos quando o tipo de pessoa é alterado
    $('input[name="tipo_pessoa"]').change(toggleFields);
  
    // Configura o evento de mudança para atualizar o endereço e nacionalidade quando o gênero é alterado
    $('input[name="genero"]').change(updateEndereco);
  });
  