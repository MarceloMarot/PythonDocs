
import ffmpeg

ruta_entrada = "demo.mp4"
audio_salida = "audio.mp3"


(
	ffmpeg.input(ruta_entrada)
	.output(audio_salida )  
	.run()
)