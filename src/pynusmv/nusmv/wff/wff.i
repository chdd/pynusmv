%module(package="pynusmv.nusmv.wff") wff

%{
#include "../../../nusmv/nusmv-config.h"
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/wff/wff.h" 
%}

%feature("autodoc", 1);

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/wff/wff.h