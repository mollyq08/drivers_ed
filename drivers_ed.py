import openai
from utils import read_str

api_key = read_str("./sec/openai.secret")
openai.api_key = api_key

def get_user_input():
    return input("You: ")

print("Hello, welcome to Molly's practice driving school!")
state = input("Please enter your state: ")
print("Okay, you live in " + state + "." + " meet your " + state + " permit test helper!")

prompt_text = [
    {"role": "system", "content": "You are a helpful assistant that provides driving permit test questions."},
    {"role": "user", "content": f"Act as a driving instructor in {state} giving a student driving permit test questions. Give them one at a time and deliver feedback on each wrong answer, praise on right answers."}
]

while True:
    user_response = get_user_input()
    prompt_text.append({"role": "user", "content": user_response})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt_text
    )

    assistant_reply = response['choices'][0]['message']['content']
    print("Assistant:", assistant_reply)
    
    prompt_text.append({"role": "assistant", "content": assistant_reply})
