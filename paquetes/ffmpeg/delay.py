import ffmpeg


delay


# extraccion audio

# audio_left = (
#     ffmpeg
#     .input('audio-left.wav')
#     .filter('atrim', start=5)
#     .filter('asetpts', 'PTS-STARTPTS')
# )

# audio_right = (
#     ffmpeg
#     .input('audio-right.wav')
#     .filter('atrim', start=10)
#     .filter('asetpts', 'PTS-STARTPTS')
# )


# audio_salida = "audio.mp3"


ruta_entrada = "video.mp4"


audio_salida = "audio.mp3"
(
	ffmpeg.input(ruta_entrada)
	.output(audio_salida )  
	.run()
)




input_video = ffmpeg.input('input-video.mp4')

(
    ffmpeg
    .filter((audio_left, audio_right), 'join', inputs=2, channel_layout='stereo')
    .output(input_video.video, 'output-video.mp4', shortest=None, vcodec='copy')
    .overwrite_output()
    .run()
)