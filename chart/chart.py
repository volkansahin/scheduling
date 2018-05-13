import io

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator


class Chart:
    def __init__(self, result_path, image_path):
        self.result_path = result_path
        self.image_path = image_path

    def create_chart(self):
        df = pd.read_csv(io.StringIO(open(self.result_path).read()), header=None, names=["Process", "Start", "Finish"])
        df["Diff"] = df.Finish - df.Start

        fig, ax = plt.subplots(figsize=(15, 3))
        red_patch = mpatches.Patch(color='red', label='Execution')
        labels = []

        print(df)
        for i, process in enumerate(df.groupby("Process")):
            labels.append(process[0])
            data = process[1][["Start", "Diff"]]
            ax.broken_barh(data.values, ((len(process)-i) - 0.5, 1), color="red")

        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(reversed(labels))

        ax.xaxis.set_major_locator(MaxNLocator(40))
        ax.xaxis.grid(True, linestyle='-', which='major', color='grey', alpha=.25)
        ax.yaxis.grid(color='k', linestyle=':')

        ax.set_xlabel("time [ms]")
        plt.tight_layout()
        plt.legend(handles=[red_patch])
        plt.savefig(self.image_path)
        plt.show()
