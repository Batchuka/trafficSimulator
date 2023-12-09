import threading
import time
import numpy as np
from collections import defaultdict

class PositionTable:
    def __init__(self, simulation):
        self.positions = defaultdict(lambda: {'x': 0, 'y': 0, 'closest_distance': np.inf})
        self.lock = threading.Lock()
        self.stop_flag = False
        self.simulation = simulation

    def update_positions_and_distances(self):

        while not self.stop_thread:
            with self.lock:
                self.update_distances()
            
            time.sleep(0.1)  # Adjust the sleep time as needed

    def update_distances(self):

        for vehicle in self.simulation.vehicles.items():
            print(vehicle)

            for vehicle in self.simulation.vehicles.items():
                position = vehicle[1]
                closest_distance = self.calculate_closest_distance(position[0], position[1], vehicle.id, segment)
                self.positions[vehicle.id] = {'x': position[0], 'y': position[1], 'closest_distance': closest_distance}

            for light in segment.lights:
                position = light.position
                closest_distance = self.calculate_closest_distance(position[0], position[1], light.id, segment)
                self.positions[light.id] = {'x': position[0], 'y': position[1], 'closest_distance': closest_distance}
            
    
    def calculate_closest_distance(self, x, y, obj_id):
        closest_distance = np.inf

        for other_id, other_position in self.positions.items():
            if obj_id != other_id:  # Não calcular para o próprio objeto
                other_x, other_y = other_position['x'], other_position['y']
                distance = np.sqrt((x - other_x)**2 + (y - other_y)**2)
                closest_distance = min(closest_distance, distance)

        return closest_distance
    

    def start_thread(self):
        self.thread = threading.Thread(target=self.update_positions_and_distances)
        self.thread.start()

    def stop_thread(self):
        self.stop_flag = True
        self.thread.join()

    def get_closest_obstacle(self, id):
        with self.lock:
            return self.positions[id]['closest_distance']
    