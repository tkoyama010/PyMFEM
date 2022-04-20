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
    from . import _schwarz
else:
    import _schwarz

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _schwarz.SWIG_PyInstanceMethod_New
_swig_new_static_method = _schwarz.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _schwarz.MFEM_VERSION
MFEM_VERSION_STRING = _schwarz.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _schwarz.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _schwarz.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _schwarz.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _schwarz.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _schwarz.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _schwarz.MFEM_VERSION_PATCH
import mfem._par.element
import mfem._par.globals
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.coefficient
import mfem._par.symmat
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.pgridfunc
import mfem._par.pfespace
import mfem._par.fespace
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.std_vectors
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.complex_operator

def is_a_patch(iv, patch_ids):
    r"""is_a_patch(int iv, intArray patch_ids) -> bool"""
    return _schwarz.is_a_patch(iv, patch_ids)
is_a_patch = _schwarz.is_a_patch

def owned(tdof, offs):
    r"""owned(int tdof, int * offs) -> bool"""
    return _schwarz.owned(tdof, offs)
owned = _schwarz.owned

def GetLocalRestriction(tdof_i, row_start, num_rows, num_cols):
    r"""GetLocalRestriction(intArray tdof_i, int const * row_start, int num_rows, int num_cols) -> SparseMatrix"""
    return _schwarz.GetLocalRestriction(tdof_i, row_start, num_rows, num_cols)
GetLocalRestriction = _schwarz.GetLocalRestriction

def GetLocal2GlobalMap(tdof_i, row_start, num_rows, num_cols, l2gmap):
    r"""GetLocal2GlobalMap(intArray tdof_i, int const * row_start, int num_rows, int num_cols, intArray l2gmap)"""
    return _schwarz.GetLocal2GlobalMap(tdof_i, row_start, num_rows, num_cols, l2gmap)
GetLocal2GlobalMap = _schwarz.GetLocal2GlobalMap

def GetOffdColumnValues(tdof_i, tdof_j, offd, cmap, row_start, PatchMat):
    r"""GetOffdColumnValues(intArray tdof_i, intArray tdof_j, SparseMatrix offd, int const * cmap, int const * row_start, SparseMatrix PatchMat)"""
    return _schwarz.GetOffdColumnValues(tdof_i, tdof_j, offd, cmap, row_start, PatchMat)
GetOffdColumnValues = _schwarz.GetOffdColumnValues

def GetArrayIntersection(A, B, C):
    r"""GetArrayIntersection(intArray A, intArray B, intArray C)"""
    return _schwarz.GetArrayIntersection(A, B, C)
GetArrayIntersection = _schwarz.GetArrayIntersection

def GetNumColumns(tdof_i, tdof_j, diag, offd, cmap, row_start):
    r"""GetNumColumns(int const tdof_i, intArray tdof_j, SparseMatrix diag, SparseMatrix offd, int const * cmap, int const * row_start) -> int"""
    return _schwarz.GetNumColumns(tdof_i, tdof_j, diag, offd, cmap, row_start)
GetNumColumns = _schwarz.GetNumColumns

def GetColumnValues(tdof_i, tdof_j, diag, offd, cmap, row_start, cols, vals):
    r"""GetColumnValues(int tdof_i, intArray tdof_j, SparseMatrix diag, SparseMatrix offd, int const * cmap, int const * row_start, intArray cols, doubleArray vals)"""
    return _schwarz.GetColumnValues(tdof_i, tdof_j, diag, offd, cmap, row_start, cols, vals)
GetColumnValues = _schwarz.GetColumnValues
class VertexPatchInfo(object):
    r"""Proxy of C++ VertexPatchInfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    mynrpatch = property(_schwarz.VertexPatchInfo_mynrpatch_get, _schwarz.VertexPatchInfo_mynrpatch_set, doc=r"""mynrpatch : int""")
    nrpatch = property(_schwarz.VertexPatchInfo_nrpatch_get, _schwarz.VertexPatchInfo_nrpatch_set, doc=r"""nrpatch : int""")
    vert_contr = property(_schwarz.VertexPatchInfo_vert_contr_get, _schwarz.VertexPatchInfo_vert_contr_set, doc=r"""vert_contr : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    edge_contr = property(_schwarz.VertexPatchInfo_edge_contr_get, _schwarz.VertexPatchInfo_edge_contr_set, doc=r"""edge_contr : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    face_contr = property(_schwarz.VertexPatchInfo_face_contr_get, _schwarz.VertexPatchInfo_face_contr_set, doc=r"""face_contr : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    elem_contr = property(_schwarz.VertexPatchInfo_elem_contr_get, _schwarz.VertexPatchInfo_elem_contr_set, doc=r"""elem_contr : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    host_rank = property(_schwarz.VertexPatchInfo_host_rank_get, _schwarz.VertexPatchInfo_host_rank_set, doc=r"""host_rank : mfem::Array<(int)>""")
    patch_natural_order_idx = property(_schwarz.VertexPatchInfo_patch_natural_order_idx_get, _schwarz.VertexPatchInfo_patch_natural_order_idx_set, doc=r"""patch_natural_order_idx : mfem::Array<(int)>""")
    patch_global_dofs_ids = property(_schwarz.VertexPatchInfo_patch_global_dofs_ids_get, _schwarz.VertexPatchInfo_patch_global_dofs_ids_set, doc=r"""patch_global_dofs_ids : mfem::Array<(int)>""")

    def __init__(self, pmesh_, ref_levels_):
        r"""__init__(VertexPatchInfo self, ParMesh pmesh_, int ref_levels_) -> VertexPatchInfo"""
        _schwarz.VertexPatchInfo_swiginit(self, _schwarz.new_VertexPatchInfo(pmesh_, ref_levels_))
    __swig_destroy__ = _schwarz.delete_VertexPatchInfo

# Register VertexPatchInfo in _schwarz:
_schwarz.VertexPatchInfo_swigregister(VertexPatchInfo)

class PatchDofInfo(object):
    r"""Proxy of C++ PatchDofInfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    comm = property(_schwarz.PatchDofInfo_comm_get, _schwarz.PatchDofInfo_comm_set, doc=r"""comm : MPI_Comm""")
    nrpatch = property(_schwarz.PatchDofInfo_nrpatch_get, _schwarz.PatchDofInfo_nrpatch_set, doc=r"""nrpatch : int""")
    host_rank = property(_schwarz.PatchDofInfo_host_rank_get, _schwarz.PatchDofInfo_host_rank_set, doc=r"""host_rank : mfem::Array<(int)>""")
    patch_tdofs = property(_schwarz.PatchDofInfo_patch_tdofs_get, _schwarz.PatchDofInfo_patch_tdofs_set, doc=r"""patch_tdofs : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    patch_local_tdofs = property(_schwarz.PatchDofInfo_patch_local_tdofs_get, _schwarz.PatchDofInfo_patch_local_tdofs_set, doc=r"""patch_local_tdofs : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")

    def __init__(self, cpmesh_, ref_levels_, fespace):
        r"""__init__(PatchDofInfo self, ParMesh cpmesh_, int ref_levels_, ParFiniteElementSpace fespace) -> PatchDofInfo"""
        _schwarz.PatchDofInfo_swiginit(self, _schwarz.new_PatchDofInfo(cpmesh_, ref_levels_, fespace))
    __swig_destroy__ = _schwarz.delete_PatchDofInfo

# Register PatchDofInfo in _schwarz:
_schwarz.PatchDofInfo_swigregister(PatchDofInfo)

class PatchAssembly(object):
    r"""Proxy of C++ PatchAssembly class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    comm = property(_schwarz.PatchAssembly_comm_get, _schwarz.PatchAssembly_comm_set, doc=r"""comm : MPI_Comm""")
    nrpatch = property(_schwarz.PatchAssembly_nrpatch_get, _schwarz.PatchAssembly_nrpatch_set, doc=r"""nrpatch : int""")
    tdof_offsets = property(_schwarz.PatchAssembly_tdof_offsets_get, _schwarz.PatchAssembly_tdof_offsets_set, doc=r"""tdof_offsets : std::vector<(int,std::allocator<(int)>)>""")
    patch_other_tdofs = property(_schwarz.PatchAssembly_patch_other_tdofs_get, _schwarz.PatchAssembly_patch_other_tdofs_set, doc=r"""patch_other_tdofs : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    patch_owned_other_tdofs = property(_schwarz.PatchAssembly_patch_owned_other_tdofs_get, _schwarz.PatchAssembly_patch_owned_other_tdofs_set, doc=r"""patch_owned_other_tdofs : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    l2gmaps = property(_schwarz.PatchAssembly_l2gmaps_get, _schwarz.PatchAssembly_l2gmaps_set, doc=r"""l2gmaps : std::vector<(mfem::Array<(int)>,std::allocator<(mfem::Array<(int)>)>)>""")
    PatchMat = property(_schwarz.PatchAssembly_PatchMat_get, _schwarz.PatchAssembly_PatchMat_set, doc=r"""PatchMat : mfem::Array<(p.mfem::SparseMatrix)>""")
    patch_tdof_info = property(_schwarz.PatchAssembly_patch_tdof_info_get, _schwarz.PatchAssembly_patch_tdof_info_set, doc=r"""patch_tdof_info : p.PatchDofInfo""")
    host_rank = property(_schwarz.PatchAssembly_host_rank_get, _schwarz.PatchAssembly_host_rank_set, doc=r"""host_rank : mfem::Array<(int)>""")
    A = property(_schwarz.PatchAssembly_A_get, _schwarz.PatchAssembly_A_set, doc=r"""A : p.mfem::HypreParMatrix""")

    def get_rank(self, tdof):
        r"""get_rank(PatchAssembly self, int tdof) -> int"""
        return _schwarz.PatchAssembly_get_rank(self, tdof)
    get_rank = _swig_new_instance_method(_schwarz.PatchAssembly_get_rank)

    def __init__(self, cpmesh_, ref_levels_, fespace_, A_):
        r"""__init__(PatchAssembly self, ParMesh cpmesh_, int ref_levels_, ParFiniteElementSpace fespace_, HypreParMatrix A_) -> PatchAssembly"""
        _schwarz.PatchAssembly_swiginit(self, _schwarz.new_PatchAssembly(cpmesh_, ref_levels_, fespace_, A_))
    __swig_destroy__ = _schwarz.delete_PatchAssembly

# Register PatchAssembly in _schwarz:
_schwarz.PatchAssembly_swigregister(PatchAssembly)

class PatchRestriction(object):
    r"""Proxy of C++ PatchRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, P_):
        r"""__init__(PatchRestriction self, PatchAssembly P_) -> PatchRestriction"""
        _schwarz.PatchRestriction_swiginit(self, _schwarz.new_PatchRestriction(P_))

    def Mult(self, r, res):
        r"""Mult(PatchRestriction self, Vector r, mfem::Array< BlockVector * > & res)"""
        return _schwarz.PatchRestriction_Mult(self, r, res)
    Mult = _swig_new_instance_method(_schwarz.PatchRestriction_Mult)

    def MultTranspose(self, sol, z):
        r"""MultTranspose(PatchRestriction self, mfem::Array< BlockVector * > const & sol, Vector z)"""
        return _schwarz.PatchRestriction_MultTranspose(self, sol, z)
    MultTranspose = _swig_new_instance_method(_schwarz.PatchRestriction_MultTranspose)
    __swig_destroy__ = _schwarz.delete_PatchRestriction

# Register PatchRestriction in _schwarz:
_schwarz.PatchRestriction_swigregister(PatchRestriction)

class SchwarzSmoother(mfem._par.operators.Solver):
    r"""Proxy of C++ SchwarzSmoother class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, cpmesh_, ref_levels_, fespace_, A_):
        r"""__init__(SchwarzSmoother self, ParMesh cpmesh_, int ref_levels_, ParFiniteElementSpace fespace_, HypreParMatrix A_) -> SchwarzSmoother"""
        _schwarz.SchwarzSmoother_swiginit(self, _schwarz.new_SchwarzSmoother(cpmesh_, ref_levels_, fespace_, A_))

    def SetNumSmoothSteps(self, iter):
        r"""SetNumSmoothSteps(SchwarzSmoother self, int const iter)"""
        return _schwarz.SchwarzSmoother_SetNumSmoothSteps(self, iter)
    SetNumSmoothSteps = _swig_new_instance_method(_schwarz.SchwarzSmoother_SetNumSmoothSteps)

    def SetDumpingParam(self, dump_param):
        r"""SetDumpingParam(SchwarzSmoother self, double const dump_param)"""
        return _schwarz.SchwarzSmoother_SetDumpingParam(self, dump_param)
    SetDumpingParam = _swig_new_instance_method(_schwarz.SchwarzSmoother_SetDumpingParam)

    def SetOperator(self, op):
        r"""SetOperator(SchwarzSmoother self, Operator op)"""
        return _schwarz.SchwarzSmoother_SetOperator(self, op)
    SetOperator = _swig_new_instance_method(_schwarz.SchwarzSmoother_SetOperator)

    def Mult(self, r, z):
        r"""Mult(SchwarzSmoother self, Vector r, Vector z)"""
        return _schwarz.SchwarzSmoother_Mult(self, r, z)
    Mult = _swig_new_instance_method(_schwarz.SchwarzSmoother_Mult)
    __swig_destroy__ = _schwarz.delete_SchwarzSmoother

# Register SchwarzSmoother in _schwarz:
_schwarz.SchwarzSmoother_swigregister(SchwarzSmoother)

class ComplexSchwarzSmoother(mfem._par.operators.Solver):
    r"""Proxy of C++ ComplexSchwarzSmoother class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, cpmesh_, ref_levels_, fespace_, A_):
        r"""__init__(ComplexSchwarzSmoother self, ParMesh cpmesh_, int ref_levels_, ParFiniteElementSpace fespace_, ComplexHypreParMatrix A_) -> ComplexSchwarzSmoother"""
        _schwarz.ComplexSchwarzSmoother_swiginit(self, _schwarz.new_ComplexSchwarzSmoother(cpmesh_, ref_levels_, fespace_, A_))

    def SetNumSmoothSteps(self, iter):
        r"""SetNumSmoothSteps(ComplexSchwarzSmoother self, int const iter)"""
        return _schwarz.ComplexSchwarzSmoother_SetNumSmoothSteps(self, iter)
    SetNumSmoothSteps = _swig_new_instance_method(_schwarz.ComplexSchwarzSmoother_SetNumSmoothSteps)

    def SetDumpingParam(self, dump_param):
        r"""SetDumpingParam(ComplexSchwarzSmoother self, double const dump_param)"""
        return _schwarz.ComplexSchwarzSmoother_SetDumpingParam(self, dump_param)
    SetDumpingParam = _swig_new_instance_method(_schwarz.ComplexSchwarzSmoother_SetDumpingParam)

    def SetOperator(self, op):
        r"""SetOperator(ComplexSchwarzSmoother self, Operator op)"""
        return _schwarz.ComplexSchwarzSmoother_SetOperator(self, op)
    SetOperator = _swig_new_instance_method(_schwarz.ComplexSchwarzSmoother_SetOperator)

    def Mult(self, r, z):
        r"""Mult(ComplexSchwarzSmoother self, Vector r, Vector z)"""
        return _schwarz.ComplexSchwarzSmoother_Mult(self, r, z)
    Mult = _swig_new_instance_method(_schwarz.ComplexSchwarzSmoother_Mult)
    __swig_destroy__ = _schwarz.delete_ComplexSchwarzSmoother

# Register ComplexSchwarzSmoother in _schwarz:
_schwarz.ComplexSchwarzSmoother_swigregister(ComplexSchwarzSmoother)



