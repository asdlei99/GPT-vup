"""
 @Author: jiran
 @Email: jiran214@qq.com
 @FileName: audio.py
 @DateTime: 2023/4/24 14:16
 @SoftWare: PyCharm
"""
import asyncio

import edge_tts
from src import config

from pygame import mixer, time as pygame_time

from src.utils.utils import worker_logger
from src.utils.utils import audio_lock

logger = worker_logger


async def tts_save(text, path):
    # tts = edge_tts.Communicate(text=text, proxy=f'http://{config.proxy}', **config.tss_settings)
    tts = edge_tts.Communicate(text=text, **config.tss_settings)
    await tts.save(path)


def play_sound(file_path):
    with audio_lock:
        # 播放生成的语音文件
        mixer.init()
        print('file_path', file_path)
        mixer.music.load(file_path)
        mixer.music.play()
        while mixer.music.get_busy():
            pygame_time.Clock().tick(10)

        mixer.music.stop()
        mixer.quit()


if __name__ == '__main__':
    asyncio.run(tts_save('你真是个臭傻*，哈哈哈哔哔哔哈哈哈', './1111.mp3'))
    play_sound('1111.mp3')