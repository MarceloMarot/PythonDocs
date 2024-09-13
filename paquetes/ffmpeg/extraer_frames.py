
import ffmpeg

ruta_entrada = "demo.mp4"

frames_salida = "frame_%d.png" # formato para nombrar los frames de salida

# Ejemplo 1: N primeros frames 
# nro_frames = 50
# (
# 	ffmpeg.input(ruta_entrada)
# 	.output(frames_salida , vframes=nro_frames)      
# 	.run()
# )

# Ejemplo 2: diezmado frames
fps = 0.1  # 1 frame cada 10 segundos
(
	ffmpeg.input(ruta_entrada)
	# .output(frames_salida , vf='fps=1')  
	.output(frames_salida , vf=f'fps={fps}')
	.run()
)