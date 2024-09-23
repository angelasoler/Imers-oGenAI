#!/usr/bin/env python3

import json
import re

import google.generativeai as genai

movie_titles = ["The Matrix", "Inception", "Pulp Fiction", "The Shawshank Redemption", "The Godfather"]

def gemini_request(formatted_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(formatted_prompt)

    return parse_llm_response(response.text)

def parse_llm_response(response):
    match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
    json_content = match.group(1)
    response_dict = json.loads(json_content)
    return response_dict

def create_prompt(movie_title):
    task = f'Provide information about the movie "{movie_title}".'
    response_format = 'JSON format: \
        {title: Movie Title, year: 0000,director: Directors Name, \
            genre: [Genre1, Genre2....],plot_summary: Brief plot summary}'
    result = '<prompt>' + \
            '<instruction>' + task + \
            '<response_format>' + response_format + '<response_format>' + \
            '</instruction>' + \
            '</prompt>'

    return result

def get_movie_info(title):
    formatted_prompt = create_prompt(title)
    return gemini_request(formatted_prompt)

for title in movie_titles:
    print(f"\nAnalyzing: {title}")
    result = get_movie_info(title)
    if result:
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print('Error: Failed to generate valid JSON')
    print("-" * 50)


