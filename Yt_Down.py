from pytube import YouTube


def video(yt_url):
    try:
        # Create a YouTube object and download the video
        yt = YouTube(yt_url)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first()

        if stream:
            stream.download()
        else:
            print("No suitable streams found for download.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def audio(yt_url):
    try:
        # Create a YouTube object and download the audio
        yt = YouTube(yt_url)

        # Filter streams to select the highest quality audio stream
        audio_stream = yt.streams.filter(
            only_audio=True).order_by('abr').desc().first()

        if audio_stream:
            audio_stream.download()
        else:
            print("No suitable audio stream found for download.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

