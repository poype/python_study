from openai import OpenAI

client = OpenAI(api_key="sk-11082a2c155b45e188b61c9bc6b02a7a", base_url="https://api.deepseek.com/beta")

COMPLETION_MODEL = "deepseek-chat"

prompt1 = """
Consideration product : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readable product title used on Amazon in english within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a price range for this product in U.S.

Output the result in json format with three properties called title, selling_points and price_range
"""

def get_response(prompt_text):
    completions = client.completions.create(
        model=COMPLETION_MODEL,
        prompt=prompt_text,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text
    return message

print(get_response(prompt1))

prompt2 = """
Man Utd must win trophies, says Ten Hag ahead of League Cup final

请将上面这句话的人名提取出来，并用json的方式展示出来
"""

print(get_response(prompt2))


# OpenAI 就只提供了 Complete 和 Embedding 两个接口:
# 1. Complete 可以让模型根据你的输入进行自动续写
# 2. Embedding 可以将你输入的文本转化成向量