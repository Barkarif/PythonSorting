import numpy as np
from utils import * 
from threadSort import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp



def run():
    while True:
        sizeOfArray = input("Enter the size of the array larger then 0: ")
        if int(sizeOfArray) > 0:
            break
    randArray= np.random.randint(1,int(sizeOfArray),size=(int(sizeOfArray)))
    randArray2= randArray.copy()

    plt.style.use('fivethirtyeight')


    sort1 = insertion_sort(randArray)
    sort2 = selection_sort(randArray2)

    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 0.50, 0.5),
                    (1.0, 0, 0)],
            "green": [(0, 0.7, 0.7),
                    (1.0, 0, 0)],
            "blue": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
        }
    )


    fig, ax = plt.subplots()
    fig.canvas.set_window_title('insertion_sort')
    fig2, ax2 = plt.subplots()
    fig2.canvas.set_window_title('selection_sort')

    rects = ax.bar(range(len(randArray)), randArray, align="edge",
                color=color_map(data_normalizer(range(len(randArray)))))

    rects2 = ax2.bar(range(len(randArray2)), randArray2, align="edge",
                color=color_map(data_normalizer(range(len(randArray2)))))

    ax.set_xlim(0, len(randArray))
    ax.set_ylim(0, int(1.1*len(randArray)))

    ax2.set_xlim(0, len(randArray2))
    ax2.set_ylim(0, int(1.1*len(randArray2)))

    text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    text2 = ax2.text(0.01, 0.95, "", transform=ax2.transAxes)
    iteration2 = [0]
    def animate(randArray, rects, iteration, text):

        for rect, val in zip(rects, randArray):
            rect.set_height(val)

        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))


    anim = FuncAnimation(fig, func=animate,
                        fargs=(rects, iteration,text), frames=sort1, interval=50,
                        repeat=False)


    anim2 = FuncAnimation(fig2, func=animate,
                        fargs=(rects2, iteration2,text2), frames=sort2, interval=50,
                        repeat=False)

    plt.show()

            