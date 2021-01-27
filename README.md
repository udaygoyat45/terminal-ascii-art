# terminal-ascii-art
This program displays a photo or plays a video with colors in your terminal!

Run `ascii_photos.py` to display photos and `ascii_videos.py` to display videos. All codec for videos and photos should be supported.
Photos need to be inside the directory called `photos` where these files are located and videos should go inside a directory called `videos`.

This program utilizes 256 color output and through ANSI codes, so make sure your terminal is compatible. 
You can check whether your terminal supports 256 color output by running `tput colors` (this should say `256`).
You can also try the following command:
```sh
curl -s https://gist.githubusercontent.com/HaleTom/89ffe32783f89f403bba96bd7bcd1263/raw/ | bash
```
