#!/usr/bin/env python3.10

import os
from groq import Groq

import google.generativeai as genai

import ollama

from IPython.display import Markdown
import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def format_prompt(job_description):
    prompt = f'Analise esta vaga de emprego. Pule o preâmbulo. Mantenha sua resposta \
            concisa e escreva apenas as informações  necessárias sem nenhum comentario \
            adicional. Liste apenas:\n \
            Name of role\n\
            Working hours\n \
            Country\n \
            Tech skills\n \
            Segue o texto da vaga:\n \
            {job_description}'
    return prompt

def grop_request(formatted_prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'{formatted_prompt}',
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def gemini_request(formatted_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(formatted_prompt)

    return to_markdown(response.text)

def qwen_request(formatted_prompt):
    response = ollama.chat(model='qwen2:1.5b', messages=[
    {
        'role': 'user',
        'content': f'{formatted_prompt}',
    },
    ])
    return response['message']['content']


def query_all_models(formatted_prompt):
    results = {}

    results['Llama 3-8b'] = grop_request(formatted_prompt)
    results['Gemini 1.5 Flash'] = gemini_request(formatted_prompt)
    results['qwen2:1.5b'] = qwen_request(formatted_prompt)

    return results


def main():
    with open("job_description.txt", "r") as file:
        job_description = file.read()

    formatted_prompt = format_prompt(job_description)
    results = query_all_models(formatted_prompt)

    for model, response in results.items():
        print(f"\nAnálise do {model}:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()