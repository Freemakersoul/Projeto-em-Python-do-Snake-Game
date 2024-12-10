# AUTOR: TIAGO ALEXANDRE DIAS PROENÇA

# UFCD 10790 - Projeto de Programação

--------------------------------------------------------------------------------------------------

# Jogo do Snake / Snake Game

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

## **Limitações**:
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

- **RNF01**: Intalação do Visual Studio Code
- **RNF02**: Python 3.12.6
- **RNF03**: Pygame 2.6.1 (Framework de python virada para jogos)
- **RNF04**: Biblioteca "json", para manipulação de ficheiros JSON
- **RNF05**: Biblioteca "random", para gerar posicionamento aleatório da comida
- **RNF06**: Biblioteca "os", para manipulação de ficheiros
- **RNF07**: Biblioteca "pygame", para criação de jogos
- **RNF08**: Biblioteca "sys", para interagir com o sistema operativo e o interpretador de Python


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

**Ficheiros**:
- Ficheiros JSON:
  - users_and_scores.json: Armazenamento de dados dos utilizadores e pontuações.

- Snake_Game_main.py:
  - Ficheiro principal da aplicação que contem toda a logica do jogo e funcionalidades.

--------------------------------------------------------------------------------------------------

## Desempenho do Projeto

### Testes Realizados
- Mensagens de depuração para verificar o funcionamento da aplicação.
- Testes manuais para verificar as funcionalidades da aplicação.

**Testes funcionais**
- Verificação das funcionalidades de navegacao entre menus e telas.
- Verificação das funcionalidades de adicionar, eliminar e listar utilizadores.
- verificação das funcionalidades de listar utilizadores e pontuações associadas.
- Verificação das funcionalidades dinâmicas entre teclado e rato.
- Verificação das funcionalidades de armazenamento e consulta de dados.
- Veriificação das funcionalidades de jogo (movimento da cobra, colisão com a comida, colisão com a 
  própria cobra, contabilidade de pontuação, pausar jogo,sair do jogo e game over)

--------------------------------------------------------------------------------------------------

## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/Freemakersoul/Projeto-em-Python-do-Snake-Game

# Navegar até ao diretório do projeto
cd Projeto_em_Python_do_Snake_Game

# Instalar as dependências (se necessário)
# instalação da biblioteca pygame no powershell do vscode
pip install pygame 

# Executar a applicação
python/Snake_Game_main.py
```
