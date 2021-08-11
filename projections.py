#%%

import matplotlib.pyplot as plt

import cartopy.crs as ccrs


def tissot_perspective():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.NearsidePerspective(0, 40))
    
    ax.tissot(facecolor='red', alpha=.5)
    ax.stock_img()
    ax.coastlines()

    plt.show()


def tissot_mercator():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

    ax.set_extent((-80, 100, 0, 90))
    
    ax.tissot(facecolor='red', alpha=.5)

    ax.stock_img()
    ax.coastlines()

    plt.show()

def tissot_equirectangular():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    ax.set_extent((-80, 100, 0, 90))
    
    ax.tissot(facecolor='red', alpha=.5)

    ax.stock_img()
    ax.coastlines()

    plt.show()

def tissot_mollweide():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mollweide())

    ax.set_extent((-80, 100, 0, 90))
    
    ax.tissot(facecolor='red', alpha=.5)

    ax.stock_img()
    ax.coastlines()

    plt.show()


def tissot_goode_homolosine():
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.InterruptedGoodeHomolosine())

    # ax.set_extent((-80, 100, 0, 90))
    
    ax.tissot(facecolor='red', alpha=.5)

    ax.stock_img()
    ax.coastlines()

    plt.show()


# %%
