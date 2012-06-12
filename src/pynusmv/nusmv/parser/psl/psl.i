%module(package="pynusmv.nusmv.parser.psl") psl

%{
#include "../../../../nusmv/nusmv-config.h"
#include "../../../../nusmv/src/node/node.h"
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/parser/psl/pslExpr.h" 
#include "../../../../nusmv/src/parser/psl/pslNode.h"
#include "../../../../nusmv/src/parser/psl/psl_grammar.h" 
#include "../../../../nusmv/src/parser/psl/psl_symbols.h"  
%}

# Removing duplicate macros definition (token macros).
#pragma SWIG nowarn=302

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/parser/psl/pslExpr.h
%include ../../../../nusmv/src/parser/psl/pslNode.h
%include ../../../../nusmv/src/parser/psl/psl_grammar.h
%include ../../../../nusmv/src/parser/psl/psl_symbols.h