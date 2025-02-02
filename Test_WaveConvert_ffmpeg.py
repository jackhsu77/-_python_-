from pydub import AudioSegment
import soundfile as sf
import numpy as np
from pydub.utils import mediainfo
import datetime as dt

# 合併2個Ulaw stereo檔案, 可以合但是有雜音
path ="D:\\speech-to-text-py\\Costco\\"
# List of input files
#input_files = [path + '20220518134049.wav', path + '20220518112549.wav']
input_files = [path + '1.wav', path + '2.wav']
# Create an empty AudioSegment for the output
merged = AudioSegment.empty()
# Load and append each file
for file in input_files:
    audio = AudioSegment.from_file(file, format="wav")
    merged += audio

# Export the merged audio as mu-law encoded WAV
merged.export(".\\merged_output.wav", format="wav", codec="pcm_mulaw")
print("Merged audio saved as 'merged_output.wav'.")
exit()


# 取得檔案格式
def get_audio_format(file_path):
    try:
        info = mediainfo(file_path)
        return info
    except Exception as e:
        print(f"无法读取文件格式: {e}")
        return None
#file_path = "c:\\euls\\msgsm.wav"      # 辨識ok
#file_path = "c:\\euls\\output.wav"     # 辨識ok
#file_path = "c:\\euls\\dvi8k.wav"      # 辨識ok
#file_path = "c:\\euls\\Ulaw.wav"       # 辨識ok
#file_path = "c:\\euls\\Alaw.wav"       # 辨識ok
file_path = "c:\\euls\\aaa.mp3"         # 辨識ok
audio_format = get_audio_format(file_path)
if audio_format:
    for k,v in audio_format.items():
        print(f"{k}: {v}")
else:
    print("unknown Format")
exit()



# 轉檔 msgsm --> pcm 16
buffer_size = 1024  # 每次处理的音频数据块大小
output_sample_rate = 8000  # 输出采样率
output_bit_depth = 'PCM_16'  # 输出位深度，可以是 'PCM_16' 或 'ULAW'

# 读取MSGSM音频文件
input_file = "c:\\euls\\msgsm.wav"
audio = AudioSegment.from_file(input_file, format="wav")

# 转换采样率为8kHz
audio = audio.set_frame_rate(output_sample_rate)

# 将音频数据转换为 numpy 数组
audio_data = np.array(audio.get_array_of_samples())

# 将音频数据按 buffer 大小分块处理
buffers = [audio_data[i:i + buffer_size] for i in range(0, len(audio_data), buffer_size)]

# 将每个buffer转换并保存
output_file = "c:\\euls\\output" + dt.datetime.now().strftime("%Y%m%d%H%M%S") + ".wav"
with sf.SoundFile(output_file, mode='w', samplerate=output_sample_rate, channels=audio.channels, subtype=output_bit_depth) as file:
    for buffer in buffers:
        file.write(buffer)

print(f"::--> {output_file}")
