import openai
from dotenv import load_dotenv, find_dotenv
from logger import initialize_logger

logger = initialize_logger(__name__)
_ = load_dotenv(find_dotenv())  # read local .env file


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    """
    Get the completion from the openai api

    Args:
        prompt (str):
            prompt to send to the api
        model (str, optional):
            openai model . Defaults to "gpt-3.5-turbo".
        temperature (int, optional):
            degree of randomness of the model's output. Defaults to 0.

    Returns:
        str: completion from the openai api
    """
    logger.debug(f"prompt: {prompt}")
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    logger.debug(f"response: {response}")
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    logger.debug(f"prompt: {messages}")
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    logger.debug(f"response: {response}")
    return response.choices[0].message["content"]
