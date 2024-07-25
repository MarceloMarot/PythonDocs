

import ffmpeg

ruta_entrada = "demo.mp4"
thumbnail_salida = "thumbnail.png" 

# Ejemplo 1
## instante fijo  
# (
# 	ffmpeg.input(ruta_entrada, ss="00:00:15")
# 	.output(thumbnail_salida, vframes=1)
# 	.run()
# )

# Ejemplo 2
# ventana seleccion 100 muestras (default)   
(
	ffmpeg.input(ruta_entrada)
	.filter('thumbnail')
	.output(thumbnail_salida, vframes=1)
	.run()
)


# Ejemplo 3
## ventana seleccion 500 muestras  
# (
# 	ffmpeg.input(ruta_entrada)
# 	.filter('thumbnail', n=500)
# 	.output(thumbnail_salida, vframes=1)
#     # .output("thumbnail_filter_2.jpg", vframes=1)
# 	.run()
# )