/* Generated code for Python module 'google.cloud.vision_v1.types.text_annotation'
 * created by Nuitka version 1.0.7
 *
 * This code is in part copyright 2022 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "nuitka/unfreezing.h"

#include "__helpers.h"

/* The "module_google$cloud$vision_v1$types$text_annotation" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_google$cloud$vision_v1$types$text_annotation;
PyDictObject *moduledict_google$cloud$vision_v1$types$text_annotation;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[119];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[119];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("google.cloud.vision_v1.types.text_annotation"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 119; i++) {
            mod_consts_hash[i] = DEEP_HASH(mod_consts[i]);
        }
#endif
    }
}

// We want to be able to initialize the "__main__" constants in any case.
#if 0
void createMainModuleConstants(void) {
    createModuleConstants();
}
#endif

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_google$cloud$vision_v1$types$text_annotation(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 119; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_e49d3c7b1b476ec58fa7db7e1a3c190b;
static PyCodeObject *codeobj_c432345856637768f47cce9ceb801963;
static PyCodeObject *codeobj_a78d2cc6bb506efb06d14111c3854097;
static PyCodeObject *codeobj_e8ffb51946009f1f43fd70dc3ae4c8bb;
static PyCodeObject *codeobj_1e57d9201f75c5f420f63ce5688a3e8b;
static PyCodeObject *codeobj_a410df66cd43733c8b52bbdf218dc5f8;
static PyCodeObject *codeobj_aae2ed367423a5fce3ebf6593eb0816b;
static PyCodeObject *codeobj_6f04537ce0314438b27dac197fa5c5b7;
static PyCodeObject *codeobj_b21bd41c7b77e2ce8f6979bb66f1458e;
static PyCodeObject *codeobj_5cea5e801737c4e565477c4e5b13c74d;
static PyCodeObject *codeobj_6c31dcf67c1bcc18b06bdd9be6ff70ce;
static PyCodeObject *codeobj_520a46f34edf5917d2b72256ec38a725;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[115]); CHECK_OBJECT(module_filename_obj);
    codeobj_e49d3c7b1b476ec58fa7db7e1a3c190b = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[116], NULL, NULL, 0, 0, 0);
    codeobj_c432345856637768f47cce9ceb801963 = MAKE_CODEOBJECT(module_filename_obj, 177, CO_NOFREE, mod_consts[84], mod_consts[117], NULL, 0, 0, 0);
    codeobj_a78d2cc6bb506efb06d14111c3854097 = MAKE_CODEOBJECT(module_filename_obj, 219, CO_NOFREE, mod_consts[86], mod_consts[117], NULL, 0, 0, 0);
    codeobj_e8ffb51946009f1f43fd70dc3ae4c8bb = MAKE_CODEOBJECT(module_filename_obj, 82, CO_NOFREE, mod_consts[42], mod_consts[117], NULL, 0, 0, 0);
    codeobj_1e57d9201f75c5f420f63ce5688a3e8b = MAKE_CODEOBJECT(module_filename_obj, 72, CO_NOFREE, mod_consts[38], mod_consts[117], NULL, 0, 0, 0);
    codeobj_a410df66cd43733c8b52bbdf218dc5f8 = MAKE_CODEOBJECT(module_filename_obj, 51, CO_NOFREE, mod_consts[27], mod_consts[117], NULL, 0, 0, 0);
    codeobj_aae2ed367423a5fce3ebf6593eb0816b = MAKE_CODEOBJECT(module_filename_obj, 134, CO_NOFREE, mod_consts[73], mod_consts[117], NULL, 0, 0, 0);
    codeobj_6f04537ce0314438b27dac197fa5c5b7 = MAKE_CODEOBJECT(module_filename_obj, 254, CO_NOFREE, mod_consts[101], mod_consts[117], NULL, 0, 0, 0);
    codeobj_b21bd41c7b77e2ce8f6979bb66f1458e = MAKE_CODEOBJECT(module_filename_obj, 349, CO_NOFREE, mod_consts[110], mod_consts[117], NULL, 0, 0, 0);
    codeobj_5cea5e801737c4e565477c4e5b13c74d = MAKE_CODEOBJECT(module_filename_obj, 34, CO_NOFREE, mod_consts[18], mod_consts[117], NULL, 0, 0, 0);
    codeobj_6c31dcf67c1bcc18b06bdd9be6ff70ce = MAKE_CODEOBJECT(module_filename_obj, 101, CO_NOFREE, mod_consts[61], mod_consts[117], NULL, 0, 0, 0);
    codeobj_520a46f34edf5917d2b72256ec38a725 = MAKE_CODEOBJECT(module_filename_obj, 302, CO_NOFREE, mod_consts[106], mod_consts[117], NULL, 0, 0, 0);
}

// The module function declarations.
NUITKA_CROSS_MODULE PyObject *impl___main__$$$function__1__mro_entries_conversion(PyObject **python_pars);


// The module function definitions.


extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();

extern PyTypeObject Nuitka_Loader_Type;

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
// Provide a way to create find a function via its C code and create it back
// in another process, useful for multiprocessing extensions like dill
extern void registerDillPluginTables(char const *module_name, PyMethodDef *reduce_compiled_function, PyMethodDef *create_compiled_function);

function_impl_code functable_google$cloud$vision_v1$types$text_annotation[] = {

    NULL
};

static char const *_reduce_compiled_function_argnames[] = {
    "func",
    NULL
};

static PyObject *_reduce_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    PyObject *func;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:reduce_compiled_function", (char **)_reduce_compiled_function_argnames, &func, NULL)) {
        return NULL;
    }

    if (Nuitka_Function_Check(func) == false) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "not a compiled function");
        return NULL;
    }

    struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)func;

    function_impl_code *current = functable_google$cloud$vision_v1$types$text_annotation;
    int offset = 0;

    while (*current != NULL) {
        if (*current == function->m_c_code) {
            break;
        }

        current += 1;
        offset += 1;
    }

    if (*current == NULL) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Cannot find compiled function in module.");
        return NULL;
    }

    PyObject *code_object_desc = PyTuple_New(6);
    PyTuple_SET_ITEM0(code_object_desc, 0, function->m_code_object->co_filename);
    PyTuple_SET_ITEM0(code_object_desc, 1, function->m_code_object->co_name);
    PyTuple_SET_ITEM(code_object_desc, 2, PyLong_FromLong(function->m_code_object->co_firstlineno));
    PyTuple_SET_ITEM0(code_object_desc, 3, function->m_code_object->co_varnames);
    PyTuple_SET_ITEM(code_object_desc, 4, PyLong_FromLong(function->m_code_object->co_argcount));
    PyTuple_SET_ITEM(code_object_desc, 5, PyLong_FromLong(function->m_code_object->co_flags));

    CHECK_OBJECT_DEEP(code_object_desc);

    PyObject *result = PyTuple_New(4);
    PyTuple_SET_ITEM(result, 0, PyLong_FromLong(offset));
    PyTuple_SET_ITEM(result, 1, code_object_desc);
    PyTuple_SET_ITEM0(result, 2, function->m_defaults);
    PyTuple_SET_ITEM0(result, 3, function->m_doc != NULL ? function->m_doc : Py_None);

    CHECK_OBJECT_DEEP(result);

    return result;
}

static PyMethodDef _method_def_reduce_compiled_function = {"reduce_compiled_function", (PyCFunction)_reduce_compiled_function,
                                                           METH_VARARGS | METH_KEYWORDS, NULL};

static char const *_create_compiled_function_argnames[] = {
    "func",
    "code_object_desc",
    "defaults",
    "doc",
    NULL
};


static PyObject *_create_compiled_function(PyObject *self, PyObject *args, PyObject *kwds) {
    CHECK_OBJECT_DEEP(args);

    PyObject *func;
    PyObject *code_object_desc;
    PyObject *defaults;
    PyObject *doc;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOOO:create_compiled_function", (char **)_create_compiled_function_argnames, &func, &code_object_desc, &defaults, &doc, NULL)) {
        return NULL;
    }

    int offset = PyLong_AsLong(func);

    if (offset == -1 && ERROR_OCCURRED()) {
        return NULL;
    }

    if (offset > sizeof(functable_google$cloud$vision_v1$types$text_annotation) || offset < 0) {
        SET_CURRENT_EXCEPTION_TYPE0_STR(PyExc_TypeError, "Wrong offset for compiled function.");
        return NULL;
    }

    PyObject *filename = PyTuple_GET_ITEM(code_object_desc, 0);
    PyObject *function_name = PyTuple_GET_ITEM(code_object_desc, 1);
    PyObject *line = PyTuple_GET_ITEM(code_object_desc, 2);
    int line_int = PyLong_AsLong(line);
    assert(!ERROR_OCCURRED());

    PyObject *argnames = PyTuple_GET_ITEM(code_object_desc, 3);
    PyObject *arg_count = PyTuple_GET_ITEM(code_object_desc, 4);
    int arg_count_int = PyLong_AsLong(arg_count);
    assert(!ERROR_OCCURRED());
    PyObject *flags = PyTuple_GET_ITEM(code_object_desc, 5);
    int flags_int = PyLong_AsLong(flags);
    assert(!ERROR_OCCURRED());

    PyCodeObject *code_object = MAKE_CODEOBJECT(
        filename,
        line_int,
        flags_int,
        function_name,
        argnames,
        NULL, // freevars
        arg_count_int,
        0, // TODO: Missing kw_only_count
        0 // TODO: Missing pos_only_count
    );

    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        functable_google$cloud$vision_v1$types$text_annotation[offset],
        code_object->co_name,
#if PYTHON_VERSION >= 0x300
        NULL, // TODO: Not transferring qualname yet
#endif
        code_object,
        defaults,
#if PYTHON_VERSION >= 0x300
        NULL, // kwdefaults are done on the outside currently
        NULL, // TODO: Not transferring annotations
#endif
        module_google$cloud$vision_v1$types$text_annotation,
        doc,
        NULL,
        0
    );

    return (PyObject *)result;
}

static PyMethodDef _method_def_create_compiled_function = {
    "create_compiled_function",
    (PyCFunction)_create_compiled_function,
    METH_VARARGS | METH_KEYWORDS, NULL
};


#endif

// Internal entry point for module code.
PyObject *modulecode_google$cloud$vision_v1$types$text_annotation(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("google.cloud.vision_v1.types.text_annotation");

    // Store the module for future use.
    module_google$cloud$vision_v1$types$text_annotation = module;

    // Modules can be loaded again in case of errors, avoid the init being done again.
    static bool init_done = false;

    if (init_done == false) {
#if defined(_NUITKA_MODULE) && 0
        // In case of an extension module loaded into a process, we need to call
        // initialization here because that's the first and potentially only time
        // we are going called.

        // Initialize the constant values used.
        _initBuiltinModule();
        createGlobalConstants();

        /* Initialize the compiled types of Nuitka. */
        _initCompiledCellType();
        _initCompiledGeneratorType();
        _initCompiledFunctionType();
        _initCompiledMethodType();
        _initCompiledFrameType();

        _initSlotCompare();
#if PYTHON_VERSION >= 0x270
        _initSlotIterNext();
#endif

        patchTypeComparison();

        // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
        PRINT_STRING("google.cloud.vision_v1.types.text_annotation: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
        patchInspectModule();
#endif

#endif

        /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("google.cloud.vision_v1.types.text_annotation: Calling createModuleConstants().\n");
#endif
        createModuleConstants();

        /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("google.cloud.vision_v1.types.text_annotation: Calling createModuleCodeObjects().\n");
#endif
        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initgoogle$cloud$vision_v1$types$text_annotation\n");

    moduledict_google$cloud$vision_v1$types$text_annotation = MODULE_DICT(module_google$cloud$vision_v1$types$text_annotation);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(loader_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_google$cloud$vision_v1$types$text_annotation,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_google$cloud$vision_v1$types$text_annotation,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[118]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_google$cloud$vision_v1$types$text_annotation,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_google$cloud$vision_v1$types$text_annotation,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_google$cloud$vision_v1$types$text_annotation,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_google$cloud$vision_v1$types$text_annotation);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_google$cloud$vision_v1$types$text_annotation);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    PyObject *outline_0_var___class__ = NULL;
    PyObject *outline_1_var___class__ = NULL;
    PyObject *outline_2_var___class__ = NULL;
    PyObject *outline_3_var___class__ = NULL;
    PyObject *outline_4_var___class__ = NULL;
    PyObject *outline_5_var___class__ = NULL;
    PyObject *outline_6_var___class__ = NULL;
    PyObject *outline_7_var___class__ = NULL;
    PyObject *outline_8_var___class__ = NULL;
    PyObject *outline_9_var___class__ = NULL;
    PyObject *outline_10_var___class__ = NULL;
    PyObject *tmp_Block$class_creation_1__bases = NULL;
    PyObject *tmp_Block$class_creation_1__bases_orig = NULL;
    PyObject *tmp_Block$class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_Block$class_creation_1__metaclass = NULL;
    PyObject *tmp_Block$class_creation_1__prepared = NULL;
    PyObject *tmp_TextAnnotation$DetectedBreak$class_creation_1__bases = NULL;
    PyObject *tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig = NULL;
    PyObject *tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass = NULL;
    PyObject *tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared = NULL;
    PyObject *tmp_TextAnnotation$class_creation_1__bases = NULL;
    PyObject *tmp_TextAnnotation$class_creation_1__bases_orig = NULL;
    PyObject *tmp_TextAnnotation$class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_TextAnnotation$class_creation_1__metaclass = NULL;
    PyObject *tmp_TextAnnotation$class_creation_1__prepared = NULL;
    PyObject *tmp_TextAnnotation$class_creation_2__bases = NULL;
    PyObject *tmp_TextAnnotation$class_creation_2__bases_orig = NULL;
    PyObject *tmp_TextAnnotation$class_creation_2__class_decl_dict = NULL;
    PyObject *tmp_TextAnnotation$class_creation_2__metaclass = NULL;
    PyObject *tmp_TextAnnotation$class_creation_2__prepared = NULL;
    PyObject *tmp_TextAnnotation$class_creation_3__bases = NULL;
    PyObject *tmp_TextAnnotation$class_creation_3__bases_orig = NULL;
    PyObject *tmp_TextAnnotation$class_creation_3__class_decl_dict = NULL;
    PyObject *tmp_TextAnnotation$class_creation_3__metaclass = NULL;
    PyObject *tmp_TextAnnotation$class_creation_3__prepared = NULL;
    PyObject *tmp_class_creation_1__bases = NULL;
    PyObject *tmp_class_creation_1__bases_orig = NULL;
    PyObject *tmp_class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_class_creation_1__metaclass = NULL;
    PyObject *tmp_class_creation_1__prepared = NULL;
    PyObject *tmp_class_creation_2__bases = NULL;
    PyObject *tmp_class_creation_2__bases_orig = NULL;
    PyObject *tmp_class_creation_2__class_decl_dict = NULL;
    PyObject *tmp_class_creation_2__metaclass = NULL;
    PyObject *tmp_class_creation_2__prepared = NULL;
    PyObject *tmp_class_creation_3__bases = NULL;
    PyObject *tmp_class_creation_3__bases_orig = NULL;
    PyObject *tmp_class_creation_3__class_decl_dict = NULL;
    PyObject *tmp_class_creation_3__metaclass = NULL;
    PyObject *tmp_class_creation_3__prepared = NULL;
    PyObject *tmp_class_creation_4__bases = NULL;
    PyObject *tmp_class_creation_4__bases_orig = NULL;
    PyObject *tmp_class_creation_4__class_decl_dict = NULL;
    PyObject *tmp_class_creation_4__metaclass = NULL;
    PyObject *tmp_class_creation_4__prepared = NULL;
    PyObject *tmp_class_creation_5__bases = NULL;
    PyObject *tmp_class_creation_5__bases_orig = NULL;
    PyObject *tmp_class_creation_5__class_decl_dict = NULL;
    PyObject *tmp_class_creation_5__metaclass = NULL;
    PyObject *tmp_class_creation_5__prepared = NULL;
    PyObject *tmp_class_creation_6__bases = NULL;
    PyObject *tmp_class_creation_6__bases_orig = NULL;
    PyObject *tmp_class_creation_6__class_decl_dict = NULL;
    PyObject *tmp_class_creation_6__metaclass = NULL;
    PyObject *tmp_class_creation_6__prepared = NULL;
    struct Nuitka_FrameObject *frame_e49d3c7b1b476ec58fa7db7e1a3c190b;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;
    PyObject *tmp_dictdel_dict;
    PyObject *tmp_dictdel_key;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34 = NULL;
    PyObject *tmp_dictset_value;
    struct Nuitka_FrameObject *frame_5cea5e801737c4e565477c4e5b13c74d_2;
    NUITKA_MAY_BE_UNUSED char const *type_description_2 = NULL;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51 = NULL;
    struct Nuitka_FrameObject *frame_a410df66cd43733c8b52bbdf218dc5f8_3;
    NUITKA_MAY_BE_UNUSED char const *type_description_3 = NULL;
    static struct Nuitka_FrameObject *cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3 = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72 = NULL;
    struct Nuitka_FrameObject *frame_1e57d9201f75c5f420f63ce5688a3e8b_4;
    NUITKA_MAY_BE_UNUSED char const *type_description_4 = NULL;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82 = NULL;
    struct Nuitka_FrameObject *frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5;
    NUITKA_MAY_BE_UNUSED char const *type_description_5 = NULL;
    static struct Nuitka_FrameObject *cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 = NULL;
    PyObject *exception_keeper_type_4;
    PyObject *exception_keeper_value_4;
    PyTracebackObject *exception_keeper_tb_4;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_4;
    PyObject *exception_keeper_type_5;
    PyObject *exception_keeper_value_5;
    PyTracebackObject *exception_keeper_tb_5;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_5;
    PyObject *exception_keeper_type_6;
    PyObject *exception_keeper_value_6;
    PyTracebackObject *exception_keeper_tb_6;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_6;
    static struct Nuitka_FrameObject *cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4 = NULL;
    PyObject *exception_keeper_type_7;
    PyObject *exception_keeper_value_7;
    PyTracebackObject *exception_keeper_tb_7;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_7;
    PyObject *exception_keeper_type_8;
    PyObject *exception_keeper_value_8;
    PyTracebackObject *exception_keeper_tb_8;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_8;
    PyObject *exception_keeper_type_9;
    PyObject *exception_keeper_value_9;
    PyTracebackObject *exception_keeper_tb_9;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_9;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101 = NULL;
    struct Nuitka_FrameObject *frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6;
    NUITKA_MAY_BE_UNUSED char const *type_description_6 = NULL;
    static struct Nuitka_FrameObject *cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 = NULL;
    PyObject *exception_keeper_type_10;
    PyObject *exception_keeper_value_10;
    PyTracebackObject *exception_keeper_tb_10;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_10;
    PyObject *exception_keeper_type_11;
    PyObject *exception_keeper_value_11;
    PyTracebackObject *exception_keeper_tb_11;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_11;
    PyObject *exception_keeper_type_12;
    PyObject *exception_keeper_value_12;
    PyTracebackObject *exception_keeper_tb_12;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_12;
    static struct Nuitka_FrameObject *cache_frame_5cea5e801737c4e565477c4e5b13c74d_2 = NULL;
    PyObject *exception_keeper_type_13;
    PyObject *exception_keeper_value_13;
    PyTracebackObject *exception_keeper_tb_13;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_13;
    PyObject *exception_keeper_type_14;
    PyObject *exception_keeper_value_14;
    PyTracebackObject *exception_keeper_tb_14;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_14;
    PyObject *exception_keeper_type_15;
    PyObject *exception_keeper_value_15;
    PyTracebackObject *exception_keeper_tb_15;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_15;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134 = NULL;
    struct Nuitka_FrameObject *frame_aae2ed367423a5fce3ebf6593eb0816b_7;
    NUITKA_MAY_BE_UNUSED char const *type_description_7 = NULL;
    static struct Nuitka_FrameObject *cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7 = NULL;
    PyObject *exception_keeper_type_16;
    PyObject *exception_keeper_value_16;
    PyTracebackObject *exception_keeper_tb_16;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_16;
    PyObject *exception_keeper_type_17;
    PyObject *exception_keeper_value_17;
    PyTracebackObject *exception_keeper_tb_17;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_17;
    PyObject *exception_keeper_type_18;
    PyObject *exception_keeper_value_18;
    PyTracebackObject *exception_keeper_tb_18;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_18;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177 = NULL;
    struct Nuitka_FrameObject *frame_c432345856637768f47cce9ceb801963_8;
    NUITKA_MAY_BE_UNUSED char const *type_description_8 = NULL;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219 = NULL;
    struct Nuitka_FrameObject *frame_a78d2cc6bb506efb06d14111c3854097_9;
    NUITKA_MAY_BE_UNUSED char const *type_description_9 = NULL;
    static struct Nuitka_FrameObject *cache_frame_a78d2cc6bb506efb06d14111c3854097_9 = NULL;
    PyObject *exception_keeper_type_19;
    PyObject *exception_keeper_value_19;
    PyTracebackObject *exception_keeper_tb_19;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_19;
    PyObject *exception_keeper_type_20;
    PyObject *exception_keeper_value_20;
    PyTracebackObject *exception_keeper_tb_20;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_20;
    PyObject *exception_keeper_type_21;
    PyObject *exception_keeper_value_21;
    PyTracebackObject *exception_keeper_tb_21;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_21;
    static struct Nuitka_FrameObject *cache_frame_c432345856637768f47cce9ceb801963_8 = NULL;
    PyObject *exception_keeper_type_22;
    PyObject *exception_keeper_value_22;
    PyTracebackObject *exception_keeper_tb_22;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_22;
    PyObject *exception_keeper_type_23;
    PyObject *exception_keeper_value_23;
    PyTracebackObject *exception_keeper_tb_23;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_23;
    PyObject *exception_keeper_type_24;
    PyObject *exception_keeper_value_24;
    PyTracebackObject *exception_keeper_tb_24;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_24;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254 = NULL;
    struct Nuitka_FrameObject *frame_6f04537ce0314438b27dac197fa5c5b7_10;
    NUITKA_MAY_BE_UNUSED char const *type_description_10 = NULL;
    static struct Nuitka_FrameObject *cache_frame_6f04537ce0314438b27dac197fa5c5b7_10 = NULL;
    PyObject *exception_keeper_type_25;
    PyObject *exception_keeper_value_25;
    PyTracebackObject *exception_keeper_tb_25;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_25;
    PyObject *exception_keeper_type_26;
    PyObject *exception_keeper_value_26;
    PyTracebackObject *exception_keeper_tb_26;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_26;
    PyObject *exception_keeper_type_27;
    PyObject *exception_keeper_value_27;
    PyTracebackObject *exception_keeper_tb_27;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_27;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302 = NULL;
    struct Nuitka_FrameObject *frame_520a46f34edf5917d2b72256ec38a725_11;
    NUITKA_MAY_BE_UNUSED char const *type_description_11 = NULL;
    static struct Nuitka_FrameObject *cache_frame_520a46f34edf5917d2b72256ec38a725_11 = NULL;
    PyObject *exception_keeper_type_28;
    PyObject *exception_keeper_value_28;
    PyTracebackObject *exception_keeper_tb_28;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_28;
    PyObject *exception_keeper_type_29;
    PyObject *exception_keeper_value_29;
    PyTracebackObject *exception_keeper_tb_29;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_29;
    PyObject *exception_keeper_type_30;
    PyObject *exception_keeper_value_30;
    PyTracebackObject *exception_keeper_tb_30;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_30;
    PyObject *locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349 = NULL;
    struct Nuitka_FrameObject *frame_b21bd41c7b77e2ce8f6979bb66f1458e_12;
    NUITKA_MAY_BE_UNUSED char const *type_description_12 = NULL;
    static struct Nuitka_FrameObject *cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 = NULL;
    PyObject *exception_keeper_type_31;
    PyObject *exception_keeper_value_31;
    PyTracebackObject *exception_keeper_tb_31;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_31;
    PyObject *exception_keeper_type_32;
    PyObject *exception_keeper_value_32;
    PyTracebackObject *exception_keeper_tb_32;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_32;
    PyObject *exception_keeper_type_33;
    PyObject *exception_keeper_value_33;
    PyTracebackObject *exception_keeper_tb_33;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_33;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_e49d3c7b1b476ec58fa7db7e1a3c190b = MAKE_MODULE_FRAME(codeobj_e49d3c7b1b476ec58fa7db7e1a3c190b, module_google$cloud$vision_v1$types$text_annotation);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_e49d3c7b1b476ec58fa7db7e1a3c190b);
    assert(Py_REFCNT(frame_e49d3c7b1b476ec58fa7db7e1a3c190b) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[2]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[3], tmp_assattr_value_1);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assattr_value_2;
        PyObject *tmp_assattr_target_2;
        tmp_assattr_value_2 = Py_True;
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[2]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[2]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[4], tmp_assattr_value_2);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[6];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_google$cloud$vision_v1$types$text_annotation;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = Py_None;
        tmp_level_value_1 = mod_consts[7];
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 16;
        tmp_assign_source_4 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_2;
        PyObject *tmp_globals_arg_value_2;
        PyObject *tmp_locals_arg_value_2;
        PyObject *tmp_fromlist_value_2;
        PyObject *tmp_level_value_2;
        tmp_name_value_2 = mod_consts[8];
        tmp_globals_arg_value_2 = (PyObject *)moduledict_google$cloud$vision_v1$types$text_annotation;
        tmp_locals_arg_value_2 = Py_None;
        tmp_fromlist_value_2 = mod_consts[9];
        tmp_level_value_2 = mod_consts[7];
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 18;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_2, tmp_globals_arg_value_2, tmp_locals_arg_value_2, tmp_fromlist_value_2, tmp_level_value_2);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 18;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_5 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_google$cloud$vision_v1$types$text_annotation,
                mod_consts[10],
                mod_consts[7]
            );
        } else {
            tmp_assign_source_5 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[10]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 18;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[10], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_args_kwsplit_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 21;

            goto frame_exception_exit_1;
        }
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[11]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 21;

            goto frame_exception_exit_1;
        }
        tmp_call_args_kwsplit_1 = DEEP_COPY_TUPLE(mod_consts[12]);
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 21;
        tmp_assign_source_6 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_1, &PyTuple_GET_ITEM(tmp_call_args_kwsplit_1, 0), mod_consts[13]);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_call_args_kwsplit_1);
        if (tmp_assign_source_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 21;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[14], tmp_assign_source_6);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_expression_value_2;
        tmp_expression_value_2 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_2 == NULL)) {
            tmp_expression_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_tuple_element_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_2, mod_consts[15]);
        if (tmp_tuple_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_assign_source_7 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_7, 0, tmp_tuple_element_1);
        assert(tmp_class_creation_1__bases_orig == NULL);
        tmp_class_creation_1__bases_orig = tmp_assign_source_7;
    }
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_dircall_arg1_1;
        CHECK_OBJECT(tmp_class_creation_1__bases_orig);
        tmp_dircall_arg1_1 = tmp_class_creation_1__bases_orig;
        Py_INCREF(tmp_dircall_arg1_1);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_1};
            tmp_assign_source_8 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__bases == NULL);
        tmp_class_creation_1__bases = tmp_assign_source_8;
    }
    {
        PyObject *tmp_assign_source_9;
        tmp_assign_source_9 = PyDict_New();
        assert(tmp_class_creation_1__class_decl_dict == NULL);
        tmp_class_creation_1__class_decl_dict = tmp_assign_source_9;
    }
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_metaclass_value_1;
        bool tmp_condition_result_1;
        PyObject *tmp_key_value_1;
        PyObject *tmp_dict_arg_value_1;
        PyObject *tmp_dict_arg_value_2;
        PyObject *tmp_key_value_2;
        nuitka_bool tmp_condition_result_2;
        int tmp_truth_name_1;
        PyObject *tmp_type_arg_1;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_subscript_value_1;
        PyObject *tmp_bases_value_1;
        tmp_key_value_1 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_dict_arg_value_1 = tmp_class_creation_1__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_1, tmp_key_value_1);
        assert(!(tmp_res == -1));
        tmp_condition_result_1 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto condexpr_true_1;
        } else {
            goto condexpr_false_1;
        }
        condexpr_true_1:;
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_dict_arg_value_2 = tmp_class_creation_1__class_decl_dict;
        tmp_key_value_2 = mod_consts[16];
        tmp_metaclass_value_1 = DICT_GET_ITEM0(tmp_dict_arg_value_2, tmp_key_value_2);
        if (tmp_metaclass_value_1 == NULL) {
            tmp_metaclass_value_1 = Py_None;
        }
        assert(!(tmp_metaclass_value_1 == NULL));
        Py_INCREF(tmp_metaclass_value_1);
        goto condexpr_end_1;
        condexpr_false_1:;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_truth_name_1 = CHECK_IF_TRUE(tmp_class_creation_1__bases);
        if (tmp_truth_name_1 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_condition_result_2 = tmp_truth_name_1 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_2 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_2;
        } else {
            goto condexpr_false_2;
        }
        condexpr_true_2:;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_expression_value_3 = tmp_class_creation_1__bases;
        tmp_subscript_value_1 = mod_consts[7];
        tmp_type_arg_1 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_3, tmp_subscript_value_1, 0);
        if (tmp_type_arg_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_metaclass_value_1 = BUILTIN_TYPE1(tmp_type_arg_1);
        Py_DECREF(tmp_type_arg_1);
        if (tmp_metaclass_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        goto condexpr_end_2;
        condexpr_false_2:;
        tmp_metaclass_value_1 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_1);
        condexpr_end_2:;
        condexpr_end_1:;
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_bases_value_1 = tmp_class_creation_1__bases;
        tmp_assign_source_10 = SELECT_METACLASS(tmp_metaclass_value_1, tmp_bases_value_1);
        Py_DECREF(tmp_metaclass_value_1);
        if (tmp_assign_source_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__metaclass == NULL);
        tmp_class_creation_1__metaclass = tmp_assign_source_10;
    }
    {
        bool tmp_condition_result_3;
        PyObject *tmp_key_value_3;
        PyObject *tmp_dict_arg_value_3;
        tmp_key_value_3 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_dict_arg_value_3 = tmp_class_creation_1__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_3, tmp_key_value_3);
        assert(!(tmp_res == -1));
        tmp_condition_result_3 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_3 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_1__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 34;

        goto try_except_handler_1;
    }
    branch_no_1:;
    {
        nuitka_bool tmp_condition_result_4;
        PyObject *tmp_expression_value_4;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_4 = tmp_class_creation_1__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_4, mod_consts[17]);
        tmp_condition_result_4 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_4 == NUITKA_BOOL_TRUE) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_called_value_2;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_kwargs_value_1;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_5 = tmp_class_creation_1__metaclass;
        tmp_called_value_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_5, mod_consts[17]);
        if (tmp_called_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_tuple_element_2 = mod_consts[18];
        tmp_args_value_1 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_1, 0, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_tuple_element_2 = tmp_class_creation_1__bases;
        PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_kwargs_value_1 = tmp_class_creation_1__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 34;
        tmp_assign_source_11 = CALL_FUNCTION(tmp_called_value_2, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_called_value_2);
        Py_DECREF(tmp_args_value_1);
        if (tmp_assign_source_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_11;
    }
    {
        bool tmp_condition_result_5;
        PyObject *tmp_operand_value_1;
        PyObject *tmp_expression_value_6;
        CHECK_OBJECT(tmp_class_creation_1__prepared);
        tmp_expression_value_6 = tmp_class_creation_1__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_6, mod_consts[19]);
        tmp_operand_value_1 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_condition_result_5 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_5 != false) {
            goto branch_yes_3;
        } else {
            goto branch_no_3;
        }
    }
    branch_yes_3:;
    {
        PyObject *tmp_raise_type_1;
        PyObject *tmp_raise_value_1;
        PyObject *tmp_mod_expr_left_1;
        PyObject *tmp_mod_expr_right_1;
        PyObject *tmp_tuple_element_3;
        PyObject *tmp_getattr_target_1;
        PyObject *tmp_getattr_attr_1;
        PyObject *tmp_getattr_default_1;
        tmp_raise_type_1 = PyExc_TypeError;
        tmp_mod_expr_left_1 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_getattr_target_1 = tmp_class_creation_1__metaclass;
        tmp_getattr_attr_1 = mod_consts[21];
        tmp_getattr_default_1 = mod_consts[22];
        tmp_tuple_element_3 = BUILTIN_GETATTR(tmp_getattr_target_1, tmp_getattr_attr_1, tmp_getattr_default_1);
        if (tmp_tuple_element_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        tmp_mod_expr_right_1 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_7;
            PyObject *tmp_type_arg_2;
            PyTuple_SET_ITEM(tmp_mod_expr_right_1, 0, tmp_tuple_element_3);
            CHECK_OBJECT(tmp_class_creation_1__prepared);
            tmp_type_arg_2 = tmp_class_creation_1__prepared;
            tmp_expression_value_7 = BUILTIN_TYPE1(tmp_type_arg_2);
            assert(!(tmp_expression_value_7 == NULL));
            tmp_tuple_element_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_7, mod_consts[21]);
            Py_DECREF(tmp_expression_value_7);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_1, 1, tmp_tuple_element_3);
        }
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_mod_expr_right_1);
        goto try_except_handler_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_raise_value_1 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_1, tmp_mod_expr_right_1);
        Py_DECREF(tmp_mod_expr_right_1);
        if (tmp_raise_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_1;
        }
        exception_type = tmp_raise_type_1;
        Py_INCREF(tmp_raise_type_1);
        exception_value = tmp_raise_value_1;
        exception_lineno = 34;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_1;
    }
    branch_no_3:;
    goto branch_end_2;
    branch_no_2:;
    {
        PyObject *tmp_assign_source_12;
        tmp_assign_source_12 = PyDict_New();
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_12;
    }
    branch_end_2:;
    {
        PyObject *tmp_assign_source_13;
        {
            PyObject *tmp_set_locals_1;
            CHECK_OBJECT(tmp_class_creation_1__prepared);
            tmp_set_locals_1 = tmp_class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34 = tmp_set_locals_1;
            Py_INCREF(tmp_set_locals_1);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_3;
        }
        tmp_dictset_value = mod_consts[25];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_3;
        }
        tmp_dictset_value = mod_consts[18];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_3;
        }
        if (isFrameUnusable(cache_frame_5cea5e801737c4e565477c4e5b13c74d_2)) {
            Py_XDECREF(cache_frame_5cea5e801737c4e565477c4e5b13c74d_2);

#if _DEBUG_REFCOUNTS
            if (cache_frame_5cea5e801737c4e565477c4e5b13c74d_2 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_5cea5e801737c4e565477c4e5b13c74d_2 = MAKE_FUNCTION_FRAME(codeobj_5cea5e801737c4e565477c4e5b13c74d, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_5cea5e801737c4e565477c4e5b13c74d_2->m_type_description == NULL);
        frame_5cea5e801737c4e565477c4e5b13c74d_2 = cache_frame_5cea5e801737c4e565477c4e5b13c74d_2;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_5cea5e801737c4e565477c4e5b13c74d_2);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_5cea5e801737c4e565477c4e5b13c74d_2) == 2); // Frame stack

        // Framed code:
        // Tried code:
        {
            PyObject *tmp_assign_source_14;
            PyObject *tmp_tuple_element_4;
            PyObject *tmp_expression_value_8;
            tmp_expression_value_8 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_8 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_8 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_8 == NULL)) {
                        tmp_expression_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_8 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 51;
                        type_description_2 = "o";
                        goto try_except_handler_4;
                    }
                    Py_INCREF(tmp_expression_value_8);
                } else {
                    goto try_except_handler_4;
                }
            }

            tmp_tuple_element_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_8, mod_consts[15]);
            Py_DECREF(tmp_expression_value_8);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_assign_source_14 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_14, 0, tmp_tuple_element_4);
            assert(tmp_TextAnnotation$class_creation_1__bases_orig == NULL);
            tmp_TextAnnotation$class_creation_1__bases_orig = tmp_assign_source_14;
        }
        {
            PyObject *tmp_assign_source_15;
            PyObject *tmp_dircall_arg1_2;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases_orig);
            tmp_dircall_arg1_2 = tmp_TextAnnotation$class_creation_1__bases_orig;
            Py_INCREF(tmp_dircall_arg1_2);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_2};
                tmp_assign_source_15 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_TextAnnotation$class_creation_1__bases == NULL);
            tmp_TextAnnotation$class_creation_1__bases = tmp_assign_source_15;
        }
        {
            PyObject *tmp_assign_source_16;
            tmp_assign_source_16 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_1__class_decl_dict == NULL);
            tmp_TextAnnotation$class_creation_1__class_decl_dict = tmp_assign_source_16;
        }
        {
            PyObject *tmp_assign_source_17;
            PyObject *tmp_metaclass_value_2;
            bool tmp_condition_result_6;
            PyObject *tmp_key_value_4;
            PyObject *tmp_dict_arg_value_4;
            PyObject *tmp_dict_arg_value_5;
            PyObject *tmp_key_value_5;
            nuitka_bool tmp_condition_result_7;
            int tmp_truth_name_2;
            PyObject *tmp_type_arg_3;
            PyObject *tmp_expression_value_9;
            PyObject *tmp_subscript_value_2;
            PyObject *tmp_bases_value_2;
            tmp_key_value_4 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_4 = tmp_TextAnnotation$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_4, tmp_key_value_4);
            assert(!(tmp_res == -1));
            tmp_condition_result_6 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_6 != false) {
                goto condexpr_true_3;
            } else {
                goto condexpr_false_3;
            }
            condexpr_true_3:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_5 = tmp_TextAnnotation$class_creation_1__class_decl_dict;
            tmp_key_value_5 = mod_consts[16];
            tmp_metaclass_value_2 = DICT_GET_ITEM0(tmp_dict_arg_value_5, tmp_key_value_5);
            if (tmp_metaclass_value_2 == NULL) {
                tmp_metaclass_value_2 = Py_None;
            }
            assert(!(tmp_metaclass_value_2 == NULL));
            Py_INCREF(tmp_metaclass_value_2);
            goto condexpr_end_3;
            condexpr_false_3:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_truth_name_2 = CHECK_IF_TRUE(tmp_TextAnnotation$class_creation_1__bases);
            if (tmp_truth_name_2 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_condition_result_7 = tmp_truth_name_2 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_7 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_4;
            } else {
                goto condexpr_false_4;
            }
            condexpr_true_4:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_expression_value_9 = tmp_TextAnnotation$class_creation_1__bases;
            tmp_subscript_value_2 = mod_consts[7];
            tmp_type_arg_3 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_9, tmp_subscript_value_2, 0);
            if (tmp_type_arg_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_metaclass_value_2 = BUILTIN_TYPE1(tmp_type_arg_3);
            Py_DECREF(tmp_type_arg_3);
            if (tmp_metaclass_value_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            goto condexpr_end_4;
            condexpr_false_4:;
            tmp_metaclass_value_2 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_2);
            condexpr_end_4:;
            condexpr_end_3:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_bases_value_2 = tmp_TextAnnotation$class_creation_1__bases;
            tmp_assign_source_17 = SELECT_METACLASS(tmp_metaclass_value_2, tmp_bases_value_2);
            Py_DECREF(tmp_metaclass_value_2);
            if (tmp_assign_source_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_TextAnnotation$class_creation_1__metaclass == NULL);
            tmp_TextAnnotation$class_creation_1__metaclass = tmp_assign_source_17;
        }
        {
            bool tmp_condition_result_8;
            PyObject *tmp_key_value_6;
            PyObject *tmp_dict_arg_value_6;
            tmp_key_value_6 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_6 = tmp_TextAnnotation$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_6, tmp_key_value_6);
            assert(!(tmp_res == -1));
            tmp_condition_result_8 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_8 != false) {
                goto branch_yes_4;
            } else {
                goto branch_no_4;
            }
        }
        branch_yes_4:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
        tmp_dictdel_dict = tmp_TextAnnotation$class_creation_1__class_decl_dict;
        tmp_dictdel_key = mod_consts[16];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_4;
        }
        branch_no_4:;
        {
            nuitka_bool tmp_condition_result_9;
            PyObject *tmp_expression_value_10;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__metaclass);
            tmp_expression_value_10 = tmp_TextAnnotation$class_creation_1__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_10, mod_consts[17]);
            tmp_condition_result_9 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_9 == NUITKA_BOOL_TRUE) {
                goto branch_yes_5;
            } else {
                goto branch_no_5;
            }
        }
        branch_yes_5:;
        {
            PyObject *tmp_assign_source_18;
            PyObject *tmp_called_value_3;
            PyObject *tmp_expression_value_11;
            PyObject *tmp_args_value_2;
            PyObject *tmp_tuple_element_5;
            PyObject *tmp_kwargs_value_2;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__metaclass);
            tmp_expression_value_11 = tmp_TextAnnotation$class_creation_1__metaclass;
            tmp_called_value_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_11, mod_consts[17]);
            if (tmp_called_value_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_tuple_element_5 = mod_consts[27];
            tmp_args_value_2 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_2, 0, tmp_tuple_element_5);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_tuple_element_5 = tmp_TextAnnotation$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_2, 1, tmp_tuple_element_5);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
            tmp_kwargs_value_2 = tmp_TextAnnotation$class_creation_1__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 51;
            tmp_assign_source_18 = CALL_FUNCTION(tmp_called_value_3, tmp_args_value_2, tmp_kwargs_value_2);
            Py_DECREF(tmp_called_value_3);
            Py_DECREF(tmp_args_value_2);
            if (tmp_assign_source_18 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_TextAnnotation$class_creation_1__prepared == NULL);
            tmp_TextAnnotation$class_creation_1__prepared = tmp_assign_source_18;
        }
        {
            bool tmp_condition_result_10;
            PyObject *tmp_operand_value_2;
            PyObject *tmp_expression_value_12;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__prepared);
            tmp_expression_value_12 = tmp_TextAnnotation$class_creation_1__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_12, mod_consts[19]);
            tmp_operand_value_2 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_2);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_condition_result_10 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_10 != false) {
                goto branch_yes_6;
            } else {
                goto branch_no_6;
            }
        }
        branch_yes_6:;
        {
            PyObject *tmp_raise_type_2;
            PyObject *tmp_raise_value_2;
            PyObject *tmp_mod_expr_left_2;
            PyObject *tmp_mod_expr_right_2;
            PyObject *tmp_tuple_element_6;
            PyObject *tmp_getattr_target_2;
            PyObject *tmp_getattr_attr_2;
            PyObject *tmp_getattr_default_2;
            tmp_raise_type_2 = PyExc_TypeError;
            tmp_mod_expr_left_2 = mod_consts[20];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__metaclass);
            tmp_getattr_target_2 = tmp_TextAnnotation$class_creation_1__metaclass;
            tmp_getattr_attr_2 = mod_consts[21];
            tmp_getattr_default_2 = mod_consts[22];
            tmp_tuple_element_6 = BUILTIN_GETATTR(tmp_getattr_target_2, tmp_getattr_attr_2, tmp_getattr_default_2);
            if (tmp_tuple_element_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_mod_expr_right_2 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_13;
                PyObject *tmp_type_arg_4;
                PyTuple_SET_ITEM(tmp_mod_expr_right_2, 0, tmp_tuple_element_6);
                CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__prepared);
                tmp_type_arg_4 = tmp_TextAnnotation$class_creation_1__prepared;
                tmp_expression_value_13 = BUILTIN_TYPE1(tmp_type_arg_4);
                assert(!(tmp_expression_value_13 == NULL));
                tmp_tuple_element_6 = LOOKUP_ATTRIBUTE(tmp_expression_value_13, mod_consts[21]);
                Py_DECREF(tmp_expression_value_13);
                if (tmp_tuple_element_6 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 51;
                    type_description_2 = "o";
                    goto tuple_build_exception_2;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_2, 1, tmp_tuple_element_6);
            }
            goto tuple_build_noexception_2;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_2:;
            Py_DECREF(tmp_mod_expr_right_2);
            goto try_except_handler_4;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_2:;
            tmp_raise_value_2 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_2, tmp_mod_expr_right_2);
            Py_DECREF(tmp_mod_expr_right_2);
            if (tmp_raise_value_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            exception_type = tmp_raise_type_2;
            Py_INCREF(tmp_raise_type_2);
            exception_value = tmp_raise_value_2;
            exception_lineno = 51;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_4;
        }
        branch_no_6:;
        goto branch_end_5;
        branch_no_5:;
        {
            PyObject *tmp_assign_source_19;
            tmp_assign_source_19 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_1__prepared == NULL);
            tmp_TextAnnotation$class_creation_1__prepared = tmp_assign_source_19;
        }
        branch_end_5:;
        {
            PyObject *tmp_set_locals_2;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__prepared);
            tmp_set_locals_2 = tmp_TextAnnotation$class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51 = tmp_set_locals_2;
            Py_INCREF(tmp_set_locals_2);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        tmp_dictset_value = mod_consts[28];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        tmp_dictset_value = mod_consts[29];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        if (isFrameUnusable(cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3)) {
            Py_XDECREF(cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3);

#if _DEBUG_REFCOUNTS
            if (cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3 = MAKE_FUNCTION_FRAME(codeobj_a410df66cd43733c8b52bbdf218dc5f8, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3->m_type_description == NULL);
        frame_a410df66cd43733c8b52bbdf218dc5f8_3 = cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_a410df66cd43733c8b52bbdf218dc5f8_3);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_a410df66cd43733c8b52bbdf218dc5f8_3) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_4;
            PyObject *tmp_expression_value_14;
            PyObject *tmp_args_value_3;
            PyObject *tmp_tuple_element_7;
            PyObject *tmp_expression_value_15;
            PyObject *tmp_kwargs_value_3;
            tmp_expression_value_14 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[6]);

            if (tmp_expression_value_14 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_14 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_14 == NULL)) {
                        tmp_expression_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_14 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 63;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_14);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_called_value_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_14, mod_consts[30]);
            Py_DECREF(tmp_expression_value_14);
            if (tmp_called_value_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_expression_value_15 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[6]);

            if (tmp_expression_value_15 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_15 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_15 == NULL)) {
                        tmp_expression_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_15 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_4);

                        exception_lineno = 64;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_15);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_tuple_element_7 = LOOKUP_ATTRIBUTE(tmp_expression_value_15, mod_consts[31]);
            Py_DECREF(tmp_expression_value_15);
            if (tmp_tuple_element_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_4);

                exception_lineno = 64;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_args_value_3 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_3, 0, tmp_tuple_element_7);
            tmp_kwargs_value_3 = PyDict_Copy(mod_consts[32]);
            frame_a410df66cd43733c8b52bbdf218dc5f8_3->m_frame.f_lineno = 63;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_4, tmp_args_value_3, tmp_kwargs_value_3);
            Py_DECREF(tmp_called_value_4);
            Py_DECREF(tmp_args_value_3);
            Py_DECREF(tmp_kwargs_value_3);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[33], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 63;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
        }
        {
            PyObject *tmp_called_value_5;
            PyObject *tmp_expression_value_16;
            PyObject *tmp_args_value_4;
            PyObject *tmp_tuple_element_8;
            PyObject *tmp_expression_value_17;
            PyObject *tmp_kwargs_value_4;
            tmp_expression_value_16 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[6]);

            if (tmp_expression_value_16 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_16 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_16 == NULL)) {
                        tmp_expression_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_16 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 67;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_16);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_called_value_5 = LOOKUP_ATTRIBUTE(tmp_expression_value_16, mod_consts[30]);
            Py_DECREF(tmp_expression_value_16);
            if (tmp_called_value_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_expression_value_17 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[6]);

            if (tmp_expression_value_17 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_17 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_17 == NULL)) {
                        tmp_expression_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_17 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_5);

                        exception_lineno = 68;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_17);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_tuple_element_8 = LOOKUP_ATTRIBUTE(tmp_expression_value_17, mod_consts[34]);
            Py_DECREF(tmp_expression_value_17);
            if (tmp_tuple_element_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_5);

                exception_lineno = 68;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_args_value_4 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_4, 0, tmp_tuple_element_8);
            tmp_kwargs_value_4 = PyDict_Copy(mod_consts[35]);
            frame_a410df66cd43733c8b52bbdf218dc5f8_3->m_frame.f_lineno = 67;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_5, tmp_args_value_4, tmp_kwargs_value_4);
            Py_DECREF(tmp_called_value_5);
            Py_DECREF(tmp_args_value_4);
            Py_DECREF(tmp_kwargs_value_4);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 67;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_a410df66cd43733c8b52bbdf218dc5f8_3);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_1;

        frame_exception_exit_3:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_a410df66cd43733c8b52bbdf218dc5f8_3);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_a410df66cd43733c8b52bbdf218dc5f8_3, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_a410df66cd43733c8b52bbdf218dc5f8_3->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_a410df66cd43733c8b52bbdf218dc5f8_3, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_a410df66cd43733c8b52bbdf218dc5f8_3,
            type_description_3,
            outline_1_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_a410df66cd43733c8b52bbdf218dc5f8_3 == cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3);
            cache_frame_a410df66cd43733c8b52bbdf218dc5f8_3 = NULL;
        }

        assertFrameObject(frame_a410df66cd43733c8b52bbdf218dc5f8_3);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_2;

        frame_no_exception_1:;
        goto skip_nested_handling_1;
        nested_frame_exit_2:;
        type_description_2 = "o";
        goto try_except_handler_6;
        skip_nested_handling_1:;
        {
            nuitka_bool tmp_condition_result_11;
            PyObject *tmp_cmp_expr_left_1;
            PyObject *tmp_cmp_expr_right_1;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_cmp_expr_left_1 = tmp_TextAnnotation$class_creation_1__bases;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases_orig);
            tmp_cmp_expr_right_1 = tmp_TextAnnotation$class_creation_1__bases_orig;
            tmp_condition_result_11 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
            if (tmp_condition_result_11 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_6;
            }
            if (tmp_condition_result_11 == NUITKA_BOOL_TRUE) {
                goto branch_yes_7;
            } else {
                goto branch_no_7;
            }
        }
        branch_yes_7:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases_orig);
        tmp_dictset_value = tmp_TextAnnotation$class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        branch_no_7:;
        {
            PyObject *tmp_assign_source_20;
            PyObject *tmp_called_value_6;
            PyObject *tmp_args_value_5;
            PyObject *tmp_tuple_element_9;
            PyObject *tmp_kwargs_value_5;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__metaclass);
            tmp_called_value_6 = tmp_TextAnnotation$class_creation_1__metaclass;
            tmp_tuple_element_9 = mod_consts[27];
            tmp_args_value_5 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_5, 0, tmp_tuple_element_9);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
            tmp_tuple_element_9 = tmp_TextAnnotation$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_5, 1, tmp_tuple_element_9);
            tmp_tuple_element_9 = locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51;
            PyTuple_SET_ITEM0(tmp_args_value_5, 2, tmp_tuple_element_9);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
            tmp_kwargs_value_5 = tmp_TextAnnotation$class_creation_1__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 51;
            tmp_assign_source_20 = CALL_FUNCTION(tmp_called_value_6, tmp_args_value_5, tmp_kwargs_value_5);
            Py_DECREF(tmp_args_value_5);
            if (tmp_assign_source_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 51;
                type_description_2 = "o";
                goto try_except_handler_6;
            }
            assert(outline_1_var___class__ == NULL);
            outline_1_var___class__ = tmp_assign_source_20;
        }
        CHECK_OBJECT(outline_1_var___class__);
        tmp_dictset_value = outline_1_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_6;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_6:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51 = NULL;
        goto try_return_handler_5;
        // Exception handler code:
        try_except_handler_6:;
        exception_keeper_type_1 = exception_type;
        exception_keeper_value_1 = exception_value;
        exception_keeper_tb_1 = exception_tb;
        exception_keeper_lineno_1 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__2_DetectedLanguage_51 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_1;
        exception_value = exception_keeper_value_1;
        exception_tb = exception_keeper_tb_1;
        exception_lineno = exception_keeper_lineno_1;

        goto try_except_handler_5;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_5:;
        CHECK_OBJECT(outline_1_var___class__);
        Py_DECREF(outline_1_var___class__);
        outline_1_var___class__ = NULL;
        goto outline_result_2;
        // Exception handler code:
        try_except_handler_5:;
        exception_keeper_type_2 = exception_type;
        exception_keeper_value_2 = exception_value;
        exception_keeper_tb_2 = exception_tb;
        exception_keeper_lineno_2 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_2;
        exception_value = exception_keeper_value_2;
        exception_tb = exception_keeper_tb_2;
        exception_lineno = exception_keeper_lineno_2;

        goto outline_exception_2;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_2:;
        exception_lineno = 51;
        goto try_except_handler_4;
        outline_result_2:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[27], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_2 = "o";
            goto try_except_handler_4;
        }
        goto try_end_1;
        // Exception handler code:
        try_except_handler_4:;
        exception_keeper_type_3 = exception_type;
        exception_keeper_value_3 = exception_value;
        exception_keeper_tb_3 = exception_tb;
        exception_keeper_lineno_3 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_TextAnnotation$class_creation_1__bases_orig);
        tmp_TextAnnotation$class_creation_1__bases_orig = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_1__bases);
        tmp_TextAnnotation$class_creation_1__bases = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_1__class_decl_dict);
        tmp_TextAnnotation$class_creation_1__class_decl_dict = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_1__metaclass);
        tmp_TextAnnotation$class_creation_1__metaclass = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_1__prepared);
        tmp_TextAnnotation$class_creation_1__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_3;
        exception_value = exception_keeper_value_3;
        exception_tb = exception_keeper_tb_3;
        exception_lineno = exception_keeper_lineno_3;

        goto frame_exception_exit_2;
        // End of try:
        try_end_1:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases_orig);
        Py_DECREF(tmp_TextAnnotation$class_creation_1__bases_orig);
        tmp_TextAnnotation$class_creation_1__bases_orig = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__bases);
        Py_DECREF(tmp_TextAnnotation$class_creation_1__bases);
        tmp_TextAnnotation$class_creation_1__bases = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__class_decl_dict);
        Py_DECREF(tmp_TextAnnotation$class_creation_1__class_decl_dict);
        tmp_TextAnnotation$class_creation_1__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__metaclass);
        Py_DECREF(tmp_TextAnnotation$class_creation_1__metaclass);
        tmp_TextAnnotation$class_creation_1__metaclass = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_1__prepared);
        Py_DECREF(tmp_TextAnnotation$class_creation_1__prepared);
        tmp_TextAnnotation$class_creation_1__prepared = NULL;
        // Tried code:
        {
            PyObject *tmp_assign_source_21;
            PyObject *tmp_tuple_element_10;
            PyObject *tmp_expression_value_18;
            tmp_expression_value_18 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_18 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_18 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_18 == NULL)) {
                        tmp_expression_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_18 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 72;
                        type_description_2 = "o";
                        goto try_except_handler_7;
                    }
                    Py_INCREF(tmp_expression_value_18);
                } else {
                    goto try_except_handler_7;
                }
            }

            tmp_tuple_element_10 = LOOKUP_ATTRIBUTE(tmp_expression_value_18, mod_consts[15]);
            Py_DECREF(tmp_expression_value_18);
            if (tmp_tuple_element_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_assign_source_21 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_21, 0, tmp_tuple_element_10);
            assert(tmp_TextAnnotation$class_creation_2__bases_orig == NULL);
            tmp_TextAnnotation$class_creation_2__bases_orig = tmp_assign_source_21;
        }
        {
            PyObject *tmp_assign_source_22;
            PyObject *tmp_dircall_arg1_3;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases_orig);
            tmp_dircall_arg1_3 = tmp_TextAnnotation$class_creation_2__bases_orig;
            Py_INCREF(tmp_dircall_arg1_3);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_3};
                tmp_assign_source_22 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_TextAnnotation$class_creation_2__bases == NULL);
            tmp_TextAnnotation$class_creation_2__bases = tmp_assign_source_22;
        }
        {
            PyObject *tmp_assign_source_23;
            tmp_assign_source_23 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_2__class_decl_dict == NULL);
            tmp_TextAnnotation$class_creation_2__class_decl_dict = tmp_assign_source_23;
        }
        {
            PyObject *tmp_assign_source_24;
            PyObject *tmp_metaclass_value_3;
            bool tmp_condition_result_12;
            PyObject *tmp_key_value_7;
            PyObject *tmp_dict_arg_value_7;
            PyObject *tmp_dict_arg_value_8;
            PyObject *tmp_key_value_8;
            nuitka_bool tmp_condition_result_13;
            int tmp_truth_name_3;
            PyObject *tmp_type_arg_5;
            PyObject *tmp_expression_value_19;
            PyObject *tmp_subscript_value_3;
            PyObject *tmp_bases_value_3;
            tmp_key_value_7 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_7 = tmp_TextAnnotation$class_creation_2__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_7, tmp_key_value_7);
            assert(!(tmp_res == -1));
            tmp_condition_result_12 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_12 != false) {
                goto condexpr_true_5;
            } else {
                goto condexpr_false_5;
            }
            condexpr_true_5:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_8 = tmp_TextAnnotation$class_creation_2__class_decl_dict;
            tmp_key_value_8 = mod_consts[16];
            tmp_metaclass_value_3 = DICT_GET_ITEM0(tmp_dict_arg_value_8, tmp_key_value_8);
            if (tmp_metaclass_value_3 == NULL) {
                tmp_metaclass_value_3 = Py_None;
            }
            assert(!(tmp_metaclass_value_3 == NULL));
            Py_INCREF(tmp_metaclass_value_3);
            goto condexpr_end_5;
            condexpr_false_5:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_truth_name_3 = CHECK_IF_TRUE(tmp_TextAnnotation$class_creation_2__bases);
            if (tmp_truth_name_3 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_condition_result_13 = tmp_truth_name_3 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_13 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_6;
            } else {
                goto condexpr_false_6;
            }
            condexpr_true_6:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_expression_value_19 = tmp_TextAnnotation$class_creation_2__bases;
            tmp_subscript_value_3 = mod_consts[7];
            tmp_type_arg_5 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_19, tmp_subscript_value_3, 0);
            if (tmp_type_arg_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_metaclass_value_3 = BUILTIN_TYPE1(tmp_type_arg_5);
            Py_DECREF(tmp_type_arg_5);
            if (tmp_metaclass_value_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            goto condexpr_end_6;
            condexpr_false_6:;
            tmp_metaclass_value_3 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_3);
            condexpr_end_6:;
            condexpr_end_5:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_bases_value_3 = tmp_TextAnnotation$class_creation_2__bases;
            tmp_assign_source_24 = SELECT_METACLASS(tmp_metaclass_value_3, tmp_bases_value_3);
            Py_DECREF(tmp_metaclass_value_3);
            if (tmp_assign_source_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_TextAnnotation$class_creation_2__metaclass == NULL);
            tmp_TextAnnotation$class_creation_2__metaclass = tmp_assign_source_24;
        }
        {
            bool tmp_condition_result_14;
            PyObject *tmp_key_value_9;
            PyObject *tmp_dict_arg_value_9;
            tmp_key_value_9 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_9 = tmp_TextAnnotation$class_creation_2__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_9, tmp_key_value_9);
            assert(!(tmp_res == -1));
            tmp_condition_result_14 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_14 != false) {
                goto branch_yes_8;
            } else {
                goto branch_no_8;
            }
        }
        branch_yes_8:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
        tmp_dictdel_dict = tmp_TextAnnotation$class_creation_2__class_decl_dict;
        tmp_dictdel_key = mod_consts[16];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        branch_no_8:;
        {
            nuitka_bool tmp_condition_result_15;
            PyObject *tmp_expression_value_20;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__metaclass);
            tmp_expression_value_20 = tmp_TextAnnotation$class_creation_2__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_20, mod_consts[17]);
            tmp_condition_result_15 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_15 == NUITKA_BOOL_TRUE) {
                goto branch_yes_9;
            } else {
                goto branch_no_9;
            }
        }
        branch_yes_9:;
        {
            PyObject *tmp_assign_source_25;
            PyObject *tmp_called_value_7;
            PyObject *tmp_expression_value_21;
            PyObject *tmp_args_value_6;
            PyObject *tmp_tuple_element_11;
            PyObject *tmp_kwargs_value_6;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__metaclass);
            tmp_expression_value_21 = tmp_TextAnnotation$class_creation_2__metaclass;
            tmp_called_value_7 = LOOKUP_ATTRIBUTE(tmp_expression_value_21, mod_consts[17]);
            if (tmp_called_value_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_tuple_element_11 = mod_consts[38];
            tmp_args_value_6 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_6, 0, tmp_tuple_element_11);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_tuple_element_11 = tmp_TextAnnotation$class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_6, 1, tmp_tuple_element_11);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
            tmp_kwargs_value_6 = tmp_TextAnnotation$class_creation_2__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 72;
            tmp_assign_source_25 = CALL_FUNCTION(tmp_called_value_7, tmp_args_value_6, tmp_kwargs_value_6);
            Py_DECREF(tmp_called_value_7);
            Py_DECREF(tmp_args_value_6);
            if (tmp_assign_source_25 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_TextAnnotation$class_creation_2__prepared == NULL);
            tmp_TextAnnotation$class_creation_2__prepared = tmp_assign_source_25;
        }
        {
            bool tmp_condition_result_16;
            PyObject *tmp_operand_value_3;
            PyObject *tmp_expression_value_22;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__prepared);
            tmp_expression_value_22 = tmp_TextAnnotation$class_creation_2__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_22, mod_consts[19]);
            tmp_operand_value_3 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_3);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_condition_result_16 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_16 != false) {
                goto branch_yes_10;
            } else {
                goto branch_no_10;
            }
        }
        branch_yes_10:;
        {
            PyObject *tmp_raise_type_3;
            PyObject *tmp_raise_value_3;
            PyObject *tmp_mod_expr_left_3;
            PyObject *tmp_mod_expr_right_3;
            PyObject *tmp_tuple_element_12;
            PyObject *tmp_getattr_target_3;
            PyObject *tmp_getattr_attr_3;
            PyObject *tmp_getattr_default_3;
            tmp_raise_type_3 = PyExc_TypeError;
            tmp_mod_expr_left_3 = mod_consts[20];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__metaclass);
            tmp_getattr_target_3 = tmp_TextAnnotation$class_creation_2__metaclass;
            tmp_getattr_attr_3 = mod_consts[21];
            tmp_getattr_default_3 = mod_consts[22];
            tmp_tuple_element_12 = BUILTIN_GETATTR(tmp_getattr_target_3, tmp_getattr_attr_3, tmp_getattr_default_3);
            if (tmp_tuple_element_12 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_mod_expr_right_3 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_23;
                PyObject *tmp_type_arg_6;
                PyTuple_SET_ITEM(tmp_mod_expr_right_3, 0, tmp_tuple_element_12);
                CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__prepared);
                tmp_type_arg_6 = tmp_TextAnnotation$class_creation_2__prepared;
                tmp_expression_value_23 = BUILTIN_TYPE1(tmp_type_arg_6);
                assert(!(tmp_expression_value_23 == NULL));
                tmp_tuple_element_12 = LOOKUP_ATTRIBUTE(tmp_expression_value_23, mod_consts[21]);
                Py_DECREF(tmp_expression_value_23);
                if (tmp_tuple_element_12 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 72;
                    type_description_2 = "o";
                    goto tuple_build_exception_3;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_3, 1, tmp_tuple_element_12);
            }
            goto tuple_build_noexception_3;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_3:;
            Py_DECREF(tmp_mod_expr_right_3);
            goto try_except_handler_7;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_3:;
            tmp_raise_value_3 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_3, tmp_mod_expr_right_3);
            Py_DECREF(tmp_mod_expr_right_3);
            if (tmp_raise_value_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            exception_type = tmp_raise_type_3;
            Py_INCREF(tmp_raise_type_3);
            exception_value = tmp_raise_value_3;
            exception_lineno = 72;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        branch_no_10:;
        goto branch_end_9;
        branch_no_9:;
        {
            PyObject *tmp_assign_source_26;
            tmp_assign_source_26 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_2__prepared == NULL);
            tmp_TextAnnotation$class_creation_2__prepared = tmp_assign_source_26;
        }
        branch_end_9:;
        {
            PyObject *tmp_set_locals_3;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__prepared);
            tmp_set_locals_3 = tmp_TextAnnotation$class_creation_2__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72 = tmp_set_locals_3;
            Py_INCREF(tmp_set_locals_3);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        tmp_dictset_value = mod_consts[39];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        tmp_dictset_value = mod_consts[40];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        if (isFrameUnusable(cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4)) {
            Py_XDECREF(cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4);

#if _DEBUG_REFCOUNTS
            if (cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4 = MAKE_FUNCTION_FRAME(codeobj_1e57d9201f75c5f420f63ce5688a3e8b, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_type_description == NULL);
        frame_1e57d9201f75c5f420f63ce5688a3e8b_4 = cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_1e57d9201f75c5f420f63ce5688a3e8b_4);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_1e57d9201f75c5f420f63ce5688a3e8b_4) == 2); // Frame stack

        // Framed code:
        // Tried code:
        {
            PyObject *tmp_assign_source_27;
            PyObject *tmp_tuple_element_13;
            PyObject *tmp_expression_value_24;
            tmp_expression_value_24 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[6]);

            if (tmp_expression_value_24 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_24 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_24 == NULL)) {
                        tmp_expression_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_24 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 82;
                        type_description_3 = "o";
                        goto try_except_handler_10;
                    }
                    Py_INCREF(tmp_expression_value_24);
                } else {
                    goto try_except_handler_10;
                }
            }

            tmp_tuple_element_13 = LOOKUP_ATTRIBUTE(tmp_expression_value_24, mod_consts[41]);
            Py_DECREF(tmp_expression_value_24);
            if (tmp_tuple_element_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_assign_source_27 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_27, 0, tmp_tuple_element_13);
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig = tmp_assign_source_27;
        }
        {
            PyObject *tmp_assign_source_28;
            PyObject *tmp_dircall_arg1_4;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
            tmp_dircall_arg1_4 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig;
            Py_INCREF(tmp_dircall_arg1_4);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_4};
                tmp_assign_source_28 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__bases = tmp_assign_source_28;
        }
        {
            PyObject *tmp_assign_source_29;
            tmp_assign_source_29 = PyDict_New();
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict = tmp_assign_source_29;
        }
        {
            PyObject *tmp_assign_source_30;
            PyObject *tmp_metaclass_value_4;
            bool tmp_condition_result_17;
            PyObject *tmp_key_value_10;
            PyObject *tmp_dict_arg_value_10;
            PyObject *tmp_dict_arg_value_11;
            PyObject *tmp_key_value_11;
            nuitka_bool tmp_condition_result_18;
            int tmp_truth_name_4;
            PyObject *tmp_type_arg_7;
            PyObject *tmp_expression_value_25;
            PyObject *tmp_subscript_value_4;
            PyObject *tmp_bases_value_4;
            tmp_key_value_10 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_10 = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_10, tmp_key_value_10);
            assert(!(tmp_res == -1));
            tmp_condition_result_17 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_17 != false) {
                goto condexpr_true_7;
            } else {
                goto condexpr_false_7;
            }
            condexpr_true_7:;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_11 = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
            tmp_key_value_11 = mod_consts[16];
            tmp_metaclass_value_4 = DICT_GET_ITEM0(tmp_dict_arg_value_11, tmp_key_value_11);
            if (tmp_metaclass_value_4 == NULL) {
                tmp_metaclass_value_4 = Py_None;
            }
            assert(!(tmp_metaclass_value_4 == NULL));
            Py_INCREF(tmp_metaclass_value_4);
            goto condexpr_end_7;
            condexpr_false_7:;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_truth_name_4 = CHECK_IF_TRUE(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            if (tmp_truth_name_4 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_condition_result_18 = tmp_truth_name_4 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_18 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_8;
            } else {
                goto condexpr_false_8;
            }
            condexpr_true_8:;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_expression_value_25 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases;
            tmp_subscript_value_4 = mod_consts[7];
            tmp_type_arg_7 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_25, tmp_subscript_value_4, 0);
            if (tmp_type_arg_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_metaclass_value_4 = BUILTIN_TYPE1(tmp_type_arg_7);
            Py_DECREF(tmp_type_arg_7);
            if (tmp_metaclass_value_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            goto condexpr_end_8;
            condexpr_false_8:;
            tmp_metaclass_value_4 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_4);
            condexpr_end_8:;
            condexpr_end_7:;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_bases_value_4 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases;
            tmp_assign_source_30 = SELECT_METACLASS(tmp_metaclass_value_4, tmp_bases_value_4);
            Py_DECREF(tmp_metaclass_value_4);
            if (tmp_assign_source_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass = tmp_assign_source_30;
        }
        {
            bool tmp_condition_result_19;
            PyObject *tmp_key_value_12;
            PyObject *tmp_dict_arg_value_12;
            tmp_key_value_12 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_12 = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_12, tmp_key_value_12);
            assert(!(tmp_res == -1));
            tmp_condition_result_19 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_19 != false) {
                goto branch_yes_11;
            } else {
                goto branch_no_11;
            }
        }
        branch_yes_11:;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
        tmp_dictdel_dict = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
        tmp_dictdel_key = mod_consts[16];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_10;
        }
        branch_no_11:;
        {
            nuitka_bool tmp_condition_result_20;
            PyObject *tmp_expression_value_26;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
            tmp_expression_value_26 = tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_26, mod_consts[17]);
            tmp_condition_result_20 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_20 == NUITKA_BOOL_TRUE) {
                goto branch_yes_12;
            } else {
                goto branch_no_12;
            }
        }
        branch_yes_12:;
        {
            PyObject *tmp_assign_source_31;
            PyObject *tmp_called_value_8;
            PyObject *tmp_expression_value_27;
            PyObject *tmp_args_value_7;
            PyObject *tmp_tuple_element_14;
            PyObject *tmp_kwargs_value_7;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
            tmp_expression_value_27 = tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass;
            tmp_called_value_8 = LOOKUP_ATTRIBUTE(tmp_expression_value_27, mod_consts[17]);
            if (tmp_called_value_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_tuple_element_14 = mod_consts[42];
            tmp_args_value_7 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_7, 0, tmp_tuple_element_14);
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_tuple_element_14 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_7, 1, tmp_tuple_element_14);
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
            tmp_kwargs_value_7 = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
            frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_frame.f_lineno = 82;
            tmp_assign_source_31 = CALL_FUNCTION(tmp_called_value_8, tmp_args_value_7, tmp_kwargs_value_7);
            Py_DECREF(tmp_called_value_8);
            Py_DECREF(tmp_args_value_7);
            if (tmp_assign_source_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared = tmp_assign_source_31;
        }
        {
            bool tmp_condition_result_21;
            PyObject *tmp_operand_value_4;
            PyObject *tmp_expression_value_28;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
            tmp_expression_value_28 = tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_28, mod_consts[19]);
            tmp_operand_value_4 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_4);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_condition_result_21 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_21 != false) {
                goto branch_yes_13;
            } else {
                goto branch_no_13;
            }
        }
        branch_yes_13:;
        {
            PyObject *tmp_raise_type_4;
            PyObject *tmp_raise_value_4;
            PyObject *tmp_mod_expr_left_4;
            PyObject *tmp_mod_expr_right_4;
            PyObject *tmp_tuple_element_15;
            PyObject *tmp_getattr_target_4;
            PyObject *tmp_getattr_attr_4;
            PyObject *tmp_getattr_default_4;
            tmp_raise_type_4 = PyExc_TypeError;
            tmp_mod_expr_left_4 = mod_consts[20];
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
            tmp_getattr_target_4 = tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass;
            tmp_getattr_attr_4 = mod_consts[21];
            tmp_getattr_default_4 = mod_consts[22];
            tmp_tuple_element_15 = BUILTIN_GETATTR(tmp_getattr_target_4, tmp_getattr_attr_4, tmp_getattr_default_4);
            if (tmp_tuple_element_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            tmp_mod_expr_right_4 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_29;
                PyObject *tmp_type_arg_8;
                PyTuple_SET_ITEM(tmp_mod_expr_right_4, 0, tmp_tuple_element_15);
                CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
                tmp_type_arg_8 = tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared;
                tmp_expression_value_29 = BUILTIN_TYPE1(tmp_type_arg_8);
                assert(!(tmp_expression_value_29 == NULL));
                tmp_tuple_element_15 = LOOKUP_ATTRIBUTE(tmp_expression_value_29, mod_consts[21]);
                Py_DECREF(tmp_expression_value_29);
                if (tmp_tuple_element_15 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 82;
                    type_description_3 = "o";
                    goto tuple_build_exception_4;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_4, 1, tmp_tuple_element_15);
            }
            goto tuple_build_noexception_4;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_4:;
            Py_DECREF(tmp_mod_expr_right_4);
            goto try_except_handler_10;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_4:;
            tmp_raise_value_4 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_4, tmp_mod_expr_right_4);
            Py_DECREF(tmp_mod_expr_right_4);
            if (tmp_raise_value_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_10;
            }
            exception_type = tmp_raise_type_4;
            Py_INCREF(tmp_raise_type_4);
            exception_value = tmp_raise_value_4;
            exception_lineno = 82;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_3 = "o";
            goto try_except_handler_10;
        }
        branch_no_13:;
        goto branch_end_12;
        branch_no_12:;
        {
            PyObject *tmp_assign_source_32;
            tmp_assign_source_32 = PyDict_New();
            assert(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared == NULL);
            tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared = tmp_assign_source_32;
        }
        branch_end_12:;
        {
            PyObject *tmp_set_locals_4;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
            tmp_set_locals_4 = tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82 = tmp_set_locals_4;
            Py_INCREF(tmp_set_locals_4);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_12;
        }
        tmp_dictset_value = mod_consts[43];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_12;
        }
        tmp_dictset_value = mod_consts[44];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_12;
        }
        if (isFrameUnusable(cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5)) {
            Py_XDECREF(cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);

#if _DEBUG_REFCOUNTS
            if (cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 = MAKE_FUNCTION_FRAME(codeobj_e8ffb51946009f1f43fd70dc3ae4c8bb, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5->m_type_description == NULL);
        frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 = cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5) == 2); // Frame stack

        // Framed code:
        tmp_dictset_value = mod_consts[7];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[45], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 84;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }
        tmp_dictset_value = mod_consts[46];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[47], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 85;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }
        tmp_dictset_value = mod_consts[48];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[49], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 86;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }
        tmp_dictset_value = mod_consts[50];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[51], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 87;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }
        tmp_dictset_value = mod_consts[52];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[53], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 88;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }
        tmp_dictset_value = mod_consts[54];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[55], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 89;
            type_description_4 = "o";
            goto frame_exception_exit_5;
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_2;

        frame_exception_exit_5:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5,
            type_description_4,
            outline_3_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 == cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);
            cache_frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5 = NULL;
        }

        assertFrameObject(frame_e8ffb51946009f1f43fd70dc3ae4c8bb_5);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_4;

        frame_no_exception_2:;
        goto skip_nested_handling_2;
        nested_frame_exit_4:;
        type_description_3 = "o";
        goto try_except_handler_12;
        skip_nested_handling_2:;
        {
            nuitka_bool tmp_condition_result_22;
            PyObject *tmp_cmp_expr_left_2;
            PyObject *tmp_cmp_expr_right_2;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_cmp_expr_left_2 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
            tmp_cmp_expr_right_2 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig;
            tmp_condition_result_22 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_2, tmp_cmp_expr_right_2);
            if (tmp_condition_result_22 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_12;
            }
            if (tmp_condition_result_22 == NUITKA_BOOL_TRUE) {
                goto branch_yes_14;
            } else {
                goto branch_no_14;
            }
        }
        branch_yes_14:;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
        tmp_dictset_value = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_12;
        }
        branch_no_14:;
        {
            PyObject *tmp_assign_source_33;
            PyObject *tmp_called_value_9;
            PyObject *tmp_args_value_8;
            PyObject *tmp_tuple_element_16;
            PyObject *tmp_kwargs_value_8;
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
            tmp_called_value_9 = tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass;
            tmp_tuple_element_16 = mod_consts[42];
            tmp_args_value_8 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_8, 0, tmp_tuple_element_16);
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
            tmp_tuple_element_16 = tmp_TextAnnotation$DetectedBreak$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_8, 1, tmp_tuple_element_16);
            tmp_tuple_element_16 = locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82;
            PyTuple_SET_ITEM0(tmp_args_value_8, 2, tmp_tuple_element_16);
            CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
            tmp_kwargs_value_8 = tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict;
            frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_frame.f_lineno = 82;
            tmp_assign_source_33 = CALL_FUNCTION(tmp_called_value_9, tmp_args_value_8, tmp_kwargs_value_8);
            Py_DECREF(tmp_args_value_8);
            if (tmp_assign_source_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_3 = "o";
                goto try_except_handler_12;
            }
            assert(outline_3_var___class__ == NULL);
            outline_3_var___class__ = tmp_assign_source_33;
        }
        CHECK_OBJECT(outline_3_var___class__);
        tmp_dictset_value = outline_3_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_12;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_12:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82 = NULL;
        goto try_return_handler_11;
        // Exception handler code:
        try_except_handler_12:;
        exception_keeper_type_4 = exception_type;
        exception_keeper_value_4 = exception_value;
        exception_keeper_tb_4 = exception_tb;
        exception_keeper_lineno_4 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__4_BreakType_82 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_4;
        exception_value = exception_keeper_value_4;
        exception_tb = exception_keeper_tb_4;
        exception_lineno = exception_keeper_lineno_4;

        goto try_except_handler_11;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_11:;
        CHECK_OBJECT(outline_3_var___class__);
        Py_DECREF(outline_3_var___class__);
        outline_3_var___class__ = NULL;
        goto outline_result_4;
        // Exception handler code:
        try_except_handler_11:;
        exception_keeper_type_5 = exception_type;
        exception_keeper_value_5 = exception_value;
        exception_keeper_tb_5 = exception_tb;
        exception_keeper_lineno_5 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_5;
        exception_value = exception_keeper_value_5;
        exception_tb = exception_keeper_tb_5;
        exception_lineno = exception_keeper_lineno_5;

        goto outline_exception_4;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_4:;
        exception_lineno = 82;
        goto try_except_handler_10;
        outline_result_4:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[42], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_3 = "o";
            goto try_except_handler_10;
        }
        goto try_end_2;
        // Exception handler code:
        try_except_handler_10:;
        exception_keeper_type_6 = exception_type;
        exception_keeper_value_6 = exception_value;
        exception_keeper_tb_6 = exception_tb;
        exception_keeper_lineno_6 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig = NULL;
        Py_XDECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__bases = NULL;
        Py_XDECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict = NULL;
        Py_XDECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass = NULL;
        Py_XDECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_6;
        exception_value = exception_keeper_value_6;
        exception_tb = exception_keeper_tb_6;
        exception_lineno = exception_keeper_lineno_6;

        goto frame_exception_exit_4;
        // End of try:
        try_end_2:;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
        Py_DECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__bases_orig = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
        Py_DECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__bases);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__bases = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
        Py_DECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
        Py_DECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__metaclass = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
        Py_DECREF(tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared);
        tmp_TextAnnotation$DetectedBreak$class_creation_1__prepared = NULL;
        {
            PyObject *tmp_called_value_10;
            PyObject *tmp_expression_value_30;
            PyObject *tmp_args_value_9;
            PyObject *tmp_tuple_element_17;
            PyObject *tmp_expression_value_31;
            PyObject *tmp_kwargs_value_9;
            tmp_expression_value_30 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[6]);

            if (tmp_expression_value_30 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_30 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_30 == NULL)) {
                        tmp_expression_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_30 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 91;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_30);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_called_value_10 = LOOKUP_ATTRIBUTE(tmp_expression_value_30, mod_consts[30]);
            Py_DECREF(tmp_expression_value_30);
            if (tmp_called_value_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 91;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_expression_value_31 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[6]);

            if (tmp_expression_value_31 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_31 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_31 == NULL)) {
                        tmp_expression_value_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_31 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_10);

                        exception_lineno = 92;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_31);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_tuple_element_17 = LOOKUP_ATTRIBUTE(tmp_expression_value_31, mod_consts[56]);
            Py_DECREF(tmp_expression_value_31);
            if (tmp_tuple_element_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_10);

                exception_lineno = 92;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_args_value_9 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_9, 0, tmp_tuple_element_17);
            tmp_kwargs_value_9 = PyDict_Copy(mod_consts[57]);
            frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_frame.f_lineno = 91;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_10, tmp_args_value_9, tmp_kwargs_value_9);
            Py_DECREF(tmp_called_value_10);
            Py_DECREF(tmp_args_value_9);
            Py_DECREF(tmp_kwargs_value_9);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 91;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[58], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 91;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
        }
        {
            PyObject *tmp_called_value_11;
            PyObject *tmp_expression_value_32;
            PyObject *tmp_args_value_10;
            PyObject *tmp_tuple_element_18;
            PyObject *tmp_expression_value_33;
            PyObject *tmp_kwargs_value_10;
            tmp_expression_value_32 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[6]);

            if (tmp_expression_value_32 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_32 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_32 == NULL)) {
                        tmp_expression_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_32 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 96;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_32);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_called_value_11 = LOOKUP_ATTRIBUTE(tmp_expression_value_32, mod_consts[30]);
            Py_DECREF(tmp_expression_value_32);
            if (tmp_called_value_11 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 96;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_expression_value_33 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[6]);

            if (tmp_expression_value_33 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_33 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_33 == NULL)) {
                        tmp_expression_value_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_33 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_11);

                        exception_lineno = 97;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_33);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_tuple_element_18 = LOOKUP_ATTRIBUTE(tmp_expression_value_33, mod_consts[59]);
            Py_DECREF(tmp_expression_value_33);
            if (tmp_tuple_element_18 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_11);

                exception_lineno = 97;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_args_value_10 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_10, 0, tmp_tuple_element_18);
            tmp_kwargs_value_10 = PyDict_Copy(mod_consts[35]);
            frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_frame.f_lineno = 96;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_11, tmp_args_value_10, tmp_kwargs_value_10);
            Py_DECREF(tmp_called_value_11);
            Py_DECREF(tmp_args_value_10);
            Py_DECREF(tmp_kwargs_value_10);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 96;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[60], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 96;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_1e57d9201f75c5f420f63ce5688a3e8b_4);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_3;

        frame_exception_exit_4:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_1e57d9201f75c5f420f63ce5688a3e8b_4);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_1e57d9201f75c5f420f63ce5688a3e8b_4, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_1e57d9201f75c5f420f63ce5688a3e8b_4->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_1e57d9201f75c5f420f63ce5688a3e8b_4, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_1e57d9201f75c5f420f63ce5688a3e8b_4,
            type_description_3,
            outline_2_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_1e57d9201f75c5f420f63ce5688a3e8b_4 == cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4);
            cache_frame_1e57d9201f75c5f420f63ce5688a3e8b_4 = NULL;
        }

        assertFrameObject(frame_1e57d9201f75c5f420f63ce5688a3e8b_4);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_3;

        frame_no_exception_3:;
        goto skip_nested_handling_3;
        nested_frame_exit_3:;
        type_description_2 = "o";
        goto try_except_handler_9;
        skip_nested_handling_3:;
        {
            nuitka_bool tmp_condition_result_23;
            PyObject *tmp_cmp_expr_left_3;
            PyObject *tmp_cmp_expr_right_3;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_cmp_expr_left_3 = tmp_TextAnnotation$class_creation_2__bases;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases_orig);
            tmp_cmp_expr_right_3 = tmp_TextAnnotation$class_creation_2__bases_orig;
            tmp_condition_result_23 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_3, tmp_cmp_expr_right_3);
            if (tmp_condition_result_23 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_9;
            }
            if (tmp_condition_result_23 == NUITKA_BOOL_TRUE) {
                goto branch_yes_15;
            } else {
                goto branch_no_15;
            }
        }
        branch_yes_15:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases_orig);
        tmp_dictset_value = tmp_TextAnnotation$class_creation_2__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        branch_no_15:;
        {
            PyObject *tmp_assign_source_34;
            PyObject *tmp_called_value_12;
            PyObject *tmp_args_value_11;
            PyObject *tmp_tuple_element_19;
            PyObject *tmp_kwargs_value_11;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__metaclass);
            tmp_called_value_12 = tmp_TextAnnotation$class_creation_2__metaclass;
            tmp_tuple_element_19 = mod_consts[38];
            tmp_args_value_11 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_11, 0, tmp_tuple_element_19);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
            tmp_tuple_element_19 = tmp_TextAnnotation$class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_11, 1, tmp_tuple_element_19);
            tmp_tuple_element_19 = locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72;
            PyTuple_SET_ITEM0(tmp_args_value_11, 2, tmp_tuple_element_19);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
            tmp_kwargs_value_11 = tmp_TextAnnotation$class_creation_2__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 72;
            tmp_assign_source_34 = CALL_FUNCTION(tmp_called_value_12, tmp_args_value_11, tmp_kwargs_value_11);
            Py_DECREF(tmp_args_value_11);
            if (tmp_assign_source_34 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 72;
                type_description_2 = "o";
                goto try_except_handler_9;
            }
            assert(outline_2_var___class__ == NULL);
            outline_2_var___class__ = tmp_assign_source_34;
        }
        CHECK_OBJECT(outline_2_var___class__);
        tmp_dictset_value = outline_2_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_9;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_9:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72 = NULL;
        goto try_return_handler_8;
        // Exception handler code:
        try_except_handler_9:;
        exception_keeper_type_7 = exception_type;
        exception_keeper_value_7 = exception_value;
        exception_keeper_tb_7 = exception_tb;
        exception_keeper_lineno_7 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__3_DetectedBreak_72 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_7;
        exception_value = exception_keeper_value_7;
        exception_tb = exception_keeper_tb_7;
        exception_lineno = exception_keeper_lineno_7;

        goto try_except_handler_8;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_8:;
        CHECK_OBJECT(outline_2_var___class__);
        Py_DECREF(outline_2_var___class__);
        outline_2_var___class__ = NULL;
        goto outline_result_3;
        // Exception handler code:
        try_except_handler_8:;
        exception_keeper_type_8 = exception_type;
        exception_keeper_value_8 = exception_value;
        exception_keeper_tb_8 = exception_tb;
        exception_keeper_lineno_8 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_8;
        exception_value = exception_keeper_value_8;
        exception_tb = exception_keeper_tb_8;
        exception_lineno = exception_keeper_lineno_8;

        goto outline_exception_3;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_3:;
        exception_lineno = 72;
        goto try_except_handler_7;
        outline_result_3:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[38], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 72;
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        goto try_end_3;
        // Exception handler code:
        try_except_handler_7:;
        exception_keeper_type_9 = exception_type;
        exception_keeper_value_9 = exception_value;
        exception_keeper_tb_9 = exception_tb;
        exception_keeper_lineno_9 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_TextAnnotation$class_creation_2__bases_orig);
        tmp_TextAnnotation$class_creation_2__bases_orig = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_2__bases);
        tmp_TextAnnotation$class_creation_2__bases = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_2__class_decl_dict);
        tmp_TextAnnotation$class_creation_2__class_decl_dict = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_2__metaclass);
        tmp_TextAnnotation$class_creation_2__metaclass = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_2__prepared);
        tmp_TextAnnotation$class_creation_2__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_9;
        exception_value = exception_keeper_value_9;
        exception_tb = exception_keeper_tb_9;
        exception_lineno = exception_keeper_lineno_9;

        goto frame_exception_exit_2;
        // End of try:
        try_end_3:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases_orig);
        Py_DECREF(tmp_TextAnnotation$class_creation_2__bases_orig);
        tmp_TextAnnotation$class_creation_2__bases_orig = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__bases);
        Py_DECREF(tmp_TextAnnotation$class_creation_2__bases);
        tmp_TextAnnotation$class_creation_2__bases = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__class_decl_dict);
        Py_DECREF(tmp_TextAnnotation$class_creation_2__class_decl_dict);
        tmp_TextAnnotation$class_creation_2__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__metaclass);
        Py_DECREF(tmp_TextAnnotation$class_creation_2__metaclass);
        tmp_TextAnnotation$class_creation_2__metaclass = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_2__prepared);
        Py_DECREF(tmp_TextAnnotation$class_creation_2__prepared);
        tmp_TextAnnotation$class_creation_2__prepared = NULL;
        // Tried code:
        {
            PyObject *tmp_assign_source_35;
            PyObject *tmp_tuple_element_20;
            PyObject *tmp_expression_value_34;
            tmp_expression_value_34 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_34 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_34 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_34 == NULL)) {
                        tmp_expression_value_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_34 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 101;
                        type_description_2 = "o";
                        goto try_except_handler_13;
                    }
                    Py_INCREF(tmp_expression_value_34);
                } else {
                    goto try_except_handler_13;
                }
            }

            tmp_tuple_element_20 = LOOKUP_ATTRIBUTE(tmp_expression_value_34, mod_consts[15]);
            Py_DECREF(tmp_expression_value_34);
            if (tmp_tuple_element_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_assign_source_35 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_35, 0, tmp_tuple_element_20);
            assert(tmp_TextAnnotation$class_creation_3__bases_orig == NULL);
            tmp_TextAnnotation$class_creation_3__bases_orig = tmp_assign_source_35;
        }
        {
            PyObject *tmp_assign_source_36;
            PyObject *tmp_dircall_arg1_5;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases_orig);
            tmp_dircall_arg1_5 = tmp_TextAnnotation$class_creation_3__bases_orig;
            Py_INCREF(tmp_dircall_arg1_5);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_5};
                tmp_assign_source_36 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_36 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_TextAnnotation$class_creation_3__bases == NULL);
            tmp_TextAnnotation$class_creation_3__bases = tmp_assign_source_36;
        }
        {
            PyObject *tmp_assign_source_37;
            tmp_assign_source_37 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_3__class_decl_dict == NULL);
            tmp_TextAnnotation$class_creation_3__class_decl_dict = tmp_assign_source_37;
        }
        {
            PyObject *tmp_assign_source_38;
            PyObject *tmp_metaclass_value_5;
            bool tmp_condition_result_24;
            PyObject *tmp_key_value_13;
            PyObject *tmp_dict_arg_value_13;
            PyObject *tmp_dict_arg_value_14;
            PyObject *tmp_key_value_14;
            nuitka_bool tmp_condition_result_25;
            int tmp_truth_name_5;
            PyObject *tmp_type_arg_9;
            PyObject *tmp_expression_value_35;
            PyObject *tmp_subscript_value_5;
            PyObject *tmp_bases_value_5;
            tmp_key_value_13 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_13 = tmp_TextAnnotation$class_creation_3__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_13, tmp_key_value_13);
            assert(!(tmp_res == -1));
            tmp_condition_result_24 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_24 != false) {
                goto condexpr_true_9;
            } else {
                goto condexpr_false_9;
            }
            condexpr_true_9:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_14 = tmp_TextAnnotation$class_creation_3__class_decl_dict;
            tmp_key_value_14 = mod_consts[16];
            tmp_metaclass_value_5 = DICT_GET_ITEM0(tmp_dict_arg_value_14, tmp_key_value_14);
            if (tmp_metaclass_value_5 == NULL) {
                tmp_metaclass_value_5 = Py_None;
            }
            assert(!(tmp_metaclass_value_5 == NULL));
            Py_INCREF(tmp_metaclass_value_5);
            goto condexpr_end_9;
            condexpr_false_9:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_truth_name_5 = CHECK_IF_TRUE(tmp_TextAnnotation$class_creation_3__bases);
            if (tmp_truth_name_5 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_condition_result_25 = tmp_truth_name_5 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_25 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_10;
            } else {
                goto condexpr_false_10;
            }
            condexpr_true_10:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_expression_value_35 = tmp_TextAnnotation$class_creation_3__bases;
            tmp_subscript_value_5 = mod_consts[7];
            tmp_type_arg_9 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_35, tmp_subscript_value_5, 0);
            if (tmp_type_arg_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_metaclass_value_5 = BUILTIN_TYPE1(tmp_type_arg_9);
            Py_DECREF(tmp_type_arg_9);
            if (tmp_metaclass_value_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            goto condexpr_end_10;
            condexpr_false_10:;
            tmp_metaclass_value_5 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_5);
            condexpr_end_10:;
            condexpr_end_9:;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_bases_value_5 = tmp_TextAnnotation$class_creation_3__bases;
            tmp_assign_source_38 = SELECT_METACLASS(tmp_metaclass_value_5, tmp_bases_value_5);
            Py_DECREF(tmp_metaclass_value_5);
            if (tmp_assign_source_38 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_TextAnnotation$class_creation_3__metaclass == NULL);
            tmp_TextAnnotation$class_creation_3__metaclass = tmp_assign_source_38;
        }
        {
            bool tmp_condition_result_26;
            PyObject *tmp_key_value_15;
            PyObject *tmp_dict_arg_value_15;
            tmp_key_value_15 = mod_consts[16];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_15 = tmp_TextAnnotation$class_creation_3__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_15, tmp_key_value_15);
            assert(!(tmp_res == -1));
            tmp_condition_result_26 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_26 != false) {
                goto branch_yes_16;
            } else {
                goto branch_no_16;
            }
        }
        branch_yes_16:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
        tmp_dictdel_dict = tmp_TextAnnotation$class_creation_3__class_decl_dict;
        tmp_dictdel_key = mod_consts[16];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_13;
        }
        branch_no_16:;
        {
            nuitka_bool tmp_condition_result_27;
            PyObject *tmp_expression_value_36;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__metaclass);
            tmp_expression_value_36 = tmp_TextAnnotation$class_creation_3__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_36, mod_consts[17]);
            tmp_condition_result_27 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_27 == NUITKA_BOOL_TRUE) {
                goto branch_yes_17;
            } else {
                goto branch_no_17;
            }
        }
        branch_yes_17:;
        {
            PyObject *tmp_assign_source_39;
            PyObject *tmp_called_value_13;
            PyObject *tmp_expression_value_37;
            PyObject *tmp_args_value_12;
            PyObject *tmp_tuple_element_21;
            PyObject *tmp_kwargs_value_12;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__metaclass);
            tmp_expression_value_37 = tmp_TextAnnotation$class_creation_3__metaclass;
            tmp_called_value_13 = LOOKUP_ATTRIBUTE(tmp_expression_value_37, mod_consts[17]);
            if (tmp_called_value_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_tuple_element_21 = mod_consts[61];
            tmp_args_value_12 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_12, 0, tmp_tuple_element_21);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_tuple_element_21 = tmp_TextAnnotation$class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_12, 1, tmp_tuple_element_21);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
            tmp_kwargs_value_12 = tmp_TextAnnotation$class_creation_3__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 101;
            tmp_assign_source_39 = CALL_FUNCTION(tmp_called_value_13, tmp_args_value_12, tmp_kwargs_value_12);
            Py_DECREF(tmp_called_value_13);
            Py_DECREF(tmp_args_value_12);
            if (tmp_assign_source_39 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_TextAnnotation$class_creation_3__prepared == NULL);
            tmp_TextAnnotation$class_creation_3__prepared = tmp_assign_source_39;
        }
        {
            bool tmp_condition_result_28;
            PyObject *tmp_operand_value_5;
            PyObject *tmp_expression_value_38;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__prepared);
            tmp_expression_value_38 = tmp_TextAnnotation$class_creation_3__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_38, mod_consts[19]);
            tmp_operand_value_5 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_5);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_condition_result_28 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_28 != false) {
                goto branch_yes_18;
            } else {
                goto branch_no_18;
            }
        }
        branch_yes_18:;
        {
            PyObject *tmp_raise_type_5;
            PyObject *tmp_raise_value_5;
            PyObject *tmp_mod_expr_left_5;
            PyObject *tmp_mod_expr_right_5;
            PyObject *tmp_tuple_element_22;
            PyObject *tmp_getattr_target_5;
            PyObject *tmp_getattr_attr_5;
            PyObject *tmp_getattr_default_5;
            tmp_raise_type_5 = PyExc_TypeError;
            tmp_mod_expr_left_5 = mod_consts[20];
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__metaclass);
            tmp_getattr_target_5 = tmp_TextAnnotation$class_creation_3__metaclass;
            tmp_getattr_attr_5 = mod_consts[21];
            tmp_getattr_default_5 = mod_consts[22];
            tmp_tuple_element_22 = BUILTIN_GETATTR(tmp_getattr_target_5, tmp_getattr_attr_5, tmp_getattr_default_5);
            if (tmp_tuple_element_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_mod_expr_right_5 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_39;
                PyObject *tmp_type_arg_10;
                PyTuple_SET_ITEM(tmp_mod_expr_right_5, 0, tmp_tuple_element_22);
                CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__prepared);
                tmp_type_arg_10 = tmp_TextAnnotation$class_creation_3__prepared;
                tmp_expression_value_39 = BUILTIN_TYPE1(tmp_type_arg_10);
                assert(!(tmp_expression_value_39 == NULL));
                tmp_tuple_element_22 = LOOKUP_ATTRIBUTE(tmp_expression_value_39, mod_consts[21]);
                Py_DECREF(tmp_expression_value_39);
                if (tmp_tuple_element_22 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 101;
                    type_description_2 = "o";
                    goto tuple_build_exception_5;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_5, 1, tmp_tuple_element_22);
            }
            goto tuple_build_noexception_5;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_5:;
            Py_DECREF(tmp_mod_expr_right_5);
            goto try_except_handler_13;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_5:;
            tmp_raise_value_5 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_5, tmp_mod_expr_right_5);
            Py_DECREF(tmp_mod_expr_right_5);
            if (tmp_raise_value_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            exception_type = tmp_raise_type_5;
            Py_INCREF(tmp_raise_type_5);
            exception_value = tmp_raise_value_5;
            exception_lineno = 101;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_13;
        }
        branch_no_18:;
        goto branch_end_17;
        branch_no_17:;
        {
            PyObject *tmp_assign_source_40;
            tmp_assign_source_40 = PyDict_New();
            assert(tmp_TextAnnotation$class_creation_3__prepared == NULL);
            tmp_TextAnnotation$class_creation_3__prepared = tmp_assign_source_40;
        }
        branch_end_17:;
        {
            PyObject *tmp_set_locals_5;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__prepared);
            tmp_set_locals_5 = tmp_TextAnnotation$class_creation_3__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101 = tmp_set_locals_5;
            Py_INCREF(tmp_set_locals_5);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        tmp_dictset_value = mod_consts[62];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        tmp_dictset_value = mod_consts[63];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        if (isFrameUnusable(cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6)) {
            Py_XDECREF(cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);

#if _DEBUG_REFCOUNTS
            if (cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 = MAKE_FUNCTION_FRAME(codeobj_6c31dcf67c1bcc18b06bdd9be6ff70ce, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6->m_type_description == NULL);
        frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 = cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_14;
            PyObject *tmp_expression_value_40;
            PyObject *tmp_args_value_13;
            PyObject *tmp_tuple_element_23;
            PyObject *tmp_expression_value_41;
            PyObject *tmp_kwargs_value_13;
            tmp_expression_value_40 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[6]);

            if (tmp_expression_value_40 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_40 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_40 == NULL)) {
                        tmp_expression_value_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_40 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 112;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_40);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_called_value_14 = LOOKUP_ATTRIBUTE(tmp_expression_value_40, mod_consts[64]);
            Py_DECREF(tmp_expression_value_40);
            if (tmp_called_value_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 112;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_expression_value_41 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[6]);

            if (tmp_expression_value_41 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_41 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_41 == NULL)) {
                        tmp_expression_value_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_41 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_14);

                        exception_lineno = 113;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_41);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_tuple_element_23 = LOOKUP_ATTRIBUTE(tmp_expression_value_41, mod_consts[65]);
            Py_DECREF(tmp_expression_value_41);
            if (tmp_tuple_element_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_14);

                exception_lineno = 113;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_args_value_13 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_13, 0, tmp_tuple_element_23);
            tmp_kwargs_value_13 = PyDict_Copy(mod_consts[66]);
            frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6->m_frame.f_lineno = 112;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_14, tmp_args_value_13, tmp_kwargs_value_13);
            Py_DECREF(tmp_called_value_14);
            Py_DECREF(tmp_args_value_13);
            Py_DECREF(tmp_kwargs_value_13);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 112;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[67], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 112;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
        }
        {
            PyObject *tmp_called_value_15;
            PyObject *tmp_expression_value_42;
            PyObject *tmp_args_value_14;
            PyObject *tmp_tuple_element_24;
            PyObject *tmp_expression_value_43;
            PyObject *tmp_kwargs_value_14;
            tmp_expression_value_42 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[6]);

            if (tmp_expression_value_42 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_42 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_42 == NULL)) {
                        tmp_expression_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_42 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 117;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_42);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_called_value_15 = LOOKUP_ATTRIBUTE(tmp_expression_value_42, mod_consts[30]);
            Py_DECREF(tmp_expression_value_42);
            if (tmp_called_value_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 117;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_expression_value_43 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[6]);

            if (tmp_expression_value_43 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_43 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_43 == NULL)) {
                        tmp_expression_value_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_43 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_15);

                        exception_lineno = 118;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_43);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_tuple_element_24 = LOOKUP_ATTRIBUTE(tmp_expression_value_43, mod_consts[65]);
            Py_DECREF(tmp_expression_value_43);
            if (tmp_tuple_element_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_15);

                exception_lineno = 118;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_args_value_14 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_14, 0, tmp_tuple_element_24);
            tmp_kwargs_value_14 = PyDict_Copy(mod_consts[68]);
            frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6->m_frame.f_lineno = 117;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_15, tmp_args_value_14, tmp_kwargs_value_14);
            Py_DECREF(tmp_called_value_15);
            Py_DECREF(tmp_args_value_14);
            Py_DECREF(tmp_kwargs_value_14);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 117;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[69], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 117;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_4;

        frame_exception_exit_6:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6,
            type_description_3,
            outline_4_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 == cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);
            cache_frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6 = NULL;
        }

        assertFrameObject(frame_6c31dcf67c1bcc18b06bdd9be6ff70ce_6);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_5;

        frame_no_exception_4:;
        goto skip_nested_handling_4;
        nested_frame_exit_5:;
        type_description_2 = "o";
        goto try_except_handler_15;
        skip_nested_handling_4:;
        {
            nuitka_bool tmp_condition_result_29;
            PyObject *tmp_cmp_expr_left_4;
            PyObject *tmp_cmp_expr_right_4;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_cmp_expr_left_4 = tmp_TextAnnotation$class_creation_3__bases;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases_orig);
            tmp_cmp_expr_right_4 = tmp_TextAnnotation$class_creation_3__bases_orig;
            tmp_condition_result_29 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_4, tmp_cmp_expr_right_4);
            if (tmp_condition_result_29 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_15;
            }
            if (tmp_condition_result_29 == NUITKA_BOOL_TRUE) {
                goto branch_yes_19;
            } else {
                goto branch_no_19;
            }
        }
        branch_yes_19:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases_orig);
        tmp_dictset_value = tmp_TextAnnotation$class_creation_3__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        branch_no_19:;
        {
            PyObject *tmp_assign_source_41;
            PyObject *tmp_called_value_16;
            PyObject *tmp_args_value_15;
            PyObject *tmp_tuple_element_25;
            PyObject *tmp_kwargs_value_15;
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__metaclass);
            tmp_called_value_16 = tmp_TextAnnotation$class_creation_3__metaclass;
            tmp_tuple_element_25 = mod_consts[61];
            tmp_args_value_15 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_15, 0, tmp_tuple_element_25);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
            tmp_tuple_element_25 = tmp_TextAnnotation$class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_15, 1, tmp_tuple_element_25);
            tmp_tuple_element_25 = locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101;
            PyTuple_SET_ITEM0(tmp_args_value_15, 2, tmp_tuple_element_25);
            CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
            tmp_kwargs_value_15 = tmp_TextAnnotation$class_creation_3__class_decl_dict;
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 101;
            tmp_assign_source_41 = CALL_FUNCTION(tmp_called_value_16, tmp_args_value_15, tmp_kwargs_value_15);
            Py_DECREF(tmp_args_value_15);
            if (tmp_assign_source_41 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 101;
                type_description_2 = "o";
                goto try_except_handler_15;
            }
            assert(outline_4_var___class__ == NULL);
            outline_4_var___class__ = tmp_assign_source_41;
        }
        CHECK_OBJECT(outline_4_var___class__);
        tmp_dictset_value = outline_4_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_15;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_15:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101 = NULL;
        goto try_return_handler_14;
        // Exception handler code:
        try_except_handler_15:;
        exception_keeper_type_10 = exception_type;
        exception_keeper_value_10 = exception_value;
        exception_keeper_tb_10 = exception_tb;
        exception_keeper_lineno_10 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__5_TextProperty_101 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_10;
        exception_value = exception_keeper_value_10;
        exception_tb = exception_keeper_tb_10;
        exception_lineno = exception_keeper_lineno_10;

        goto try_except_handler_14;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_14:;
        CHECK_OBJECT(outline_4_var___class__);
        Py_DECREF(outline_4_var___class__);
        outline_4_var___class__ = NULL;
        goto outline_result_5;
        // Exception handler code:
        try_except_handler_14:;
        exception_keeper_type_11 = exception_type;
        exception_keeper_value_11 = exception_value;
        exception_keeper_tb_11 = exception_tb;
        exception_keeper_lineno_11 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_11;
        exception_value = exception_keeper_value_11;
        exception_tb = exception_keeper_tb_11;
        exception_lineno = exception_keeper_lineno_11;

        goto outline_exception_5;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_5:;
        exception_lineno = 101;
        goto try_except_handler_13;
        outline_result_5:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[61], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 101;
            type_description_2 = "o";
            goto try_except_handler_13;
        }
        goto try_end_4;
        // Exception handler code:
        try_except_handler_13:;
        exception_keeper_type_12 = exception_type;
        exception_keeper_value_12 = exception_value;
        exception_keeper_tb_12 = exception_tb;
        exception_keeper_lineno_12 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_TextAnnotation$class_creation_3__bases_orig);
        tmp_TextAnnotation$class_creation_3__bases_orig = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_3__bases);
        tmp_TextAnnotation$class_creation_3__bases = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_3__class_decl_dict);
        tmp_TextAnnotation$class_creation_3__class_decl_dict = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_3__metaclass);
        tmp_TextAnnotation$class_creation_3__metaclass = NULL;
        Py_XDECREF(tmp_TextAnnotation$class_creation_3__prepared);
        tmp_TextAnnotation$class_creation_3__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_12;
        exception_value = exception_keeper_value_12;
        exception_tb = exception_keeper_tb_12;
        exception_lineno = exception_keeper_lineno_12;

        goto frame_exception_exit_2;
        // End of try:
        try_end_4:;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases_orig);
        Py_DECREF(tmp_TextAnnotation$class_creation_3__bases_orig);
        tmp_TextAnnotation$class_creation_3__bases_orig = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__bases);
        Py_DECREF(tmp_TextAnnotation$class_creation_3__bases);
        tmp_TextAnnotation$class_creation_3__bases = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__class_decl_dict);
        Py_DECREF(tmp_TextAnnotation$class_creation_3__class_decl_dict);
        tmp_TextAnnotation$class_creation_3__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__metaclass);
        Py_DECREF(tmp_TextAnnotation$class_creation_3__metaclass);
        tmp_TextAnnotation$class_creation_3__metaclass = NULL;
        CHECK_OBJECT(tmp_TextAnnotation$class_creation_3__prepared);
        Py_DECREF(tmp_TextAnnotation$class_creation_3__prepared);
        tmp_TextAnnotation$class_creation_3__prepared = NULL;
        {
            PyObject *tmp_called_value_17;
            PyObject *tmp_expression_value_44;
            PyObject *tmp_args_value_16;
            PyObject *tmp_tuple_element_26;
            PyObject *tmp_expression_value_45;
            PyObject *tmp_kwargs_value_16;
            tmp_expression_value_44 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_44 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_44 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_44 == NULL)) {
                        tmp_expression_value_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_44 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 123;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_44);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_17 = LOOKUP_ATTRIBUTE(tmp_expression_value_44, mod_consts[64]);
            Py_DECREF(tmp_expression_value_44);
            if (tmp_called_value_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 123;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_45 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_45 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_45 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_45 == NULL)) {
                        tmp_expression_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_45 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_17);

                        exception_lineno = 124;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_45);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_tuple_element_26 = LOOKUP_ATTRIBUTE(tmp_expression_value_45, mod_consts[65]);
            Py_DECREF(tmp_expression_value_45);
            if (tmp_tuple_element_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_17);

                exception_lineno = 124;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_args_value_16 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_16, 0, tmp_tuple_element_26);
            tmp_kwargs_value_16 = PyDict_Copy(mod_consts[70]);
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 123;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_17, tmp_args_value_16, tmp_kwargs_value_16);
            Py_DECREF(tmp_called_value_17);
            Py_DECREF(tmp_args_value_16);
            Py_DECREF(tmp_kwargs_value_16);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 123;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[71], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 123;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_18;
            PyObject *tmp_expression_value_46;
            PyObject *tmp_args_value_17;
            PyObject *tmp_tuple_element_27;
            PyObject *tmp_expression_value_47;
            PyObject *tmp_kwargs_value_17;
            tmp_expression_value_46 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_46 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_46 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_46 == NULL)) {
                        tmp_expression_value_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_46 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 128;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_46);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_18 = LOOKUP_ATTRIBUTE(tmp_expression_value_46, mod_consts[30]);
            Py_DECREF(tmp_expression_value_46);
            if (tmp_called_value_18 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 128;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_47 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[6]);

            if (tmp_expression_value_47 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_47 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_47 == NULL)) {
                        tmp_expression_value_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_47 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_18);

                        exception_lineno = 129;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_47);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_tuple_element_27 = LOOKUP_ATTRIBUTE(tmp_expression_value_47, mod_consts[31]);
            Py_DECREF(tmp_expression_value_47);
            if (tmp_tuple_element_27 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_18);

                exception_lineno = 129;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_args_value_17 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_17, 0, tmp_tuple_element_27);
            tmp_kwargs_value_17 = PyDict_Copy(mod_consts[35]);
            frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame.f_lineno = 128;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_18, tmp_args_value_17, tmp_kwargs_value_17);
            Py_DECREF(tmp_called_value_18);
            Py_DECREF(tmp_args_value_17);
            Py_DECREF(tmp_kwargs_value_17);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 128;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[72], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 128;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_5cea5e801737c4e565477c4e5b13c74d_2);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_5;

        frame_exception_exit_2:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_5cea5e801737c4e565477c4e5b13c74d_2);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_5cea5e801737c4e565477c4e5b13c74d_2, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_5cea5e801737c4e565477c4e5b13c74d_2->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_5cea5e801737c4e565477c4e5b13c74d_2, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_5cea5e801737c4e565477c4e5b13c74d_2,
            type_description_2,
            outline_0_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_5cea5e801737c4e565477c4e5b13c74d_2 == cache_frame_5cea5e801737c4e565477c4e5b13c74d_2) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_5cea5e801737c4e565477c4e5b13c74d_2);
            cache_frame_5cea5e801737c4e565477c4e5b13c74d_2 = NULL;
        }

        assertFrameObject(frame_5cea5e801737c4e565477c4e5b13c74d_2);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_1;

        frame_no_exception_5:;
        goto skip_nested_handling_5;
        nested_frame_exit_1:;

        goto try_except_handler_3;
        skip_nested_handling_5:;
        {
            nuitka_bool tmp_condition_result_30;
            PyObject *tmp_cmp_expr_left_5;
            PyObject *tmp_cmp_expr_right_5;
            CHECK_OBJECT(tmp_class_creation_1__bases);
            tmp_cmp_expr_left_5 = tmp_class_creation_1__bases;
            CHECK_OBJECT(tmp_class_creation_1__bases_orig);
            tmp_cmp_expr_right_5 = tmp_class_creation_1__bases_orig;
            tmp_condition_result_30 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_5, tmp_cmp_expr_right_5);
            if (tmp_condition_result_30 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto try_except_handler_3;
            }
            if (tmp_condition_result_30 == NUITKA_BOOL_TRUE) {
                goto branch_yes_20;
            } else {
                goto branch_no_20;
            }
        }
        branch_yes_20:;
        CHECK_OBJECT(tmp_class_creation_1__bases_orig);
        tmp_dictset_value = tmp_class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 34;

            goto try_except_handler_3;
        }
        branch_no_20:;
        {
            PyObject *tmp_assign_source_42;
            PyObject *tmp_called_value_19;
            PyObject *tmp_args_value_18;
            PyObject *tmp_tuple_element_28;
            PyObject *tmp_kwargs_value_18;
            CHECK_OBJECT(tmp_class_creation_1__metaclass);
            tmp_called_value_19 = tmp_class_creation_1__metaclass;
            tmp_tuple_element_28 = mod_consts[18];
            tmp_args_value_18 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_18, 0, tmp_tuple_element_28);
            CHECK_OBJECT(tmp_class_creation_1__bases);
            tmp_tuple_element_28 = tmp_class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_18, 1, tmp_tuple_element_28);
            tmp_tuple_element_28 = locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34;
            PyTuple_SET_ITEM0(tmp_args_value_18, 2, tmp_tuple_element_28);
            CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
            tmp_kwargs_value_18 = tmp_class_creation_1__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 34;
            tmp_assign_source_42 = CALL_FUNCTION(tmp_called_value_19, tmp_args_value_18, tmp_kwargs_value_18);
            Py_DECREF(tmp_args_value_18);
            if (tmp_assign_source_42 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 34;

                goto try_except_handler_3;
            }
            assert(outline_0_var___class__ == NULL);
            outline_0_var___class__ = tmp_assign_source_42;
        }
        CHECK_OBJECT(outline_0_var___class__);
        tmp_assign_source_13 = outline_0_var___class__;
        Py_INCREF(tmp_assign_source_13);
        goto try_return_handler_3;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_3:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34 = NULL;
        goto try_return_handler_2;
        // Exception handler code:
        try_except_handler_3:;
        exception_keeper_type_13 = exception_type;
        exception_keeper_value_13 = exception_value;
        exception_keeper_tb_13 = exception_tb;
        exception_keeper_lineno_13 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__1_TextAnnotation_34 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_13;
        exception_value = exception_keeper_value_13;
        exception_tb = exception_keeper_tb_13;
        exception_lineno = exception_keeper_lineno_13;

        goto try_except_handler_2;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_2:;
        CHECK_OBJECT(outline_0_var___class__);
        Py_DECREF(outline_0_var___class__);
        outline_0_var___class__ = NULL;
        goto outline_result_1;
        // Exception handler code:
        try_except_handler_2:;
        exception_keeper_type_14 = exception_type;
        exception_keeper_value_14 = exception_value;
        exception_keeper_tb_14 = exception_tb;
        exception_keeper_lineno_14 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_14;
        exception_value = exception_keeper_value_14;
        exception_tb = exception_keeper_tb_14;
        exception_lineno = exception_keeper_lineno_14;

        goto outline_exception_1;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_1:;
        exception_lineno = 34;
        goto try_except_handler_1;
        outline_result_1:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[18], tmp_assign_source_13);
    }
    goto try_end_5;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_15 = exception_type;
    exception_keeper_value_15 = exception_value;
    exception_keeper_tb_15 = exception_tb;
    exception_keeper_lineno_15 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_1__bases_orig);
    tmp_class_creation_1__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_1__bases);
    tmp_class_creation_1__bases = NULL;
    Py_XDECREF(tmp_class_creation_1__class_decl_dict);
    tmp_class_creation_1__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_1__metaclass);
    tmp_class_creation_1__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_1__prepared);
    tmp_class_creation_1__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_15;
    exception_value = exception_keeper_value_15;
    exception_tb = exception_keeper_tb_15;
    exception_lineno = exception_keeper_lineno_15;

    goto frame_exception_exit_1;
    // End of try:
    try_end_5:;
    CHECK_OBJECT(tmp_class_creation_1__bases_orig);
    Py_DECREF(tmp_class_creation_1__bases_orig);
    tmp_class_creation_1__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_1__bases);
    Py_DECREF(tmp_class_creation_1__bases);
    tmp_class_creation_1__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
    Py_DECREF(tmp_class_creation_1__class_decl_dict);
    tmp_class_creation_1__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_1__metaclass);
    Py_DECREF(tmp_class_creation_1__metaclass);
    tmp_class_creation_1__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_1__prepared);
    Py_DECREF(tmp_class_creation_1__prepared);
    tmp_class_creation_1__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_43;
        PyObject *tmp_tuple_element_29;
        PyObject *tmp_expression_value_48;
        tmp_expression_value_48 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_48 == NULL)) {
            tmp_expression_value_48 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_48 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_tuple_element_29 = LOOKUP_ATTRIBUTE(tmp_expression_value_48, mod_consts[15]);
        if (tmp_tuple_element_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_assign_source_43 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_43, 0, tmp_tuple_element_29);
        assert(tmp_class_creation_2__bases_orig == NULL);
        tmp_class_creation_2__bases_orig = tmp_assign_source_43;
    }
    {
        PyObject *tmp_assign_source_44;
        PyObject *tmp_dircall_arg1_6;
        CHECK_OBJECT(tmp_class_creation_2__bases_orig);
        tmp_dircall_arg1_6 = tmp_class_creation_2__bases_orig;
        Py_INCREF(tmp_dircall_arg1_6);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_6};
            tmp_assign_source_44 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        assert(tmp_class_creation_2__bases == NULL);
        tmp_class_creation_2__bases = tmp_assign_source_44;
    }
    {
        PyObject *tmp_assign_source_45;
        tmp_assign_source_45 = PyDict_New();
        assert(tmp_class_creation_2__class_decl_dict == NULL);
        tmp_class_creation_2__class_decl_dict = tmp_assign_source_45;
    }
    {
        PyObject *tmp_assign_source_46;
        PyObject *tmp_metaclass_value_6;
        bool tmp_condition_result_31;
        PyObject *tmp_key_value_16;
        PyObject *tmp_dict_arg_value_16;
        PyObject *tmp_dict_arg_value_17;
        PyObject *tmp_key_value_17;
        nuitka_bool tmp_condition_result_32;
        int tmp_truth_name_6;
        PyObject *tmp_type_arg_11;
        PyObject *tmp_expression_value_49;
        PyObject *tmp_subscript_value_6;
        PyObject *tmp_bases_value_6;
        tmp_key_value_16 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
        tmp_dict_arg_value_16 = tmp_class_creation_2__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_16, tmp_key_value_16);
        assert(!(tmp_res == -1));
        tmp_condition_result_31 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_31 != false) {
            goto condexpr_true_11;
        } else {
            goto condexpr_false_11;
        }
        condexpr_true_11:;
        CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
        tmp_dict_arg_value_17 = tmp_class_creation_2__class_decl_dict;
        tmp_key_value_17 = mod_consts[16];
        tmp_metaclass_value_6 = DICT_GET_ITEM0(tmp_dict_arg_value_17, tmp_key_value_17);
        if (tmp_metaclass_value_6 == NULL) {
            tmp_metaclass_value_6 = Py_None;
        }
        assert(!(tmp_metaclass_value_6 == NULL));
        Py_INCREF(tmp_metaclass_value_6);
        goto condexpr_end_11;
        condexpr_false_11:;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_truth_name_6 = CHECK_IF_TRUE(tmp_class_creation_2__bases);
        if (tmp_truth_name_6 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_condition_result_32 = tmp_truth_name_6 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_32 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_12;
        } else {
            goto condexpr_false_12;
        }
        condexpr_true_12:;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_expression_value_49 = tmp_class_creation_2__bases;
        tmp_subscript_value_6 = mod_consts[7];
        tmp_type_arg_11 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_49, tmp_subscript_value_6, 0);
        if (tmp_type_arg_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_metaclass_value_6 = BUILTIN_TYPE1(tmp_type_arg_11);
        Py_DECREF(tmp_type_arg_11);
        if (tmp_metaclass_value_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        goto condexpr_end_12;
        condexpr_false_12:;
        tmp_metaclass_value_6 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_6);
        condexpr_end_12:;
        condexpr_end_11:;
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_bases_value_6 = tmp_class_creation_2__bases;
        tmp_assign_source_46 = SELECT_METACLASS(tmp_metaclass_value_6, tmp_bases_value_6);
        Py_DECREF(tmp_metaclass_value_6);
        if (tmp_assign_source_46 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        assert(tmp_class_creation_2__metaclass == NULL);
        tmp_class_creation_2__metaclass = tmp_assign_source_46;
    }
    {
        bool tmp_condition_result_33;
        PyObject *tmp_key_value_18;
        PyObject *tmp_dict_arg_value_18;
        tmp_key_value_18 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
        tmp_dict_arg_value_18 = tmp_class_creation_2__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_18, tmp_key_value_18);
        assert(!(tmp_res == -1));
        tmp_condition_result_33 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_33 != false) {
            goto branch_yes_21;
        } else {
            goto branch_no_21;
        }
    }
    branch_yes_21:;
    CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_2__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 134;

        goto try_except_handler_16;
    }
    branch_no_21:;
    {
        nuitka_bool tmp_condition_result_34;
        PyObject *tmp_expression_value_50;
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_expression_value_50 = tmp_class_creation_2__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_50, mod_consts[17]);
        tmp_condition_result_34 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_34 == NUITKA_BOOL_TRUE) {
            goto branch_yes_22;
        } else {
            goto branch_no_22;
        }
    }
    branch_yes_22:;
    {
        PyObject *tmp_assign_source_47;
        PyObject *tmp_called_value_20;
        PyObject *tmp_expression_value_51;
        PyObject *tmp_args_value_19;
        PyObject *tmp_tuple_element_30;
        PyObject *tmp_kwargs_value_19;
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_expression_value_51 = tmp_class_creation_2__metaclass;
        tmp_called_value_20 = LOOKUP_ATTRIBUTE(tmp_expression_value_51, mod_consts[17]);
        if (tmp_called_value_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_tuple_element_30 = mod_consts[73];
        tmp_args_value_19 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_19, 0, tmp_tuple_element_30);
        CHECK_OBJECT(tmp_class_creation_2__bases);
        tmp_tuple_element_30 = tmp_class_creation_2__bases;
        PyTuple_SET_ITEM0(tmp_args_value_19, 1, tmp_tuple_element_30);
        CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
        tmp_kwargs_value_19 = tmp_class_creation_2__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 134;
        tmp_assign_source_47 = CALL_FUNCTION(tmp_called_value_20, tmp_args_value_19, tmp_kwargs_value_19);
        Py_DECREF(tmp_called_value_20);
        Py_DECREF(tmp_args_value_19);
        if (tmp_assign_source_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        assert(tmp_class_creation_2__prepared == NULL);
        tmp_class_creation_2__prepared = tmp_assign_source_47;
    }
    {
        bool tmp_condition_result_35;
        PyObject *tmp_operand_value_6;
        PyObject *tmp_expression_value_52;
        CHECK_OBJECT(tmp_class_creation_2__prepared);
        tmp_expression_value_52 = tmp_class_creation_2__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_52, mod_consts[19]);
        tmp_operand_value_6 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_6);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_condition_result_35 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_35 != false) {
            goto branch_yes_23;
        } else {
            goto branch_no_23;
        }
    }
    branch_yes_23:;
    {
        PyObject *tmp_raise_type_6;
        PyObject *tmp_raise_value_6;
        PyObject *tmp_mod_expr_left_6;
        PyObject *tmp_mod_expr_right_6;
        PyObject *tmp_tuple_element_31;
        PyObject *tmp_getattr_target_6;
        PyObject *tmp_getattr_attr_6;
        PyObject *tmp_getattr_default_6;
        tmp_raise_type_6 = PyExc_TypeError;
        tmp_mod_expr_left_6 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_2__metaclass);
        tmp_getattr_target_6 = tmp_class_creation_2__metaclass;
        tmp_getattr_attr_6 = mod_consts[21];
        tmp_getattr_default_6 = mod_consts[22];
        tmp_tuple_element_31 = BUILTIN_GETATTR(tmp_getattr_target_6, tmp_getattr_attr_6, tmp_getattr_default_6);
        if (tmp_tuple_element_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        tmp_mod_expr_right_6 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_53;
            PyObject *tmp_type_arg_12;
            PyTuple_SET_ITEM(tmp_mod_expr_right_6, 0, tmp_tuple_element_31);
            CHECK_OBJECT(tmp_class_creation_2__prepared);
            tmp_type_arg_12 = tmp_class_creation_2__prepared;
            tmp_expression_value_53 = BUILTIN_TYPE1(tmp_type_arg_12);
            assert(!(tmp_expression_value_53 == NULL));
            tmp_tuple_element_31 = LOOKUP_ATTRIBUTE(tmp_expression_value_53, mod_consts[21]);
            Py_DECREF(tmp_expression_value_53);
            if (tmp_tuple_element_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 134;

                goto tuple_build_exception_6;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_6, 1, tmp_tuple_element_31);
        }
        goto tuple_build_noexception_6;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_6:;
        Py_DECREF(tmp_mod_expr_right_6);
        goto try_except_handler_16;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_6:;
        tmp_raise_value_6 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_6, tmp_mod_expr_right_6);
        Py_DECREF(tmp_mod_expr_right_6);
        if (tmp_raise_value_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_16;
        }
        exception_type = tmp_raise_type_6;
        Py_INCREF(tmp_raise_type_6);
        exception_value = tmp_raise_value_6;
        exception_lineno = 134;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_16;
    }
    branch_no_23:;
    goto branch_end_22;
    branch_no_22:;
    {
        PyObject *tmp_assign_source_48;
        tmp_assign_source_48 = PyDict_New();
        assert(tmp_class_creation_2__prepared == NULL);
        tmp_class_creation_2__prepared = tmp_assign_source_48;
    }
    branch_end_22:;
    {
        PyObject *tmp_assign_source_49;
        {
            PyObject *tmp_set_locals_6;
            CHECK_OBJECT(tmp_class_creation_2__prepared);
            tmp_set_locals_6 = tmp_class_creation_2__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134 = tmp_set_locals_6;
            Py_INCREF(tmp_set_locals_6);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_18;
        }
        tmp_dictset_value = mod_consts[74];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_18;
        }
        tmp_dictset_value = mod_consts[73];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_18;
        }
        if (isFrameUnusable(cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7)) {
            Py_XDECREF(cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7);

#if _DEBUG_REFCOUNTS
            if (cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7 = MAKE_FUNCTION_FRAME(codeobj_aae2ed367423a5fce3ebf6593eb0816b, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_type_description == NULL);
        frame_aae2ed367423a5fce3ebf6593eb0816b_7 = cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_aae2ed367423a5fce3ebf6593eb0816b_7);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_aae2ed367423a5fce3ebf6593eb0816b_7) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_21;
            PyObject *tmp_expression_value_54;
            PyObject *tmp_args_value_20;
            PyObject *tmp_tuple_element_32;
            PyObject *tmp_expression_value_55;
            PyObject *tmp_kwargs_value_20;
            tmp_expression_value_54 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_54 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_54 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_54 == NULL)) {
                        tmp_expression_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_54 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 153;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_54);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_called_value_21 = LOOKUP_ATTRIBUTE(tmp_expression_value_54, mod_consts[30]);
            Py_DECREF(tmp_expression_value_54);
            if (tmp_called_value_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 153;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_expression_value_55 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_55 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_55 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_55 == NULL)) {
                        tmp_expression_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_55 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_21);

                        exception_lineno = 154;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_55);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_tuple_element_32 = LOOKUP_ATTRIBUTE(tmp_expression_value_55, mod_consts[65]);
            Py_DECREF(tmp_expression_value_55);
            if (tmp_tuple_element_32 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_21);

                exception_lineno = 154;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_args_value_20 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_20, 0, tmp_tuple_element_32);
            tmp_kwargs_value_20 = PyDict_Copy(mod_consts[75]);
            frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame.f_lineno = 153;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_21, tmp_args_value_20, tmp_kwargs_value_20);
            Py_DECREF(tmp_called_value_21);
            Py_DECREF(tmp_args_value_20);
            Py_DECREF(tmp_kwargs_value_20);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 153;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[76], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 153;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
        }
        {
            PyObject *tmp_called_value_22;
            PyObject *tmp_expression_value_56;
            PyObject *tmp_args_value_21;
            PyObject *tmp_tuple_element_33;
            PyObject *tmp_expression_value_57;
            PyObject *tmp_kwargs_value_21;
            tmp_expression_value_56 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_56 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_56 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_56 == NULL)) {
                        tmp_expression_value_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_56 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 158;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_56);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_called_value_22 = LOOKUP_ATTRIBUTE(tmp_expression_value_56, mod_consts[30]);
            Py_DECREF(tmp_expression_value_56);
            if (tmp_called_value_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 158;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_expression_value_57 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_57 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_57 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_57 == NULL)) {
                        tmp_expression_value_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_57 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_22);

                        exception_lineno = 159;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_57);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_tuple_element_33 = LOOKUP_ATTRIBUTE(tmp_expression_value_57, mod_consts[77]);
            Py_DECREF(tmp_expression_value_57);
            if (tmp_tuple_element_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_22);

                exception_lineno = 159;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_args_value_21 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_21, 0, tmp_tuple_element_33);
            tmp_kwargs_value_21 = PyDict_Copy(mod_consts[35]);
            frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame.f_lineno = 158;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_22, tmp_args_value_21, tmp_kwargs_value_21);
            Py_DECREF(tmp_called_value_22);
            Py_DECREF(tmp_args_value_21);
            Py_DECREF(tmp_kwargs_value_21);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 158;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[78], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 158;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
        }
        {
            PyObject *tmp_called_value_23;
            PyObject *tmp_expression_value_58;
            PyObject *tmp_args_value_22;
            PyObject *tmp_tuple_element_34;
            PyObject *tmp_expression_value_59;
            PyObject *tmp_kwargs_value_22;
            tmp_expression_value_58 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_58 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_58 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_58 == NULL)) {
                        tmp_expression_value_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_58 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 162;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_58);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_called_value_23 = LOOKUP_ATTRIBUTE(tmp_expression_value_58, mod_consts[30]);
            Py_DECREF(tmp_expression_value_58);
            if (tmp_called_value_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 162;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_expression_value_59 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_59 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_59 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_59 == NULL)) {
                        tmp_expression_value_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_59 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_23);

                        exception_lineno = 163;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_59);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_tuple_element_34 = LOOKUP_ATTRIBUTE(tmp_expression_value_59, mod_consts[77]);
            Py_DECREF(tmp_expression_value_59);
            if (tmp_tuple_element_34 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_23);

                exception_lineno = 163;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_args_value_22 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_22, 0, tmp_tuple_element_34);
            tmp_kwargs_value_22 = PyDict_Copy(mod_consts[79]);
            frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame.f_lineno = 162;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_23, tmp_args_value_22, tmp_kwargs_value_22);
            Py_DECREF(tmp_called_value_23);
            Py_DECREF(tmp_args_value_22);
            Py_DECREF(tmp_kwargs_value_22);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 162;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[80], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 162;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
        }
        {
            PyObject *tmp_called_value_24;
            PyObject *tmp_expression_value_60;
            PyObject *tmp_args_value_23;
            PyObject *tmp_tuple_element_35;
            PyObject *tmp_expression_value_61;
            PyObject *tmp_kwargs_value_23;
            tmp_expression_value_60 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_60 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_60 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_60 == NULL)) {
                        tmp_expression_value_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_60 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 166;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_60);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_called_value_24 = LOOKUP_ATTRIBUTE(tmp_expression_value_60, mod_consts[64]);
            Py_DECREF(tmp_expression_value_60);
            if (tmp_called_value_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 166;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_expression_value_61 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_61 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_61 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_61 == NULL)) {
                        tmp_expression_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_61 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_24);

                        exception_lineno = 167;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_61);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_tuple_element_35 = LOOKUP_ATTRIBUTE(tmp_expression_value_61, mod_consts[65]);
            Py_DECREF(tmp_expression_value_61);
            if (tmp_tuple_element_35 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_24);

                exception_lineno = 167;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_args_value_23 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_23, 0, tmp_tuple_element_35);
            tmp_kwargs_value_23 = PyDict_Copy(mod_consts[81]);
            frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame.f_lineno = 166;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_24, tmp_args_value_23, tmp_kwargs_value_23);
            Py_DECREF(tmp_called_value_24);
            Py_DECREF(tmp_args_value_23);
            Py_DECREF(tmp_kwargs_value_23);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 166;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[82], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 166;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
        }
        {
            PyObject *tmp_called_value_25;
            PyObject *tmp_expression_value_62;
            PyObject *tmp_args_value_24;
            PyObject *tmp_tuple_element_36;
            PyObject *tmp_expression_value_63;
            PyObject *tmp_kwargs_value_24;
            tmp_expression_value_62 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_62 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_62 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_62 == NULL)) {
                        tmp_expression_value_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_62 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 171;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_62);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_called_value_25 = LOOKUP_ATTRIBUTE(tmp_expression_value_62, mod_consts[30]);
            Py_DECREF(tmp_expression_value_62);
            if (tmp_called_value_25 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 171;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_expression_value_63 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[6]);

            if (tmp_expression_value_63 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_63 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_63 == NULL)) {
                        tmp_expression_value_63 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_63 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_25);

                        exception_lineno = 172;
                        type_description_2 = "o";
                        goto frame_exception_exit_7;
                    }
                    Py_INCREF(tmp_expression_value_63);
                } else {
                    goto frame_exception_exit_7;
                }
            }

            tmp_tuple_element_36 = LOOKUP_ATTRIBUTE(tmp_expression_value_63, mod_consts[34]);
            Py_DECREF(tmp_expression_value_63);
            if (tmp_tuple_element_36 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_25);

                exception_lineno = 172;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_args_value_24 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_24, 0, tmp_tuple_element_36);
            tmp_kwargs_value_24 = PyDict_Copy(mod_consts[83]);
            frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame.f_lineno = 171;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_25, tmp_args_value_24, tmp_kwargs_value_24);
            Py_DECREF(tmp_called_value_25);
            Py_DECREF(tmp_args_value_24);
            Py_DECREF(tmp_kwargs_value_24);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 171;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 171;
                type_description_2 = "o";
                goto frame_exception_exit_7;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_aae2ed367423a5fce3ebf6593eb0816b_7);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_6;

        frame_exception_exit_7:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_aae2ed367423a5fce3ebf6593eb0816b_7);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_aae2ed367423a5fce3ebf6593eb0816b_7, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_aae2ed367423a5fce3ebf6593eb0816b_7->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_aae2ed367423a5fce3ebf6593eb0816b_7, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_aae2ed367423a5fce3ebf6593eb0816b_7,
            type_description_2,
            outline_5_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_aae2ed367423a5fce3ebf6593eb0816b_7 == cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7);
            cache_frame_aae2ed367423a5fce3ebf6593eb0816b_7 = NULL;
        }

        assertFrameObject(frame_aae2ed367423a5fce3ebf6593eb0816b_7);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_6;

        frame_no_exception_6:;
        goto skip_nested_handling_6;
        nested_frame_exit_6:;

        goto try_except_handler_18;
        skip_nested_handling_6:;
        {
            nuitka_bool tmp_condition_result_36;
            PyObject *tmp_cmp_expr_left_6;
            PyObject *tmp_cmp_expr_right_6;
            CHECK_OBJECT(tmp_class_creation_2__bases);
            tmp_cmp_expr_left_6 = tmp_class_creation_2__bases;
            CHECK_OBJECT(tmp_class_creation_2__bases_orig);
            tmp_cmp_expr_right_6 = tmp_class_creation_2__bases_orig;
            tmp_condition_result_36 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_6, tmp_cmp_expr_right_6);
            if (tmp_condition_result_36 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 134;

                goto try_except_handler_18;
            }
            if (tmp_condition_result_36 == NUITKA_BOOL_TRUE) {
                goto branch_yes_24;
            } else {
                goto branch_no_24;
            }
        }
        branch_yes_24:;
        CHECK_OBJECT(tmp_class_creation_2__bases_orig);
        tmp_dictset_value = tmp_class_creation_2__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 134;

            goto try_except_handler_18;
        }
        branch_no_24:;
        {
            PyObject *tmp_assign_source_50;
            PyObject *tmp_called_value_26;
            PyObject *tmp_args_value_25;
            PyObject *tmp_tuple_element_37;
            PyObject *tmp_kwargs_value_25;
            CHECK_OBJECT(tmp_class_creation_2__metaclass);
            tmp_called_value_26 = tmp_class_creation_2__metaclass;
            tmp_tuple_element_37 = mod_consts[73];
            tmp_args_value_25 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_25, 0, tmp_tuple_element_37);
            CHECK_OBJECT(tmp_class_creation_2__bases);
            tmp_tuple_element_37 = tmp_class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_25, 1, tmp_tuple_element_37);
            tmp_tuple_element_37 = locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134;
            PyTuple_SET_ITEM0(tmp_args_value_25, 2, tmp_tuple_element_37);
            CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
            tmp_kwargs_value_25 = tmp_class_creation_2__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 134;
            tmp_assign_source_50 = CALL_FUNCTION(tmp_called_value_26, tmp_args_value_25, tmp_kwargs_value_25);
            Py_DECREF(tmp_args_value_25);
            if (tmp_assign_source_50 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 134;

                goto try_except_handler_18;
            }
            assert(outline_5_var___class__ == NULL);
            outline_5_var___class__ = tmp_assign_source_50;
        }
        CHECK_OBJECT(outline_5_var___class__);
        tmp_assign_source_49 = outline_5_var___class__;
        Py_INCREF(tmp_assign_source_49);
        goto try_return_handler_18;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_18:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134 = NULL;
        goto try_return_handler_17;
        // Exception handler code:
        try_except_handler_18:;
        exception_keeper_type_16 = exception_type;
        exception_keeper_value_16 = exception_value;
        exception_keeper_tb_16 = exception_tb;
        exception_keeper_lineno_16 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__6_Page_134 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_16;
        exception_value = exception_keeper_value_16;
        exception_tb = exception_keeper_tb_16;
        exception_lineno = exception_keeper_lineno_16;

        goto try_except_handler_17;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_17:;
        CHECK_OBJECT(outline_5_var___class__);
        Py_DECREF(outline_5_var___class__);
        outline_5_var___class__ = NULL;
        goto outline_result_6;
        // Exception handler code:
        try_except_handler_17:;
        exception_keeper_type_17 = exception_type;
        exception_keeper_value_17 = exception_value;
        exception_keeper_tb_17 = exception_tb;
        exception_keeper_lineno_17 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_17;
        exception_value = exception_keeper_value_17;
        exception_tb = exception_keeper_tb_17;
        exception_lineno = exception_keeper_lineno_17;

        goto outline_exception_6;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_6:;
        exception_lineno = 134;
        goto try_except_handler_16;
        outline_result_6:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[73], tmp_assign_source_49);
    }
    goto try_end_6;
    // Exception handler code:
    try_except_handler_16:;
    exception_keeper_type_18 = exception_type;
    exception_keeper_value_18 = exception_value;
    exception_keeper_tb_18 = exception_tb;
    exception_keeper_lineno_18 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_2__bases_orig);
    tmp_class_creation_2__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_2__bases);
    tmp_class_creation_2__bases = NULL;
    Py_XDECREF(tmp_class_creation_2__class_decl_dict);
    tmp_class_creation_2__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_2__metaclass);
    tmp_class_creation_2__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_2__prepared);
    tmp_class_creation_2__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_18;
    exception_value = exception_keeper_value_18;
    exception_tb = exception_keeper_tb_18;
    exception_lineno = exception_keeper_lineno_18;

    goto frame_exception_exit_1;
    // End of try:
    try_end_6:;
    CHECK_OBJECT(tmp_class_creation_2__bases_orig);
    Py_DECREF(tmp_class_creation_2__bases_orig);
    tmp_class_creation_2__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_2__bases);
    Py_DECREF(tmp_class_creation_2__bases);
    tmp_class_creation_2__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_2__class_decl_dict);
    Py_DECREF(tmp_class_creation_2__class_decl_dict);
    tmp_class_creation_2__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_2__metaclass);
    Py_DECREF(tmp_class_creation_2__metaclass);
    tmp_class_creation_2__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_2__prepared);
    Py_DECREF(tmp_class_creation_2__prepared);
    tmp_class_creation_2__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_51;
        PyObject *tmp_tuple_element_38;
        PyObject *tmp_expression_value_64;
        tmp_expression_value_64 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_64 == NULL)) {
            tmp_expression_value_64 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_64 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_tuple_element_38 = LOOKUP_ATTRIBUTE(tmp_expression_value_64, mod_consts[15]);
        if (tmp_tuple_element_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_assign_source_51 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_51, 0, tmp_tuple_element_38);
        assert(tmp_class_creation_3__bases_orig == NULL);
        tmp_class_creation_3__bases_orig = tmp_assign_source_51;
    }
    {
        PyObject *tmp_assign_source_52;
        PyObject *tmp_dircall_arg1_7;
        CHECK_OBJECT(tmp_class_creation_3__bases_orig);
        tmp_dircall_arg1_7 = tmp_class_creation_3__bases_orig;
        Py_INCREF(tmp_dircall_arg1_7);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_7};
            tmp_assign_source_52 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_52 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        assert(tmp_class_creation_3__bases == NULL);
        tmp_class_creation_3__bases = tmp_assign_source_52;
    }
    {
        PyObject *tmp_assign_source_53;
        tmp_assign_source_53 = PyDict_New();
        assert(tmp_class_creation_3__class_decl_dict == NULL);
        tmp_class_creation_3__class_decl_dict = tmp_assign_source_53;
    }
    {
        PyObject *tmp_assign_source_54;
        PyObject *tmp_metaclass_value_7;
        bool tmp_condition_result_37;
        PyObject *tmp_key_value_19;
        PyObject *tmp_dict_arg_value_19;
        PyObject *tmp_dict_arg_value_20;
        PyObject *tmp_key_value_20;
        nuitka_bool tmp_condition_result_38;
        int tmp_truth_name_7;
        PyObject *tmp_type_arg_13;
        PyObject *tmp_expression_value_65;
        PyObject *tmp_subscript_value_7;
        PyObject *tmp_bases_value_7;
        tmp_key_value_19 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
        tmp_dict_arg_value_19 = tmp_class_creation_3__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_19, tmp_key_value_19);
        assert(!(tmp_res == -1));
        tmp_condition_result_37 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_37 != false) {
            goto condexpr_true_13;
        } else {
            goto condexpr_false_13;
        }
        condexpr_true_13:;
        CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
        tmp_dict_arg_value_20 = tmp_class_creation_3__class_decl_dict;
        tmp_key_value_20 = mod_consts[16];
        tmp_metaclass_value_7 = DICT_GET_ITEM0(tmp_dict_arg_value_20, tmp_key_value_20);
        if (tmp_metaclass_value_7 == NULL) {
            tmp_metaclass_value_7 = Py_None;
        }
        assert(!(tmp_metaclass_value_7 == NULL));
        Py_INCREF(tmp_metaclass_value_7);
        goto condexpr_end_13;
        condexpr_false_13:;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_truth_name_7 = CHECK_IF_TRUE(tmp_class_creation_3__bases);
        if (tmp_truth_name_7 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_condition_result_38 = tmp_truth_name_7 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_38 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_14;
        } else {
            goto condexpr_false_14;
        }
        condexpr_true_14:;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_expression_value_65 = tmp_class_creation_3__bases;
        tmp_subscript_value_7 = mod_consts[7];
        tmp_type_arg_13 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_65, tmp_subscript_value_7, 0);
        if (tmp_type_arg_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_metaclass_value_7 = BUILTIN_TYPE1(tmp_type_arg_13);
        Py_DECREF(tmp_type_arg_13);
        if (tmp_metaclass_value_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        goto condexpr_end_14;
        condexpr_false_14:;
        tmp_metaclass_value_7 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_7);
        condexpr_end_14:;
        condexpr_end_13:;
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_bases_value_7 = tmp_class_creation_3__bases;
        tmp_assign_source_54 = SELECT_METACLASS(tmp_metaclass_value_7, tmp_bases_value_7);
        Py_DECREF(tmp_metaclass_value_7);
        if (tmp_assign_source_54 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        assert(tmp_class_creation_3__metaclass == NULL);
        tmp_class_creation_3__metaclass = tmp_assign_source_54;
    }
    {
        bool tmp_condition_result_39;
        PyObject *tmp_key_value_21;
        PyObject *tmp_dict_arg_value_21;
        tmp_key_value_21 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
        tmp_dict_arg_value_21 = tmp_class_creation_3__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_21, tmp_key_value_21);
        assert(!(tmp_res == -1));
        tmp_condition_result_39 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_39 != false) {
            goto branch_yes_25;
        } else {
            goto branch_no_25;
        }
    }
    branch_yes_25:;
    CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_3__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 177;

        goto try_except_handler_19;
    }
    branch_no_25:;
    {
        nuitka_bool tmp_condition_result_40;
        PyObject *tmp_expression_value_66;
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_expression_value_66 = tmp_class_creation_3__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_66, mod_consts[17]);
        tmp_condition_result_40 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_40 == NUITKA_BOOL_TRUE) {
            goto branch_yes_26;
        } else {
            goto branch_no_26;
        }
    }
    branch_yes_26:;
    {
        PyObject *tmp_assign_source_55;
        PyObject *tmp_called_value_27;
        PyObject *tmp_expression_value_67;
        PyObject *tmp_args_value_26;
        PyObject *tmp_tuple_element_39;
        PyObject *tmp_kwargs_value_26;
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_expression_value_67 = tmp_class_creation_3__metaclass;
        tmp_called_value_27 = LOOKUP_ATTRIBUTE(tmp_expression_value_67, mod_consts[17]);
        if (tmp_called_value_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_tuple_element_39 = mod_consts[84];
        tmp_args_value_26 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_26, 0, tmp_tuple_element_39);
        CHECK_OBJECT(tmp_class_creation_3__bases);
        tmp_tuple_element_39 = tmp_class_creation_3__bases;
        PyTuple_SET_ITEM0(tmp_args_value_26, 1, tmp_tuple_element_39);
        CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
        tmp_kwargs_value_26 = tmp_class_creation_3__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 177;
        tmp_assign_source_55 = CALL_FUNCTION(tmp_called_value_27, tmp_args_value_26, tmp_kwargs_value_26);
        Py_DECREF(tmp_called_value_27);
        Py_DECREF(tmp_args_value_26);
        if (tmp_assign_source_55 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        assert(tmp_class_creation_3__prepared == NULL);
        tmp_class_creation_3__prepared = tmp_assign_source_55;
    }
    {
        bool tmp_condition_result_41;
        PyObject *tmp_operand_value_7;
        PyObject *tmp_expression_value_68;
        CHECK_OBJECT(tmp_class_creation_3__prepared);
        tmp_expression_value_68 = tmp_class_creation_3__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_68, mod_consts[19]);
        tmp_operand_value_7 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_7);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_condition_result_41 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_41 != false) {
            goto branch_yes_27;
        } else {
            goto branch_no_27;
        }
    }
    branch_yes_27:;
    {
        PyObject *tmp_raise_type_7;
        PyObject *tmp_raise_value_7;
        PyObject *tmp_mod_expr_left_7;
        PyObject *tmp_mod_expr_right_7;
        PyObject *tmp_tuple_element_40;
        PyObject *tmp_getattr_target_7;
        PyObject *tmp_getattr_attr_7;
        PyObject *tmp_getattr_default_7;
        tmp_raise_type_7 = PyExc_TypeError;
        tmp_mod_expr_left_7 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_3__metaclass);
        tmp_getattr_target_7 = tmp_class_creation_3__metaclass;
        tmp_getattr_attr_7 = mod_consts[21];
        tmp_getattr_default_7 = mod_consts[22];
        tmp_tuple_element_40 = BUILTIN_GETATTR(tmp_getattr_target_7, tmp_getattr_attr_7, tmp_getattr_default_7);
        if (tmp_tuple_element_40 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        tmp_mod_expr_right_7 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_69;
            PyObject *tmp_type_arg_14;
            PyTuple_SET_ITEM(tmp_mod_expr_right_7, 0, tmp_tuple_element_40);
            CHECK_OBJECT(tmp_class_creation_3__prepared);
            tmp_type_arg_14 = tmp_class_creation_3__prepared;
            tmp_expression_value_69 = BUILTIN_TYPE1(tmp_type_arg_14);
            assert(!(tmp_expression_value_69 == NULL));
            tmp_tuple_element_40 = LOOKUP_ATTRIBUTE(tmp_expression_value_69, mod_consts[21]);
            Py_DECREF(tmp_expression_value_69);
            if (tmp_tuple_element_40 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 177;

                goto tuple_build_exception_7;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_7, 1, tmp_tuple_element_40);
        }
        goto tuple_build_noexception_7;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_7:;
        Py_DECREF(tmp_mod_expr_right_7);
        goto try_except_handler_19;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_7:;
        tmp_raise_value_7 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_7, tmp_mod_expr_right_7);
        Py_DECREF(tmp_mod_expr_right_7);
        if (tmp_raise_value_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_19;
        }
        exception_type = tmp_raise_type_7;
        Py_INCREF(tmp_raise_type_7);
        exception_value = tmp_raise_value_7;
        exception_lineno = 177;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_19;
    }
    branch_no_27:;
    goto branch_end_26;
    branch_no_26:;
    {
        PyObject *tmp_assign_source_56;
        tmp_assign_source_56 = PyDict_New();
        assert(tmp_class_creation_3__prepared == NULL);
        tmp_class_creation_3__prepared = tmp_assign_source_56;
    }
    branch_end_26:;
    {
        PyObject *tmp_assign_source_57;
        {
            PyObject *tmp_set_locals_7;
            CHECK_OBJECT(tmp_class_creation_3__prepared);
            tmp_set_locals_7 = tmp_class_creation_3__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177 = tmp_set_locals_7;
            Py_INCREF(tmp_set_locals_7);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_21;
        }
        tmp_dictset_value = mod_consts[85];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_21;
        }
        tmp_dictset_value = mod_consts[84];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_21;
        }
        if (isFrameUnusable(cache_frame_c432345856637768f47cce9ceb801963_8)) {
            Py_XDECREF(cache_frame_c432345856637768f47cce9ceb801963_8);

#if _DEBUG_REFCOUNTS
            if (cache_frame_c432345856637768f47cce9ceb801963_8 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_c432345856637768f47cce9ceb801963_8 = MAKE_FUNCTION_FRAME(codeobj_c432345856637768f47cce9ceb801963, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_c432345856637768f47cce9ceb801963_8->m_type_description == NULL);
        frame_c432345856637768f47cce9ceb801963_8 = cache_frame_c432345856637768f47cce9ceb801963_8;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_c432345856637768f47cce9ceb801963_8);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_c432345856637768f47cce9ceb801963_8) == 2); // Frame stack

        // Framed code:
        // Tried code:
        {
            PyObject *tmp_assign_source_58;
            PyObject *tmp_tuple_element_41;
            PyObject *tmp_expression_value_70;
            tmp_expression_value_70 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_70 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_70 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_70 == NULL)) {
                        tmp_expression_value_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_70 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 219;
                        type_description_2 = "o";
                        goto try_except_handler_22;
                    }
                    Py_INCREF(tmp_expression_value_70);
                } else {
                    goto try_except_handler_22;
                }
            }

            tmp_tuple_element_41 = LOOKUP_ATTRIBUTE(tmp_expression_value_70, mod_consts[41]);
            Py_DECREF(tmp_expression_value_70);
            if (tmp_tuple_element_41 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_assign_source_58 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_58, 0, tmp_tuple_element_41);
            assert(tmp_Block$class_creation_1__bases_orig == NULL);
            tmp_Block$class_creation_1__bases_orig = tmp_assign_source_58;
        }
        {
            PyObject *tmp_assign_source_59;
            PyObject *tmp_dircall_arg1_8;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases_orig);
            tmp_dircall_arg1_8 = tmp_Block$class_creation_1__bases_orig;
            Py_INCREF(tmp_dircall_arg1_8);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_8};
                tmp_assign_source_59 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_59 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            assert(tmp_Block$class_creation_1__bases == NULL);
            tmp_Block$class_creation_1__bases = tmp_assign_source_59;
        }
        {
            PyObject *tmp_assign_source_60;
            tmp_assign_source_60 = PyDict_New();
            assert(tmp_Block$class_creation_1__class_decl_dict == NULL);
            tmp_Block$class_creation_1__class_decl_dict = tmp_assign_source_60;
        }
        {
            PyObject *tmp_assign_source_61;
            PyObject *tmp_metaclass_value_8;
            bool tmp_condition_result_42;
            PyObject *tmp_key_value_22;
            PyObject *tmp_dict_arg_value_22;
            PyObject *tmp_dict_arg_value_23;
            PyObject *tmp_key_value_23;
            nuitka_bool tmp_condition_result_43;
            int tmp_truth_name_8;
            PyObject *tmp_type_arg_15;
            PyObject *tmp_expression_value_71;
            PyObject *tmp_subscript_value_8;
            PyObject *tmp_bases_value_8;
            tmp_key_value_22 = mod_consts[16];
            CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_22 = tmp_Block$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_22, tmp_key_value_22);
            assert(!(tmp_res == -1));
            tmp_condition_result_42 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_42 != false) {
                goto condexpr_true_15;
            } else {
                goto condexpr_false_15;
            }
            condexpr_true_15:;
            CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_23 = tmp_Block$class_creation_1__class_decl_dict;
            tmp_key_value_23 = mod_consts[16];
            tmp_metaclass_value_8 = DICT_GET_ITEM0(tmp_dict_arg_value_23, tmp_key_value_23);
            if (tmp_metaclass_value_8 == NULL) {
                tmp_metaclass_value_8 = Py_None;
            }
            assert(!(tmp_metaclass_value_8 == NULL));
            Py_INCREF(tmp_metaclass_value_8);
            goto condexpr_end_15;
            condexpr_false_15:;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_truth_name_8 = CHECK_IF_TRUE(tmp_Block$class_creation_1__bases);
            if (tmp_truth_name_8 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_condition_result_43 = tmp_truth_name_8 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_43 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_16;
            } else {
                goto condexpr_false_16;
            }
            condexpr_true_16:;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_expression_value_71 = tmp_Block$class_creation_1__bases;
            tmp_subscript_value_8 = mod_consts[7];
            tmp_type_arg_15 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_71, tmp_subscript_value_8, 0);
            if (tmp_type_arg_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_metaclass_value_8 = BUILTIN_TYPE1(tmp_type_arg_15);
            Py_DECREF(tmp_type_arg_15);
            if (tmp_metaclass_value_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            goto condexpr_end_16;
            condexpr_false_16:;
            tmp_metaclass_value_8 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_8);
            condexpr_end_16:;
            condexpr_end_15:;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_bases_value_8 = tmp_Block$class_creation_1__bases;
            tmp_assign_source_61 = SELECT_METACLASS(tmp_metaclass_value_8, tmp_bases_value_8);
            Py_DECREF(tmp_metaclass_value_8);
            if (tmp_assign_source_61 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            assert(tmp_Block$class_creation_1__metaclass == NULL);
            tmp_Block$class_creation_1__metaclass = tmp_assign_source_61;
        }
        {
            bool tmp_condition_result_44;
            PyObject *tmp_key_value_24;
            PyObject *tmp_dict_arg_value_24;
            tmp_key_value_24 = mod_consts[16];
            CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_24 = tmp_Block$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_24, tmp_key_value_24);
            assert(!(tmp_res == -1));
            tmp_condition_result_44 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_44 != false) {
                goto branch_yes_28;
            } else {
                goto branch_no_28;
            }
        }
        branch_yes_28:;
        CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
        tmp_dictdel_dict = tmp_Block$class_creation_1__class_decl_dict;
        tmp_dictdel_key = mod_consts[16];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_22;
        }
        branch_no_28:;
        {
            nuitka_bool tmp_condition_result_45;
            PyObject *tmp_expression_value_72;
            CHECK_OBJECT(tmp_Block$class_creation_1__metaclass);
            tmp_expression_value_72 = tmp_Block$class_creation_1__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_72, mod_consts[17]);
            tmp_condition_result_45 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_45 == NUITKA_BOOL_TRUE) {
                goto branch_yes_29;
            } else {
                goto branch_no_29;
            }
        }
        branch_yes_29:;
        {
            PyObject *tmp_assign_source_62;
            PyObject *tmp_called_value_28;
            PyObject *tmp_expression_value_73;
            PyObject *tmp_args_value_27;
            PyObject *tmp_tuple_element_42;
            PyObject *tmp_kwargs_value_27;
            CHECK_OBJECT(tmp_Block$class_creation_1__metaclass);
            tmp_expression_value_73 = tmp_Block$class_creation_1__metaclass;
            tmp_called_value_28 = LOOKUP_ATTRIBUTE(tmp_expression_value_73, mod_consts[17]);
            if (tmp_called_value_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_tuple_element_42 = mod_consts[86];
            tmp_args_value_27 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_27, 0, tmp_tuple_element_42);
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_tuple_element_42 = tmp_Block$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_27, 1, tmp_tuple_element_42);
            CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
            tmp_kwargs_value_27 = tmp_Block$class_creation_1__class_decl_dict;
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 219;
            tmp_assign_source_62 = CALL_FUNCTION(tmp_called_value_28, tmp_args_value_27, tmp_kwargs_value_27);
            Py_DECREF(tmp_called_value_28);
            Py_DECREF(tmp_args_value_27);
            if (tmp_assign_source_62 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            assert(tmp_Block$class_creation_1__prepared == NULL);
            tmp_Block$class_creation_1__prepared = tmp_assign_source_62;
        }
        {
            bool tmp_condition_result_46;
            PyObject *tmp_operand_value_8;
            PyObject *tmp_expression_value_74;
            CHECK_OBJECT(tmp_Block$class_creation_1__prepared);
            tmp_expression_value_74 = tmp_Block$class_creation_1__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_74, mod_consts[19]);
            tmp_operand_value_8 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_8);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_condition_result_46 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_46 != false) {
                goto branch_yes_30;
            } else {
                goto branch_no_30;
            }
        }
        branch_yes_30:;
        {
            PyObject *tmp_raise_type_8;
            PyObject *tmp_raise_value_8;
            PyObject *tmp_mod_expr_left_8;
            PyObject *tmp_mod_expr_right_8;
            PyObject *tmp_tuple_element_43;
            PyObject *tmp_getattr_target_8;
            PyObject *tmp_getattr_attr_8;
            PyObject *tmp_getattr_default_8;
            tmp_raise_type_8 = PyExc_TypeError;
            tmp_mod_expr_left_8 = mod_consts[20];
            CHECK_OBJECT(tmp_Block$class_creation_1__metaclass);
            tmp_getattr_target_8 = tmp_Block$class_creation_1__metaclass;
            tmp_getattr_attr_8 = mod_consts[21];
            tmp_getattr_default_8 = mod_consts[22];
            tmp_tuple_element_43 = BUILTIN_GETATTR(tmp_getattr_target_8, tmp_getattr_attr_8, tmp_getattr_default_8);
            if (tmp_tuple_element_43 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            tmp_mod_expr_right_8 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_75;
                PyObject *tmp_type_arg_16;
                PyTuple_SET_ITEM(tmp_mod_expr_right_8, 0, tmp_tuple_element_43);
                CHECK_OBJECT(tmp_Block$class_creation_1__prepared);
                tmp_type_arg_16 = tmp_Block$class_creation_1__prepared;
                tmp_expression_value_75 = BUILTIN_TYPE1(tmp_type_arg_16);
                assert(!(tmp_expression_value_75 == NULL));
                tmp_tuple_element_43 = LOOKUP_ATTRIBUTE(tmp_expression_value_75, mod_consts[21]);
                Py_DECREF(tmp_expression_value_75);
                if (tmp_tuple_element_43 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 219;
                    type_description_2 = "o";
                    goto tuple_build_exception_8;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_8, 1, tmp_tuple_element_43);
            }
            goto tuple_build_noexception_8;
            // Exception handling pass through code for tuple_build:
            tuple_build_exception_8:;
            Py_DECREF(tmp_mod_expr_right_8);
            goto try_except_handler_22;
            // Finished with no exception for tuple_build:
            tuple_build_noexception_8:;
            tmp_raise_value_8 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_8, tmp_mod_expr_right_8);
            Py_DECREF(tmp_mod_expr_right_8);
            if (tmp_raise_value_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_22;
            }
            exception_type = tmp_raise_type_8;
            Py_INCREF(tmp_raise_type_8);
            exception_value = tmp_raise_value_8;
            exception_lineno = 219;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_22;
        }
        branch_no_30:;
        goto branch_end_29;
        branch_no_29:;
        {
            PyObject *tmp_assign_source_63;
            tmp_assign_source_63 = PyDict_New();
            assert(tmp_Block$class_creation_1__prepared == NULL);
            tmp_Block$class_creation_1__prepared = tmp_assign_source_63;
        }
        branch_end_29:;
        {
            PyObject *tmp_set_locals_8;
            CHECK_OBJECT(tmp_Block$class_creation_1__prepared);
            tmp_set_locals_8 = tmp_Block$class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219 = tmp_set_locals_8;
            Py_INCREF(tmp_set_locals_8);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_24;
        }
        tmp_dictset_value = mod_consts[87];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_24;
        }
        tmp_dictset_value = mod_consts[88];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_24;
        }
        if (isFrameUnusable(cache_frame_a78d2cc6bb506efb06d14111c3854097_9)) {
            Py_XDECREF(cache_frame_a78d2cc6bb506efb06d14111c3854097_9);

#if _DEBUG_REFCOUNTS
            if (cache_frame_a78d2cc6bb506efb06d14111c3854097_9 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_a78d2cc6bb506efb06d14111c3854097_9 = MAKE_FUNCTION_FRAME(codeobj_a78d2cc6bb506efb06d14111c3854097, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_a78d2cc6bb506efb06d14111c3854097_9->m_type_description == NULL);
        frame_a78d2cc6bb506efb06d14111c3854097_9 = cache_frame_a78d2cc6bb506efb06d14111c3854097_9;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_a78d2cc6bb506efb06d14111c3854097_9);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_a78d2cc6bb506efb06d14111c3854097_9) == 2); // Frame stack

        // Framed code:
        tmp_dictset_value = mod_consts[7];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[45], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 221;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }
        tmp_dictset_value = mod_consts[46];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[89], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 222;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }
        tmp_dictset_value = mod_consts[48];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[90], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 223;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }
        tmp_dictset_value = mod_consts[50];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[91], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 224;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }
        tmp_dictset_value = mod_consts[52];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[92], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 225;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }
        tmp_dictset_value = mod_consts[54];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[93], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 226;
            type_description_3 = "o";
            goto frame_exception_exit_9;
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_a78d2cc6bb506efb06d14111c3854097_9);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_7;

        frame_exception_exit_9:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_a78d2cc6bb506efb06d14111c3854097_9);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_a78d2cc6bb506efb06d14111c3854097_9, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_a78d2cc6bb506efb06d14111c3854097_9->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_a78d2cc6bb506efb06d14111c3854097_9, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_a78d2cc6bb506efb06d14111c3854097_9,
            type_description_3,
            outline_7_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_a78d2cc6bb506efb06d14111c3854097_9 == cache_frame_a78d2cc6bb506efb06d14111c3854097_9) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_a78d2cc6bb506efb06d14111c3854097_9);
            cache_frame_a78d2cc6bb506efb06d14111c3854097_9 = NULL;
        }

        assertFrameObject(frame_a78d2cc6bb506efb06d14111c3854097_9);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_8;

        frame_no_exception_7:;
        goto skip_nested_handling_7;
        nested_frame_exit_8:;
        type_description_2 = "o";
        goto try_except_handler_24;
        skip_nested_handling_7:;
        {
            nuitka_bool tmp_condition_result_47;
            PyObject *tmp_cmp_expr_left_7;
            PyObject *tmp_cmp_expr_right_7;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_cmp_expr_left_7 = tmp_Block$class_creation_1__bases;
            CHECK_OBJECT(tmp_Block$class_creation_1__bases_orig);
            tmp_cmp_expr_right_7 = tmp_Block$class_creation_1__bases_orig;
            tmp_condition_result_47 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_7, tmp_cmp_expr_right_7);
            if (tmp_condition_result_47 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_24;
            }
            if (tmp_condition_result_47 == NUITKA_BOOL_TRUE) {
                goto branch_yes_31;
            } else {
                goto branch_no_31;
            }
        }
        branch_yes_31:;
        CHECK_OBJECT(tmp_Block$class_creation_1__bases_orig);
        tmp_dictset_value = tmp_Block$class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_24;
        }
        branch_no_31:;
        {
            PyObject *tmp_assign_source_64;
            PyObject *tmp_called_value_29;
            PyObject *tmp_args_value_28;
            PyObject *tmp_tuple_element_44;
            PyObject *tmp_kwargs_value_28;
            CHECK_OBJECT(tmp_Block$class_creation_1__metaclass);
            tmp_called_value_29 = tmp_Block$class_creation_1__metaclass;
            tmp_tuple_element_44 = mod_consts[86];
            tmp_args_value_28 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_28, 0, tmp_tuple_element_44);
            CHECK_OBJECT(tmp_Block$class_creation_1__bases);
            tmp_tuple_element_44 = tmp_Block$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_28, 1, tmp_tuple_element_44);
            tmp_tuple_element_44 = locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219;
            PyTuple_SET_ITEM0(tmp_args_value_28, 2, tmp_tuple_element_44);
            CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
            tmp_kwargs_value_28 = tmp_Block$class_creation_1__class_decl_dict;
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 219;
            tmp_assign_source_64 = CALL_FUNCTION(tmp_called_value_29, tmp_args_value_28, tmp_kwargs_value_28);
            Py_DECREF(tmp_args_value_28);
            if (tmp_assign_source_64 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 219;
                type_description_2 = "o";
                goto try_except_handler_24;
            }
            assert(outline_7_var___class__ == NULL);
            outline_7_var___class__ = tmp_assign_source_64;
        }
        CHECK_OBJECT(outline_7_var___class__);
        tmp_dictset_value = outline_7_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_24;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_24:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219 = NULL;
        goto try_return_handler_23;
        // Exception handler code:
        try_except_handler_24:;
        exception_keeper_type_19 = exception_type;
        exception_keeper_value_19 = exception_value;
        exception_keeper_tb_19 = exception_tb;
        exception_keeper_lineno_19 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__8_BlockType_219 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_19;
        exception_value = exception_keeper_value_19;
        exception_tb = exception_keeper_tb_19;
        exception_lineno = exception_keeper_lineno_19;

        goto try_except_handler_23;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_23:;
        CHECK_OBJECT(outline_7_var___class__);
        Py_DECREF(outline_7_var___class__);
        outline_7_var___class__ = NULL;
        goto outline_result_8;
        // Exception handler code:
        try_except_handler_23:;
        exception_keeper_type_20 = exception_type;
        exception_keeper_value_20 = exception_value;
        exception_keeper_tb_20 = exception_tb;
        exception_keeper_lineno_20 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_20;
        exception_value = exception_keeper_value_20;
        exception_tb = exception_keeper_tb_20;
        exception_lineno = exception_keeper_lineno_20;

        goto outline_exception_8;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_8:;
        exception_lineno = 219;
        goto try_except_handler_22;
        outline_result_8:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[86], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 219;
            type_description_2 = "o";
            goto try_except_handler_22;
        }
        goto try_end_7;
        // Exception handler code:
        try_except_handler_22:;
        exception_keeper_type_21 = exception_type;
        exception_keeper_value_21 = exception_value;
        exception_keeper_tb_21 = exception_tb;
        exception_keeper_lineno_21 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_Block$class_creation_1__bases_orig);
        tmp_Block$class_creation_1__bases_orig = NULL;
        Py_XDECREF(tmp_Block$class_creation_1__bases);
        tmp_Block$class_creation_1__bases = NULL;
        Py_XDECREF(tmp_Block$class_creation_1__class_decl_dict);
        tmp_Block$class_creation_1__class_decl_dict = NULL;
        Py_XDECREF(tmp_Block$class_creation_1__metaclass);
        tmp_Block$class_creation_1__metaclass = NULL;
        Py_XDECREF(tmp_Block$class_creation_1__prepared);
        tmp_Block$class_creation_1__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_21;
        exception_value = exception_keeper_value_21;
        exception_tb = exception_keeper_tb_21;
        exception_lineno = exception_keeper_lineno_21;

        goto frame_exception_exit_8;
        // End of try:
        try_end_7:;
        CHECK_OBJECT(tmp_Block$class_creation_1__bases_orig);
        Py_DECREF(tmp_Block$class_creation_1__bases_orig);
        tmp_Block$class_creation_1__bases_orig = NULL;
        CHECK_OBJECT(tmp_Block$class_creation_1__bases);
        Py_DECREF(tmp_Block$class_creation_1__bases);
        tmp_Block$class_creation_1__bases = NULL;
        CHECK_OBJECT(tmp_Block$class_creation_1__class_decl_dict);
        Py_DECREF(tmp_Block$class_creation_1__class_decl_dict);
        tmp_Block$class_creation_1__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_Block$class_creation_1__metaclass);
        Py_DECREF(tmp_Block$class_creation_1__metaclass);
        tmp_Block$class_creation_1__metaclass = NULL;
        CHECK_OBJECT(tmp_Block$class_creation_1__prepared);
        Py_DECREF(tmp_Block$class_creation_1__prepared);
        tmp_Block$class_creation_1__prepared = NULL;
        {
            PyObject *tmp_called_value_30;
            PyObject *tmp_expression_value_76;
            PyObject *tmp_args_value_29;
            PyObject *tmp_tuple_element_45;
            PyObject *tmp_expression_value_77;
            PyObject *tmp_kwargs_value_29;
            tmp_expression_value_76 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_76 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_76 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_76 == NULL)) {
                        tmp_expression_value_76 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_76 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 228;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_76);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_called_value_30 = LOOKUP_ATTRIBUTE(tmp_expression_value_76, mod_consts[30]);
            Py_DECREF(tmp_expression_value_76);
            if (tmp_called_value_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 228;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_expression_value_77 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_77 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_77 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_77 == NULL)) {
                        tmp_expression_value_77 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_77 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_30);

                        exception_lineno = 229;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_77);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_tuple_element_45 = LOOKUP_ATTRIBUTE(tmp_expression_value_77, mod_consts[65]);
            Py_DECREF(tmp_expression_value_77);
            if (tmp_tuple_element_45 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_30);

                exception_lineno = 229;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_args_value_29 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_29, 0, tmp_tuple_element_45);
            tmp_kwargs_value_29 = PyDict_Copy(mod_consts[75]);
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 228;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_30, tmp_args_value_29, tmp_kwargs_value_29);
            Py_DECREF(tmp_called_value_30);
            Py_DECREF(tmp_args_value_29);
            Py_DECREF(tmp_kwargs_value_29);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 228;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[76], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 228;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
        }
        {
            PyObject *tmp_called_value_31;
            PyObject *tmp_expression_value_78;
            PyObject *tmp_kw_call_arg_value_0_1;
            PyObject *tmp_expression_value_79;
            PyObject *tmp_kw_call_dict_value_0_1;
            PyObject *tmp_kw_call_dict_value_1_1;
            PyObject *tmp_expression_value_80;
            tmp_expression_value_78 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_78 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_78 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_78 == NULL)) {
                        tmp_expression_value_78 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_78 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 233;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_78);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_called_value_31 = LOOKUP_ATTRIBUTE(tmp_expression_value_78, mod_consts[30]);
            Py_DECREF(tmp_expression_value_78);
            if (tmp_called_value_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 233;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_expression_value_79 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_79 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_79 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_79 == NULL)) {
                        tmp_expression_value_79 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_79 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_31);

                        exception_lineno = 234;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_79);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_kw_call_arg_value_0_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_79, mod_consts[65]);
            Py_DECREF(tmp_expression_value_79);
            if (tmp_kw_call_arg_value_0_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_31);

                exception_lineno = 234;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_kw_call_dict_value_0_1 = mod_consts[48];
            tmp_expression_value_80 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[10]);

            if (tmp_expression_value_80 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_80 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[10]);

                    if (unlikely(tmp_expression_value_80 == NULL)) {
                        tmp_expression_value_80 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
                    }

                    if (tmp_expression_value_80 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_31);
                        Py_DECREF(tmp_kw_call_arg_value_0_1);

                        exception_lineno = 236;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_80);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_kw_call_dict_value_1_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_80, mod_consts[94]);
            Py_DECREF(tmp_expression_value_80);
            if (tmp_kw_call_dict_value_1_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_31);
                Py_DECREF(tmp_kw_call_arg_value_0_1);

                exception_lineno = 236;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 233;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_1};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_1, tmp_kw_call_dict_value_1_1};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_31, args, kw_values, mod_consts[95]);
            }

            Py_DECREF(tmp_called_value_31);
            Py_DECREF(tmp_kw_call_arg_value_0_1);
            Py_DECREF(tmp_kw_call_dict_value_1_1);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 233;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[96], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 233;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
        }
        {
            PyObject *tmp_called_value_32;
            PyObject *tmp_expression_value_81;
            PyObject *tmp_args_value_30;
            PyObject *tmp_tuple_element_46;
            PyObject *tmp_expression_value_82;
            PyObject *tmp_kwargs_value_30;
            tmp_expression_value_81 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_81 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_81 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_81 == NULL)) {
                        tmp_expression_value_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_81 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 238;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_81);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_called_value_32 = LOOKUP_ATTRIBUTE(tmp_expression_value_81, mod_consts[64]);
            Py_DECREF(tmp_expression_value_81);
            if (tmp_called_value_32 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 238;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_expression_value_82 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_82 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_82 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_82 == NULL)) {
                        tmp_expression_value_82 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_82 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_32);

                        exception_lineno = 239;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_82);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_tuple_element_46 = LOOKUP_ATTRIBUTE(tmp_expression_value_82, mod_consts[65]);
            Py_DECREF(tmp_expression_value_82);
            if (tmp_tuple_element_46 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_32);

                exception_lineno = 239;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_args_value_30 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_30, 0, tmp_tuple_element_46);
            tmp_kwargs_value_30 = PyDict_Copy(mod_consts[97]);
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 238;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_32, tmp_args_value_30, tmp_kwargs_value_30);
            Py_DECREF(tmp_called_value_32);
            Py_DECREF(tmp_args_value_30);
            Py_DECREF(tmp_kwargs_value_30);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 238;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[98], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 238;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
        }
        {
            PyObject *tmp_called_value_33;
            PyObject *tmp_expression_value_83;
            PyObject *tmp_kw_call_arg_value_0_2;
            PyObject *tmp_expression_value_84;
            PyObject *tmp_kw_call_dict_value_0_2;
            PyObject *tmp_kw_call_dict_value_1_2;
            tmp_expression_value_83 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_83 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_83 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_83 == NULL)) {
                        tmp_expression_value_83 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_83 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 243;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_83);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_called_value_33 = LOOKUP_ATTRIBUTE(tmp_expression_value_83, mod_consts[30]);
            Py_DECREF(tmp_expression_value_83);
            if (tmp_called_value_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 243;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_expression_value_84 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_84 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_84 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_84 == NULL)) {
                        tmp_expression_value_84 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_84 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_33);

                        exception_lineno = 244;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_84);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_kw_call_arg_value_0_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_84, mod_consts[56]);
            Py_DECREF(tmp_expression_value_84);
            if (tmp_kw_call_arg_value_0_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_33);

                exception_lineno = 244;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_kw_call_dict_value_0_2 = mod_consts[52];
            tmp_kw_call_dict_value_1_2 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[86]);

            if (unlikely(tmp_kw_call_dict_value_1_2 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_33);
                Py_DECREF(tmp_kw_call_arg_value_0_2);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[86]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 246;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }

            if (tmp_kw_call_dict_value_1_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_33);
                Py_DECREF(tmp_kw_call_arg_value_0_2);

                exception_lineno = 246;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 243;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_2};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_2, tmp_kw_call_dict_value_1_2};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_33, args, kw_values, mod_consts[99]);
            }

            Py_DECREF(tmp_called_value_33);
            Py_DECREF(tmp_kw_call_arg_value_0_2);
            Py_DECREF(tmp_kw_call_dict_value_1_2);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 243;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[100], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 243;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
        }
        {
            PyObject *tmp_called_value_34;
            PyObject *tmp_expression_value_85;
            PyObject *tmp_args_value_31;
            PyObject *tmp_tuple_element_47;
            PyObject *tmp_expression_value_86;
            PyObject *tmp_kwargs_value_31;
            tmp_expression_value_85 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_85 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_85 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_85 == NULL)) {
                        tmp_expression_value_85 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_85 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 248;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_85);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_called_value_34 = LOOKUP_ATTRIBUTE(tmp_expression_value_85, mod_consts[30]);
            Py_DECREF(tmp_expression_value_85);
            if (tmp_called_value_34 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 248;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_expression_value_86 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[6]);

            if (tmp_expression_value_86 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_86 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_86 == NULL)) {
                        tmp_expression_value_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_86 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_34);

                        exception_lineno = 249;
                        type_description_2 = "o";
                        goto frame_exception_exit_8;
                    }
                    Py_INCREF(tmp_expression_value_86);
                } else {
                    goto frame_exception_exit_8;
                }
            }

            tmp_tuple_element_47 = LOOKUP_ATTRIBUTE(tmp_expression_value_86, mod_consts[34]);
            Py_DECREF(tmp_expression_value_86);
            if (tmp_tuple_element_47 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_34);

                exception_lineno = 249;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_args_value_31 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_31, 0, tmp_tuple_element_47);
            tmp_kwargs_value_31 = PyDict_Copy(mod_consts[83]);
            frame_c432345856637768f47cce9ceb801963_8->m_frame.f_lineno = 248;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_34, tmp_args_value_31, tmp_kwargs_value_31);
            Py_DECREF(tmp_called_value_34);
            Py_DECREF(tmp_args_value_31);
            Py_DECREF(tmp_kwargs_value_31);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 248;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 248;
                type_description_2 = "o";
                goto frame_exception_exit_8;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_c432345856637768f47cce9ceb801963_8);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_8;

        frame_exception_exit_8:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_c432345856637768f47cce9ceb801963_8);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_c432345856637768f47cce9ceb801963_8, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_c432345856637768f47cce9ceb801963_8->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_c432345856637768f47cce9ceb801963_8, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_c432345856637768f47cce9ceb801963_8,
            type_description_2,
            outline_6_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_c432345856637768f47cce9ceb801963_8 == cache_frame_c432345856637768f47cce9ceb801963_8) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_c432345856637768f47cce9ceb801963_8);
            cache_frame_c432345856637768f47cce9ceb801963_8 = NULL;
        }

        assertFrameObject(frame_c432345856637768f47cce9ceb801963_8);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_7;

        frame_no_exception_8:;
        goto skip_nested_handling_8;
        nested_frame_exit_7:;

        goto try_except_handler_21;
        skip_nested_handling_8:;
        {
            nuitka_bool tmp_condition_result_48;
            PyObject *tmp_cmp_expr_left_8;
            PyObject *tmp_cmp_expr_right_8;
            CHECK_OBJECT(tmp_class_creation_3__bases);
            tmp_cmp_expr_left_8 = tmp_class_creation_3__bases;
            CHECK_OBJECT(tmp_class_creation_3__bases_orig);
            tmp_cmp_expr_right_8 = tmp_class_creation_3__bases_orig;
            tmp_condition_result_48 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_8, tmp_cmp_expr_right_8);
            if (tmp_condition_result_48 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 177;

                goto try_except_handler_21;
            }
            if (tmp_condition_result_48 == NUITKA_BOOL_TRUE) {
                goto branch_yes_32;
            } else {
                goto branch_no_32;
            }
        }
        branch_yes_32:;
        CHECK_OBJECT(tmp_class_creation_3__bases_orig);
        tmp_dictset_value = tmp_class_creation_3__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 177;

            goto try_except_handler_21;
        }
        branch_no_32:;
        {
            PyObject *tmp_assign_source_65;
            PyObject *tmp_called_value_35;
            PyObject *tmp_args_value_32;
            PyObject *tmp_tuple_element_48;
            PyObject *tmp_kwargs_value_32;
            CHECK_OBJECT(tmp_class_creation_3__metaclass);
            tmp_called_value_35 = tmp_class_creation_3__metaclass;
            tmp_tuple_element_48 = mod_consts[84];
            tmp_args_value_32 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_32, 0, tmp_tuple_element_48);
            CHECK_OBJECT(tmp_class_creation_3__bases);
            tmp_tuple_element_48 = tmp_class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_32, 1, tmp_tuple_element_48);
            tmp_tuple_element_48 = locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177;
            PyTuple_SET_ITEM0(tmp_args_value_32, 2, tmp_tuple_element_48);
            CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
            tmp_kwargs_value_32 = tmp_class_creation_3__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 177;
            tmp_assign_source_65 = CALL_FUNCTION(tmp_called_value_35, tmp_args_value_32, tmp_kwargs_value_32);
            Py_DECREF(tmp_args_value_32);
            if (tmp_assign_source_65 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 177;

                goto try_except_handler_21;
            }
            assert(outline_6_var___class__ == NULL);
            outline_6_var___class__ = tmp_assign_source_65;
        }
        CHECK_OBJECT(outline_6_var___class__);
        tmp_assign_source_57 = outline_6_var___class__;
        Py_INCREF(tmp_assign_source_57);
        goto try_return_handler_21;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_21:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177 = NULL;
        goto try_return_handler_20;
        // Exception handler code:
        try_except_handler_21:;
        exception_keeper_type_22 = exception_type;
        exception_keeper_value_22 = exception_value;
        exception_keeper_tb_22 = exception_tb;
        exception_keeper_lineno_22 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__7_Block_177 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_22;
        exception_value = exception_keeper_value_22;
        exception_tb = exception_keeper_tb_22;
        exception_lineno = exception_keeper_lineno_22;

        goto try_except_handler_20;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_20:;
        CHECK_OBJECT(outline_6_var___class__);
        Py_DECREF(outline_6_var___class__);
        outline_6_var___class__ = NULL;
        goto outline_result_7;
        // Exception handler code:
        try_except_handler_20:;
        exception_keeper_type_23 = exception_type;
        exception_keeper_value_23 = exception_value;
        exception_keeper_tb_23 = exception_tb;
        exception_keeper_lineno_23 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_23;
        exception_value = exception_keeper_value_23;
        exception_tb = exception_keeper_tb_23;
        exception_lineno = exception_keeper_lineno_23;

        goto outline_exception_7;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_7:;
        exception_lineno = 177;
        goto try_except_handler_19;
        outline_result_7:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[84], tmp_assign_source_57);
    }
    goto try_end_8;
    // Exception handler code:
    try_except_handler_19:;
    exception_keeper_type_24 = exception_type;
    exception_keeper_value_24 = exception_value;
    exception_keeper_tb_24 = exception_tb;
    exception_keeper_lineno_24 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_3__bases_orig);
    tmp_class_creation_3__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_3__bases);
    tmp_class_creation_3__bases = NULL;
    Py_XDECREF(tmp_class_creation_3__class_decl_dict);
    tmp_class_creation_3__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_3__metaclass);
    tmp_class_creation_3__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_3__prepared);
    tmp_class_creation_3__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_24;
    exception_value = exception_keeper_value_24;
    exception_tb = exception_keeper_tb_24;
    exception_lineno = exception_keeper_lineno_24;

    goto frame_exception_exit_1;
    // End of try:
    try_end_8:;
    CHECK_OBJECT(tmp_class_creation_3__bases_orig);
    Py_DECREF(tmp_class_creation_3__bases_orig);
    tmp_class_creation_3__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_3__bases);
    Py_DECREF(tmp_class_creation_3__bases);
    tmp_class_creation_3__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_3__class_decl_dict);
    Py_DECREF(tmp_class_creation_3__class_decl_dict);
    tmp_class_creation_3__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_3__metaclass);
    Py_DECREF(tmp_class_creation_3__metaclass);
    tmp_class_creation_3__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_3__prepared);
    Py_DECREF(tmp_class_creation_3__prepared);
    tmp_class_creation_3__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_66;
        PyObject *tmp_tuple_element_49;
        PyObject *tmp_expression_value_87;
        tmp_expression_value_87 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_87 == NULL)) {
            tmp_expression_value_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_87 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_tuple_element_49 = LOOKUP_ATTRIBUTE(tmp_expression_value_87, mod_consts[15]);
        if (tmp_tuple_element_49 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_assign_source_66 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_66, 0, tmp_tuple_element_49);
        assert(tmp_class_creation_4__bases_orig == NULL);
        tmp_class_creation_4__bases_orig = tmp_assign_source_66;
    }
    {
        PyObject *tmp_assign_source_67;
        PyObject *tmp_dircall_arg1_9;
        CHECK_OBJECT(tmp_class_creation_4__bases_orig);
        tmp_dircall_arg1_9 = tmp_class_creation_4__bases_orig;
        Py_INCREF(tmp_dircall_arg1_9);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_9};
            tmp_assign_source_67 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_67 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        assert(tmp_class_creation_4__bases == NULL);
        tmp_class_creation_4__bases = tmp_assign_source_67;
    }
    {
        PyObject *tmp_assign_source_68;
        tmp_assign_source_68 = PyDict_New();
        assert(tmp_class_creation_4__class_decl_dict == NULL);
        tmp_class_creation_4__class_decl_dict = tmp_assign_source_68;
    }
    {
        PyObject *tmp_assign_source_69;
        PyObject *tmp_metaclass_value_9;
        bool tmp_condition_result_49;
        PyObject *tmp_key_value_25;
        PyObject *tmp_dict_arg_value_25;
        PyObject *tmp_dict_arg_value_26;
        PyObject *tmp_key_value_26;
        nuitka_bool tmp_condition_result_50;
        int tmp_truth_name_9;
        PyObject *tmp_type_arg_17;
        PyObject *tmp_expression_value_88;
        PyObject *tmp_subscript_value_9;
        PyObject *tmp_bases_value_9;
        tmp_key_value_25 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
        tmp_dict_arg_value_25 = tmp_class_creation_4__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_25, tmp_key_value_25);
        assert(!(tmp_res == -1));
        tmp_condition_result_49 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_49 != false) {
            goto condexpr_true_17;
        } else {
            goto condexpr_false_17;
        }
        condexpr_true_17:;
        CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
        tmp_dict_arg_value_26 = tmp_class_creation_4__class_decl_dict;
        tmp_key_value_26 = mod_consts[16];
        tmp_metaclass_value_9 = DICT_GET_ITEM0(tmp_dict_arg_value_26, tmp_key_value_26);
        if (tmp_metaclass_value_9 == NULL) {
            tmp_metaclass_value_9 = Py_None;
        }
        assert(!(tmp_metaclass_value_9 == NULL));
        Py_INCREF(tmp_metaclass_value_9);
        goto condexpr_end_17;
        condexpr_false_17:;
        CHECK_OBJECT(tmp_class_creation_4__bases);
        tmp_truth_name_9 = CHECK_IF_TRUE(tmp_class_creation_4__bases);
        if (tmp_truth_name_9 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_condition_result_50 = tmp_truth_name_9 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_50 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_18;
        } else {
            goto condexpr_false_18;
        }
        condexpr_true_18:;
        CHECK_OBJECT(tmp_class_creation_4__bases);
        tmp_expression_value_88 = tmp_class_creation_4__bases;
        tmp_subscript_value_9 = mod_consts[7];
        tmp_type_arg_17 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_88, tmp_subscript_value_9, 0);
        if (tmp_type_arg_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_metaclass_value_9 = BUILTIN_TYPE1(tmp_type_arg_17);
        Py_DECREF(tmp_type_arg_17);
        if (tmp_metaclass_value_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        goto condexpr_end_18;
        condexpr_false_18:;
        tmp_metaclass_value_9 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_9);
        condexpr_end_18:;
        condexpr_end_17:;
        CHECK_OBJECT(tmp_class_creation_4__bases);
        tmp_bases_value_9 = tmp_class_creation_4__bases;
        tmp_assign_source_69 = SELECT_METACLASS(tmp_metaclass_value_9, tmp_bases_value_9);
        Py_DECREF(tmp_metaclass_value_9);
        if (tmp_assign_source_69 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        assert(tmp_class_creation_4__metaclass == NULL);
        tmp_class_creation_4__metaclass = tmp_assign_source_69;
    }
    {
        bool tmp_condition_result_51;
        PyObject *tmp_key_value_27;
        PyObject *tmp_dict_arg_value_27;
        tmp_key_value_27 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
        tmp_dict_arg_value_27 = tmp_class_creation_4__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_27, tmp_key_value_27);
        assert(!(tmp_res == -1));
        tmp_condition_result_51 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_51 != false) {
            goto branch_yes_33;
        } else {
            goto branch_no_33;
        }
    }
    branch_yes_33:;
    CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_4__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 254;

        goto try_except_handler_25;
    }
    branch_no_33:;
    {
        nuitka_bool tmp_condition_result_52;
        PyObject *tmp_expression_value_89;
        CHECK_OBJECT(tmp_class_creation_4__metaclass);
        tmp_expression_value_89 = tmp_class_creation_4__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_89, mod_consts[17]);
        tmp_condition_result_52 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_52 == NUITKA_BOOL_TRUE) {
            goto branch_yes_34;
        } else {
            goto branch_no_34;
        }
    }
    branch_yes_34:;
    {
        PyObject *tmp_assign_source_70;
        PyObject *tmp_called_value_36;
        PyObject *tmp_expression_value_90;
        PyObject *tmp_args_value_33;
        PyObject *tmp_tuple_element_50;
        PyObject *tmp_kwargs_value_33;
        CHECK_OBJECT(tmp_class_creation_4__metaclass);
        tmp_expression_value_90 = tmp_class_creation_4__metaclass;
        tmp_called_value_36 = LOOKUP_ATTRIBUTE(tmp_expression_value_90, mod_consts[17]);
        if (tmp_called_value_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_tuple_element_50 = mod_consts[101];
        tmp_args_value_33 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_33, 0, tmp_tuple_element_50);
        CHECK_OBJECT(tmp_class_creation_4__bases);
        tmp_tuple_element_50 = tmp_class_creation_4__bases;
        PyTuple_SET_ITEM0(tmp_args_value_33, 1, tmp_tuple_element_50);
        CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
        tmp_kwargs_value_33 = tmp_class_creation_4__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 254;
        tmp_assign_source_70 = CALL_FUNCTION(tmp_called_value_36, tmp_args_value_33, tmp_kwargs_value_33);
        Py_DECREF(tmp_called_value_36);
        Py_DECREF(tmp_args_value_33);
        if (tmp_assign_source_70 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        assert(tmp_class_creation_4__prepared == NULL);
        tmp_class_creation_4__prepared = tmp_assign_source_70;
    }
    {
        bool tmp_condition_result_53;
        PyObject *tmp_operand_value_9;
        PyObject *tmp_expression_value_91;
        CHECK_OBJECT(tmp_class_creation_4__prepared);
        tmp_expression_value_91 = tmp_class_creation_4__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_91, mod_consts[19]);
        tmp_operand_value_9 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_9);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_condition_result_53 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_53 != false) {
            goto branch_yes_35;
        } else {
            goto branch_no_35;
        }
    }
    branch_yes_35:;
    {
        PyObject *tmp_raise_type_9;
        PyObject *tmp_raise_value_9;
        PyObject *tmp_mod_expr_left_9;
        PyObject *tmp_mod_expr_right_9;
        PyObject *tmp_tuple_element_51;
        PyObject *tmp_getattr_target_9;
        PyObject *tmp_getattr_attr_9;
        PyObject *tmp_getattr_default_9;
        tmp_raise_type_9 = PyExc_TypeError;
        tmp_mod_expr_left_9 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_4__metaclass);
        tmp_getattr_target_9 = tmp_class_creation_4__metaclass;
        tmp_getattr_attr_9 = mod_consts[21];
        tmp_getattr_default_9 = mod_consts[22];
        tmp_tuple_element_51 = BUILTIN_GETATTR(tmp_getattr_target_9, tmp_getattr_attr_9, tmp_getattr_default_9);
        if (tmp_tuple_element_51 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        tmp_mod_expr_right_9 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_92;
            PyObject *tmp_type_arg_18;
            PyTuple_SET_ITEM(tmp_mod_expr_right_9, 0, tmp_tuple_element_51);
            CHECK_OBJECT(tmp_class_creation_4__prepared);
            tmp_type_arg_18 = tmp_class_creation_4__prepared;
            tmp_expression_value_92 = BUILTIN_TYPE1(tmp_type_arg_18);
            assert(!(tmp_expression_value_92 == NULL));
            tmp_tuple_element_51 = LOOKUP_ATTRIBUTE(tmp_expression_value_92, mod_consts[21]);
            Py_DECREF(tmp_expression_value_92);
            if (tmp_tuple_element_51 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 254;

                goto tuple_build_exception_9;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_9, 1, tmp_tuple_element_51);
        }
        goto tuple_build_noexception_9;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_9:;
        Py_DECREF(tmp_mod_expr_right_9);
        goto try_except_handler_25;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_9:;
        tmp_raise_value_9 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_9, tmp_mod_expr_right_9);
        Py_DECREF(tmp_mod_expr_right_9);
        if (tmp_raise_value_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_25;
        }
        exception_type = tmp_raise_type_9;
        Py_INCREF(tmp_raise_type_9);
        exception_value = tmp_raise_value_9;
        exception_lineno = 254;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_25;
    }
    branch_no_35:;
    goto branch_end_34;
    branch_no_34:;
    {
        PyObject *tmp_assign_source_71;
        tmp_assign_source_71 = PyDict_New();
        assert(tmp_class_creation_4__prepared == NULL);
        tmp_class_creation_4__prepared = tmp_assign_source_71;
    }
    branch_end_34:;
    {
        PyObject *tmp_assign_source_72;
        {
            PyObject *tmp_set_locals_9;
            CHECK_OBJECT(tmp_class_creation_4__prepared);
            tmp_set_locals_9 = tmp_class_creation_4__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254 = tmp_set_locals_9;
            Py_INCREF(tmp_set_locals_9);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_27;
        }
        tmp_dictset_value = mod_consts[102];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_27;
        }
        tmp_dictset_value = mod_consts[101];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_27;
        }
        if (isFrameUnusable(cache_frame_6f04537ce0314438b27dac197fa5c5b7_10)) {
            Py_XDECREF(cache_frame_6f04537ce0314438b27dac197fa5c5b7_10);

#if _DEBUG_REFCOUNTS
            if (cache_frame_6f04537ce0314438b27dac197fa5c5b7_10 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_6f04537ce0314438b27dac197fa5c5b7_10 = MAKE_FUNCTION_FRAME(codeobj_6f04537ce0314438b27dac197fa5c5b7, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_6f04537ce0314438b27dac197fa5c5b7_10->m_type_description == NULL);
        frame_6f04537ce0314438b27dac197fa5c5b7_10 = cache_frame_6f04537ce0314438b27dac197fa5c5b7_10;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_6f04537ce0314438b27dac197fa5c5b7_10);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_6f04537ce0314438b27dac197fa5c5b7_10) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_37;
            PyObject *tmp_expression_value_93;
            PyObject *tmp_args_value_34;
            PyObject *tmp_tuple_element_52;
            PyObject *tmp_expression_value_94;
            PyObject *tmp_kwargs_value_34;
            tmp_expression_value_93 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_93 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_93 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_93 == NULL)) {
                        tmp_expression_value_93 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_93 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 281;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_93);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_called_value_37 = LOOKUP_ATTRIBUTE(tmp_expression_value_93, mod_consts[30]);
            Py_DECREF(tmp_expression_value_93);
            if (tmp_called_value_37 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 281;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_expression_value_94 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_94 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_94 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_94 == NULL)) {
                        tmp_expression_value_94 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_94 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_37);

                        exception_lineno = 282;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_94);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_tuple_element_52 = LOOKUP_ATTRIBUTE(tmp_expression_value_94, mod_consts[65]);
            Py_DECREF(tmp_expression_value_94);
            if (tmp_tuple_element_52 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_37);

                exception_lineno = 282;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_args_value_34 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_34, 0, tmp_tuple_element_52);
            tmp_kwargs_value_34 = PyDict_Copy(mod_consts[75]);
            frame_6f04537ce0314438b27dac197fa5c5b7_10->m_frame.f_lineno = 281;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_37, tmp_args_value_34, tmp_kwargs_value_34);
            Py_DECREF(tmp_called_value_37);
            Py_DECREF(tmp_args_value_34);
            Py_DECREF(tmp_kwargs_value_34);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 281;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[76], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 281;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
        }
        {
            PyObject *tmp_called_value_38;
            PyObject *tmp_expression_value_95;
            PyObject *tmp_kw_call_arg_value_0_3;
            PyObject *tmp_expression_value_96;
            PyObject *tmp_kw_call_dict_value_0_3;
            PyObject *tmp_kw_call_dict_value_1_3;
            PyObject *tmp_expression_value_97;
            tmp_expression_value_95 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_95 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_95 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_95 == NULL)) {
                        tmp_expression_value_95 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_95 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 286;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_95);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_called_value_38 = LOOKUP_ATTRIBUTE(tmp_expression_value_95, mod_consts[30]);
            Py_DECREF(tmp_expression_value_95);
            if (tmp_called_value_38 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 286;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_expression_value_96 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_96 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_96 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_96 == NULL)) {
                        tmp_expression_value_96 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_96 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_38);

                        exception_lineno = 287;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_96);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_kw_call_arg_value_0_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_96, mod_consts[65]);
            Py_DECREF(tmp_expression_value_96);
            if (tmp_kw_call_arg_value_0_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_38);

                exception_lineno = 287;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_kw_call_dict_value_0_3 = mod_consts[48];
            tmp_expression_value_97 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[10]);

            if (tmp_expression_value_97 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_97 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[10]);

                    if (unlikely(tmp_expression_value_97 == NULL)) {
                        tmp_expression_value_97 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
                    }

                    if (tmp_expression_value_97 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_38);
                        Py_DECREF(tmp_kw_call_arg_value_0_3);

                        exception_lineno = 289;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_97);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_kw_call_dict_value_1_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_97, mod_consts[94]);
            Py_DECREF(tmp_expression_value_97);
            if (tmp_kw_call_dict_value_1_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_38);
                Py_DECREF(tmp_kw_call_arg_value_0_3);

                exception_lineno = 289;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            frame_6f04537ce0314438b27dac197fa5c5b7_10->m_frame.f_lineno = 286;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_3};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_3, tmp_kw_call_dict_value_1_3};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_38, args, kw_values, mod_consts[95]);
            }

            Py_DECREF(tmp_called_value_38);
            Py_DECREF(tmp_kw_call_arg_value_0_3);
            Py_DECREF(tmp_kw_call_dict_value_1_3);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 286;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[96], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 286;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
        }
        {
            PyObject *tmp_called_value_39;
            PyObject *tmp_expression_value_98;
            PyObject *tmp_args_value_35;
            PyObject *tmp_tuple_element_53;
            PyObject *tmp_expression_value_99;
            PyObject *tmp_kwargs_value_35;
            tmp_expression_value_98 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_98 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_98 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_98 == NULL)) {
                        tmp_expression_value_98 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_98 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 291;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_98);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_called_value_39 = LOOKUP_ATTRIBUTE(tmp_expression_value_98, mod_consts[64]);
            Py_DECREF(tmp_expression_value_98);
            if (tmp_called_value_39 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 291;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_expression_value_99 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_99 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_99 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_99 == NULL)) {
                        tmp_expression_value_99 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_99 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_39);

                        exception_lineno = 292;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_99);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_tuple_element_53 = LOOKUP_ATTRIBUTE(tmp_expression_value_99, mod_consts[65]);
            Py_DECREF(tmp_expression_value_99);
            if (tmp_tuple_element_53 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_39);

                exception_lineno = 292;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_args_value_35 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_35, 0, tmp_tuple_element_53);
            tmp_kwargs_value_35 = PyDict_Copy(mod_consts[103]);
            frame_6f04537ce0314438b27dac197fa5c5b7_10->m_frame.f_lineno = 291;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_39, tmp_args_value_35, tmp_kwargs_value_35);
            Py_DECREF(tmp_called_value_39);
            Py_DECREF(tmp_args_value_35);
            Py_DECREF(tmp_kwargs_value_35);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 291;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[104], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 291;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
        }
        {
            PyObject *tmp_called_value_40;
            PyObject *tmp_expression_value_100;
            PyObject *tmp_args_value_36;
            PyObject *tmp_tuple_element_54;
            PyObject *tmp_expression_value_101;
            PyObject *tmp_kwargs_value_36;
            tmp_expression_value_100 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_100 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_100 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_100 == NULL)) {
                        tmp_expression_value_100 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_100 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 296;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_100);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_called_value_40 = LOOKUP_ATTRIBUTE(tmp_expression_value_100, mod_consts[30]);
            Py_DECREF(tmp_expression_value_100);
            if (tmp_called_value_40 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 296;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_expression_value_101 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[6]);

            if (tmp_expression_value_101 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_101 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_101 == NULL)) {
                        tmp_expression_value_101 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_101 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_40);

                        exception_lineno = 297;
                        type_description_2 = "o";
                        goto frame_exception_exit_10;
                    }
                    Py_INCREF(tmp_expression_value_101);
                } else {
                    goto frame_exception_exit_10;
                }
            }

            tmp_tuple_element_54 = LOOKUP_ATTRIBUTE(tmp_expression_value_101, mod_consts[34]);
            Py_DECREF(tmp_expression_value_101);
            if (tmp_tuple_element_54 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_40);

                exception_lineno = 297;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_args_value_36 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_36, 0, tmp_tuple_element_54);
            tmp_kwargs_value_36 = PyDict_Copy(mod_consts[105]);
            frame_6f04537ce0314438b27dac197fa5c5b7_10->m_frame.f_lineno = 296;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_40, tmp_args_value_36, tmp_kwargs_value_36);
            Py_DECREF(tmp_called_value_40);
            Py_DECREF(tmp_args_value_36);
            Py_DECREF(tmp_kwargs_value_36);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 296;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 296;
                type_description_2 = "o";
                goto frame_exception_exit_10;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6f04537ce0314438b27dac197fa5c5b7_10);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_9;

        frame_exception_exit_10:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6f04537ce0314438b27dac197fa5c5b7_10);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_6f04537ce0314438b27dac197fa5c5b7_10, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_6f04537ce0314438b27dac197fa5c5b7_10->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_6f04537ce0314438b27dac197fa5c5b7_10, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_6f04537ce0314438b27dac197fa5c5b7_10,
            type_description_2,
            outline_8_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_6f04537ce0314438b27dac197fa5c5b7_10 == cache_frame_6f04537ce0314438b27dac197fa5c5b7_10) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_6f04537ce0314438b27dac197fa5c5b7_10);
            cache_frame_6f04537ce0314438b27dac197fa5c5b7_10 = NULL;
        }

        assertFrameObject(frame_6f04537ce0314438b27dac197fa5c5b7_10);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_9;

        frame_no_exception_9:;
        goto skip_nested_handling_9;
        nested_frame_exit_9:;

        goto try_except_handler_27;
        skip_nested_handling_9:;
        {
            nuitka_bool tmp_condition_result_54;
            PyObject *tmp_cmp_expr_left_9;
            PyObject *tmp_cmp_expr_right_9;
            CHECK_OBJECT(tmp_class_creation_4__bases);
            tmp_cmp_expr_left_9 = tmp_class_creation_4__bases;
            CHECK_OBJECT(tmp_class_creation_4__bases_orig);
            tmp_cmp_expr_right_9 = tmp_class_creation_4__bases_orig;
            tmp_condition_result_54 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_9, tmp_cmp_expr_right_9);
            if (tmp_condition_result_54 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 254;

                goto try_except_handler_27;
            }
            if (tmp_condition_result_54 == NUITKA_BOOL_TRUE) {
                goto branch_yes_36;
            } else {
                goto branch_no_36;
            }
        }
        branch_yes_36:;
        CHECK_OBJECT(tmp_class_creation_4__bases_orig);
        tmp_dictset_value = tmp_class_creation_4__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 254;

            goto try_except_handler_27;
        }
        branch_no_36:;
        {
            PyObject *tmp_assign_source_73;
            PyObject *tmp_called_value_41;
            PyObject *tmp_args_value_37;
            PyObject *tmp_tuple_element_55;
            PyObject *tmp_kwargs_value_37;
            CHECK_OBJECT(tmp_class_creation_4__metaclass);
            tmp_called_value_41 = tmp_class_creation_4__metaclass;
            tmp_tuple_element_55 = mod_consts[101];
            tmp_args_value_37 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_37, 0, tmp_tuple_element_55);
            CHECK_OBJECT(tmp_class_creation_4__bases);
            tmp_tuple_element_55 = tmp_class_creation_4__bases;
            PyTuple_SET_ITEM0(tmp_args_value_37, 1, tmp_tuple_element_55);
            tmp_tuple_element_55 = locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254;
            PyTuple_SET_ITEM0(tmp_args_value_37, 2, tmp_tuple_element_55);
            CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
            tmp_kwargs_value_37 = tmp_class_creation_4__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 254;
            tmp_assign_source_73 = CALL_FUNCTION(tmp_called_value_41, tmp_args_value_37, tmp_kwargs_value_37);
            Py_DECREF(tmp_args_value_37);
            if (tmp_assign_source_73 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 254;

                goto try_except_handler_27;
            }
            assert(outline_8_var___class__ == NULL);
            outline_8_var___class__ = tmp_assign_source_73;
        }
        CHECK_OBJECT(outline_8_var___class__);
        tmp_assign_source_72 = outline_8_var___class__;
        Py_INCREF(tmp_assign_source_72);
        goto try_return_handler_27;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_27:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254 = NULL;
        goto try_return_handler_26;
        // Exception handler code:
        try_except_handler_27:;
        exception_keeper_type_25 = exception_type;
        exception_keeper_value_25 = exception_value;
        exception_keeper_tb_25 = exception_tb;
        exception_keeper_lineno_25 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__9_Paragraph_254 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_25;
        exception_value = exception_keeper_value_25;
        exception_tb = exception_keeper_tb_25;
        exception_lineno = exception_keeper_lineno_25;

        goto try_except_handler_26;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_26:;
        CHECK_OBJECT(outline_8_var___class__);
        Py_DECREF(outline_8_var___class__);
        outline_8_var___class__ = NULL;
        goto outline_result_9;
        // Exception handler code:
        try_except_handler_26:;
        exception_keeper_type_26 = exception_type;
        exception_keeper_value_26 = exception_value;
        exception_keeper_tb_26 = exception_tb;
        exception_keeper_lineno_26 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_26;
        exception_value = exception_keeper_value_26;
        exception_tb = exception_keeper_tb_26;
        exception_lineno = exception_keeper_lineno_26;

        goto outline_exception_9;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_9:;
        exception_lineno = 254;
        goto try_except_handler_25;
        outline_result_9:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[101], tmp_assign_source_72);
    }
    goto try_end_9;
    // Exception handler code:
    try_except_handler_25:;
    exception_keeper_type_27 = exception_type;
    exception_keeper_value_27 = exception_value;
    exception_keeper_tb_27 = exception_tb;
    exception_keeper_lineno_27 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_4__bases_orig);
    tmp_class_creation_4__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_4__bases);
    tmp_class_creation_4__bases = NULL;
    Py_XDECREF(tmp_class_creation_4__class_decl_dict);
    tmp_class_creation_4__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_4__metaclass);
    tmp_class_creation_4__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_4__prepared);
    tmp_class_creation_4__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_27;
    exception_value = exception_keeper_value_27;
    exception_tb = exception_keeper_tb_27;
    exception_lineno = exception_keeper_lineno_27;

    goto frame_exception_exit_1;
    // End of try:
    try_end_9:;
    CHECK_OBJECT(tmp_class_creation_4__bases_orig);
    Py_DECREF(tmp_class_creation_4__bases_orig);
    tmp_class_creation_4__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_4__bases);
    Py_DECREF(tmp_class_creation_4__bases);
    tmp_class_creation_4__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_4__class_decl_dict);
    Py_DECREF(tmp_class_creation_4__class_decl_dict);
    tmp_class_creation_4__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_4__metaclass);
    Py_DECREF(tmp_class_creation_4__metaclass);
    tmp_class_creation_4__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_4__prepared);
    Py_DECREF(tmp_class_creation_4__prepared);
    tmp_class_creation_4__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_74;
        PyObject *tmp_tuple_element_56;
        PyObject *tmp_expression_value_102;
        tmp_expression_value_102 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_102 == NULL)) {
            tmp_expression_value_102 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_102 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_tuple_element_56 = LOOKUP_ATTRIBUTE(tmp_expression_value_102, mod_consts[15]);
        if (tmp_tuple_element_56 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_assign_source_74 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_74, 0, tmp_tuple_element_56);
        assert(tmp_class_creation_5__bases_orig == NULL);
        tmp_class_creation_5__bases_orig = tmp_assign_source_74;
    }
    {
        PyObject *tmp_assign_source_75;
        PyObject *tmp_dircall_arg1_10;
        CHECK_OBJECT(tmp_class_creation_5__bases_orig);
        tmp_dircall_arg1_10 = tmp_class_creation_5__bases_orig;
        Py_INCREF(tmp_dircall_arg1_10);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_10};
            tmp_assign_source_75 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_75 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        assert(tmp_class_creation_5__bases == NULL);
        tmp_class_creation_5__bases = tmp_assign_source_75;
    }
    {
        PyObject *tmp_assign_source_76;
        tmp_assign_source_76 = PyDict_New();
        assert(tmp_class_creation_5__class_decl_dict == NULL);
        tmp_class_creation_5__class_decl_dict = tmp_assign_source_76;
    }
    {
        PyObject *tmp_assign_source_77;
        PyObject *tmp_metaclass_value_10;
        bool tmp_condition_result_55;
        PyObject *tmp_key_value_28;
        PyObject *tmp_dict_arg_value_28;
        PyObject *tmp_dict_arg_value_29;
        PyObject *tmp_key_value_29;
        nuitka_bool tmp_condition_result_56;
        int tmp_truth_name_10;
        PyObject *tmp_type_arg_19;
        PyObject *tmp_expression_value_103;
        PyObject *tmp_subscript_value_10;
        PyObject *tmp_bases_value_10;
        tmp_key_value_28 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
        tmp_dict_arg_value_28 = tmp_class_creation_5__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_28, tmp_key_value_28);
        assert(!(tmp_res == -1));
        tmp_condition_result_55 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_55 != false) {
            goto condexpr_true_19;
        } else {
            goto condexpr_false_19;
        }
        condexpr_true_19:;
        CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
        tmp_dict_arg_value_29 = tmp_class_creation_5__class_decl_dict;
        tmp_key_value_29 = mod_consts[16];
        tmp_metaclass_value_10 = DICT_GET_ITEM0(tmp_dict_arg_value_29, tmp_key_value_29);
        if (tmp_metaclass_value_10 == NULL) {
            tmp_metaclass_value_10 = Py_None;
        }
        assert(!(tmp_metaclass_value_10 == NULL));
        Py_INCREF(tmp_metaclass_value_10);
        goto condexpr_end_19;
        condexpr_false_19:;
        CHECK_OBJECT(tmp_class_creation_5__bases);
        tmp_truth_name_10 = CHECK_IF_TRUE(tmp_class_creation_5__bases);
        if (tmp_truth_name_10 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_condition_result_56 = tmp_truth_name_10 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_56 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_20;
        } else {
            goto condexpr_false_20;
        }
        condexpr_true_20:;
        CHECK_OBJECT(tmp_class_creation_5__bases);
        tmp_expression_value_103 = tmp_class_creation_5__bases;
        tmp_subscript_value_10 = mod_consts[7];
        tmp_type_arg_19 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_103, tmp_subscript_value_10, 0);
        if (tmp_type_arg_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_metaclass_value_10 = BUILTIN_TYPE1(tmp_type_arg_19);
        Py_DECREF(tmp_type_arg_19);
        if (tmp_metaclass_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        goto condexpr_end_20;
        condexpr_false_20:;
        tmp_metaclass_value_10 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_10);
        condexpr_end_20:;
        condexpr_end_19:;
        CHECK_OBJECT(tmp_class_creation_5__bases);
        tmp_bases_value_10 = tmp_class_creation_5__bases;
        tmp_assign_source_77 = SELECT_METACLASS(tmp_metaclass_value_10, tmp_bases_value_10);
        Py_DECREF(tmp_metaclass_value_10);
        if (tmp_assign_source_77 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        assert(tmp_class_creation_5__metaclass == NULL);
        tmp_class_creation_5__metaclass = tmp_assign_source_77;
    }
    {
        bool tmp_condition_result_57;
        PyObject *tmp_key_value_30;
        PyObject *tmp_dict_arg_value_30;
        tmp_key_value_30 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
        tmp_dict_arg_value_30 = tmp_class_creation_5__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_30, tmp_key_value_30);
        assert(!(tmp_res == -1));
        tmp_condition_result_57 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_57 != false) {
            goto branch_yes_37;
        } else {
            goto branch_no_37;
        }
    }
    branch_yes_37:;
    CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_5__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 302;

        goto try_except_handler_28;
    }
    branch_no_37:;
    {
        nuitka_bool tmp_condition_result_58;
        PyObject *tmp_expression_value_104;
        CHECK_OBJECT(tmp_class_creation_5__metaclass);
        tmp_expression_value_104 = tmp_class_creation_5__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_104, mod_consts[17]);
        tmp_condition_result_58 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_58 == NUITKA_BOOL_TRUE) {
            goto branch_yes_38;
        } else {
            goto branch_no_38;
        }
    }
    branch_yes_38:;
    {
        PyObject *tmp_assign_source_78;
        PyObject *tmp_called_value_42;
        PyObject *tmp_expression_value_105;
        PyObject *tmp_args_value_38;
        PyObject *tmp_tuple_element_57;
        PyObject *tmp_kwargs_value_38;
        CHECK_OBJECT(tmp_class_creation_5__metaclass);
        tmp_expression_value_105 = tmp_class_creation_5__metaclass;
        tmp_called_value_42 = LOOKUP_ATTRIBUTE(tmp_expression_value_105, mod_consts[17]);
        if (tmp_called_value_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_tuple_element_57 = mod_consts[106];
        tmp_args_value_38 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_38, 0, tmp_tuple_element_57);
        CHECK_OBJECT(tmp_class_creation_5__bases);
        tmp_tuple_element_57 = tmp_class_creation_5__bases;
        PyTuple_SET_ITEM0(tmp_args_value_38, 1, tmp_tuple_element_57);
        CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
        tmp_kwargs_value_38 = tmp_class_creation_5__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 302;
        tmp_assign_source_78 = CALL_FUNCTION(tmp_called_value_42, tmp_args_value_38, tmp_kwargs_value_38);
        Py_DECREF(tmp_called_value_42);
        Py_DECREF(tmp_args_value_38);
        if (tmp_assign_source_78 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        assert(tmp_class_creation_5__prepared == NULL);
        tmp_class_creation_5__prepared = tmp_assign_source_78;
    }
    {
        bool tmp_condition_result_59;
        PyObject *tmp_operand_value_10;
        PyObject *tmp_expression_value_106;
        CHECK_OBJECT(tmp_class_creation_5__prepared);
        tmp_expression_value_106 = tmp_class_creation_5__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_106, mod_consts[19]);
        tmp_operand_value_10 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_10);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_condition_result_59 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_59 != false) {
            goto branch_yes_39;
        } else {
            goto branch_no_39;
        }
    }
    branch_yes_39:;
    {
        PyObject *tmp_raise_type_10;
        PyObject *tmp_raise_value_10;
        PyObject *tmp_mod_expr_left_10;
        PyObject *tmp_mod_expr_right_10;
        PyObject *tmp_tuple_element_58;
        PyObject *tmp_getattr_target_10;
        PyObject *tmp_getattr_attr_10;
        PyObject *tmp_getattr_default_10;
        tmp_raise_type_10 = PyExc_TypeError;
        tmp_mod_expr_left_10 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_5__metaclass);
        tmp_getattr_target_10 = tmp_class_creation_5__metaclass;
        tmp_getattr_attr_10 = mod_consts[21];
        tmp_getattr_default_10 = mod_consts[22];
        tmp_tuple_element_58 = BUILTIN_GETATTR(tmp_getattr_target_10, tmp_getattr_attr_10, tmp_getattr_default_10);
        if (tmp_tuple_element_58 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        tmp_mod_expr_right_10 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_107;
            PyObject *tmp_type_arg_20;
            PyTuple_SET_ITEM(tmp_mod_expr_right_10, 0, tmp_tuple_element_58);
            CHECK_OBJECT(tmp_class_creation_5__prepared);
            tmp_type_arg_20 = tmp_class_creation_5__prepared;
            tmp_expression_value_107 = BUILTIN_TYPE1(tmp_type_arg_20);
            assert(!(tmp_expression_value_107 == NULL));
            tmp_tuple_element_58 = LOOKUP_ATTRIBUTE(tmp_expression_value_107, mod_consts[21]);
            Py_DECREF(tmp_expression_value_107);
            if (tmp_tuple_element_58 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 302;

                goto tuple_build_exception_10;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_10, 1, tmp_tuple_element_58);
        }
        goto tuple_build_noexception_10;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_10:;
        Py_DECREF(tmp_mod_expr_right_10);
        goto try_except_handler_28;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_10:;
        tmp_raise_value_10 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_10, tmp_mod_expr_right_10);
        Py_DECREF(tmp_mod_expr_right_10);
        if (tmp_raise_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_28;
        }
        exception_type = tmp_raise_type_10;
        Py_INCREF(tmp_raise_type_10);
        exception_value = tmp_raise_value_10;
        exception_lineno = 302;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_28;
    }
    branch_no_39:;
    goto branch_end_38;
    branch_no_38:;
    {
        PyObject *tmp_assign_source_79;
        tmp_assign_source_79 = PyDict_New();
        assert(tmp_class_creation_5__prepared == NULL);
        tmp_class_creation_5__prepared = tmp_assign_source_79;
    }
    branch_end_38:;
    {
        PyObject *tmp_assign_source_80;
        {
            PyObject *tmp_set_locals_10;
            CHECK_OBJECT(tmp_class_creation_5__prepared);
            tmp_set_locals_10 = tmp_class_creation_5__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302 = tmp_set_locals_10;
            Py_INCREF(tmp_set_locals_10);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_30;
        }
        tmp_dictset_value = mod_consts[107];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_30;
        }
        tmp_dictset_value = mod_consts[106];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_30;
        }
        if (isFrameUnusable(cache_frame_520a46f34edf5917d2b72256ec38a725_11)) {
            Py_XDECREF(cache_frame_520a46f34edf5917d2b72256ec38a725_11);

#if _DEBUG_REFCOUNTS
            if (cache_frame_520a46f34edf5917d2b72256ec38a725_11 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_520a46f34edf5917d2b72256ec38a725_11 = MAKE_FUNCTION_FRAME(codeobj_520a46f34edf5917d2b72256ec38a725, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_520a46f34edf5917d2b72256ec38a725_11->m_type_description == NULL);
        frame_520a46f34edf5917d2b72256ec38a725_11 = cache_frame_520a46f34edf5917d2b72256ec38a725_11;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_520a46f34edf5917d2b72256ec38a725_11);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_520a46f34edf5917d2b72256ec38a725_11) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_43;
            PyObject *tmp_expression_value_108;
            PyObject *tmp_args_value_39;
            PyObject *tmp_tuple_element_59;
            PyObject *tmp_expression_value_109;
            PyObject *tmp_kwargs_value_39;
            tmp_expression_value_108 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_108 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_108 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_108 == NULL)) {
                        tmp_expression_value_108 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_108 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 328;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_108);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_called_value_43 = LOOKUP_ATTRIBUTE(tmp_expression_value_108, mod_consts[30]);
            Py_DECREF(tmp_expression_value_108);
            if (tmp_called_value_43 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 328;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_expression_value_109 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_109 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_109 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_109 == NULL)) {
                        tmp_expression_value_109 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_109 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_43);

                        exception_lineno = 329;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_109);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_tuple_element_59 = LOOKUP_ATTRIBUTE(tmp_expression_value_109, mod_consts[65]);
            Py_DECREF(tmp_expression_value_109);
            if (tmp_tuple_element_59 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_43);

                exception_lineno = 329;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_args_value_39 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_39, 0, tmp_tuple_element_59);
            tmp_kwargs_value_39 = PyDict_Copy(mod_consts[75]);
            frame_520a46f34edf5917d2b72256ec38a725_11->m_frame.f_lineno = 328;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_43, tmp_args_value_39, tmp_kwargs_value_39);
            Py_DECREF(tmp_called_value_43);
            Py_DECREF(tmp_args_value_39);
            Py_DECREF(tmp_kwargs_value_39);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 328;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[76], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 328;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
        }
        {
            PyObject *tmp_called_value_44;
            PyObject *tmp_expression_value_110;
            PyObject *tmp_kw_call_arg_value_0_4;
            PyObject *tmp_expression_value_111;
            PyObject *tmp_kw_call_dict_value_0_4;
            PyObject *tmp_kw_call_dict_value_1_4;
            PyObject *tmp_expression_value_112;
            tmp_expression_value_110 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_110 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_110 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_110 == NULL)) {
                        tmp_expression_value_110 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_110 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 333;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_110);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_called_value_44 = LOOKUP_ATTRIBUTE(tmp_expression_value_110, mod_consts[30]);
            Py_DECREF(tmp_expression_value_110);
            if (tmp_called_value_44 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 333;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_expression_value_111 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_111 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_111 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_111 == NULL)) {
                        tmp_expression_value_111 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_111 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_44);

                        exception_lineno = 334;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_111);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_kw_call_arg_value_0_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_111, mod_consts[65]);
            Py_DECREF(tmp_expression_value_111);
            if (tmp_kw_call_arg_value_0_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_44);

                exception_lineno = 334;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_kw_call_dict_value_0_4 = mod_consts[48];
            tmp_expression_value_112 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[10]);

            if (tmp_expression_value_112 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_112 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[10]);

                    if (unlikely(tmp_expression_value_112 == NULL)) {
                        tmp_expression_value_112 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
                    }

                    if (tmp_expression_value_112 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_44);
                        Py_DECREF(tmp_kw_call_arg_value_0_4);

                        exception_lineno = 336;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_112);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_kw_call_dict_value_1_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_112, mod_consts[94]);
            Py_DECREF(tmp_expression_value_112);
            if (tmp_kw_call_dict_value_1_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_44);
                Py_DECREF(tmp_kw_call_arg_value_0_4);

                exception_lineno = 336;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            frame_520a46f34edf5917d2b72256ec38a725_11->m_frame.f_lineno = 333;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_4};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_4, tmp_kw_call_dict_value_1_4};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_44, args, kw_values, mod_consts[95]);
            }

            Py_DECREF(tmp_called_value_44);
            Py_DECREF(tmp_kw_call_arg_value_0_4);
            Py_DECREF(tmp_kw_call_dict_value_1_4);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 333;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[96], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 333;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
        }
        {
            PyObject *tmp_called_value_45;
            PyObject *tmp_expression_value_113;
            PyObject *tmp_args_value_40;
            PyObject *tmp_tuple_element_60;
            PyObject *tmp_expression_value_114;
            PyObject *tmp_kwargs_value_40;
            tmp_expression_value_113 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_113 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_113 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_113 == NULL)) {
                        tmp_expression_value_113 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_113 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 338;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_113);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_called_value_45 = LOOKUP_ATTRIBUTE(tmp_expression_value_113, mod_consts[64]);
            Py_DECREF(tmp_expression_value_113);
            if (tmp_called_value_45 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 338;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_expression_value_114 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_114 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_114 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_114 == NULL)) {
                        tmp_expression_value_114 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_114 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_45);

                        exception_lineno = 339;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_114);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_tuple_element_60 = LOOKUP_ATTRIBUTE(tmp_expression_value_114, mod_consts[65]);
            Py_DECREF(tmp_expression_value_114);
            if (tmp_tuple_element_60 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_45);

                exception_lineno = 339;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_args_value_40 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_40, 0, tmp_tuple_element_60);
            tmp_kwargs_value_40 = PyDict_Copy(mod_consts[108]);
            frame_520a46f34edf5917d2b72256ec38a725_11->m_frame.f_lineno = 338;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_45, tmp_args_value_40, tmp_kwargs_value_40);
            Py_DECREF(tmp_called_value_45);
            Py_DECREF(tmp_args_value_40);
            Py_DECREF(tmp_kwargs_value_40);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 338;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[109], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 338;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
        }
        {
            PyObject *tmp_called_value_46;
            PyObject *tmp_expression_value_115;
            PyObject *tmp_args_value_41;
            PyObject *tmp_tuple_element_61;
            PyObject *tmp_expression_value_116;
            PyObject *tmp_kwargs_value_41;
            tmp_expression_value_115 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_115 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_115 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_115 == NULL)) {
                        tmp_expression_value_115 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_115 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 343;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_115);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_called_value_46 = LOOKUP_ATTRIBUTE(tmp_expression_value_115, mod_consts[30]);
            Py_DECREF(tmp_expression_value_115);
            if (tmp_called_value_46 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 343;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_expression_value_116 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[6]);

            if (tmp_expression_value_116 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_116 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_116 == NULL)) {
                        tmp_expression_value_116 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_116 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_46);

                        exception_lineno = 344;
                        type_description_2 = "o";
                        goto frame_exception_exit_11;
                    }
                    Py_INCREF(tmp_expression_value_116);
                } else {
                    goto frame_exception_exit_11;
                }
            }

            tmp_tuple_element_61 = LOOKUP_ATTRIBUTE(tmp_expression_value_116, mod_consts[34]);
            Py_DECREF(tmp_expression_value_116);
            if (tmp_tuple_element_61 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_46);

                exception_lineno = 344;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_args_value_41 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_41, 0, tmp_tuple_element_61);
            tmp_kwargs_value_41 = PyDict_Copy(mod_consts[105]);
            frame_520a46f34edf5917d2b72256ec38a725_11->m_frame.f_lineno = 343;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_46, tmp_args_value_41, tmp_kwargs_value_41);
            Py_DECREF(tmp_called_value_46);
            Py_DECREF(tmp_args_value_41);
            Py_DECREF(tmp_kwargs_value_41);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 343;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 343;
                type_description_2 = "o";
                goto frame_exception_exit_11;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_520a46f34edf5917d2b72256ec38a725_11);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_10;

        frame_exception_exit_11:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_520a46f34edf5917d2b72256ec38a725_11);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_520a46f34edf5917d2b72256ec38a725_11, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_520a46f34edf5917d2b72256ec38a725_11->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_520a46f34edf5917d2b72256ec38a725_11, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_520a46f34edf5917d2b72256ec38a725_11,
            type_description_2,
            outline_9_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_520a46f34edf5917d2b72256ec38a725_11 == cache_frame_520a46f34edf5917d2b72256ec38a725_11) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_520a46f34edf5917d2b72256ec38a725_11);
            cache_frame_520a46f34edf5917d2b72256ec38a725_11 = NULL;
        }

        assertFrameObject(frame_520a46f34edf5917d2b72256ec38a725_11);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_10;

        frame_no_exception_10:;
        goto skip_nested_handling_10;
        nested_frame_exit_10:;

        goto try_except_handler_30;
        skip_nested_handling_10:;
        {
            nuitka_bool tmp_condition_result_60;
            PyObject *tmp_cmp_expr_left_10;
            PyObject *tmp_cmp_expr_right_10;
            CHECK_OBJECT(tmp_class_creation_5__bases);
            tmp_cmp_expr_left_10 = tmp_class_creation_5__bases;
            CHECK_OBJECT(tmp_class_creation_5__bases_orig);
            tmp_cmp_expr_right_10 = tmp_class_creation_5__bases_orig;
            tmp_condition_result_60 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_10, tmp_cmp_expr_right_10);
            if (tmp_condition_result_60 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 302;

                goto try_except_handler_30;
            }
            if (tmp_condition_result_60 == NUITKA_BOOL_TRUE) {
                goto branch_yes_40;
            } else {
                goto branch_no_40;
            }
        }
        branch_yes_40:;
        CHECK_OBJECT(tmp_class_creation_5__bases_orig);
        tmp_dictset_value = tmp_class_creation_5__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 302;

            goto try_except_handler_30;
        }
        branch_no_40:;
        {
            PyObject *tmp_assign_source_81;
            PyObject *tmp_called_value_47;
            PyObject *tmp_args_value_42;
            PyObject *tmp_tuple_element_62;
            PyObject *tmp_kwargs_value_42;
            CHECK_OBJECT(tmp_class_creation_5__metaclass);
            tmp_called_value_47 = tmp_class_creation_5__metaclass;
            tmp_tuple_element_62 = mod_consts[106];
            tmp_args_value_42 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_42, 0, tmp_tuple_element_62);
            CHECK_OBJECT(tmp_class_creation_5__bases);
            tmp_tuple_element_62 = tmp_class_creation_5__bases;
            PyTuple_SET_ITEM0(tmp_args_value_42, 1, tmp_tuple_element_62);
            tmp_tuple_element_62 = locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302;
            PyTuple_SET_ITEM0(tmp_args_value_42, 2, tmp_tuple_element_62);
            CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
            tmp_kwargs_value_42 = tmp_class_creation_5__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 302;
            tmp_assign_source_81 = CALL_FUNCTION(tmp_called_value_47, tmp_args_value_42, tmp_kwargs_value_42);
            Py_DECREF(tmp_args_value_42);
            if (tmp_assign_source_81 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 302;

                goto try_except_handler_30;
            }
            assert(outline_9_var___class__ == NULL);
            outline_9_var___class__ = tmp_assign_source_81;
        }
        CHECK_OBJECT(outline_9_var___class__);
        tmp_assign_source_80 = outline_9_var___class__;
        Py_INCREF(tmp_assign_source_80);
        goto try_return_handler_30;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_30:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302 = NULL;
        goto try_return_handler_29;
        // Exception handler code:
        try_except_handler_30:;
        exception_keeper_type_28 = exception_type;
        exception_keeper_value_28 = exception_value;
        exception_keeper_tb_28 = exception_tb;
        exception_keeper_lineno_28 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__10_Word_302 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_28;
        exception_value = exception_keeper_value_28;
        exception_tb = exception_keeper_tb_28;
        exception_lineno = exception_keeper_lineno_28;

        goto try_except_handler_29;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_29:;
        CHECK_OBJECT(outline_9_var___class__);
        Py_DECREF(outline_9_var___class__);
        outline_9_var___class__ = NULL;
        goto outline_result_10;
        // Exception handler code:
        try_except_handler_29:;
        exception_keeper_type_29 = exception_type;
        exception_keeper_value_29 = exception_value;
        exception_keeper_tb_29 = exception_tb;
        exception_keeper_lineno_29 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_29;
        exception_value = exception_keeper_value_29;
        exception_tb = exception_keeper_tb_29;
        exception_lineno = exception_keeper_lineno_29;

        goto outline_exception_10;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_10:;
        exception_lineno = 302;
        goto try_except_handler_28;
        outline_result_10:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[106], tmp_assign_source_80);
    }
    goto try_end_10;
    // Exception handler code:
    try_except_handler_28:;
    exception_keeper_type_30 = exception_type;
    exception_keeper_value_30 = exception_value;
    exception_keeper_tb_30 = exception_tb;
    exception_keeper_lineno_30 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_5__bases_orig);
    tmp_class_creation_5__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_5__bases);
    tmp_class_creation_5__bases = NULL;
    Py_XDECREF(tmp_class_creation_5__class_decl_dict);
    tmp_class_creation_5__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_5__metaclass);
    tmp_class_creation_5__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_5__prepared);
    tmp_class_creation_5__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_30;
    exception_value = exception_keeper_value_30;
    exception_tb = exception_keeper_tb_30;
    exception_lineno = exception_keeper_lineno_30;

    goto frame_exception_exit_1;
    // End of try:
    try_end_10:;
    CHECK_OBJECT(tmp_class_creation_5__bases_orig);
    Py_DECREF(tmp_class_creation_5__bases_orig);
    tmp_class_creation_5__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_5__bases);
    Py_DECREF(tmp_class_creation_5__bases);
    tmp_class_creation_5__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_5__class_decl_dict);
    Py_DECREF(tmp_class_creation_5__class_decl_dict);
    tmp_class_creation_5__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_5__metaclass);
    Py_DECREF(tmp_class_creation_5__metaclass);
    tmp_class_creation_5__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_5__prepared);
    Py_DECREF(tmp_class_creation_5__prepared);
    tmp_class_creation_5__prepared = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_82;
        PyObject *tmp_tuple_element_63;
        PyObject *tmp_expression_value_117;
        tmp_expression_value_117 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_117 == NULL)) {
            tmp_expression_value_117 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_117 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_tuple_element_63 = LOOKUP_ATTRIBUTE(tmp_expression_value_117, mod_consts[15]);
        if (tmp_tuple_element_63 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_assign_source_82 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_82, 0, tmp_tuple_element_63);
        assert(tmp_class_creation_6__bases_orig == NULL);
        tmp_class_creation_6__bases_orig = tmp_assign_source_82;
    }
    {
        PyObject *tmp_assign_source_83;
        PyObject *tmp_dircall_arg1_11;
        CHECK_OBJECT(tmp_class_creation_6__bases_orig);
        tmp_dircall_arg1_11 = tmp_class_creation_6__bases_orig;
        Py_INCREF(tmp_dircall_arg1_11);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_11};
            tmp_assign_source_83 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_83 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        assert(tmp_class_creation_6__bases == NULL);
        tmp_class_creation_6__bases = tmp_assign_source_83;
    }
    {
        PyObject *tmp_assign_source_84;
        tmp_assign_source_84 = PyDict_New();
        assert(tmp_class_creation_6__class_decl_dict == NULL);
        tmp_class_creation_6__class_decl_dict = tmp_assign_source_84;
    }
    {
        PyObject *tmp_assign_source_85;
        PyObject *tmp_metaclass_value_11;
        bool tmp_condition_result_61;
        PyObject *tmp_key_value_31;
        PyObject *tmp_dict_arg_value_31;
        PyObject *tmp_dict_arg_value_32;
        PyObject *tmp_key_value_32;
        nuitka_bool tmp_condition_result_62;
        int tmp_truth_name_11;
        PyObject *tmp_type_arg_21;
        PyObject *tmp_expression_value_118;
        PyObject *tmp_subscript_value_11;
        PyObject *tmp_bases_value_11;
        tmp_key_value_31 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
        tmp_dict_arg_value_31 = tmp_class_creation_6__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_31, tmp_key_value_31);
        assert(!(tmp_res == -1));
        tmp_condition_result_61 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_61 != false) {
            goto condexpr_true_21;
        } else {
            goto condexpr_false_21;
        }
        condexpr_true_21:;
        CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
        tmp_dict_arg_value_32 = tmp_class_creation_6__class_decl_dict;
        tmp_key_value_32 = mod_consts[16];
        tmp_metaclass_value_11 = DICT_GET_ITEM0(tmp_dict_arg_value_32, tmp_key_value_32);
        if (tmp_metaclass_value_11 == NULL) {
            tmp_metaclass_value_11 = Py_None;
        }
        assert(!(tmp_metaclass_value_11 == NULL));
        Py_INCREF(tmp_metaclass_value_11);
        goto condexpr_end_21;
        condexpr_false_21:;
        CHECK_OBJECT(tmp_class_creation_6__bases);
        tmp_truth_name_11 = CHECK_IF_TRUE(tmp_class_creation_6__bases);
        if (tmp_truth_name_11 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_condition_result_62 = tmp_truth_name_11 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        if (tmp_condition_result_62 == NUITKA_BOOL_TRUE) {
            goto condexpr_true_22;
        } else {
            goto condexpr_false_22;
        }
        condexpr_true_22:;
        CHECK_OBJECT(tmp_class_creation_6__bases);
        tmp_expression_value_118 = tmp_class_creation_6__bases;
        tmp_subscript_value_11 = mod_consts[7];
        tmp_type_arg_21 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_118, tmp_subscript_value_11, 0);
        if (tmp_type_arg_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_metaclass_value_11 = BUILTIN_TYPE1(tmp_type_arg_21);
        Py_DECREF(tmp_type_arg_21);
        if (tmp_metaclass_value_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        goto condexpr_end_22;
        condexpr_false_22:;
        tmp_metaclass_value_11 = (PyObject *)&PyType_Type;
        Py_INCREF(tmp_metaclass_value_11);
        condexpr_end_22:;
        condexpr_end_21:;
        CHECK_OBJECT(tmp_class_creation_6__bases);
        tmp_bases_value_11 = tmp_class_creation_6__bases;
        tmp_assign_source_85 = SELECT_METACLASS(tmp_metaclass_value_11, tmp_bases_value_11);
        Py_DECREF(tmp_metaclass_value_11);
        if (tmp_assign_source_85 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        assert(tmp_class_creation_6__metaclass == NULL);
        tmp_class_creation_6__metaclass = tmp_assign_source_85;
    }
    {
        bool tmp_condition_result_63;
        PyObject *tmp_key_value_33;
        PyObject *tmp_dict_arg_value_33;
        tmp_key_value_33 = mod_consts[16];
        CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
        tmp_dict_arg_value_33 = tmp_class_creation_6__class_decl_dict;
        tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_33, tmp_key_value_33);
        assert(!(tmp_res == -1));
        tmp_condition_result_63 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_63 != false) {
            goto branch_yes_41;
        } else {
            goto branch_no_41;
        }
    }
    branch_yes_41:;
    CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
    tmp_dictdel_dict = tmp_class_creation_6__class_decl_dict;
    tmp_dictdel_key = mod_consts[16];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 349;

        goto try_except_handler_31;
    }
    branch_no_41:;
    {
        nuitka_bool tmp_condition_result_64;
        PyObject *tmp_expression_value_119;
        CHECK_OBJECT(tmp_class_creation_6__metaclass);
        tmp_expression_value_119 = tmp_class_creation_6__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_119, mod_consts[17]);
        tmp_condition_result_64 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_64 == NUITKA_BOOL_TRUE) {
            goto branch_yes_42;
        } else {
            goto branch_no_42;
        }
    }
    branch_yes_42:;
    {
        PyObject *tmp_assign_source_86;
        PyObject *tmp_called_value_48;
        PyObject *tmp_expression_value_120;
        PyObject *tmp_args_value_43;
        PyObject *tmp_tuple_element_64;
        PyObject *tmp_kwargs_value_43;
        CHECK_OBJECT(tmp_class_creation_6__metaclass);
        tmp_expression_value_120 = tmp_class_creation_6__metaclass;
        tmp_called_value_48 = LOOKUP_ATTRIBUTE(tmp_expression_value_120, mod_consts[17]);
        if (tmp_called_value_48 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_tuple_element_64 = mod_consts[110];
        tmp_args_value_43 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_43, 0, tmp_tuple_element_64);
        CHECK_OBJECT(tmp_class_creation_6__bases);
        tmp_tuple_element_64 = tmp_class_creation_6__bases;
        PyTuple_SET_ITEM0(tmp_args_value_43, 1, tmp_tuple_element_64);
        CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
        tmp_kwargs_value_43 = tmp_class_creation_6__class_decl_dict;
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 349;
        tmp_assign_source_86 = CALL_FUNCTION(tmp_called_value_48, tmp_args_value_43, tmp_kwargs_value_43);
        Py_DECREF(tmp_called_value_48);
        Py_DECREF(tmp_args_value_43);
        if (tmp_assign_source_86 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        assert(tmp_class_creation_6__prepared == NULL);
        tmp_class_creation_6__prepared = tmp_assign_source_86;
    }
    {
        bool tmp_condition_result_65;
        PyObject *tmp_operand_value_11;
        PyObject *tmp_expression_value_121;
        CHECK_OBJECT(tmp_class_creation_6__prepared);
        tmp_expression_value_121 = tmp_class_creation_6__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_121, mod_consts[19]);
        tmp_operand_value_11 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_11);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_condition_result_65 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_65 != false) {
            goto branch_yes_43;
        } else {
            goto branch_no_43;
        }
    }
    branch_yes_43:;
    {
        PyObject *tmp_raise_type_11;
        PyObject *tmp_raise_value_11;
        PyObject *tmp_mod_expr_left_11;
        PyObject *tmp_mod_expr_right_11;
        PyObject *tmp_tuple_element_65;
        PyObject *tmp_getattr_target_11;
        PyObject *tmp_getattr_attr_11;
        PyObject *tmp_getattr_default_11;
        tmp_raise_type_11 = PyExc_TypeError;
        tmp_mod_expr_left_11 = mod_consts[20];
        CHECK_OBJECT(tmp_class_creation_6__metaclass);
        tmp_getattr_target_11 = tmp_class_creation_6__metaclass;
        tmp_getattr_attr_11 = mod_consts[21];
        tmp_getattr_default_11 = mod_consts[22];
        tmp_tuple_element_65 = BUILTIN_GETATTR(tmp_getattr_target_11, tmp_getattr_attr_11, tmp_getattr_default_11);
        if (tmp_tuple_element_65 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        tmp_mod_expr_right_11 = PyTuple_New(2);
        {
            PyObject *tmp_expression_value_122;
            PyObject *tmp_type_arg_22;
            PyTuple_SET_ITEM(tmp_mod_expr_right_11, 0, tmp_tuple_element_65);
            CHECK_OBJECT(tmp_class_creation_6__prepared);
            tmp_type_arg_22 = tmp_class_creation_6__prepared;
            tmp_expression_value_122 = BUILTIN_TYPE1(tmp_type_arg_22);
            assert(!(tmp_expression_value_122 == NULL));
            tmp_tuple_element_65 = LOOKUP_ATTRIBUTE(tmp_expression_value_122, mod_consts[21]);
            Py_DECREF(tmp_expression_value_122);
            if (tmp_tuple_element_65 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 349;

                goto tuple_build_exception_11;
            }
            PyTuple_SET_ITEM(tmp_mod_expr_right_11, 1, tmp_tuple_element_65);
        }
        goto tuple_build_noexception_11;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_11:;
        Py_DECREF(tmp_mod_expr_right_11);
        goto try_except_handler_31;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_11:;
        tmp_raise_value_11 = BINARY_OPERATION_MOD_OBJECT_UNICODE_TUPLE(tmp_mod_expr_left_11, tmp_mod_expr_right_11);
        Py_DECREF(tmp_mod_expr_right_11);
        if (tmp_raise_value_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_31;
        }
        exception_type = tmp_raise_type_11;
        Py_INCREF(tmp_raise_type_11);
        exception_value = tmp_raise_value_11;
        exception_lineno = 349;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_31;
    }
    branch_no_43:;
    goto branch_end_42;
    branch_no_42:;
    {
        PyObject *tmp_assign_source_87;
        tmp_assign_source_87 = PyDict_New();
        assert(tmp_class_creation_6__prepared == NULL);
        tmp_class_creation_6__prepared = tmp_assign_source_87;
    }
    branch_end_42:;
    {
        PyObject *tmp_assign_source_88;
        {
            PyObject *tmp_set_locals_11;
            CHECK_OBJECT(tmp_class_creation_6__prepared);
            tmp_set_locals_11 = tmp_class_creation_6__prepared;
            locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349 = tmp_set_locals_11;
            Py_INCREF(tmp_set_locals_11);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[23];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[24], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_33;
        }
        tmp_dictset_value = mod_consts[111];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_33;
        }
        tmp_dictset_value = mod_consts[110];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[26], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_33;
        }
        if (isFrameUnusable(cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12)) {
            Py_XDECREF(cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);

#if _DEBUG_REFCOUNTS
            if (cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 = MAKE_FUNCTION_FRAME(codeobj_b21bd41c7b77e2ce8f6979bb66f1458e, module_google$cloud$vision_v1$types$text_annotation, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_type_description == NULL);
        frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 = cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_49;
            PyObject *tmp_expression_value_123;
            PyObject *tmp_args_value_44;
            PyObject *tmp_tuple_element_66;
            PyObject *tmp_expression_value_124;
            PyObject *tmp_kwargs_value_44;
            tmp_expression_value_123 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_123 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_123 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_123 == NULL)) {
                        tmp_expression_value_123 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_123 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 375;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_123);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_called_value_49 = LOOKUP_ATTRIBUTE(tmp_expression_value_123, mod_consts[30]);
            Py_DECREF(tmp_expression_value_123);
            if (tmp_called_value_49 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 375;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_expression_value_124 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_124 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_124 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_124 == NULL)) {
                        tmp_expression_value_124 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_124 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_49);

                        exception_lineno = 376;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_124);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_tuple_element_66 = LOOKUP_ATTRIBUTE(tmp_expression_value_124, mod_consts[65]);
            Py_DECREF(tmp_expression_value_124);
            if (tmp_tuple_element_66 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_49);

                exception_lineno = 376;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_args_value_44 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_44, 0, tmp_tuple_element_66);
            tmp_kwargs_value_44 = PyDict_Copy(mod_consts[75]);
            frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_frame.f_lineno = 375;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_49, tmp_args_value_44, tmp_kwargs_value_44);
            Py_DECREF(tmp_called_value_49);
            Py_DECREF(tmp_args_value_44);
            Py_DECREF(tmp_kwargs_value_44);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 375;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[76], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 375;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
        }
        {
            PyObject *tmp_called_value_50;
            PyObject *tmp_expression_value_125;
            PyObject *tmp_kw_call_arg_value_0_5;
            PyObject *tmp_expression_value_126;
            PyObject *tmp_kw_call_dict_value_0_5;
            PyObject *tmp_kw_call_dict_value_1_5;
            PyObject *tmp_expression_value_127;
            tmp_expression_value_125 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_125 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_125 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_125 == NULL)) {
                        tmp_expression_value_125 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_125 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 380;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_125);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_called_value_50 = LOOKUP_ATTRIBUTE(tmp_expression_value_125, mod_consts[30]);
            Py_DECREF(tmp_expression_value_125);
            if (tmp_called_value_50 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 380;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_expression_value_126 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_126 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_126 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_126 == NULL)) {
                        tmp_expression_value_126 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_126 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_50);

                        exception_lineno = 381;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_126);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_kw_call_arg_value_0_5 = LOOKUP_ATTRIBUTE(tmp_expression_value_126, mod_consts[65]);
            Py_DECREF(tmp_expression_value_126);
            if (tmp_kw_call_arg_value_0_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_50);

                exception_lineno = 381;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_kw_call_dict_value_0_5 = mod_consts[48];
            tmp_expression_value_127 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[10]);

            if (tmp_expression_value_127 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_127 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[10]);

                    if (unlikely(tmp_expression_value_127 == NULL)) {
                        tmp_expression_value_127 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[10]);
                    }

                    if (tmp_expression_value_127 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_50);
                        Py_DECREF(tmp_kw_call_arg_value_0_5);

                        exception_lineno = 383;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_127);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_kw_call_dict_value_1_5 = LOOKUP_ATTRIBUTE(tmp_expression_value_127, mod_consts[94]);
            Py_DECREF(tmp_expression_value_127);
            if (tmp_kw_call_dict_value_1_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_50);
                Py_DECREF(tmp_kw_call_arg_value_0_5);

                exception_lineno = 383;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_frame.f_lineno = 380;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_5};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_5, tmp_kw_call_dict_value_1_5};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_50, args, kw_values, mod_consts[95]);
            }

            Py_DECREF(tmp_called_value_50);
            Py_DECREF(tmp_kw_call_arg_value_0_5);
            Py_DECREF(tmp_kw_call_dict_value_1_5);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 380;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[96], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 380;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
        }
        {
            PyObject *tmp_called_value_51;
            PyObject *tmp_expression_value_128;
            PyObject *tmp_args_value_45;
            PyObject *tmp_tuple_element_67;
            PyObject *tmp_expression_value_129;
            PyObject *tmp_kwargs_value_45;
            tmp_expression_value_128 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_128 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_128 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_128 == NULL)) {
                        tmp_expression_value_128 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_128 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 385;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_128);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_called_value_51 = LOOKUP_ATTRIBUTE(tmp_expression_value_128, mod_consts[30]);
            Py_DECREF(tmp_expression_value_128);
            if (tmp_called_value_51 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 385;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_expression_value_129 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_129 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_129 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_129 == NULL)) {
                        tmp_expression_value_129 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_129 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_51);

                        exception_lineno = 386;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_129);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_tuple_element_67 = LOOKUP_ATTRIBUTE(tmp_expression_value_129, mod_consts[31]);
            Py_DECREF(tmp_expression_value_129);
            if (tmp_tuple_element_67 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_51);

                exception_lineno = 386;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_args_value_45 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_45, 0, tmp_tuple_element_67);
            tmp_kwargs_value_45 = PyDict_Copy(mod_consts[79]);
            frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_frame.f_lineno = 385;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_51, tmp_args_value_45, tmp_kwargs_value_45);
            Py_DECREF(tmp_called_value_51);
            Py_DECREF(tmp_args_value_45);
            Py_DECREF(tmp_kwargs_value_45);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 385;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[72], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 385;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
        }
        {
            PyObject *tmp_called_value_52;
            PyObject *tmp_expression_value_130;
            PyObject *tmp_args_value_46;
            PyObject *tmp_tuple_element_68;
            PyObject *tmp_expression_value_131;
            PyObject *tmp_kwargs_value_46;
            tmp_expression_value_130 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_130 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_130 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_130 == NULL)) {
                        tmp_expression_value_130 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_130 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 389;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_130);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_called_value_52 = LOOKUP_ATTRIBUTE(tmp_expression_value_130, mod_consts[30]);
            Py_DECREF(tmp_expression_value_130);
            if (tmp_called_value_52 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 389;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_expression_value_131 = PyObject_GetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[6]);

            if (tmp_expression_value_131 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_131 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_131 == NULL)) {
                        tmp_expression_value_131 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_131 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_52);

                        exception_lineno = 390;
                        type_description_2 = "o";
                        goto frame_exception_exit_12;
                    }
                    Py_INCREF(tmp_expression_value_131);
                } else {
                    goto frame_exception_exit_12;
                }
            }

            tmp_tuple_element_68 = LOOKUP_ATTRIBUTE(tmp_expression_value_131, mod_consts[34]);
            Py_DECREF(tmp_expression_value_131);
            if (tmp_tuple_element_68 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_52);

                exception_lineno = 390;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_args_value_46 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_46, 0, tmp_tuple_element_68);
            tmp_kwargs_value_46 = PyDict_Copy(mod_consts[105]);
            frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_frame.f_lineno = 389;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_52, tmp_args_value_46, tmp_kwargs_value_46);
            Py_DECREF(tmp_called_value_52);
            Py_DECREF(tmp_args_value_46);
            Py_DECREF(tmp_kwargs_value_46);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 389;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[36], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 389;
                type_description_2 = "o";
                goto frame_exception_exit_12;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_11;

        frame_exception_exit_12:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_b21bd41c7b77e2ce8f6979bb66f1458e_12->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_b21bd41c7b77e2ce8f6979bb66f1458e_12, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_b21bd41c7b77e2ce8f6979bb66f1458e_12,
            type_description_2,
            outline_10_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 == cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);
            cache_frame_b21bd41c7b77e2ce8f6979bb66f1458e_12 = NULL;
        }

        assertFrameObject(frame_b21bd41c7b77e2ce8f6979bb66f1458e_12);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_11;

        frame_no_exception_11:;
        goto skip_nested_handling_11;
        nested_frame_exit_11:;

        goto try_except_handler_33;
        skip_nested_handling_11:;
        {
            nuitka_bool tmp_condition_result_66;
            PyObject *tmp_cmp_expr_left_11;
            PyObject *tmp_cmp_expr_right_11;
            CHECK_OBJECT(tmp_class_creation_6__bases);
            tmp_cmp_expr_left_11 = tmp_class_creation_6__bases;
            CHECK_OBJECT(tmp_class_creation_6__bases_orig);
            tmp_cmp_expr_right_11 = tmp_class_creation_6__bases_orig;
            tmp_condition_result_66 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_11, tmp_cmp_expr_right_11);
            if (tmp_condition_result_66 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 349;

                goto try_except_handler_33;
            }
            if (tmp_condition_result_66 == NUITKA_BOOL_TRUE) {
                goto branch_yes_44;
            } else {
                goto branch_no_44;
            }
        }
        branch_yes_44:;
        CHECK_OBJECT(tmp_class_creation_6__bases_orig);
        tmp_dictset_value = tmp_class_creation_6__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349, mod_consts[37], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 349;

            goto try_except_handler_33;
        }
        branch_no_44:;
        {
            PyObject *tmp_assign_source_89;
            PyObject *tmp_called_value_53;
            PyObject *tmp_args_value_47;
            PyObject *tmp_tuple_element_69;
            PyObject *tmp_kwargs_value_47;
            CHECK_OBJECT(tmp_class_creation_6__metaclass);
            tmp_called_value_53 = tmp_class_creation_6__metaclass;
            tmp_tuple_element_69 = mod_consts[110];
            tmp_args_value_47 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_47, 0, tmp_tuple_element_69);
            CHECK_OBJECT(tmp_class_creation_6__bases);
            tmp_tuple_element_69 = tmp_class_creation_6__bases;
            PyTuple_SET_ITEM0(tmp_args_value_47, 1, tmp_tuple_element_69);
            tmp_tuple_element_69 = locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349;
            PyTuple_SET_ITEM0(tmp_args_value_47, 2, tmp_tuple_element_69);
            CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
            tmp_kwargs_value_47 = tmp_class_creation_6__class_decl_dict;
            frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 349;
            tmp_assign_source_89 = CALL_FUNCTION(tmp_called_value_53, tmp_args_value_47, tmp_kwargs_value_47);
            Py_DECREF(tmp_args_value_47);
            if (tmp_assign_source_89 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 349;

                goto try_except_handler_33;
            }
            assert(outline_10_var___class__ == NULL);
            outline_10_var___class__ = tmp_assign_source_89;
        }
        CHECK_OBJECT(outline_10_var___class__);
        tmp_assign_source_88 = outline_10_var___class__;
        Py_INCREF(tmp_assign_source_88);
        goto try_return_handler_33;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_33:;
        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349 = NULL;
        goto try_return_handler_32;
        // Exception handler code:
        try_except_handler_33:;
        exception_keeper_type_31 = exception_type;
        exception_keeper_value_31 = exception_value;
        exception_keeper_tb_31 = exception_tb;
        exception_keeper_lineno_31 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349);
        locals_google$cloud$vision_v1$types$text_annotation$$$class__11_Symbol_349 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_31;
        exception_value = exception_keeper_value_31;
        exception_tb = exception_keeper_tb_31;
        exception_lineno = exception_keeper_lineno_31;

        goto try_except_handler_32;
        // End of try:
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_32:;
        CHECK_OBJECT(outline_10_var___class__);
        Py_DECREF(outline_10_var___class__);
        outline_10_var___class__ = NULL;
        goto outline_result_11;
        // Exception handler code:
        try_except_handler_32:;
        exception_keeper_type_32 = exception_type;
        exception_keeper_value_32 = exception_value;
        exception_keeper_tb_32 = exception_tb;
        exception_keeper_lineno_32 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        // Re-raise.
        exception_type = exception_keeper_type_32;
        exception_value = exception_keeper_value_32;
        exception_tb = exception_keeper_tb_32;
        exception_lineno = exception_keeper_lineno_32;

        goto outline_exception_11;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_11:;
        exception_lineno = 349;
        goto try_except_handler_31;
        outline_result_11:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[110], tmp_assign_source_88);
    }
    goto try_end_11;
    // Exception handler code:
    try_except_handler_31:;
    exception_keeper_type_33 = exception_type;
    exception_keeper_value_33 = exception_value;
    exception_keeper_tb_33 = exception_tb;
    exception_keeper_lineno_33 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_class_creation_6__bases_orig);
    tmp_class_creation_6__bases_orig = NULL;
    Py_XDECREF(tmp_class_creation_6__bases);
    tmp_class_creation_6__bases = NULL;
    Py_XDECREF(tmp_class_creation_6__class_decl_dict);
    tmp_class_creation_6__class_decl_dict = NULL;
    Py_XDECREF(tmp_class_creation_6__metaclass);
    tmp_class_creation_6__metaclass = NULL;
    Py_XDECREF(tmp_class_creation_6__prepared);
    tmp_class_creation_6__prepared = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_33;
    exception_value = exception_keeper_value_33;
    exception_tb = exception_keeper_tb_33;
    exception_lineno = exception_keeper_lineno_33;

    goto frame_exception_exit_1;
    // End of try:
    try_end_11:;
    CHECK_OBJECT(tmp_class_creation_6__bases_orig);
    Py_DECREF(tmp_class_creation_6__bases_orig);
    tmp_class_creation_6__bases_orig = NULL;
    CHECK_OBJECT(tmp_class_creation_6__bases);
    Py_DECREF(tmp_class_creation_6__bases);
    tmp_class_creation_6__bases = NULL;
    CHECK_OBJECT(tmp_class_creation_6__class_decl_dict);
    Py_DECREF(tmp_class_creation_6__class_decl_dict);
    tmp_class_creation_6__class_decl_dict = NULL;
    CHECK_OBJECT(tmp_class_creation_6__metaclass);
    Py_DECREF(tmp_class_creation_6__metaclass);
    tmp_class_creation_6__metaclass = NULL;
    CHECK_OBJECT(tmp_class_creation_6__prepared);
    Py_DECREF(tmp_class_creation_6__prepared);
    tmp_class_creation_6__prepared = NULL;
    {
        PyObject *tmp_assign_source_90;
        PyObject *tmp_tuple_arg_1;
        PyObject *tmp_called_value_54;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_expression_value_132;
        tmp_called_value_54 = LOOKUP_BUILTIN(mod_consts[112]);
        assert(tmp_called_value_54 != NULL);
        tmp_expression_value_132 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[14]);

        if (unlikely(tmp_expression_value_132 == NULL)) {
            tmp_expression_value_132 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[14]);
        }

        if (tmp_expression_value_132 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 395;

            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_132, mod_consts[113]);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 395;

            goto frame_exception_exit_1;
        }
        frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame.f_lineno = 395;
        tmp_tuple_arg_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_54, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_tuple_arg_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 395;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_90 = PySequence_Tuple(tmp_tuple_arg_1);
        Py_DECREF(tmp_tuple_arg_1);
        if (tmp_assign_source_90 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 395;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)mod_consts[114], tmp_assign_source_90);
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_e49d3c7b1b476ec58fa7db7e1a3c190b);
#endif
    popFrameStack();

    assertFrameObject(frame_e49d3c7b1b476ec58fa7db7e1a3c190b);

    goto frame_no_exception_12;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_e49d3c7b1b476ec58fa7db7e1a3c190b);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_e49d3c7b1b476ec58fa7db7e1a3c190b, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_e49d3c7b1b476ec58fa7db7e1a3c190b->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_e49d3c7b1b476ec58fa7db7e1a3c190b, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_12:;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("google.cloud.vision_v1.types.text_annotation", false);

    Py_INCREF(module_google$cloud$vision_v1$types$text_annotation);
    return module_google$cloud$vision_v1$types$text_annotation;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$text_annotation, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(module_name);
        }
    }
#endif
    PGO_onModuleExit("google$cloud$vision_v1$types$text_annotation", false);

    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}
