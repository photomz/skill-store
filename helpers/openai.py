import openai
from strenum import StrEnum


class Model(StrEnum):
    """OpenAI available models."""

    GPT_4_32K = "gpt-4-32k"
    GPT_4 = "gpt-4"
    DAVINCI = "text-davinci-003"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    EMBEDDING_ADA_2 = "text-embedding-ada-002"
