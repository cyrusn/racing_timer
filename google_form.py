from urllib.parse import urlencode
from urllib.request import urlopen

url = "https://docs.google.com/forms/d/e/1FAIpQLSewkygNwfc-liPX3jZFf_5gZvRGBimdhEThRk5Le7-PHcFHOg/formResponse"  # Set destination URL here


class Form:
    def __init__(self):
        self.response = None

    def submit(self, team_name, track, time):
        form_data = {
            "entry.102136851": team_name,
            "entry.1499830162": track,
            "entry.2008640348": time,
        }

        data = urlencode(form_data).encode("ascii")
        with urlopen(url, data) as f:
            if f.getcode() == 200:
                print("submitted: [{}] {} - {}s".format(track, team_name, time))


if __name__ == "__main__":
    form = Form()
    form.submit("李炳一隊", "Left", 13.3)
    form.submit("李炳二隊", "Right", 12.1)
    form.submit("李炳三隊", "Left", 9.1)

