from pydub import AudioSegment
import numpy as np

# 创建一个示例的中文文本
text_channel_0 = "你好，这是左声道的声音。"
text_channel_1 = "您好，这是右声道的声音。"

# 使用 pydub 生成音频
def text_to_speech(text, sample_rate=8000, duration_ms=2000):
    # 简单生成一个正弦波作为音频内容，实际应用中应使用 TTS 服务生成语音
    frequency = 440  # 频率 Hz
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * duration_ms / 1000))
    audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
    audio_segment = AudioSegment(
        (audio_data * (2**15 - 1)).astype(np.int16).tobytes(), 
        frame_rate=sample_rate, 
        sample_width=2, 
        channels=1
    )
    return audio_segment

# 生成左声道和右声道音频
left_channel = text_to_speech(text_channel_0)
right_channel = text_to_speech(text_channel_1)

# 创建立体声音频
stereo_audio = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

# 保存为 PCM 编码的 WAV 文件
pcm_wav_path = "stereo_pcm_chinese.wav"
stereo_audio.export(pcm_wav_path, format="wav")

# 重新加载并转为 uLaw 编码
audio = AudioSegment.from_file(pcm_wav_path)
ulaw_audio = audio.set_frame_rate(8000).set_sample_width(1).set_channels(2)

# 保存为 uLaw 编码的 WAV 文件
ulaw_wav_path = "stereo_ulaw_chinese.wav"
ulaw_audio.export(ulaw_wav_path, format="wav", codec="ulaw")

print("生成完成：stereo_ulaw_chinese.wav")
