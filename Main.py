import whisper

# Cargar el modelo Whisper
model = whisper.load_model("base")  # Puedes cambiar "base" por "small", "medium", "large" según el rendimiento que desees

# Ruta del archivo de audio
audio_path = '/home/mitros/Downloads/Audio.mp4'  # Reemplaza con la ruta correcta

# Transcribir el audio
print("Transcribiendo el audio...")
result = model.transcribe(audio_path)

# Imprimir la transcripción
print("Transcripción:")
print(result['text'])

# Guardar la transcripción en un archivo de texto
with open("transcripcion.txt", "w") as file:
    file.write(result['text'])

print("La transcripción ha sido guardada en 'transcripcion.txt'.")
