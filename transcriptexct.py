from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_youtube_transcript(video_id):
    try:
        # Fetch the transcript using the video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript without timestamps
        formatted_transcript = ""
        for entry in transcript:
            text = entry['text']
            formatted_transcript += f"{text}\n"

        return formatted_transcript

    except Exception as e:
        return f"Error: {e}"

def extract_video_id(url):
    # Extract video ID from the YouTube URL
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

if __name__ == "__main__":
    # Ask user to input the YouTube video link
    video_url = input("Please enter the YouTube video URL: ")

    try:
        # Extract the video ID from the provided URL
        video_id = extract_video_id(video_url)

        # Get the transcript
        transcript = get_youtube_transcript(video_id)

        # Save the transcript to a file
        with open("transcript.txt", "w", encoding="utf-8") as file:
            file.write(transcript)

        print("Transcript saved to transcript.txt")
    except Exception as e:
        print(f"Error: {e}")
