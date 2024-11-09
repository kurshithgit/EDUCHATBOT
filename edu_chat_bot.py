# edu_chat_bot.py

class EduChatBot:
    def __init__(self):
        # Define a dictionary of simple Q&A responses
        self.responses = {
            "hello": "Hi there! How can I help you with your studies?",
            "what is python": "Python is a high-level, interpreted programming language known for its readability and versatility.",
            "who invented calculus": "Calculus was independently developed by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century.",
            "tell me about machine learning": "Machine learning is a field of AI focused on enabling systems to learn and improve from experience without explicit programming.",
            "how to integrate": "In calculus, integration is the process of finding the integral of a function, often used to find areas under curves.",
            # Add more responses as needed
        }

    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()
        for question, response in self.responses.items():
            if question in user_input:
                return response
        return "I'm sorry, I don't understand that question. Could you please rephrase?"

    def start_chat(self):
        print("Welcome to the Edu Chat Bot! Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Edu Chat Bot: Goodbye! Happy studying!")
                break
            print("Edu Chat Bot:", self.get_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    bot = EduChatBot()
    bot.start_chat()
