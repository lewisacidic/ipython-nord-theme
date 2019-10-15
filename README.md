# ipython-nord-theme

An arctic, north-bluish theme for the IPython interactive prompt.


## Quickstart

To easily get the theme installed and loading at startup:

```shell
pip install ipython_nord_theme[hook]
python -m ipython_startup_hook.install
```


## Installation

Install using [`pip`](https://pip.pypa.io/en/stable/):

```shell
pip install ipython-nord-theme 
```

or with [`conda`](https://conda.io):

```shell
conda install -c lewisacidic ipython-nord-theme
```

## Usage

Load the theme with IPython magic:

```shell
%load_ext ipython_nord_theme
```

To set the theme back to what you had previously:

```shell
%unload_ext ipython_nord_theme
```


## Running this at startup

You can either put the following snippet in your IPython startup directory (usually `$HOME/.ipython/profile_default/startup`):

```shell
try:
    from ipython_nord_theme.startup import load
    load()
    del load  # don't pollute global namespace!!
except ModuleNotFoundError:
    pass
```

Or use [`ipython-startup-hook`](https://github.com/lewisacidic/ipython-startup-hook) (recommended if you use IPython within virtual environments).

This may be done at install with the command given in the [Quickstart](#quickstart).


## Development 

Create the conda environment:

```shell
conda env create -f envs/dev.yml
conda activate ipython-nord-theme-dev
```

Format code by running the pre-commit tasks:

```shell
pre-commit run --all
```

Run the tests with pytest (note we need to use `ipython` rather than `python` for these tests):

```shell
ipython -m pytest
```
