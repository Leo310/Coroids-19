from gameobject import GameObject


class Healthbar(GameObject):
    def __init__(self, health):
        super().__init__((60, 580), image_paths=[
            "assets/thermometer/dead.png",
            "assets/thermometer/40_deg.png",
            "assets/thermometer/39_deg.png",
            "assets/thermometer/38_deg.png",
            "assets/thermometer/37_deg.png"
        ], image_size=(100, 300))
        self._layer = 20
        self.health = health + 1  # +1 because there is also 1 death img
        self.image = self._images[self.health-1]

    def update(self, dt):
        self.image = self._images[self.health-1]
