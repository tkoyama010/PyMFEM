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
    from . import _plinearform
else:
    import _plinearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _plinearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _plinearform.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _plinearform.MFEM_VERSION
MFEM_VERSION_STRING = _plinearform.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _plinearform.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _plinearform.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _plinearform.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _plinearform.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _plinearform.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _plinearform.MFEM_VERSION_PATCH
import mfem._par.linearform
import mfem._par.coefficient
import mfem._par.globals
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.matrix
import mfem._par.vector
import mfem._par.operators
import mfem._par.symmat
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.nonlininteg
import mfem._par.std_vectors
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.pgridfunc
class ParLinearForm(mfem._par.linearform.LinearForm):
    r"""Proxy of C++ mfem::ParLinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParLinearForm self) -> ParLinearForm
        __init__(ParLinearForm self, ParFiniteElementSpace pf) -> ParLinearForm
        __init__(ParLinearForm self, ParFiniteElementSpace pf, double * data) -> ParLinearForm
        __init__(ParLinearForm self, ParFiniteElementSpace pf, ParLinearForm plf) -> ParLinearForm
        """
        _plinearform.ParLinearForm_swiginit(self, _plinearform.new_ParLinearForm(*args))

    def ParFESpace(self):
        r"""ParFESpace(ParLinearForm self) -> ParFiniteElementSpace"""
        return _plinearform.ParLinearForm_ParFESpace(self)
    ParFESpace = _swig_new_instance_method(_plinearform.ParLinearForm_ParFESpace)

    def Update(self, *args):
        r"""
        Update(ParLinearForm self, ParFiniteElementSpace pf=None)
        Update(ParLinearForm self, ParFiniteElementSpace pf, Vector v, int v_offset)
        """
        return _plinearform.ParLinearForm_Update(self, *args)
    Update = _swig_new_instance_method(_plinearform.ParLinearForm_Update)

    def MakeRef(self, *args):
        r"""
        MakeRef(ParLinearForm self, FiniteElementSpace f, Vector v, int v_offset)
        MakeRef(ParLinearForm self, ParFiniteElementSpace pf, Vector v, int v_offset)
        """
        return _plinearform.ParLinearForm_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_plinearform.ParLinearForm_MakeRef)

    def Assemble(self):
        r"""Assemble(ParLinearForm self)"""
        return _plinearform.ParLinearForm_Assemble(self)
    Assemble = _swig_new_instance_method(_plinearform.ParLinearForm_Assemble)

    def AssembleSharedFaces(self):
        r"""AssembleSharedFaces(ParLinearForm self)"""
        return _plinearform.ParLinearForm_AssembleSharedFaces(self)
    AssembleSharedFaces = _swig_new_instance_method(_plinearform.ParLinearForm_AssembleSharedFaces)

    def ParallelAssemble(self, *args):
        r"""
        ParallelAssemble(ParLinearForm self, Vector tv)
        ParallelAssemble(ParLinearForm self) -> HypreParVector
        """
        return _plinearform.ParLinearForm_ParallelAssemble(self, *args)
    ParallelAssemble = _swig_new_instance_method(_plinearform.ParLinearForm_ParallelAssemble)

    def __call__(self, gf):
        r"""__call__(ParLinearForm self, ParGridFunction gf) -> double"""
        return _plinearform.ParLinearForm___call__(self, gf)
    __call__ = _swig_new_instance_method(_plinearform.ParLinearForm___call__)
    __swig_destroy__ = _plinearform.delete_ParLinearForm

# Register ParLinearForm in _plinearform:
_plinearform.ParLinearForm_swigregister(ParLinearForm)



