'''
import wave

def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # 取得聲道數量、取樣寬度、取樣率、總取樣數
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        frame_count = wav_file.getnframes()
        
        # 計算長度（秒）
        duration = frame_count / frame_rate
        return duration

# 替換成你的 .wav 文件路徑
file_path = 'D:\\speech-to-text-py\\Costco\\20220518134049.wav'
duration = get_wav_duration(file_path)
print(f"The duration of the .wav file is {duration:.2f} seconds.")
'''
import soundfile as sf

def get_wav_duration(file_path):
    # 讀取音頻文件
    with sf.SoundFile(file_path) as audio_file:
        # 獲取取樣率和總取樣數
        frames = audio_file.frames
        sample_rate = audio_file.samplerate
        
        # 計算音頻長度（秒數）
        duration = frames / sample_rate
        return duration

# 替換成你的 .wav 文件路徑
file_path = 'D:\\speech-to-text-py\\Costco\\20220518134049.wav' # ulaw 雙聲道可以判斷出來長度
file_path = 'D:\\speech-to-text-py\\Costco\\20220518124316.wav' # ulaw 雙聲道可以判斷出來長度
file_path = 'D:\\speech-to-text-py\\Costco\\else\\eaststone_20240530144744.wav' # ulaw 單聲道
file_path = "C:\\Users\\jackhsu\\Documents\\Multisuns\\各種聲音檔\\18_GSMWave.wav"  # gsmwave 單聲道
file_path = r"c:\Users\jackhsu\Documents\Multisuns\各種聲音檔\12_DVI_ADPCM_8K.wav"  # dvi adpcm 8k 單聲道

duration = get_wav_duration(file_path)
print(f"The duration of the .wav file is {duration:.2f} seconds.")
