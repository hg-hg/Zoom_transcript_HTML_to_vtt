# Zoom_transcript_HTML_to_vtt

Convert Zoom transcript from HTML text to vtt format

This is not to be used to download transcript of any Zoom videos that you do not have permission from the creator to download

## Usage

1. Open the video in ``Chrome``

2. Press ``F12`` in the Zoom video window, click ``Elements`` tab

3. Find the ``<ul>`` label which contains ``aria-label="Audio Transcript List"``

4. Copy the whole section that is contained by that label

5. Paste the text into a file called ``transcript.txt`` in the same directory as ``transcript.py``

6. Run ``transcript.py``

7. ``formatted_transcript.transcript.vtt`` in the same directory is the vtt transcript file
