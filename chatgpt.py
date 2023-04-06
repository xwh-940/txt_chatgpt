import openai
import os
import time
import numpy as np
from IPython.display import display, Markdown
# 填你的秘钥
openai.api_key = str(np.load("/home/ubuntu/key_know.npy"))

if not os.path.exists("gpt_txt"):
    os.makedirs("gpt_txt")
# 作为对话记录的文件名
run_time = str(time.strftime("%Y%m%d_%Hh%Mmin", time.localtime()))
dirs_name = "gpt_txt/"+run_time
txt_print = dirs_name+"/"+run_time+".txt"
md_print = dirs_name+"/"+run_time+".md"

os.makedirs(dirs_name)
# 保存到txt文本中的函数
def save_txt(*arg):
    output_writter = open(txt_print, "a+")
    arg_number = len(arg)
    # for i in range(arg_number):
    #     print(s(arg[i])+" ", end='')
    # print()
    for i in range(arg_number):
        output_writter.write(str(arg[i])+" ")
    output_writter.write("\n")
    output_writter.close()

def save_md(*arg):
    output_writter = open(md_print, "a+")
    arg_number = len(arg)
    # for i in range(arg_number):
    #     print(s(arg[i])+" ", end='')
    # print()
    for i in range(arg_number):
        output_writter.write(str(arg[i])+" ")
    output_writter.write("\n")
    output_writter.close()

def save_massage():
    np.save(dirs_name+"/"+run_time+".npy",message)

# 对话变量
message=[]
def clean():
    message=[]

# 用户对话格式
def user_content(txt):
    set_n = {"content": txt, "role": "user"}
    save_txt(set_n)
    return set_n

# 将用户提问纳入上文
def chat_gpt(prompt):
    save_md("User:<br>"+prompt+"<br>")
    message.append(user_content(prompt))
    chat_gpt_func()

# 提问代码
def chat_gpt_func():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    # 将gpt回答纳入上文
    response = completion.choices[0].message
    message.append(response)
    save_md("GPT:<br>"+response["content"]+"<br>")
    save_txt({"content":response["content"],"role":"assistant"})
    display(Markdown(response["content"]))
