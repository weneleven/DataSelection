from transformers import LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained("/home/ck/llm/model/Llama-2-7b-hf")
max_length = model.config.max_position_embeddings
print("最大输入长度:", max_length)
#最大输入长度: 4096