# 🧮 Sistema de Gerenciamento de Produtos (Trabalho de Lógica de Programação)

Este projeto foi desenvolvido como **trabalho da disciplina de Lógica de Programação** da faculdade **Uninter**.
O objetivo é aplicar os conceitos aprendidos durante o curso, utilizando **estruturas condicionais**, **laços de repetição**, **funções** e **listas** em Python.

---

## 💡 Sobre o Sistema

O programa é um **sistema simples de gerenciamento de produtos**, executado totalmente no terminal.
Ele permite **adicionar, remover, atualizar e listar produtos**, além de **encerrar o programa** de forma controlada.

Todas as operações são feitas em **listas** (`lista_produtos` e `lista_precos`), sem o uso de banco de dados, o que reforça o aprendizado de manipulação de dados em memória.

---

## ⚙️ Funcionalidades

### 1. Adicionar Produto

Permite registrar novos produtos com nome e preço.
Após adicionar, o usuário pode optar por continuar adicionando ou voltar ao menu principal.

### 2. Remover Produto

Exibe todos os produtos cadastrados e permite remover um item pelo número correspondente.
Também é possível remover todos os produtos de uma vez, se desejar.

### 3. Atualizar Produto

O usuário pode escolher entre:

* Alterar o **nome** de um produto existente.
* Alterar o **preço** de um produto existente.

### 4. Listar Produtos

Mostra a lista de todos os produtos cadastrados, com seus respectivos preços e quantidades totais.

### 5. Sair

Encerra o sistema de forma segura.

---

## 🧰 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca:** `os` (usada apenas para limpar o terminal)

---

## 🧩 Estrutura do Código

O código foi organizado em **funções**, cada uma responsável por uma parte do sistema:

* `msgInicial()` → Exibe o menu principal
* `adicionar_produto()` → Adiciona novos produtos
* `remover_produto()` → Remove produtos cadastrados
* `atualizar_produto()` → Atualiza nome ou preço de produtos
* `listar_produtos()` → Lista todos os produtos cadastrados
* `indice_valido()` → Auxilia na validação de índices de produtos

---

## 🎓 Objetivo do Trabalho

Este projeto foi criado com a finalidade de **praticar lógica de programação**, reforçando o raciocínio computacional e o entendimento de como o computador "pensa".
Também demonstra o uso de **estruturas de decisão**, **repetição**, **funções** e **tratamento de erros**.

---

## 📘 Outros Estudos

Além dos trabalhos realizados na faculdade, mantenho um repositório público chamado **[My Notes](https://github.com/zJuliano/my_notes)**, onde registro todas as minhas **anotações, estudos e exercícios** feitos por fora da graduação.
O objetivo desse repositório é documentar toda a minha **evolução na programação**, de mim para mim, desde o início dos estudos até o momento em que eu criar uma carreira sólida como desenvolvedor.

---

## ✍️ Autor

- **Juliano De Almeida Santos**
- Estudante de **Análise e Desenvolvimento de Sistemas** na **Uninter**
- 💻 Foco em desenvolvimento de software e aprimoramento constante na área de programação.
- 📂 [Repositório de estudos pessoais - My Notes](https://github.com/zJuliano/my_notes)

---