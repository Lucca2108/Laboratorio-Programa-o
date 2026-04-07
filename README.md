# 🎮 Ruína Fantasmagórica - Jogo em Python

## 📌 Descrição do Projeto

Este projeto consiste em um jogo interativo em Python, inspirado em RPGs clássicos baseados em texto, onde o jogador toma decisões que influenciam diretamente o rumo da história.

O jogador explora uma ruína misteriosa, enfrenta inimigos, coleta itens e evolui seu personagem ao longo da jornada.

Além disso, o projeto aplica conceitos fundamentais de programação, como funções, herança, programatratamento de erros e testes unitários.

---

## 🎯 Objetivo

Desenvolver um sistema simples utilizando Python que:

* Utilize funções bem definidas
* Implemente tratamento de exceções
* Separe responsabilidades em diferentes arquivos
* Inclua testes automatizados
* Simule uma narrativa interativa

---

## 🧠 Conceitos Aplicados

* Funções (`def`)
* Retorno de valores (`return`)
* Tuplas (`tuple`)
* Estruturas condicionais (`if`, `elif`, `else`)
* Laços de repetição (`while`)
* Tratamento de exceções (`try`, `except`, `raise ValueError`)
* Testes unitários (`unittest`)

---

## 📁 Estrutura do Projeto

```
📦 projeto/
 ┣ 📜 historia.py       → Arquivo principal (jogo interativo)
 ┣ 📜 funcoes.py        → Funções reutilizáveis do jogo
 ┣ 📜 test_teste.py     → Testes unitários
 ┗ 📜 README.md         → Documentação do projeto
```

---

## ⚙️ Como Executar o Projeto

### ▶️ Executar o jogo

No terminal:

```
python historia.py
```

---

### 🧪 Executar os testes

```
python -m unittest teste_jogo.py
python -m unittest teste_classes.py
```
Se tudo estiver correto, o resultado será:
```
OK
```

---

## 🧩 Funções Principais

### 🔹 calcular_vida(vida, dano)

Calcula a vida restante após receber dano.

---

### 🔹 esta_vivo(vida)

Verifica se o personagem ainda está vivo.

---

### 🔹 curar(vida, cura)

Aumenta a vida do personagem.

---

### 🔹 upar_nivel(nivel, vida)

Aumenta o nível do personagem e sua vida.
Retorna dois valores (tupla).

---

### 🔹 caminho(lugar)

Retorna uma descrição com base no local escolhido.
Lança erro caso o local seja inválido.

---

## ⚠️ Tratamento de Erros

O sistema utiliza `ValueError` para evitar entradas inválidas, como:

* Dano negativo
* Cura negativa
* Locais inexistentes

Exemplo:

```
raise ValueError("Cura não pode ser negativa")
```

---

## 🧪 Testes Unitários

Os testes foram implementados utilizando a biblioteca `unittest`.

Eles garantem que:

* As funções retornam valores corretos
* Erros são lançados corretamente
* O sistema se comporta como esperado

Exemplo de teste:

```
with self.assertRaises(ValueError):
    curar(10, -5)
```

---

## 🎮 Sobre o Jogo

O jogador:

* Escolhe ações durante a exploração
* Enfrenta inimigos
* Pode usar poções de cura
* Sobe de nível
* Pode morrer (Game Over)

As escolhas impactam diretamente o desfecho da história.

---

## 🚀 Possíveis Melhorias

* Sistema de combate mais complexo
* Inventário estruturado (listas/dicionários)
* Salvamento de progresso
* Interface gráfica
* Mais caminhos e finais diferentes

## 📌 Considerações Finais

Este projeto demonstra a aplicação prática de conceitos fundamentais de programação em Python, integrando lógica, organização de código e testes automatizados em um sistema funcional e interativo.
