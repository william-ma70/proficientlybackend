import real_time_transcription
import chatbot

def main():
    print(chatbot("Hi"))
    start_listening()
    if json.loads(result_str)['message_type'] == 'FinalTranscript':
        stop_listening()
        chatbot(json.loads(result_str)['text'])


cont = True

def start_listening():
    global cont 
    cont = True

def stop_listening():
    global cont 
    cont = False