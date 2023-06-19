import hosbot

# Function to greet the user
def greet():
    responses = ["Hello! Welcome to the hospital chatbot.", "Hi there! How can I assist you today?"]
    return hosbot.choice(responses)

# Function to provide information about hospital services
def provide_services_info():
    services = ["We offer a wide range of medical services including general check-ups, surgeries, and specialized treatments.", 
                "Our hospital provides emergency care, laboratory services, and diagnostic imaging.", 
                "We have a team of experienced doctors and nurses to cater to your medical needs."]
    return hosbot.choice(services)

# Function to schedule an appointment
def schedule_appointment():
    return "To schedule an appointment, please call our reception at 123-456-7890 during office hours."

# Function to handle user queries
def handle_query(user_input):
    if "greet" in user_input:
        return greet()
    elif "services" in user_input:
        return provide_services_info()
    elif "appointment" in user_input:
        return schedule_appointment()
    else:
        return "I'm sorry, I couldn't understand your query. How can I assist you?"

# Main function to run the chatbot
def run_chatbot():
    print("Hospital Chatbot")
    print("Type 'exit' to end the conversation.")
    print("-----------------------------")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for using our hospital chatbot. Take care!")
            break
        response = handle_query(user_input)
        print("Chatbot:", response)
        print("-----------------------------")

# Run the chatbot
run_chatbot()
