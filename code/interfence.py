import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 加载模型和分词器
model_path = "/home/ck/LLaMA-Factory/fmodels/llama2-dolly-1"  # 替换为你的模型目录路径
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)


# 输入文本
input_text = "Hello, how are you??"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# 使用模型生成文本
with torch.no_grad():
    output_ids = model.generate(input_ids, max_length=50)

print(output_ids.size()) 

# 解码生成的 token ids 为文本
generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("responce:\n")
print(generated_text)
