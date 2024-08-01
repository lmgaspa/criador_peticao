$(document).ready(function() {
  // Função para aplicar a máscara
  function aplicarMascara() {
      $('#cpf').unmask().mask('000.000.000-00', {reverse: true});
      $('#cep').unmask().mask('00000-000', {reverse: true});
      $('#testemunha_cpf1').unmask().mask('000.000.000-00', {reverse: true});
      $('#testemunha_cpf2').unmask().mask('000.000.000-00', {reverse: true});
  }

  // Inicializa as máscaras
  aplicarMascara();

  // Consulta o CEP e preenche os campos
  $('#consultar_cep').click(function() {
      const cep = $('#cep').val();
      if (cep) {
          $.ajax({
              url: '{% url "consultar_cep" %}',
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
});
