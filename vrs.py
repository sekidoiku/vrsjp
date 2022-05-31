import requests,re
import pandas as pd
import matplotlib.pyplot as plt
import io

url = 'http://data.vrs.digital.go.jp/vaccination/opendata/latest/summary_by_date.csv'
r = requests.get(url).content

def main():
    df = pd.read_csv(io.BytesIO(r),sep=",")
    fig, ax1 = plt.subplots( )
    ax1.plot(df['date'],df['count_first_shot_general'],"b-")
    ax2 = ax1.twinx()
    ax2.plot(df['date'],df['count_second_shot_general'],"r-")
    ax3 = ax1.twinx()
    ax3.plot(df['date'],df['count_third_shot_general'],"g-")
    ax3.spines["right"].set_position(("axes", 1.2))
    ax1.set_xticks([])
    ax1.set_ylim(0,1500000)
    ax2.set_ylim(0,1500000)
    ax3.set_ylim(0,1500000)
    ax2.set_yticks([])
    ax3.set_yticks([])
    ax1.set_title('first_shot-blue,second_shot-red,third_shot-green')

    plt.savefig("vrs.png")
    plt.show()

if __name__ == "__main__":
    main()
