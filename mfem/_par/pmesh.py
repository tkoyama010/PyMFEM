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
    from . import _pmesh
else:
    import _pmesh

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _pmesh.SWIG_PyInstanceMethod_New
_swig_new_static_method = _pmesh.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _pmesh.MFEM_VERSION

MFEM_VERSION_STRING = _pmesh.MFEM_VERSION_STRING

MFEM_VERSION_TYPE = _pmesh.MFEM_VERSION_TYPE

MFEM_VERSION_TYPE_RELEASE = _pmesh.MFEM_VERSION_TYPE_RELEASE

MFEM_VERSION_TYPE_DEVELOPMENT = _pmesh.MFEM_VERSION_TYPE_DEVELOPMENT

MFEM_VERSION_MAJOR = _pmesh.MFEM_VERSION_MAJOR

MFEM_VERSION_MINOR = _pmesh.MFEM_VERSION_MINOR

MFEM_VERSION_PATCH = _pmesh.MFEM_VERSION_PATCH

import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.globals
import mfem._par.vtk
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
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
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.std_vectors
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParMesh(mfem._par.mesh.Mesh):
    r"""Proxy of C++ mfem::ParMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParMesh self) -> ParMesh
        __init__(ParMesh self, MPI_Comm comm, Mesh mesh, int * partitioning_=None, int part_method=1) -> ParMesh
        __init__(ParMesh self, ParMesh pmesh, bool copy_nodes=True) -> ParMesh
        __init__(ParMesh self, MPI_Comm comm, std::istream & input, bool refine=True) -> ParMesh
        __init__(ParMesh self, ParMesh orig_mesh, int ref_factor, int ref_type) -> ParMesh
        __init__(ParMesh self, ParMesh mesh) -> ParMesh
        """
        _pmesh.ParMesh_swiginit(self, _pmesh.new_ParMesh(*args))

    @staticmethod
    def MakeRefined(orig_mesh, ref_factor, ref_type):
        r"""MakeRefined(ParMesh orig_mesh, int ref_factor, int ref_type) -> ParMesh"""
        return _pmesh.ParMesh_MakeRefined(orig_mesh, ref_factor, ref_type)
    MakeRefined = _swig_new_static_method(_pmesh.ParMesh_MakeRefined)

    @staticmethod
    def MakeSimplicial(orig_mesh):
        r"""MakeSimplicial(ParMesh orig_mesh) -> ParMesh"""
        return _pmesh.ParMesh_MakeSimplicial(orig_mesh)
    MakeSimplicial = _swig_new_static_method(_pmesh.ParMesh_MakeSimplicial)

    def Finalize(self, refine=False, fix_orientation=False):
        r"""Finalize(ParMesh self, bool refine=False, bool fix_orientation=False)"""
        return _pmesh.ParMesh_Finalize(self, refine, fix_orientation)
    Finalize = _swig_new_instance_method(_pmesh.ParMesh_Finalize)

    def SetAttributes(self):
        r"""SetAttributes(ParMesh self)"""
        return _pmesh.ParMesh_SetAttributes(self)
    SetAttributes = _swig_new_instance_method(_pmesh.ParMesh_SetAttributes)

    def HasBoundaryElements(self):
        r"""HasBoundaryElements(ParMesh self) -> bool"""
        return _pmesh.ParMesh_HasBoundaryElements(self)
    HasBoundaryElements = _swig_new_instance_method(_pmesh.ParMesh_HasBoundaryElements)

    def GetComm(self):
        r"""GetComm(ParMesh self) -> MPI_Comm"""
        return _pmesh.ParMesh_GetComm(self)
    GetComm = _swig_new_instance_method(_pmesh.ParMesh_GetComm)

    def GetNRanks(self):
        r"""GetNRanks(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNRanks(self)
    GetNRanks = _swig_new_instance_method(_pmesh.ParMesh_GetNRanks)

    def GetMyRank(self):
        r"""GetMyRank(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetMyRank(self)
    GetMyRank = _swig_new_instance_method(_pmesh.ParMesh_GetMyRank)

    def GetLocalElementNum(self, global_element_num):
        r"""GetLocalElementNum(ParMesh self, long global_element_num) -> int"""
        return _pmesh.ParMesh_GetLocalElementNum(self, global_element_num)
    GetLocalElementNum = _swig_new_instance_method(_pmesh.ParMesh_GetLocalElementNum)

    def GetGlobalElementNum(self, local_element_num):
        r"""GetGlobalElementNum(ParMesh self, int local_element_num) -> long"""
        return _pmesh.ParMesh_GetGlobalElementNum(self, local_element_num)
    GetGlobalElementNum = _swig_new_instance_method(_pmesh.ParMesh_GetGlobalElementNum)

    def GetGlobalVertexIndices(self, gi):
        r"""GetGlobalVertexIndices(ParMesh self, intArray gi)"""
        return _pmesh.ParMesh_GetGlobalVertexIndices(self, gi)
    GetGlobalVertexIndices = _swig_new_instance_method(_pmesh.ParMesh_GetGlobalVertexIndices)

    def GetGlobalEdgeIndices(self, gi):
        r"""GetGlobalEdgeIndices(ParMesh self, intArray gi)"""
        return _pmesh.ParMesh_GetGlobalEdgeIndices(self, gi)
    GetGlobalEdgeIndices = _swig_new_instance_method(_pmesh.ParMesh_GetGlobalEdgeIndices)

    def GetGlobalFaceIndices(self, gi):
        r"""GetGlobalFaceIndices(ParMesh self, intArray gi)"""
        return _pmesh.ParMesh_GetGlobalFaceIndices(self, gi)
    GetGlobalFaceIndices = _swig_new_instance_method(_pmesh.ParMesh_GetGlobalFaceIndices)

    def GetGlobalElementIndices(self, gi):
        r"""GetGlobalElementIndices(ParMesh self, intArray gi)"""
        return _pmesh.ParMesh_GetGlobalElementIndices(self, gi)
    GetGlobalElementIndices = _swig_new_instance_method(_pmesh.ParMesh_GetGlobalElementIndices)
    gtopo = property(_pmesh.ParMesh_gtopo_get, doc=r"""gtopo : mfem::GroupTopology""")
    have_face_nbr_data = property(_pmesh.ParMesh_have_face_nbr_data_get, _pmesh.ParMesh_have_face_nbr_data_set, doc=r"""have_face_nbr_data : bool""")
    face_nbr_group = property(_pmesh.ParMesh_face_nbr_group_get, _pmesh.ParMesh_face_nbr_group_set, doc=r"""face_nbr_group : mfem::Array<(int)>""")
    face_nbr_elements_offset = property(_pmesh.ParMesh_face_nbr_elements_offset_get, _pmesh.ParMesh_face_nbr_elements_offset_set, doc=r"""face_nbr_elements_offset : mfem::Array<(int)>""")
    face_nbr_vertices_offset = property(_pmesh.ParMesh_face_nbr_vertices_offset_get, _pmesh.ParMesh_face_nbr_vertices_offset_set, doc=r"""face_nbr_vertices_offset : mfem::Array<(int)>""")
    face_nbr_elements = property(_pmesh.ParMesh_face_nbr_elements_get, doc=r"""face_nbr_elements : mfem::Array<(p.mfem::Element)>""")
    face_nbr_vertices = property(_pmesh.ParMesh_face_nbr_vertices_get, doc=r"""face_nbr_vertices : mfem::Array<(mfem::Vertex)>""")
    send_face_nbr_elements = property(_pmesh.ParMesh_send_face_nbr_elements_get, _pmesh.ParMesh_send_face_nbr_elements_set, doc=r"""send_face_nbr_elements : mfem::Table""")
    send_face_nbr_vertices = property(_pmesh.ParMesh_send_face_nbr_vertices_get, _pmesh.ParMesh_send_face_nbr_vertices_set, doc=r"""send_face_nbr_vertices : mfem::Table""")
    pncmesh = property(_pmesh.ParMesh_pncmesh_get, _pmesh.ParMesh_pncmesh_set, doc=r"""pncmesh : p.mfem::ParNCMesh""")

    def GetNGroups(self):
        r"""GetNGroups(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNGroups(self)
    GetNGroups = _swig_new_instance_method(_pmesh.ParMesh_GetNGroups)

    def GroupNVertices(self, group):
        r"""GroupNVertices(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNVertices(self, group)
    GroupNVertices = _swig_new_instance_method(_pmesh.ParMesh_GroupNVertices)

    def GroupNEdges(self, group):
        r"""GroupNEdges(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNEdges(self, group)
    GroupNEdges = _swig_new_instance_method(_pmesh.ParMesh_GroupNEdges)

    def GroupNTriangles(self, group):
        r"""GroupNTriangles(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNTriangles(self, group)
    GroupNTriangles = _swig_new_instance_method(_pmesh.ParMesh_GroupNTriangles)

    def GroupNQuadrilaterals(self, group):
        r"""GroupNQuadrilaterals(ParMesh self, int group) -> int"""
        return _pmesh.ParMesh_GroupNQuadrilaterals(self, group)
    GroupNQuadrilaterals = _swig_new_instance_method(_pmesh.ParMesh_GroupNQuadrilaterals)

    def GroupVertex(self, group, i):
        r"""GroupVertex(ParMesh self, int group, int i) -> int"""
        return _pmesh.ParMesh_GroupVertex(self, group, i)
    GroupVertex = _swig_new_instance_method(_pmesh.ParMesh_GroupVertex)

    def GroupEdge(self, group, i, *args):
        if len(args) == 0:
            from mfem.par import intp  
            edge = intp()
            o = intp()  
            _pmesh.ParMesh_GroupEdge(self, group, i, edge, o)
            return edge.value(), o.value()
        else:
            return _pmesh.ParMesh_GroupEdge(self, group, i, *args)      



    def GroupTriangle(self, group, i, face, o):
        r"""GroupTriangle(ParMesh self, int group, int i, int & face, int & o)"""
        return _pmesh.ParMesh_GroupTriangle(self, group, i, face, o)
    GroupTriangle = _swig_new_instance_method(_pmesh.ParMesh_GroupTriangle)

    def GroupQuadrilateral(self, group, i, face, o):
        r"""GroupQuadrilateral(ParMesh self, int group, int i, int & face, int & o)"""
        return _pmesh.ParMesh_GroupQuadrilateral(self, group, i, face, o)
    GroupQuadrilateral = _swig_new_instance_method(_pmesh.ParMesh_GroupQuadrilateral)

    def GenerateOffsets(self, N, loc_sizes, offsets):
        r"""GenerateOffsets(ParMesh self, int N, HYPRE_BigInt [] loc_sizes, mfem::Array< HYPRE_BigInt > *[] offsets)"""
        return _pmesh.ParMesh_GenerateOffsets(self, N, loc_sizes, offsets)
    GenerateOffsets = _swig_new_instance_method(_pmesh.ParMesh_GenerateOffsets)

    def ExchangeFaceNbrData(self):
        r"""ExchangeFaceNbrData(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrData(self)
    ExchangeFaceNbrData = _swig_new_instance_method(_pmesh.ParMesh_ExchangeFaceNbrData)

    def ExchangeFaceNbrNodes(self):
        r"""ExchangeFaceNbrNodes(ParMesh self)"""
        return _pmesh.ParMesh_ExchangeFaceNbrNodes(self)
    ExchangeFaceNbrNodes = _swig_new_instance_method(_pmesh.ParMesh_ExchangeFaceNbrNodes)

    def SetCurvature(self, order, discont=False, space_dim=-1, ordering=1):
        r"""SetCurvature(ParMesh self, int order, bool discont=False, int space_dim=-1, int ordering=1)"""
        return _pmesh.ParMesh_SetCurvature(self, order, discont, space_dim, ordering)
    SetCurvature = _swig_new_instance_method(_pmesh.ParMesh_SetCurvature)

    def GetNFaceNeighbors(self):
        r"""GetNFaceNeighbors(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNFaceNeighbors(self)
    GetNFaceNeighbors = _swig_new_instance_method(_pmesh.ParMesh_GetNFaceNeighbors)

    def GetNFaceNeighborElements(self):
        r"""GetNFaceNeighborElements(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNFaceNeighborElements(self)
    GetNFaceNeighborElements = _swig_new_instance_method(_pmesh.ParMesh_GetNFaceNeighborElements)

    def GetFaceNbrGroup(self, fn):
        r"""GetFaceNbrGroup(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrGroup(self, fn)
    GetFaceNbrGroup = _swig_new_instance_method(_pmesh.ParMesh_GetFaceNbrGroup)

    def GetFaceNbrRank(self, fn):
        r"""GetFaceNbrRank(ParMesh self, int fn) -> int"""
        return _pmesh.ParMesh_GetFaceNbrRank(self, fn)
    GetFaceNbrRank = _swig_new_instance_method(_pmesh.ParMesh_GetFaceNbrRank)

    def GetFaceNbrElementFaces(self, i, fcs, cor):
        r"""GetFaceNbrElementFaces(ParMesh self, int i, intArray fcs, intArray cor)"""
        return _pmesh.ParMesh_GetFaceNbrElementFaces(self, i, fcs, cor)
    GetFaceNbrElementFaces = _swig_new_instance_method(_pmesh.ParMesh_GetFaceNbrElementFaces)

    def GetFaceToAllElementTable(self):
        r"""GetFaceToAllElementTable(ParMesh self) -> Table"""
        return _pmesh.ParMesh_GetFaceToAllElementTable(self)
    GetFaceToAllElementTable = _swig_new_instance_method(_pmesh.ParMesh_GetFaceToAllElementTable)

    def GetFaceElementTransformations(self, FaceNo, mask=31):
        r"""GetFaceElementTransformations(ParMesh self, int FaceNo, int mask=31) -> FaceElementTransformations"""
        return _pmesh.ParMesh_GetFaceElementTransformations(self, FaceNo, mask)
    GetFaceElementTransformations = _swig_new_instance_method(_pmesh.ParMesh_GetFaceElementTransformations)

    def GetSharedFaceTransformations(self, sf, fill2=True):
        r"""GetSharedFaceTransformations(ParMesh self, int sf, bool fill2=True) -> FaceElementTransformations"""
        return _pmesh.ParMesh_GetSharedFaceTransformations(self, sf, fill2)
    GetSharedFaceTransformations = _swig_new_instance_method(_pmesh.ParMesh_GetSharedFaceTransformations)

    def GetSharedFaceTransformationsByLocalIndex(self, FaceNo, fill2=True):
        r"""GetSharedFaceTransformationsByLocalIndex(ParMesh self, int FaceNo, bool fill2=True) -> FaceElementTransformations"""
        return _pmesh.ParMesh_GetSharedFaceTransformationsByLocalIndex(self, FaceNo, fill2)
    GetSharedFaceTransformationsByLocalIndex = _swig_new_instance_method(_pmesh.ParMesh_GetSharedFaceTransformationsByLocalIndex)

    def GetFaceNbrElementTransformation(self, i):
        r"""GetFaceNbrElementTransformation(ParMesh self, int i) -> ElementTransformation"""
        return _pmesh.ParMesh_GetFaceNbrElementTransformation(self, i)
    GetFaceNbrElementTransformation = _swig_new_instance_method(_pmesh.ParMesh_GetFaceNbrElementTransformation)

    def GetFaceNbrElementSize(self, i, type=0):
        r"""GetFaceNbrElementSize(ParMesh self, int i, int type=0) -> double"""
        return _pmesh.ParMesh_GetFaceNbrElementSize(self, i, type)
    GetFaceNbrElementSize = _swig_new_instance_method(_pmesh.ParMesh_GetFaceNbrElementSize)

    def GetNSharedFaces(self):
        r"""GetNSharedFaces(ParMesh self) -> int"""
        return _pmesh.ParMesh_GetNSharedFaces(self)
    GetNSharedFaces = _swig_new_instance_method(_pmesh.ParMesh_GetNSharedFaces)

    def GetSharedFace(self, sface):
        r"""GetSharedFace(ParMesh self, int sface) -> int"""
        return _pmesh.ParMesh_GetSharedFace(self, sface)
    GetSharedFace = _swig_new_instance_method(_pmesh.ParMesh_GetSharedFace)

    def GetNFbyType(self, type):
        r"""GetNFbyType(ParMesh self, mfem::FaceType type) -> int"""
        return _pmesh.ParMesh_GetNFbyType(self, type)
    GetNFbyType = _swig_new_instance_method(_pmesh.ParMesh_GetNFbyType)

    def ReorientTetMesh(self):
        r"""ReorientTetMesh(ParMesh self)"""
        return _pmesh.ParMesh_ReorientTetMesh(self)
    ReorientTetMesh = _swig_new_instance_method(_pmesh.ParMesh_ReorientTetMesh)

    def ReduceInt(self, value):
        r"""ReduceInt(ParMesh self, int value) -> long"""
        return _pmesh.ParMesh_ReduceInt(self, value)
    ReduceInt = _swig_new_instance_method(_pmesh.ParMesh_ReduceInt)

    def Rebalance(self, *args):
        r"""
        Rebalance(ParMesh self)
        Rebalance(ParMesh self, intArray partition)
        """
        return _pmesh.ParMesh_Rebalance(self, *args)
    Rebalance = _swig_new_instance_method(_pmesh.ParMesh_Rebalance)

    def Save(self, fname, precision=16):
        r"""Save(ParMesh self, char const * fname, int precision=16)"""
        return _pmesh.ParMesh_Save(self, fname, precision)
    Save = _swig_new_instance_method(_pmesh.ParMesh_Save)

    def SaveAsOne(self, fname, precision=16):
        r"""SaveAsOne(ParMesh self, char const * fname, int precision=16)"""
        return _pmesh.ParMesh_SaveAsOne(self, fname, precision)
    SaveAsOne = _swig_new_instance_method(_pmesh.ParMesh_SaveAsOne)

    def PrintVTU(self, *args, **kwargs):
        r"""PrintVTU(ParMesh self, std::string pathname, mfem::VTKFormat format=ASCII, bool high_order_output=False, int compression_level=0, bool bdr=False)"""
        return _pmesh.ParMesh_PrintVTU(self, *args, **kwargs)
    PrintVTU = _swig_new_instance_method(_pmesh.ParMesh_PrintVTU)

    def Load(self, input, generate_edges=0, refine=1, fix_orientation=True):
        r"""Load(ParMesh self, std::istream & input, int generate_edges=0, int refine=1, bool fix_orientation=True)"""
        return _pmesh.ParMesh_Load(self, input, generate_edges, refine, fix_orientation)
    Load = _swig_new_instance_method(_pmesh.ParMesh_Load)

    def GetBoundingBox(self, ref = 2):
        from  .vector import Vector
        min = Vector()
        max = Vector()      
        _pmesh.ParMesh_GetBoundingBox(self, min, max, ref)      
        return min.GetDataArray().copy(), max.GetDataArray().copy()



    def GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max):
        r"""GetCharacteristics(ParMesh self, double & h_min, double & h_max, double & kappa_min, double & kappa_max)"""
        return _pmesh.ParMesh_GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max)
    GetCharacteristics = _swig_new_instance_method(_pmesh.ParMesh_GetCharacteristics)

    def Swap(self, other):
        r"""Swap(ParMesh self, ParMesh other)"""
        return _pmesh.ParMesh_Swap(self, other)
    Swap = _swig_new_instance_method(_pmesh.ParMesh_Swap)

    def FindPoints(self, pp, warn=True, inv_trans=None):            
        r"""count, element_id, integration_points = FindPoints(points, warn=True, int_trans=None)"""
        import numpy as np
        import mfem.par as mfem

        pp = np.array(pp, copy=False, dtype=float).transpose()      
        M = mfem.DenseMatrix(pp.shape[0], pp.shape[1])
        M.Assign(pp)
        elem_ids = mfem.intArray()
        int_points = mfem.IntegrationPointArray()
        count = _pmesh.ParMesh_FindPoints(self, M, elem_ids, int_points, warn, inv_trans)      
        elem_ids = elem_ids.ToList()
        return count, elem_ids, int_points



    def PrintSharedEntities(self, fname_prefix):
        r"""PrintSharedEntities(ParMesh self, char const * fname_prefix)"""
        return _pmesh.ParMesh_PrintSharedEntities(self, fname_prefix)
    PrintSharedEntities = _swig_new_instance_method(_pmesh.ParMesh_PrintSharedEntities)
    __swig_destroy__ = _pmesh.delete_ParMesh

    def ParPrintToFile(self, mesh_file, precision):
        r"""ParPrintToFile(ParMesh self, char const * mesh_file, int const precision)"""
        return _pmesh.ParMesh_ParPrintToFile(self, mesh_file, precision)
    ParPrintToFile = _swig_new_instance_method(_pmesh.ParMesh_ParPrintToFile)

    def Print(self, *args):
        r"""
        Print(ParMesh self, std::ostream & out=out)
        Print(ParMesh self, char const * file, int precision=16)
        """
        return _pmesh.ParMesh_Print(self, *args)
    Print = _swig_new_instance_method(_pmesh.ParMesh_Print)

    def PrintGZ(self, file, precision=16):
        r"""PrintGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_PrintGZ(self, file, precision)
    PrintGZ = _swig_new_instance_method(_pmesh.ParMesh_PrintGZ)

    def PrintXG(self, *args):
        r"""
        PrintXG(ParMesh self, std::ostream & out=out)
        PrintXG(ParMesh self, char const * file, int precision=16)
        """
        return _pmesh.ParMesh_PrintXG(self, *args)
    PrintXG = _swig_new_instance_method(_pmesh.ParMesh_PrintXG)

    def PrintXGGZ(self, file, precision=16):
        r"""PrintXGGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_PrintXGGZ(self, file, precision)
    PrintXGGZ = _swig_new_instance_method(_pmesh.ParMesh_PrintXGGZ)

    def PrintAsOne(self, *args):
        r"""
        PrintAsOne(ParMesh self, std::ostream & out=out)
        PrintAsOne(ParMesh self, char const * file, int precision=16)
        """
        return _pmesh.ParMesh_PrintAsOne(self, *args)
    PrintAsOne = _swig_new_instance_method(_pmesh.ParMesh_PrintAsOne)

    def PrintAsOneGZ(self, file, precision=16):
        r"""PrintAsOneGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_PrintAsOneGZ(self, file, precision)
    PrintAsOneGZ = _swig_new_instance_method(_pmesh.ParMesh_PrintAsOneGZ)

    def PrintAsOneXG(self, *args):
        r"""
        PrintAsOneXG(ParMesh self, std::ostream & out=out)
        PrintAsOneXG(ParMesh self, char const * file, int precision=16)
        """
        return _pmesh.ParMesh_PrintAsOneXG(self, *args)
    PrintAsOneXG = _swig_new_instance_method(_pmesh.ParMesh_PrintAsOneXG)

    def PrintAsOneXGGZ(self, file, precision=16):
        r"""PrintAsOneXGGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_PrintAsOneXGGZ(self, file, precision)
    PrintAsOneXGGZ = _swig_new_instance_method(_pmesh.ParMesh_PrintAsOneXGGZ)

    def PrintInfo(self, *args):
        r"""
        PrintInfo(ParMesh self, std::ostream & out=out)
        PrintInfo(ParMesh self, char const * file, int precision=16)
        """
        return _pmesh.ParMesh_PrintInfo(self, *args)
    PrintInfo = _swig_new_instance_method(_pmesh.ParMesh_PrintInfo)

    def PrintInfoGZ(self, file, precision=16):
        r"""PrintInfoGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_PrintInfoGZ(self, file, precision)
    PrintInfoGZ = _swig_new_instance_method(_pmesh.ParMesh_PrintInfoGZ)

    def ParPrintGZ(self, file, precision=16):
        r"""ParPrintGZ(ParMesh self, char const * file, int precision=16)"""
        return _pmesh.ParMesh_ParPrintGZ(self, file, precision)
    ParPrintGZ = _swig_new_instance_method(_pmesh.ParMesh_ParPrintGZ)

    def ParPrint(self, *args):
        r"""
        ParPrint(ParMesh self, std::ostream & out)
        ParPrint(ParMesh self, char const * file, int precision=16)
        ParPrint(ParMesh self)
        """
        return _pmesh.ParMesh_ParPrint(self, *args)
    ParPrint = _swig_new_instance_method(_pmesh.ParMesh_ParPrint)

# Register ParMesh in _pmesh:
_pmesh.ParMesh_swigregister(ParMesh)

def ParMesh_MakeRefined(orig_mesh, ref_factor, ref_type):
    r"""ParMesh_MakeRefined(ParMesh orig_mesh, int ref_factor, int ref_type) -> ParMesh"""
    return _pmesh.ParMesh_MakeRefined(orig_mesh, ref_factor, ref_type)
ParMesh_MakeRefined = _pmesh.ParMesh_MakeRefined

def ParMesh_MakeSimplicial(orig_mesh):
    r"""ParMesh_MakeSimplicial(ParMesh orig_mesh) -> ParMesh"""
    return _pmesh.ParMesh_MakeSimplicial(orig_mesh)
ParMesh_MakeSimplicial = _pmesh.ParMesh_MakeSimplicial



