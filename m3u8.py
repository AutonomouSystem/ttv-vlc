import streamlink
import subprocess

def get_m3u8_links(url, stream_quality="best"):
    streams = streamlink.streams(url)
    hls_streams = {name: stream.url for name, stream in streams.items() if stream.url.endswith('.m3u8')}
    if stream_quality in hls_streams:
        return [hls_streams[stream_quality]]
    else:
        return list(hls_streams.values())

def play_in_vlc(url):
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  
    subprocess.Popen([vlc_path, "--network-caching=1000", url])

if __name__ == "__main__":
    streamname = input("What stream would you like to 'ave a look at? ")
    twitch_stream_url = f"https://www.twitch.tv/{streamname}"
    links = get_m3u8_links(twitch_stream_url)
    
    if links:
        first_link = links[0]
        print(f"Opening the first m3u8 link in VLC: {first_link}")
        play_in_vlc(first_link)
    else:
        print("No m3u8 links found for the specified stream.")