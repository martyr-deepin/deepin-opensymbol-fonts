# Makefile to create Multicoloure SVGinOT color font

# Where to find scfbuild?
BUILD := tools/svgs2ttf

.PHONY: all clean build

SRC := $(wildcard *.json)

all: build

build:
	mkdir -p build
	$(foreach var, $(SRC), $(BUILD) $(var);)

clean:
	-rm -rf build

