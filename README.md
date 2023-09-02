# FAQ Guru - LLM Project
a small project (3-4) hours coding with a dear friend, we want to use Cohere and Langchain to build an app using LLM

## Usage
It is recommended to run the project on GitHub Codespaces.

1- Make sure to add your FAQ in a csv file. It should have columns QuestionId, Question, Answer. For the demo purpose we used [Mental Health FAQ for Chatbot
](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot) from Kaggle.

2- Run `pip install -r requirements.txt`

3- Run `python generate_embeddings.py` to generate embeddings for all questions and save to the questions_index.faiss

4- Run `python app.py` and enter your question, then you will get the answer of the most similar question from your FAQ list.

## Useful links
- https://python.langchain.com/docs/integrations/text_embedding/cohere
- https://cohere.com/
- https://faiss.ai/
