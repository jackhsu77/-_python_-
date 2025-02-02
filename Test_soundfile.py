import soundfile as sf

# 載入 ulaw stereo 聲音檔
#audio_file_path = "D:\\speech-to-text-py\\M1F1-mulaw-AFsp.wav"
audio_file_path = "D:\\speech-to-text-py\\ulaw_stereo.wav"
y, sr = sf.read(audio_file_path)

# 分離左聲道和右聲道
left_channel = y[:, 0]
right_channel = y[:, 1]

# 保存左聲道和右聲道到新的音訊檔案
sf.write("D:\\speech-to-text-py\\left_channel.wav", left_channel, sr)
sf.write("D:\\speech-to-text-py\\right_channel.wav", right_channel, sr)