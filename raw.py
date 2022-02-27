from base64 import b16decode
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

df = pd.read_csv('/Users/ljp2/trade/Data/bars1/20220204.csv', parse_dates=['time'], index_col=0)
width = (df.index[1] - df.index[0]) * 0.8
width2 = width * 0.2
col1 = 'green'
col2 = 'red'



fig, ax = plt.subplots(figsize=(16,8))
ax.set_xlim(left = df.index[0], right=df.index[-1])
ax.set_ylim(bottom=440, top=450)


def candles(i):
    xf = df.iloc[1: 20 + i]
    up = xf[xf.close>=xf.open]
    down = xf[xf.close<xf.open]

    b1 = ax.bar(up.index,up.close-up.open,width,bottom=up.open,color=col1)
    b2 = ax.bar(up.index,up.high-up.close,width2,bottom=up.close,color=col1)
    b3 = ax.bar(up.index,up.low-up.open,width2,bottom=up.open,color=col1)

    b4 = ax.bar(down.index,down.close-down.open,width,bottom=down.open,color=col2)
    b5 = ax.bar(down.index,down.high-down.open,width2,bottom=down.open,color=col2)
    b6 = ax.bar(down.index,down.low-down.close,width2,bottom=down.close,color=col2)



ani = animation.FuncAnimation(fig, candles, frames=20, interval=250)


plt.show()

