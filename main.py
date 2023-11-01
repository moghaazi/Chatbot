import json
import random

def load_intents(file_path: str) -> dict:
  with open(file_path, "r") as file:
    intents = json.loads(file.read())
    return intents

def find_best_match(user_input: str, intents: list[dict]) -> str | None:
  for intent in intents["intents"]:
    for pattern in intent["patterns"]:
      if user_input.lower() in pattern.lower():
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
