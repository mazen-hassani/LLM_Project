import cohapi

coh_api = cohapi.API(api_key='your_api_key')

def process_user_input(user_input):
    response = coh_api.analyze(user_input)
    intent = response['intent']
    entities = response['entities']
    return intent, entities

user_query = input("Ask a blockchain-related question: ")
intent, entities = process_user_input(user_query)

# Now you have the user's intent and entities for further processing.