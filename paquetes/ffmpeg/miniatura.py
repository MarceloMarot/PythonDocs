import ffmpeg

ruta_entrada = "demo.mp4"

# Ejemplo 1: PNG con anchura 500 px
salida_png = "miniatura.png"

instante = 4  # segundo 4
ancho = 500  # 500 px
alto = -1  # automatico 

video = ffmpeg.input(ruta_entrada, ss=instante)
video = video.filter("scale", ancho, alto) # (mantiene proporcion)
video = ffmpeg.output(video, salida_png , vframes=1)

# orden de ejecucion
ffmpeg.run(video)

# Ejemplo 2: JPG con altura 500 px
salida_jpg = "miniatura.jpg"

instante = 10 # segundo 10
ancho = -1  # automatico 
alto= 500  # 500 px

video = ffmpeg.input(ruta_entrada, ss=instante)
video = video.filter("scale", ancho, alto) # (mantiene proporcion)
video = ffmpeg.output(video, salida_jpg , vframes=1)

# orden de ejecucion
ffmpeg.run(video)