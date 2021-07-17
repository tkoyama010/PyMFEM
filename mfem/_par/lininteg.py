# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _lininteg
else:
    import _lininteg

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _lininteg.SWIG_PyInstanceMethod_New
_swig_new_static_method = _lininteg.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.fe
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.geom
import mfem._par.intrules
import mfem._par.densemat
import mfem._par.operators
import mfem._par.matrix
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.globals
import mfem._par.coefficient
class LinearFormIntegrator(object):
    r"""Proxy of C++ mfem::LinearFormIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(LinearFormIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(LinearFormIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(LinearFormIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.LinearFormIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.LinearFormIntegrator_AssembleRHSElementVect)

    def SetIntRule(self, ir):
        r"""SetIntRule(LinearFormIntegrator self, IntegrationRule ir)"""
        return _lininteg.LinearFormIntegrator_SetIntRule(self, ir)
    SetIntRule = _swig_new_instance_method(_lininteg.LinearFormIntegrator_SetIntRule)

    def GetIntRule(self):
        r"""GetIntRule(LinearFormIntegrator self) -> IntegrationRule"""
        return _lininteg.LinearFormIntegrator_GetIntRule(self)
    GetIntRule = _swig_new_instance_method(_lininteg.LinearFormIntegrator_GetIntRule)
    __swig_destroy__ = _lininteg.delete_LinearFormIntegrator

# Register LinearFormIntegrator in _lininteg:
_lininteg.LinearFormIntegrator_swigregister(LinearFormIntegrator)

class DeltaLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::DeltaLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def IsDelta(self):
        r"""IsDelta(DeltaLFIntegrator self) -> bool"""
        return _lininteg.DeltaLFIntegrator_IsDelta(self)
    IsDelta = _swig_new_instance_method(_lininteg.DeltaLFIntegrator_IsDelta)

    def GetDeltaCenter(self, center):
        r"""GetDeltaCenter(DeltaLFIntegrator self, Vector center)"""
        return _lininteg.DeltaLFIntegrator_GetDeltaCenter(self, center)
    GetDeltaCenter = _swig_new_instance_method(_lininteg.DeltaLFIntegrator_GetDeltaCenter)

    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(DeltaLFIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.DeltaLFIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.DeltaLFIntegrator_AssembleDeltaElementVect)
    __swig_destroy__ = _lininteg.delete_DeltaLFIntegrator

# Register DeltaLFIntegrator in _lininteg:
_lininteg.DeltaLFIntegrator_swigregister(DeltaLFIntegrator)

class DomainLFIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::DomainLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(DomainLFIntegrator self, Coefficient QF, int a=2, int b=0) -> DomainLFIntegrator
        __init__(DomainLFIntegrator self, Coefficient QF, IntegrationRule ir) -> DomainLFIntegrator
        """
        _lininteg.DomainLFIntegrator_swiginit(self, _lininteg.new_DomainLFIntegrator(*args))

        self._coeff = args




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(DomainLFIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.DomainLFIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.DomainLFIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(DomainLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(DomainLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(DomainLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.DomainLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.DomainLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_DomainLFIntegrator

# Register DomainLFIntegrator in _lininteg:
_lininteg.DomainLFIntegrator_swigregister(DomainLFIntegrator)

class DomainLFGradIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::DomainLFGradIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QF):
        r"""__init__(DomainLFGradIntegrator self, VectorCoefficient QF) -> DomainLFGradIntegrator"""
        _lininteg.DomainLFGradIntegrator_swiginit(self, _lininteg.new_DomainLFGradIntegrator(QF))

        self._coeff = QF




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(DomainLFGradIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.DomainLFGradIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.DomainLFGradIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(DomainLFGradIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(DomainLFGradIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(DomainLFGradIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.DomainLFGradIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.DomainLFGradIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_DomainLFGradIntegrator

# Register DomainLFGradIntegrator in _lininteg:
_lininteg.DomainLFGradIntegrator_swigregister(DomainLFGradIntegrator)

class BoundaryLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::BoundaryLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QG, a=1, b=1):
        r"""__init__(BoundaryLFIntegrator self, Coefficient QG, int a=1, int b=1) -> BoundaryLFIntegrator"""
        _lininteg.BoundaryLFIntegrator_swiginit(self, _lininteg.new_BoundaryLFIntegrator(QG, a, b))

        self._coeff = QG




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(BoundaryLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.BoundaryLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.BoundaryLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_BoundaryLFIntegrator

# Register BoundaryLFIntegrator in _lininteg:
_lininteg.BoundaryLFIntegrator_swigregister(BoundaryLFIntegrator)

class BoundaryNormalLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::BoundaryNormalLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QG, a=1, b=1):
        r"""__init__(BoundaryNormalLFIntegrator self, VectorCoefficient QG, int a=1, int b=1) -> BoundaryNormalLFIntegrator"""
        _lininteg.BoundaryNormalLFIntegrator_swiginit(self, _lininteg.new_BoundaryNormalLFIntegrator(QG, a, b))

        self._coeff = QG




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(BoundaryNormalLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryNormalLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryNormalLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.BoundaryNormalLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.BoundaryNormalLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_BoundaryNormalLFIntegrator

# Register BoundaryNormalLFIntegrator in _lininteg:
_lininteg.BoundaryNormalLFIntegrator_swigregister(BoundaryNormalLFIntegrator)

class BoundaryTangentialLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::BoundaryTangentialLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QG, a=1, b=1):
        r"""__init__(BoundaryTangentialLFIntegrator self, VectorCoefficient QG, int a=1, int b=1) -> BoundaryTangentialLFIntegrator"""
        _lininteg.BoundaryTangentialLFIntegrator_swiginit(self, _lininteg.new_BoundaryTangentialLFIntegrator(QG, a, b))

        self._coeff = QG




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(BoundaryTangentialLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryTangentialLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryTangentialLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.BoundaryTangentialLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.BoundaryTangentialLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_BoundaryTangentialLFIntegrator

# Register BoundaryTangentialLFIntegrator in _lininteg:
_lininteg.BoundaryTangentialLFIntegrator_swigregister(BoundaryTangentialLFIntegrator)

class VectorDomainLFIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::VectorDomainLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QF):
        r"""__init__(VectorDomainLFIntegrator self, VectorCoefficient QF) -> VectorDomainLFIntegrator"""
        _lininteg.VectorDomainLFIntegrator_swiginit(self, _lininteg.new_VectorDomainLFIntegrator(QF))

        self._coeff = QF




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(VectorDomainLFIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.VectorDomainLFIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.VectorDomainLFIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorDomainLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorDomainLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorDomainLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorDomainLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorDomainLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorDomainLFIntegrator

# Register VectorDomainLFIntegrator in _lininteg:
_lininteg.VectorDomainLFIntegrator_swigregister(VectorDomainLFIntegrator)

class VectorBoundaryLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorBoundaryLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QG):
        r"""__init__(VectorBoundaryLFIntegrator self, VectorCoefficient QG) -> VectorBoundaryLFIntegrator"""
        _lininteg.VectorBoundaryLFIntegrator_swiginit(self, _lininteg.new_VectorBoundaryLFIntegrator(QG))

        self._coeff = QG




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorBoundaryLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorBoundaryLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorBoundaryLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorBoundaryLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorBoundaryLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorBoundaryLFIntegrator

# Register VectorBoundaryLFIntegrator in _lininteg:
_lininteg.VectorBoundaryLFIntegrator_swigregister(VectorBoundaryLFIntegrator)

class VectorFEDomainLFIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::VectorFEDomainLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, F):
        r"""__init__(VectorFEDomainLFIntegrator self, VectorCoefficient F) -> VectorFEDomainLFIntegrator"""
        _lininteg.VectorFEDomainLFIntegrator_swiginit(self, _lininteg.new_VectorFEDomainLFIntegrator(F))

        self._coeff = F




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(VectorFEDomainLFIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.VectorFEDomainLFIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorFEDomainLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorFEDomainLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorFEDomainLFIntegrator

# Register VectorFEDomainLFIntegrator in _lininteg:
_lininteg.VectorFEDomainLFIntegrator_swigregister(VectorFEDomainLFIntegrator)

class VectorFEDomainLFCurlIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::VectorFEDomainLFCurlIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, F):
        r"""__init__(VectorFEDomainLFCurlIntegrator self, VectorCoefficient F) -> VectorFEDomainLFCurlIntegrator"""
        _lininteg.VectorFEDomainLFCurlIntegrator_swiginit(self, _lininteg.new_VectorFEDomainLFCurlIntegrator(F))

        self._coeff = F




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(VectorFEDomainLFCurlIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.VectorFEDomainLFCurlIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFCurlIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorFEDomainLFCurlIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFCurlIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFCurlIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorFEDomainLFCurlIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFCurlIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorFEDomainLFCurlIntegrator

# Register VectorFEDomainLFCurlIntegrator in _lininteg:
_lininteg.VectorFEDomainLFCurlIntegrator_swigregister(VectorFEDomainLFCurlIntegrator)

class VectorFEDomainLFDivIntegrator(DeltaLFIntegrator):
    r"""Proxy of C++ mfem::VectorFEDomainLFDivIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QF):
        r"""__init__(VectorFEDomainLFDivIntegrator self, Coefficient QF) -> VectorFEDomainLFDivIntegrator"""
        _lininteg.VectorFEDomainLFDivIntegrator_swiginit(self, _lininteg.new_VectorFEDomainLFDivIntegrator(QF))

        self._coeff = QF




    def AssembleDeltaElementVect(self, fe, Trans, elvect):
        r"""AssembleDeltaElementVect(VectorFEDomainLFDivIntegrator self, FiniteElement fe, ElementTransformation Trans, Vector elvect)"""
        return _lininteg.VectorFEDomainLFDivIntegrator_AssembleDeltaElementVect(self, fe, Trans, elvect)
    AssembleDeltaElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFDivIntegrator_AssembleDeltaElementVect)

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorFEDomainLFDivIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFDivIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEDomainLFDivIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorFEDomainLFDivIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorFEDomainLFDivIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorFEDomainLFDivIntegrator

# Register VectorFEDomainLFDivIntegrator in _lininteg:
_lininteg.VectorFEDomainLFDivIntegrator_swigregister(VectorFEDomainLFDivIntegrator)

class VectorBoundaryFluxLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorBoundaryFluxLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, f, s=1.0, ir=None):
        r"""__init__(VectorBoundaryFluxLFIntegrator self, Coefficient f, double s=1.0, IntegrationRule ir=None) -> VectorBoundaryFluxLFIntegrator"""
        _lininteg.VectorBoundaryFluxLFIntegrator_swiginit(self, _lininteg.new_VectorBoundaryFluxLFIntegrator(f, s, ir))

        self._coeff = (f, ir)




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorBoundaryFluxLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorBoundaryFluxLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorBoundaryFluxLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorBoundaryFluxLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorBoundaryFluxLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorBoundaryFluxLFIntegrator

# Register VectorBoundaryFluxLFIntegrator in _lininteg:
_lininteg.VectorBoundaryFluxLFIntegrator_swigregister(VectorBoundaryFluxLFIntegrator)

class VectorFEBoundaryFluxLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorFEBoundaryFluxLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(VectorFEBoundaryFluxLFIntegrator self, int a=1, int b=-1) -> VectorFEBoundaryFluxLFIntegrator
        __init__(VectorFEBoundaryFluxLFIntegrator self, Coefficient f, int a=2, int b=0) -> VectorFEBoundaryFluxLFIntegrator
        """
        _lininteg.VectorFEBoundaryFluxLFIntegrator_swiginit(self, _lininteg.new_VectorFEBoundaryFluxLFIntegrator(*args))

        self._coeff = args




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorFEBoundaryFluxLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEBoundaryFluxLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEBoundaryFluxLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorFEBoundaryFluxLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorFEBoundaryFluxLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorFEBoundaryFluxLFIntegrator

# Register VectorFEBoundaryFluxLFIntegrator in _lininteg:
_lininteg.VectorFEBoundaryFluxLFIntegrator_swigregister(VectorFEBoundaryFluxLFIntegrator)

class VectorFEBoundaryTangentLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorFEBoundaryTangentLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, QG, a=2, b=0):
        r"""__init__(VectorFEBoundaryTangentLFIntegrator self, VectorCoefficient QG, int a=2, int b=0) -> VectorFEBoundaryTangentLFIntegrator"""
        _lininteg.VectorFEBoundaryTangentLFIntegrator_swiginit(self, _lininteg.new_VectorFEBoundaryTangentLFIntegrator(QG, a, b))

        self._coeff = QG




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorFEBoundaryTangentLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEBoundaryTangentLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorFEBoundaryTangentLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.VectorFEBoundaryTangentLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorFEBoundaryTangentLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_VectorFEBoundaryTangentLFIntegrator

# Register VectorFEBoundaryTangentLFIntegrator in _lininteg:
_lininteg.VectorFEBoundaryTangentLFIntegrator_swigregister(VectorFEBoundaryTangentLFIntegrator)

class BoundaryFlowIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::BoundaryFlowIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(BoundaryFlowIntegrator self, Coefficient f_, VectorCoefficient u_, double a) -> BoundaryFlowIntegrator
        __init__(BoundaryFlowIntegrator self, Coefficient f_, VectorCoefficient u_, double a, double b) -> BoundaryFlowIntegrator
        """
        _lininteg.BoundaryFlowIntegrator_swiginit(self, _lininteg.new_BoundaryFlowIntegrator(*args))

        self._coeff = args




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(BoundaryFlowIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryFlowIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(BoundaryFlowIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.BoundaryFlowIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.BoundaryFlowIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_BoundaryFlowIntegrator

# Register BoundaryFlowIntegrator in _lininteg:
_lininteg.BoundaryFlowIntegrator_swigregister(BoundaryFlowIntegrator)

class DGDirichletLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::DGDirichletLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(DGDirichletLFIntegrator self, Coefficient u, double const s, double const k) -> DGDirichletLFIntegrator
        __init__(DGDirichletLFIntegrator self, Coefficient u, Coefficient q, double const s, double const k) -> DGDirichletLFIntegrator
        __init__(DGDirichletLFIntegrator self, Coefficient u, MatrixCoefficient q, double const s, double const k) -> DGDirichletLFIntegrator
        """
        _lininteg.DGDirichletLFIntegrator_swiginit(self, _lininteg.new_DGDirichletLFIntegrator(*args))

        self._coeff = args




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(DGDirichletLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(DGDirichletLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(DGDirichletLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.DGDirichletLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.DGDirichletLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_DGDirichletLFIntegrator

# Register DGDirichletLFIntegrator in _lininteg:
_lininteg.DGDirichletLFIntegrator_swigregister(DGDirichletLFIntegrator)

class DGElasticityDirichletLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::DGElasticityDirichletLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, uD_, lambda_, mu_, alpha_, kappa_):
        r"""__init__(DGElasticityDirichletLFIntegrator self, VectorCoefficient uD_, Coefficient lambda_, Coefficient mu_, double alpha_, double kappa_) -> DGElasticityDirichletLFIntegrator"""
        _lininteg.DGElasticityDirichletLFIntegrator_swiginit(self, _lininteg.new_DGElasticityDirichletLFIntegrator(uD_, lambda_, mu_, alpha_, kappa_))

        self._coeff = uD_




    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(DGElasticityDirichletLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(DGElasticityDirichletLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(DGElasticityDirichletLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        """
        return _lininteg.DGElasticityDirichletLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.DGElasticityDirichletLFIntegrator_AssembleRHSElementVect)
    __swig_destroy__ = _lininteg.delete_DGElasticityDirichletLFIntegrator

# Register DGElasticityDirichletLFIntegrator in _lininteg:
_lininteg.DGElasticityDirichletLFIntegrator_swigregister(DGElasticityDirichletLFIntegrator)

class VectorQuadratureLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorQuadratureLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(VectorQuadratureLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(VectorQuadratureLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorQuadratureLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(VectorQuadratureLFIntegrator self, FiniteElement fe, ElementTransformation Tr, Vector elvect)
        """
        return _lininteg.VectorQuadratureLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.VectorQuadratureLFIntegrator_AssembleRHSElementVect)

    def SetIntRule(self, ir):
        r"""SetIntRule(VectorQuadratureLFIntegrator self, IntegrationRule ir)"""
        return _lininteg.VectorQuadratureLFIntegrator_SetIntRule(self, ir)
    SetIntRule = _swig_new_instance_method(_lininteg.VectorQuadratureLFIntegrator_SetIntRule)
    __swig_destroy__ = _lininteg.delete_VectorQuadratureLFIntegrator

# Register VectorQuadratureLFIntegrator in _lininteg:
_lininteg.VectorQuadratureLFIntegrator_swigregister(VectorQuadratureLFIntegrator)

class QuadratureLFIntegrator(LinearFormIntegrator):
    r"""Proxy of C++ mfem::QuadratureLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def AssembleRHSElementVect(self, *args):
        r"""
        AssembleRHSElementVect(QuadratureLFIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elvect)
        AssembleRHSElementVect(QuadratureLFIntegrator self, FiniteElement el, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(QuadratureLFIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elvect)
        AssembleRHSElementVect(QuadratureLFIntegrator self, FiniteElement fe, ElementTransformation Tr, Vector elvect)
        """
        return _lininteg.QuadratureLFIntegrator_AssembleRHSElementVect(self, *args)
    AssembleRHSElementVect = _swig_new_instance_method(_lininteg.QuadratureLFIntegrator_AssembleRHSElementVect)

    def SetIntRule(self, ir):
        r"""SetIntRule(QuadratureLFIntegrator self, IntegrationRule ir)"""
        return _lininteg.QuadratureLFIntegrator_SetIntRule(self, ir)
    SetIntRule = _swig_new_instance_method(_lininteg.QuadratureLFIntegrator_SetIntRule)
    __swig_destroy__ = _lininteg.delete_QuadratureLFIntegrator

# Register QuadratureLFIntegrator in _lininteg:
_lininteg.QuadratureLFIntegrator_swigregister(QuadratureLFIntegrator)



