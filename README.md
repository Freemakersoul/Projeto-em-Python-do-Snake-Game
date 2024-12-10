# AUTOR: TIAGO ALEXANDRE DIAS PROENÇA

# UFCD 10790 - Projeto de Programação

--------------------------------------------------------------------------------------------------

# Jogo do Snake / Snake Game

Uma aplicação simples que serve para jogar o jogo Snake, foi desenvolvida com a framework Pygame 
de Python, que permite adicionar, eliminar utilizadores e listar os utilizadores e pontuações 
associadas, permite ainda selecionar o utilizador desejado para jogar.

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
  - Implementar funcionalidades dinâmicas entre teclado e rato
  - Utilizar um ficheiro JSON para armazenamento e consulta de dados.


- **Público-Alvo**: 
- Jogadores em geral
- Jogadores de retro games
- Pessoas nas faixas etárias de 6 anos para cima.

--------------------------------------------------------------------------------------------------

## **Limitações**:
- Falta de conhecimento em programação em geral
- Falta de conhecimento da framework Pygame
- Tempo limitado para desenvolvimento
- Falta de conhecimento em manipulação de ficheiros JSON ou 
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
  - `pygame (versão - 2.6.1)`: Para criação de jogos.
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
- Correr a aplicação através do terminal.

### Testes funcionais
- Verificação das funcionalidades de navegação entre menus e telas.
- Verificação das funcionalidades de adicionar, eliminar e listar utilizadores.
- verificação das funcionalidades de listar utilizadores e pontuações associadas.
- Verificação das funcionalidades dinâmicas entre teclado e rato.
- Verificação das funcionalidades de armazenamento e consulta de dados.
- Veriificação das funcionalidades de jogo (movimento da cobra, colisão com a comida, colisão com 
  a própria cobra, contabilidade de pontuação, pausar jogo, sair do jogo e game over)

--------------------------------------------------------------------------------------------------

## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/Freemakersoul/Projeto-em-Python-do-Snake-Game

# Instalar as dependências 
# Instalação da biblioteca pygame no powershell do vscode
pip install pygame 

# Navegar até ao diretório do projeto
cd Projeto_em_Python_do_Snake_Game

# Executar a applicação
python Snake_Game_main.py
```
--------------------------------------------------------------------------------------------------

## Conclusão

### Difilcudades
Neste projeto, enfrentei algumas dificuldades por ter falta de conhecimento em programação de um 
modo geral, falta de conhecimento da framework Pygame, que foi a que escolhi para desenvolver o 
meu projeto e falta de conhecimento em manipulação de ficheiros JSON ou base de dados para 
implementar no projeto.

Na manipulação de ficheiros tive dificuldades em passar e remover parametros para o ficheiro JSON, 
pois não sabia bem como o fazer, mas depois de pesquisar e estudar consegui resolver uma parte do 
problema. Consegui passar e remover utilizadores mas nao conseguia lista-los corretamente, a nivel 
das pontuacoes associadas aos utilizadores nao consegui resolver, mas com a ajuda do formador 
todos os problemas foram resolvidos e consegui finalizar o projeto como tinha idealizado.

### Reflexão
Adorei fazer este projeto, foi uma experiência muito boa e aprendi muito, mesmo com as dificuldades
que apareceram, e aprendi muito com o formador, que foi muito paciente e sempre disposto a ajudar.
Ainda assim tenho de continuar a estudar e aprender mais sobre programação para poder compreender e 
aplicar melhor os conceitos e funcionalidades num projeto. O facto de explorarmos por nós mesmos 
e criar algo do nosso gosto foi muito gratificante e deu-me mais vontade de continuar a aprender e 
evoluir cada vez mais.

### Trabalhos Futuros
Espero em projetos futuros poder aplicar melhor o que aprendi neste projeto e poder trabalhar 
melhor o código sempre de forma a mante-lo simples, eficiente e o mais legível possível. 
Espero também evoluir bastante na manipulação de informação de base de dados e/ou ficheiros JSON
para implementar noutros projetos de aplicações e web sites.
Pretendo evoluir a todos os níveis e poder aplicar a minha criatividade livremente.


