# FAQ Guru - LLM Project
a small project (3-4) hours coding with a dear friend, we want to use Cohere and Langchain to build an app using LLM

## Usage

### Using GitHub Codespaces:

1- Make sure to add your FAQ in a csv file. It should have columns QuestionId, Question, Answer. For the demo purpose we used [Mental Health FAQ for Chatbot
](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot) from Kaggle.

2- Run `pip install -r requirements.txt`

3- Run `python embeddings_generator.py` to generate embeddings for all questions and save to the questions_index.faiss

4- Run `python app.py` and enter your question, then you will get the answer of the most similar question from your FAQ list.

### Using Docker:
- To run the project, open terminal within the project directory and run `docker compose up`
- to stop it, Run `docker compose down` 

## Useful links
- https://python.langchain.com/docs/integrations/text_embedding/cohere
- https://cohere.com/
- https://faiss.ai/
