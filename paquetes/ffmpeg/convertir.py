import ffmpeg

ruta_entrada = "demo.webm"
ruta_salida = "demo.mp4"

(
	ffmpeg.input(ruta_entrada)
	.output(ruta_salida)
	.run()
)