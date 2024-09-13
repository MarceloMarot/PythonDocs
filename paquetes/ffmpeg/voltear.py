import ffmpeg

ruta_entrada = "demo.mp4"


salida_horizontal = "horizontal.mp4"
salida_vertical = "vertical.mp4"

# Ejemplo 1
# 'hflip': voltea de derecha a izquierda
video = ffmpeg.input(ruta_entrada)
video = ffmpeg.hflip(video)
video = ffmpeg.output(video, salida_horizontal)

# orden de ejecucion
ffmpeg.run(video)

# Ejemplo 2
# 'vflip' : voltea de arriba a abajo
video = ffmpeg.input(ruta_entrada)
video = ffmpeg.vflip(video)
video = ffmpeg.output(video, salida_vertical)

# orden de ejecucion
ffmpeg.run(video)

