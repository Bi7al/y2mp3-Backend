from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
from urllib.parse import unquote
app = Flask(__name__)





CORS(app,resources={r"/*": {"origins": ["http://127.0.0.1:5500", "https://y2mp3-front-end.vercel.app"]}})

@app.route('/')
def default_function():
    try:
        return jsonify({"message":"This is the Default Route for Youtube to Mp3 Site"})
    except Exception as e:
        app.logger.error(f"Error in default_function: {str(e)}")
        raise
@app.route('/download/<path:url>',methods=['POST'])
def download_function(url):
    decoded_url = unquote(url)
    try:
        # Get YouTube URL from frontend


        # Download video
        yt = YouTube(decoded_url)
        video_stream = yt.streams.filter(only_audio=True).first()

        # Use /tmp directory for temporary storage
        video_path = os.path.join('/tmp', "temp_video.mp4")
        video_stream.download(output_path='/tmp', filename="temp_video.mp4")

        # Convert to MP3
        mp3_path = os.path.join('/tmp', "output.mp3")
        audio_clip = AudioFileClip(video_path)
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()

        # Remove the video file to save space
        os.remove(video_path)

        # Send the MP3 file to the frontend
        return send_file(mp3_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500






# Vercel requires the application to be exported as 'app'
app = app
