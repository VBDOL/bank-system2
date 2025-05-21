# 🏦 Sistema Bancário em Python - Versão 2

## 📌 Sobre o Projeto
Este projeto é uma **versão aprimorada** do sistema bancário inicial, agora mais **modularizado** e escalável! 🎯 Ele permite que usuários realizem operações bancárias como **depósitos, saques e consultas de extrato**, além de **cadastrar clientes e criar contas bancárias**.  

A modularização foi realizada separando as funcionalidades em arquivos distintos para **melhor organização** e **facilidade de manutenção**.  

---

## 📁 Estrutura do Projeto
```shell
bank-system2/
│── clientes.py            # Funções para cadastro e listagem de usuários
│── contas.py              # Funções para criar e listar contas bancárias
│── operacoes_bancarias.py # Funções para saque, depósito e extrato
│── main.py                # Arquivo principal para interação com o usuário
│── README.md              # Documentação do projeto

````

##🚀 Funcionalidades<br>
🔹 Operações Bancárias<br>
✅ Depositar: Usuário pode inserir valores e atualizar saldo. <br>✅ Sacar: Verifica saldo disponível, limite por saque e número máximo de saques. <br>✅ Exibir Extrato: Lista todas as movimentações financeiras.

🔹 Gerenciamento de Clientes<br>
✅ Criar Usuário: Nome, data de nascimento, CPF e endereço são cadastrados. <br>✅ Evita CPFs duplicados: Garante que não haja clientes repetidos no sistema. <br>✅ Listar Usuários: Exibe todos os clientes cadastrados.

🔹 Gerenciamento de Contas<br>
✅ Criar Conta Corrente: Vincula um cliente do banco à conta, gerando um número sequencial. <br>✅ Listar Contas: Exibe todas as contas bancárias existentes.

🔄 Melhorias Implementadas<br>
##📌 Código Modularizado<br>
Antes, todas as funções estavam em um único arquivo. Agora, cada responsabilidade foi separada:<br> ✔️ operacoes_bancarias.py → Saque, depósito e extrato.<br>✔️ clientes.py → Cadastro e listagem de clientes. <br>✔️ contas.py → Criação e listagem de contas bancárias. <br>✔️ main.py → Interface principal que chama todas as funções.

##📌 Uso de Listas para Registro de Dados<br>
✔️ Extrato armazenado em uma lista, melhorando manipulação de transações. <br>✔️ Usuários e Contas também armazenados em listas, facilitando validações.

##📌 Melhor Validação e Feedback<br>
✔️ CPF formatado corretamente para evitar erros na busca de clientes. <br>✔️ Verificação de duplicidade de CPF ao criar clientes. <br>✔️ Confirmações mais claras para cada operação realizada.

##🎯 Como Executar<br>
1️⃣ Baixe o projeto ou clone via Git:

shell
git clone https://github.com/VBDOL/bank-system2.git
cd bank-system2
2️⃣ Execute o arquivo principal (main.py):

shell
python main.py
3️⃣ Utilize o menu interativo para operações bancárias!

shell
[d] Depositar  
[s] Sacar  
[e] Extrato  
[c] Criar usuário  
[l] Listar usuários  
[n] Criar conta  
[m] Listar contas  
[q] Sair

##🤝 Contribuição
🔹 Se quiser contribuir, sinta-se à vontade para abrir pull requests! 💡 🔹 Sugestões e melhorias são sempre bem-vindas!

📩 Contato: VBDOL.DEV

🎉 Obrigado por explorar nosso sistema bancário! 🚀

---

### 🔥 **O que este `README.md` faz?**
✅ Explica o propósito do projeto.  
✅ Apresenta a **estrutura dos arquivos**.  
✅ Detalha **funcionalidades e melhorias** da versão 2.  
✅ Fornece **instruções de execução**.  
✅ Incentiva **colaboração no GitHub**.  
