%module(package="pynusmv.nusmv.trans") trans

%{
#include "../../../nusmv/nusmv-config.h"
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/trans/trans.h" 
%}

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/trans/trans.h