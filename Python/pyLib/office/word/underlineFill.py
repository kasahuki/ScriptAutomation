from docx import Document
from docx.enum.text import WD_UNDERLINE

# 打开文档
doc = Document('./office/word/produ1.docx')  # 替换为你的文档路径

# 遍历文档中所有的段落
for paragraph in doc.paragraphs:
    # 遍历段落中的每一个run
    runs = paragraph.runs
    i = 0
    while i < len(runs):
        if runs[i].underline and (runs[i].text.startswith(" ") or runs[i].text.startswith("\t")):
           run = runs[i] # 赋值给run对象
           run.text="5245"
           while i + 1 < len(runs) and runs[i+1].underline and (runs[i+1].text.startswith(" ") or runs[i+1].text.startswith("\t")): # 连续的处理方案 以及空格字符多样化问题
               run.text = "  "+run.text # 保持居中
               i+=1     
        i+=1

        

        
# 保存修改后的文档
doc.save('./office/word/produ1.docx')
