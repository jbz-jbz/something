from nltk.chat.util import Chat, reflections

pairs = [
    ['hi',['hi how are you', 'Hi, how can i help you?', 'Do you need my assistance']],
    ['what is a chatbot',['A chatbot is a program designed to simulate conversation with human users. How can I assist you further?']]
]

chatbot = Chat(pairs,reflections)

print('Hi, I am chatbot. How can I help you?')
while True:
    user_input = input("YOU: ")
    response = chatbot.respond(user_input.lower())
    print(f"CHATBOT: {response}")
    if(user_input.lower()=='exit'):
        break
