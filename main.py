import json
global chatbotname
chatbotname = ("Chatbot: ")

with open('knowledge.json') as f:
   data = json.load(f)

while True:
  chat = input("You: ")
  if chat in data:
    print(chatbotname + data[chat])
  else:
    new_answer = input(chatbotname + "I dont know how to respond to that. How should I? ")
    data[chat] = new_answer
    with open('knowledge.json', 'w') as f:
      json.dump(data, f)