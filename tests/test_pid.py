from core.pid_controller import PIDController

pid = PIDController(Kp=2.0, Ki=0.1, Kd=0.5)

# Far from setpoint: output should be large (near max)
u = pid.compute(setpoint=70, measured=20, dt=0.1)
print(f"Control output when far from target: {u}")  # Expected: near 100

# Reset and test: at setpoint, output should be near 0
pid.reset()
u = pid.compute(setpoint=70, measured=70, dt=0.1)
print(f"Control output when at target: {u}")  # Expected: near 0