#!/usr/bin/env python3

import google.generativeai as genai
import json
import sys
import re

github_comments = [
    {
        "text": "Ótimo trabalho na implementação desta feature! O código está limpo e bem documentado. Isso vai ajudar muito nossa produtividade.",
        "sentiment": ""
    },
    {
        "text": "Esta mudança quebrou a funcionalidade X. Por favor, reverta o commit imediatamente.",
        "sentiment": ""
    },
    {
        "text": "Podemos discutir uma abordagem alternativa para este problema? Acho que a solução atual pode causar problemas de desempenho no futuro.",
        "sentiment": ""
    },
    {
        "text": "Obrigado por relatar este bug. Vou investigar e atualizar a issue assim que tiver mais informações.",
        "sentiment": ""
    },
    {
        "text": "Este pull request não segue nossas diretrizes de estilo de código. Por favor, revise e faça as correções necessárias.",
        "sentiment": ""
    },
    {
        "text": "Excelente ideia! Isso resolve um problema que estávamos enfrentando há semanas. Mal posso esperar para ver isso implementado.",
        "sentiment": ""
    },
    {
        "text": "Esta issue está aberta há meses sem nenhum progresso. Podemos considerar fechá-la se não for mais relevante?",
        "sentiment": ""
    },
    {
        "text": "Ótimo trabalho na implementação desta feature! O código está limpo e bem documentado. Isso vai ajudar muito nossa produtividade.",
        "sentiment": ""
    }
]

def create_prompt(context, task, examples, clasify, response_format):
    all_examples = ''
    for example in examples:
        all_examples += example
    result = '<prompt>' + \
            '<context>' + context + '</context>' + \
            '<instruction>' + task + \
            '<response_format>' + response_format + '<response_format>' + \
            all_examples + \
            '<clasify>' + clasify + '</clasify>' + \
            '</instruction>' + \
            '</prompt>'

    return result

def call_llm(text):
    examples = ['comentario: Não entendo por que estamos priorizando esta feature. Existem problemas mais críticos que deveríamos estar abordando.\nsentimento: Negativo', \
                'comentario: Boa captura! Este edge case não tinha sido considerado. Vou adicionar testes para cobrir este cenário..\nsentimento: Positivo', \
                'comentario: O novo recurso está causando conflitos com o módulo Y. Precisamos de uma solução urgente para isso.\nsentimento: Negativo'
                ]
    prompt = create_prompt('Nossa equipe saber os comentarios do usuarios, \
                            para antender as demandas quando forem negativos, \
                            para se sentirem motivados quando forem positivos.',
                            'Clasifique o comentario por sentimeto, positivo ou negativo:',
                            examples,
                            text,
                            'Retorne a responsta em fomato json: {text: comentario, sentiment: positivo/negativo}'
                            )
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text

def parse_llm_response(response):
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    json_content = match.group(1)
    response_dict = json.loads(json_content)
    return response_dict['sentiment']

def analyze_sentiments(comments):
    for comment in comments:
        llm_response = call_llm(comment["text"])
        comment["sentiment"] = parse_llm_response(llm_response)

analyze_sentiments(github_comments)

# Imprimir resultados
for comment in github_comments:
    print(f"Texto: {comment['text']}")
    print(f"Sentimento: {comment['sentiment']}")
    print("-" * 50)