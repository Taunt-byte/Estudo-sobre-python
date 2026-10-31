# 20 exercícios de Python — Do básico ao intermediário

## Nível 1 — Fundamentos e lógica

Objetivo: desenvolver raciocínio lógico e dominar os principais recursos da linguagem.

Exercício 01 — Analisador de informações pessoais

Crie um programa que solicite nome, idade, altura e cidade do usuário.

O programa deverá:

- Exibir um resumo das informações.
- Calcular quantos anos faltam para completar 100 anos.
- Informar se o usuário é maior ou menor de idade.
- Exibir uma mensagem personalizada.

Exercício 02 — Calculadora inteligente

Desenvolva uma calculadora que receba dois números e uma operação matemática.

Operações:

- Adição.
- Subtração.
- Multiplicação.
- Divisão.
- Potenciação.
- Resto da divisão.

O programa deverá tratar divisão por zero e operações inválidas.

Exercício 03 — Conversor de unidades

Desenvolva um conversor que permita transformar:

- Celsius em Fahrenheit e Kelvin.
- Quilômetros em milhas.
- Metros em centímetros.
- Quilogramas em libras.
- Horas em minutos e segundos.

Permita que o usuário escolha a conversão desejada.

Exercício 04 — Analisador de números

Solicite cinco números ao usuário e apresente:

- Maior número.
- Menor número.
- Média aritmética.
- Quantidade de números pares.
- Quantidade de números ímpares.
- Números em ordem crescente.

Exercício 05 — Simulador de caixa eletrônico

Desenvolva um programa que simule um caixa eletrônico.

O usuário deverá informar o valor que deseja sacar.

O sistema deverá:

- Verificar se possui saldo suficiente.
- Calcular a quantidade de notas necessárias.
- Trabalhar com notas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
- Atualizar o saldo após o saque.
- Impedir operações inválidas.

## Nível 2 — Estruturas de dados e controle

Objetivo: trabalhar com listas, dicionários, repetições e manipulação de informações.

Exercício 06 — Gerenciador de tarefas

Crie um programa de gerenciamento de tarefas.

Funcionalidades:

- Adicionar tarefas.
- Listar tarefas.
- Marcar tarefas como concluídas.
- Excluir tarefas.
- Exibir quantidade de tarefas pendentes e concluídas.

Utilize listas e dicionários.

Exercício 07 — Sistema de votação

Desenvolva um sistema de votação com três candidatos.

O programa deverá:

- Registrar votos.
- Permitir votos em branco.
- Impedir opções inválidas.
- Contabilizar os votos.
- Apresentar o vencedor.
- Calcular a porcentagem de votos de cada candidato.

Exercício 08 — Analisador de palavras

Solicite uma frase ao usuário e desenvolva um programa que:

- Conte a quantidade de palavras.
- Conte a quantidade de caracteres.
- Identifique a palavra mais longa.
- Identifique palavras repetidas.
- Conte quantas vogais existem.
- Exiba as palavras em ordem alfabética.

Exercício 09 — Agenda de contatos

Desenvolva uma agenda telefônica.

Cada contato deverá possuir:

- Nome.
- Telefone.
- E-mail.
- Cidade.

Funcionalidades:

- Cadastrar contatos.
- Pesquisar por nome.
- Atualizar informações.
- Excluir contatos.
- Listar todos os contatos.

Exercício 10 — Jogo de adivinhação avançado

Crie um jogo no qual o computador escolhe um número aleatório.

Requisitos:

- Três níveis de dificuldade.
- Quantidade limitada de tentativas.
- Dicas de números maiores ou menores.
- Pontuação baseada na quantidade de tentativas.
- Possibilidade de jogar novamente.
- Histórico das melhores pontuações.

## Nível 3 — Funções e organização

Objetivo: aprender a dividir programas em partes menores, reutilizáveis e organizadas.

Exercício 11 — Validador de senhas

Desenvolva um programa que avalie a segurança de uma senha.

Critérios:

- Pelo menos oito caracteres.
- Uma letra maiúscula.
- Uma letra minúscula.
- Um número.
- Um caractere especial.

O programa deverá informar quais critérios foram atendidos e quais precisam ser corrigidos.

Exercício 12 — Gerador de senhas aleatórias

Crie um gerador de senhas personalizável.

O usuário deverá escolher:

- Comprimento da senha.
- Inclusão de letras maiúsculas.
- Inclusão de letras minúsculas.
- Inclusão de números.
- Inclusão de caracteres especiais.

O programa deverá gerar uma senha aleatória seguindo as preferências.

Exercício 13 — Sistema de análise de notas

Crie um programa para gerenciar notas de estudantes.

Cada estudante deverá possuir três notas.

O sistema deverá:

- Calcular a média.
- Identificar aprovação ou reprovação.
- Listar estudantes aprovados.
- Listar estudantes reprovados.
- Identificar a maior e menor média.
- Calcular a média geral da turma.

Utilize funções para organizar as operações.

Exercício 14 — Simulador bancário

Desenvolva um sistema bancário com as seguintes operações:

- Criar conta.
- Consultar saldo.
- Depositar dinheiro.
- Sacar dinheiro.
- Consultar extrato.
- Encerrar o programa.

Registre as movimentações e impeça saques superiores ao saldo disponível.

Exercício 15 — Analisador de arquivos de texto

Crie um programa que receba um arquivo `.txt` e analise seu conteúdo.

O sistema deverá:

- Contar linhas.
- Contar palavras.
- Contar caracteres.
- Identificar as palavras mais frequentes.
- Identificar a linha mais extensa.
- Gerar um relatório com os resultados.

## Nível 4 — Projetos práticos

Objetivo: desenvolver pequenos sistemas utilizando conceitos mais próximos de aplicações reais.

Exercício 16 — Sistema de estoque

Desenvolva um sistema de gerenciamento de estoque.

Cada produto deverá possuir:

- Código identificador.
- Nome.
- Preço.
- Quantidade disponível.

Funcionalidades:

- Cadastrar produtos.
- Atualizar produtos.
- Registrar entrada de mercadorias.
- Registrar saída de mercadorias.
- Consultar estoque.
- Calcular o valor total do estoque.
- Identificar produtos com estoque baixo.

Exercício 17 — Investigador de logs

Crie um programa capaz de analisar arquivos de log de um sistema.

Considere registros como:

```
2026-10-31 08:30:15 INFO User logged in
2026-10-31 08:31:20 WARNING Failed login attempt
2026-10-31 08:32:10 ERROR Database connection failed
2026-10-31 08:35:40 INFO File uploaded
2026-10-31 08:40:00 ERROR Request timeout
```

O programa deverá:

- Ler o arquivo de log.
- Contabilizar INFO, WARNING e ERROR.
- Identificar os erros mais frequentes.
- Localizar tentativas de login malsucedidas.
- Identificar horários com maior quantidade de erros.
- Gerar um relatório de investigação.

Exercício 18 — Sistema de biblioteca

Desenvolva um sistema de gerenciamento de biblioteca.

Cada livro deverá possuir:

- ISBN.
- Título.
- Autor.
- Ano de publicação.
- Disponibilidade.

Funcionalidades:

- Cadastrar livros.
- Pesquisar livros.
- Registrar empréstimos.
- Registrar devoluções.
- Consultar livros disponíveis.
- Consultar livros emprestados.

Exercício 19 — Sistema de gerenciamento financeiro

Crie uma aplicação para controle financeiro pessoal.

Funcionalidades:

- Registrar receitas.
- Registrar despesas.
- Categorizar movimentações.
- Consultar saldo.
- Gerar relatório mensal.
- Identificar categorias com maiores despesas.
- Calcular percentual de gastos por categoria.

Exemplo de categorias: alimentação, transporte, moradia, lazer e educação.

Exercício 20 — Sistema de monitoramento de arquivos

Desenvolva um programa que monitore uma pasta do computador.

O sistema deverá:

- Identificar novos arquivos.
- Detectar arquivos removidos.
- Identificar arquivos modificados.
- Registrar data e horário das alterações.
- Salvar um histórico em arquivo.
- Gerar um relatório das atividades.

Utilize bibliotecas como `os`, `pathlib`, `datetime` e, como desafio extra, `hashlib`.