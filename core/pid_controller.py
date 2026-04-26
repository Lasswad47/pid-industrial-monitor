class PIDController:
    def __init__(self, Kp=2.0, Ki=0.1, Kd=0.5, output_min=0.0, output_max=100.0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.output_min = output_min
        self.output_max = output_max
        self._integral = 0.0
        self._prev_error = 0.0

    def compute(self, setpoint, measured, dt):
        error = setpoint - measured
        P = self.Kp * error
        self._integral += error * dt
        I = self.Ki * self._integral
        D = self.Kd * (error - self._prev_error) / dt if dt > 0 else 0.0
        output = P + I + D
        output = max(self.output_min, min(self.output_max, output))
        return output

    def reset(self):
        self._integral = 0.0
        self._prev_error = 0.0

