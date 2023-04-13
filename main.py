#! /usr/bin/python3
import pydub, pytube, sys, os

def yt2mp3(url, path):
    streams = sorted(pytube.YouTube(url).streams.filter(only_audio=True), key=lambda s: float(s.abr.replace("kbps", "")), reverse=True)

    name, ext = os.path.splitext(streams[0].download(path))
    if ext != ".mp3":
        pydub.AudioSegment.from_file(name + ext).export(name + ".mp3", format="mp3", bitrate="320k")
        os.remove(name + ext)

    print(f"Downloaded {name}.mp3")

def main():
    url = sys.argv[1]
    path = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.getcwd()
    yt2mp3(url, path)

if __name__ == "__main__":
    main()
