import taichi as ti


class Engine:

    def __init__(self, dt, grid_res, dim=3):
        self.dim = dim
        self.dt = dt
        self.substep_dt = dt
        self.grid_res = grid_res
        self._is_particle_initialized = False
        self._is_grid_initialized = False
        self.particle_system_list = dict()

        pass

    def set_param(self):
        pass

    def add_particle_system(self):
        pass

    def p2g(self):
        pass

    def g2p(self):
        pass

    def substep(self):
        pass

    def update_grid(self):
        pass

    def update_particle(self):
        pass

    pass
