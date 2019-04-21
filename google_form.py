from urllib.parse import urlencode
from urllib.error import URLError, HTTPError
from urllib.request import urlopen
from school import School
from format_string import format_string


url = "https://docs.google.com/forms/d/e/1FAIpQLSewkygNwfc-liPX3jZFf_5gZvRGBimdhEThRk5Le7-PHcFHOg/formResponse"  # Set destination URL here


class Form:
    def __init__(self):
        self.response = None

    def submit(self, school_code, team, track, time):
        school_name = School.getName(school_code)

        form_data = {
            "entry.1154166350": school_name,
            "entry.102136851": team,
            "entry.1499830162": track,
            "entry.2008640348": time,
        }

        data = urlencode(form_data).encode("ascii")
        try:
            with urlopen(url, data) as f:
                if f.getcode() == 200:
                    print(format_string("Submitted", track, school_name, team, time))
                else:
                    print("ERROR: {}\n{}".format(f.getcode(), f.info()))
        except HTTPError as e:
            print(e.code)
            print(e.read())


if __name__ == "__main__":
    School.printList()

    form = Form()
    school_code = input("Select School Code: ")
    team = input("Team (1-3): ")
    track = "B"
    duration = 12.3

    form.submit(school_code, team, track, duration)
