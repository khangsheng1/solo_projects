import asyncio
import os
import io  # Import the io module
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm  # Import the tqdm library for the progress bar
import edge_tts  # type: ignore

async def text_to_speech(text, rate="0%", voice="en-US-JennyNeural"):
    # Create an instance of the Communicate class with the desired text, voice, and parameters
    communicate = edge_tts.Communicate(
        text=text,
        rate=rate,
        voice=voice
    )

    # Create an in-memory buffer to store the audio
    audio_buffer = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])

    audio_buffer.seek(0)
    return audio_buffer

async def convert_text_file_to_speech(input_file, output_dir):
    # Define the output file path
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    output_media = os.path.join(output_dir, f"{base_filename}.mp3")
    
    # Read the content from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Split the text into chunks and process each chunk
    num_chunks = (len(text) // chunk_size) + 1
    audio_buffers = []

    with tqdm(total=num_chunks, desc=f"Processing {base_filename}", unit="chunk") as pbar:
        for start in range(0, len(text), chunk_size):
            end = min(start + chunk_size, len(text))
            chunk_text = text[start:end]

            # Convert the chunk to speech and collect the audio buffer
            audio_buffer = await text_to_speech(
                text=chunk_text,
                rate=rate,
                voice=voice
            )
            audio_buffers.append(audio_buffer)
            pbar.update(1)

    # Combine all audio chunks into one file
    with open(output_media, "wb") as audio_file:
        for buffer in audio_buffers:
            audio_file.write(buffer.getvalue())

def select_files_and_convert():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select multiple text files
    input_files = filedialog.askopenfilenames(title="Select Text Files", filetypes=[("Text Files", "*.txt")])
    
    if input_files:
        # Open file dialog to select the output directory
        output_dir = filedialog.askdirectory(title="Select the Output Directory")
        
        if output_dir:
            # Initialize the progress bar
            for input_file in tqdm(input_files, desc="Processing Files", unit="file"):
                # Run the conversion with the selected file and directory
                asyncio.run(convert_text_file_to_speech(
                    input_file=input_file,
                    output_dir=output_dir
                ))

if __name__ == "__main__":
    # Define the rate and voice you want to use
    rate = "-13%"  # Example rate change: slower rate by 13%
    voice = "en-US-EmmaMultilingualNeural"  # Choose a different voice
    chunk_size = 1000  # Number of characters per chunk (adjust as needed)

    select_files_and_convert()
