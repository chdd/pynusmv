%module(package="pynusmv.nusmv.addons_core") addons_core

%{
#include "../../../nusmv/nusmv-config.h"
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/addons_core/addonsCore.h" 
%}

%feature("autodoc", 1);

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/addons_core/addonsCore.h