import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from core.process_model import ThermalProcess
model=ThermalProcess(tau=10, K=1.5,T_ext=20, T_init=20)
t_span=(0,100)
t_eval=np.linspace(0,100,500)
u_fixed = 50
result=solve_ivp(
    fun=lambda t,T:[model.derivative(T[0],t,u_fixed)],
    t_span=t_span,
    y0=[model.T_init],
    t_eval=t_eval
)
plt.plot(result.t, result.y[0], label="Tank Temperature (°C)", color="orangered")
plt.axhline(y=model.T_ext + model.K * u_fixed, color="gray", linestyle="--", label="Steady state")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Open-Loop: Tank response to 50% heater (no controller)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("assets/open_loop_test.png",dpi=150)
plt.show()
