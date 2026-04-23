class ThermalProcess:
    def __init__(self, tau=10.0, K=1.5, T_ext=20.0, T_init=20.0):
        self.tau=tau
        self.K=K
        self.T_ext=T_ext
        self.T_init=T_init
    def derivative(self,T,t,u):
        dTdt=(-T + self.K *u + self.T_ext)/self.tau
        return dTdt
    def get_intial_temperature(self):
        return self.T_init
