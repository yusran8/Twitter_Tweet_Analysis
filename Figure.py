from matplotlib import pyplot as plt
import pandas as pd

def create_bar(dataFrame, user):
    df = dataFrame.groupby(['created_at']).size().reset_index(name='tweets')
    date = df['created_at']
    max_tweets = df['tweets'].max()
 
    x=df['created_at']
    y=df['tweets']

    
    figx = plt.figure(figsize=(50,5))
    plt.bar(x, y, width=0.5)
    figx.suptitle('Persebaran Tweet @' + user, fontsize=20)
    plt.xlabel('Tanggal', fontsize=14)
    plt.ylabel('Jumlah Tweet', fontsize=14)
    
    # Show Plot
    plt.show()

#price = df['price'].head(12)


