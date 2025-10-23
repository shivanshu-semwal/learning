# `yt-dlp` `youtube-dl`

## `youtube-dl`

- `youtube-dl [url]` basic download command `[url]` can be a video url, a playlist url or a complete channel url
- `youtube-dl [url] -F` see all formats in which you can download a video or audio
- `youtube-dl [url] -f [no-of-format]` select the format in which you want to download the video `[no-of-format]` is achieved form the `-F` flag
- `youtube-dl [url] -f bestaudio` download the audio only (lazy to use the `-F` flag)
- `youtube-dl --write-thumbnail --skip-download [url]` download only thumbnails of a playlist
- `youtube-dl --add-metadata [url]` get metadata of a file and writes into the file
- `youtube-dl --write-info-json [url]` get metadata of a file and creates a separate the json file
- `youtube-dl -i [url]` ignore errors and continue
- `youtube-dl [url] --external-downloader aria2c --external-downloader-args "-j 8 -s 8 -x 8 -k 5M"` use external downloader
    for small files for more speed (`aria2c` used in this case)
- `youtube-dl [url] --external-downloader aria2c --external-downloader-args "-j 12 -s 12 -x 12 -k 5M"` use external downloader
    for small large for more speed (`aria2c` used in this case)
- `youtube-dl --write-auto-sub --sub-lang en  --skip-download [url]` get subtitles in english auto generated
- `youtube-dl --flat-playlist --dump-json https://www.youtube.com/playlist?list=<insertplaylistid>` - get info about a playlist in json

## `yt-dlp`

- `yt-dlp --list-formats [url]` see all formats in which you can download a video or audio
- `yt-dlp --list-subs  [url]` list all subtitles
- `yt-dlp --write-sub --sub-lang en --skip-download [url]` get subtitles in english
- `yt-dlp --write-sub --sub-lang en --sub-format vtt --skip-download [url]` get subtitles in english, subtitle format vtt
- `yt-dlp --get-filename -o "%(upload_date)s, %(title)s, https://www.youtube.com/watch?v=%(id)s" [url]` set the name format for downloaded file
- `yt-dlp -f 'bestvideo[height<=720]+bestaudio' [url]` download video with 720 resolution
- `yt-dlp -f bestaudio [url]` download audio only
- `yt-dlp --flat-playlist --print "%(url)s | %(title)s " https://www.youtube.com/@Computerphile/videos` get list of all videos in a channel
