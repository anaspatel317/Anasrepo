import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over the MP3 files in the input folder
    for filename in os.listdir(mp3_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(mp3_folder, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(output_folder, wav_filename)

            # Load the MP3 file
            audio = AudioSegment.from_mp3(mp3_path)

            # Export the audio as WAV file
            audio.export(wav_path, format="wav")

            print(f"Converted {mp3_path} to {wav_path}")

if _name_ == "_main_":
    if len(sys.argv) < 3:
        print("Usage: python audio_converter.py <mp3_folder> <output_folder>")
    else:
        mp3_folder = sys.argv[1]
        output_folder = sys.argv[2]
        convert_mp3_to_wav(mp3_folder, output_folder)
