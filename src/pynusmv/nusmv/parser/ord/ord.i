%module(package="pynusmv.nusmv.parser.ord") ord

%{
#include "../../../../nusmv/nusmv-config.h"
#include "../../../../nusmv/src/node/node.h"
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/parser/ord/ord_grammar.h"
#include "../../../../nusmv/src/parser/ord/ParserOrd.h" 
%}

# Removing duplicate macros definition (TOK_X macros).
#pragma SWIG nowarn=302

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/parser/ord/ord_grammar.h
%include ../../../../nusmv/src/parser/ord/ParserOrd.h