import uuid

class TrafficLight:

    def __init__(self, position, green_time, red_time):
        self.id = uuid.uuid4()
        self.position = position
        self.green_time = green_time
        self.red_time = red_time
        self.state = "green"
        self.remaining_time = green_time
        self.obstacle = True

    def update(self, dt):
        # Atualiza o semáforo decrementando o tempo restante
        self.remaining_time -= dt
        if self.remaining_time <= 0:
            # Alterna entre verde e vermelho quando o tempo acabar
            if self.state == "green":
                self.state = "red"
                self.remaining_time = self.red_time
                self.obstacle = True  # Está vermelho, configura como obstáculo
            else:
                self.state = "green"
                self.remaining_time = self.green_time
                self.obstacle = False  # Está verde, configura como não obstáculo

    # modifies the duration of traffic lights based on the number of vehicles in front of them
    def kmeans_time_actuator():
        pass