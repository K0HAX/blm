all:
	gcc -o blm blm.c -lsqlite3 -std=c99

clean:
	rm -vf blm
