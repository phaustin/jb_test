# test builds for windows

```
conda env create -f environment.yml
conda activate june22
```

then:

```
cd multi_level
jupyter-build build toc
```

which produces the rendered html file at `toc/_build/html/index.html`
