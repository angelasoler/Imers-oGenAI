#!/usr/bin/env python3

import os
from groq import Groq

import google.generativeai as genai

roles = {
    "Educador tradicional": "Você é um educador tradicional com anos de experiência em universidades \
    convencionais. Analise a École 42 de uma perspectiva acadêmica.",
    "Estudante de tecnologia": "Você é um estudante de tecnologia ansioso para aprender programação. \
    Analise a École 42 do ponto de vista de um potencial aluno.",
    "Recrutador de tecnologia": "Você é um recrutador de profissionais de uma grande empresa de tecnologia \
    . Avalie a École 42 considerando as habilidades que você busca em candidatos."
}

grop_responses = {}

gemini_responses = {}

user_prompt = "Descreva a École 42 e seu método de ensino. Destaque os pontos principais que seriam relevantes para sua perspectiva."

def grop_request(role, system_prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'{system_prompt}',
            },
            {
                "role": "user",
                "content": f'{create_user_prompt()}',
            }
        ],
        model="llama3-8b-8192",
    )
    grop_responses[role] = chat_completion.choices[0].message.content

def gemini_request(role, system_prompt):
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_prompt)
    response = model.generate_content(create_user_prompt())
    gemini_responses[role] = response.text

def create_user_prompt():
    context = 'precisamos de um resumo muito curto porem contundente do que é a escola'
    response_format = 'retorne os pontos principais separados por virgulas'
    result = '<prompt>' + \
            '<context>' + context + '</context>' + \
            '<instruction>' + user_prompt + \
            '<response_format>' + response_format + '<response_format>' + \
            '</instruction>' + \
            '</prompt>'
    return result


if __name__ == "__main__":
    for role, system_prompt in roles.items():
        gemini_request(role, system_prompt)
        grop_request(role, system_prompt)

    print(f'=== Análises usando GEMINI ===')
    for role, response in gemini_responses.items():
        print(f'--- Análise da perspectiva de {role} ---')
        print(response, end='\n')

    print(f'=== Análises usando LLAMA ===')
    for role, response in grop_responses.items():
        print(f'--- Análise da perspectiva de {role} ---')
        print(response, end='\n\n')