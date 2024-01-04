import urllib.request
import xml.etree.ElementTree as ET
from openai import OpenAI
import os
from dotenv import load_dotenv
import time
from scipy.spatial.distance import cosine


load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def fetch_papers():
    """Fetches papers from the arXiv API and returns them as a list of strings."""
    url = 'http://export.arxiv.org/api/query?search_query=ti:llama&start=0&max_results=70'
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    root = ET.fromstring(data)

    papers_list = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
        paper_info = f"Title: {title}\nSummary: {summary}\n"
        papers_list.append(paper_info)

    # Delay of at least 3 seconds before making the next request
    time.sleep(3)

    return papers_list


def get_embedding(text):
    """Gets the OpenAI embedding for the given text using text-embedding-ada-002."""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding


def calculate_semantic_similarity(embedding1, embedding2):
    """Calculates the cosine similarity between two embeddings."""
    similarity = 1 - cosine(embedding1, embedding2)
    return similarity


def find_most_similar_paper(user_query, papers):
    """Finds the most semantically similar paper to the user's query."""
    user_query_embedding = get_embedding(
        user_query.lower())  # Lowercasing for consistency
    max_similarity = -1
    most_similar_paper = None

    for paper in papers:
        paper_embedding = get_embedding(paper.lower())
        similarity = calculate_semantic_similarity(
            user_query_embedding, paper_embedding)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_paper = paper

    return most_similar_paper


def ask_openai(question, context):
    """Uses OpenAI GPT-3.5 Turbo to answer the given question based on the provided context."""
    response = client.completions.create(
        model="text-davinci-003",  # You can use the desired model here
        prompt=f"Context: {context}\nQuestion: {question}",
        max_tokens=4097
    )
    return response.choices[0].text


def main():
    papers = fetch_papers()

    # Example questions
    questions = [
        "For which tasks has Llama-2 already been used successfully?",
        "What are promising areas of application for Llama-2?",
        "Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2.",
        "What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"
    ]

    for question in questions:
        # Find the most semantically similar paper to the user's query
        relevant_paper = find_most_similar_paper(question, papers)

        # Ask OpenAI using the relevant paper's context
        answer = ask_openai(question, relevant_paper)
        print(f"Question: {question}\nAnswer: {answer}\n")


if __name__ == "__main__":
    main()
