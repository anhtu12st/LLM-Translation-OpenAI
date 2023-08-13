# Translation App

## Overview

This is a translation application that leverages OpenAI's GPT models to provide language translation services. The application translates text from one language to another using the OpenAI API and offers both single text and batch translation capabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Available Models](#available-models)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up and run the translation application, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/translation-app.git`
2. Install the required packages: `pip install openai` (you might need to install other packages as well)
3. Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY=your-api-key
    ```
4. Navigate to the project directory: `cd translation-app`

## Usage

The translation application provides two main functions: `translate_text(text, dest_language)` and `translate_text_list(text_list, dest_language)`.

- `translate_text(text, dest_language)`: Translates a single text to the specified destination language.
- `translate_text_list(text_list, dest_language)`: Translates a list of texts to the specified destination language.

## Configuration

You can configure the application by adjusting the following parameters in the code:

- `_DEFAULT_MODEL_NAME`: The default GPT model to use for translation.
- `_PROMPT_TRANSLATION`: The prompt used to instruct the model for translation.

## Available Models

The application supports various GPT models, including:
- gpt-4
- gpt-4-0613
- gpt-4-32k
- ...

You can choose the model by updating the `_DEFAULT_MODEL_NAME` parameter.

## Example

```python
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
