"""
openai_answerer.py - Module for answering questions using OpenAI GPT-3.5 Turbo.

This module contains the OpenAIQuestionAnswerer class, which is responsible for
interacting with OpenAI GPT-3.5 Turbo to generate answers to user questions.
"""

from openai import OpenAI


class OpenAIQuestionAnswerer:
    """
    OpenAIQuestionAnswerer - Interacts with OpenAI GPT-3.5 Turbo to answer user questions.

    Attributes:
        client (OpenAI): OpenAI API client.

    Methods:
        __init__(self, api_key: str) -> None:
            Initializes the OpenAIQuestionAnswerer with the OpenAI API key.

        ask_openai_individual(self, question: str, context: str) -> str:
            Uses OpenAI GPT-3.5 Turbo to answer the given question based on the provided context.
    """

    def __init__(self, api_key: str) -> None:
        """
        Initializes the OpenAIQuestionAnswerer with the OpenAI API key.

        Parameters:
            api_key (str): The OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    def ask_openai_individual(self, question: str, context: str) -> str:
        """
        Uses OpenAI GPT-3.5 Turbo to answer the given question based on the provided context.

        Parameters:
            question (str): The user's question.
            context (str): The context in which the question is asked.

        Returns:
            str: The generated answer.
        """
        response = self.client.completions.create(
            model="text-davinci-003",
            prompt=f"Context: {context}\nQuestion: {question}",
            # max number of tokens to generate, 300 by default (can be changed)
            max_tokens=300
        )
        # Remove leading and trailing whitespaces
        answer = response.choices[0].text.strip()
        # Remove the first occurrence of "Answer:" if present
        if answer.startswith("Answer:"):
            answer = answer.replace("Answer:", "", 1).strip()
        return answer
