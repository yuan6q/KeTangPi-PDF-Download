import os
import re
import img2pdf

# 获取用户输入的文件夹路径
folder_path = input("Folder Path: ").strip()

# 获取所有以 img 开头的文件，并按顺序排序
img_files = sorted(
    (f for f in os.listdir(folder_path) if f.startswith("img")),
    key=lambda x: int(re.search(r"\((\d+)\)$", x).group(1)) if re.search(r"\((\d+)\)$", x) else -1
)
# 检查是否有图片
if not img_files:
    print("❌ 没有找到以 img 开头的文件，请检查文件夹路径。")
    exit(1)

# 合成 PDF 的输出路径
output_pdf = os.path.join(folder_path, "output.pdf")

# 合成 PDF
with open(output_pdf, "wb") as pdf_file:
    pdf_data = img2pdf.convert([os.path.join(folder_path, img) for img in img_files])
    pdf_file.write(pdf_data)

print(f"✅ PDF 文件已成功生成: {output_pdf}")
