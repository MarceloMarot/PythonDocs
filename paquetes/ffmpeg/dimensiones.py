import ffmpeg

ruta_entrada = "demo.mp4"


probe = ffmpeg.probe(ruta_entrada)

video = next(
    (stream for stream in probe["streams"] if stream["codec_type"] == "video"), None
)

ancho = int( video["width"])
alto = int(video["height"])

print(f"Ancho: {ancho}")
print(f"Alto : {alto}")