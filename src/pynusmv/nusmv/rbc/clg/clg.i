%module(package="pynusmv.nusmv.rbc.clg") clg

%{
#include "../../../../nusmv/nusmv-config.h"
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/rbc/clg/clg.h" 
%}

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/rbc/clg/clg.h