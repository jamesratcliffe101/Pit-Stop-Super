class RaceTrack:
    def __init__(self):
        track_image = None  # jpg of racetrack
        track_scale = 0  # integer for scaling of track size
        track_racing_line = []  # node graph thing is the same format of other racing ai game

    def load_track(self, track):
        """
        this method loads a racetrack into the game from one source (probably a file)
        if a new track is loaded while another track is already loaded, replace track
        """
        pass


class RaceManagement:
    def __init__(self):
        pass



def main():
    # create track
    race_track = RaceTrack()
    race_track.load_track("track123.png")

    # create car and driver, then a team

    # start "render thread" to draw everything

    # tell car to enter racetrack and do some laps

if __name__ == "__main__":
    main()
