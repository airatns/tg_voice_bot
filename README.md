# Telegram Bot, voice/image.

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/opencv/opencv-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/numpy/numpy-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original-wordmark.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;

## **The case:**

Create a Telegram Bot that can

1. Save audio messages from dialogs to a database (DBMS or hard drive) by user IDs.

2. Convert all audio messages to **.wav** format with a sampling rate of **16 kHz**. </br>
Recording format: uid -> [audio_message_1, audio_message_2, ..., audio_message_N].

3. Detect faces in sent photos. Save only those where the face is.

</br>

## **Getting Started:**

Clone the repository:

>*git clone git@github.com:airatns/tg_voice_bot.git*

Set up the virtual environment:

>*python -m venv env* \
>*source env/scripts/activate*

Install dependencies in the app using requirements.txt:

>*python -m pip install --upgrade pip* \
>*pip install -r requirements.txt*

Run the app locally:

>*python main.py*

</br>

In case of problems with **[FFmpeg](https://www.wikihow.com/Install-FFmpeg-on-Windows)**
