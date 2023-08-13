import openai
from typing import List
import os

from translator.constants import _LANGUAGE_CODE

# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

_MODEL_NAMES = ['gpt-4', 'gpt-4-0613', 'gpt-4-32k', 'gpt-4-32k-0613', 
                'gpt-3.5-turbo', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k', 
                'gpt-3.5-turbo-16k-0613']
_DEFAULT_MODEL_NAME = 'gpt-3.5-turbo'

_PROMPT_TRANSLATION = "I want you to act as an {0} translator, spelling \
    corrector and improver. I will speak to you in any language and you will \
    detect the language, translate it and answer in the corrected and improved \
    version of my text, in {0}. I want you to replace my simplified A0-level \
    words and sentences with more beautiful and elegant, upper level {0} \
    words and sentences. Keep the meaning same, but make them more literary. \
    I want you to only reply the correction, the improvements and nothing else, \
    do not write explanations."

# Function to translate a single text
def translate_text(text, dest_language):

    if dest_language in _LANGUAGE_CODE:
        dest_language = _LANGUAGE_CODE[dest_language]

    response = openai.ChatCompletion.create(
        model=_DEFAULT_MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": _PROMPT_TRANSLATION.format(dest_language)
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    translation = response['choices'][0]['message']['content']
    return translation

# Function to translate a list of texts
def translate_text_list(text_list, dest_language):
    translations = []
    for text in text_list:
        translation = translate_text(text, dest_language)
        translations.append(translation)
    return translations


if __name__ == '__main__':
    input_dict = {
        "text": ["Hello", "I am Peter"],
        "dest_language": "fr"
    }

    input_text = input_dict["text"]
    dest_language = input_dict["dest_language"]

    if isinstance(input_text, List):
        translated_text = translate_text_list(input_text, dest_language)
    else:
        translated_text = translate_text(input_text, dest_language)

    print(translated_text)

# def sumOfOddNumbers(a,b):
#     a += 1 if a % 2 == 0 else 2
#     b -= 1 if b % 2 == 0 else 2

#     if b < a:
#         return 0
#     elif b == a:
#         return a

#     n_nums = (b - a) / 2 + 1 # Number odd numbers between a and b (including a and b)
        
#     return (n_nums * (b+a) / 2) % 10000007
