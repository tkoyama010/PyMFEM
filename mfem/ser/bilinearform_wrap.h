/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 3.0.12
 *
 * This file is not intended to be easily readable and contains a number of
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG
 * interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_bilinearform_WRAP_H_
#define SWIG_bilinearform_WRAP_H_

#include <map>
#include <string>


class SwigDirector_BilinearForm : public mfem::BilinearForm, public Swig::Director {

public:
    SwigDirector_BilinearForm(PyObject *self);
    SwigDirector_BilinearForm(PyObject *self, mfem::FiniteElementSpace *f);
    SwigDirector_BilinearForm(PyObject *self, mfem::FiniteElementSpace *f, mfem::BilinearForm *bf, int ps = 0);
    virtual void Mult(mfem::Vector const &x, mfem::Vector &y) const;
    virtual void MultTranspose(mfem::Vector const &x, mfem::Vector &y) const;
    virtual mfem::Operator &GetGradient(mfem::Vector const &x) const;
    virtual mfem::Operator const *GetProlongation() const;
    virtual mfem::Operator const *GetRestriction() const;
    virtual void RecoverFEMSolution(mfem::Vector const &X, mfem::Vector const &b, mfem::Vector &x);
    virtual ~SwigDirector_BilinearForm();
    virtual double &Elem(int i, int j);
    virtual double const &Elem(int i, int j) const;
    virtual mfem::MatrixInverse *Inverse() const;
    virtual void Finalize(int skip_zeros = 1);
    virtual void Print(std::ostream &out = mfem::out, int width_ = 4) const;
    virtual void AddMult(mfem::Vector const &x, mfem::Vector &y, double const a = 1.0) const;
    virtual void AddMultTranspose(mfem::Vector const &x, mfem::Vector &y, double const a = 1.0) const;
    virtual void Update(mfem::FiniteElementSpace *nfes = NULL);

/* Internal director utilities */
public:
    bool swig_get_inner(const char *swig_protected_method_name) const {
      std::map<std::string, bool>::const_iterator iv = swig_inner.find(swig_protected_method_name);
      return (iv != swig_inner.end() ? iv->second : false);
    }
    void swig_set_inner(const char *swig_protected_method_name, bool swig_val) const {
      swig_inner[swig_protected_method_name] = swig_val;
    }
private:
    mutable std::map<std::string, bool> swig_inner;

#if defined(SWIG_PYTHON_DIRECTOR_VTABLE)
/* VTable implementation */
    PyObject *swig_get_method(size_t method_index, const char *method_name) const {
      PyObject *method = vtable[method_index];
      if (!method) {
        swig::SwigVar_PyObject name = SWIG_Python_str_FromChar(method_name);
        method = PyObject_GetAttr(swig_get_self(), name);
        if (!method) {
          std::string msg = "Method in class BilinearForm doesn't exist, undefined ";
          msg += method_name;
          Swig::DirectorMethodException::raise(msg.c_str());
        }
        vtable[method_index] = method;
      }
      return method;
    }
private:
    mutable swig::SwigVar_PyObject vtable[20];
#endif

};


#endif
