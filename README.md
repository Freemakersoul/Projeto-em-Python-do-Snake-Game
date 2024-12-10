# AUTOR: TIAGO ALEXANDRE DIAS PROENÇA

# UFCD 10790 - Projeto de Programação

--------------------------------------------------------------------------------------------------

# Jogo do Snake

Uma aplicação simples que serve para jogar o jogo Snake, foi desenvolvida com a framework Pygame 
de Python, que permite adicionar, eliminar e listar os utilizadores e pontuações associadas, 
permite ainda selecionar o utilizador desejado para jogar.

--------------------------------------------------------------------------------------------------

## Índice

- [Introdução](#introdução)
- [Âmbito do Projeto](#âmbito-do-projeto)
- [Levantamento de Requisitos](#levantamento-de-requisitos)
- [Elaboração do Projeto](#elaboração-do-projeto)
- [Desempenho do Projeto](#desempenho-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Resultados](#resultados)
- [Conclusão](#conclusão)
- [Trabalhos Futuros](#trabalhos-futuros)

--------------------------------------------------------------------------------------------------

## Introdução

Este projeto consiste numa numa aplicação com um ambiente gráfico simples para jogar o jogo 
da cobra (o "Snake").
A aplicação possuí funcionalidades para adicionar e remover utilizadores, e funcionalidades para listar os 
utilizadores e as pontuações associadas ao mesmos.

--------------------------------------------------------------------------------------------------

## Âmbito do Projeto

- **Objetivo**: Desenvolver uma aplicação simples do jogo da cobra para o utilizador se entreter.
- **Objetivos Específicos**:

  - Implementar funcionalidades CRUD (Adicionar, Eliminar, Listar, Ler e Escrever)
  - Implementar funcionalidades de navegação entre menus e telas.
  - Implementar funcionalidades dinamicas entre teclado e rato
  - Utilizar uma ficheiro JSON para armazenamento e consulta de dados.


- **Público-Alvo**: 
- Jogadores em geral
- Jogadores de retro games
- Pessoas nas faixas etarias de 6 anos para cima.

--------------------------------------------------------------------------------------------------

- ## **Limitações**:
- Falta de conhecimento em programação  em geral
- Falta de conhecimento da framework Pygame
- Tempo limitado para desenvolvimento
- Falta de conhecimento em manipulacao de ficheiros JSON ou 
  base de dados para implementar no projeto

--------------------------------------------------------------------------------------------------

## Levantamento de Requisitos

### Requisitos Funcionais

- **RF01**: A aplicação deve permitir adicionar utilizadores.
- **RF02**: A aplicação deve permitir eliminar utilizadores.
- **RF03**: A aplicação deve permitir listar utilizadores.
- **RF04**: A aplicação deve permitir listar utilizadores e pontuações associadas.

### Requisitos Não Funcionais

- **RNF01**: Python 3.12.6
- **RNF02**: Pygame 2.6.1 (Framework de python virada para jogos)
- **RNF03**: Biblioteca "json", para manipulação de ficheiros JSON
- **RNF04**: Biblioteca "random", para gerar posicionamento aleatório da comida
- **RNF05**: Biblioteca "os", para manipulação de ficheiros
- **RNF06**: Biblioteca "pygame", para criação de jogos
- **RNF07**: Biblioteca "sys", para interagir com o sistema operativo e o interpretador de Python

--------------------------------------------------------------------------------------------------

## Desenvolvimento do Projeto

### Arquitetura

A arquitetura da aplicação é dividida em duas partes principais:

- **Front-End**: Interface gráfica para facilitar a interação do utilizador com a aplicação.
- **Back-End**: Lógica de jogo, funcionalidades da aplicação e manipulação de dados.

### Tecnologias Utilizadas

- **Linguagens**: Python 3.12.6
- **Bibliotecas**:
  - `json`: Para manipulação de ficheiros JSON.
  - `random`: Para gerar posicionamento aleatório da comida.
  - `os`: Para manipulação de ficheiros.
  - `pygame`: Para criação de jogos.
  - `sys`: Para interagir com o sistema operativo e o interpretador de Python.
- **Ferramentas**:
  - GitHub para controlo de versão.
  - Visual Studio Code como IDE.

### Implementação

- Documentar ficheiros do projeto com os comentários para perceber as funcionalidades

--------------------------------------------------------------------------------------------------

## Desempenho do Projeto

### Testes Realizados

- **Testes funcionais**: Verificação da funcionalidade xpto...

--------------------------------------------------------------------------------------------------

## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/nome-do-utilizador/nome-do-projeto.git

# Navegar até ao diretório do projeto
cd nome-do-projeto

# Instalar as dependências (se necessário)
pip install biblioteca

# Executar a applicação
python main.py
```
