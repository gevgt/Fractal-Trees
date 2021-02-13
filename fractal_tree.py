import numpy as np
from matplotlib import pyplot as plt
import math
import time


class fractal_tree:
    
    def __init__(self, height, angle, depth):
        self.height = height
        self.angle = angle
        self.depth = depth
        self.liste = []
        self.leaves = []
        
    
    def rotation(self, d):
        d = 2*math.pi/360*d
        r = np.array([[math.cos(d), math.sin(d)], 
                       [-math.sin(d), math.cos(d)]])
        return r
    
    
    def trunk(self):
        trunk = [[0,0], [0, 0 + self.height]]
        self.liste.append(trunk)
        return trunk
    
    
    def branch(self, v, trunk, angle):
        b = np.matmul(self.rotation(angle), v) * self.height
        branch_x = [trunk[0][1], b[0]+trunk[0][1]]
        branch_y = [trunk[1][1], b[1]+trunk[1][1]]
        b = [branch_x, branch_y]
        return b

    
    def branches(self, trunk, i):
        if i > 0:
            v = np.array([trunk[0][1]-trunk[0][0], trunk[1][1]-trunk[1][0]])
            
            # Right Branch
            b_right = self.branch(v, trunk, self.angle)
            self.liste.append(b_right)
            
            # Left Branch
            b_left = self.branch(v, trunk, -self.angle)
            self.liste.append(b_left)
            
            # Recursion
            self.branches(b_left, i-1)
            self.branches(b_right, i-1)
            
            # Leaves
            if self.depth == 10 and i == 1:
                self.leaves.append([b_right[0], b_right[1]])
                self.leaves.append([b_left[0], b_left[1]])   
        else:
            return
    

    def plot(self):
        fig, ax = plt.subplots(figsize=(10, 8))

        # Plotting Branches
        for l in self.liste:
            plt.plot(l[0], l[1], color="#3D2C0F")
        
        # Plotting Leaves
        for l in self.leaves:
            plt.scatter(l[0], l[1], color="#3E5722")

        # Settings for the Plot
        plt.axis('off') 
        plt.xlim(-2.5,2.5)
        plt.ylim(0,4) 
        name = "Heigth: " + str(self.height) + ", Angle: " + str(self.angle) + ", Depth: " + str(self.depth)
        plt.title(name)
        plt.show()
        

    def main(self):
        y = self.trunk()
        self.branches(y, self.depth)
        self.plot()





if __name__ == '__main__':
	for d in range(1,11):
	    x = fractal_tree(0.8, 20, d)
	    time.sleep(0.5)
	    x.main()