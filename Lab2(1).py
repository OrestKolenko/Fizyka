import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_sinusoidal_wave(B, S, w):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = B * np.sin(S * x + w)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title('Sinusoidal Wave')

    return fig

def calculate_and_display_parameters(B, S, w):
    T = 2 * np.pi / w
    BSw = B * S * w
    neg_BSw = -BSw

    result_label.config(text=f'BSw = {BSw:.5f}, -BSw = {neg_BSw:.5f}, T = {T:.2f}')

    fig = plot_sinusoidal_wave(B, S, w)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def on_submit():
    B = float(B_entry.get())
    S = float(S_entry.get())
    w = float(w_entry.get())

    calculate_and_display_parameters(B, S, w)

root = tk.Tk()
root.title('Sinusoidal Wave')

input_frame = ttk.Frame(root, padding='10')
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.RIGHT, padx=10, pady=10)

B_label = ttk.Label(input_frame, text='B:')
B_label.grid(column=0, row=0, sticky=tk.W)
B_entry = ttk.Entry(input_frame)
B_entry.grid(column=1, row=0, sticky=tk.W)

S_label = ttk.Label(input_frame, text='S:')
S_label.grid(column=0, row=1, sticky=tk.W)
S_entry = ttk.Entry(input_frame)
S_entry.grid(column=1, row=1, sticky=tk.W)

w_label = ttk.Label(input_frame, text='w:')
w_label.grid(column=0, row=2, sticky=tk.W)
w_entry = ttk.Entry(input_frame)
w_entry.grid(column=1, row=2, sticky=tk.W)

submit_button = ttk.Button(input_frame, text='Plot Graph', command=on_submit)
submit_button.grid(column=0, row=3, columnspan=2, pady=10)

result_label = ttk.Label(input_frame, text='')
result_label.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
