# Text-to-Speech (TTS) Scripts

This repository contains multiple Python scripts for converting text files and EPUB documents to speech using different libraries and approaches. Each script showcases a different method for generating speech from text, offering flexibility depending on the desired use case.

## Scripts Overview

### 1. `TTS_BUILD.py`
This script utilizes the `edge_tts` library for converting text files to speech using Edge Text-to-Speech voices. The user can select multiple text files and an output directory through a graphical user interface (GUI) powered by `tkinter`. The conversion progress is displayed using `tqdm` for a visual progress bar.

#### Key Features:
- Converts multiple text files to audio (MP3 format) using Azure TTS voices.
- GUI file selection for input files and output directory.
- Configurable voice selection, volume, and speech parameters.
- Uses `asyncio` for asynchronous operations.

### 2. `pyttsx3_example.py`
A basic demonstration of text-to-speech using the `pyttsx3` library, which is an offline, lightweight TTS engine. The script showcases adjusting voice rate, volume, and selecting different voices (male or female). Additionally, it demonstrates saving the generated speech to an MP3 file.

#### Key Features:
- Offline TTS using `pyttsx3` without the need for an internet connection.
- Controls for adjusting speech rate, volume, and voice gender.
- Example of saving generated speech to an MP3 file.

### 3. `epub_to_text.py`
A script for extracting text content from EPUB files and saving it as a plain text file. This can be useful for converting eBooks into a format that can then be used for further text-to-speech processing.

#### Key Features:
- Converts EPUB content to plain text format.
- Utilizes `ebooklib` and `BeautifulSoup` to parse and extract text.
- Handles warnings related to the EPUB parsing library.

### 4. `tts_testing_different_libraries.py`
This script demonstrates the usage of the `edge_tts` library for fetching and listing available voices. It can be helpful for users to know which voices are available in their Edge Text-to-Speech account.

#### Key Features:
- Fetches and displays available Azure TTS voices.
- Asynchronous function for efficient voice retrieval.

## Demonstration

A small demonstration has been included in the repository to show the use of these scripts. Simply run the TTS_BUILD script and select the short passage to convert the TXT file to an MP3 file. You can use the tts_testing_different_librarires script to test out the different voices included in edge_tts.

This has been by far the best TTS library I have used so. 

### Requirements

- Python 3.8+
- Required libraries: `asyncio`, `os`, `tkinter`, `tqdm`, `edge_tts`, `pyttsx3`, `ebooklib`, `BeautifulSoup`, `warnings`, `io`

You can install the dependencies using:

```bash
pip install asyncio tqdm edge-tts pyttsx3 ebooklib beautifulsoup4
```

Contributing
Feel free to contribute by adding new features, improving existing ones, or reporting any issues. Pull requests are always welcome!
