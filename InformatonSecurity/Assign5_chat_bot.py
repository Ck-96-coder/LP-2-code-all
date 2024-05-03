import streamlit as st
import random
from datetime import datetime

# Define responses
responses = {
    "greeting": {
        "morning": ["Good morning! Welcome to our restaurant.", "Good morning! How can I assist you today?"],
        "afternoon": ["Good afternoon! Welcome to our restaurant.", "Good afternoon! How can I assist you today?"],
        "evening": ["Good evening! Welcome to our restaurant.", "Good evening! How can I assist you today?"],
    },
    "menu": {
        "pizza": "Our pizza is priced at ₹700.",
        "pasta": "Our pasta is priced at ₹800.",
        "burgers": "Our burgers are priced at ₹500.",
        "salads": "Our salads are priced at ₹400.",
        "seafood": "Our seafood dish is priced at ₹1000.",
        "steaks": "Our steaks are priced at ₹1500.",
        "vegetarian": "Our vegetarian dish is priced at ₹600.",
    },
    "hours": ["We are open from 11:00 AM to 10:00 PM every day.", "Our restaurant hours are from 11:00 AM to 10:00 PM, seven days a week."],
    "location": ["We are located at 123 Main Street, City, State.", "Our restaurant is situated at the corner of First Avenue and Elm Street."],
    "thanks": ["You're welcome! Enjoy your meal.", "No problem! Let me know if you need anything else."],
    "goodbye": ["Goodbye! Have a great day.", "Thanks for visiting us! Come back soon."],
}

# Streamlit UI
def main():
    st.title("Restaurant Chatbot")
    st.write("Welcome to our restaurant! How can I assist you today?")
    
    # Initialize chat history
    chat_history = st.session_state.setdefault("chat_history", [])

    chat_container = st.empty()

    user_input = st.text_input("You: ")

    if st.button("Send"):
        if user_input:
            user_message = f"You: {user_input}"
            bot_response = f"Bot: {get_bot_response(user_input)}"
            chat_history.append(user_message)
            chat_history.append(bot_response)
            display_chat_history(chat_container, chat_history)

# Function to generate bot response
def get_bot_response(user_input):
    user_input = user_input.lower()

    # Get the current time
    current_time = datetime.now().time()

    # Determine the time of day
    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        time_of_day = "morning"
    elif current_time < datetime.strptime("18:00:00", "%H:%M:%S").time():
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"][time_of_day])
    elif "menu" in user_input or "food" in user_input:
        return "Our menu items include pizza, pasta, burgers, salads, seafood, steaks, and vegetarian dishes."
    elif "price" in user_input:
        return "Please specify the item you want to know the price for."
    elif "hours" in user_input or "open" in user_input:
        return random.choice(responses["hours"])
    elif "location" in user_input or "address" in user_input:
        return random.choice(responses["location"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    elif "bye" in user_input:
        return random.choice(responses["goodbye"])
    elif any(item in user_input for item in responses["menu"].keys()):
        for item in responses["menu"].keys():
            if item in user_input:
                return responses["menu"][item]
    else:
        return "I'm sorry, I didn't understand that. How can I assist you?"

# Function to display chat history
def display_chat_history(container, chat_history):
    container.markdown("<br>".join(chat_history), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
