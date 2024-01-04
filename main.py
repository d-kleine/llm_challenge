import urllib.request
import xml.etree.ElementTree as ET
from openai import OpenAI
import os
from dotenv import load_dotenv
import time


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


def ask_openai(question, context):
    """Uses OpenAI GPT-3.5 Turbo to answer the given question based on the provided context."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"},
        ],
    )
    return response.choices[0].message.content


def main():
    papers = fetch_papers()

    for paper in papers:
        title = paper.split('\n')[0].replace('Title: ', '')
        context = paper.replace('Title: ', f"{title}\n")

        # Example questions
        questions = [
            "For which tasks has Llama-2 already been used successfully?",
            "What are promising areas of application for Llama-2?",
            "Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2.",
            "What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?"
        ]

        for question in questions:
            answer = ask_openai(question, context)
            print(f"Question: {question}\nAnswer: {answer}\n")


if __name__ == "__main__":
    main()
