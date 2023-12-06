
class TrafficLight:

    def __init__(self, position, green_time, red_time):
        self.position = position
        self.green_time = green_time
        self.red_time = red_time
        self.state = "green"
        self.remaining_time = green_time

    def update(self, dt):
        # Atualiza o semáforo decrementando o tempo restante
        self.remaining_time -= dt
        if self.remaining_time <= 0:
            # Alterna entre verde e vermelho quando o tempo acabar
            if self.state == "green":
                self.state = "red"
                self.remaining_time = self.red_time
            else:
                self.state = "green"
                self.remaining_time = self.green_time
