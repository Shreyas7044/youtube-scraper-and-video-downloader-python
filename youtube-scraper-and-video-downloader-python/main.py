from pytube import YouTube

print("===== YouTube Scraper & Downloader =====")
link = input("Enter Link of YouTube Video: ")

try:
    yt = YouTube(link)

    # Scraping Details
    print("\n--- Video Details ---")
    print("Title      :", yt.title)
    print("Views      :", yt.views)
    print("Duration   :", yt.length, "seconds")
    print("Rating     :", yt.rating)
    print("\nDescription:\n", yt.description[:500], "...")

    # Downloading Video
    print("\nDownloading highest resolution video...")
    stream = yt.streams.get_highest_resolution()
    stream.download()

    print("\nDownload Completed Successfully!")

except Exception as e:
    print("Error occurred:", e)