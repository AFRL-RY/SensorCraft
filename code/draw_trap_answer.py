def draw_trap(self):
        vector = self.get_sight_vector()
        block = self.model.hit_test(self.position, vector)[0]
        if block:
            x, y, z = block
            for i in xrange(-3, 4):
                for j in xrange(-3, 4):
                    if (i == -3 or i == 3 or j == -3 or j == 3):
                        for k in xrange(-2, y + 3):
                            if (x + i, k, z + j) not in self.model.world:
                                self.model.add_block((x + i, k , z + j), SAND)
                    if (x + i, y + 3, z + j) not in self.model.world:
                        self.model.add_block((x + i, y + 3, z + j), SAND)
            # check mob inside trap
            in_x, in_y, in_z = False, False, False
            if self.model.mob_x_position in xrange(x-3, x+4):
                in_x = True
            if self.model.mob_z_position in xrange(z-3, z+4):
                in_z = True
            if self.model.mob_y_position < y + 3:
                in_y = True
            drew_trap = True
            # if trapped, stop the mob from moving and attacking
            # and place blocks of health
            if in_x and in_y and in_z and drew_trap:
                self.model.trapped = True
                self.model.ai.status = False
                self.model.remove_block((self.model.mob_x_position,
                                         self.model.mob_y_position,
                                         self.model.mob_z_position))
                self.place_health()