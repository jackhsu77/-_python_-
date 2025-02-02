from sentence_transformers import SentenceTransformer, util

# 加載預訓練的 Sentence-BERT 模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 句子列表
sentences = [
    "很高興為你服務",
    "很樂意在此服務",
    "請問有何需要服務的地方",
    "我想要退貨"
]

# 將句子轉換為嵌入向量
embeddings = model.encode(sentences, convert_to_tensor=True)

# 計算句子之間的相似度
similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings)

# 顯示相似度矩陣
print(similarity_matrix)

# 逐對打印相似度
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        print(f"'{sentences[i]}' 和 '{sentences[j]}' 的相似度: {similarity_matrix[i][j].item():.4f}")