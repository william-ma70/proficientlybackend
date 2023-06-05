import openai
import gradio as gr

openai.api_key = 0

# List of interview questions
# interview_questions = [
#     "Ask me this question: Tell me about yourself.",
#     "Ask me this question: What are your strengths?",
#     "Ask me this question: What are your weaknesses?",
#     "Ask me this question: Why are you interested in this position?",
#     # Add more questions as needed
# ]

# Initialize the interview question index
question_index = 0

industry = "Consulting"
firm = "McKinsey"
name = "William"

messages = [
    {"role": "system", "content": "Your name is John "+firm+" and you are an interviewer for a company in \
    the "+industry+ " industry, specifically "+firm+". Treat all of the \
    user's prompts as though the user is an interviewee."},
    {'role':'user', 'content':'Hi, my name is '+name}
]

conversation_logs = []


def chatbot(input, model="gpt-3.5-turbo", temperature=0):
    global question_index

    # If input is provided, assume it's the user's response to the question
    if input:
        messages.append({"role": "user", "content": input})

    # # If all questions have been asked, use the input as a regular chat message
    # if question_index >= len(interview_questions):
    #     messages.append({"role": "user", "content": input})
    # else:
    #     # Ask the next interview question
    #     messages.append({"role": "assistant", "content": interview_questions[question_index]})
    #     question_index += 1

    chat = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    # Add current prompt-response pair to conversation logs
    conversation_logs.append({"prompt": messages[-2]["content"], "response": reply})

    return reply

# print(chatbot("Hi"))

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)

print(conversation_logs)