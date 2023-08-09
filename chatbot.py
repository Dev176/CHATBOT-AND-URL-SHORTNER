import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot. I'm here to help.",]
    ],
    [
        r"who created you ?",
        ["I was created by Devesh.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thank you!",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with various topics. Just let me know what you need.",]
    ],
    [
        r"(.*) your favorite (food|movie|song) ?",
        ["I don't have preferences as I am just a bot!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"what time is it ?",
        ["Sorry, I'm not equipped to tell time.",]
    ],
    [
        r"how is the weather ?",
        ["I'm not connected to weather data, but you can check online for accurate weather information.",]
    ],
    [
        r"tell me about badminton",
        ["Badminton is a racket sport that is played by two or four players. The players use rackets to hit a shuttlecock back and forth over a net.",]
    ],
    [
        r"who is your favorite badminton player ?",
        ["I don't have personal preferences, but some famous badminton players are Lin Dan, Lee Chong Wei, and PV Sindhu.",]
    ],
    [
        r"(.*) bye (.*)",
        ["Goodbye! Have a great day.", "See you later!",]
    ],
]

chatbot = Chat(pairs, reflections)

print("Hello! I'm ChatBot. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
