import pytube
import sys

# replace sys.argv[1] with your youtube link
yt = pytube.YouTube(sys.argv[1])
stream = yt.streams.first()
stream.download("D:/")
print("Video Downloaded")
