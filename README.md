# Inmersão GenAI 42

Este repositório contém o projeto desenvolvido durante a **Imersão GenAI**, onde exploramos desde a introdução ao **Python**, passando por **Web Scraping**, **engenharia de prompts**, até a utilização de **ChromaDB** para embeddings e a criação de um sistema de **RAG (Retrieval-Augmented Generation)** com o modelo **Gemini**.

## Estrutura dos Projetos

### Projeto 1: Introdução à Linguagem Shell
- **Objetivo:** Primeiros passos com comandos e scripts em shell.

### Projeto 2: Introdução ao Python e Web Scraping
- **Objetivo:** Uso de Python para capturar dados da API da Wikipedia e web scraping do site para seguir o "Roads to Philosophy" apartir do input.

### Projeto 3: Modelos Locais e por API
   - **Técnica:** Completion prompting e estruturação do prompt com **XML*
     
      - Descrição: Testamos modelos como **Qwen** (local), **LLaMA com Groq** e **Gemini** para analisar vagas de emprego e retornar os dados de maneira estruturada.

### Técnicas de Prompting Utilizadas no Projeto 4

- **ex00: Análise de Sentimentos**
  - **Técnica:** Few-shot prompting
    - Descrição: Alguns exemplos de análises anteriores foram incluídos no prompt para guiar o modelo em como estruturar a resposta.

- **ex01: Análise de Perspectivas (École 42)**
  - **Técnica:** Role prompting
    - Descrição: Utilizamos diferentes "papéis" (educador, estudante, recrutador) para guiar o modelo a responder a partir de perspectivas específicas.

- **ex02: Análise de Filmes**
  - **Técnica:** Structured output prompting e Few-shot prompting
    - Descrição: O prompt foi criado para que o modelo retornasse as informações estruturadas em formato JSON, garantindo que os dados fossem organizados conforme o esperado.

- **ex03: Cadeia de Prompts (Claude Shannon)**
  - **Técnica:** Chain-of-thought prompting
    - Descrição: A tarefa foi dividida em várias etapas, onde cada parte do processo se baseava nas respostas anteriores para criar uma análise mais profunda e estruturada.
  - **Técnica:** Multi-shot prompting
    - Descrição: Vários prompts interligados foram usados para solicitar ao modelo que desenvolvesse e sintetizasse informações em uma análise final abrangente.


### Projeto 5: Segurança em APIs
- **Objetivo:** Estudo sobre OWASP Top 10 API Security Risks.

### Técnicas de Prompting Utilizadas no Projeto 6

- **ex00: Criação de Embeddings e Retorno de Trechos Relacionados**
  - **Técnica:** Embedding-based retrieval
    - Descrição: Utilizamos o **ChromaDB** para gerar embeddings dos currículos e realizar a recuperação de trechos relevantes dos documentos com base no input do usuário, utilizando a similaridade de cosseno entre os embeddings.

- **ex01: Geração de Respostas com RAG (Retrieval-Augmented Generation)**
  - **Técnica:** Contextual prompting
    - Descrição: Construímos um prompt dinâmico que inclui tanto a pergunta do usuário quanto trechos relevantes dos documentos recuperados via embeddings. Esse prompt é enviado ao modelo **Gemini**, que gera uma resposta utilizando as informações de referência.
  - **Técnica:** Natural language prompting
    - Descrição: O prompt foi criado para garantir que o modelo forneça uma resposta clara, abrangente e em linguagem simples, ajustada para um público não técnico.

## Tecnologias Utilizadas
- **Python**
- **ChromaDB**
- **Gemini**
- **Qwen (local)**
- **LLaMA**
- **Streamlit**
- **Groq**
- **Web Scraping**
- **Segurança em APIs**

## Como rodar os projetos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
2. Crie o ambiente virtual e instale as dependencias:
   ```bash
   pytho3 -m venv venv
   pip install -r requirements.txt
3. Execute cada projeto na respectiva pasta.
   
