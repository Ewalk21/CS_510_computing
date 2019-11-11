.PHONY : test clean

export CC = gcc
export CFLAGS = -Wall -O2
# Change to flags below for debugging with gdb
#export CFLAGS = -Wall -O0 -g

all:
	mkdir -p bin
	$(MAKE) -C src/

clean:
	$(MAKE) -C src/ clean

cleaner: clean
	rm -f bin/*
	$(MAKE) -C src/ cleaner