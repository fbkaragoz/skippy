import openai

def gpt_response(prompt, context, gpt_api_key, max_tokens=150, temperature=0.7):
    """
    Get a response from GPT based on the given prompt and context.

    :param prompt: The prompt to send to GPT.
    :param context: Contextual dialogue history.
    :param gpt_api_key: Your OpenAI API key.
    :param max_tokens: The maximum number of tokens to generate.
    :param temperature: Controls randomness in the response.
    :return: The GPT-generated response as a string.
    """
    openai.api_key = gpt_api_key
    full_prompt = "\n".join(context + [prompt])

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage (use environment variables for API keys):
# import os
# gpt_api_key = os.getenv('GPT_API_KEY')
# gpt_response("hello", ["welcoming"], gpt_api_key)