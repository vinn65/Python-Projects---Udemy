import webbrowser as web

def WebAuto():
    chrome_path = "C:Program Files/Google/Chrome/Application/chrome.exe"

    URLS = (
        "stackoverflow.com",
        "google.com",
        "gmail.com",
        "youtube.com",
    )

    for url in URLS:
        print("opening: "+url)

        web.get(chrome_path).open(url)


WebAuto()