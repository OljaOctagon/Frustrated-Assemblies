import numpy as np 
import seaborn as sns 
import mdtraj as md 
import matplotlib.pyplot as plt 
import argparse 
from matplotlib.patches import Wedge, Rectangle

def read_file(filen):
    particles = []
    with open(filen, "r") as flmp:
            collect_line =False
            for line in flmp.readlines():
                    
                if line.startswith("ITEM: TIMESTEP"):
                    collect_line=False 
                
                if collect_line == True:
                    entry = np.array([float(x) for x in line.split()])
                    particles[-1].append(entry)
                    
                if line.startswith("ITEM: ATOMS"):
                    collect_line=True
                    particles.append([])
                    
    return particles 


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", 
                        type=str, 
                        default="trajectory.lammpstrj")
    
    parser.add_argument("-l", type=float)
    args = parser.parse_args()

    frames = read_file(args.f)
    freq = 10
    boxl = float(args.l)
    radius=0.5/boxl
    pradius=0.025/boxl
    
    for j in range(len(frames)-1, len(frames),freq):
        print(j)
        frame = np.array(frames[j])
        c_part= frame[::5,2:4]*boxl
        p1_part = frame[1::5,2:4]*boxl
        p2_part = frame[2::5,2:4]*boxl
        p3_part = frame[3::5,2:4]*boxl
        p4_part = frame[4::5,2:4]*boxl
            
        fig, ax = plt.subplots(figsize=(20,20))
        ax.set_aspect('equal')

        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.axis("off")

        for i, center_i in enumerate(c_part):

            center = (center_i[0]/boxl,center_i[1]/boxl)  
            c = plt.Circle(center,
                            radius, 
                            color='#d0ccdb')  
            ax.add_patch(c) 
            
            p1_tuple = (p1_part[i,0]/boxl,p1_part[i,1]/boxl)
            p1 = plt.Circle(p1_tuple,
                            pradius, 
                            color='#f44336')  
            ax.add_patch(p1) 
            
            p2_tuple = (p2_part[i,0]/boxl,p2_part[i,1]/boxl)
            p2 = plt.Circle(p2_tuple,
                            pradius, 
                            color='#2986cc')  
            ax.add_patch(p2) 
            
            p3_tuple = (p3_part[i,0]/boxl,p3_part[i,1]/boxl)
            p3 = plt.Circle(p3_tuple,
                            pradius, 
                            color='#2986cc')  
            ax.add_patch(p3) 
            
            p4_tuple = (p4_part[i,0]/boxl,p4_part[i,1]/boxl)
            p4 = plt.Circle(p4_tuple,
                            pradius, 
                            color='#f44336')  
            ax.add_patch(p4) 
            
            
        plt.savefig("pngs/frame_{}.png".format(j),dpi=300)
        plt.savefig("pdfs/frame_{}.pdf".format(j))
        plt.close(fig)

  