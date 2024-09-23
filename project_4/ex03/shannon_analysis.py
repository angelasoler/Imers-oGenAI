#!/usr/bin/env python3


import google.generativeai as genai

def gemini_request(task):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(create_user_prompt(task))
    return response.text

def create_user_prompt(task):
    result = '<prompt>' + \
            '<instruction>' + task + \
            '</instruction>' + \
            '</prompt>'
    return result

def create_prompt_from_promt(context, task):
    result = '<prompt>' + \
            '<context>' + context + '</context>' + \
            '<instruction>' + task + \
            '</instruction>' + \
            '</prompt>'
    return result

def sintetize_info():
    task = 'Sintetize as informações das respostas anteriores em uma análise abrangente'
    result = '<prompt>' + \
        '<instruction>' + task + \
        '</instruction>' + \
        '</prompt>'
    return result

def gemini_request_chat(tasks):
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    chat.send_message(tasks[0])
    chat.send_message(tasks[1])
    response = chat.send_message(sintetize_info())

    return response.text

def run_prompt_chain():
    task = 'retorne uma visão geral da vida e carreira de Claude Shannon.'
    prompt1 = gemini_request(task)
    tasks = []
    tasks.append(create_prompt_from_promt(prompt1, 'Analisar suas principais contribuições para a teoria da informação.'))
    tasks.append(create_prompt_from_promt(prompt1, 'Explorar o impacto de seu trabalho na computação moderna e nas tecnologias de comunicação.'))
    result = gemini_request_chat(tasks)
    print(result)

if __name__ == "__main__":
    run_prompt_chain()
