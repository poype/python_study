# 通过大语言模型来进行情感分析，最简单的方式就是利用它提供的 Embedding 这个 API
# 这个 API 可以把任何一段文本，变成一个大语言模型下的向量，向量就是用一组固定长度的参数来代表任意一段文本

# 提前计算“好评”和“差评”这两个字的 Embedding
# 然后对于任何一段文本评论，我们也都可以通过 API 拿到它的 Embedding，再把这段文本的 Embedding 和“好评”以及“差评”通过余弦距离（Cosine Similarity）计算出它的相似度。


from openai import OpenAI
import numpy as np

client = OpenAI(api_key="sk-11082a2c155b45e188b61c9bc6b02a7a", base_url="https://api.deepseek.com/v1 ")

EMBEDDING_MODEL = "deepseek-embed"

def get_embedding(text, model=EMBEDDING_MODEL):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    epsilon = 1e-10
    cosine_similarity = dot_product / (norm_a * norm_b + epsilon)
    return cosine_similarity

positive_review = get_embedding("好评")
negative_review = get_embedding("差评")

positive_example = get_embedding("买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质")
negative_example = get_embedding("随意降价，不予价保，服务态度差")

def get_score(sample_embedding):
    return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)

positive_score = get_score(positive_example)
negative_score = get_score(negative_example)

print("好评例子的评分 : %f" % (positive_score))
print("差评例子的评分 : %f" % (negative_score))
