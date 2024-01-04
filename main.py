"""
main.py - Main script for querying arXiv papers and generating answers using OpenAI GPT-3.5 Turbo.

This script fetches relevant papers from arXiv, combines information from the top k most relevant papers,
and then asks OpenAI GPT-3.5 Turbo questions based on the combined information.
"""

import os
from dotenv import load_dotenv
from arxiv_fetcher import ArxivPaperFetcher
from openai_answerer import OpenAIQuestionAnswerer


def main():
    """
    Main function to orchestrate the process of fetching papers, combining information,
    and generating answers to a set of predefined questions.
    """
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    arxiv_fetcher = ArxivPaperFetcher(api_key)
    openai_answerer = OpenAIQuestionAnswerer(api_key)

    papers = arxiv_fetcher.fetch_papers()

    questions = [
        "For which tasks has Llama-2 already been used successfully?",
        "What are promising areas of application for Llama-2?",
        "Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2.",
        "What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"
    ]

    individual_answers = []

    for question in questions:
        top_k_papers = arxiv_fetcher.find_most_similar_papers(
            question, papers, k=5)

        # Combine information from the top k papers
        combined_info = '\n'.join([paper for paper, _ in top_k_papers])

        # Ask OpenAI using the combined information
        answer = openai_answerer.ask_openai_individual(question, combined_info)
        individual_answers.append((question, answer))

        # print(f"Combined Information from Top {len(top_k_papers)} Papers:")
        # for paper, similarity in top_k_papers:
        #     print(f"  - {paper} (Similarity Score: {similarity})")
        print(f"Question: {question}")
        print(f"Answer: {answer}\n")


if __name__ == "__main__":
    main()
