# LLM assessment for ArXiv chatbot

## Task
The current initiative aims to simplify and enhance knowledge building within the team. Exploration is underway to potentially replace OpenAI's GPT APIs with Meta's Llama-2 technology in various projects, driven by the consideration of achieving privacy-compliant implementation on company servers.

The objective is to rapidly comprehend the diverse applications of Llama-2 by developing a Question-Answering System based on scientific publications from Arxiv.org. This approach seeks to provide thorough insights into Llama-2's functionality and use cases, facilitating informed decision-making regarding its integration into projects.

## Demands:
* Use Git for documenting the development process
* Choose between an open-source model or GPT 3.5-Turbo
* Evaluate functionality using sample questions, including inquiries about Llama-2's successful applications, promising areas of use, domain-specific LLMs created by fine-tuning, and details about the model structure.
* All queries should be limited to a single connection

## Requirements

**Step 1: Setup Python**

Ensure Python 3.11.5 is installed on your system. If not, download and install it from the official Python website.

**Step 2: Setup a Virtual Environment**

Create Virtual Environment:

```bash
python -m venv openai-env
```
Activate on Windows:

```bash
openai-env\Scripts\activate
```

Activate on Unix/MacOS:
```bash
source openai-env/bin/activate
```

**Step 3: Install Dependencies**

Install the dependencies from the *requirements.txt* file:
```bash
pip install -r requirements.txt
```

For further information, please visit [Get up and running with the OpenAI API](https://platform.openai.com/docs/quickstart?context=python)

**Step 4: Set up OpenAI API key**

You can either add the 

To set up an API key for a single project, create a local *.env* file in the project folder and add the key as OPENAI_API_KEY. Also, create a *.gitignore* file in the project root to ensure the *.env file* is not included in version control. After creating the files, copy the secret API key into the .env file.

The *.env* file should look like the following:

```OPENAI_API_KEY=sk-...```

For further information, please visit [Get up and running with the OpenAI API](https://platform.openai.com/docs/quickstart?context=python)
 
**Step 5: Run the app**

Run `main.py` to fetch relevant papers from the arXiv API, combine information from the top 5 most semantically similar papers to predefined questions, and generate answers using OpenAI GPT-3.5 Turbo:

```bash
python main.py
```

The script employs the `ArxivPaperFetcher` class to retrieve papers, extract information, and calculate semantic similarities (based on cosine similarity), while the `OpenAIQuestionAnswerer` class interacts with the OpenAI API to provide comprehensive answers. Customize the predefined questions to suit your needs, and the script outputs individual question-answer pairs along with a complete response summary.

Sample output for example questions:
```
Question: For which tasks has Llama-2 already been used successfully?
Answer: Llama 2 has been successfully used for a wide range of tasks, including dialogue tasks, language modeling, instruction following, writing assistance, financial news analytics and table to text generation.

Question: What are promising areas of application for Llama-2?
Answer: Promising areas of application for Llama-2 include dialogue, legal domain knowledge, writing assistance, and table to text generation. In dialogue, the model has already shown strong performance on various benchmark datasets. It can also be used for legal domain knowledge, enabling LLMs to answer legal domain queries and leverage domain-specific knowledge. In writing assistance, fine-tuning Llama 2 on writing instruction data has been shown to significantly improve its ability on writing tasks. Additionally, Llama 2 can be used for table to text generation, incorporating reasoning information into the input by highlighting relevant table-specific row data.

Question: Name at least 5 domain-specific LLMs that have been created by fine-tuning Llama-2.
Answer: 1. Lawyer LLaMa: A legal domain LLM for resolving domain-related problems.
2. Writing Assistant LLM: A model built for writing assistance tasks.
3. Financial News LLM: A model fine-tuned for analyzing financial news.
4. Clinical LLaMa-LoRA: A PEFT adapter layer trained using clinical notes.
5. Downstream LLaMa-LoRA: A PEFT adapter layer specialised for downstream tasks.

Question: What can you find out about the model structure of Llama-2 (required memory, required computing capacity, number of parameters, available quantizations)?
Answer: Llama-2 models range from 7 billion to 70 billion parameters. The 7 billion parameter model requires 2.5TB of memory and 4 to 5 cloud TPUv3 cores for best performance. The 70 billion parameter model requires a 24TB of memory and 128 TPUv3 cores for best performance. Llama-2 models can be quantized into 8 or 16-bit versions depending on the type of compression required.
```
