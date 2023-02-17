
def update_car_physics():
    pass


class Driver:
    def __init__(self, name):
        self.name = name

        self.skill = 0  # tunable parameter
        self.stamina = 0  # tunable parameter
        self.variation = 0  # tunable parameter
        self.pit_skill = 0  # tunable parameter
        self.overtake_skill = 0  # tunable parameter
        self.defend_skill = 0  # tunable parameter

        self.pitting = False
        self.throttle_pos = 0
        self.steering_pos = 0
        self.brake_pos = 0

    def update_driver_ai(self):  # given all the information it needs, update drivers specific variables

        # needs to know...
        """
        - racing lines and current node
        - pit location and pit nodes
        - location of nearby cars
        - braking distance
        - cornering capability
        - its owns stats (skill, fatigue etc...)

        """
        pass


class Team:
    def __init__(self, name):
        self.name = name

        self.refuel_speed = 0  # tunable parameter
        self.tire_change_speed = 0  # tunable parameter

        self.current_pit_strategy = []

    def request_car_to_pit(self, car):
        pass

    def send_car_to_track(self, car):
        pass

    def create_pit_strategy(self):
        pass


class Car:
    def __init__(self, name):
        self.name = name

        self.coordinates = [0, 0]
        self.velocity = 0.0
        self.direction = 0.0

        self.acceleration_power = 0  # tunable parameter
        self.top_speed = 0  # tunable parameter
        self.tire_grip_multiplier = 0  # tunable parameter
        self.braking_power = 0  # tunable parameter
        self.fuel_tank_size = 0  # tunable parameter
        self.fuel_burn_rate = 0  # tunable parameter

        self.fuel_level = 0
        self.tire_degradation_rate = 0

    def update_physics(self):
        pass


class RaceManagement:
    def __init__(self):
        self.current_session = 0
        self.best_laps = []
        self.last_laps = []
        self.laps_done = []
        self.race_position = []

    def update_timing(self):
        pass


class Display:
    def __init__(self):
        pass

    def startup_display(self):  # may need to run concurrently
        pass

    def stop_display(self):
        pass

