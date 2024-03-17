messages = ['Hello', 'Goodbye', 'Goodnight', 'Good morning', 
            'Good afternoon', 'Good evening', 'Good day', 'Good luck', 
            'Good job', 'Good news', 'Good grief', 'Good heavens']

sent_messages = []

def send_messages(message_list, sent_message_list):
    while message_list:
        current_message = message_list.pop()
        print(f"Sent: {current_message}.")
        sent_message_list.append(current_message)

def show_messages(message_list):
    for message in message_list:
        print(message)

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)