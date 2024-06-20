
import ffmpeg

ruta_entrada = "demo.mp4"
ruta_salida = "clip.mp4"

# # version A
# video = ffmpeg.input(ruta_entrada)
# video = video.trim(start=0, duration=10) # BIEN
# video = video.trim(start=10, duration=10) # MAL: primeros segundos congelado
# video =  ffmpeg.output(video, ruta_salida) 

# # orden de ejecucion
# ffmpeg.run(video)


# # version B
# (
#     ffmpeg.input(ruta_entrada,ss=10, to=15) #BIEN
#     .output( ruta_salida) 
#     .run()
# )


# version C

video = ffmpeg.input(ruta_entrada,ss=10, to=20) #BIEN
video =  ffmpeg.output(video, ruta_salida) 
ffmpeg.run(video)
