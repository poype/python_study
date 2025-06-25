from openai import OpenAI

client = OpenAI(api_key="sk-11082a2c155b45e188b61c9bc6b02a7a", base_url="https://api.deepseek.com/beta")

def ask_llm(prompt):
    response = client.completions.create(
        model="deepseek-chat",
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

print("你好，我是一个聊天机器人，请你提出你的问题吧?")

questions = []
answers = []

def generate_prompt(prompt, questions, answers):
    num = len(answers)
    for i in range(num):
        prompt += "\n Q : " + questions[i]
        prompt += "\n A : " + answers[i]
    prompt += "\n Q : " + questions[num] + "\n A : "
    return prompt

while True:
    user_input = input("> ")
    questions.append(user_input)
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break

    prompt = generate_prompt("", questions, answers)

    answer = ask_llm(prompt)
    print(answer)
    answers.append(answer)