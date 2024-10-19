import json

# 原始 JSONL 文件路径
input_file_path = '/home/ck/LLaMA-Factory/data/databricks-dolly-15k.jsonl'
# 新的 JSONL 文件路径
output_file_path = '/home/ck/LLaMA-Factory/data/dolly_no_category.jsonl'

with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)  # 读取每一行并转换为字典
        if 'category' in data:
            del data['category']  # 删除 category 项
        outfile.write(json.dumps(data) + '\n')  # 将修改后的数据写入新文件
