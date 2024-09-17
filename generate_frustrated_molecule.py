import argparse 
from jinja2 import Environment, FileSystemLoader
import numpy as np 
parser = argparse.ArgumentParser()

parser.add_argument("-beta1", type=float)
parser.add_argument("-beta2", type=float)

args = parser.parse_args()

beta1 = float(args.beta1)
beta2 = float(args.beta2)

sigma = 1.0
r = sigma / 2

alpha1 = np.pi/2 - beta1*np.pi/180
alpha2 = np.pi/2 - beta2*np.pi/180

x1 = np.cos(alpha1)/r 
y1 = np.sin(alpha1)/r 

x2 = np.cos(alpha2)/r
y2 = np.sin(alpha2)/r

npart=5
pos = np.zeros((npart,3))
pos[1,:] = np.array([-x1,y2,0])
pos[2,:] = np.array([x1,y1,0])
pos[3,:] = np.array([x2,y2,0])
pos[4,:] = np.array([-x2,y2,0])

print(pos)
ptype = np.array([1,2,2,3,3])

atoms=[]
types=[]
for pid in range (1,npart+1):
    print(pid)
    print(pos[pid-1])
    atom_pos = {
        "id": pid,
        "x": pos[pid-1,0],
        "y": pos[pid-1,1],
        "z": pos[pid-1,2],
    }
    atoms.append(atom_pos)
    
    type = {
        "id": pid,
        "type": ptype[pid-1]}

    types.append(type)
    
context = {
    "number_of_atoms": npart,
}
context["atoms"] = atoms
context["types"] = types 

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("starting_template.txt")

filename = "patchy_start.txt"
with open(filename, mode="w") as output:
    output.write(template.render(context))

