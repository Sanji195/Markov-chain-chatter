import random

class MarkovChainChatbot:
    def __init__(self, corpus):
        self.corpus = corpus
        self.transitions = {}
        self.start_words = []
        self.end_words = []
        self.build_chain()

    def build_chain(self):
        for sentence in self.corpus:
            words = sentence.split()
            if len(words) > 1:
                self.start_words.append(words[0])
                self.end_words.append(words[-1])
                for i in range(len(words) - 1):
                    if words[i] not in self.transitions:
                        self.transitions[words[i]] = []
                    self.transitions[words[i]].append(words[i+1])

    def generate_response(self):
        current_word = random.choice(self.start_words)
        response = current_word
        while current_word not in self.end_words:
            if current_word in self.transitions:
                next_word = random.choice(self.transitions[current_word])
                response += " " + next_word
                current_word = next_word
            else:
                break
        return response

# Example corpus
corpus = [
    "I am good",
    "You are great person",
    "We are awesome G",
    "Goodbye...",
    "Wsg gang"
]

# Create a Markov Chain chatbot
chatbot = MarkovChainChatbot(corpus)

# Start chatting
print("Welcome to the Markov Chain Chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        bot_response = chatbot.generate_response()
        print("Chatbot:", bot_response)
