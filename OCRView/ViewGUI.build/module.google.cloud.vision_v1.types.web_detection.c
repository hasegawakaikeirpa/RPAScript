/* Generated code for Python module 'google.cloud.vision_v1.types.web_detection'
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

/* The "module_google$cloud$vision_v1$types$web_detection" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_google$cloud$vision_v1$types$web_detection;
PyDictObject *moduledict_google$cloud$vision_v1$types$web_detection;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[74];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[74];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("google.cloud.vision_v1.types.web_detection"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 74; i++) {
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
void checkModuleConstants_google$cloud$vision_v1$types$web_detection(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 74; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_a891ac0a5faafd098b6484b6abf7803b;
static PyCodeObject *codeobj_48704dc34b9b47c55848cd9834e21857;
static PyCodeObject *codeobj_37fd69bcc3b557d3c7ba929d03776cae;
static PyCodeObject *codeobj_399714034290bc720b8a12943283967a;
static PyCodeObject *codeobj_6f55b0b2050a5d5d71e3344b8f66d8af;
static PyCodeObject *codeobj_68b58394039f6e7254b4dd7a134349d9;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[70]); CHECK_OBJECT(module_filename_obj);
    codeobj_a891ac0a5faafd098b6484b6abf7803b = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[71], NULL, NULL, 0, 0, 0);
    codeobj_48704dc34b9b47c55848cd9834e21857 = MAKE_CODEOBJECT(module_filename_obj, 27, CO_NOFREE, mod_consts[15], mod_consts[72], NULL, 0, 0, 0);
    codeobj_37fd69bcc3b557d3c7ba929d03776cae = MAKE_CODEOBJECT(module_filename_obj, 54, CO_NOFREE, mod_consts[24], mod_consts[72], NULL, 0, 0, 0);
    codeobj_399714034290bc720b8a12943283967a = MAKE_CODEOBJECT(module_filename_obj, 82, CO_NOFREE, mod_consts[37], mod_consts[72], NULL, 0, 0, 0);
    codeobj_6f55b0b2050a5d5d71e3344b8f66d8af = MAKE_CODEOBJECT(module_filename_obj, 148, CO_NOFREE, mod_consts[51], mod_consts[72], NULL, 0, 0, 0);
    codeobj_68b58394039f6e7254b4dd7a134349d9 = MAKE_CODEOBJECT(module_filename_obj, 102, CO_NOFREE, mod_consts[41], mod_consts[72], NULL, 0, 0, 0);
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

function_impl_code functable_google$cloud$vision_v1$types$web_detection[] = {

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

    function_impl_code *current = functable_google$cloud$vision_v1$types$web_detection;
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

    if (offset > sizeof(functable_google$cloud$vision_v1$types$web_detection) || offset < 0) {
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
        functable_google$cloud$vision_v1$types$web_detection[offset],
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
        module_google$cloud$vision_v1$types$web_detection,
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
PyObject *modulecode_google$cloud$vision_v1$types$web_detection(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("google.cloud.vision_v1.types.web_detection");

    // Store the module for future use.
    module_google$cloud$vision_v1$types$web_detection = module;

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
        PRINT_STRING("google.cloud.vision_v1.types.web_detection: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
        patchInspectModule();
#endif

#endif

        /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("google.cloud.vision_v1.types.web_detection: Calling createModuleConstants().\n");
#endif
        createModuleConstants();

        /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("google.cloud.vision_v1.types.web_detection: Calling createModuleCodeObjects().\n");
#endif
        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initgoogle$cloud$vision_v1$types$web_detection\n");

    moduledict_google$cloud$vision_v1$types$web_detection = MODULE_DICT(module_google$cloud$vision_v1$types$web_detection);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(loader_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_google$cloud$vision_v1$types$web_detection,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_google$cloud$vision_v1$types$web_detection,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[73]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_google$cloud$vision_v1$types$web_detection,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_google$cloud$vision_v1$types$web_detection,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_google$cloud$vision_v1$types$web_detection,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_google$cloud$vision_v1$types$web_detection);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_google$cloud$vision_v1$types$web_detection);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    PyObject *outline_0_var___class__ = NULL;
    PyObject *outline_1_var___class__ = NULL;
    PyObject *outline_2_var___class__ = NULL;
    PyObject *outline_3_var___class__ = NULL;
    PyObject *outline_4_var___class__ = NULL;
    PyObject *tmp_WebDetection$class_creation_1__bases = NULL;
    PyObject *tmp_WebDetection$class_creation_1__bases_orig = NULL;
    PyObject *tmp_WebDetection$class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_WebDetection$class_creation_1__metaclass = NULL;
    PyObject *tmp_WebDetection$class_creation_1__prepared = NULL;
    PyObject *tmp_WebDetection$class_creation_2__bases = NULL;
    PyObject *tmp_WebDetection$class_creation_2__bases_orig = NULL;
    PyObject *tmp_WebDetection$class_creation_2__class_decl_dict = NULL;
    PyObject *tmp_WebDetection$class_creation_2__metaclass = NULL;
    PyObject *tmp_WebDetection$class_creation_2__prepared = NULL;
    PyObject *tmp_WebDetection$class_creation_3__bases = NULL;
    PyObject *tmp_WebDetection$class_creation_3__bases_orig = NULL;
    PyObject *tmp_WebDetection$class_creation_3__class_decl_dict = NULL;
    PyObject *tmp_WebDetection$class_creation_3__metaclass = NULL;
    PyObject *tmp_WebDetection$class_creation_3__prepared = NULL;
    PyObject *tmp_WebDetection$class_creation_4__bases = NULL;
    PyObject *tmp_WebDetection$class_creation_4__bases_orig = NULL;
    PyObject *tmp_WebDetection$class_creation_4__class_decl_dict = NULL;
    PyObject *tmp_WebDetection$class_creation_4__metaclass = NULL;
    PyObject *tmp_WebDetection$class_creation_4__prepared = NULL;
    PyObject *tmp_class_creation_1__bases = NULL;
    PyObject *tmp_class_creation_1__bases_orig = NULL;
    PyObject *tmp_class_creation_1__class_decl_dict = NULL;
    PyObject *tmp_class_creation_1__metaclass = NULL;
    PyObject *tmp_class_creation_1__prepared = NULL;
    struct Nuitka_FrameObject *frame_a891ac0a5faafd098b6484b6abf7803b;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    int tmp_res;
    PyObject *tmp_dictdel_dict;
    PyObject *tmp_dictdel_key;
    PyObject *locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27 = NULL;
    PyObject *tmp_dictset_value;
    struct Nuitka_FrameObject *frame_48704dc34b9b47c55848cd9834e21857_2;
    NUITKA_MAY_BE_UNUSED char const *type_description_2 = NULL;
    PyObject *locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54 = NULL;
    struct Nuitka_FrameObject *frame_37fd69bcc3b557d3c7ba929d03776cae_3;
    NUITKA_MAY_BE_UNUSED char const *type_description_3 = NULL;
    static struct Nuitka_FrameObject *cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3 = NULL;
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
    PyObject *locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82 = NULL;
    struct Nuitka_FrameObject *frame_399714034290bc720b8a12943283967a_4;
    NUITKA_MAY_BE_UNUSED char const *type_description_4 = NULL;
    static struct Nuitka_FrameObject *cache_frame_399714034290bc720b8a12943283967a_4 = NULL;
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
    PyObject *locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102 = NULL;
    struct Nuitka_FrameObject *frame_68b58394039f6e7254b4dd7a134349d9_5;
    NUITKA_MAY_BE_UNUSED char const *type_description_5 = NULL;
    static struct Nuitka_FrameObject *cache_frame_68b58394039f6e7254b4dd7a134349d9_5 = NULL;
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
    PyObject *locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148 = NULL;
    struct Nuitka_FrameObject *frame_6f55b0b2050a5d5d71e3344b8f66d8af_6;
    NUITKA_MAY_BE_UNUSED char const *type_description_6 = NULL;
    static struct Nuitka_FrameObject *cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 = NULL;
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
    static struct Nuitka_FrameObject *cache_frame_48704dc34b9b47c55848cd9834e21857_2 = NULL;
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

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[0], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[1], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_a891ac0a5faafd098b6484b6abf7803b = MAKE_MODULE_FRAME(codeobj_a891ac0a5faafd098b6484b6abf7803b, module_google$cloud$vision_v1$types$web_detection);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_a891ac0a5faafd098b6484b6abf7803b);
    assert(Py_REFCNT(frame_a891ac0a5faafd098b6484b6abf7803b) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[2]);

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
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[2]);

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
        UPDATE_STRING_DICT0(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[6];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_google$cloud$vision_v1$types$web_detection;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = Py_None;
        tmp_level_value_1 = mod_consts[7];
        frame_a891ac0a5faafd098b6484b6abf7803b->m_frame.f_lineno = 16;
        tmp_assign_source_4 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_args_kwsplit_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        assert(!(tmp_expression_value_1 == NULL));
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[8]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 19;

            goto frame_exception_exit_1;
        }
        tmp_call_args_kwsplit_1 = DEEP_COPY_TUPLE(mod_consts[9]);
        frame_a891ac0a5faafd098b6484b6abf7803b->m_frame.f_lineno = 19;
        tmp_assign_source_5 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_1, &PyTuple_GET_ITEM(tmp_call_args_kwsplit_1, 0), mod_consts[10]);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_call_args_kwsplit_1);
        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 19;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[11], tmp_assign_source_5);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_expression_value_2;
        tmp_expression_value_2 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

        if (unlikely(tmp_expression_value_2 == NULL)) {
            tmp_expression_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
        }

        if (tmp_expression_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        tmp_tuple_element_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_2, mod_consts[12]);
        if (tmp_tuple_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        tmp_assign_source_6 = PyTuple_New(1);
        PyTuple_SET_ITEM(tmp_assign_source_6, 0, tmp_tuple_element_1);
        assert(tmp_class_creation_1__bases_orig == NULL);
        tmp_class_creation_1__bases_orig = tmp_assign_source_6;
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_dircall_arg1_1;
        CHECK_OBJECT(tmp_class_creation_1__bases_orig);
        tmp_dircall_arg1_1 = tmp_class_creation_1__bases_orig;
        Py_INCREF(tmp_dircall_arg1_1);

        {
            PyObject *dir_call_args[] = {tmp_dircall_arg1_1};
            tmp_assign_source_7 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
        }
        if (tmp_assign_source_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__bases == NULL);
        tmp_class_creation_1__bases = tmp_assign_source_7;
    }
    {
        PyObject *tmp_assign_source_8;
        tmp_assign_source_8 = PyDict_New();
        assert(tmp_class_creation_1__class_decl_dict == NULL);
        tmp_class_creation_1__class_decl_dict = tmp_assign_source_8;
    }
    {
        PyObject *tmp_assign_source_9;
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
        tmp_key_value_1 = mod_consts[13];
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
        tmp_key_value_2 = mod_consts[13];
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


            exception_lineno = 27;

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


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        tmp_metaclass_value_1 = BUILTIN_TYPE1(tmp_type_arg_1);
        Py_DECREF(tmp_type_arg_1);
        if (tmp_metaclass_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

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
        tmp_assign_source_9 = SELECT_METACLASS(tmp_metaclass_value_1, tmp_bases_value_1);
        Py_DECREF(tmp_metaclass_value_1);
        if (tmp_assign_source_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__metaclass == NULL);
        tmp_class_creation_1__metaclass = tmp_assign_source_9;
    }
    {
        bool tmp_condition_result_3;
        PyObject *tmp_key_value_3;
        PyObject *tmp_dict_arg_value_3;
        tmp_key_value_3 = mod_consts[13];
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
    tmp_dictdel_key = mod_consts[13];
    tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
    if (tmp_result == false) {
        assert(ERROR_OCCURRED());

        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


        exception_lineno = 27;

        goto try_except_handler_1;
    }
    branch_no_1:;
    {
        nuitka_bool tmp_condition_result_4;
        PyObject *tmp_expression_value_4;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_4 = tmp_class_creation_1__metaclass;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_4, mod_consts[14]);
        tmp_condition_result_4 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_4 == NUITKA_BOOL_TRUE) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_called_value_2;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_kwargs_value_1;
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_expression_value_5 = tmp_class_creation_1__metaclass;
        tmp_called_value_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_5, mod_consts[14]);
        if (tmp_called_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        tmp_tuple_element_2 = mod_consts[15];
        tmp_args_value_1 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_1, 0, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__bases);
        tmp_tuple_element_2 = tmp_class_creation_1__bases;
        PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_2);
        CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
        tmp_kwargs_value_1 = tmp_class_creation_1__class_decl_dict;
        frame_a891ac0a5faafd098b6484b6abf7803b->m_frame.f_lineno = 27;
        tmp_assign_source_10 = CALL_FUNCTION(tmp_called_value_2, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_called_value_2);
        Py_DECREF(tmp_args_value_1);
        if (tmp_assign_source_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_10;
    }
    {
        bool tmp_condition_result_5;
        PyObject *tmp_operand_value_1;
        PyObject *tmp_expression_value_6;
        CHECK_OBJECT(tmp_class_creation_1__prepared);
        tmp_expression_value_6 = tmp_class_creation_1__prepared;
        tmp_result = HAS_ATTR_BOOL(tmp_expression_value_6, mod_consts[16]);
        tmp_operand_value_1 = (tmp_result) ? Py_True : Py_False;
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

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
        tmp_mod_expr_left_1 = mod_consts[17];
        CHECK_OBJECT(tmp_class_creation_1__metaclass);
        tmp_getattr_target_1 = tmp_class_creation_1__metaclass;
        tmp_getattr_attr_1 = mod_consts[18];
        tmp_getattr_default_1 = mod_consts[19];
        tmp_tuple_element_3 = BUILTIN_GETATTR(tmp_getattr_target_1, tmp_getattr_attr_1, tmp_getattr_default_1);
        if (tmp_tuple_element_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

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
            tmp_tuple_element_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_7, mod_consts[18]);
            Py_DECREF(tmp_expression_value_7);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 27;

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


            exception_lineno = 27;

            goto try_except_handler_1;
        }
        exception_type = tmp_raise_type_1;
        Py_INCREF(tmp_raise_type_1);
        exception_value = tmp_raise_value_1;
        exception_lineno = 27;
        RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);

        goto try_except_handler_1;
    }
    branch_no_3:;
    goto branch_end_2;
    branch_no_2:;
    {
        PyObject *tmp_assign_source_11;
        tmp_assign_source_11 = PyDict_New();
        assert(tmp_class_creation_1__prepared == NULL);
        tmp_class_creation_1__prepared = tmp_assign_source_11;
    }
    branch_end_2:;
    {
        PyObject *tmp_assign_source_12;
        {
            PyObject *tmp_set_locals_1;
            CHECK_OBJECT(tmp_class_creation_1__prepared);
            tmp_set_locals_1 = tmp_class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27 = tmp_set_locals_1;
            Py_INCREF(tmp_set_locals_1);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[20];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[21], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_3;
        }
        tmp_dictset_value = mod_consts[22];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_3;
        }
        tmp_dictset_value = mod_consts[15];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[23], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_3;
        }
        if (isFrameUnusable(cache_frame_48704dc34b9b47c55848cd9834e21857_2)) {
            Py_XDECREF(cache_frame_48704dc34b9b47c55848cd9834e21857_2);

#if _DEBUG_REFCOUNTS
            if (cache_frame_48704dc34b9b47c55848cd9834e21857_2 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_48704dc34b9b47c55848cd9834e21857_2 = MAKE_FUNCTION_FRAME(codeobj_48704dc34b9b47c55848cd9834e21857, module_google$cloud$vision_v1$types$web_detection, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_48704dc34b9b47c55848cd9834e21857_2->m_type_description == NULL);
        frame_48704dc34b9b47c55848cd9834e21857_2 = cache_frame_48704dc34b9b47c55848cd9834e21857_2;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_48704dc34b9b47c55848cd9834e21857_2);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_48704dc34b9b47c55848cd9834e21857_2) == 2); // Frame stack

        // Framed code:
        // Tried code:
        {
            PyObject *tmp_assign_source_13;
            PyObject *tmp_tuple_element_4;
            PyObject *tmp_expression_value_8;
            tmp_expression_value_8 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_8 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_8 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_8 == NULL)) {
                        tmp_expression_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_8 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 54;
                        type_description_2 = "o";
                        goto try_except_handler_4;
                    }
                    Py_INCREF(tmp_expression_value_8);
                } else {
                    goto try_except_handler_4;
                }
            }

            tmp_tuple_element_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_8, mod_consts[12]);
            Py_DECREF(tmp_expression_value_8);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_assign_source_13 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_13, 0, tmp_tuple_element_4);
            assert(tmp_WebDetection$class_creation_1__bases_orig == NULL);
            tmp_WebDetection$class_creation_1__bases_orig = tmp_assign_source_13;
        }
        {
            PyObject *tmp_assign_source_14;
            PyObject *tmp_dircall_arg1_2;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases_orig);
            tmp_dircall_arg1_2 = tmp_WebDetection$class_creation_1__bases_orig;
            Py_INCREF(tmp_dircall_arg1_2);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_2};
                tmp_assign_source_14 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_WebDetection$class_creation_1__bases == NULL);
            tmp_WebDetection$class_creation_1__bases = tmp_assign_source_14;
        }
        {
            PyObject *tmp_assign_source_15;
            tmp_assign_source_15 = PyDict_New();
            assert(tmp_WebDetection$class_creation_1__class_decl_dict == NULL);
            tmp_WebDetection$class_creation_1__class_decl_dict = tmp_assign_source_15;
        }
        {
            PyObject *tmp_assign_source_16;
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
            tmp_key_value_4 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_4 = tmp_WebDetection$class_creation_1__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_4, tmp_key_value_4);
            assert(!(tmp_res == -1));
            tmp_condition_result_6 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_6 != false) {
                goto condexpr_true_3;
            } else {
                goto condexpr_false_3;
            }
            condexpr_true_3:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_5 = tmp_WebDetection$class_creation_1__class_decl_dict;
            tmp_key_value_5 = mod_consts[13];
            tmp_metaclass_value_2 = DICT_GET_ITEM0(tmp_dict_arg_value_5, tmp_key_value_5);
            if (tmp_metaclass_value_2 == NULL) {
                tmp_metaclass_value_2 = Py_None;
            }
            assert(!(tmp_metaclass_value_2 == NULL));
            Py_INCREF(tmp_metaclass_value_2);
            goto condexpr_end_3;
            condexpr_false_3:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_truth_name_2 = CHECK_IF_TRUE(tmp_WebDetection$class_creation_1__bases);
            if (tmp_truth_name_2 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
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
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_expression_value_9 = tmp_WebDetection$class_creation_1__bases;
            tmp_subscript_value_2 = mod_consts[7];
            tmp_type_arg_3 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_9, tmp_subscript_value_2, 0);
            if (tmp_type_arg_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_metaclass_value_2 = BUILTIN_TYPE1(tmp_type_arg_3);
            Py_DECREF(tmp_type_arg_3);
            if (tmp_metaclass_value_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            goto condexpr_end_4;
            condexpr_false_4:;
            tmp_metaclass_value_2 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_2);
            condexpr_end_4:;
            condexpr_end_3:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_bases_value_2 = tmp_WebDetection$class_creation_1__bases;
            tmp_assign_source_16 = SELECT_METACLASS(tmp_metaclass_value_2, tmp_bases_value_2);
            Py_DECREF(tmp_metaclass_value_2);
            if (tmp_assign_source_16 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_WebDetection$class_creation_1__metaclass == NULL);
            tmp_WebDetection$class_creation_1__metaclass = tmp_assign_source_16;
        }
        {
            bool tmp_condition_result_8;
            PyObject *tmp_key_value_6;
            PyObject *tmp_dict_arg_value_6;
            tmp_key_value_6 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
            tmp_dict_arg_value_6 = tmp_WebDetection$class_creation_1__class_decl_dict;
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
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
        tmp_dictdel_dict = tmp_WebDetection$class_creation_1__class_decl_dict;
        tmp_dictdel_key = mod_consts[13];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_2 = "o";
            goto try_except_handler_4;
        }
        branch_no_4:;
        {
            nuitka_bool tmp_condition_result_9;
            PyObject *tmp_expression_value_10;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__metaclass);
            tmp_expression_value_10 = tmp_WebDetection$class_creation_1__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_10, mod_consts[14]);
            tmp_condition_result_9 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_9 == NUITKA_BOOL_TRUE) {
                goto branch_yes_5;
            } else {
                goto branch_no_5;
            }
        }
        branch_yes_5:;
        {
            PyObject *tmp_assign_source_17;
            PyObject *tmp_called_value_3;
            PyObject *tmp_expression_value_11;
            PyObject *tmp_args_value_2;
            PyObject *tmp_tuple_element_5;
            PyObject *tmp_kwargs_value_2;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__metaclass);
            tmp_expression_value_11 = tmp_WebDetection$class_creation_1__metaclass;
            tmp_called_value_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_11, mod_consts[14]);
            if (tmp_called_value_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_tuple_element_5 = mod_consts[24];
            tmp_args_value_2 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_2, 0, tmp_tuple_element_5);
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_tuple_element_5 = tmp_WebDetection$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_2, 1, tmp_tuple_element_5);
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
            tmp_kwargs_value_2 = tmp_WebDetection$class_creation_1__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 54;
            tmp_assign_source_17 = CALL_FUNCTION(tmp_called_value_3, tmp_args_value_2, tmp_kwargs_value_2);
            Py_DECREF(tmp_called_value_3);
            Py_DECREF(tmp_args_value_2);
            if (tmp_assign_source_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            assert(tmp_WebDetection$class_creation_1__prepared == NULL);
            tmp_WebDetection$class_creation_1__prepared = tmp_assign_source_17;
        }
        {
            bool tmp_condition_result_10;
            PyObject *tmp_operand_value_2;
            PyObject *tmp_expression_value_12;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__prepared);
            tmp_expression_value_12 = tmp_WebDetection$class_creation_1__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_12, mod_consts[16]);
            tmp_operand_value_2 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_2);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
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
            tmp_mod_expr_left_2 = mod_consts[17];
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__metaclass);
            tmp_getattr_target_2 = tmp_WebDetection$class_creation_1__metaclass;
            tmp_getattr_attr_2 = mod_consts[18];
            tmp_getattr_default_2 = mod_consts[19];
            tmp_tuple_element_6 = BUILTIN_GETATTR(tmp_getattr_target_2, tmp_getattr_attr_2, tmp_getattr_default_2);
            if (tmp_tuple_element_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            tmp_mod_expr_right_2 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_13;
                PyObject *tmp_type_arg_4;
                PyTuple_SET_ITEM(tmp_mod_expr_right_2, 0, tmp_tuple_element_6);
                CHECK_OBJECT(tmp_WebDetection$class_creation_1__prepared);
                tmp_type_arg_4 = tmp_WebDetection$class_creation_1__prepared;
                tmp_expression_value_13 = BUILTIN_TYPE1(tmp_type_arg_4);
                assert(!(tmp_expression_value_13 == NULL));
                tmp_tuple_element_6 = LOOKUP_ATTRIBUTE(tmp_expression_value_13, mod_consts[18]);
                Py_DECREF(tmp_expression_value_13);
                if (tmp_tuple_element_6 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 54;
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


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_4;
            }
            exception_type = tmp_raise_type_2;
            Py_INCREF(tmp_raise_type_2);
            exception_value = tmp_raise_value_2;
            exception_lineno = 54;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_4;
        }
        branch_no_6:;
        goto branch_end_5;
        branch_no_5:;
        {
            PyObject *tmp_assign_source_18;
            tmp_assign_source_18 = PyDict_New();
            assert(tmp_WebDetection$class_creation_1__prepared == NULL);
            tmp_WebDetection$class_creation_1__prepared = tmp_assign_source_18;
        }
        branch_end_5:;
        {
            PyObject *tmp_set_locals_2;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__prepared);
            tmp_set_locals_2 = tmp_WebDetection$class_creation_1__prepared;
            locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54 = tmp_set_locals_2;
            Py_INCREF(tmp_set_locals_2);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[20];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[21], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        tmp_dictset_value = mod_consts[25];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        tmp_dictset_value = mod_consts[26];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[23], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        if (isFrameUnusable(cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3)) {
            Py_XDECREF(cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3);

#if _DEBUG_REFCOUNTS
            if (cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3 = MAKE_FUNCTION_FRAME(codeobj_37fd69bcc3b557d3c7ba929d03776cae, module_google$cloud$vision_v1$types$web_detection, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3->m_type_description == NULL);
        frame_37fd69bcc3b557d3c7ba929d03776cae_3 = cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_37fd69bcc3b557d3c7ba929d03776cae_3);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_37fd69bcc3b557d3c7ba929d03776cae_3) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_4;
            PyObject *tmp_expression_value_14;
            PyObject *tmp_args_value_3;
            PyObject *tmp_tuple_element_7;
            PyObject *tmp_expression_value_15;
            PyObject *tmp_kwargs_value_3;
            tmp_expression_value_14 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_14 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_14 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_14 == NULL)) {
                        tmp_expression_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_14 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 69;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_14);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_called_value_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_14, mod_consts[27]);
            Py_DECREF(tmp_expression_value_14);
            if (tmp_called_value_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_expression_value_15 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_15 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_15 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_15 == NULL)) {
                        tmp_expression_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_15 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_4);

                        exception_lineno = 70;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_15);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_tuple_element_7 = LOOKUP_ATTRIBUTE(tmp_expression_value_15, mod_consts[28]);
            Py_DECREF(tmp_expression_value_15);
            if (tmp_tuple_element_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_4);

                exception_lineno = 70;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_args_value_3 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_3, 0, tmp_tuple_element_7);
            tmp_kwargs_value_3 = PyDict_Copy(mod_consts[29]);
            frame_37fd69bcc3b557d3c7ba929d03776cae_3->m_frame.f_lineno = 69;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_4, tmp_args_value_3, tmp_kwargs_value_3);
            Py_DECREF(tmp_called_value_4);
            Py_DECREF(tmp_args_value_3);
            Py_DECREF(tmp_kwargs_value_3);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[30], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 69;
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
            tmp_expression_value_16 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_16 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_16 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_16 == NULL)) {
                        tmp_expression_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_16 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 73;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_16);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_called_value_5 = LOOKUP_ATTRIBUTE(tmp_expression_value_16, mod_consts[27]);
            Py_DECREF(tmp_expression_value_16);
            if (tmp_called_value_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_expression_value_17 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_17 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_17 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_17 == NULL)) {
                        tmp_expression_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_17 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_5);

                        exception_lineno = 74;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_17);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_tuple_element_8 = LOOKUP_ATTRIBUTE(tmp_expression_value_17, mod_consts[31]);
            Py_DECREF(tmp_expression_value_17);
            if (tmp_tuple_element_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_5);

                exception_lineno = 74;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_args_value_4 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_4, 0, tmp_tuple_element_8);
            tmp_kwargs_value_4 = PyDict_Copy(mod_consts[32]);
            frame_37fd69bcc3b557d3c7ba929d03776cae_3->m_frame.f_lineno = 73;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_5, tmp_args_value_4, tmp_kwargs_value_4);
            Py_DECREF(tmp_called_value_5);
            Py_DECREF(tmp_args_value_4);
            Py_DECREF(tmp_kwargs_value_4);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[33], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 73;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
        }
        {
            PyObject *tmp_called_value_6;
            PyObject *tmp_expression_value_18;
            PyObject *tmp_args_value_5;
            PyObject *tmp_tuple_element_9;
            PyObject *tmp_expression_value_19;
            PyObject *tmp_kwargs_value_5;
            tmp_expression_value_18 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_18 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_18 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_18 == NULL)) {
                        tmp_expression_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_18 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 77;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_18);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_called_value_6 = LOOKUP_ATTRIBUTE(tmp_expression_value_18, mod_consts[27]);
            Py_DECREF(tmp_expression_value_18);
            if (tmp_called_value_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_expression_value_19 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[6]);

            if (tmp_expression_value_19 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_19 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_19 == NULL)) {
                        tmp_expression_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_19 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_6);

                        exception_lineno = 78;
                        type_description_3 = "o";
                        goto frame_exception_exit_3;
                    }
                    Py_INCREF(tmp_expression_value_19);
                } else {
                    goto frame_exception_exit_3;
                }
            }

            tmp_tuple_element_9 = LOOKUP_ATTRIBUTE(tmp_expression_value_19, mod_consts[28]);
            Py_DECREF(tmp_expression_value_19);
            if (tmp_tuple_element_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_6);

                exception_lineno = 78;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_args_value_5 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_5, 0, tmp_tuple_element_9);
            tmp_kwargs_value_5 = PyDict_Copy(mod_consts[34]);
            frame_37fd69bcc3b557d3c7ba929d03776cae_3->m_frame.f_lineno = 77;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_6, tmp_args_value_5, tmp_kwargs_value_5);
            Py_DECREF(tmp_called_value_6);
            Py_DECREF(tmp_args_value_5);
            Py_DECREF(tmp_kwargs_value_5);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[35], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 77;
                type_description_3 = "o";
                goto frame_exception_exit_3;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_37fd69bcc3b557d3c7ba929d03776cae_3);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_1;

        frame_exception_exit_3:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_37fd69bcc3b557d3c7ba929d03776cae_3);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_37fd69bcc3b557d3c7ba929d03776cae_3, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_37fd69bcc3b557d3c7ba929d03776cae_3->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_37fd69bcc3b557d3c7ba929d03776cae_3, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_37fd69bcc3b557d3c7ba929d03776cae_3,
            type_description_3,
            outline_1_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_37fd69bcc3b557d3c7ba929d03776cae_3 == cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3);
            cache_frame_37fd69bcc3b557d3c7ba929d03776cae_3 = NULL;
        }

        assertFrameObject(frame_37fd69bcc3b557d3c7ba929d03776cae_3);

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
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_cmp_expr_left_1 = tmp_WebDetection$class_creation_1__bases;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases_orig);
            tmp_cmp_expr_right_1 = tmp_WebDetection$class_creation_1__bases_orig;
            tmp_condition_result_11 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
            if (tmp_condition_result_11 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
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
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases_orig);
        tmp_dictset_value = tmp_WebDetection$class_creation_1__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54, mod_consts[36], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
            type_description_2 = "o";
            goto try_except_handler_6;
        }
        branch_no_7:;
        {
            PyObject *tmp_assign_source_19;
            PyObject *tmp_called_value_7;
            PyObject *tmp_args_value_6;
            PyObject *tmp_tuple_element_10;
            PyObject *tmp_kwargs_value_6;
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__metaclass);
            tmp_called_value_7 = tmp_WebDetection$class_creation_1__metaclass;
            tmp_tuple_element_10 = mod_consts[24];
            tmp_args_value_6 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_6, 0, tmp_tuple_element_10);
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
            tmp_tuple_element_10 = tmp_WebDetection$class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_6, 1, tmp_tuple_element_10);
            tmp_tuple_element_10 = locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54;
            PyTuple_SET_ITEM0(tmp_args_value_6, 2, tmp_tuple_element_10);
            CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
            tmp_kwargs_value_6 = tmp_WebDetection$class_creation_1__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 54;
            tmp_assign_source_19 = CALL_FUNCTION(tmp_called_value_7, tmp_args_value_6, tmp_kwargs_value_6);
            Py_DECREF(tmp_args_value_6);
            if (tmp_assign_source_19 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 54;
                type_description_2 = "o";
                goto try_except_handler_6;
            }
            assert(outline_1_var___class__ == NULL);
            outline_1_var___class__ = tmp_assign_source_19;
        }
        CHECK_OBJECT(outline_1_var___class__);
        tmp_dictset_value = outline_1_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_6;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_6:;
        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54);
        locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54 = NULL;
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

        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54);
        locals_google$cloud$vision_v1$types$web_detection$$$class__2_WebEntity_54 = NULL;
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
        exception_lineno = 54;
        goto try_except_handler_4;
        outline_result_2:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[24], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 54;
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

        Py_XDECREF(tmp_WebDetection$class_creation_1__bases_orig);
        tmp_WebDetection$class_creation_1__bases_orig = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_1__bases);
        tmp_WebDetection$class_creation_1__bases = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_1__class_decl_dict);
        tmp_WebDetection$class_creation_1__class_decl_dict = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_1__metaclass);
        tmp_WebDetection$class_creation_1__metaclass = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_1__prepared);
        tmp_WebDetection$class_creation_1__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_3;
        exception_value = exception_keeper_value_3;
        exception_tb = exception_keeper_tb_3;
        exception_lineno = exception_keeper_lineno_3;

        goto frame_exception_exit_2;
        // End of try:
        try_end_1:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases_orig);
        Py_DECREF(tmp_WebDetection$class_creation_1__bases_orig);
        tmp_WebDetection$class_creation_1__bases_orig = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__bases);
        Py_DECREF(tmp_WebDetection$class_creation_1__bases);
        tmp_WebDetection$class_creation_1__bases = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__class_decl_dict);
        Py_DECREF(tmp_WebDetection$class_creation_1__class_decl_dict);
        tmp_WebDetection$class_creation_1__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__metaclass);
        Py_DECREF(tmp_WebDetection$class_creation_1__metaclass);
        tmp_WebDetection$class_creation_1__metaclass = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_1__prepared);
        Py_DECREF(tmp_WebDetection$class_creation_1__prepared);
        tmp_WebDetection$class_creation_1__prepared = NULL;
        // Tried code:
        {
            PyObject *tmp_assign_source_20;
            PyObject *tmp_tuple_element_11;
            PyObject *tmp_expression_value_20;
            tmp_expression_value_20 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_20 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_20 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_20 == NULL)) {
                        tmp_expression_value_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_20 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 82;
                        type_description_2 = "o";
                        goto try_except_handler_7;
                    }
                    Py_INCREF(tmp_expression_value_20);
                } else {
                    goto try_except_handler_7;
                }
            }

            tmp_tuple_element_11 = LOOKUP_ATTRIBUTE(tmp_expression_value_20, mod_consts[12]);
            Py_DECREF(tmp_expression_value_20);
            if (tmp_tuple_element_11 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_assign_source_20 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_20, 0, tmp_tuple_element_11);
            assert(tmp_WebDetection$class_creation_2__bases_orig == NULL);
            tmp_WebDetection$class_creation_2__bases_orig = tmp_assign_source_20;
        }
        {
            PyObject *tmp_assign_source_21;
            PyObject *tmp_dircall_arg1_3;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases_orig);
            tmp_dircall_arg1_3 = tmp_WebDetection$class_creation_2__bases_orig;
            Py_INCREF(tmp_dircall_arg1_3);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_3};
                tmp_assign_source_21 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_WebDetection$class_creation_2__bases == NULL);
            tmp_WebDetection$class_creation_2__bases = tmp_assign_source_21;
        }
        {
            PyObject *tmp_assign_source_22;
            tmp_assign_source_22 = PyDict_New();
            assert(tmp_WebDetection$class_creation_2__class_decl_dict == NULL);
            tmp_WebDetection$class_creation_2__class_decl_dict = tmp_assign_source_22;
        }
        {
            PyObject *tmp_assign_source_23;
            PyObject *tmp_metaclass_value_3;
            bool tmp_condition_result_12;
            PyObject *tmp_key_value_7;
            PyObject *tmp_dict_arg_value_7;
            PyObject *tmp_dict_arg_value_8;
            PyObject *tmp_key_value_8;
            nuitka_bool tmp_condition_result_13;
            int tmp_truth_name_3;
            PyObject *tmp_type_arg_5;
            PyObject *tmp_expression_value_21;
            PyObject *tmp_subscript_value_3;
            PyObject *tmp_bases_value_3;
            tmp_key_value_7 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_7 = tmp_WebDetection$class_creation_2__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_7, tmp_key_value_7);
            assert(!(tmp_res == -1));
            tmp_condition_result_12 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_12 != false) {
                goto condexpr_true_5;
            } else {
                goto condexpr_false_5;
            }
            condexpr_true_5:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_8 = tmp_WebDetection$class_creation_2__class_decl_dict;
            tmp_key_value_8 = mod_consts[13];
            tmp_metaclass_value_3 = DICT_GET_ITEM0(tmp_dict_arg_value_8, tmp_key_value_8);
            if (tmp_metaclass_value_3 == NULL) {
                tmp_metaclass_value_3 = Py_None;
            }
            assert(!(tmp_metaclass_value_3 == NULL));
            Py_INCREF(tmp_metaclass_value_3);
            goto condexpr_end_5;
            condexpr_false_5:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_truth_name_3 = CHECK_IF_TRUE(tmp_WebDetection$class_creation_2__bases);
            if (tmp_truth_name_3 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
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
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_expression_value_21 = tmp_WebDetection$class_creation_2__bases;
            tmp_subscript_value_3 = mod_consts[7];
            tmp_type_arg_5 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_21, tmp_subscript_value_3, 0);
            if (tmp_type_arg_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_metaclass_value_3 = BUILTIN_TYPE1(tmp_type_arg_5);
            Py_DECREF(tmp_type_arg_5);
            if (tmp_metaclass_value_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            goto condexpr_end_6;
            condexpr_false_6:;
            tmp_metaclass_value_3 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_3);
            condexpr_end_6:;
            condexpr_end_5:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_bases_value_3 = tmp_WebDetection$class_creation_2__bases;
            tmp_assign_source_23 = SELECT_METACLASS(tmp_metaclass_value_3, tmp_bases_value_3);
            Py_DECREF(tmp_metaclass_value_3);
            if (tmp_assign_source_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_WebDetection$class_creation_2__metaclass == NULL);
            tmp_WebDetection$class_creation_2__metaclass = tmp_assign_source_23;
        }
        {
            bool tmp_condition_result_14;
            PyObject *tmp_key_value_9;
            PyObject *tmp_dict_arg_value_9;
            tmp_key_value_9 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
            tmp_dict_arg_value_9 = tmp_WebDetection$class_creation_2__class_decl_dict;
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
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
        tmp_dictdel_dict = tmp_WebDetection$class_creation_2__class_decl_dict;
        tmp_dictdel_key = mod_consts[13];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        branch_no_8:;
        {
            nuitka_bool tmp_condition_result_15;
            PyObject *tmp_expression_value_22;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__metaclass);
            tmp_expression_value_22 = tmp_WebDetection$class_creation_2__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_22, mod_consts[14]);
            tmp_condition_result_15 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_15 == NUITKA_BOOL_TRUE) {
                goto branch_yes_9;
            } else {
                goto branch_no_9;
            }
        }
        branch_yes_9:;
        {
            PyObject *tmp_assign_source_24;
            PyObject *tmp_called_value_8;
            PyObject *tmp_expression_value_23;
            PyObject *tmp_args_value_7;
            PyObject *tmp_tuple_element_12;
            PyObject *tmp_kwargs_value_7;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__metaclass);
            tmp_expression_value_23 = tmp_WebDetection$class_creation_2__metaclass;
            tmp_called_value_8 = LOOKUP_ATTRIBUTE(tmp_expression_value_23, mod_consts[14]);
            if (tmp_called_value_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_tuple_element_12 = mod_consts[37];
            tmp_args_value_7 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_7, 0, tmp_tuple_element_12);
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_tuple_element_12 = tmp_WebDetection$class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_7, 1, tmp_tuple_element_12);
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
            tmp_kwargs_value_7 = tmp_WebDetection$class_creation_2__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 82;
            tmp_assign_source_24 = CALL_FUNCTION(tmp_called_value_8, tmp_args_value_7, tmp_kwargs_value_7);
            Py_DECREF(tmp_called_value_8);
            Py_DECREF(tmp_args_value_7);
            if (tmp_assign_source_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            assert(tmp_WebDetection$class_creation_2__prepared == NULL);
            tmp_WebDetection$class_creation_2__prepared = tmp_assign_source_24;
        }
        {
            bool tmp_condition_result_16;
            PyObject *tmp_operand_value_3;
            PyObject *tmp_expression_value_24;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__prepared);
            tmp_expression_value_24 = tmp_WebDetection$class_creation_2__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_24, mod_consts[16]);
            tmp_operand_value_3 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_3);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
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
            PyObject *tmp_tuple_element_13;
            PyObject *tmp_getattr_target_3;
            PyObject *tmp_getattr_attr_3;
            PyObject *tmp_getattr_default_3;
            tmp_raise_type_3 = PyExc_TypeError;
            tmp_mod_expr_left_3 = mod_consts[17];
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__metaclass);
            tmp_getattr_target_3 = tmp_WebDetection$class_creation_2__metaclass;
            tmp_getattr_attr_3 = mod_consts[18];
            tmp_getattr_default_3 = mod_consts[19];
            tmp_tuple_element_13 = BUILTIN_GETATTR(tmp_getattr_target_3, tmp_getattr_attr_3, tmp_getattr_default_3);
            if (tmp_tuple_element_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            tmp_mod_expr_right_3 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_25;
                PyObject *tmp_type_arg_6;
                PyTuple_SET_ITEM(tmp_mod_expr_right_3, 0, tmp_tuple_element_13);
                CHECK_OBJECT(tmp_WebDetection$class_creation_2__prepared);
                tmp_type_arg_6 = tmp_WebDetection$class_creation_2__prepared;
                tmp_expression_value_25 = BUILTIN_TYPE1(tmp_type_arg_6);
                assert(!(tmp_expression_value_25 == NULL));
                tmp_tuple_element_13 = LOOKUP_ATTRIBUTE(tmp_expression_value_25, mod_consts[18]);
                Py_DECREF(tmp_expression_value_25);
                if (tmp_tuple_element_13 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 82;
                    type_description_2 = "o";
                    goto tuple_build_exception_3;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_3, 1, tmp_tuple_element_13);
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


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_7;
            }
            exception_type = tmp_raise_type_3;
            Py_INCREF(tmp_raise_type_3);
            exception_value = tmp_raise_value_3;
            exception_lineno = 82;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        branch_no_10:;
        goto branch_end_9;
        branch_no_9:;
        {
            PyObject *tmp_assign_source_25;
            tmp_assign_source_25 = PyDict_New();
            assert(tmp_WebDetection$class_creation_2__prepared == NULL);
            tmp_WebDetection$class_creation_2__prepared = tmp_assign_source_25;
        }
        branch_end_9:;
        {
            PyObject *tmp_set_locals_3;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__prepared);
            tmp_set_locals_3 = tmp_WebDetection$class_creation_2__prepared;
            locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82 = tmp_set_locals_3;
            Py_INCREF(tmp_set_locals_3);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[20];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[21], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        tmp_dictset_value = mod_consts[38];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        tmp_dictset_value = mod_consts[39];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[23], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        if (isFrameUnusable(cache_frame_399714034290bc720b8a12943283967a_4)) {
            Py_XDECREF(cache_frame_399714034290bc720b8a12943283967a_4);

#if _DEBUG_REFCOUNTS
            if (cache_frame_399714034290bc720b8a12943283967a_4 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_399714034290bc720b8a12943283967a_4 = MAKE_FUNCTION_FRAME(codeobj_399714034290bc720b8a12943283967a, module_google$cloud$vision_v1$types$web_detection, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_399714034290bc720b8a12943283967a_4->m_type_description == NULL);
        frame_399714034290bc720b8a12943283967a_4 = cache_frame_399714034290bc720b8a12943283967a_4;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_399714034290bc720b8a12943283967a_4);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_399714034290bc720b8a12943283967a_4) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_9;
            PyObject *tmp_expression_value_26;
            PyObject *tmp_args_value_8;
            PyObject *tmp_tuple_element_14;
            PyObject *tmp_expression_value_27;
            PyObject *tmp_kwargs_value_8;
            tmp_expression_value_26 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[6]);

            if (tmp_expression_value_26 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_26 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_26 == NULL)) {
                        tmp_expression_value_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_26 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 93;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_26);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_called_value_9 = LOOKUP_ATTRIBUTE(tmp_expression_value_26, mod_consts[27]);
            Py_DECREF(tmp_expression_value_26);
            if (tmp_called_value_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 93;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_expression_value_27 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[6]);

            if (tmp_expression_value_27 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_27 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_27 == NULL)) {
                        tmp_expression_value_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_27 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_9);

                        exception_lineno = 94;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_27);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_tuple_element_14 = LOOKUP_ATTRIBUTE(tmp_expression_value_27, mod_consts[28]);
            Py_DECREF(tmp_expression_value_27);
            if (tmp_tuple_element_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_9);

                exception_lineno = 94;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_args_value_8 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_8, 0, tmp_tuple_element_14);
            tmp_kwargs_value_8 = PyDict_Copy(mod_consts[29]);
            frame_399714034290bc720b8a12943283967a_4->m_frame.f_lineno = 93;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_9, tmp_args_value_8, tmp_kwargs_value_8);
            Py_DECREF(tmp_called_value_9);
            Py_DECREF(tmp_args_value_8);
            Py_DECREF(tmp_kwargs_value_8);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 93;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[40], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 93;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
        }
        {
            PyObject *tmp_called_value_10;
            PyObject *tmp_expression_value_28;
            PyObject *tmp_args_value_9;
            PyObject *tmp_tuple_element_15;
            PyObject *tmp_expression_value_29;
            PyObject *tmp_kwargs_value_9;
            tmp_expression_value_28 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[6]);

            if (tmp_expression_value_28 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_28 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_28 == NULL)) {
                        tmp_expression_value_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_28 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 97;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_28);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_called_value_10 = LOOKUP_ATTRIBUTE(tmp_expression_value_28, mod_consts[27]);
            Py_DECREF(tmp_expression_value_28);
            if (tmp_called_value_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 97;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_expression_value_29 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[6]);

            if (tmp_expression_value_29 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_29 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_29 == NULL)) {
                        tmp_expression_value_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_29 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_10);

                        exception_lineno = 98;
                        type_description_3 = "o";
                        goto frame_exception_exit_4;
                    }
                    Py_INCREF(tmp_expression_value_29);
                } else {
                    goto frame_exception_exit_4;
                }
            }

            tmp_tuple_element_15 = LOOKUP_ATTRIBUTE(tmp_expression_value_29, mod_consts[31]);
            Py_DECREF(tmp_expression_value_29);
            if (tmp_tuple_element_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_10);

                exception_lineno = 98;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_args_value_9 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_9, 0, tmp_tuple_element_15);
            tmp_kwargs_value_9 = PyDict_Copy(mod_consts[32]);
            frame_399714034290bc720b8a12943283967a_4->m_frame.f_lineno = 97;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_10, tmp_args_value_9, tmp_kwargs_value_9);
            Py_DECREF(tmp_called_value_10);
            Py_DECREF(tmp_args_value_9);
            Py_DECREF(tmp_kwargs_value_9);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 97;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[33], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 97;
                type_description_3 = "o";
                goto frame_exception_exit_4;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_399714034290bc720b8a12943283967a_4);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_2;

        frame_exception_exit_4:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_399714034290bc720b8a12943283967a_4);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_399714034290bc720b8a12943283967a_4, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_399714034290bc720b8a12943283967a_4->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_399714034290bc720b8a12943283967a_4, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_399714034290bc720b8a12943283967a_4,
            type_description_3,
            outline_2_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_399714034290bc720b8a12943283967a_4 == cache_frame_399714034290bc720b8a12943283967a_4) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_399714034290bc720b8a12943283967a_4);
            cache_frame_399714034290bc720b8a12943283967a_4 = NULL;
        }

        assertFrameObject(frame_399714034290bc720b8a12943283967a_4);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_3;

        frame_no_exception_2:;
        goto skip_nested_handling_2;
        nested_frame_exit_3:;
        type_description_2 = "o";
        goto try_except_handler_9;
        skip_nested_handling_2:;
        {
            nuitka_bool tmp_condition_result_17;
            PyObject *tmp_cmp_expr_left_2;
            PyObject *tmp_cmp_expr_right_2;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_cmp_expr_left_2 = tmp_WebDetection$class_creation_2__bases;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases_orig);
            tmp_cmp_expr_right_2 = tmp_WebDetection$class_creation_2__bases_orig;
            tmp_condition_result_17 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_2, tmp_cmp_expr_right_2);
            if (tmp_condition_result_17 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_9;
            }
            if (tmp_condition_result_17 == NUITKA_BOOL_TRUE) {
                goto branch_yes_11;
            } else {
                goto branch_no_11;
            }
        }
        branch_yes_11:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases_orig);
        tmp_dictset_value = tmp_WebDetection$class_creation_2__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82, mod_consts[36], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_9;
        }
        branch_no_11:;
        {
            PyObject *tmp_assign_source_26;
            PyObject *tmp_called_value_11;
            PyObject *tmp_args_value_10;
            PyObject *tmp_tuple_element_16;
            PyObject *tmp_kwargs_value_10;
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__metaclass);
            tmp_called_value_11 = tmp_WebDetection$class_creation_2__metaclass;
            tmp_tuple_element_16 = mod_consts[37];
            tmp_args_value_10 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_10, 0, tmp_tuple_element_16);
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
            tmp_tuple_element_16 = tmp_WebDetection$class_creation_2__bases;
            PyTuple_SET_ITEM0(tmp_args_value_10, 1, tmp_tuple_element_16);
            tmp_tuple_element_16 = locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82;
            PyTuple_SET_ITEM0(tmp_args_value_10, 2, tmp_tuple_element_16);
            CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
            tmp_kwargs_value_10 = tmp_WebDetection$class_creation_2__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 82;
            tmp_assign_source_26 = CALL_FUNCTION(tmp_called_value_11, tmp_args_value_10, tmp_kwargs_value_10);
            Py_DECREF(tmp_args_value_10);
            if (tmp_assign_source_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 82;
                type_description_2 = "o";
                goto try_except_handler_9;
            }
            assert(outline_2_var___class__ == NULL);
            outline_2_var___class__ = tmp_assign_source_26;
        }
        CHECK_OBJECT(outline_2_var___class__);
        tmp_dictset_value = outline_2_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_9;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_9:;
        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82);
        locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82 = NULL;
        goto try_return_handler_8;
        // Exception handler code:
        try_except_handler_9:;
        exception_keeper_type_4 = exception_type;
        exception_keeper_value_4 = exception_value;
        exception_keeper_tb_4 = exception_tb;
        exception_keeper_lineno_4 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82);
        locals_google$cloud$vision_v1$types$web_detection$$$class__3_WebImage_82 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_4;
        exception_value = exception_keeper_value_4;
        exception_tb = exception_keeper_tb_4;
        exception_lineno = exception_keeper_lineno_4;

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

        goto outline_exception_3;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_3:;
        exception_lineno = 82;
        goto try_except_handler_7;
        outline_result_3:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[37], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;
            type_description_2 = "o";
            goto try_except_handler_7;
        }
        goto try_end_2;
        // Exception handler code:
        try_except_handler_7:;
        exception_keeper_type_6 = exception_type;
        exception_keeper_value_6 = exception_value;
        exception_keeper_tb_6 = exception_tb;
        exception_keeper_lineno_6 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_WebDetection$class_creation_2__bases_orig);
        tmp_WebDetection$class_creation_2__bases_orig = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_2__bases);
        tmp_WebDetection$class_creation_2__bases = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_2__class_decl_dict);
        tmp_WebDetection$class_creation_2__class_decl_dict = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_2__metaclass);
        tmp_WebDetection$class_creation_2__metaclass = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_2__prepared);
        tmp_WebDetection$class_creation_2__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_6;
        exception_value = exception_keeper_value_6;
        exception_tb = exception_keeper_tb_6;
        exception_lineno = exception_keeper_lineno_6;

        goto frame_exception_exit_2;
        // End of try:
        try_end_2:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases_orig);
        Py_DECREF(tmp_WebDetection$class_creation_2__bases_orig);
        tmp_WebDetection$class_creation_2__bases_orig = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__bases);
        Py_DECREF(tmp_WebDetection$class_creation_2__bases);
        tmp_WebDetection$class_creation_2__bases = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__class_decl_dict);
        Py_DECREF(tmp_WebDetection$class_creation_2__class_decl_dict);
        tmp_WebDetection$class_creation_2__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__metaclass);
        Py_DECREF(tmp_WebDetection$class_creation_2__metaclass);
        tmp_WebDetection$class_creation_2__metaclass = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_2__prepared);
        Py_DECREF(tmp_WebDetection$class_creation_2__prepared);
        tmp_WebDetection$class_creation_2__prepared = NULL;
        // Tried code:
        {
            PyObject *tmp_assign_source_27;
            PyObject *tmp_tuple_element_17;
            PyObject *tmp_expression_value_30;
            tmp_expression_value_30 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_30 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_30 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_30 == NULL)) {
                        tmp_expression_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_30 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 102;
                        type_description_2 = "o";
                        goto try_except_handler_10;
                    }
                    Py_INCREF(tmp_expression_value_30);
                } else {
                    goto try_except_handler_10;
                }
            }

            tmp_tuple_element_17 = LOOKUP_ATTRIBUTE(tmp_expression_value_30, mod_consts[12]);
            Py_DECREF(tmp_expression_value_30);
            if (tmp_tuple_element_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_assign_source_27 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_27, 0, tmp_tuple_element_17);
            assert(tmp_WebDetection$class_creation_3__bases_orig == NULL);
            tmp_WebDetection$class_creation_3__bases_orig = tmp_assign_source_27;
        }
        {
            PyObject *tmp_assign_source_28;
            PyObject *tmp_dircall_arg1_4;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases_orig);
            tmp_dircall_arg1_4 = tmp_WebDetection$class_creation_3__bases_orig;
            Py_INCREF(tmp_dircall_arg1_4);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_4};
                tmp_assign_source_28 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_WebDetection$class_creation_3__bases == NULL);
            tmp_WebDetection$class_creation_3__bases = tmp_assign_source_28;
        }
        {
            PyObject *tmp_assign_source_29;
            tmp_assign_source_29 = PyDict_New();
            assert(tmp_WebDetection$class_creation_3__class_decl_dict == NULL);
            tmp_WebDetection$class_creation_3__class_decl_dict = tmp_assign_source_29;
        }
        {
            PyObject *tmp_assign_source_30;
            PyObject *tmp_metaclass_value_4;
            bool tmp_condition_result_18;
            PyObject *tmp_key_value_10;
            PyObject *tmp_dict_arg_value_10;
            PyObject *tmp_dict_arg_value_11;
            PyObject *tmp_key_value_11;
            nuitka_bool tmp_condition_result_19;
            int tmp_truth_name_4;
            PyObject *tmp_type_arg_7;
            PyObject *tmp_expression_value_31;
            PyObject *tmp_subscript_value_4;
            PyObject *tmp_bases_value_4;
            tmp_key_value_10 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_10 = tmp_WebDetection$class_creation_3__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_10, tmp_key_value_10);
            assert(!(tmp_res == -1));
            tmp_condition_result_18 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_18 != false) {
                goto condexpr_true_7;
            } else {
                goto condexpr_false_7;
            }
            condexpr_true_7:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_11 = tmp_WebDetection$class_creation_3__class_decl_dict;
            tmp_key_value_11 = mod_consts[13];
            tmp_metaclass_value_4 = DICT_GET_ITEM0(tmp_dict_arg_value_11, tmp_key_value_11);
            if (tmp_metaclass_value_4 == NULL) {
                tmp_metaclass_value_4 = Py_None;
            }
            assert(!(tmp_metaclass_value_4 == NULL));
            Py_INCREF(tmp_metaclass_value_4);
            goto condexpr_end_7;
            condexpr_false_7:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_truth_name_4 = CHECK_IF_TRUE(tmp_WebDetection$class_creation_3__bases);
            if (tmp_truth_name_4 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_condition_result_19 = tmp_truth_name_4 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
            if (tmp_condition_result_19 == NUITKA_BOOL_TRUE) {
                goto condexpr_true_8;
            } else {
                goto condexpr_false_8;
            }
            condexpr_true_8:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_expression_value_31 = tmp_WebDetection$class_creation_3__bases;
            tmp_subscript_value_4 = mod_consts[7];
            tmp_type_arg_7 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_31, tmp_subscript_value_4, 0);
            if (tmp_type_arg_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_metaclass_value_4 = BUILTIN_TYPE1(tmp_type_arg_7);
            Py_DECREF(tmp_type_arg_7);
            if (tmp_metaclass_value_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            goto condexpr_end_8;
            condexpr_false_8:;
            tmp_metaclass_value_4 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_4);
            condexpr_end_8:;
            condexpr_end_7:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_bases_value_4 = tmp_WebDetection$class_creation_3__bases;
            tmp_assign_source_30 = SELECT_METACLASS(tmp_metaclass_value_4, tmp_bases_value_4);
            Py_DECREF(tmp_metaclass_value_4);
            if (tmp_assign_source_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_WebDetection$class_creation_3__metaclass == NULL);
            tmp_WebDetection$class_creation_3__metaclass = tmp_assign_source_30;
        }
        {
            bool tmp_condition_result_20;
            PyObject *tmp_key_value_12;
            PyObject *tmp_dict_arg_value_12;
            tmp_key_value_12 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
            tmp_dict_arg_value_12 = tmp_WebDetection$class_creation_3__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_12, tmp_key_value_12);
            assert(!(tmp_res == -1));
            tmp_condition_result_20 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_20 != false) {
                goto branch_yes_12;
            } else {
                goto branch_no_12;
            }
        }
        branch_yes_12:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
        tmp_dictdel_dict = tmp_WebDetection$class_creation_3__class_decl_dict;
        tmp_dictdel_key = mod_consts[13];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_10;
        }
        branch_no_12:;
        {
            nuitka_bool tmp_condition_result_21;
            PyObject *tmp_expression_value_32;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__metaclass);
            tmp_expression_value_32 = tmp_WebDetection$class_creation_3__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_32, mod_consts[14]);
            tmp_condition_result_21 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_21 == NUITKA_BOOL_TRUE) {
                goto branch_yes_13;
            } else {
                goto branch_no_13;
            }
        }
        branch_yes_13:;
        {
            PyObject *tmp_assign_source_31;
            PyObject *tmp_called_value_12;
            PyObject *tmp_expression_value_33;
            PyObject *tmp_args_value_11;
            PyObject *tmp_tuple_element_18;
            PyObject *tmp_kwargs_value_11;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__metaclass);
            tmp_expression_value_33 = tmp_WebDetection$class_creation_3__metaclass;
            tmp_called_value_12 = LOOKUP_ATTRIBUTE(tmp_expression_value_33, mod_consts[14]);
            if (tmp_called_value_12 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_tuple_element_18 = mod_consts[41];
            tmp_args_value_11 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_11, 0, tmp_tuple_element_18);
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_tuple_element_18 = tmp_WebDetection$class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_11, 1, tmp_tuple_element_18);
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
            tmp_kwargs_value_11 = tmp_WebDetection$class_creation_3__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 102;
            tmp_assign_source_31 = CALL_FUNCTION(tmp_called_value_12, tmp_args_value_11, tmp_kwargs_value_11);
            Py_DECREF(tmp_called_value_12);
            Py_DECREF(tmp_args_value_11);
            if (tmp_assign_source_31 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            assert(tmp_WebDetection$class_creation_3__prepared == NULL);
            tmp_WebDetection$class_creation_3__prepared = tmp_assign_source_31;
        }
        {
            bool tmp_condition_result_22;
            PyObject *tmp_operand_value_4;
            PyObject *tmp_expression_value_34;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__prepared);
            tmp_expression_value_34 = tmp_WebDetection$class_creation_3__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_34, mod_consts[16]);
            tmp_operand_value_4 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_4);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_condition_result_22 = (tmp_res == 0) ? true : false;
            if (tmp_condition_result_22 != false) {
                goto branch_yes_14;
            } else {
                goto branch_no_14;
            }
        }
        branch_yes_14:;
        {
            PyObject *tmp_raise_type_4;
            PyObject *tmp_raise_value_4;
            PyObject *tmp_mod_expr_left_4;
            PyObject *tmp_mod_expr_right_4;
            PyObject *tmp_tuple_element_19;
            PyObject *tmp_getattr_target_4;
            PyObject *tmp_getattr_attr_4;
            PyObject *tmp_getattr_default_4;
            tmp_raise_type_4 = PyExc_TypeError;
            tmp_mod_expr_left_4 = mod_consts[17];
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__metaclass);
            tmp_getattr_target_4 = tmp_WebDetection$class_creation_3__metaclass;
            tmp_getattr_attr_4 = mod_consts[18];
            tmp_getattr_default_4 = mod_consts[19];
            tmp_tuple_element_19 = BUILTIN_GETATTR(tmp_getattr_target_4, tmp_getattr_attr_4, tmp_getattr_default_4);
            if (tmp_tuple_element_19 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            tmp_mod_expr_right_4 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_35;
                PyObject *tmp_type_arg_8;
                PyTuple_SET_ITEM(tmp_mod_expr_right_4, 0, tmp_tuple_element_19);
                CHECK_OBJECT(tmp_WebDetection$class_creation_3__prepared);
                tmp_type_arg_8 = tmp_WebDetection$class_creation_3__prepared;
                tmp_expression_value_35 = BUILTIN_TYPE1(tmp_type_arg_8);
                assert(!(tmp_expression_value_35 == NULL));
                tmp_tuple_element_19 = LOOKUP_ATTRIBUTE(tmp_expression_value_35, mod_consts[18]);
                Py_DECREF(tmp_expression_value_35);
                if (tmp_tuple_element_19 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 102;
                    type_description_2 = "o";
                    goto tuple_build_exception_4;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_4, 1, tmp_tuple_element_19);
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


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_10;
            }
            exception_type = tmp_raise_type_4;
            Py_INCREF(tmp_raise_type_4);
            exception_value = tmp_raise_value_4;
            exception_lineno = 102;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_10;
        }
        branch_no_14:;
        goto branch_end_13;
        branch_no_13:;
        {
            PyObject *tmp_assign_source_32;
            tmp_assign_source_32 = PyDict_New();
            assert(tmp_WebDetection$class_creation_3__prepared == NULL);
            tmp_WebDetection$class_creation_3__prepared = tmp_assign_source_32;
        }
        branch_end_13:;
        {
            PyObject *tmp_set_locals_4;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__prepared);
            tmp_set_locals_4 = tmp_WebDetection$class_creation_3__prepared;
            locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102 = tmp_set_locals_4;
            Py_INCREF(tmp_set_locals_4);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[20];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[21], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_12;
        }
        tmp_dictset_value = mod_consts[42];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_12;
        }
        tmp_dictset_value = mod_consts[43];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[23], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_12;
        }
        if (isFrameUnusable(cache_frame_68b58394039f6e7254b4dd7a134349d9_5)) {
            Py_XDECREF(cache_frame_68b58394039f6e7254b4dd7a134349d9_5);

#if _DEBUG_REFCOUNTS
            if (cache_frame_68b58394039f6e7254b4dd7a134349d9_5 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_68b58394039f6e7254b4dd7a134349d9_5 = MAKE_FUNCTION_FRAME(codeobj_68b58394039f6e7254b4dd7a134349d9, module_google$cloud$vision_v1$types$web_detection, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_68b58394039f6e7254b4dd7a134349d9_5->m_type_description == NULL);
        frame_68b58394039f6e7254b4dd7a134349d9_5 = cache_frame_68b58394039f6e7254b4dd7a134349d9_5;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_68b58394039f6e7254b4dd7a134349d9_5);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_68b58394039f6e7254b4dd7a134349d9_5) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_13;
            PyObject *tmp_expression_value_36;
            PyObject *tmp_args_value_12;
            PyObject *tmp_tuple_element_20;
            PyObject *tmp_expression_value_37;
            PyObject *tmp_kwargs_value_12;
            tmp_expression_value_36 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_36 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_36 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_36 == NULL)) {
                        tmp_expression_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_36 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 125;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_36);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_called_value_13 = LOOKUP_ATTRIBUTE(tmp_expression_value_36, mod_consts[27]);
            Py_DECREF(tmp_expression_value_36);
            if (tmp_called_value_13 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 125;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_expression_value_37 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_37 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_37 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_37 == NULL)) {
                        tmp_expression_value_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_37 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_13);

                        exception_lineno = 126;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_37);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_tuple_element_20 = LOOKUP_ATTRIBUTE(tmp_expression_value_37, mod_consts[28]);
            Py_DECREF(tmp_expression_value_37);
            if (tmp_tuple_element_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_13);

                exception_lineno = 126;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_args_value_12 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_12, 0, tmp_tuple_element_20);
            tmp_kwargs_value_12 = PyDict_Copy(mod_consts[29]);
            frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame.f_lineno = 125;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_13, tmp_args_value_12, tmp_kwargs_value_12);
            Py_DECREF(tmp_called_value_13);
            Py_DECREF(tmp_args_value_12);
            Py_DECREF(tmp_kwargs_value_12);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 125;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[40], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 125;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
        }
        {
            PyObject *tmp_called_value_14;
            PyObject *tmp_expression_value_38;
            PyObject *tmp_args_value_13;
            PyObject *tmp_tuple_element_21;
            PyObject *tmp_expression_value_39;
            PyObject *tmp_kwargs_value_13;
            tmp_expression_value_38 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_38 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_38 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_38 == NULL)) {
                        tmp_expression_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_38 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 129;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_38);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_called_value_14 = LOOKUP_ATTRIBUTE(tmp_expression_value_38, mod_consts[27]);
            Py_DECREF(tmp_expression_value_38);
            if (tmp_called_value_14 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 129;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_expression_value_39 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_39 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_39 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_39 == NULL)) {
                        tmp_expression_value_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_39 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_14);

                        exception_lineno = 130;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_39);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_tuple_element_21 = LOOKUP_ATTRIBUTE(tmp_expression_value_39, mod_consts[31]);
            Py_DECREF(tmp_expression_value_39);
            if (tmp_tuple_element_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_14);

                exception_lineno = 130;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_args_value_13 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_13, 0, tmp_tuple_element_21);
            tmp_kwargs_value_13 = PyDict_Copy(mod_consts[32]);
            frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame.f_lineno = 129;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_14, tmp_args_value_13, tmp_kwargs_value_13);
            Py_DECREF(tmp_called_value_14);
            Py_DECREF(tmp_args_value_13);
            Py_DECREF(tmp_kwargs_value_13);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 129;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[33], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 129;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
        }
        {
            PyObject *tmp_called_value_15;
            PyObject *tmp_expression_value_40;
            PyObject *tmp_args_value_14;
            PyObject *tmp_tuple_element_22;
            PyObject *tmp_expression_value_41;
            PyObject *tmp_kwargs_value_14;
            tmp_expression_value_40 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_40 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_40 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_40 == NULL)) {
                        tmp_expression_value_40 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_40 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 133;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_40);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_called_value_15 = LOOKUP_ATTRIBUTE(tmp_expression_value_40, mod_consts[27]);
            Py_DECREF(tmp_expression_value_40);
            if (tmp_called_value_15 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 133;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_expression_value_41 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_41 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_41 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_41 == NULL)) {
                        tmp_expression_value_41 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_41 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_15);

                        exception_lineno = 134;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_41);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_tuple_element_22 = LOOKUP_ATTRIBUTE(tmp_expression_value_41, mod_consts[28]);
            Py_DECREF(tmp_expression_value_41);
            if (tmp_tuple_element_22 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_15);

                exception_lineno = 134;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_args_value_14 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_14, 0, tmp_tuple_element_22);
            tmp_kwargs_value_14 = PyDict_Copy(mod_consts[34]);
            frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame.f_lineno = 133;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_15, tmp_args_value_14, tmp_kwargs_value_14);
            Py_DECREF(tmp_called_value_15);
            Py_DECREF(tmp_args_value_14);
            Py_DECREF(tmp_kwargs_value_14);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 133;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[44], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 133;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
        }
        {
            PyObject *tmp_called_value_16;
            PyObject *tmp_expression_value_42;
            PyObject *tmp_args_value_15;
            PyObject *tmp_tuple_element_23;
            PyObject *tmp_expression_value_43;
            PyObject *tmp_kwargs_value_15;
            tmp_expression_value_42 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_42 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_42 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_42 == NULL)) {
                        tmp_expression_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_42 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 137;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_42);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_called_value_16 = LOOKUP_ATTRIBUTE(tmp_expression_value_42, mod_consts[45]);
            Py_DECREF(tmp_expression_value_42);
            if (tmp_called_value_16 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 137;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_expression_value_43 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_43 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_43 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_43 == NULL)) {
                        tmp_expression_value_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_43 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_16);

                        exception_lineno = 138;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_43);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_tuple_element_23 = LOOKUP_ATTRIBUTE(tmp_expression_value_43, mod_consts[46]);
            Py_DECREF(tmp_expression_value_43);
            if (tmp_tuple_element_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_16);

                exception_lineno = 138;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_args_value_15 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_15, 0, tmp_tuple_element_23);
            tmp_kwargs_value_15 = PyDict_Copy(mod_consts[47]);
            frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame.f_lineno = 137;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_16, tmp_args_value_15, tmp_kwargs_value_15);
            Py_DECREF(tmp_called_value_16);
            Py_DECREF(tmp_args_value_15);
            Py_DECREF(tmp_kwargs_value_15);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 137;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[48], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 137;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
        }
        {
            PyObject *tmp_called_value_17;
            PyObject *tmp_expression_value_44;
            PyObject *tmp_args_value_16;
            PyObject *tmp_tuple_element_24;
            PyObject *tmp_expression_value_45;
            PyObject *tmp_kwargs_value_16;
            tmp_expression_value_44 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_44 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_44 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_44 == NULL)) {
                        tmp_expression_value_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_44 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 142;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_44);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_called_value_17 = LOOKUP_ATTRIBUTE(tmp_expression_value_44, mod_consts[45]);
            Py_DECREF(tmp_expression_value_44);
            if (tmp_called_value_17 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 142;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_expression_value_45 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[6]);

            if (tmp_expression_value_45 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_45 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_45 == NULL)) {
                        tmp_expression_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_45 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_17);

                        exception_lineno = 143;
                        type_description_3 = "o";
                        goto frame_exception_exit_5;
                    }
                    Py_INCREF(tmp_expression_value_45);
                } else {
                    goto frame_exception_exit_5;
                }
            }

            tmp_tuple_element_24 = LOOKUP_ATTRIBUTE(tmp_expression_value_45, mod_consts[46]);
            Py_DECREF(tmp_expression_value_45);
            if (tmp_tuple_element_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_17);

                exception_lineno = 143;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_args_value_16 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_16, 0, tmp_tuple_element_24);
            tmp_kwargs_value_16 = PyDict_Copy(mod_consts[49]);
            frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame.f_lineno = 142;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_17, tmp_args_value_16, tmp_kwargs_value_16);
            Py_DECREF(tmp_called_value_17);
            Py_DECREF(tmp_args_value_16);
            Py_DECREF(tmp_kwargs_value_16);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 142;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[50], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 142;
                type_description_3 = "o";
                goto frame_exception_exit_5;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_68b58394039f6e7254b4dd7a134349d9_5);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_3;

        frame_exception_exit_5:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_68b58394039f6e7254b4dd7a134349d9_5);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_68b58394039f6e7254b4dd7a134349d9_5, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_68b58394039f6e7254b4dd7a134349d9_5->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_68b58394039f6e7254b4dd7a134349d9_5, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_68b58394039f6e7254b4dd7a134349d9_5,
            type_description_3,
            outline_3_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_68b58394039f6e7254b4dd7a134349d9_5 == cache_frame_68b58394039f6e7254b4dd7a134349d9_5) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_68b58394039f6e7254b4dd7a134349d9_5);
            cache_frame_68b58394039f6e7254b4dd7a134349d9_5 = NULL;
        }

        assertFrameObject(frame_68b58394039f6e7254b4dd7a134349d9_5);

        // Put the previous frame back on top.
        popFrameStack();

        // Return the error.
        goto nested_frame_exit_4;

        frame_no_exception_3:;
        goto skip_nested_handling_3;
        nested_frame_exit_4:;
        type_description_2 = "o";
        goto try_except_handler_12;
        skip_nested_handling_3:;
        {
            nuitka_bool tmp_condition_result_23;
            PyObject *tmp_cmp_expr_left_3;
            PyObject *tmp_cmp_expr_right_3;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_cmp_expr_left_3 = tmp_WebDetection$class_creation_3__bases;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases_orig);
            tmp_cmp_expr_right_3 = tmp_WebDetection$class_creation_3__bases_orig;
            tmp_condition_result_23 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_3, tmp_cmp_expr_right_3);
            if (tmp_condition_result_23 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
                goto try_except_handler_12;
            }
            if (tmp_condition_result_23 == NUITKA_BOOL_TRUE) {
                goto branch_yes_15;
            } else {
                goto branch_no_15;
            }
        }
        branch_yes_15:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases_orig);
        tmp_dictset_value = tmp_WebDetection$class_creation_3__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102, mod_consts[36], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_12;
        }
        branch_no_15:;
        {
            PyObject *tmp_assign_source_33;
            PyObject *tmp_called_value_18;
            PyObject *tmp_args_value_17;
            PyObject *tmp_tuple_element_25;
            PyObject *tmp_kwargs_value_17;
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__metaclass);
            tmp_called_value_18 = tmp_WebDetection$class_creation_3__metaclass;
            tmp_tuple_element_25 = mod_consts[41];
            tmp_args_value_17 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_17, 0, tmp_tuple_element_25);
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
            tmp_tuple_element_25 = tmp_WebDetection$class_creation_3__bases;
            PyTuple_SET_ITEM0(tmp_args_value_17, 1, tmp_tuple_element_25);
            tmp_tuple_element_25 = locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102;
            PyTuple_SET_ITEM0(tmp_args_value_17, 2, tmp_tuple_element_25);
            CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
            tmp_kwargs_value_17 = tmp_WebDetection$class_creation_3__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 102;
            tmp_assign_source_33 = CALL_FUNCTION(tmp_called_value_18, tmp_args_value_17, tmp_kwargs_value_17);
            Py_DECREF(tmp_args_value_17);
            if (tmp_assign_source_33 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 102;
                type_description_2 = "o";
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
        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102);
        locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102 = NULL;
        goto try_return_handler_11;
        // Exception handler code:
        try_except_handler_12:;
        exception_keeper_type_7 = exception_type;
        exception_keeper_value_7 = exception_value;
        exception_keeper_tb_7 = exception_tb;
        exception_keeper_lineno_7 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102);
        locals_google$cloud$vision_v1$types$web_detection$$$class__4_WebPage_102 = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_7;
        exception_value = exception_keeper_value_7;
        exception_tb = exception_keeper_tb_7;
        exception_lineno = exception_keeper_lineno_7;

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

        goto outline_exception_4;
        // End of try:
        NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
        return NULL;
        outline_exception_4:;
        exception_lineno = 102;
        goto try_except_handler_10;
        outline_result_4:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[41], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 102;
            type_description_2 = "o";
            goto try_except_handler_10;
        }
        goto try_end_3;
        // Exception handler code:
        try_except_handler_10:;
        exception_keeper_type_9 = exception_type;
        exception_keeper_value_9 = exception_value;
        exception_keeper_tb_9 = exception_tb;
        exception_keeper_lineno_9 = exception_lineno;
        exception_type = NULL;
        exception_value = NULL;
        exception_tb = NULL;
        exception_lineno = 0;

        Py_XDECREF(tmp_WebDetection$class_creation_3__bases_orig);
        tmp_WebDetection$class_creation_3__bases_orig = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_3__bases);
        tmp_WebDetection$class_creation_3__bases = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_3__class_decl_dict);
        tmp_WebDetection$class_creation_3__class_decl_dict = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_3__metaclass);
        tmp_WebDetection$class_creation_3__metaclass = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_3__prepared);
        tmp_WebDetection$class_creation_3__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_9;
        exception_value = exception_keeper_value_9;
        exception_tb = exception_keeper_tb_9;
        exception_lineno = exception_keeper_lineno_9;

        goto frame_exception_exit_2;
        // End of try:
        try_end_3:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases_orig);
        Py_DECREF(tmp_WebDetection$class_creation_3__bases_orig);
        tmp_WebDetection$class_creation_3__bases_orig = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__bases);
        Py_DECREF(tmp_WebDetection$class_creation_3__bases);
        tmp_WebDetection$class_creation_3__bases = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__class_decl_dict);
        Py_DECREF(tmp_WebDetection$class_creation_3__class_decl_dict);
        tmp_WebDetection$class_creation_3__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__metaclass);
        Py_DECREF(tmp_WebDetection$class_creation_3__metaclass);
        tmp_WebDetection$class_creation_3__metaclass = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_3__prepared);
        Py_DECREF(tmp_WebDetection$class_creation_3__prepared);
        tmp_WebDetection$class_creation_3__prepared = NULL;
        // Tried code:
        {
            PyObject *tmp_assign_source_34;
            PyObject *tmp_tuple_element_26;
            PyObject *tmp_expression_value_46;
            tmp_expression_value_46 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_46 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_46 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_46 == NULL)) {
                        tmp_expression_value_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_46 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 148;
                        type_description_2 = "o";
                        goto try_except_handler_13;
                    }
                    Py_INCREF(tmp_expression_value_46);
                } else {
                    goto try_except_handler_13;
                }
            }

            tmp_tuple_element_26 = LOOKUP_ATTRIBUTE(tmp_expression_value_46, mod_consts[12]);
            Py_DECREF(tmp_expression_value_46);
            if (tmp_tuple_element_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_assign_source_34 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_assign_source_34, 0, tmp_tuple_element_26);
            assert(tmp_WebDetection$class_creation_4__bases_orig == NULL);
            tmp_WebDetection$class_creation_4__bases_orig = tmp_assign_source_34;
        }
        {
            PyObject *tmp_assign_source_35;
            PyObject *tmp_dircall_arg1_5;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases_orig);
            tmp_dircall_arg1_5 = tmp_WebDetection$class_creation_4__bases_orig;
            Py_INCREF(tmp_dircall_arg1_5);

            {
                PyObject *dir_call_args[] = {tmp_dircall_arg1_5};
                tmp_assign_source_35 = impl___main__$$$function__1__mro_entries_conversion(dir_call_args);
            }
            if (tmp_assign_source_35 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_WebDetection$class_creation_4__bases == NULL);
            tmp_WebDetection$class_creation_4__bases = tmp_assign_source_35;
        }
        {
            PyObject *tmp_assign_source_36;
            tmp_assign_source_36 = PyDict_New();
            assert(tmp_WebDetection$class_creation_4__class_decl_dict == NULL);
            tmp_WebDetection$class_creation_4__class_decl_dict = tmp_assign_source_36;
        }
        {
            PyObject *tmp_assign_source_37;
            PyObject *tmp_metaclass_value_5;
            bool tmp_condition_result_24;
            PyObject *tmp_key_value_13;
            PyObject *tmp_dict_arg_value_13;
            PyObject *tmp_dict_arg_value_14;
            PyObject *tmp_key_value_14;
            nuitka_bool tmp_condition_result_25;
            int tmp_truth_name_5;
            PyObject *tmp_type_arg_9;
            PyObject *tmp_expression_value_47;
            PyObject *tmp_subscript_value_5;
            PyObject *tmp_bases_value_5;
            tmp_key_value_13 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
            tmp_dict_arg_value_13 = tmp_WebDetection$class_creation_4__class_decl_dict;
            tmp_res = DICT_HAS_ITEM(tmp_dict_arg_value_13, tmp_key_value_13);
            assert(!(tmp_res == -1));
            tmp_condition_result_24 = (tmp_res != 0) ? true : false;
            if (tmp_condition_result_24 != false) {
                goto condexpr_true_9;
            } else {
                goto condexpr_false_9;
            }
            condexpr_true_9:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
            tmp_dict_arg_value_14 = tmp_WebDetection$class_creation_4__class_decl_dict;
            tmp_key_value_14 = mod_consts[13];
            tmp_metaclass_value_5 = DICT_GET_ITEM0(tmp_dict_arg_value_14, tmp_key_value_14);
            if (tmp_metaclass_value_5 == NULL) {
                tmp_metaclass_value_5 = Py_None;
            }
            assert(!(tmp_metaclass_value_5 == NULL));
            Py_INCREF(tmp_metaclass_value_5);
            goto condexpr_end_9;
            condexpr_false_9:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_truth_name_5 = CHECK_IF_TRUE(tmp_WebDetection$class_creation_4__bases);
            if (tmp_truth_name_5 == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
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
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_expression_value_47 = tmp_WebDetection$class_creation_4__bases;
            tmp_subscript_value_5 = mod_consts[7];
            tmp_type_arg_9 = LOOKUP_SUBSCRIPT_CONST(tmp_expression_value_47, tmp_subscript_value_5, 0);
            if (tmp_type_arg_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_metaclass_value_5 = BUILTIN_TYPE1(tmp_type_arg_9);
            Py_DECREF(tmp_type_arg_9);
            if (tmp_metaclass_value_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            goto condexpr_end_10;
            condexpr_false_10:;
            tmp_metaclass_value_5 = (PyObject *)&PyType_Type;
            Py_INCREF(tmp_metaclass_value_5);
            condexpr_end_10:;
            condexpr_end_9:;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_bases_value_5 = tmp_WebDetection$class_creation_4__bases;
            tmp_assign_source_37 = SELECT_METACLASS(tmp_metaclass_value_5, tmp_bases_value_5);
            Py_DECREF(tmp_metaclass_value_5);
            if (tmp_assign_source_37 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_WebDetection$class_creation_4__metaclass == NULL);
            tmp_WebDetection$class_creation_4__metaclass = tmp_assign_source_37;
        }
        {
            bool tmp_condition_result_26;
            PyObject *tmp_key_value_15;
            PyObject *tmp_dict_arg_value_15;
            tmp_key_value_15 = mod_consts[13];
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
            tmp_dict_arg_value_15 = tmp_WebDetection$class_creation_4__class_decl_dict;
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
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
        tmp_dictdel_dict = tmp_WebDetection$class_creation_4__class_decl_dict;
        tmp_dictdel_key = mod_consts[13];
        tmp_result = DICT_REMOVE_ITEM(tmp_dictdel_dict, tmp_dictdel_key);
        if (tmp_result == false) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_2 = "o";
            goto try_except_handler_13;
        }
        branch_no_16:;
        {
            nuitka_bool tmp_condition_result_27;
            PyObject *tmp_expression_value_48;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__metaclass);
            tmp_expression_value_48 = tmp_WebDetection$class_creation_4__metaclass;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_48, mod_consts[14]);
            tmp_condition_result_27 = (tmp_result) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
            if (tmp_condition_result_27 == NUITKA_BOOL_TRUE) {
                goto branch_yes_17;
            } else {
                goto branch_no_17;
            }
        }
        branch_yes_17:;
        {
            PyObject *tmp_assign_source_38;
            PyObject *tmp_called_value_19;
            PyObject *tmp_expression_value_49;
            PyObject *tmp_args_value_18;
            PyObject *tmp_tuple_element_27;
            PyObject *tmp_kwargs_value_18;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__metaclass);
            tmp_expression_value_49 = tmp_WebDetection$class_creation_4__metaclass;
            tmp_called_value_19 = LOOKUP_ATTRIBUTE(tmp_expression_value_49, mod_consts[14]);
            if (tmp_called_value_19 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_tuple_element_27 = mod_consts[51];
            tmp_args_value_18 = PyTuple_New(2);
            PyTuple_SET_ITEM0(tmp_args_value_18, 0, tmp_tuple_element_27);
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_tuple_element_27 = tmp_WebDetection$class_creation_4__bases;
            PyTuple_SET_ITEM0(tmp_args_value_18, 1, tmp_tuple_element_27);
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
            tmp_kwargs_value_18 = tmp_WebDetection$class_creation_4__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 148;
            tmp_assign_source_38 = CALL_FUNCTION(tmp_called_value_19, tmp_args_value_18, tmp_kwargs_value_18);
            Py_DECREF(tmp_called_value_19);
            Py_DECREF(tmp_args_value_18);
            if (tmp_assign_source_38 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            assert(tmp_WebDetection$class_creation_4__prepared == NULL);
            tmp_WebDetection$class_creation_4__prepared = tmp_assign_source_38;
        }
        {
            bool tmp_condition_result_28;
            PyObject *tmp_operand_value_5;
            PyObject *tmp_expression_value_50;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__prepared);
            tmp_expression_value_50 = tmp_WebDetection$class_creation_4__prepared;
            tmp_result = HAS_ATTR_BOOL(tmp_expression_value_50, mod_consts[16]);
            tmp_operand_value_5 = (tmp_result) ? Py_True : Py_False;
            tmp_res = CHECK_IF_TRUE(tmp_operand_value_5);
            if (tmp_res == -1) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
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
            PyObject *tmp_tuple_element_28;
            PyObject *tmp_getattr_target_5;
            PyObject *tmp_getattr_attr_5;
            PyObject *tmp_getattr_default_5;
            tmp_raise_type_5 = PyExc_TypeError;
            tmp_mod_expr_left_5 = mod_consts[17];
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__metaclass);
            tmp_getattr_target_5 = tmp_WebDetection$class_creation_4__metaclass;
            tmp_getattr_attr_5 = mod_consts[18];
            tmp_getattr_default_5 = mod_consts[19];
            tmp_tuple_element_28 = BUILTIN_GETATTR(tmp_getattr_target_5, tmp_getattr_attr_5, tmp_getattr_default_5);
            if (tmp_tuple_element_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            tmp_mod_expr_right_5 = PyTuple_New(2);
            {
                PyObject *tmp_expression_value_51;
                PyObject *tmp_type_arg_10;
                PyTuple_SET_ITEM(tmp_mod_expr_right_5, 0, tmp_tuple_element_28);
                CHECK_OBJECT(tmp_WebDetection$class_creation_4__prepared);
                tmp_type_arg_10 = tmp_WebDetection$class_creation_4__prepared;
                tmp_expression_value_51 = BUILTIN_TYPE1(tmp_type_arg_10);
                assert(!(tmp_expression_value_51 == NULL));
                tmp_tuple_element_28 = LOOKUP_ATTRIBUTE(tmp_expression_value_51, mod_consts[18]);
                Py_DECREF(tmp_expression_value_51);
                if (tmp_tuple_element_28 == NULL) {
                    assert(ERROR_OCCURRED());

                    FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                    exception_lineno = 148;
                    type_description_2 = "o";
                    goto tuple_build_exception_5;
                }
                PyTuple_SET_ITEM(tmp_mod_expr_right_5, 1, tmp_tuple_element_28);
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


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_13;
            }
            exception_type = tmp_raise_type_5;
            Py_INCREF(tmp_raise_type_5);
            exception_value = tmp_raise_value_5;
            exception_lineno = 148;
            RAISE_EXCEPTION_IMPLICIT(&exception_type, &exception_value, &exception_tb);
            type_description_2 = "o";
            goto try_except_handler_13;
        }
        branch_no_18:;
        goto branch_end_17;
        branch_no_17:;
        {
            PyObject *tmp_assign_source_39;
            tmp_assign_source_39 = PyDict_New();
            assert(tmp_WebDetection$class_creation_4__prepared == NULL);
            tmp_WebDetection$class_creation_4__prepared = tmp_assign_source_39;
        }
        branch_end_17:;
        {
            PyObject *tmp_set_locals_5;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__prepared);
            tmp_set_locals_5 = tmp_WebDetection$class_creation_4__prepared;
            locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148 = tmp_set_locals_5;
            Py_INCREF(tmp_set_locals_5);
        }
        // Tried code:
        // Tried code:
        tmp_dictset_value = mod_consts[20];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[21], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        tmp_dictset_value = mod_consts[52];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[0], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        tmp_dictset_value = mod_consts[53];
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[23], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        if (isFrameUnusable(cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6)) {
            Py_XDECREF(cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);

#if _DEBUG_REFCOUNTS
            if (cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 == NULL) {
                count_active_frame_cache_instances += 1;
            } else {
                count_released_frame_cache_instances += 1;
            }
            count_allocated_frame_cache_instances += 1;
#endif
            cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 = MAKE_FUNCTION_FRAME(codeobj_6f55b0b2050a5d5d71e3344b8f66d8af, module_google$cloud$vision_v1$types$web_detection, sizeof(void *));
#if _DEBUG_REFCOUNTS
        } else {
            count_hit_frame_cache_instances += 1;
#endif
        }
        assert(cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6->m_type_description == NULL);
        frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 = cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6;

        // Push the new frame as the currently active one.
        pushFrameStack(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);

        // Mark the frame object as in use, ref count 1 will be up for reuse.
        assert(Py_REFCNT(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6) == 2); // Frame stack

        // Framed code:
        {
            PyObject *tmp_called_value_20;
            PyObject *tmp_expression_value_52;
            PyObject *tmp_args_value_19;
            PyObject *tmp_tuple_element_29;
            PyObject *tmp_expression_value_53;
            PyObject *tmp_kwargs_value_19;
            tmp_expression_value_52 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[6]);

            if (tmp_expression_value_52 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_52 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_52 == NULL)) {
                        tmp_expression_value_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_52 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 160;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_52);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_called_value_20 = LOOKUP_ATTRIBUTE(tmp_expression_value_52, mod_consts[27]);
            Py_DECREF(tmp_expression_value_52);
            if (tmp_called_value_20 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 160;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_expression_value_53 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[6]);

            if (tmp_expression_value_53 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_53 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_53 == NULL)) {
                        tmp_expression_value_53 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_53 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_20);

                        exception_lineno = 161;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_53);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_tuple_element_29 = LOOKUP_ATTRIBUTE(tmp_expression_value_53, mod_consts[28]);
            Py_DECREF(tmp_expression_value_53);
            if (tmp_tuple_element_29 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_20);

                exception_lineno = 161;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_args_value_19 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_19, 0, tmp_tuple_element_29);
            tmp_kwargs_value_19 = PyDict_Copy(mod_consts[29]);
            frame_6f55b0b2050a5d5d71e3344b8f66d8af_6->m_frame.f_lineno = 160;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_20, tmp_args_value_19, tmp_kwargs_value_19);
            Py_DECREF(tmp_called_value_20);
            Py_DECREF(tmp_args_value_19);
            Py_DECREF(tmp_kwargs_value_19);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 160;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[54], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 160;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
        }
        {
            PyObject *tmp_called_value_21;
            PyObject *tmp_expression_value_54;
            PyObject *tmp_args_value_20;
            PyObject *tmp_tuple_element_30;
            PyObject *tmp_expression_value_55;
            PyObject *tmp_kwargs_value_20;
            tmp_expression_value_54 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[6]);

            if (tmp_expression_value_54 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_54 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_54 == NULL)) {
                        tmp_expression_value_54 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_54 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 164;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_54);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_called_value_21 = LOOKUP_ATTRIBUTE(tmp_expression_value_54, mod_consts[27]);
            Py_DECREF(tmp_expression_value_54);
            if (tmp_called_value_21 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 164;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_expression_value_55 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[6]);

            if (tmp_expression_value_55 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_55 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_55 == NULL)) {
                        tmp_expression_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_55 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_21);

                        exception_lineno = 165;
                        type_description_3 = "o";
                        goto frame_exception_exit_6;
                    }
                    Py_INCREF(tmp_expression_value_55);
                } else {
                    goto frame_exception_exit_6;
                }
            }

            tmp_tuple_element_30 = LOOKUP_ATTRIBUTE(tmp_expression_value_55, mod_consts[28]);
            Py_DECREF(tmp_expression_value_55);
            if (tmp_tuple_element_30 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_21);

                exception_lineno = 165;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_args_value_20 = PyTuple_New(1);
            PyTuple_SET_ITEM(tmp_args_value_20, 0, tmp_tuple_element_30);
            tmp_kwargs_value_20 = PyDict_Copy(mod_consts[32]);
            frame_6f55b0b2050a5d5d71e3344b8f66d8af_6->m_frame.f_lineno = 164;
            tmp_dictset_value = CALL_FUNCTION(tmp_called_value_21, tmp_args_value_20, tmp_kwargs_value_20);
            Py_DECREF(tmp_called_value_21);
            Py_DECREF(tmp_args_value_20);
            Py_DECREF(tmp_kwargs_value_20);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 164;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[55], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 164;
                type_description_3 = "o";
                goto frame_exception_exit_6;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_4;

        frame_exception_exit_6:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_6f55b0b2050a5d5d71e3344b8f66d8af_6->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_6f55b0b2050a5d5d71e3344b8f66d8af_6, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_6f55b0b2050a5d5d71e3344b8f66d8af_6,
            type_description_3,
            outline_4_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 == cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);
            cache_frame_6f55b0b2050a5d5d71e3344b8f66d8af_6 = NULL;
        }

        assertFrameObject(frame_6f55b0b2050a5d5d71e3344b8f66d8af_6);

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
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_cmp_expr_left_4 = tmp_WebDetection$class_creation_4__bases;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases_orig);
            tmp_cmp_expr_right_4 = tmp_WebDetection$class_creation_4__bases_orig;
            tmp_condition_result_29 = RICH_COMPARE_NE_NBOOL_OBJECT_TUPLE(tmp_cmp_expr_left_4, tmp_cmp_expr_right_4);
            if (tmp_condition_result_29 == NUITKA_BOOL_EXCEPTION) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
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
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases_orig);
        tmp_dictset_value = tmp_WebDetection$class_creation_4__bases_orig;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148, mod_consts[36], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
            type_description_2 = "o";
            goto try_except_handler_15;
        }
        branch_no_19:;
        {
            PyObject *tmp_assign_source_40;
            PyObject *tmp_called_value_22;
            PyObject *tmp_args_value_21;
            PyObject *tmp_tuple_element_31;
            PyObject *tmp_kwargs_value_21;
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__metaclass);
            tmp_called_value_22 = tmp_WebDetection$class_creation_4__metaclass;
            tmp_tuple_element_31 = mod_consts[51];
            tmp_args_value_21 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_21, 0, tmp_tuple_element_31);
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
            tmp_tuple_element_31 = tmp_WebDetection$class_creation_4__bases;
            PyTuple_SET_ITEM0(tmp_args_value_21, 1, tmp_tuple_element_31);
            tmp_tuple_element_31 = locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148;
            PyTuple_SET_ITEM0(tmp_args_value_21, 2, tmp_tuple_element_31);
            CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
            tmp_kwargs_value_21 = tmp_WebDetection$class_creation_4__class_decl_dict;
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 148;
            tmp_assign_source_40 = CALL_FUNCTION(tmp_called_value_22, tmp_args_value_21, tmp_kwargs_value_21);
            Py_DECREF(tmp_args_value_21);
            if (tmp_assign_source_40 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 148;
                type_description_2 = "o";
                goto try_except_handler_15;
            }
            assert(outline_4_var___class__ == NULL);
            outline_4_var___class__ = tmp_assign_source_40;
        }
        CHECK_OBJECT(outline_4_var___class__);
        tmp_dictset_value = outline_4_var___class__;
        Py_INCREF(tmp_dictset_value);
        goto try_return_handler_15;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_15:;
        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148);
        locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148 = NULL;
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

        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148);
        locals_google$cloud$vision_v1$types$web_detection$$$class__5_WebLabel_148 = NULL;
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
        exception_lineno = 148;
        goto try_except_handler_13;
        outline_result_5:;
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[51], tmp_dictset_value);
        Py_DECREF(tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 148;
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

        Py_XDECREF(tmp_WebDetection$class_creation_4__bases_orig);
        tmp_WebDetection$class_creation_4__bases_orig = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_4__bases);
        tmp_WebDetection$class_creation_4__bases = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_4__class_decl_dict);
        tmp_WebDetection$class_creation_4__class_decl_dict = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_4__metaclass);
        tmp_WebDetection$class_creation_4__metaclass = NULL;
        Py_XDECREF(tmp_WebDetection$class_creation_4__prepared);
        tmp_WebDetection$class_creation_4__prepared = NULL;
        // Re-raise.
        exception_type = exception_keeper_type_12;
        exception_value = exception_keeper_value_12;
        exception_tb = exception_keeper_tb_12;
        exception_lineno = exception_keeper_lineno_12;

        goto frame_exception_exit_2;
        // End of try:
        try_end_4:;
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases_orig);
        Py_DECREF(tmp_WebDetection$class_creation_4__bases_orig);
        tmp_WebDetection$class_creation_4__bases_orig = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__bases);
        Py_DECREF(tmp_WebDetection$class_creation_4__bases);
        tmp_WebDetection$class_creation_4__bases = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__class_decl_dict);
        Py_DECREF(tmp_WebDetection$class_creation_4__class_decl_dict);
        tmp_WebDetection$class_creation_4__class_decl_dict = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__metaclass);
        Py_DECREF(tmp_WebDetection$class_creation_4__metaclass);
        tmp_WebDetection$class_creation_4__metaclass = NULL;
        CHECK_OBJECT(tmp_WebDetection$class_creation_4__prepared);
        Py_DECREF(tmp_WebDetection$class_creation_4__prepared);
        tmp_WebDetection$class_creation_4__prepared = NULL;
        {
            PyObject *tmp_called_value_23;
            PyObject *tmp_expression_value_56;
            PyObject *tmp_kw_call_arg_value_0_1;
            PyObject *tmp_expression_value_57;
            PyObject *tmp_kw_call_dict_value_0_1;
            PyObject *tmp_kw_call_dict_value_1_1;
            tmp_expression_value_56 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_56 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_56 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_56 == NULL)) {
                        tmp_expression_value_56 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_56 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 169;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_56);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_23 = LOOKUP_ATTRIBUTE(tmp_expression_value_56, mod_consts[45]);
            Py_DECREF(tmp_expression_value_56);
            if (tmp_called_value_23 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 169;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_57 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_57 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_57 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_57 == NULL)) {
                        tmp_expression_value_57 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_57 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_23);

                        exception_lineno = 170;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_57);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_57, mod_consts[46]);
            Py_DECREF(tmp_expression_value_57);
            if (tmp_kw_call_arg_value_0_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_23);

                exception_lineno = 170;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_1 = mod_consts[56];
            tmp_kw_call_dict_value_1_1 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[24]);

            if (unlikely(tmp_kw_call_dict_value_1_1 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_23);
                Py_DECREF(tmp_kw_call_arg_value_0_1);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[24]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 172;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_23);
                Py_DECREF(tmp_kw_call_arg_value_0_1);

                exception_lineno = 172;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 169;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_1};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_1, tmp_kw_call_dict_value_1_1};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_23, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_23);
            Py_DECREF(tmp_kw_call_arg_value_0_1);
            Py_DECREF(tmp_kw_call_dict_value_1_1);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 169;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[58], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 169;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_24;
            PyObject *tmp_expression_value_58;
            PyObject *tmp_kw_call_arg_value_0_2;
            PyObject *tmp_expression_value_59;
            PyObject *tmp_kw_call_dict_value_0_2;
            PyObject *tmp_kw_call_dict_value_1_2;
            tmp_expression_value_58 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_58 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_58 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_58 == NULL)) {
                        tmp_expression_value_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_58 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 174;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_58);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_24 = LOOKUP_ATTRIBUTE(tmp_expression_value_58, mod_consts[45]);
            Py_DECREF(tmp_expression_value_58);
            if (tmp_called_value_24 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 174;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_59 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_59 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_59 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_59 == NULL)) {
                        tmp_expression_value_59 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_59 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_24);

                        exception_lineno = 175;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_59);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_59, mod_consts[46]);
            Py_DECREF(tmp_expression_value_59);
            if (tmp_kw_call_arg_value_0_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_24);

                exception_lineno = 175;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_2 = mod_consts[59];
            tmp_kw_call_dict_value_1_2 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[37]);

            if (unlikely(tmp_kw_call_dict_value_1_2 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_24);
                Py_DECREF(tmp_kw_call_arg_value_0_2);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[37]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 177;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_24);
                Py_DECREF(tmp_kw_call_arg_value_0_2);

                exception_lineno = 177;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 174;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_2};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_2, tmp_kw_call_dict_value_1_2};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_24, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_24);
            Py_DECREF(tmp_kw_call_arg_value_0_2);
            Py_DECREF(tmp_kw_call_dict_value_1_2);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 174;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[48], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 174;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_25;
            PyObject *tmp_expression_value_60;
            PyObject *tmp_kw_call_arg_value_0_3;
            PyObject *tmp_expression_value_61;
            PyObject *tmp_kw_call_dict_value_0_3;
            PyObject *tmp_kw_call_dict_value_1_3;
            tmp_expression_value_60 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_60 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_60 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_60 == NULL)) {
                        tmp_expression_value_60 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_60 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 179;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_60);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_25 = LOOKUP_ATTRIBUTE(tmp_expression_value_60, mod_consts[45]);
            Py_DECREF(tmp_expression_value_60);
            if (tmp_called_value_25 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 179;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_61 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_61 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_61 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_61 == NULL)) {
                        tmp_expression_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_61 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_25);

                        exception_lineno = 180;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_61);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_61, mod_consts[46]);
            Py_DECREF(tmp_expression_value_61);
            if (tmp_kw_call_arg_value_0_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_25);

                exception_lineno = 180;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_3 = mod_consts[60];
            tmp_kw_call_dict_value_1_3 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[37]);

            if (unlikely(tmp_kw_call_dict_value_1_3 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_25);
                Py_DECREF(tmp_kw_call_arg_value_0_3);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[37]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 182;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_25);
                Py_DECREF(tmp_kw_call_arg_value_0_3);

                exception_lineno = 182;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 179;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_3};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_3, tmp_kw_call_dict_value_1_3};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_25, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_25);
            Py_DECREF(tmp_kw_call_arg_value_0_3);
            Py_DECREF(tmp_kw_call_dict_value_1_3);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 179;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[50], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 179;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_26;
            PyObject *tmp_expression_value_62;
            PyObject *tmp_kw_call_arg_value_0_4;
            PyObject *tmp_expression_value_63;
            PyObject *tmp_kw_call_dict_value_0_4;
            PyObject *tmp_kw_call_dict_value_1_4;
            tmp_expression_value_62 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_62 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_62 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_62 == NULL)) {
                        tmp_expression_value_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_62 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 184;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_62);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_26 = LOOKUP_ATTRIBUTE(tmp_expression_value_62, mod_consts[45]);
            Py_DECREF(tmp_expression_value_62);
            if (tmp_called_value_26 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 184;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_63 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_63 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_63 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_63 == NULL)) {
                        tmp_expression_value_63 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_63 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_26);

                        exception_lineno = 185;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_63);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_63, mod_consts[46]);
            Py_DECREF(tmp_expression_value_63);
            if (tmp_kw_call_arg_value_0_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_26);

                exception_lineno = 185;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_4 = mod_consts[61];
            tmp_kw_call_dict_value_1_4 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[41]);

            if (unlikely(tmp_kw_call_dict_value_1_4 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_26);
                Py_DECREF(tmp_kw_call_arg_value_0_4);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[41]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 187;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_26);
                Py_DECREF(tmp_kw_call_arg_value_0_4);

                exception_lineno = 187;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 184;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_4};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_4, tmp_kw_call_dict_value_1_4};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_26, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_26);
            Py_DECREF(tmp_kw_call_arg_value_0_4);
            Py_DECREF(tmp_kw_call_dict_value_1_4);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 184;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[62], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 184;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_27;
            PyObject *tmp_expression_value_64;
            PyObject *tmp_kw_call_arg_value_0_5;
            PyObject *tmp_expression_value_65;
            PyObject *tmp_kw_call_dict_value_0_5;
            PyObject *tmp_kw_call_dict_value_1_5;
            tmp_expression_value_64 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_64 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_64 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_64 == NULL)) {
                        tmp_expression_value_64 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_64 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 189;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_64);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_27 = LOOKUP_ATTRIBUTE(tmp_expression_value_64, mod_consts[45]);
            Py_DECREF(tmp_expression_value_64);
            if (tmp_called_value_27 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 189;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_65 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_65 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_65 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_65 == NULL)) {
                        tmp_expression_value_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_65 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_27);

                        exception_lineno = 190;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_65);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_5 = LOOKUP_ATTRIBUTE(tmp_expression_value_65, mod_consts[46]);
            Py_DECREF(tmp_expression_value_65);
            if (tmp_kw_call_arg_value_0_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_27);

                exception_lineno = 190;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_5 = mod_consts[63];
            tmp_kw_call_dict_value_1_5 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[37]);

            if (unlikely(tmp_kw_call_dict_value_1_5 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_27);
                Py_DECREF(tmp_kw_call_arg_value_0_5);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[37]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 192;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_5 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_27);
                Py_DECREF(tmp_kw_call_arg_value_0_5);

                exception_lineno = 192;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 189;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_5};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_5, tmp_kw_call_dict_value_1_5};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_27, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_27);
            Py_DECREF(tmp_kw_call_arg_value_0_5);
            Py_DECREF(tmp_kw_call_dict_value_1_5);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 189;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[64], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 189;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }
        {
            PyObject *tmp_called_value_28;
            PyObject *tmp_expression_value_66;
            PyObject *tmp_kw_call_arg_value_0_6;
            PyObject *tmp_expression_value_67;
            PyObject *tmp_kw_call_dict_value_0_6;
            PyObject *tmp_kw_call_dict_value_1_6;
            tmp_expression_value_66 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_66 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_66 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_66 == NULL)) {
                        tmp_expression_value_66 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_66 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                        exception_lineno = 194;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_66);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_called_value_28 = LOOKUP_ATTRIBUTE(tmp_expression_value_66, mod_consts[45]);
            Py_DECREF(tmp_expression_value_66);
            if (tmp_called_value_28 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 194;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_expression_value_67 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[6]);

            if (tmp_expression_value_67 == NULL) {
                if (CHECK_AND_CLEAR_KEY_ERROR_OCCURRED()) {
                    tmp_expression_value_67 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[6]);

                    if (unlikely(tmp_expression_value_67 == NULL)) {
                        tmp_expression_value_67 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[6]);
                    }

                    if (tmp_expression_value_67 == NULL) {
                        assert(ERROR_OCCURRED());

                        FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                        Py_DECREF(tmp_called_value_28);

                        exception_lineno = 195;
                        type_description_2 = "o";
                        goto frame_exception_exit_2;
                    }
                    Py_INCREF(tmp_expression_value_67);
                } else {
                    goto frame_exception_exit_2;
                }
            }

            tmp_kw_call_arg_value_0_6 = LOOKUP_ATTRIBUTE(tmp_expression_value_67, mod_consts[46]);
            Py_DECREF(tmp_expression_value_67);
            if (tmp_kw_call_arg_value_0_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_28);

                exception_lineno = 195;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_kw_call_dict_value_0_6 = mod_consts[65];
            tmp_kw_call_dict_value_1_6 = PyObject_GetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[51]);

            if (unlikely(tmp_kw_call_dict_value_1_6 == NULL && CHECK_AND_CLEAR_KEY_ERROR_OCCURRED())) {
                Py_DECREF(tmp_called_value_28);
                Py_DECREF(tmp_kw_call_arg_value_0_6);
                FORMAT_NAME_ERROR(&exception_type, &exception_value, mod_consts[51]);
                NORMALIZE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
                CHAIN_EXCEPTION(exception_value);

                exception_lineno = 197;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }

            if (tmp_kw_call_dict_value_1_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_28);
                Py_DECREF(tmp_kw_call_arg_value_0_6);

                exception_lineno = 197;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            frame_48704dc34b9b47c55848cd9834e21857_2->m_frame.f_lineno = 194;
            {
                PyObject *args[] = {tmp_kw_call_arg_value_0_6};
                PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_6, tmp_kw_call_dict_value_1_6};
                tmp_dictset_value = CALL_FUNCTION_WITH_ARGS1_KWSPLIT(tmp_called_value_28, args, kw_values, mod_consts[57]);
            }

            Py_DECREF(tmp_called_value_28);
            Py_DECREF(tmp_kw_call_arg_value_0_6);
            Py_DECREF(tmp_kw_call_dict_value_1_6);
            if (tmp_dictset_value == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 194;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
            tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[66], tmp_dictset_value);
            Py_DECREF(tmp_dictset_value);
            if (tmp_res != 0) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 194;
                type_description_2 = "o";
                goto frame_exception_exit_2;
            }
        }

#if 0
        RESTORE_FRAME_EXCEPTION(frame_48704dc34b9b47c55848cd9834e21857_2);
#endif

        // Put the previous frame back on top.
        popFrameStack();

        goto frame_no_exception_5;

        frame_exception_exit_2:;

#if 0
        RESTORE_FRAME_EXCEPTION(frame_48704dc34b9b47c55848cd9834e21857_2);
#endif

        if (exception_tb == NULL) {
            exception_tb = MAKE_TRACEBACK(frame_48704dc34b9b47c55848cd9834e21857_2, exception_lineno);
        } else if (exception_tb->tb_frame != &frame_48704dc34b9b47c55848cd9834e21857_2->m_frame) {
            exception_tb = ADD_TRACEBACK(exception_tb, frame_48704dc34b9b47c55848cd9834e21857_2, exception_lineno);
        }

        // Attaches locals to frame if any.
        Nuitka_Frame_AttachLocals(
            frame_48704dc34b9b47c55848cd9834e21857_2,
            type_description_2,
            outline_0_var___class__
        );


        // Release cached frame if used for exception.
        if (frame_48704dc34b9b47c55848cd9834e21857_2 == cache_frame_48704dc34b9b47c55848cd9834e21857_2) {
#if _DEBUG_REFCOUNTS
            count_active_frame_cache_instances -= 1;
            count_released_frame_cache_instances += 1;
#endif

            Py_DECREF(cache_frame_48704dc34b9b47c55848cd9834e21857_2);
            cache_frame_48704dc34b9b47c55848cd9834e21857_2 = NULL;
        }

        assertFrameObject(frame_48704dc34b9b47c55848cd9834e21857_2);

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


                exception_lineno = 27;

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
        tmp_res = PyObject_SetItem(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27, mod_consts[36], tmp_dictset_value);
        if (tmp_res != 0) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 27;

            goto try_except_handler_3;
        }
        branch_no_20:;
        {
            PyObject *tmp_assign_source_41;
            PyObject *tmp_called_value_29;
            PyObject *tmp_args_value_22;
            PyObject *tmp_tuple_element_32;
            PyObject *tmp_kwargs_value_22;
            CHECK_OBJECT(tmp_class_creation_1__metaclass);
            tmp_called_value_29 = tmp_class_creation_1__metaclass;
            tmp_tuple_element_32 = mod_consts[15];
            tmp_args_value_22 = PyTuple_New(3);
            PyTuple_SET_ITEM0(tmp_args_value_22, 0, tmp_tuple_element_32);
            CHECK_OBJECT(tmp_class_creation_1__bases);
            tmp_tuple_element_32 = tmp_class_creation_1__bases;
            PyTuple_SET_ITEM0(tmp_args_value_22, 1, tmp_tuple_element_32);
            tmp_tuple_element_32 = locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27;
            PyTuple_SET_ITEM0(tmp_args_value_22, 2, tmp_tuple_element_32);
            CHECK_OBJECT(tmp_class_creation_1__class_decl_dict);
            tmp_kwargs_value_22 = tmp_class_creation_1__class_decl_dict;
            frame_a891ac0a5faafd098b6484b6abf7803b->m_frame.f_lineno = 27;
            tmp_assign_source_41 = CALL_FUNCTION(tmp_called_value_29, tmp_args_value_22, tmp_kwargs_value_22);
            Py_DECREF(tmp_args_value_22);
            if (tmp_assign_source_41 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 27;

                goto try_except_handler_3;
            }
            assert(outline_0_var___class__ == NULL);
            outline_0_var___class__ = tmp_assign_source_41;
        }
        CHECK_OBJECT(outline_0_var___class__);
        tmp_assign_source_12 = outline_0_var___class__;
        Py_INCREF(tmp_assign_source_12);
        goto try_return_handler_3;
        NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
        return NULL;
        // Return handler code:
        try_return_handler_3:;
        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27);
        locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27 = NULL;
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

        Py_DECREF(locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27);
        locals_google$cloud$vision_v1$types$web_detection$$$class__1_WebDetection_27 = NULL;
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
        exception_lineno = 27;
        goto try_except_handler_1;
        outline_result_1:;
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[15], tmp_assign_source_12);
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
    {
        PyObject *tmp_assign_source_42;
        PyObject *tmp_tuple_arg_1;
        PyObject *tmp_called_value_30;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_expression_value_68;
        tmp_called_value_30 = LOOKUP_BUILTIN(mod_consts[67]);
        assert(tmp_called_value_30 != NULL);
        tmp_expression_value_68 = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[11]);

        if (unlikely(tmp_expression_value_68 == NULL)) {
            tmp_expression_value_68 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[11]);
        }

        if (tmp_expression_value_68 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;

            goto frame_exception_exit_1;
        }
        tmp_args_element_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_68, mod_consts[68]);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;

            goto frame_exception_exit_1;
        }
        frame_a891ac0a5faafd098b6484b6abf7803b->m_frame.f_lineno = 201;
        tmp_tuple_arg_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_30, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_tuple_arg_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;

            goto frame_exception_exit_1;
        }
        tmp_assign_source_42 = PySequence_Tuple(tmp_tuple_arg_1);
        Py_DECREF(tmp_tuple_arg_1);
        if (tmp_assign_source_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 201;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)mod_consts[69], tmp_assign_source_42);
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_a891ac0a5faafd098b6484b6abf7803b);
#endif
    popFrameStack();

    assertFrameObject(frame_a891ac0a5faafd098b6484b6abf7803b);

    goto frame_no_exception_6;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_a891ac0a5faafd098b6484b6abf7803b);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_a891ac0a5faafd098b6484b6abf7803b, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_a891ac0a5faafd098b6484b6abf7803b->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_a891ac0a5faafd098b6484b6abf7803b, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_6:;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("google.cloud.vision_v1.types.web_detection", false);

    Py_INCREF(module_google$cloud$vision_v1$types$web_detection);
    return module_google$cloud$vision_v1$types$web_detection;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_google$cloud$vision_v1$types$web_detection, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(module_name);
        }
    }
#endif
    PGO_onModuleExit("google$cloud$vision_v1$types$web_detection", false);

    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}
