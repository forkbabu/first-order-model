ffmpeg -i jadoo.mp4 -map 0:a output.mp3
ffmpeg -i generated.mp4 -i output.mp3 -c copy -shortest output.mp4
