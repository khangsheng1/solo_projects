import asyncio
import os
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm  # Import the tqdm library for the progress bar
import edge_tts  # type: ignore

async def text_to_speech(text, volume="0%", voice="en-US-JennyNeural", output_media="output.mp3"):
    # Create an instance of the Communicate class with the desired text, voice, and parameters
    communicate = edge_tts.Communicate(
        text=text,
        volume=volume,
        voice=voice
    )

    # Prepare to write the audio to the output file
    with open(output_media, "wb") as audio_file:
        # Stream the TTS result to the audio file
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])

async def convert_text_file_to_speech(input_file, output_dir, volume="+0%", voice="en-US-JennyNeural"):
    # Define the output file path
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    output_media = os.path.join(output_dir, f"{base_filename}.mp3")
    
    # Read the content from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Convert the text to speech without changing rate and pitch
    await text_to_speech(
        text=text,
        volume=volume,
        voice=voice,
        output_media=output_media
    )

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
                    output_dir=output_dir,
                    volume="+0%",  # Default volume
                    voice="en-US-EmmaMultilingualNeural"  # Choose a different voice
                ))

if __name__ == "__main__":
    select_files_and_convert()
