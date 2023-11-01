import json
import random
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")

def load_intents(file_path: str) -> dict:
    with open(file_path, "r") as file:
        intents = json.loads(file.read())
    return intents

def tokenize_and_stem(text: str) -> list:
    tokens = word_tokenize(text)
    stems = [stemmer.stem(token) for token in tokens]
    return stems

def find_best_match(user_input: str, intents: list[dict]) -> str | None:
    user_tokens = tokenize_and_stem(user_input.lower())
    
    if any(keyword in user_tokens for keyword in ["payment", "pay", "credit", "card"]):
        return "payment"
    
    if any(keyword in user_tokens for keyword in ["greeting", "hello", "hi", "hey"]):
        return "greeting"
    
    if any(keyword in user_tokens for keyword in ["farewell", "goodbye", "bye"]):
        return "goodbye"
    
    if any(keyword in user_tokens for keyword in ["thanks", "thank", "appreciate"]):
        return "thanks"
    
    if any(keyword in user_tokens for keyword in ["menu", "food", "order"]):
        return "menu"
    
    if any(keyword in user_tokens for keyword in ["reservation", "book", "table"]):
        return "reservation"

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = tokenize_and_stem(pattern.lower())
            if any(token in user_tokens for token in pattern_tokens):
                return intent["tag"]
    return None

def get_answer_for_intent(intent_tag: str, intents: dict) -> str | None:
    for intent in intents["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])
    return None

def chat_bot():
    intents = load_intents("intents_base.json")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        best_match = find_best_match(user_input, intents)

        if best_match:
            answer = get_answer_for_intent(best_match, intents)
            print(f"Bot: {answer}") if answer else print("Bot: Sorry, I don't have an answer for that.")
        else:
            print("Bot: Sorry, I don't have an answer for that.")

if __name__ == "__main__":
    chat_bot()
