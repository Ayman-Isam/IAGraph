import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 150, 0.1)
y1 = -310+5.24817521300686 * x
y2 = -200+5.83348110403927 * x
y3 = -350+12.5783393186096 * x
y4 = -150+1.79212582251241 * x
y5 = -660+21.6321234097324 * x
y6 = -700+29.909652748047 * x
y7 = -990+34.1542402012756 * x
y8 = -1010+30.3138007599191 * x
y9 = -1300+33.3625352293534 * x
y10 = -1400+51.6139559008127 * x


line1, = plt.plot(x, y1, label="Mediterranean Avenue", color="brown")
line2, = plt.plot(x, y2, label="Reading Railroad", color="gray")
line3, = plt.plot(x, y3, label="Vermont Avenue", color="pink")
line4, = plt.plot(x, y4, label="Electric Company", color="black")
line5, = plt.plot(x, y5, label="Virginia Avenue", color="pink")
line6, = plt.plot(x, y6, label="New York Avenue", color="orange")
line7, = plt.plot(x, y7, label="Illinois Avenue", color="red")
line8, = plt.plot(x, y8, label="Atlantic Avenue", color="yellow")
line9, = plt.plot(x, y9, label="Pacific Avenue", color="green")
line10, = plt.plot(x, y10, label="Boardwalk", color="blue")
line_extra, = plt.plot(x, np.zeros_like(x), label="Dotted Gray", linestyle="dotted", color="gray")

handles = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line_extra]
labels = (["Mediterranean Avenue", "Reading Railroad", "Vermont Avenue", " Electric Company", "Virginia Avenue", "New York Avenue", " Illinois Avenue", " Atlantic Avenue", "Pacific Avenue", " Boardwalk"])

plt.legend(handles, labels)

plt.title("Property Revenue and rolls")
plt.xlabel("Number of Opponent Rolls")
plt.ylabel("Net Profit")

plt.show()
