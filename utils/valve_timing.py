"""
ToDo:
- plot in/close by scatter
- plot line within two points
- arrange in/ex plot height
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import matplotlib.pyplot as plt

from libs.vlv import VLV 

def plot_base_timing(vlv, ax, xmin=0, xmax=720, ymin=-5, ymax=10, xtick_step=90):
    ax.scatter(vlv.ivo_base, 0, marker="|", color="k")
    ax.scatter(vlv.ivc_base, 0, marker="|", color="k")
    ax.scatter(vlv.evo_base, 0, marker="|", color="k")
    ax.scatter(vlv.evc_base, 0, marker="|", color="k")

    ax.text(vlv.ivo_base, -2, "IVO")
    ax.text(vlv.ivc_base, -2, "IVC")
    ax.text(vlv.evo_base, -2, "EVO")
    ax.text(vlv.evc_base, -2.5, "EVC")

    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.plot(range(xmin, xmax), [0 for i in range(xmin, xmax)], color="k")

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    ax.set_xticks(range(xmin, xmax, xtick_step))

v = VLV()
fig = plt.figure()
ax = plt.subplot()
plot_base_timing(v, ax)

v1_h = VLV()
v1_l = VLV()
v2_h = VLV()
v2_l = VLV()

v1_h.add(ivo=-55, ivc=35, evo=50, evc=0)
v1_l.add(ivo=-35, ivc=45, evo=45, evc=-10)
v2_h.add(ivo=-40, ivc=45, evo=35, evc=-15)
v2_l.add(ivo=-25, ivc=40, evo=25, evc=-20)

for i, vlv_list in enumerate([[v1_h, v1_l], [v2_h, v2_l]]):
    if i == 0:
        m = "o"
    elif i == 1:
        m = "^"
    ax.plot([vlv_list[0].ivo, vlv_list[0].ivc], [(i+1)*3, (i+1)*3], "-"+m, color="blue", label="vlv" + str(i) + "_h_in")
    ax.plot([vlv_list[0].evo, vlv_list[0].evc], [(i+1)*3, (i+1)*3], "-"+m, color="red", label="vlv" + str(i) + "_h_ex")
    ax.plot([vlv_list[1].ivo, vlv_list[1].ivc], [(i+1)*2.5, (i+1)*2.5], "--"+m, color="blue", label="vlv" + str(i) + "_l_in")
    ax.plot([vlv_list[1].evo, vlv_list[1].evc], [(i+1)*2.5, (i+1)*2.5], "--"+m, color="red", label="vlv" + str(i) + "_l_ex")
 
plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0, fontsize=8)
plt.show()