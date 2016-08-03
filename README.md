# Deepin OpenSymbol fonts
Deepin OpenSymbol fonts, a replacement for MS Wingdings font family.

## Build Dependencies
* **fontforge** with python support
* python3

## Build and Install
Just run `make` to generate fonts

### Addtion infomation
* extract svg from ttf

````
      fontforge -lang=ff -c 'Open($1); SelectWorthOutputting(); foreach Export("svg"); endloop;' font.ttf
```

* use `tools/parser_wingdings.py` to generate glyphs maps
