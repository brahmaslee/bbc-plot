# bbc-matplotlib
A matplotlibrc file loosely based on [BBCplot](https://github.com/bbc/bbplot).

This stylesheet and example are distributed with [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt).

## Installation (?) Instructions
1. Determine your `matplotlib` configuration file path:

```
import matplotlib as mpl
print(mpl.get_configdir()) # Let's call this MPL_CONFIGDIR for now
```

2. `mkdir MPL_CONFIGDIR/stylelib`

3. Copy `bbc.mplstyle` to `MPL_CONFIGDIR/stylelib`

4. Use like any other stylesheet from `matplotlib`

```
import matplotlib.pyplot as plt
plt.style.use("bbc")
```

## Usage
See the example `plot.py` script and have fun!
