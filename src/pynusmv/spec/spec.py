from ..nusmv.parser import parser
from ..nusmv.node import node as nsnode

from ..utils.pointerwrapper import PointerWrapper


class Spec(PointerWrapper):
    """
    A specification stored as NuSMV nodes.
    
    The Spec class implements a NuSMV nodes-based specification.
    
    No check is made to insure that the node is effectively a specification,
    i.e. the stored pointer is not checked against spec types.
    
    Specs do not have to be freed.
    """
    
    def __init__(self, ptr, freeit = False):
        super().__init__(ptr, freeit = freeit)
        
        
    @property
    def type(self):
        """The type of this spec node."""
        return self._ptr.type
    
    @property
    def car(self):
        """The left Spec-typed child of this node."""
        left = nsnode.car(self._ptr)
        if left:
            return Spec(left, freeit = self._freeit)
        else:
            return None
        
    @property
    def cdr(self):
        """The right Spec-typed child of this node."""
        right = nsnode.cdr(self._ptr)
        if right:
            return Spec(right, freeit = self._freeit)
        else:
            return None
            
    def __str__(self):
        return nsnode.sprint_node(self._ptr)

    def __or__(self, other):
        if other is None:
            raise ValueError()
        return Spec(nsnode.find_node(parser.OR, self._ptr, other._ptr))
        
    def __and__(self, other):
        if other is None:
            raise ValueError()
        return Spec(nsnode.find_node(parser.AND, self._ptr, other._ptr))
        
    def __invert__(self):
        return Spec(nsnode.find_node(parser.NOT, self._ptr, None))
        

def true():
    """Return a new Spec corresponding to TRUE"""
    return Spec(nsnode.find_node(parser.TRUEEXP, None, None))
    

def false():
    """Return a new Spec corresponding to FALSE"""
    return Spec(nsnode.find_node(parser.FALSEEXP, None, None))
    
    
def nott(spec):
    """Return a new Spec corresponding to NOT spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.NOT, spec._ptr, None))
    

def andd(left, right):
    """Return a new Spec corresponding to left AND right"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AND, left._ptr, right._ptr))
    

def orr(left, right):
    """Return a new Spec corresponding to left OR right"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.OR, left._ptr, right._ptr))
       

def imply(left, right):
    """Return a new Spec corresponding to (left IMPLIES right)"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.IMPLIES, left._ptr, right._ptr))
    

def iff(left, right):
    """Return a new Spec corresponding to (left IFF right)"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.IFF, left._ptr, right._ptr))
    
    
def ex(spec):
    """Return a new Spec corresponding to EX spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.EX, spec._ptr, None))
    

def eg(spec):
    """Return a new Spec corresponding to EG spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.EG, spec._ptr, None))
    
    
def ef(spec):
    """Return a new Spec corresponding to EF spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.EF, spec._ptr, None))
    
    
def eu(left, right):
    """Return a new Spec corresponding to EU[left U right]"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.EU, left._ptr, right._ptr))
    
    
def ew(left, right):
    """Return a new Spec corresponding to EW[left U right]"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.EW, left._ptr, right._ptr))
    
    
def ax(spec):
    """Return a new Spec corresponding to AX spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AX, spec._ptr, None))
    

def ag(spec):
    """Return a new Spec corresponding to AG spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AG, spec._ptr, None))
    
    
def af(spec):
    """Return a new Spec corresponding to AF spec"""
    if spec is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AF, spec._ptr, None))
    
    
def au(left, right):
    """Return a new Spec corresponding to AU[left U right]"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AU, left._ptr, right._ptr))
    
    
def aw(left, right):
    """Return a new Spec corresponding to AW[left U right]"""
    if left is None or right is None:
        raise ValueError()
    return Spec(nsnode.find_node(parser.AW, left._ptr, right._ptr))


def atom(strrep):
    """
    Return a new Spec corresponding to the given atom.
    
    Parse strrep and provide a new Spec representing this atom.
    
    Throw a NuSMVParserError if strrep is not a valid atomic proposition.
    """
    # FIXME NuSMV abruptly exits when strrep is not an atomic proposition
    node, err = parser.ReadSimpExprFromString(strrep)
    if err:
        raise NuSMVParserError(strrep + " is not a valid atomic proposition.")
    return Spec(nsnode.car(node))
    
    

class NuSMVParserError(Exception):
    """An error occured while parsing a string with NUSMV."""