# Full-Stack – Adaptable Petition Creator for Automating .docx Models

## Description
I developed a website using Django and Bootstrap to create contract templates. The system allows users to fill in the necessary data and automatically replaces the variables in the contract, respecting the administrator's gender in this project, adjusting the new .docx according to the grammatical rules of the Portuguese language. The contract is generated in .docx format.

## Key Features

- **Customization Capability:** 
  - The system can be adapted to automate any manual document in .docx format.
  - Initially, it was based on a contract used by the political research company GPE. To ensure privacy, the company's data was replaced.
  - The true version, containing the real company data, is hosted on another cloud with closed code and restricted access.
  - This project is a practical example used in a real need of a company (preventive law), but it can be adapted for any type of petition or document .docx.

- **Form Masks:**
  - Implementation of masks for CNPJ (similar for Employer Identification Number (EIN) in the United States), CPF (similar for Social Security Number (SSN) in the United States), and CEP (similar for ZIP Code in United States), lookup using jQuery Mask.
  - The format for CPF follows xxx.xxx.xxx-xx and for CNPJ, xx.xxx.xxx/xxxx-xx (Brazilian standard).
  - Additionally, an AJAX function was implemented for automatic filling of fields related to CEP, using the brazilcep library, with a mask for the 00000-000 format (Brazilian standard).

- **File Generation:** 
  - By clicking the "Generate Contract" button, the system creates a new .docx file with the data filled in by the user.

- **Testing:** 
  - Use of pytest and pytest-django to ensure the quality and reliability of the system, ensuring that all functionalities work as expected.

## Technologies Used
- **Backend:** Django
- **Frontend:** Bootstrap, jQuery, AJAX
- **Additional Libraries:** jQuery Mask, brazilcep
- **Software Testing:** pytest, pytest-django

This system not only facilitates the creation of personalized and automated documents but can also be easily adapted to meet the specific needs of different types of legal or business documents.

---

# FullStack – Criador de Petições Adaptável para Automação de Modelos .docx

## Descrição
Desenvolvi um website utilizando Django e Bootstrap para criar modelos de contratos. O sistema permite que os usuários preencham os dados necessários e substitui automaticamente as variáveis no contrato, respeitando, no caso deste projeto, o gênero do administrador, ajustando o novo .docx conforme as regras gramaticais da língua portuguesa. O contrato é gerado em formato .docx.

## Características Principais

- **Capacidade de Customização:** 
  - O sistema pode ser adaptado para automatizar qualquer documento manual em formato .docx.
  - Inicialmente, foi baseado em um contrato utilizado pela empresa de pesquisas políticas do instituto GPE. Para garantir a privacidade, os dados da empresa contratada foram substituídos.
  - A versão verdadeira, contendo os dados reais da empresa, está hospedada em outra nuvem com código fechado e acesso restrito.
  - Este projeto é um exemplo prático utilizado em uma necessidade real de uma empresa (advocacia preventiva), mas pode ser adaptado para qualquer tipo de petição ou documento .docx.

- **Máscaras de Formulário:**
  - Implementação de máscaras para CNPJ, CPF e consulta por CEP utilizando jQuery Mask.
  - A formatação para CPF segue o formato xxx.xxx.xxx-xx e para CNPJ, xx.xxx.xxx/xxxx-xx (padrão brasileiro).
  - Além disso, foi implementada uma função AJAX para preenchimento automático dos campos relacionados ao CEP, utilizando a biblioteca brazilcep, com máscara para o formato 00000-000 (padrão brasileiro).

- **Geração de Arquivo:** 
  - Ao clicar no botão "Gerar Contrato", o sistema cria um novo arquivo .docx com os dados preenchidos pelo usuário.

- **Testes:** 
  - Utilização de pytest e pytest-django para garantir a qualidade e a confiabilidade do sistema, assegurando que todas as funcionalidades funcionem conforme esperado.

## Tecnologias Utilizadas
- **Backend:** Django
- **Frontend:** Bootstrap, jQuery, AJAX
- **Bibliotecas Adicionais:** jQuery Mask, brazilcep
- **Teste de Software:** pytest, pytest-django

Este sistema não só facilita a criação de documentos personalizados e automatizados, como também pode ser facilmente adaptado para atender às necessidades específicas de diferentes tipos de documentos legais ou empresariais.
