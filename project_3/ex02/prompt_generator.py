#!/usr/bin/env python3.10

import google.generativeai as genai

def create_prompt(role, task, topic, specific_question):
    result = '<prompt>' + \
            '<role>' + role + '</role>' + \
            '<instruction>' + task + '</instruction>' + \
            '<context>' + topic + '</context>' + \
            '<user_input>' + specific_question + '</user_input>' + \
            '</prompt>'

    return result


def send_to_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text

def main():
    role = "assistente especializado em ensinar programação Python para iniciantes"
    task = "explicar conceitos básicos de Python e fornecer exemplos simples e práticos"
    topic = "list comprehensions em Python"
    specific_question = "O que é uma list comprehension e como posso usá-la para criar uma lista de números pares de 0 a 10?"
    prompt = create_prompt(role, task, topic, specific_question)
    response = send_to_gemini(prompt)
    print("\nResposta do Gemini 1.5 Flash:")
    print(response)

if __name__ == '__main__':
    main()