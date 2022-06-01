import numpy as np
from utils import * 
from threadSort import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp


def matplotValues(sortType,randArray):
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
    fig.canvas.set_window_title(sortType)
    rects = ax.bar(range(len(randArray)), randArray, align="edge",
                color=color_map(data_normalizer(range(len(randArray)))))
    ax.set_xlim(0, len(randArray))
    ax.set_ylim(0, int(1.1*len(randArray)))
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
    comparisons = [0]
    return fig, rects, comparisons, text


def animate(randArray, rects, comparisons, text):
    for rect, val in zip(rects, randArray):
        rect.set_height(val)

    comparisons[0] += 1
    text.set_text("Comparisons : {}".format(comparisons[0]))


def run():
    while True:
        sizeOfArray = input("Enter the size of the array larger then 0: ")
        if int(sizeOfArray) > 0:
            break
    randArray= np.random.randint(1,int(sizeOfArray),size=(int(sizeOfArray)))
    randArray2= randArray.copy()

    plt.style.use('fivethirtyeight')

    sortInsertion = insertion_sort_yeild(randArray)
    sortSelection = selection_sort_yeild(randArray2)

    fig, rects, comparisons, text = matplotValues('Insertion sort',randArray)
    fig2, rects2, comparisons2, text2 = matplotValues('Selection sort',randArray2)

    anim = FuncAnimation(fig, func=animate,
                        fargs=(rects, comparisons, text), frames=sortInsertion, interval=50,
                        repeat=False)

    anim2 = FuncAnimation(fig2, func=animate,
                        fargs=(rects2, comparisons2, text2), frames=sortSelection, interval=50,
                        repeat=False)

    plt.show()

            