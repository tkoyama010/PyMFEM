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
    from . import _fe_l2
else:
    import _fe_l2

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _fe_l2.SWIG_PyInstanceMethod_New
_swig_new_static_method = _fe_l2.SWIG_PyStaticMethod_New

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

import mfem._par.fe_h1
import mfem._par.fe_base
import mfem._par.intrules
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.geom
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.element
import mfem._par.globals
import mfem._par.table
import mfem._par.hash
class L2_SegmentElement(mfem._par.fe_base.NodalTensorFiniteElement):
    r"""Proxy of C++ mfem::L2_SegmentElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_SegmentElement self, int const p, int const btype=GaussLegendre) -> L2_SegmentElement"""
        _fe_l2.L2_SegmentElement_swiginit(self, _fe_l2.new_L2_SegmentElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_SegmentElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_SegmentElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_SegmentElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_SegmentElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_SegmentElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_SegmentElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2_SegmentElement self, int vertex, Vector dofs)"""
        return _fe_l2.L2_SegmentElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_l2.L2_SegmentElement_ProjectDelta)
    __swig_destroy__ = _fe_l2.delete_L2_SegmentElement

# Register L2_SegmentElement in _fe_l2:
_fe_l2.L2_SegmentElement_swigregister(L2_SegmentElement)

class L2_QuadrilateralElement(mfem._par.fe_base.NodalTensorFiniteElement):
    r"""Proxy of C++ mfem::L2_QuadrilateralElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_QuadrilateralElement self, int const p, int const btype=GaussLegendre) -> L2_QuadrilateralElement"""
        _fe_l2.L2_QuadrilateralElement_swiginit(self, _fe_l2.new_L2_QuadrilateralElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_QuadrilateralElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_QuadrilateralElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_QuadrilateralElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_QuadrilateralElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_QuadrilateralElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2_QuadrilateralElement self, int vertex, Vector dofs)"""
        return _fe_l2.L2_QuadrilateralElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_l2.L2_QuadrilateralElement_ProjectDelta)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(L2_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_l2.L2_QuadrilateralElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_l2.L2_QuadrilateralElement_ProjectCurl)
    __swig_destroy__ = _fe_l2.delete_L2_QuadrilateralElement

# Register L2_QuadrilateralElement in _fe_l2:
_fe_l2.L2_QuadrilateralElement_swigregister(L2_QuadrilateralElement)

class L2_HexahedronElement(mfem._par.fe_base.NodalTensorFiniteElement):
    r"""Proxy of C++ mfem::L2_HexahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_HexahedronElement self, int const p, int const btype=GaussLegendre) -> L2_HexahedronElement"""
        _fe_l2.L2_HexahedronElement_swiginit(self, _fe_l2.new_L2_HexahedronElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_HexahedronElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_HexahedronElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_HexahedronElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_HexahedronElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_HexahedronElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_HexahedronElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2_HexahedronElement self, int vertex, Vector dofs)"""
        return _fe_l2.L2_HexahedronElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_l2.L2_HexahedronElement_ProjectDelta)
    __swig_destroy__ = _fe_l2.delete_L2_HexahedronElement

# Register L2_HexahedronElement in _fe_l2:
_fe_l2.L2_HexahedronElement_swigregister(L2_HexahedronElement)

class L2_TriangleElement(mfem._par.fe_base.NodalFiniteElement):
    r"""Proxy of C++ mfem::L2_TriangleElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_TriangleElement self, int const p, int const btype=GaussLegendre) -> L2_TriangleElement"""
        _fe_l2.L2_TriangleElement_swiginit(self, _fe_l2.new_L2_TriangleElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_TriangleElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_TriangleElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_TriangleElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_TriangleElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_TriangleElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_TriangleElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2_TriangleElement self, int vertex, Vector dofs)"""
        return _fe_l2.L2_TriangleElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_l2.L2_TriangleElement_ProjectDelta)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(L2_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_l2.L2_TriangleElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_l2.L2_TriangleElement_ProjectCurl)
    __swig_destroy__ = _fe_l2.delete_L2_TriangleElement

# Register L2_TriangleElement in _fe_l2:
_fe_l2.L2_TriangleElement_swigregister(L2_TriangleElement)

class L2_TetrahedronElement(mfem._par.fe_base.NodalFiniteElement):
    r"""Proxy of C++ mfem::L2_TetrahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_TetrahedronElement self, int const p, int const btype=GaussLegendre) -> L2_TetrahedronElement"""
        _fe_l2.L2_TetrahedronElement_swiginit(self, _fe_l2.new_L2_TetrahedronElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_TetrahedronElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_TetrahedronElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_TetrahedronElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_TetrahedronElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_TetrahedronElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_TetrahedronElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2_TetrahedronElement self, int vertex, Vector dofs)"""
        return _fe_l2.L2_TetrahedronElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_l2.L2_TetrahedronElement_ProjectDelta)
    __swig_destroy__ = _fe_l2.delete_L2_TetrahedronElement

# Register L2_TetrahedronElement in _fe_l2:
_fe_l2.L2_TetrahedronElement_swigregister(L2_TetrahedronElement)

class L2_WedgeElement(mfem._par.fe_base.NodalFiniteElement):
    r"""Proxy of C++ mfem::L2_WedgeElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(L2_WedgeElement self, int const p, int const btype=GaussLegendre) -> L2_WedgeElement"""
        _fe_l2.L2_WedgeElement_swiginit(self, _fe_l2.new_L2_WedgeElement(*args, **kwargs))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2_WedgeElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_l2.L2_WedgeElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_l2.L2_WedgeElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2_WedgeElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_l2.L2_WedgeElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_l2.L2_WedgeElement_CalcDShape)
    __swig_destroy__ = _fe_l2.delete_L2_WedgeElement

# Register L2_WedgeElement in _fe_l2:
_fe_l2.L2_WedgeElement_swigregister(L2_WedgeElement)



