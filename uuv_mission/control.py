class PDController:
    def __init__(self, kp, kd):
        self.kp = kp
        self.kd = kd
        self.prev_error = 0

    def compute_control(self, error):
        derivative = error - self.prev_error
        control_signal = self.kp * error + self.kd * derivative
        self.prev_error = error
        return control_signal