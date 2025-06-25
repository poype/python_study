from openai import OpenAI

client = OpenAI(api_key="sk-11082a2c155b45e188b61c9bc6b02a7a", base_url="https://api.deepseek.com")

class Conversation:
    def __init__(self, prompt, num_of_round):
        self.prompt = prompt
        self.num_of_round = num_of_round
        self.messages = []
        self.messages.append({"role": "system", "content": self.prompt})

    def ask(self, question):
        try:
            self.messages.append({"role": "user", "content": question})
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=self.messages,
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
                stream=False
            )
        except Exception as e:
            print(e)
            return e

        message = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": message})

        if len(self.messages) > self.num_of_round*2 + 1:
            del self.messages[1:3]  # Remove the first round conversation left.
        return message



system_prompt = """
你是一个中国厨师，用中文回答做菜的问题。你的回答需要满足以下要求:
1. 你的回答必须是中文
2. 回答限制在100个字以内
"""
conv1 = Conversation(system_prompt, 2)
question1 = "你是谁？"
print("User : %s" % question1)
print("Assistant : %s\n" % conv1.ask(question1))

question2 = "请问鱼香肉丝怎么做？"
print("User : %s" % question2)
print("Assistant : %s\n" % conv1.ask(question2))

question3 = "那蚝油牛肉呢？"
print("User : %s" % question3)
print("Assistant : %s\n" % conv1.ask(question3))


# 需要传入的参数，从一段 Prompt 变成了一个数组，数组的每个元素都有 role 和 content 两个字段。
# role 这个字段一共有三个角色可以选择，其中 system 代表系统，user 代表用户，而 assistant 则代表 AI 的回答。
# 当 role 是 system 的时候，content 里面的内容代表我们给 AI 的一个指令，也就是告诉 AI 应该怎么回答用户的问题。
# 比如我们希望 AI 都通过中文回答，我们就可以在 content 里面写“你是一个只会用中文回答问题的助理”，这样即使用户问的问题都是英文的，AI 的回复也都会是中文的。
# 而当 role 是 user 或者 assistant 的时候，content 里面的内容就代表用户和 AI 对话的内容。
# 你需要把历史上的对话一起发送给 OpenAI 的接口，它才能有理解整个对话的上下文的能力。

# 相比于之前实现的聊天机器人，ChatCompletion接口不但用起来更容易，速度还快，而且价格也更便宜，可谓是物美价廉了。