import vimeo
import sys

# Replace these with your credentials from https://developer.vimeo.com/apps
CLIENT_ID     = input("Vimeo Client ID: ")
CLIENT_SECRET = input("Vimeo Client Secret: ")
ACCESS_TOKEN  = input("Vimeo Access Token: ")

client = vimeo.VimeoClient(
    token=ACCESS_TOKEN,
    key=CLIENT_ID,
    secret=CLIENT_SECRET,
)

video_path = "/Users/oceaneboulais/aiconsultansea/trimmed_1.75x.mov"

print("\nUploading to Vimeo...")
try:
    uri = client.upload(
        video_path,
        data={
            "name": "AI ConsultanSea — Team Pitch",
            "description": "SEASCAPE pitch video — AI ConsultanSea team.",
            "privacy": {"view": "anybody"},
        },
    )
    video_id = uri.split("/")[-1]
    print(f"\nUpload complete!")
    print(f"Vimeo URI : {uri}")
    print(f"Video URL : https://vimeo.com/{video_id}")
except Exception as e:
    print(f"Upload failed: {e}")
    sys.exit(1)
