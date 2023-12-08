#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main.py

Extremely tiny experiment to integrate OpenAI ChatGPT 3.5 in python program.
"""

from openai import OpenAI, completions

client: OpenAI = OpenAI(api_key="YOUR_API_KEY")

completion: completions = client.completions.create(
    max_tokens = 1024,
    n = 1,
    stop = None,
    model = "gpt-3.5-turbo",
    prompt = "Hello, how are you today?"
)

def main() -> None:
    """program entrypoint and logic."""
    response = completion.choices[0].text
    print(response)
    return None

if __name__ == "__main__":
    main()
