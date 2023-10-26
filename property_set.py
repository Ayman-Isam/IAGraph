import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 150, 0.1)
y1 = -310+5.24817521300686 * x + -310+9.58916962773444 * x
y2 = -350+12.2469482444426 * x + -350+12.5783393186096 * x + -370+13.6269605537099 * x
y3 = -640+19.9959297519734 * x + -640+17.4317461697178 * x + -660+21.6321234097324 * x
y4 = -680+25.6910927192504 * x + -680+26.9832899891725 * x + -700+29.909652748047 * x
y5 = -970+28.9452083163005 * x + -970+28.007892123482 * x + -990+34.1542402012756 * x
y6 = -1010+30.3138007599191 * x + -1010+30.0092963712245 * x + -1030+30.2846558524396 * x
y7 = -1300+33.3625352293534 * x + -1300+32.7074107064555 * x + -1320+34.2314708677966 * x
y8 = -1350+32.194945677992 * x + -1400+51.6139559008127 * x
y9 = -150+1.79212582251241 * x + -150+1.91627397508691 * x
y10 = -200+4.76540358421452 * x + -200+5.96778651022566 * x + -200+5.68573852663659 * x + -200+5.83348110403927 * x


line1, = plt.plot(x, y1, label="Brown", color="brown")
line2, = plt.plot(x, y2, label="Light Blue", color="lightblue")
line3, = plt.plot(x, y3, label="Pink", color="pink")
line4, = plt.plot(x, y4, label="Orange", color="orange")
line5, = plt.plot(x, y5, label="Red", color="red")
line6, = plt.plot(x, y6, label="Yellow", color="yellow")
line7, = plt.plot(x, y7, label="Green", color="green")
line8, = plt.plot(x, y8, label="Navy Blue", color="blue")
line9, = plt.plot(x, y9, label="Utility", color="black")
line10, = plt.plot(x, y10, label="Railway", color="gray")
line_extra, = plt.plot(x, np.zeros_like(x), label="Dotted Gray", linestyle="dotted", color="gray")

handles = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line_extra]
labels = ["Brown", "Light Blue", "Pink", "Orange", "Red", "Yellow", "Green", "Navy Blue", "Utility", "Railway"]

plt.legend(handles, labels)

plt.title("Property Revenue and rolls")
plt.xlabel("Number of Rolls")
plt.ylabel("Net Profit")

plt.show()
