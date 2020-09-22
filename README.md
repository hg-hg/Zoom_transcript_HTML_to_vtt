# Zoom_transcript_HTML_to_vtt

Convert Zoom transcript from HTML text to vtt format

This is not to be used to download transcript of any Zoom videos that you do not have permission from the creator to download

## Usage

1. Press ``F12`` in the Zoom video window, click ``Elements`` tab

2. Find the ``<ul>`` label which contains ``aria-label="Audio Transcript List"``

3. Copy the whole section that is contained by that label

4. Paste the text into a file called ``transcript.txt`` in the same directory as ``transcript.py``

5. Run ``transcript.py``

6. ``formatted_transcript.transcript.vtt`` in the same directory is the vtt transcript file
