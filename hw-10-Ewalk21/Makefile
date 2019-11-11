.PHONY : test clean
export CFLAGS = -Wall -O2
#export CFLAGS = -Wall -O0 -g

all:
	$(MAKE) -C src/
	$(MAKE) -C test/

test: 
	$(MAKE) -C test/ test

clean:
	$(MAKE) -C src/ clean
	$(MAKE) -C test/ clean

cleaner:
	$(MAKE) -C src/ cleaner
	$(MAKE) -C test/ cleaner
