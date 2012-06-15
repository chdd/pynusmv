%module(package="pynusmv.nusmv.addons_core.compass.parser.ap") ap

%{
#include "../../../../../../nusmv/nusmv-config.h"
#include "../../../../../../nusmv/src/node/node.h"
#include "../../../../../../nusmv/src/utils/defs.h"
#include "../../../../../../nusmv/src/addons_core/compass/parser/ap/ap_grammar.h" 
#include "../../../../../../nusmv/src/addons_core/compass/parser/ap/ParserAp.h" 
%}

# Removing warnings for redefined macros (TOK_X defined twice in ap_grammar)
#pragma SWIG nowarn=302

%feature("autodoc", 1);

%include ../../../../../../nusmv/src/utils/defs.h
%include ../../../../../../nusmv/src/addons_core/compass/parser/ap/ap_grammar.h
%include ../../../../../../nusmv/src/addons_core/compass/parser/ap/ParserAp.h