import sys
import re
import requests
import time


def get_video_urls(url):
    html = requests.get(url).text
    p_name = "var username ?= ?'(.*?)';"
    name = re.search(p_name, html).group(1)
    p_pwd = "var password ?= ?'(.*?)';"
    pwd = re.search(p_pwd, html).group(1)
    p_resource = "var resourceId ?= ?'(.*?)';"
    resource = re.search(p_resource, html).group(1)

    headers = {
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Mobile Safari/537.36",
    }
    server = "http://210.76.211.10/vplus/"
    t = int(time.time() * 1000)
    url = f"{server}remote.do?method=query&loginname={name}&pwd={pwd}&resource={resource}&timeStamp={t}"
    r = requests.get(url, headers=headers)
    if '视频转码中，无法播放' in r.text:
        print("视频转码中，无法播放")
        return None

    p_stat = "\"video\":\"(.*?)\"}]"
    stat_url = re.search(p_stat, r.text).group(1)

    r = requests.get(stat_url)
    p_video = "http://210.76.211.10/vplus/m3u8.*?\.m3u8"
    video_urls = re.findall(p_video, r.text)
    if len(video_urls) == 4:
        return {
            "视频": video_urls[1],
            "PPT视频": video_urls[2],
        }
    else:
        return {
            "视频": video_urls[0],
        }


if __name__ == "__main__":
    print(get_video_urls(sys.argv[1]))
