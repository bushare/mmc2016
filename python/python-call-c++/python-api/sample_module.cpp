#include <Python.h>


int func(int a)
{
    return a + 1;
}

static PyObject * _func(PyObject * self, PyObject * args)
{
     int _a;
     int res;
     if (!PyArg_ParseTuple(args, "i", &_a))
         return NULL;
     res = func(_a);
     return PyLong_FromLong(res);
}

static PyMethodDef GreateModuleMethods[] = {
    { "func", _func, METH_VARARGS, "" },
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initsample_module(void) {
    (void) Py_InitModule("sample_module", GreateModuleMethods);
}
// gcc -fPIC -shared mymodule_wrap.c -o _mymodule.so -I/usr/include/python2.7/ -lpython2.7
