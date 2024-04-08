from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = respond(user_message)
    return jsonify({'bot_response': bot_response})

def respond(user_message):
    user_message = user_message.lower()
    if 'hello' in user_message or 'hi' in user_message:
        return "Hi there! How can I assist you today?"
    elif 'help' in user_message:
        return "Of course! I'm here to assist you. What do you need help with regarding your appointment?"
    elif 'available' in user_message:
        return "To check availability, please provide the type of appointment and your preferred date/time. I'll see what I can do."
    elif 'insurance' in user_message:
        return "We accept most major insurance plans. Could you please provide your insurance details so I can verify coverage for you?"
    elif 'location' in user_message:
        return "Our clinic is located at [insert address]. If you need directions or assistance finding us, let me know."
    elif 'prescription' in user_message:
        return "For prescription refills or new prescriptions, please provide your medication details and I'll assist you accordingly."
    elif 'doctor' in user_message:
        return "If you have a preferred doctor, please let me know and I'll check their availability for you."
    elif 'procedure' in user_message:
        return "If you're unsure about a procedure or need more information, feel free to ask. I'm here to help clarify any concerns."
    elif 'follow-up' in user_message:
        return "To schedule a follow-up appointment, please provide your previous appointment details and the reason for follow-up."
    elif 'appointment' in user_message:
        if 'book' in user_message:
            return "Sure! I can help you with that. Could you please provide your name and preferred date for the appointment?"
        elif 'cancel' in user_message:
            return "I'm sorry to hear that you need to cancel your appointment. Please provide your appointment details so I can assist you further."
        elif 'reschedule' in user_message:
            return "Sure, I can assist you with rescheduling your appointment. Please provide your appointment details and your preferred new date."
        else:
            return "Would you like to book, cancel, or reschedule an appointment?"
    elif 'urgent' in user_message:
        return "If your condition is urgent, please call emergency services immediately."
    elif 'thank you' in user_message:
        return "You're welcome! If you need any further assistance, feel free to ask."
    else:
        return "How may I assist you?"

if __name__ == '__main__':
    app.run(debug=True)
