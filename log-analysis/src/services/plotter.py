import pandas as pd
import matplotlib.pyplot as plt

def plot_log_types(data:pd.Series):

    ax = data.plot(kind="bar")
    ax.set_title("Log Types")
    ax.set_xlabel("Level")
    ax.set_ylabel("Count")

    for container in ax.containers:
        ax.bar_label(container)

    plt.tight_layout()
    plt.show()

def plot_log_frequency(data:pd.Series):
    ax = data.plot(kind="bar", title="Log Frequency")
    ax.set_xlabel("Message")
    ax.set_ylabel("Count")

    for container in ax.containers:
        ax.bar_label(container)
    
    plt.tight_layout()
    plt.show()

def plot_log_by_date(data:pd.Series):

    ax = data.plot(title="Log Analyze")
    ax.set_xlabel("datetime")
    ax.set_ylabel("Count")

    plt.tight_layout()
    plt.show()