#%%

import numpy as np
import matplotlib.pyplot as plt

class Chord():

    def __init__(self, th1=None, th2=None):
    
        self.th1 = th1
        self.th2 = th2
        
    @property
    def midpoint_r(self):
        delta_theta = np.abs(self.th1 - self.th2)
        return np.abs(np.cos(delta_theta / 2))
    
    @property
    def is_inside(self):
        return self.midpoint_r <= 1/2.

    @classmethod
    def from_angles(cls, th1=None, th2=None):
        if th1 is None:
            th1 = np.random.uniform(0, 2 * np.pi) 
        if th2 is None:
            th2 = np.random.uniform(0, 2 * np.pi) 
        return cls(th1, th2)
        
    @classmethod
    def from_midpoint_r(cls, r=None, th1=None):
        if r is None:
            r = np.random.uniform(0, 1)
        if th1 is None:
            th1 = np.random.uniform(0, 2 * np.pi)
        th2 = th1 + 2 * np.arccos(r)
        return cls(th1, th2)
        
    @classmethod
    def from_midpoint_xy(cls, x=None, y=None):
        if x is None and y is None:
            t = 2*np.pi*np.random.uniform()
            u = np.random.uniform()+np.random.uniform()
            r = 2-u if u>1 else u
            x = r*np.cos(t)
            y = r*np.sin(t)
            return cls.from_midpoint_r(r, t)
    
        r = np.sqrt(x**2 + y**2)
        th1 = np.arctan2(y, x)
        return cls.from_midpoint_r(r, th1)
        
class ChordCollection():
    
    def __init__(self, constructor, name=None, n_trials=int(5e2)):
        
        self.chords = [
            constructor()
            for _ in range(n_trials)
        ]
        self.name = name
    
    @property
    def midpoint_rs(self):
        return [chord.midpoint_r for chord in self.chords]
        
    @property
    def delta_thetas(self):
        return [(chord.th1 - chord.th2) % 2 * np.pi for chord in self.chords]
        
    @property
    def are_inside(self):
        return [chord.is_inside for chord in self.chords]
    
    @property
    def colors(self):
        
        color = lambda x : 'red' if x else 'black'
        
        return list(map(color, self.are_inside))
    
    @property
    def midpoint_xys(self):
        return (
            [(np.cos(chord.th1)+np.cos(chord.th2))/2 for chord in self.chords],
            [(np.sin(chord.th1)+np.sin(chord.th2))/2 for chord in self.chords])

    def plot_chords(self):
        for chord, color in zip(self.chords, self.colors):
            plt.plot(
                [np.cos(chord.th1), np.cos(chord.th2)],
                [np.sin(chord.th1), np.sin(chord.th2)],
                lw=.7,
                c=color,
                alpha=.5
                )
        angles = np.linspace(0, 2 * np.pi, num=100)
        plt.plot(np.cos(angles), np.sin(angles), lw=.8, c='black')
        plt.plot(.5*np.cos(angles), .5*np.sin(angles), ls='--', c='red', lw=.6)
        plt.gca().set_aspect('equal')
        plt.title(name)
    
    def plot_midpoints(self):
        plt.scatter(
            *self.midpoint_xys,
            c=self.colors,
            s=1.,
            alpha=.8
            )
        plt.gca().set_aspect('equal')
        plt.title(name)
        
    
    def plot_midpoints_kde(self):
        pass

    def histogram_midpoint(self):
        plt.hist(self.midpoint_rs, bins=100, density=True)
        plt.title(name)
        plt.xlabel('Raggio del punto medio')
        plt.ylabel('Conteggi normalizzati')

    def histogram_delta_theta(self):
        plt.hist(self.delta_thetas, bins=100, density=True)
        plt.title(name)
        plt.xlabel('$\\Delta \\theta$: distanza angolare fra gli estremi della corda')
        plt.ylabel('Conteggi normalizzati')

        
    def histogram_midpoint_normalized(self):
        plt.hist(self.midpoint_rs, bins=100, density=True, weights=
        [1 / r for r in self.midpoint_rs])
        plt.title(name)
        
    
    @property
    def fraction(self):
        return len(self.chords) / len([c for c in self.chords if c.is_inside])
    
#%%

constructors = {
    'Posizione degli estremi': Chord.from_angles,
    'Raggio del punto medio': Chord.from_midpoint_r,
    'Posizione del punto medio': Chord.from_midpoint_xy
}

#%%

for name, constructor in constructors.items():
    
    collection = ChordCollection(constructor, name=name, n_trials=int(3e3))
    collection.plot_midpoints()
    plt.tight_layout()
    plt.savefig(f'Scatterplot dei punti medi - {name}.png', facecolor='white', transparent=False, dpi=150)
    plt.show()


# %%

for name, constructor in constructors.items():
    
    collection = ChordCollection(constructor, name=name, n_trials=int(5e4))

    collection.histogram_midpoint()
    
    plt.tight_layout()
    plt.savefig(f'Istogramma dei punti medi - {name}.png', facecolor='white', transparent=False, dpi=150)
    plt.show()

# %%

for name, constructor in constructors.items():
    
    collection = ChordCollection(constructor, name=name, n_trials=int(5e4))

    collection.histogram_delta_theta()
    
    plt.tight_layout()
    plt.savefig(f'Istogramma delle distanze angolari - {name}.png', facecolor='white', transparent=False, dpi=150)
    plt.show()

# %%

for name, constructor in constructors.items():
    
    collection = ChordCollection(constructor, name=name, n_trials=int(2e2))

    collection.plot_chords()
    
    plt.show()

# %%

for name, constructor in constructors.items():
    
    collection = ChordCollection(constructor, name=name, n_trials=int(2e5))

    print(collection.fraction)
    
    plt.show()

# %%

collection = ChordCollection(Chord.from_midpoint_r, n_trials=6)
collection.plot_chords()
plt.title('')
plt.savefig('bertrand-chords.pdf', dpi=150)
# %%
