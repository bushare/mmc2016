swig:
	swig -python sample_module.i

compile:
	g++ -fPIC -shared sample_module_wrap.c test.c -o _sample_module.so -I/usr/include/python2.7/ -lpython2.7

clean:
	rm *.pyc
	rm *_wrap.c
	rm *.so
