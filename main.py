from paddleocr import PaddleOCR
import subprocess
import re

# 使用OCR库识别图像中的文本
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = r'E:\identification\img\1.jpg'
result = ocr.ocr(img_path, cls=True)

# 提取OCR识别的文本并连接成一个字符串
recognized_text = ""
for line in result[0]:
    for word_info in line:
        text = str(word_info[0])  # 将文本内容转换为字符串
        # 使用正则表达式来匹配坐标信息并删除
        text_without_coordinates = re.sub(r'\d+\.\d+', '', text)
        recognized_text += text_without_coordinates

# 指定要保存的音频文件路径
output_file_path = r'E:\identification\voice\1.mp3'

# 指定语音选项
voice = 'zh-CN-XiaoyiNeural'

# 构建edge-tts命令
tts_command = f'edge-tts --text "{recognized_text.strip()}" --write-media "{output_file_path}" --voice {voice}'

# 执行edge-tts命令
subprocess.run(tts_command, shell=True)

# 播放生成的语音
play_command = f'start {output_file_path}'
subprocess.run(play_command, shell=True)





