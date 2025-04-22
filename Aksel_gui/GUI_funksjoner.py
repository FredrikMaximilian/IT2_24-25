import io
import matplotlib.pyplot as plt
import pygame as pg
import numpy as np

def autopct_if_large(pct):
    return f"{pct:.0f}%" if pct > 4 else ""

def plott_graf(x, y, type, størrelse, x_tittel, y_tittel):

    buf = io.BytesIO()
    fig, ax = plt.subplots(figsize = størrelse)
    #ax.set_position

    if type == "Linje":

        ax.plot(x, y)
        ax.set_ylim(bottom = 0) #Juster slik nødvendig

    if type == "Bar":

        ax.bar(x, y) #Barh om det er knappt om plass
        ax.set_ylim(bottom = 0)

    if type == "Gruppert stolpediagram":

        offset = 0.2
        x_arr = np.arange(len(x))
        ax.barh(x_arr + offset, y[0], label = "Menn", height = offset * 2)
        ax.barh(x_arr - offset, y[1], label = "Kvinner", height = offset * 2)
        ax.set_yticks(x_arr)
        ax.set_yticklabels(x)
        ax.legend(loc = "upper right", fontsize = 8)
        
    if type == "Histogram":

        plt.hist(y, bins = 5)
    
    if type == "Sektor":

        fig, ax = plt.subplots(figsize = (12, 6)) # Se ann
        pie_resultat = ax.pie(y, autopct=autopct_if_large)

        if len(pie_resultat) == 3:
            wedges, texts, autotexts = pie_resultat
        else:
            wedges, texts = pie_resultat

        ax.legend(wedges, x, loc = "center left", bbox_to_anchor = (-1.1, 0.5), frameon=False, ncol = 4) #bbox_to_anchor=(-0.6, 0.5) syntaks plasser legend x, y. Bruk ncol = antall kolonner om det er lite plass
        ax.set_position([0.2, 0.5, 0.6, 0.6])  # Få posisjonen til å passe bedre. Syntaks: ax.set_position([left, bottom, width, height])
        ax.set_title(y_tittel)
    
    else: 
        ax.set_xlabel(x_tittel, fontsize = 12, labelpad = 13)
        ax.set_ylabel(y_tittel, fontsize = 12, labelpad = 13)
        
    plt.savefig(buf, format="PNG", bbox_inches = "tight")
    buf.seek(0)
    return pg.image.load(buf, ".png")
