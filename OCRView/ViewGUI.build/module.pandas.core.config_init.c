/* Generated code for Python module 'pandas.core.config_init'
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

/* The "module_pandas$core$config_init" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_pandas$core$config_init;
PyDictObject *moduledict_pandas$core$config_init;

/* The declarations of module constants used, if any. */
static PyObject *mod_consts[309];
#ifndef __NUITKA_NO_ASSERT__
static Py_hash_t mod_consts_hash[309];
#endif

static PyObject *module_filename_obj = NULL;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants(void) {
    if (constants_created == false) {
        loadConstantsBlob(&mod_consts[0], UNTRANSLATE("pandas.core.config_init"));
        constants_created = true;

#ifndef __NUITKA_NO_ASSERT__
        for (int i = 0; i < 309; i++) {
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
void checkModuleConstants_pandas$core$config_init(void) {
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;

    for (int i = 0; i < 309; i++) {
        assert(mod_consts_hash[i] == DEEP_HASH(mod_consts[i]));
        CHECK_OBJECT_DEEP(mod_consts[i]);
    }
}
#endif

// The module code objects.
static PyCodeObject *codeobj_929860c9d36c161b6d170f2111d32473;
static PyCodeObject *codeobj_f954a9529706a5eb0e5d2add33aecc20;
static PyCodeObject *codeobj_1c880146936b4a2917b74abd641b9da1;
static PyCodeObject *codeobj_47e6ae525728d504189c90506f905d4a;
static PyCodeObject *codeobj_300ec405869239b6a50424577dd93e35;
static PyCodeObject *codeobj_5d56c938023a616cfc889b1a95efc30c;
static PyCodeObject *codeobj_d8229fc15baa3fd6a08f492465654d13;
static PyCodeObject *codeobj_038ed0ca4b8bb2ec6afe24cd4563f254;
static PyCodeObject *codeobj_c0ac126fd9a3a4d5e92d1167e144fd46;
static PyCodeObject *codeobj_4b193017610ed33740f231139759b565;

static void createModuleCodeObjects(void) {
    module_filename_obj = MAKE_RELATIVE_PATH(mod_consts[297]); CHECK_OBJECT(module_filename_obj);
    codeobj_929860c9d36c161b6d170f2111d32473 = MAKE_CODEOBJECT(module_filename_obj, 1, CO_NOFREE, mod_consts[298], NULL, NULL, 0, 0, 0);
    codeobj_f954a9529706a5eb0e5d2add33aecc20 = MAKE_CODEOBJECT(module_filename_obj, 366, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[158], mod_consts[299], NULL, 1, 0, 0);
    codeobj_1c880146936b4a2917b74abd641b9da1 = MAKE_CODEOBJECT(module_filename_obj, 324, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[141], mod_consts[300], NULL, 0, 0, 0);
    codeobj_47e6ae525728d504189c90506f905d4a = MAKE_CODEOBJECT(module_filename_obj, 722, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[281], mod_consts[301], NULL, 1, 0, 0);
    codeobj_300ec405869239b6a50424577dd93e35 = MAKE_CODEOBJECT(module_filename_obj, 696, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[275], mod_consts[302], NULL, 1, 0, 0);
    codeobj_5d56c938023a616cfc889b1a95efc30c = MAKE_CODEOBJECT(module_filename_obj, 318, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[139], mod_consts[303], NULL, 1, 0, 0);
    codeobj_d8229fc15baa3fd6a08f492465654d13 = MAKE_CODEOBJECT(module_filename_obj, 36, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[58], mod_consts[304], NULL, 1, 0, 0);
    codeobj_038ed0ca4b8bb2ec6afe24cd4563f254 = MAKE_CODEOBJECT(module_filename_obj, 476, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[205], mod_consts[305], NULL, 1, 0, 0);
    codeobj_c0ac126fd9a3a4d5e92d1167e144fd46 = MAKE_CODEOBJECT(module_filename_obj, 64, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[64], mod_consts[306], NULL, 1, 0, 0);
    codeobj_4b193017610ed33740f231139759b565 = MAKE_CODEOBJECT(module_filename_obj, 50, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE, mod_consts[61], mod_consts[307], NULL, 1, 0, 0);
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__1_use_bottleneck_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__2_use_numexpr_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__3_use_numba_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__4_table_schema_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__5_is_terminal(PyObject *annotations);


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__7_use_inf_as_na_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__8_register_plotting_backend_cb();


static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__9_register_converter_cb();


// The module function definitions.
static PyObject *impl_pandas$core$config_init$$$function__1_use_bottleneck_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_nanops = NULL;
    struct Nuitka_FrameObject *frame_d8229fc15baa3fd6a08f492465654d13;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_d8229fc15baa3fd6a08f492465654d13 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_d8229fc15baa3fd6a08f492465654d13)) {
        Py_XDECREF(cache_frame_d8229fc15baa3fd6a08f492465654d13);

#if _DEBUG_REFCOUNTS
        if (cache_frame_d8229fc15baa3fd6a08f492465654d13 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_d8229fc15baa3fd6a08f492465654d13 = MAKE_FUNCTION_FRAME(codeobj_d8229fc15baa3fd6a08f492465654d13, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_d8229fc15baa3fd6a08f492465654d13->m_type_description == NULL);
    frame_d8229fc15baa3fd6a08f492465654d13 = cache_frame_d8229fc15baa3fd6a08f492465654d13;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_d8229fc15baa3fd6a08f492465654d13);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_d8229fc15baa3fd6a08f492465654d13) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[0];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[1];
        tmp_level_value_1 = mod_consts[2];
        frame_d8229fc15baa3fd6a08f492465654d13->m_frame.f_lineno = 37;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[3],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[3]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 37;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var_nanops == NULL);
        var_nanops = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_args_element_value_2;
        CHECK_OBJECT(var_nanops);
        tmp_expression_value_1 = var_nanops;
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[4]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 39;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 39;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_2 = par_key;
        frame_d8229fc15baa3fd6a08f492465654d13->m_frame.f_lineno = 39;
        tmp_args_element_value_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_2);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 39;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_d8229fc15baa3fd6a08f492465654d13->m_frame.f_lineno = 39;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 39;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_d8229fc15baa3fd6a08f492465654d13);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_d8229fc15baa3fd6a08f492465654d13);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_d8229fc15baa3fd6a08f492465654d13, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_d8229fc15baa3fd6a08f492465654d13->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_d8229fc15baa3fd6a08f492465654d13, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_d8229fc15baa3fd6a08f492465654d13,
        type_description_1,
        par_key,
        var_nanops
    );


    // Release cached frame if used for exception.
    if (frame_d8229fc15baa3fd6a08f492465654d13 == cache_frame_d8229fc15baa3fd6a08f492465654d13) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_d8229fc15baa3fd6a08f492465654d13);
        cache_frame_d8229fc15baa3fd6a08f492465654d13 = NULL;
    }

    assertFrameObject(frame_d8229fc15baa3fd6a08f492465654d13);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_nanops);
    Py_DECREF(var_nanops);
    var_nanops = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_nanops);
    var_nanops = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__2_use_numexpr_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_expressions = NULL;
    struct Nuitka_FrameObject *frame_4b193017610ed33740f231139759b565;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_4b193017610ed33740f231139759b565 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_4b193017610ed33740f231139759b565)) {
        Py_XDECREF(cache_frame_4b193017610ed33740f231139759b565);

#if _DEBUG_REFCOUNTS
        if (cache_frame_4b193017610ed33740f231139759b565 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_4b193017610ed33740f231139759b565 = MAKE_FUNCTION_FRAME(codeobj_4b193017610ed33740f231139759b565, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_4b193017610ed33740f231139759b565->m_type_description == NULL);
    frame_4b193017610ed33740f231139759b565 = cache_frame_4b193017610ed33740f231139759b565;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_4b193017610ed33740f231139759b565);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_4b193017610ed33740f231139759b565) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[7];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[8];
        tmp_level_value_1 = mod_consts[2];
        frame_4b193017610ed33740f231139759b565->m_frame.f_lineno = 51;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[9],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[9]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 51;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var_expressions == NULL);
        var_expressions = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_args_element_value_2;
        CHECK_OBJECT(var_expressions);
        tmp_expression_value_1 = var_expressions;
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[10]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 53;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_2 = par_key;
        frame_4b193017610ed33740f231139759b565->m_frame.f_lineno = 53;
        tmp_args_element_value_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_2);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 53;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_4b193017610ed33740f231139759b565->m_frame.f_lineno = 53;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 53;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_4b193017610ed33740f231139759b565);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_4b193017610ed33740f231139759b565);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_4b193017610ed33740f231139759b565, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_4b193017610ed33740f231139759b565->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_4b193017610ed33740f231139759b565, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_4b193017610ed33740f231139759b565,
        type_description_1,
        par_key,
        var_expressions
    );


    // Release cached frame if used for exception.
    if (frame_4b193017610ed33740f231139759b565 == cache_frame_4b193017610ed33740f231139759b565) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_4b193017610ed33740f231139759b565);
        cache_frame_4b193017610ed33740f231139759b565 = NULL;
    }

    assertFrameObject(frame_4b193017610ed33740f231139759b565);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_expressions);
    Py_DECREF(var_expressions);
    var_expressions = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_expressions);
    var_expressions = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__3_use_numba_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_numba_ = NULL;
    struct Nuitka_FrameObject *frame_c0ac126fd9a3a4d5e92d1167e144fd46;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46)) {
        Py_XDECREF(cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46);

#if _DEBUG_REFCOUNTS
        if (cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46 = MAKE_FUNCTION_FRAME(codeobj_c0ac126fd9a3a4d5e92d1167e144fd46, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46->m_type_description == NULL);
    frame_c0ac126fd9a3a4d5e92d1167e144fd46 = cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_c0ac126fd9a3a4d5e92d1167e144fd46);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_c0ac126fd9a3a4d5e92d1167e144fd46) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[11];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[12];
        tmp_level_value_1 = mod_consts[2];
        frame_c0ac126fd9a3a4d5e92d1167e144fd46->m_frame.f_lineno = 65;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[13],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[13]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 65;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var_numba_ == NULL);
        var_numba_ = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_args_element_value_2;
        CHECK_OBJECT(var_numba_);
        tmp_expression_value_1 = var_numba_;
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[14]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 67;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 67;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_2 = par_key;
        frame_c0ac126fd9a3a4d5e92d1167e144fd46->m_frame.f_lineno = 67;
        tmp_args_element_value_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_2);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_1);

            exception_lineno = 67;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_c0ac126fd9a3a4d5e92d1167e144fd46->m_frame.f_lineno = 67;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 67;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_c0ac126fd9a3a4d5e92d1167e144fd46);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_c0ac126fd9a3a4d5e92d1167e144fd46);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_c0ac126fd9a3a4d5e92d1167e144fd46, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_c0ac126fd9a3a4d5e92d1167e144fd46->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_c0ac126fd9a3a4d5e92d1167e144fd46, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_c0ac126fd9a3a4d5e92d1167e144fd46,
        type_description_1,
        par_key,
        var_numba_
    );


    // Release cached frame if used for exception.
    if (frame_c0ac126fd9a3a4d5e92d1167e144fd46 == cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46);
        cache_frame_c0ac126fd9a3a4d5e92d1167e144fd46 = NULL;
    }

    assertFrameObject(frame_c0ac126fd9a3a4d5e92d1167e144fd46);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_numba_);
    Py_DECREF(var_numba_);
    var_numba_ = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_numba_);
    var_numba_ = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__4_table_schema_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_enable_data_resource_formatter = NULL;
    struct Nuitka_FrameObject *frame_5d56c938023a616cfc889b1a95efc30c;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_5d56c938023a616cfc889b1a95efc30c = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_5d56c938023a616cfc889b1a95efc30c)) {
        Py_XDECREF(cache_frame_5d56c938023a616cfc889b1a95efc30c);

#if _DEBUG_REFCOUNTS
        if (cache_frame_5d56c938023a616cfc889b1a95efc30c == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_5d56c938023a616cfc889b1a95efc30c = MAKE_FUNCTION_FRAME(codeobj_5d56c938023a616cfc889b1a95efc30c, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_5d56c938023a616cfc889b1a95efc30c->m_type_description == NULL);
    frame_5d56c938023a616cfc889b1a95efc30c = cache_frame_5d56c938023a616cfc889b1a95efc30c;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_5d56c938023a616cfc889b1a95efc30c);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_5d56c938023a616cfc889b1a95efc30c) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[15];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[16];
        tmp_level_value_1 = mod_consts[2];
        frame_5d56c938023a616cfc889b1a95efc30c->m_frame.f_lineno = 319;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 319;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[17],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[17]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 319;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var_enable_data_resource_formatter == NULL);
        var_enable_data_resource_formatter = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_args_element_value_2;
        CHECK_OBJECT(var_enable_data_resource_formatter);
        tmp_called_value_1 = var_enable_data_resource_formatter;
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 321;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_2 = par_key;
        frame_5d56c938023a616cfc889b1a95efc30c->m_frame.f_lineno = 321;
        tmp_args_element_value_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_2);
        if (tmp_args_element_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 321;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        frame_5d56c938023a616cfc889b1a95efc30c->m_frame.f_lineno = 321;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        Py_DECREF(tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 321;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_5d56c938023a616cfc889b1a95efc30c);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_5d56c938023a616cfc889b1a95efc30c);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_5d56c938023a616cfc889b1a95efc30c, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_5d56c938023a616cfc889b1a95efc30c->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_5d56c938023a616cfc889b1a95efc30c, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_5d56c938023a616cfc889b1a95efc30c,
        type_description_1,
        par_key,
        var_enable_data_resource_formatter
    );


    // Release cached frame if used for exception.
    if (frame_5d56c938023a616cfc889b1a95efc30c == cache_frame_5d56c938023a616cfc889b1a95efc30c) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_5d56c938023a616cfc889b1a95efc30c);
        cache_frame_5d56c938023a616cfc889b1a95efc30c = NULL;
    }

    assertFrameObject(frame_5d56c938023a616cfc889b1a95efc30c);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_enable_data_resource_formatter);
    Py_DECREF(var_enable_data_resource_formatter);
    var_enable_data_resource_formatter = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_enable_data_resource_formatter);
    var_enable_data_resource_formatter = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__5_is_terminal(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *var_ip = NULL;
    struct Nuitka_FrameObject *frame_1c880146936b4a2917b74abd641b9da1;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    PyObject *exception_preserved_type_1;
    PyObject *exception_preserved_value_1;
    PyTracebackObject *exception_preserved_tb_1;
    int tmp_res;
    PyObject *tmp_return_value = NULL;
    bool tmp_result;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    static struct Nuitka_FrameObject *cache_frame_1c880146936b4a2917b74abd641b9da1 = NULL;
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_1c880146936b4a2917b74abd641b9da1)) {
        Py_XDECREF(cache_frame_1c880146936b4a2917b74abd641b9da1);

#if _DEBUG_REFCOUNTS
        if (cache_frame_1c880146936b4a2917b74abd641b9da1 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_1c880146936b4a2917b74abd641b9da1 = MAKE_FUNCTION_FRAME(codeobj_1c880146936b4a2917b74abd641b9da1, module_pandas$core$config_init, sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_1c880146936b4a2917b74abd641b9da1->m_type_description == NULL);
    frame_1c880146936b4a2917b74abd641b9da1 = cache_frame_1c880146936b4a2917b74abd641b9da1;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_1c880146936b4a2917b74abd641b9da1);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_1c880146936b4a2917b74abd641b9da1) == 2); // Frame stack

    // Framed code:
    // Tried code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_called_value_1;
        tmp_called_value_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[18]);

        if (unlikely(tmp_called_value_1 == NULL)) {
            tmp_called_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[18]);
        }

        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 332;
            type_description_1 = "o";
            goto try_except_handler_2;
        }
        frame_1c880146936b4a2917b74abd641b9da1->m_frame.f_lineno = 332;
        tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 332;
            type_description_1 = "o";
            goto try_except_handler_2;
        }
        assert(var_ip == NULL);
        var_ip = tmp_assign_source_1;
    }
    goto try_end_1;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 1.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_1, &exception_preserved_value_1, &exception_preserved_tb_1);

    if (exception_keeper_tb_1 == NULL) {
        exception_keeper_tb_1 = MAKE_TRACEBACK(frame_1c880146936b4a2917b74abd641b9da1, exception_keeper_lineno_1);
    } else if (exception_keeper_lineno_1 != 0) {
        exception_keeper_tb_1 = ADD_TRACEBACK(exception_keeper_tb_1, frame_1c880146936b4a2917b74abd641b9da1, exception_keeper_lineno_1);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_1, exception_keeper_tb_1);
    PUBLISH_EXCEPTION(&exception_keeper_type_1, &exception_keeper_value_1, &exception_keeper_tb_1);
    // Tried code:
    {
        bool tmp_condition_result_1;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        tmp_cmp_expr_left_1 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_1 = PyExc_NameError;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
        assert(!(tmp_res == -1));
        tmp_condition_result_1 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    tmp_return_value = Py_True;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_3;
    goto branch_end_1;
    branch_no_1:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 330;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_1c880146936b4a2917b74abd641b9da1->m_frame) frame_1c880146936b4a2917b74abd641b9da1->m_frame.f_lineno = exception_tb->tb_lineno;
    type_description_1 = "o";
    goto try_except_handler_3;
    branch_end_1:;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_3:;
    // Restore previous exception id 1.
    SET_CURRENT_EXCEPTION(exception_preserved_type_1, exception_preserved_value_1, exception_preserved_tb_1);

    goto frame_return_exit_1;
    // Exception handler code:
    try_except_handler_3:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 1.
    SET_CURRENT_EXCEPTION(exception_preserved_type_1, exception_preserved_value_1, exception_preserved_tb_1);

    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto frame_exception_exit_1;
    // End of try:
    // End of try:
    try_end_1:;
    {
        nuitka_bool tmp_condition_result_2;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_attribute_value_1;
        CHECK_OBJECT(var_ip);
        tmp_expression_value_1 = var_ip;
        tmp_attribute_value_1 = mod_consts[19];
        tmp_res = BUILTIN_HASATTR_BOOL(tmp_expression_value_1, tmp_attribute_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 336;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        tmp_condition_result_2 = (tmp_res != 0) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        if (tmp_condition_result_2 == NUITKA_BOOL_TRUE) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    tmp_return_value = Py_False;
    Py_INCREF(tmp_return_value);
    goto frame_return_exit_1;
    goto branch_end_2;
    branch_no_2:;
    tmp_return_value = Py_True;
    Py_INCREF(tmp_return_value);
    goto frame_return_exit_1;
    branch_end_2:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_1c880146936b4a2917b74abd641b9da1);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_1c880146936b4a2917b74abd641b9da1);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto try_return_handler_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_1c880146936b4a2917b74abd641b9da1);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_1c880146936b4a2917b74abd641b9da1, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_1c880146936b4a2917b74abd641b9da1->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_1c880146936b4a2917b74abd641b9da1, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_1c880146936b4a2917b74abd641b9da1,
        type_description_1,
        var_ip
    );


    // Release cached frame if used for exception.
    if (frame_1c880146936b4a2917b74abd641b9da1 == cache_frame_1c880146936b4a2917b74abd641b9da1) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_1c880146936b4a2917b74abd641b9da1);
        cache_frame_1c880146936b4a2917b74abd641b9da1 = NULL;
    }

    assertFrameObject(frame_1c880146936b4a2917b74abd641b9da1);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    Py_XDECREF(var_ip);
    var_ip = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_3 = exception_type;
    exception_keeper_value_3 = exception_value;
    exception_keeper_tb_3 = exception_tb;
    exception_keeper_lineno_3 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_ip);
    var_ip = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_3;
    exception_value = exception_keeper_value_3;
    exception_tb = exception_keeper_tb_3;
    exception_lineno = exception_keeper_lineno_3;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_value = NULL;
    struct Nuitka_FrameObject *frame_f954a9529706a5eb0e5d2add33aecc20;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_f954a9529706a5eb0e5d2add33aecc20 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_f954a9529706a5eb0e5d2add33aecc20)) {
        Py_XDECREF(cache_frame_f954a9529706a5eb0e5d2add33aecc20);

#if _DEBUG_REFCOUNTS
        if (cache_frame_f954a9529706a5eb0e5d2add33aecc20 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_f954a9529706a5eb0e5d2add33aecc20 = MAKE_FUNCTION_FRAME(codeobj_f954a9529706a5eb0e5d2add33aecc20, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_f954a9529706a5eb0e5d2add33aecc20->m_type_description == NULL);
    frame_f954a9529706a5eb0e5d2add33aecc20 = cache_frame_f954a9529706a5eb0e5d2add33aecc20;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_f954a9529706a5eb0e5d2add33aecc20);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_f954a9529706a5eb0e5d2add33aecc20) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_args_element_value_1;
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 367;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_1 = par_key;
        frame_f954a9529706a5eb0e5d2add33aecc20->m_frame.f_lineno = 367;
        tmp_assign_source_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 367;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var_value == NULL);
        var_value = tmp_assign_source_1;
    }
    {
        nuitka_bool tmp_condition_result_1;
        int tmp_and_left_truth_1;
        nuitka_bool tmp_and_left_value_1;
        nuitka_bool tmp_and_right_value_1;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        PyObject *tmp_cmp_expr_left_2;
        PyObject *tmp_cmp_expr_right_2;
        CHECK_OBJECT(var_value);
        tmp_cmp_expr_left_1 = var_value;
        tmp_cmp_expr_right_1 = Py_None;
        tmp_and_left_value_1 = (tmp_cmp_expr_left_1 != tmp_cmp_expr_right_1) ? NUITKA_BOOL_TRUE : NUITKA_BOOL_FALSE;
        tmp_and_left_truth_1 = tmp_and_left_value_1 == NUITKA_BOOL_TRUE ? 1 : 0;
        if (tmp_and_left_truth_1 == 1) {
            goto and_right_1;
        } else {
            goto and_left_1;
        }
        and_right_1:;
        CHECK_OBJECT(var_value);
        tmp_cmp_expr_left_2 = var_value;
        tmp_cmp_expr_right_2 = mod_consts[2];
        tmp_and_right_value_1 = RICH_COMPARE_LT_NBOOL_OBJECT_LONG(tmp_cmp_expr_left_2, tmp_cmp_expr_right_2);
        if (tmp_and_right_value_1 == NUITKA_BOOL_EXCEPTION) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 368;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_condition_result_1 = tmp_and_right_value_1;
        goto and_end_1;
        and_left_1:;
        tmp_condition_result_1 = tmp_and_left_value_1;
        and_end_1:;
        if (tmp_condition_result_1 == NUITKA_BOOL_TRUE) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_kwargs_value_1;
        tmp_expression_value_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[21]);

        if (unlikely(tmp_expression_value_1 == NULL)) {
            tmp_expression_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[21]);
        }

        if (tmp_expression_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 369;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_called_value_1 = LOOKUP_ATTRIBUTE(tmp_expression_value_1, mod_consts[22]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 369;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        tmp_tuple_element_1 = mod_consts[23];
        tmp_args_value_1 = PyTuple_New(2);
        PyTuple_SET_ITEM0(tmp_args_value_1, 0, tmp_tuple_element_1);
        tmp_tuple_element_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[24]);

        if (unlikely(tmp_tuple_element_1 == NULL)) {
            tmp_tuple_element_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[24]);
        }

        if (tmp_tuple_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 373;
            type_description_1 = "oo";
            goto tuple_build_exception_1;
        }
        PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_1);
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_value_1);
        goto frame_exception_exit_1;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_kwargs_value_1 = PyDict_Copy(mod_consts[25]);
        frame_f954a9529706a5eb0e5d2add33aecc20->m_frame.f_lineno = 369;
        tmp_call_result_1 = CALL_FUNCTION(tmp_called_value_1, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_called_value_1);
        Py_DECREF(tmp_args_value_1);
        Py_DECREF(tmp_kwargs_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 369;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }
    branch_no_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_f954a9529706a5eb0e5d2add33aecc20);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_f954a9529706a5eb0e5d2add33aecc20);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_f954a9529706a5eb0e5d2add33aecc20, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_f954a9529706a5eb0e5d2add33aecc20->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_f954a9529706a5eb0e5d2add33aecc20, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_f954a9529706a5eb0e5d2add33aecc20,
        type_description_1,
        par_key,
        var_value
    );


    // Release cached frame if used for exception.
    if (frame_f954a9529706a5eb0e5d2add33aecc20 == cache_frame_f954a9529706a5eb0e5d2add33aecc20) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_f954a9529706a5eb0e5d2add33aecc20);
        cache_frame_f954a9529706a5eb0e5d2add33aecc20 = NULL;
    }

    assertFrameObject(frame_f954a9529706a5eb0e5d2add33aecc20);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var_value);
    Py_DECREF(var_value);
    var_value = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_value);
    var_value = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__7_use_inf_as_na_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var__use_inf_as_na = NULL;
    struct Nuitka_FrameObject *frame_038ed0ca4b8bb2ec6afe24cd4563f254;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254)) {
        Py_XDECREF(cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254);

#if _DEBUG_REFCOUNTS
        if (cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254 = MAKE_FUNCTION_FRAME(codeobj_038ed0ca4b8bb2ec6afe24cd4563f254, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254->m_type_description == NULL);
    frame_038ed0ca4b8bb2ec6afe24cd4563f254 = cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_038ed0ca4b8bb2ec6afe24cd4563f254);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_038ed0ca4b8bb2ec6afe24cd4563f254) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[26];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[27];
        tmp_level_value_1 = mod_consts[2];
        frame_038ed0ca4b8bb2ec6afe24cd4563f254->m_frame.f_lineno = 477;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 477;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[28],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[28]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 477;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var__use_inf_as_na == NULL);
        var__use_inf_as_na = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        CHECK_OBJECT(var__use_inf_as_na);
        tmp_called_value_1 = var__use_inf_as_na;
        CHECK_OBJECT(par_key);
        tmp_args_element_value_1 = par_key;
        frame_038ed0ca4b8bb2ec6afe24cd4563f254->m_frame.f_lineno = 479;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 479;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_038ed0ca4b8bb2ec6afe24cd4563f254);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_038ed0ca4b8bb2ec6afe24cd4563f254);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_038ed0ca4b8bb2ec6afe24cd4563f254, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_038ed0ca4b8bb2ec6afe24cd4563f254->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_038ed0ca4b8bb2ec6afe24cd4563f254, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_038ed0ca4b8bb2ec6afe24cd4563f254,
        type_description_1,
        par_key,
        var__use_inf_as_na
    );


    // Release cached frame if used for exception.
    if (frame_038ed0ca4b8bb2ec6afe24cd4563f254 == cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254);
        cache_frame_038ed0ca4b8bb2ec6afe24cd4563f254 = NULL;
    }

    assertFrameObject(frame_038ed0ca4b8bb2ec6afe24cd4563f254);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT(var__use_inf_as_na);
    Py_DECREF(var__use_inf_as_na);
    var__use_inf_as_na = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var__use_inf_as_na);
    var__use_inf_as_na = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__8_register_plotting_backend_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var__get_plot_backend = NULL;
    struct Nuitka_FrameObject *frame_300ec405869239b6a50424577dd93e35;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *tmp_return_value = NULL;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_300ec405869239b6a50424577dd93e35 = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_300ec405869239b6a50424577dd93e35)) {
        Py_XDECREF(cache_frame_300ec405869239b6a50424577dd93e35);

#if _DEBUG_REFCOUNTS
        if (cache_frame_300ec405869239b6a50424577dd93e35 == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_300ec405869239b6a50424577dd93e35 = MAKE_FUNCTION_FRAME(codeobj_300ec405869239b6a50424577dd93e35, module_pandas$core$config_init, sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_300ec405869239b6a50424577dd93e35->m_type_description == NULL);
    frame_300ec405869239b6a50424577dd93e35 = cache_frame_300ec405869239b6a50424577dd93e35;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_300ec405869239b6a50424577dd93e35);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_300ec405869239b6a50424577dd93e35) == 2); // Frame stack

    // Framed code:
    {
        nuitka_bool tmp_condition_result_1;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        CHECK_OBJECT(par_key);
        tmp_cmp_expr_left_1 = par_key;
        tmp_cmp_expr_right_1 = mod_consts[29];
        tmp_condition_result_1 = RICH_COMPARE_EQ_NBOOL_OBJECT_UNICODE(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
        if (tmp_condition_result_1 == NUITKA_BOOL_EXCEPTION) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 697;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (tmp_condition_result_1 == NUITKA_BOOL_TRUE) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto frame_return_exit_1;
    branch_no_1:;
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[30];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[31];
        tmp_level_value_1 = mod_consts[2];
        frame_300ec405869239b6a50424577dd93e35->m_frame.f_lineno = 700;
        tmp_import_name_from_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 700;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[32],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_1 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[32]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 700;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        assert(var__get_plot_backend == NULL);
        var__get_plot_backend = tmp_assign_source_1;
    }
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        CHECK_OBJECT(var__get_plot_backend);
        tmp_called_value_1 = var__get_plot_backend;
        CHECK_OBJECT(par_key);
        tmp_args_element_value_1 = par_key;
        frame_300ec405869239b6a50424577dd93e35->m_frame.f_lineno = 702;
        tmp_call_result_1 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_1, tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 702;
            type_description_1 = "oo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_1);
    }

#if 0
    RESTORE_FRAME_EXCEPTION(frame_300ec405869239b6a50424577dd93e35);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_300ec405869239b6a50424577dd93e35);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto try_return_handler_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_300ec405869239b6a50424577dd93e35);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_300ec405869239b6a50424577dd93e35, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_300ec405869239b6a50424577dd93e35->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_300ec405869239b6a50424577dd93e35, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_300ec405869239b6a50424577dd93e35,
        type_description_1,
        par_key,
        var__get_plot_backend
    );


    // Release cached frame if used for exception.
    if (frame_300ec405869239b6a50424577dd93e35 == cache_frame_300ec405869239b6a50424577dd93e35) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_300ec405869239b6a50424577dd93e35);
        cache_frame_300ec405869239b6a50424577dd93e35 = NULL;
    }

    assertFrameObject(frame_300ec405869239b6a50424577dd93e35);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    Py_XDECREF(var__get_plot_backend);
    var__get_plot_backend = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var__get_plot_backend);
    var__get_plot_backend = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}


static PyObject *impl_pandas$core$config_init$$$function__9_register_converter_cb(struct Nuitka_FunctionObject const *self, PyObject **python_pars) {
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_key = python_pars[0];
    PyObject *var_deregister_matplotlib_converters = NULL;
    PyObject *var_register_matplotlib_converters = NULL;
    PyObject *tmp_import_from_1__module = NULL;
    struct Nuitka_FrameObject *frame_47e6ae525728d504189c90506f905d4a;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    static struct Nuitka_FrameObject *cache_frame_47e6ae525728d504189c90506f905d4a = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;

    // Actual function body.
    // Tried code:
    if (isFrameUnusable(cache_frame_47e6ae525728d504189c90506f905d4a)) {
        Py_XDECREF(cache_frame_47e6ae525728d504189c90506f905d4a);

#if _DEBUG_REFCOUNTS
        if (cache_frame_47e6ae525728d504189c90506f905d4a == NULL) {
            count_active_frame_cache_instances += 1;
        } else {
            count_released_frame_cache_instances += 1;
        }
        count_allocated_frame_cache_instances += 1;
#endif
        cache_frame_47e6ae525728d504189c90506f905d4a = MAKE_FUNCTION_FRAME(codeobj_47e6ae525728d504189c90506f905d4a, module_pandas$core$config_init, sizeof(void *)+sizeof(void *)+sizeof(void *));
#if _DEBUG_REFCOUNTS
    } else {
        count_hit_frame_cache_instances += 1;
#endif
    }
    assert(cache_frame_47e6ae525728d504189c90506f905d4a->m_type_description == NULL);
    frame_47e6ae525728d504189c90506f905d4a = cache_frame_47e6ae525728d504189c90506f905d4a;

    // Push the new frame as the currently active one.
    pushFrameStack(frame_47e6ae525728d504189c90506f905d4a);

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert(Py_REFCNT(frame_47e6ae525728d504189c90506f905d4a) == 2); // Frame stack

    // Framed code:
    {
        PyObject *tmp_assign_source_1;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[33];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = mod_consts[34];
        tmp_level_value_1 = mod_consts[2];
        frame_47e6ae525728d504189c90506f905d4a->m_frame.f_lineno = 723;
        tmp_assign_source_1 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 723;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        assert(tmp_import_from_1__module == NULL);
        tmp_import_from_1__module = tmp_assign_source_1;
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_2;
        PyObject *tmp_import_name_from_1;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_1 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_2 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[35],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_2 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[35]);
        }

        if (tmp_assign_source_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 723;
            type_description_1 = "ooo";
            goto try_except_handler_2;
        }
        assert(var_deregister_matplotlib_converters == NULL);
        var_deregister_matplotlib_converters = tmp_assign_source_2;
    }
    {
        PyObject *tmp_assign_source_3;
        PyObject *tmp_import_name_from_2;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_2 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_assign_source_3 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_2,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[36],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_3 = IMPORT_NAME(tmp_import_name_from_2, mod_consts[36]);
        }

        if (tmp_assign_source_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 723;
            type_description_1 = "ooo";
            goto try_except_handler_2;
        }
        assert(var_register_matplotlib_converters == NULL);
        var_register_matplotlib_converters = tmp_assign_source_3;
    }
    goto try_end_1;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    {
        nuitka_bool tmp_condition_result_1;
        PyObject *tmp_called_instance_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_value_1;
        int tmp_truth_name_1;
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 728;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        CHECK_OBJECT(par_key);
        tmp_args_element_value_1 = par_key;
        frame_47e6ae525728d504189c90506f905d4a->m_frame.f_lineno = 728;
        tmp_call_result_1 = CALL_METHOD_WITH_SINGLE_ARG(tmp_called_instance_1, mod_consts[6], tmp_args_element_value_1);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 728;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        tmp_truth_name_1 = CHECK_IF_TRUE(tmp_call_result_1);
        if (tmp_truth_name_1 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_call_result_1);

            exception_lineno = 728;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        tmp_condition_result_1 = tmp_truth_name_1 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        Py_DECREF(tmp_call_result_1);
        if (tmp_condition_result_1 == NUITKA_BOOL_TRUE) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        PyObject *tmp_called_value_1;
        PyObject *tmp_call_result_2;
        CHECK_OBJECT(var_register_matplotlib_converters);
        tmp_called_value_1 = var_register_matplotlib_converters;
        frame_47e6ae525728d504189c90506f905d4a->m_frame.f_lineno = 729;
        tmp_call_result_2 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        if (tmp_call_result_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 729;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_2);
    }
    goto branch_end_1;
    branch_no_1:;
    {
        PyObject *tmp_called_value_2;
        PyObject *tmp_call_result_3;
        CHECK_OBJECT(var_deregister_matplotlib_converters);
        tmp_called_value_2 = var_deregister_matplotlib_converters;
        frame_47e6ae525728d504189c90506f905d4a->m_frame.f_lineno = 731;
        tmp_call_result_3 = CALL_FUNCTION_NO_ARGS(tmp_called_value_2);
        if (tmp_call_result_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 731;
            type_description_1 = "ooo";
            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_3);
    }
    branch_end_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_47e6ae525728d504189c90506f905d4a);
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION(frame_47e6ae525728d504189c90506f905d4a);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_47e6ae525728d504189c90506f905d4a, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_47e6ae525728d504189c90506f905d4a->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_47e6ae525728d504189c90506f905d4a, exception_lineno);
    }

    // Attaches locals to frame if any.
    Nuitka_Frame_AttachLocals(
        frame_47e6ae525728d504189c90506f905d4a,
        type_description_1,
        par_key,
        var_deregister_matplotlib_converters,
        var_register_matplotlib_converters
    );


    // Release cached frame if used for exception.
    if (frame_47e6ae525728d504189c90506f905d4a == cache_frame_47e6ae525728d504189c90506f905d4a) {
#if _DEBUG_REFCOUNTS
        count_active_frame_cache_instances -= 1;
        count_released_frame_cache_instances += 1;
#endif

        Py_DECREF(cache_frame_47e6ae525728d504189c90506f905d4a);
        cache_frame_47e6ae525728d504189c90506f905d4a = NULL;
    }

    assertFrameObject(frame_47e6ae525728d504189c90506f905d4a);

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF(tmp_return_value);
    goto try_return_handler_1;
    NUITKA_CANNOT_GET_HERE("tried codes exits in all cases");
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    Py_XDECREF(var_deregister_matplotlib_converters);
    var_deregister_matplotlib_converters = NULL;
    CHECK_OBJECT(var_register_matplotlib_converters);
    Py_DECREF(var_register_matplotlib_converters);
    var_register_matplotlib_converters = NULL;
    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(var_deregister_matplotlib_converters);
    var_deregister_matplotlib_converters = NULL;
    Py_XDECREF(var_register_matplotlib_converters);
    var_register_matplotlib_converters = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_2;
    exception_value = exception_keeper_value_2;
    exception_tb = exception_keeper_tb_2;
    exception_lineno = exception_keeper_lineno_2;

    goto function_exception_exit;
    // End of try:

    NUITKA_CANNOT_GET_HERE("Return statement must have exited already.");
    return NULL;

function_exception_exit:
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);    assert(exception_type);
    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);

    return NULL;

function_return_exit:
   // Function cleanup code if any.
    CHECK_OBJECT(par_key);
    Py_DECREF(par_key);

   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT(tmp_return_value);
   assert(had_error || !ERROR_OCCURRED());
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__1_use_bottleneck_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__1_use_bottleneck_cb,
        mod_consts[58],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_d8229fc15baa3fd6a08f492465654d13,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__2_use_numexpr_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__2_use_numexpr_cb,
        mod_consts[61],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_4b193017610ed33740f231139759b565,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__3_use_numba_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__3_use_numba_cb,
        mod_consts[64],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_c0ac126fd9a3a4d5e92d1167e144fd46,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__4_table_schema_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__4_table_schema_cb,
        mod_consts[139],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_5d56c938023a616cfc889b1a95efc30c,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__5_is_terminal(PyObject *annotations) {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__5_is_terminal,
        mod_consts[141],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_1c880146936b4a2917b74abd641b9da1,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        annotations,
#endif
        module_pandas$core$config_init,
        mod_consts[20],
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth,
        mod_consts[158],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_f954a9529706a5eb0e5d2add33aecc20,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__7_use_inf_as_na_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__7_use_inf_as_na_cb,
        mod_consts[205],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_038ed0ca4b8bb2ec6afe24cd4563f254,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__8_register_plotting_backend_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__8_register_plotting_backend_cb,
        mod_consts[275],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_300ec405869239b6a50424577dd93e35,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION_pandas$core$config_init$$$function__9_register_converter_cb() {
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_pandas$core$config_init$$$function__9_register_converter_cb,
        mod_consts[281],
#if PYTHON_VERSION >= 0x300
        NULL,
#endif
        codeobj_47e6ae525728d504189c90506f905d4a,
        NULL,
#if PYTHON_VERSION >= 0x300
        NULL,
        NULL,
#endif
        module_pandas$core$config_init,
        NULL,
        NULL,
        0
    );


    return (PyObject *)result;
}


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

function_impl_code functable_pandas$core$config_init[] = {
    impl_pandas$core$config_init$$$function__1_use_bottleneck_cb,
    impl_pandas$core$config_init$$$function__2_use_numexpr_cb,
    impl_pandas$core$config_init$$$function__3_use_numba_cb,
    impl_pandas$core$config_init$$$function__4_table_schema_cb,
    impl_pandas$core$config_init$$$function__5_is_terminal,
    impl_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth,
    impl_pandas$core$config_init$$$function__7_use_inf_as_na_cb,
    impl_pandas$core$config_init$$$function__8_register_plotting_backend_cb,
    impl_pandas$core$config_init$$$function__9_register_converter_cb,
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

    function_impl_code *current = functable_pandas$core$config_init;
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

    if (offset > sizeof(functable_pandas$core$config_init) || offset < 0) {
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
        functable_pandas$core$config_init[offset],
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
        module_pandas$core$config_init,
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
PyObject *modulecode_pandas$core$config_init(PyObject *module, struct Nuitka_MetaPathBasedLoaderEntry const *loader_entry) {
    // Report entry to PGO.
    PGO_onModuleEntered("pandas.core.config_init");

    // Store the module for future use.
    module_pandas$core$config_init = module;

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
        PRINT_STRING("pandas.core.config_init: Calling setupMetaPathBasedLoader().\n");
#endif
        setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 0x300
        patchInspectModule();
#endif

#endif

        /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("pandas.core.config_init: Calling createModuleConstants().\n");
#endif
        createModuleConstants();

        /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
        PRINT_STRING("pandas.core.config_init: Calling createModuleCodeObjects().\n");
#endif
        createModuleCodeObjects();

        init_done = true;
    }

    // PRINT_STRING("in initpandas$core$config_init\n");

    moduledict_pandas$core$config_init = MODULE_DICT(module_pandas$core$config_init);

#ifdef _NUITKA_PLUGIN_DILL_ENABLED
    registerDillPluginTables(loader_entry->name, &_method_def_reduce_compiled_function, &_method_def_create_compiled_function);
#endif

    // Set "__compiled__" to what version information we have.
    UPDATE_STRING_DICT0(
        moduledict_pandas$core$config_init,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        UPDATE_STRING_DICT0(
            moduledict_pandas$core$config_init,
            (Nuitka_StringObject *)const_str_plain___package__,
            mod_consts[308]
        );
#elif 0
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___name__);

        UPDATE_STRING_DICT0(
            moduledict_pandas$core$config_init,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 0x300
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___name__);
        char const *module_name_cstr = PyString_AS_STRING(module_name);

        char const *last_dot = strrchr(module_name_cstr, '.');

        if (last_dot != NULL) {
            UPDATE_STRING_DICT1(
                moduledict_pandas$core$config_init,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize(module_name_cstr, last_dot - module_name_cstr)
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___name__);
        Py_ssize_t dot_index = PyUnicode_Find(module_name, const_str_dot, 0, PyUnicode_GetLength(module_name), -1);

        if (dot_index != -1) {
            UPDATE_STRING_DICT1(
                moduledict_pandas$core$config_init,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring(module_name, 0, dot_index)
            );
        }
#endif
#endif
    }

    CHECK_OBJECT(module_pandas$core$config_init);

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if (GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___builtins__) == NULL) {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if defined(_NUITKA_MODULE) || !0
        value = PyModule_GetDict(value);
#endif

        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___builtins__, value);
    }

#if PYTHON_VERSION >= 0x300
    UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type);
#endif

#if PYTHON_VERSION >= 0x340
// Set the "__spec__" value

#if 0
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___spec__, Py_None);
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = getImportLibBootstrapModule();
        CHECK_OBJECT(bootstrap_module);

        PyObject *_spec_from_module = PyObject_GetAttrString(bootstrap_module, "_spec_from_module");
        CHECK_OBJECT(_spec_from_module);

        PyObject *spec_value = CALL_FUNCTION_WITH_SINGLE_ARG(_spec_from_module, module_pandas$core$config_init);
        Py_DECREF(_spec_from_module);

        // We can assume this to never fail, or else we are in trouble anyway.
        // CHECK_OBJECT(spec_value);

        if (spec_value == NULL) {
            PyErr_PrintEx(0);
            abort();
        }

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE(spec_value, const_str_plain__initializing, Py_True);

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___spec__, spec_value);
    }
#endif
#endif

    // Temp variables if any
    PyObject *tmp_import_from_1__module = NULL;
    PyObject *tmp_with_10__enter = NULL;
    PyObject *tmp_with_10__exit = NULL;
    nuitka_bool tmp_with_10__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_10__source = NULL;
    PyObject *tmp_with_11__enter = NULL;
    PyObject *tmp_with_11__exit = NULL;
    nuitka_bool tmp_with_11__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_11__source = NULL;
    PyObject *tmp_with_12__enter = NULL;
    PyObject *tmp_with_12__exit = NULL;
    nuitka_bool tmp_with_12__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_12__source = NULL;
    PyObject *tmp_with_13__enter = NULL;
    PyObject *tmp_with_13__exit = NULL;
    nuitka_bool tmp_with_13__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_13__source = NULL;
    PyObject *tmp_with_14__enter = NULL;
    PyObject *tmp_with_14__exit = NULL;
    nuitka_bool tmp_with_14__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_14__source = NULL;
    PyObject *tmp_with_15__enter = NULL;
    PyObject *tmp_with_15__exit = NULL;
    nuitka_bool tmp_with_15__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_15__source = NULL;
    PyObject *tmp_with_16__enter = NULL;
    PyObject *tmp_with_16__exit = NULL;
    nuitka_bool tmp_with_16__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_16__source = NULL;
    PyObject *tmp_with_17__enter = NULL;
    PyObject *tmp_with_17__exit = NULL;
    nuitka_bool tmp_with_17__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_17__source = NULL;
    PyObject *tmp_with_18__enter = NULL;
    PyObject *tmp_with_18__exit = NULL;
    nuitka_bool tmp_with_18__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_18__source = NULL;
    PyObject *tmp_with_19__enter = NULL;
    PyObject *tmp_with_19__exit = NULL;
    nuitka_bool tmp_with_19__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_19__source = NULL;
    PyObject *tmp_with_1__enter = NULL;
    PyObject *tmp_with_1__exit = NULL;
    nuitka_bool tmp_with_1__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_1__source = NULL;
    PyObject *tmp_with_20__enter = NULL;
    PyObject *tmp_with_20__exit = NULL;
    nuitka_bool tmp_with_20__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_20__source = NULL;
    PyObject *tmp_with_21__enter = NULL;
    PyObject *tmp_with_21__exit = NULL;
    nuitka_bool tmp_with_21__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_21__source = NULL;
    PyObject *tmp_with_2__enter = NULL;
    PyObject *tmp_with_2__exit = NULL;
    nuitka_bool tmp_with_2__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_2__source = NULL;
    PyObject *tmp_with_3__enter = NULL;
    PyObject *tmp_with_3__exit = NULL;
    nuitka_bool tmp_with_3__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_3__source = NULL;
    PyObject *tmp_with_4__enter = NULL;
    PyObject *tmp_with_4__exit = NULL;
    nuitka_bool tmp_with_4__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_4__source = NULL;
    PyObject *tmp_with_5__enter = NULL;
    PyObject *tmp_with_5__exit = NULL;
    nuitka_bool tmp_with_5__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_5__source = NULL;
    PyObject *tmp_with_6__enter = NULL;
    PyObject *tmp_with_6__exit = NULL;
    nuitka_bool tmp_with_6__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_6__source = NULL;
    PyObject *tmp_with_7__enter = NULL;
    PyObject *tmp_with_7__exit = NULL;
    nuitka_bool tmp_with_7__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_7__source = NULL;
    PyObject *tmp_with_8__enter = NULL;
    PyObject *tmp_with_8__exit = NULL;
    nuitka_bool tmp_with_8__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_8__source = NULL;
    PyObject *tmp_with_9__enter = NULL;
    PyObject *tmp_with_9__exit = NULL;
    nuitka_bool tmp_with_9__indicator = NUITKA_BOOL_UNASSIGNED;
    PyObject *tmp_with_9__source = NULL;
    struct Nuitka_FrameObject *frame_929860c9d36c161b6d170f2111d32473;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    bool tmp_result;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;
    NUITKA_MAY_BE_UNUSED nuitka_void tmp_unused;
    PyObject *exception_keeper_type_2;
    PyObject *exception_keeper_value_2;
    PyTracebackObject *exception_keeper_tb_2;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_2;
    PyObject *exception_preserved_type_1;
    PyObject *exception_preserved_value_1;
    PyTracebackObject *exception_preserved_tb_1;
    int tmp_res;
    PyObject *exception_keeper_type_3;
    PyObject *exception_keeper_value_3;
    PyTracebackObject *exception_keeper_tb_3;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_3;
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
    PyObject *exception_preserved_type_2;
    PyObject *exception_preserved_value_2;
    PyTracebackObject *exception_preserved_tb_2;
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
    PyObject *exception_keeper_type_10;
    PyObject *exception_keeper_value_10;
    PyTracebackObject *exception_keeper_tb_10;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_10;
    PyObject *exception_preserved_type_3;
    PyObject *exception_preserved_value_3;
    PyTracebackObject *exception_preserved_tb_3;
    PyObject *exception_keeper_type_11;
    PyObject *exception_keeper_value_11;
    PyTracebackObject *exception_keeper_tb_11;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_11;
    PyObject *exception_keeper_type_12;
    PyObject *exception_keeper_value_12;
    PyTracebackObject *exception_keeper_tb_12;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_12;
    PyObject *exception_keeper_type_13;
    PyObject *exception_keeper_value_13;
    PyTracebackObject *exception_keeper_tb_13;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_13;
    PyObject *exception_keeper_type_14;
    PyObject *exception_keeper_value_14;
    PyTracebackObject *exception_keeper_tb_14;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_14;
    PyObject *exception_preserved_type_4;
    PyObject *exception_preserved_value_4;
    PyTracebackObject *exception_preserved_tb_4;
    PyObject *exception_keeper_type_15;
    PyObject *exception_keeper_value_15;
    PyTracebackObject *exception_keeper_tb_15;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_15;
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
    PyObject *exception_preserved_type_5;
    PyObject *exception_preserved_value_5;
    PyTracebackObject *exception_preserved_tb_5;
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
    PyObject *exception_keeper_type_22;
    PyObject *exception_keeper_value_22;
    PyTracebackObject *exception_keeper_tb_22;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_22;
    PyObject *exception_preserved_type_6;
    PyObject *exception_preserved_value_6;
    PyTracebackObject *exception_preserved_tb_6;
    PyObject *exception_keeper_type_23;
    PyObject *exception_keeper_value_23;
    PyTracebackObject *exception_keeper_tb_23;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_23;
    PyObject *exception_keeper_type_24;
    PyObject *exception_keeper_value_24;
    PyTracebackObject *exception_keeper_tb_24;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_24;
    PyObject *exception_keeper_type_25;
    PyObject *exception_keeper_value_25;
    PyTracebackObject *exception_keeper_tb_25;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_25;
    PyObject *exception_keeper_type_26;
    PyObject *exception_keeper_value_26;
    PyTracebackObject *exception_keeper_tb_26;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_26;
    PyObject *exception_preserved_type_7;
    PyObject *exception_preserved_value_7;
    PyTracebackObject *exception_preserved_tb_7;
    PyObject *exception_keeper_type_27;
    PyObject *exception_keeper_value_27;
    PyTracebackObject *exception_keeper_tb_27;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_27;
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
    PyObject *exception_preserved_type_8;
    PyObject *exception_preserved_value_8;
    PyTracebackObject *exception_preserved_tb_8;
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
    PyObject *exception_keeper_type_34;
    PyObject *exception_keeper_value_34;
    PyTracebackObject *exception_keeper_tb_34;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_34;
    PyObject *exception_preserved_type_9;
    PyObject *exception_preserved_value_9;
    PyTracebackObject *exception_preserved_tb_9;
    PyObject *exception_keeper_type_35;
    PyObject *exception_keeper_value_35;
    PyTracebackObject *exception_keeper_tb_35;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_35;
    PyObject *exception_keeper_type_36;
    PyObject *exception_keeper_value_36;
    PyTracebackObject *exception_keeper_tb_36;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_36;
    PyObject *exception_keeper_type_37;
    PyObject *exception_keeper_value_37;
    PyTracebackObject *exception_keeper_tb_37;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_37;
    PyObject *exception_keeper_type_38;
    PyObject *exception_keeper_value_38;
    PyTracebackObject *exception_keeper_tb_38;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_38;
    PyObject *exception_preserved_type_10;
    PyObject *exception_preserved_value_10;
    PyTracebackObject *exception_preserved_tb_10;
    PyObject *exception_keeper_type_39;
    PyObject *exception_keeper_value_39;
    PyTracebackObject *exception_keeper_tb_39;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_39;
    PyObject *exception_keeper_type_40;
    PyObject *exception_keeper_value_40;
    PyTracebackObject *exception_keeper_tb_40;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_40;
    PyObject *exception_keeper_type_41;
    PyObject *exception_keeper_value_41;
    PyTracebackObject *exception_keeper_tb_41;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_41;
    PyObject *exception_keeper_type_42;
    PyObject *exception_keeper_value_42;
    PyTracebackObject *exception_keeper_tb_42;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_42;
    PyObject *exception_preserved_type_11;
    PyObject *exception_preserved_value_11;
    PyTracebackObject *exception_preserved_tb_11;
    PyObject *exception_keeper_type_43;
    PyObject *exception_keeper_value_43;
    PyTracebackObject *exception_keeper_tb_43;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_43;
    PyObject *exception_keeper_type_44;
    PyObject *exception_keeper_value_44;
    PyTracebackObject *exception_keeper_tb_44;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_44;
    PyObject *exception_keeper_type_45;
    PyObject *exception_keeper_value_45;
    PyTracebackObject *exception_keeper_tb_45;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_45;
    PyObject *exception_keeper_type_46;
    PyObject *exception_keeper_value_46;
    PyTracebackObject *exception_keeper_tb_46;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_46;
    PyObject *exception_preserved_type_12;
    PyObject *exception_preserved_value_12;
    PyTracebackObject *exception_preserved_tb_12;
    PyObject *exception_keeper_type_47;
    PyObject *exception_keeper_value_47;
    PyTracebackObject *exception_keeper_tb_47;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_47;
    PyObject *exception_keeper_type_48;
    PyObject *exception_keeper_value_48;
    PyTracebackObject *exception_keeper_tb_48;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_48;
    PyObject *exception_keeper_type_49;
    PyObject *exception_keeper_value_49;
    PyTracebackObject *exception_keeper_tb_49;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_49;
    PyObject *exception_keeper_type_50;
    PyObject *exception_keeper_value_50;
    PyTracebackObject *exception_keeper_tb_50;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_50;
    PyObject *exception_preserved_type_13;
    PyObject *exception_preserved_value_13;
    PyTracebackObject *exception_preserved_tb_13;
    PyObject *exception_keeper_type_51;
    PyObject *exception_keeper_value_51;
    PyTracebackObject *exception_keeper_tb_51;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_51;
    PyObject *exception_keeper_type_52;
    PyObject *exception_keeper_value_52;
    PyTracebackObject *exception_keeper_tb_52;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_52;
    PyObject *exception_keeper_type_53;
    PyObject *exception_keeper_value_53;
    PyTracebackObject *exception_keeper_tb_53;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_53;
    PyObject *exception_keeper_type_54;
    PyObject *exception_keeper_value_54;
    PyTracebackObject *exception_keeper_tb_54;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_54;
    PyObject *exception_preserved_type_14;
    PyObject *exception_preserved_value_14;
    PyTracebackObject *exception_preserved_tb_14;
    PyObject *exception_keeper_type_55;
    PyObject *exception_keeper_value_55;
    PyTracebackObject *exception_keeper_tb_55;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_55;
    PyObject *exception_keeper_type_56;
    PyObject *exception_keeper_value_56;
    PyTracebackObject *exception_keeper_tb_56;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_56;
    PyObject *exception_keeper_type_57;
    PyObject *exception_keeper_value_57;
    PyTracebackObject *exception_keeper_tb_57;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_57;
    PyObject *exception_keeper_type_58;
    PyObject *exception_keeper_value_58;
    PyTracebackObject *exception_keeper_tb_58;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_58;
    PyObject *exception_preserved_type_15;
    PyObject *exception_preserved_value_15;
    PyTracebackObject *exception_preserved_tb_15;
    PyObject *exception_keeper_type_59;
    PyObject *exception_keeper_value_59;
    PyTracebackObject *exception_keeper_tb_59;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_59;
    PyObject *exception_keeper_type_60;
    PyObject *exception_keeper_value_60;
    PyTracebackObject *exception_keeper_tb_60;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_60;
    PyObject *exception_keeper_type_61;
    PyObject *exception_keeper_value_61;
    PyTracebackObject *exception_keeper_tb_61;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_61;
    PyObject *exception_keeper_type_62;
    PyObject *exception_keeper_value_62;
    PyTracebackObject *exception_keeper_tb_62;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_62;
    PyObject *exception_preserved_type_16;
    PyObject *exception_preserved_value_16;
    PyTracebackObject *exception_preserved_tb_16;
    PyObject *exception_keeper_type_63;
    PyObject *exception_keeper_value_63;
    PyTracebackObject *exception_keeper_tb_63;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_63;
    PyObject *exception_keeper_type_64;
    PyObject *exception_keeper_value_64;
    PyTracebackObject *exception_keeper_tb_64;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_64;
    PyObject *exception_keeper_type_65;
    PyObject *exception_keeper_value_65;
    PyTracebackObject *exception_keeper_tb_65;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_65;
    PyObject *exception_keeper_type_66;
    PyObject *exception_keeper_value_66;
    PyTracebackObject *exception_keeper_tb_66;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_66;
    PyObject *exception_preserved_type_17;
    PyObject *exception_preserved_value_17;
    PyTracebackObject *exception_preserved_tb_17;
    PyObject *exception_keeper_type_67;
    PyObject *exception_keeper_value_67;
    PyTracebackObject *exception_keeper_tb_67;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_67;
    PyObject *exception_keeper_type_68;
    PyObject *exception_keeper_value_68;
    PyTracebackObject *exception_keeper_tb_68;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_68;
    PyObject *exception_keeper_type_69;
    PyObject *exception_keeper_value_69;
    PyTracebackObject *exception_keeper_tb_69;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_69;
    PyObject *exception_keeper_type_70;
    PyObject *exception_keeper_value_70;
    PyTracebackObject *exception_keeper_tb_70;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_70;
    PyObject *exception_preserved_type_18;
    PyObject *exception_preserved_value_18;
    PyTracebackObject *exception_preserved_tb_18;
    PyObject *exception_keeper_type_71;
    PyObject *exception_keeper_value_71;
    PyTracebackObject *exception_keeper_tb_71;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_71;
    PyObject *exception_keeper_type_72;
    PyObject *exception_keeper_value_72;
    PyTracebackObject *exception_keeper_tb_72;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_72;
    PyObject *exception_keeper_type_73;
    PyObject *exception_keeper_value_73;
    PyTracebackObject *exception_keeper_tb_73;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_73;
    PyObject *exception_keeper_type_74;
    PyObject *exception_keeper_value_74;
    PyTracebackObject *exception_keeper_tb_74;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_74;
    PyObject *exception_preserved_type_19;
    PyObject *exception_preserved_value_19;
    PyTracebackObject *exception_preserved_tb_19;
    PyObject *exception_keeper_type_75;
    PyObject *exception_keeper_value_75;
    PyTracebackObject *exception_keeper_tb_75;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_75;
    PyObject *exception_keeper_type_76;
    PyObject *exception_keeper_value_76;
    PyTracebackObject *exception_keeper_tb_76;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_76;
    PyObject *exception_keeper_type_77;
    PyObject *exception_keeper_value_77;
    PyTracebackObject *exception_keeper_tb_77;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_77;
    PyObject *exception_keeper_type_78;
    PyObject *exception_keeper_value_78;
    PyTracebackObject *exception_keeper_tb_78;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_78;
    PyObject *exception_preserved_type_20;
    PyObject *exception_preserved_value_20;
    PyTracebackObject *exception_preserved_tb_20;
    PyObject *exception_keeper_type_79;
    PyObject *exception_keeper_value_79;
    PyTracebackObject *exception_keeper_tb_79;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_79;
    PyObject *exception_keeper_type_80;
    PyObject *exception_keeper_value_80;
    PyTracebackObject *exception_keeper_tb_80;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_80;
    PyObject *exception_keeper_type_81;
    PyObject *exception_keeper_value_81;
    PyTracebackObject *exception_keeper_tb_81;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_81;
    PyObject *exception_keeper_type_82;
    PyObject *exception_keeper_value_82;
    PyTracebackObject *exception_keeper_tb_82;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_82;
    PyObject *exception_preserved_type_21;
    PyObject *exception_preserved_value_21;
    PyTracebackObject *exception_preserved_tb_21;
    PyObject *exception_keeper_type_83;
    PyObject *exception_keeper_value_83;
    PyTracebackObject *exception_keeper_tb_83;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_83;
    PyObject *exception_keeper_type_84;
    PyObject *exception_keeper_value_84;
    PyTracebackObject *exception_keeper_tb_84;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_84;
    PyObject *exception_keeper_type_85;
    PyObject *exception_keeper_value_85;
    PyTracebackObject *exception_keeper_tb_85;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_85;

    // Module code.
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = mod_consts[37];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[38], tmp_assign_source_1);
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[39], tmp_assign_source_2);
    }
    // Frame without reuse.
    frame_929860c9d36c161b6d170f2111d32473 = MAKE_MODULE_FRAME(codeobj_929860c9d36c161b6d170f2111d32473, module_pandas$core$config_init);

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack(frame_929860c9d36c161b6d170f2111d32473);
    assert(Py_REFCNT(frame_929860c9d36c161b6d170f2111d32473) == 2);

    // Framed code:
    {
        PyObject *tmp_assattr_value_1;
        PyObject *tmp_assattr_target_1;
        tmp_assattr_value_1 = module_filename_obj;
        tmp_assattr_target_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[40]);

        if (unlikely(tmp_assattr_target_1 == NULL)) {
            tmp_assattr_target_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[40]);
        }

        assert(!(tmp_assattr_target_1 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_1, mod_consts[41], tmp_assattr_value_1);
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
        tmp_assattr_target_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[40]);

        if (unlikely(tmp_assattr_target_2 == NULL)) {
            tmp_assattr_target_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[40]);
        }

        assert(!(tmp_assattr_target_2 == NULL));
        tmp_result = SET_ATTRIBUTE(tmp_assattr_target_2, mod_consts[42], tmp_assattr_value_2);
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
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[43], tmp_assign_source_3);
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = IMPORT_HARD_OS();
        assert(!(tmp_assign_source_4 == NULL));
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[44], tmp_assign_source_4);
    }
    {
        PyObject *tmp_assign_source_5;
        PyObject *tmp_name_value_1;
        PyObject *tmp_globals_arg_value_1;
        PyObject *tmp_locals_arg_value_1;
        PyObject *tmp_fromlist_value_1;
        PyObject *tmp_level_value_1;
        tmp_name_value_1 = mod_consts[21];
        tmp_globals_arg_value_1 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_1 = Py_None;
        tmp_fromlist_value_1 = Py_None;
        tmp_level_value_1 = mod_consts[2];
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 13;
        tmp_assign_source_5 = IMPORT_MODULE5(tmp_name_value_1, tmp_globals_arg_value_1, tmp_locals_arg_value_1, tmp_fromlist_value_1, tmp_level_value_1);
        if (tmp_assign_source_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 13;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[21], tmp_assign_source_5);
    }
    {
        PyObject *tmp_assign_source_6;
        PyObject *tmp_import_name_from_1;
        PyObject *tmp_import_name_from_2;
        PyObject *tmp_name_value_2;
        PyObject *tmp_globals_arg_value_2;
        PyObject *tmp_locals_arg_value_2;
        PyObject *tmp_fromlist_value_2;
        PyObject *tmp_level_value_2;
        tmp_name_value_2 = mod_consts[45];
        tmp_globals_arg_value_2 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_2 = Py_None;
        tmp_fromlist_value_2 = Py_None;
        tmp_level_value_2 = mod_consts[2];
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 15;
        tmp_import_name_from_2 = IMPORT_MODULE5(tmp_name_value_2, tmp_globals_arg_value_2, tmp_locals_arg_value_2, tmp_fromlist_value_2, tmp_level_value_2);
        if (tmp_import_name_from_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 15;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_2)) {
            tmp_import_name_from_1 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_2,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[46],
                mod_consts[2]
            );
        } else {
            tmp_import_name_from_1 = IMPORT_NAME(tmp_import_name_from_2, mod_consts[46]);
        }

        Py_DECREF(tmp_import_name_from_2);
        if (tmp_import_name_from_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 15;

            goto frame_exception_exit_1;
        }
        if (PyModule_Check(tmp_import_name_from_1)) {
            tmp_assign_source_6 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_1,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[47],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_6 = IMPORT_NAME(tmp_import_name_from_1, mod_consts[47]);
        }

        Py_DECREF(tmp_import_name_from_1);
        if (tmp_assign_source_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 15;

            goto frame_exception_exit_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5], tmp_assign_source_6);
    }
    {
        PyObject *tmp_assign_source_7;
        PyObject *tmp_name_value_3;
        PyObject *tmp_globals_arg_value_3;
        PyObject *tmp_locals_arg_value_3;
        PyObject *tmp_fromlist_value_3;
        PyObject *tmp_level_value_3;
        tmp_name_value_3 = mod_consts[45];
        tmp_globals_arg_value_3 = (PyObject *)moduledict_pandas$core$config_init;
        tmp_locals_arg_value_3 = Py_None;
        tmp_fromlist_value_3 = mod_consts[48];
        tmp_level_value_3 = mod_consts[2];
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 16;
        tmp_assign_source_7 = IMPORT_MODULE5(tmp_name_value_3, tmp_globals_arg_value_3, tmp_locals_arg_value_3, tmp_fromlist_value_3, tmp_level_value_3);
        if (tmp_assign_source_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto frame_exception_exit_1;
        }
        assert(tmp_import_from_1__module == NULL);
        tmp_import_from_1__module = tmp_assign_source_7;
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_8;
        PyObject *tmp_import_name_from_3;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_3 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_3)) {
            tmp_assign_source_8 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_3,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[49],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_8 = IMPORT_NAME(tmp_import_name_from_3, mod_consts[49]);
        }

        if (tmp_assign_source_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49], tmp_assign_source_8);
    }
    {
        PyObject *tmp_assign_source_9;
        PyObject *tmp_import_name_from_4;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_4 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_4)) {
            tmp_assign_source_9 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_4,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[50],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_9 = IMPORT_NAME(tmp_import_name_from_4, mod_consts[50]);
        }

        if (tmp_assign_source_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[50], tmp_assign_source_9);
    }
    {
        PyObject *tmp_assign_source_10;
        PyObject *tmp_import_name_from_5;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_5 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_5)) {
            tmp_assign_source_10 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_5,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[51],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_10 = IMPORT_NAME(tmp_import_name_from_5, mod_consts[51]);
        }

        if (tmp_assign_source_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[51], tmp_assign_source_10);
    }
    {
        PyObject *tmp_assign_source_11;
        PyObject *tmp_import_name_from_6;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_6 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_6)) {
            tmp_assign_source_11 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_6,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[52],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_11 = IMPORT_NAME(tmp_import_name_from_6, mod_consts[52]);
        }

        if (tmp_assign_source_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52], tmp_assign_source_11);
    }
    {
        PyObject *tmp_assign_source_12;
        PyObject *tmp_import_name_from_7;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_7 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_7)) {
            tmp_assign_source_12 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_7,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[53],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_12 = IMPORT_NAME(tmp_import_name_from_7, mod_consts[53]);
        }

        if (tmp_assign_source_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[53], tmp_assign_source_12);
    }
    {
        PyObject *tmp_assign_source_13;
        PyObject *tmp_import_name_from_8;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_8 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_8)) {
            tmp_assign_source_13 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_8,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[54],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_13 = IMPORT_NAME(tmp_import_name_from_8, mod_consts[54]);
        }

        if (tmp_assign_source_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54], tmp_assign_source_13);
    }
    {
        PyObject *tmp_assign_source_14;
        PyObject *tmp_import_name_from_9;
        CHECK_OBJECT(tmp_import_from_1__module);
        tmp_import_name_from_9 = tmp_import_from_1__module;
        if (PyModule_Check(tmp_import_name_from_9)) {
            tmp_assign_source_14 = IMPORT_NAME_OR_MODULE(
                tmp_import_name_from_9,
                (PyObject *)moduledict_pandas$core$config_init,
                mod_consts[55],
                mod_consts[2]
            );
        } else {
            tmp_assign_source_14 = IMPORT_NAME(tmp_import_name_from_9, mod_consts[55]);
        }

        if (tmp_assign_source_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 16;

            goto try_except_handler_1;
        }
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[55], tmp_assign_source_14);
    }
    goto try_end_1;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto frame_exception_exit_1;
    // End of try:
    try_end_1:;
    CHECK_OBJECT(tmp_import_from_1__module);
    Py_DECREF(tmp_import_from_1__module);
    tmp_import_from_1__module = NULL;
    {
        PyObject *tmp_assign_source_15;
        tmp_assign_source_15 = mod_consts[56];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[57], tmp_assign_source_15);
    }
    {
        PyObject *tmp_assign_source_16;


        tmp_assign_source_16 = MAKE_FUNCTION_pandas$core$config_init$$$function__1_use_bottleneck_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[58], tmp_assign_source_16);
    }
    {
        PyObject *tmp_assign_source_17;
        tmp_assign_source_17 = mod_consts[59];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[60], tmp_assign_source_17);
    }
    {
        PyObject *tmp_assign_source_18;


        tmp_assign_source_18 = MAKE_FUNCTION_pandas$core$config_init$$$function__2_use_numexpr_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[61], tmp_assign_source_18);
    }
    {
        PyObject *tmp_assign_source_19;
        tmp_assign_source_19 = mod_consts[62];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[63], tmp_assign_source_19);
    }
    {
        PyObject *tmp_assign_source_20;


        tmp_assign_source_20 = MAKE_FUNCTION_pandas$core$config_init$$$function__3_use_numba_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[64], tmp_assign_source_20);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_21;
        PyObject *tmp_called_instance_1;
        tmp_called_instance_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_1 == NULL)) {
            tmp_called_instance_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 70;

            goto try_except_handler_2;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 70;
        tmp_assign_source_21 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_1,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[66], 0)
        );

        if (tmp_assign_source_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 70;

            goto try_except_handler_2;
        }
        assert(tmp_with_1__source == NULL);
        tmp_with_1__source = tmp_assign_source_21;
    }
    {
        PyObject *tmp_assign_source_22;
        PyObject *tmp_called_value_1;
        PyObject *tmp_expression_value_1;
        CHECK_OBJECT(tmp_with_1__source);
        tmp_expression_value_1 = tmp_with_1__source;
        tmp_called_value_1 = LOOKUP_SPECIAL(tmp_expression_value_1, mod_consts[67]);
        if (tmp_called_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 70;

            goto try_except_handler_2;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 70;
        tmp_assign_source_22 = CALL_FUNCTION_NO_ARGS(tmp_called_value_1);
        Py_DECREF(tmp_called_value_1);
        if (tmp_assign_source_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 70;

            goto try_except_handler_2;
        }
        assert(tmp_with_1__enter == NULL);
        tmp_with_1__enter = tmp_assign_source_22;
    }
    {
        PyObject *tmp_assign_source_23;
        PyObject *tmp_expression_value_2;
        CHECK_OBJECT(tmp_with_1__source);
        tmp_expression_value_2 = tmp_with_1__source;
        tmp_assign_source_23 = LOOKUP_SPECIAL(tmp_expression_value_2, mod_consts[68]);
        if (tmp_assign_source_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 70;

            goto try_except_handler_2;
        }
        assert(tmp_with_1__exit == NULL);
        tmp_with_1__exit = tmp_assign_source_23;
    }
    {
        nuitka_bool tmp_assign_source_24;
        tmp_assign_source_24 = NUITKA_BOOL_TRUE;
        tmp_with_1__indicator = tmp_assign_source_24;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_2;
        PyObject *tmp_expression_value_3;
        PyObject *tmp_call_result_1;
        PyObject *tmp_kw_call_arg_value_0_1;
        PyObject *tmp_kw_call_arg_value_1_1;
        PyObject *tmp_kw_call_arg_value_2_1;
        PyObject *tmp_kw_call_dict_value_0_1;
        PyObject *tmp_kw_call_dict_value_1_1;
        tmp_expression_value_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_3 == NULL)) {
            tmp_expression_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;

            goto try_except_handler_4;
        }
        tmp_called_value_2 = LOOKUP_ATTRIBUTE(tmp_expression_value_3, mod_consts[69]);
        if (tmp_called_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;

            goto try_except_handler_4;
        }
        tmp_kw_call_arg_value_0_1 = mod_consts[70];
        tmp_kw_call_arg_value_1_1 = Py_True;
        tmp_kw_call_arg_value_2_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[57]);

        if (unlikely(tmp_kw_call_arg_value_2_1 == NULL)) {
            tmp_kw_call_arg_value_2_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[57]);
        }

        if (tmp_kw_call_arg_value_2_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_2);

            exception_lineno = 74;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_0_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_1 == NULL)) {
            tmp_kw_call_dict_value_0_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_2);

            exception_lineno = 75;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_1_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[58]);

        if (unlikely(tmp_kw_call_dict_value_1_1 == NULL)) {
            tmp_kw_call_dict_value_1_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[58]);
        }

        if (tmp_kw_call_dict_value_1_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_2);

            exception_lineno = 76;

            goto try_except_handler_4;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 71;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_1, tmp_kw_call_arg_value_1_1, tmp_kw_call_arg_value_2_1};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_1, tmp_kw_call_dict_value_1_1};
            tmp_call_result_1 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_2, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_2);
        if (tmp_call_result_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 71;

            goto try_except_handler_4;
        }
        Py_DECREF(tmp_call_result_1);
    }
    {
        PyObject *tmp_called_value_3;
        PyObject *tmp_expression_value_4;
        PyObject *tmp_call_result_2;
        PyObject *tmp_kw_call_arg_value_0_2;
        PyObject *tmp_kw_call_arg_value_1_2;
        PyObject *tmp_kw_call_arg_value_2_2;
        PyObject *tmp_kw_call_dict_value_0_2;
        PyObject *tmp_kw_call_dict_value_1_2;
        tmp_expression_value_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_4 == NULL)) {
            tmp_expression_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;

            goto try_except_handler_4;
        }
        tmp_called_value_3 = LOOKUP_ATTRIBUTE(tmp_expression_value_4, mod_consts[69]);
        if (tmp_called_value_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;

            goto try_except_handler_4;
        }
        tmp_kw_call_arg_value_0_2 = mod_consts[72];
        tmp_kw_call_arg_value_1_2 = Py_True;
        tmp_kw_call_arg_value_2_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[60]);

        if (unlikely(tmp_kw_call_arg_value_2_2 == NULL)) {
            tmp_kw_call_arg_value_2_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[60]);
        }

        if (tmp_kw_call_arg_value_2_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_3);

            exception_lineno = 79;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_0_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_2 == NULL)) {
            tmp_kw_call_dict_value_0_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_3);

            exception_lineno = 79;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_1_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[61]);

        if (unlikely(tmp_kw_call_dict_value_1_2 == NULL)) {
            tmp_kw_call_dict_value_1_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[61]);
        }

        if (tmp_kw_call_dict_value_1_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_3);

            exception_lineno = 79;

            goto try_except_handler_4;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 78;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_2, tmp_kw_call_arg_value_1_2, tmp_kw_call_arg_value_2_2};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_2, tmp_kw_call_dict_value_1_2};
            tmp_call_result_2 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_3, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_3);
        if (tmp_call_result_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 78;

            goto try_except_handler_4;
        }
        Py_DECREF(tmp_call_result_2);
    }
    {
        PyObject *tmp_called_value_4;
        PyObject *tmp_expression_value_5;
        PyObject *tmp_call_result_3;
        PyObject *tmp_kw_call_arg_value_0_3;
        PyObject *tmp_kw_call_arg_value_1_3;
        PyObject *tmp_kw_call_arg_value_2_3;
        PyObject *tmp_kw_call_dict_value_0_3;
        PyObject *tmp_kw_call_dict_value_1_3;
        tmp_expression_value_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_5 == NULL)) {
            tmp_expression_value_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 81;

            goto try_except_handler_4;
        }
        tmp_called_value_4 = LOOKUP_ATTRIBUTE(tmp_expression_value_5, mod_consts[69]);
        if (tmp_called_value_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 81;

            goto try_except_handler_4;
        }
        tmp_kw_call_arg_value_0_3 = mod_consts[73];
        tmp_kw_call_arg_value_1_3 = Py_False;
        tmp_kw_call_arg_value_2_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[63]);

        if (unlikely(tmp_kw_call_arg_value_2_3 == NULL)) {
            tmp_kw_call_arg_value_2_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[63]);
        }

        if (tmp_kw_call_arg_value_2_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_4);

            exception_lineno = 82;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_0_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_3 == NULL)) {
            tmp_kw_call_dict_value_0_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_4);

            exception_lineno = 82;

            goto try_except_handler_4;
        }
        tmp_kw_call_dict_value_1_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[64]);

        if (unlikely(tmp_kw_call_dict_value_1_3 == NULL)) {
            tmp_kw_call_dict_value_1_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[64]);
        }

        if (tmp_kw_call_dict_value_1_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_4);

            exception_lineno = 82;

            goto try_except_handler_4;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 81;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_3, tmp_kw_call_arg_value_1_3, tmp_kw_call_arg_value_2_3};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_3, tmp_kw_call_dict_value_1_3};
            tmp_call_result_3 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_4, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_4);
        if (tmp_call_result_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 81;

            goto try_except_handler_4;
        }
        Py_DECREF(tmp_call_result_3);
    }
    goto try_end_2;
    // Exception handler code:
    try_except_handler_4:;
    exception_keeper_type_2 = exception_type;
    exception_keeper_value_2 = exception_value;
    exception_keeper_tb_2 = exception_tb;
    exception_keeper_lineno_2 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 1.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_1, &exception_preserved_value_1, &exception_preserved_tb_1);

    if (exception_keeper_tb_2 == NULL) {
        exception_keeper_tb_2 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_2);
    } else if (exception_keeper_lineno_2 != 0) {
        exception_keeper_tb_2 = ADD_TRACEBACK(exception_keeper_tb_2, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_2);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_2, &exception_keeper_value_2, &exception_keeper_tb_2);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_2, exception_keeper_tb_2);
    PUBLISH_EXCEPTION(&exception_keeper_type_2, &exception_keeper_value_2, &exception_keeper_tb_2);
    // Tried code:
    {
        bool tmp_condition_result_1;
        PyObject *tmp_cmp_expr_left_1;
        PyObject *tmp_cmp_expr_right_1;
        tmp_cmp_expr_left_1 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_1 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_1, tmp_cmp_expr_right_1);
        assert(!(tmp_res == -1));
        tmp_condition_result_1 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_1 != false) {
            goto branch_yes_1;
        } else {
            goto branch_no_1;
        }
    }
    branch_yes_1:;
    {
        nuitka_bool tmp_assign_source_25;
        tmp_assign_source_25 = NUITKA_BOOL_FALSE;
        tmp_with_1__indicator = tmp_assign_source_25;
    }
    {
        bool tmp_condition_result_2;
        PyObject *tmp_operand_value_1;
        PyObject *tmp_called_value_5;
        PyObject *tmp_args_element_value_1;
        PyObject *tmp_args_element_value_2;
        PyObject *tmp_args_element_value_3;
        CHECK_OBJECT(tmp_with_1__exit);
        tmp_called_value_5 = tmp_with_1__exit;
        tmp_args_element_value_1 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_2 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_3 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 82;
        {
            PyObject *call_args[] = {tmp_args_element_value_1, tmp_args_element_value_2, tmp_args_element_value_3};
            tmp_operand_value_1 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_5, call_args);
        }

        if (tmp_operand_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;

            goto try_except_handler_5;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_1);
        Py_DECREF(tmp_operand_value_1);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;

            goto try_except_handler_5;
        }
        tmp_condition_result_2 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_2 != false) {
            goto branch_yes_2;
        } else {
            goto branch_no_2;
        }
    }
    branch_yes_2:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 82;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_5;
    branch_no_2:;
    goto branch_end_1;
    branch_no_1:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 70;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_5;
    branch_end_1:;
    goto try_end_3;
    // Exception handler code:
    try_except_handler_5:;
    exception_keeper_type_3 = exception_type;
    exception_keeper_value_3 = exception_value;
    exception_keeper_tb_3 = exception_tb;
    exception_keeper_lineno_3 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 1.
    SET_CURRENT_EXCEPTION(exception_preserved_type_1, exception_preserved_value_1, exception_preserved_tb_1);

    // Re-raise.
    exception_type = exception_keeper_type_3;
    exception_value = exception_keeper_value_3;
    exception_tb = exception_keeper_tb_3;
    exception_lineno = exception_keeper_lineno_3;

    goto try_except_handler_3;
    // End of try:
    try_end_3:;
    // Restore previous exception id 1.
    SET_CURRENT_EXCEPTION(exception_preserved_type_1, exception_preserved_value_1, exception_preserved_tb_1);

    goto try_end_2;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_2:;
    goto try_end_4;
    // Exception handler code:
    try_except_handler_3:;
    exception_keeper_type_4 = exception_type;
    exception_keeper_value_4 = exception_value;
    exception_keeper_tb_4 = exception_tb;
    exception_keeper_lineno_4 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_3;
        nuitka_bool tmp_cmp_expr_left_2;
        nuitka_bool tmp_cmp_expr_right_2;
        assert(tmp_with_1__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_2 = tmp_with_1__indicator;
        tmp_cmp_expr_right_2 = NUITKA_BOOL_TRUE;
        tmp_condition_result_3 = (tmp_cmp_expr_left_2 == tmp_cmp_expr_right_2) ? true : false;
        if (tmp_condition_result_3 != false) {
            goto branch_yes_3;
        } else {
            goto branch_no_3;
        }
    }
    branch_yes_3:;
    {
        PyObject *tmp_called_value_6;
        PyObject *tmp_call_result_4;
        CHECK_OBJECT(tmp_with_1__exit);
        tmp_called_value_6 = tmp_with_1__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 82;
        tmp_call_result_4 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_6, mod_consts[74]);

        if (tmp_call_result_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_4);
            Py_XDECREF(exception_keeper_value_4);
            Py_XDECREF(exception_keeper_tb_4);

            exception_lineno = 82;

            goto try_except_handler_2;
        }
        Py_DECREF(tmp_call_result_4);
    }
    branch_no_3:;
    // Re-raise.
    exception_type = exception_keeper_type_4;
    exception_value = exception_keeper_value_4;
    exception_tb = exception_keeper_tb_4;
    exception_lineno = exception_keeper_lineno_4;

    goto try_except_handler_2;
    // End of try:
    try_end_4:;
    {
        bool tmp_condition_result_4;
        nuitka_bool tmp_cmp_expr_left_3;
        nuitka_bool tmp_cmp_expr_right_3;
        assert(tmp_with_1__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_3 = tmp_with_1__indicator;
        tmp_cmp_expr_right_3 = NUITKA_BOOL_TRUE;
        tmp_condition_result_4 = (tmp_cmp_expr_left_3 == tmp_cmp_expr_right_3) ? true : false;
        if (tmp_condition_result_4 != false) {
            goto branch_yes_4;
        } else {
            goto branch_no_4;
        }
    }
    branch_yes_4:;
    {
        PyObject *tmp_called_value_7;
        PyObject *tmp_call_result_5;
        CHECK_OBJECT(tmp_with_1__exit);
        tmp_called_value_7 = tmp_with_1__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 82;
        tmp_call_result_5 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_7, mod_consts[74]);

        if (tmp_call_result_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 82;

            goto try_except_handler_2;
        }
        Py_DECREF(tmp_call_result_5);
    }
    branch_no_4:;
    goto try_end_5;
    // Exception handler code:
    try_except_handler_2:;
    exception_keeper_type_5 = exception_type;
    exception_keeper_value_5 = exception_value;
    exception_keeper_tb_5 = exception_tb;
    exception_keeper_lineno_5 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_1__source);
    tmp_with_1__source = NULL;
    Py_XDECREF(tmp_with_1__enter);
    tmp_with_1__enter = NULL;
    Py_XDECREF(tmp_with_1__exit);
    tmp_with_1__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_5;
    exception_value = exception_keeper_value_5;
    exception_tb = exception_keeper_tb_5;
    exception_lineno = exception_keeper_lineno_5;

    goto frame_exception_exit_1;
    // End of try:
    try_end_5:;
    CHECK_OBJECT(tmp_with_1__source);
    Py_DECREF(tmp_with_1__source);
    tmp_with_1__source = NULL;
    CHECK_OBJECT(tmp_with_1__enter);
    Py_DECREF(tmp_with_1__enter);
    tmp_with_1__enter = NULL;
    Py_XDECREF(tmp_with_1__exit);
    tmp_with_1__exit = NULL;
    {
        PyObject *tmp_assign_source_26;
        tmp_assign_source_26 = mod_consts[75];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[76], tmp_assign_source_26);
    }
    {
        PyObject *tmp_assign_source_27;
        tmp_assign_source_27 = mod_consts[77];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[78], tmp_assign_source_27);
    }
    {
        PyObject *tmp_assign_source_28;
        tmp_assign_source_28 = mod_consts[79];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[80], tmp_assign_source_28);
    }
    {
        PyObject *tmp_assign_source_29;
        tmp_assign_source_29 = mod_consts[81];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[82], tmp_assign_source_29);
    }
    {
        PyObject *tmp_assign_source_30;
        tmp_assign_source_30 = mod_consts[83];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[84], tmp_assign_source_30);
    }
    {
        PyObject *tmp_assign_source_31;
        tmp_assign_source_31 = mod_consts[85];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[86], tmp_assign_source_31);
    }
    {
        PyObject *tmp_assign_source_32;
        tmp_assign_source_32 = mod_consts[87];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[88], tmp_assign_source_32);
    }
    {
        PyObject *tmp_assign_source_33;
        tmp_assign_source_33 = mod_consts[89];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[90], tmp_assign_source_33);
    }
    {
        PyObject *tmp_assign_source_34;
        tmp_assign_source_34 = mod_consts[91];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[92], tmp_assign_source_34);
    }
    {
        PyObject *tmp_assign_source_35;
        tmp_assign_source_35 = mod_consts[93];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[94], tmp_assign_source_35);
    }
    {
        PyObject *tmp_assign_source_36;
        tmp_assign_source_36 = mod_consts[95];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[96], tmp_assign_source_36);
    }
    {
        PyObject *tmp_assign_source_37;
        tmp_assign_source_37 = mod_consts[97];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[98], tmp_assign_source_37);
    }
    {
        PyObject *tmp_assign_source_38;
        tmp_assign_source_38 = mod_consts[99];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[100], tmp_assign_source_38);
    }
    {
        PyObject *tmp_assign_source_39;
        tmp_assign_source_39 = mod_consts[101];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[102], tmp_assign_source_39);
    }
    {
        PyObject *tmp_assign_source_40;
        tmp_assign_source_40 = mod_consts[103];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[104], tmp_assign_source_40);
    }
    {
        PyObject *tmp_assign_source_41;
        tmp_assign_source_41 = mod_consts[105];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[106], tmp_assign_source_41);
    }
    {
        PyObject *tmp_assign_source_42;
        tmp_assign_source_42 = mod_consts[107];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[108], tmp_assign_source_42);
    }
    {
        PyObject *tmp_assign_source_43;
        tmp_assign_source_43 = mod_consts[109];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[110], tmp_assign_source_43);
    }
    {
        PyObject *tmp_assign_source_44;
        tmp_assign_source_44 = mod_consts[111];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[112], tmp_assign_source_44);
    }
    {
        PyObject *tmp_assign_source_45;
        tmp_assign_source_45 = mod_consts[113];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[114], tmp_assign_source_45);
    }
    {
        PyObject *tmp_assign_source_46;
        tmp_assign_source_46 = mod_consts[115];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[116], tmp_assign_source_46);
    }
    {
        PyObject *tmp_assign_source_47;
        tmp_assign_source_47 = mod_consts[117];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[118], tmp_assign_source_47);
    }
    {
        PyObject *tmp_assign_source_48;
        tmp_assign_source_48 = mod_consts[119];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[120], tmp_assign_source_48);
    }
    {
        PyObject *tmp_assign_source_49;
        tmp_assign_source_49 = mod_consts[121];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[122], tmp_assign_source_49);
    }
    {
        PyObject *tmp_assign_source_50;
        tmp_assign_source_50 = mod_consts[123];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[124], tmp_assign_source_50);
    }
    {
        PyObject *tmp_assign_source_51;
        tmp_assign_source_51 = mod_consts[125];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[126], tmp_assign_source_51);
    }
    {
        PyObject *tmp_assign_source_52;
        tmp_assign_source_52 = mod_consts[127];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[128], tmp_assign_source_52);
    }
    {
        PyObject *tmp_assign_source_53;
        tmp_assign_source_53 = mod_consts[129];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[130], tmp_assign_source_53);
    }
    {
        PyObject *tmp_assign_source_54;
        tmp_assign_source_54 = mod_consts[131];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[132], tmp_assign_source_54);
    }
    {
        PyObject *tmp_assign_source_55;
        tmp_assign_source_55 = mod_consts[133];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[134], tmp_assign_source_55);
    }
    {
        PyObject *tmp_assign_source_56;
        tmp_assign_source_56 = mod_consts[135];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[136], tmp_assign_source_56);
    }
    {
        PyObject *tmp_assign_source_57;
        tmp_assign_source_57 = mod_consts[137];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[138], tmp_assign_source_57);
    }
    {
        PyObject *tmp_assign_source_58;


        tmp_assign_source_58 = MAKE_FUNCTION_pandas$core$config_init$$$function__4_table_schema_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[139], tmp_assign_source_58);
    }
    {
        PyObject *tmp_assign_source_59;
        PyObject *tmp_annotations_1;
        tmp_annotations_1 = PyDict_Copy(mod_consts[140]);


        tmp_assign_source_59 = MAKE_FUNCTION_pandas$core$config_init$$$function__5_is_terminal(tmp_annotations_1);

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[141], tmp_assign_source_59);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_60;
        PyObject *tmp_called_instance_2;
        tmp_called_instance_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_2 == NULL)) {
            tmp_called_instance_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 342;

            goto try_except_handler_6;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 342;
        tmp_assign_source_60 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_2,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[142], 0)
        );

        if (tmp_assign_source_60 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 342;

            goto try_except_handler_6;
        }
        assert(tmp_with_2__source == NULL);
        tmp_with_2__source = tmp_assign_source_60;
    }
    {
        PyObject *tmp_assign_source_61;
        PyObject *tmp_called_value_8;
        PyObject *tmp_expression_value_6;
        CHECK_OBJECT(tmp_with_2__source);
        tmp_expression_value_6 = tmp_with_2__source;
        tmp_called_value_8 = LOOKUP_SPECIAL(tmp_expression_value_6, mod_consts[67]);
        if (tmp_called_value_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 342;

            goto try_except_handler_6;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 342;
        tmp_assign_source_61 = CALL_FUNCTION_NO_ARGS(tmp_called_value_8);
        Py_DECREF(tmp_called_value_8);
        if (tmp_assign_source_61 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 342;

            goto try_except_handler_6;
        }
        assert(tmp_with_2__enter == NULL);
        tmp_with_2__enter = tmp_assign_source_61;
    }
    {
        PyObject *tmp_assign_source_62;
        PyObject *tmp_expression_value_7;
        CHECK_OBJECT(tmp_with_2__source);
        tmp_expression_value_7 = tmp_with_2__source;
        tmp_assign_source_62 = LOOKUP_SPECIAL(tmp_expression_value_7, mod_consts[68]);
        if (tmp_assign_source_62 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 342;

            goto try_except_handler_6;
        }
        assert(tmp_with_2__exit == NULL);
        tmp_with_2__exit = tmp_assign_source_62;
    }
    {
        nuitka_bool tmp_assign_source_63;
        tmp_assign_source_63 = NUITKA_BOOL_TRUE;
        tmp_with_2__indicator = tmp_assign_source_63;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_9;
        PyObject *tmp_expression_value_8;
        PyObject *tmp_call_result_6;
        PyObject *tmp_kw_call_arg_value_0_4;
        PyObject *tmp_kw_call_arg_value_1_4;
        PyObject *tmp_kw_call_arg_value_2_4;
        PyObject *tmp_kw_call_dict_value_0_4;
        tmp_expression_value_8 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_8 == NULL)) {
            tmp_expression_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 343;

            goto try_except_handler_8;
        }
        tmp_called_value_9 = LOOKUP_ATTRIBUTE(tmp_expression_value_8, mod_consts[69]);
        if (tmp_called_value_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 343;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_4 = mod_consts[143];
        tmp_kw_call_arg_value_1_4 = mod_consts[144];
        tmp_kw_call_arg_value_2_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[76]);

        if (unlikely(tmp_kw_call_arg_value_2_4 == NULL)) {
            tmp_kw_call_arg_value_2_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[76]);
        }

        if (tmp_kw_call_arg_value_2_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_9);

            exception_lineno = 343;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[53]);

        if (unlikely(tmp_kw_call_dict_value_0_4 == NULL)) {
            tmp_kw_call_dict_value_0_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[53]);
        }

        if (tmp_kw_call_dict_value_0_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_9);

            exception_lineno = 343;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 343;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_4, tmp_kw_call_arg_value_1_4, tmp_kw_call_arg_value_2_4};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_4};
            tmp_call_result_6 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_9, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_9);
        if (tmp_call_result_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 343;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_6);
    }
    {
        PyObject *tmp_called_value_10;
        PyObject *tmp_expression_value_9;
        PyObject *tmp_call_result_7;
        PyObject *tmp_kw_call_arg_value_0_5;
        PyObject *tmp_kw_call_arg_value_1_5;
        PyObject *tmp_kw_call_arg_value_2_5;
        PyObject *tmp_kw_call_dict_value_0_5;
        PyObject *tmp_called_value_11;
        PyObject *tmp_args_element_value_4;
        PyObject *tmp_list_element_1;
        tmp_expression_value_9 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_9 == NULL)) {
            tmp_expression_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 344;

            goto try_except_handler_8;
        }
        tmp_called_value_10 = LOOKUP_ATTRIBUTE(tmp_expression_value_9, mod_consts[69]);
        if (tmp_called_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 344;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_5 = mod_consts[146];
        tmp_kw_call_arg_value_1_5 = Py_None;
        tmp_kw_call_arg_value_2_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[96]);

        if (unlikely(tmp_kw_call_arg_value_2_5 == NULL)) {
            tmp_kw_call_arg_value_2_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[96]);
        }

        if (tmp_kw_call_arg_value_2_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 347;

            goto try_except_handler_8;
        }
        tmp_called_value_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_11 == NULL)) {
            tmp_called_value_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 348;

            goto try_except_handler_8;
        }
        tmp_list_element_1 = Py_None;
        tmp_args_element_value_4 = PyList_New(2);
        PyList_SET_ITEM0(tmp_args_element_value_4, 0, tmp_list_element_1);
        tmp_list_element_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[50]);

        if (unlikely(tmp_list_element_1 == NULL)) {
            tmp_list_element_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[50]);
        }

        if (tmp_list_element_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 348;

            goto list_build_exception_1;
        }
        PyList_SET_ITEM0(tmp_args_element_value_4, 1, tmp_list_element_1);
        goto list_build_noexception_1;
        // Exception handling pass through code for list_build:
        list_build_exception_1:;
        Py_DECREF(tmp_called_value_10);
        Py_DECREF(tmp_args_element_value_4);
        goto try_except_handler_8;
        // Finished with no exception for list_build:
        list_build_noexception_1:;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 348;
        tmp_kw_call_dict_value_0_5 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_11, tmp_args_element_value_4);
        Py_DECREF(tmp_args_element_value_4);
        if (tmp_kw_call_dict_value_0_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_10);

            exception_lineno = 348;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 344;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_5, tmp_kw_call_arg_value_1_5, tmp_kw_call_arg_value_2_5};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_5};
            tmp_call_result_7 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_10, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_10);
        Py_DECREF(tmp_kw_call_dict_value_0_5);
        if (tmp_call_result_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 344;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_7);
    }
    {
        PyObject *tmp_called_value_12;
        PyObject *tmp_expression_value_10;
        PyObject *tmp_call_result_8;
        PyObject *tmp_kw_call_value_0_1;
        tmp_expression_value_10 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_10 == NULL)) {
            tmp_expression_value_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 350;

            goto try_except_handler_8;
        }
        tmp_called_value_12 = LOOKUP_ATTRIBUTE(tmp_expression_value_10, mod_consts[69]);
        if (tmp_called_value_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 350;

            goto try_except_handler_8;
        }
        tmp_kw_call_value_0_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52]);

        if (unlikely(tmp_kw_call_value_0_1 == NULL)) {
            tmp_kw_call_value_0_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[52]);
        }

        if (tmp_kw_call_value_0_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_12);

            exception_lineno = 350;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 350;
        {
            PyObject *kw_values[1] = {tmp_kw_call_value_0_1};
            tmp_call_result_8 = CALL_FUNCTION_WITH_POSARGS2_KWSPLIT(tmp_called_value_12, mod_consts[147], kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_12);
        if (tmp_call_result_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 350;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_8);
    }
    {
        PyObject *tmp_called_value_13;
        PyObject *tmp_expression_value_11;
        PyObject *tmp_call_result_9;
        PyObject *tmp_kw_call_arg_value_0_6;
        PyObject *tmp_kw_call_arg_value_1_6;
        PyObject *tmp_kw_call_arg_value_2_6;
        PyObject *tmp_kw_call_dict_value_0_6;
        PyObject *tmp_called_value_14;
        tmp_expression_value_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_11 == NULL)) {
            tmp_expression_value_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 351;

            goto try_except_handler_8;
        }
        tmp_called_value_13 = LOOKUP_ATTRIBUTE(tmp_expression_value_11, mod_consts[69]);
        if (tmp_called_value_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 351;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_6 = mod_consts[148];
        tmp_kw_call_arg_value_1_6 = mod_consts[149];
        tmp_kw_call_arg_value_2_6 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[124]);

        if (unlikely(tmp_kw_call_arg_value_2_6 == NULL)) {
            tmp_kw_call_arg_value_2_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[124]);
        }

        if (tmp_kw_call_arg_value_2_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_13);

            exception_lineno = 354;

            goto try_except_handler_8;
        }
        tmp_called_value_14 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[51]);

        if (unlikely(tmp_called_value_14 == NULL)) {
            tmp_called_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[51]);
        }

        if (tmp_called_value_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_13);

            exception_lineno = 355;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 355;
        tmp_kw_call_dict_value_0_6 = CALL_FUNCTION_WITH_POSARGS1(tmp_called_value_14, mod_consts[150]);

        if (tmp_kw_call_dict_value_0_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_13);

            exception_lineno = 355;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 351;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_6, tmp_kw_call_arg_value_1_6, tmp_kw_call_arg_value_2_6};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_6};
            tmp_call_result_9 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_13, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_13);
        Py_DECREF(tmp_kw_call_dict_value_0_6);
        if (tmp_call_result_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 351;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_9);
    }
    {
        PyObject *tmp_called_value_15;
        PyObject *tmp_expression_value_12;
        PyObject *tmp_call_result_10;
        PyObject *tmp_kw_call_arg_value_0_7;
        PyObject *tmp_kw_call_arg_value_1_7;
        PyObject *tmp_kw_call_arg_value_2_7;
        PyObject *tmp_kw_call_dict_value_0_7;
        tmp_expression_value_12 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_12 == NULL)) {
            tmp_expression_value_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 357;

            goto try_except_handler_8;
        }
        tmp_called_value_15 = LOOKUP_ATTRIBUTE(tmp_expression_value_12, mod_consts[69]);
        if (tmp_called_value_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 357;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_7 = mod_consts[151];
        tmp_kw_call_arg_value_1_7 = mod_consts[152];
        tmp_kw_call_arg_value_2_7 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[80]);

        if (unlikely(tmp_kw_call_arg_value_2_7 == NULL)) {
            tmp_kw_call_arg_value_2_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[80]);
        }

        if (tmp_kw_call_arg_value_2_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_15);

            exception_lineno = 357;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_7 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[53]);

        if (unlikely(tmp_kw_call_dict_value_0_7 == NULL)) {
            tmp_kw_call_dict_value_0_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[53]);
        }

        if (tmp_kw_call_dict_value_0_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_15);

            exception_lineno = 357;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 357;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_7, tmp_kw_call_arg_value_1_7, tmp_kw_call_arg_value_2_7};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_7};
            tmp_call_result_10 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_15, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_15);
        if (tmp_call_result_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 357;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_10);
    }
    {
        PyObject *tmp_called_value_16;
        PyObject *tmp_expression_value_13;
        PyObject *tmp_call_result_11;
        PyObject *tmp_kw_call_arg_value_0_8;
        PyObject *tmp_kw_call_arg_value_1_8;
        PyObject *tmp_kw_call_arg_value_2_8;
        PyObject *tmp_kw_call_dict_value_0_8;
        PyObject *tmp_called_value_17;
        PyObject *tmp_call_arg_element_1;
        tmp_expression_value_13 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_13 == NULL)) {
            tmp_expression_value_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 358;

            goto try_except_handler_8;
        }
        tmp_called_value_16 = LOOKUP_ATTRIBUTE(tmp_expression_value_13, mod_consts[69]);
        if (tmp_called_value_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 358;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_8 = mod_consts[153];
        tmp_kw_call_arg_value_1_8 = mod_consts[154];
        tmp_kw_call_arg_value_2_8 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[82]);

        if (unlikely(tmp_kw_call_arg_value_2_8 == NULL)) {
            tmp_kw_call_arg_value_2_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[82]);
        }

        if (tmp_kw_call_arg_value_2_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 361;

            goto try_except_handler_8;
        }
        tmp_called_value_17 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[51]);

        if (unlikely(tmp_called_value_17 == NULL)) {
            tmp_called_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[51]);
        }

        if (tmp_called_value_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 362;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_1 = LIST_COPY(mod_consts[155]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 362;
        tmp_kw_call_dict_value_0_8 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_17, tmp_call_arg_element_1);
        Py_DECREF(tmp_call_arg_element_1);
        if (tmp_kw_call_dict_value_0_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_16);

            exception_lineno = 362;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 358;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_8, tmp_kw_call_arg_value_1_8, tmp_kw_call_arg_value_2_8};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_8};
            tmp_call_result_11 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_16, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_16);
        Py_DECREF(tmp_kw_call_dict_value_0_8);
        if (tmp_call_result_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 358;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_11);
    }
    {
        PyObject *tmp_called_value_18;
        PyObject *tmp_expression_value_14;
        PyObject *tmp_call_result_12;
        PyObject *tmp_kw_call_arg_value_0_9;
        PyObject *tmp_kw_call_arg_value_1_9;
        PyObject *tmp_kw_call_arg_value_2_9;
        PyObject *tmp_kw_call_dict_value_0_9;
        tmp_expression_value_14 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_14 == NULL)) {
            tmp_expression_value_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 364;

            goto try_except_handler_8;
        }
        tmp_called_value_18 = LOOKUP_ATTRIBUTE(tmp_expression_value_14, mod_consts[69]);
        if (tmp_called_value_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 364;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_9 = mod_consts[156];
        tmp_kw_call_arg_value_1_9 = mod_consts[157];
        tmp_kw_call_arg_value_2_9 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[86]);

        if (unlikely(tmp_kw_call_arg_value_2_9 == NULL)) {
            tmp_kw_call_arg_value_2_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[86]);
        }

        if (tmp_kw_call_arg_value_2_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_18);

            exception_lineno = 364;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_9 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52]);

        if (unlikely(tmp_kw_call_dict_value_0_9 == NULL)) {
            tmp_kw_call_dict_value_0_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[52]);
        }

        if (tmp_kw_call_dict_value_0_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_18);

            exception_lineno = 364;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 364;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_9, tmp_kw_call_arg_value_1_9, tmp_kw_call_arg_value_2_9};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_9};
            tmp_call_result_12 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_18, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_18);
        if (tmp_call_result_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 364;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_12);
    }
    {
        PyObject *tmp_assign_source_64;


        tmp_assign_source_64 = MAKE_FUNCTION_pandas$core$config_init$$$function__6__deprecate_negative_int_max_colwidth();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[158], tmp_assign_source_64);
    }
    {
        PyObject *tmp_called_value_19;
        PyObject *tmp_expression_value_15;
        PyObject *tmp_call_result_13;
        PyObject *tmp_kw_call_arg_value_0_10;
        PyObject *tmp_kw_call_arg_value_1_10;
        PyObject *tmp_kw_call_arg_value_2_10;
        PyObject *tmp_kw_call_dict_value_0_10;
        PyObject *tmp_called_value_20;
        PyObject *tmp_call_arg_element_2;
        PyObject *tmp_kw_call_dict_value_1_4;
        tmp_expression_value_15 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_15 == NULL)) {
            tmp_expression_value_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 377;

            goto try_except_handler_8;
        }
        tmp_called_value_19 = LOOKUP_ATTRIBUTE(tmp_expression_value_15, mod_consts[69]);
        if (tmp_called_value_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 377;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_10 = mod_consts[159];
        tmp_kw_call_arg_value_1_10 = mod_consts[160];
        tmp_kw_call_arg_value_2_10 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[98]);

        if (unlikely(tmp_kw_call_arg_value_2_10 == NULL)) {
            tmp_kw_call_arg_value_2_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[98]);
        }

        if (tmp_kw_call_arg_value_2_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_19);

            exception_lineno = 381;

            goto try_except_handler_8;
        }
        tmp_called_value_20 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[51]);

        if (unlikely(tmp_called_value_20 == NULL)) {
            tmp_called_value_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[51]);
        }

        if (tmp_called_value_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_19);

            exception_lineno = 382;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_2 = LIST_COPY(mod_consts[155]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 382;
        tmp_kw_call_dict_value_0_10 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_20, tmp_call_arg_element_2);
        Py_DECREF(tmp_call_arg_element_2);
        if (tmp_kw_call_dict_value_0_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_19);

            exception_lineno = 382;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_1_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[158]);

        if (unlikely(tmp_kw_call_dict_value_1_4 == NULL)) {
            tmp_kw_call_dict_value_1_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[158]);
        }

        if (tmp_kw_call_dict_value_1_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_19);
            Py_DECREF(tmp_kw_call_dict_value_0_10);

            exception_lineno = 383;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 377;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_10, tmp_kw_call_arg_value_1_10, tmp_kw_call_arg_value_2_10};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_10, tmp_kw_call_dict_value_1_4};
            tmp_call_result_13 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_19, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_19);
        Py_DECREF(tmp_kw_call_dict_value_0_10);
        if (tmp_call_result_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 377;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_13);
    }
    {
        nuitka_bool tmp_condition_result_5;
        PyObject *tmp_called_value_21;
        PyObject *tmp_call_result_14;
        int tmp_truth_name_1;
        tmp_called_value_21 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[141]);

        if (unlikely(tmp_called_value_21 == NULL)) {
            tmp_called_value_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[141]);
        }

        if (tmp_called_value_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 385;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 385;
        tmp_call_result_14 = CALL_FUNCTION_NO_ARGS(tmp_called_value_21);
        if (tmp_call_result_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 385;

            goto try_except_handler_8;
        }
        tmp_truth_name_1 = CHECK_IF_TRUE(tmp_call_result_14);
        if (tmp_truth_name_1 == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_call_result_14);

            exception_lineno = 385;

            goto try_except_handler_8;
        }
        tmp_condition_result_5 = tmp_truth_name_1 == 0 ? NUITKA_BOOL_FALSE : NUITKA_BOOL_TRUE;
        Py_DECREF(tmp_call_result_14);
        if (tmp_condition_result_5 == NUITKA_BOOL_TRUE) {
            goto branch_yes_5;
        } else {
            goto branch_no_5;
        }
    }
    branch_yes_5:;
    {
        PyObject *tmp_assign_source_65;
        tmp_assign_source_65 = mod_consts[2];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[161], tmp_assign_source_65);
    }
    goto branch_end_5;
    branch_no_5:;
    {
        PyObject *tmp_assign_source_66;
        tmp_assign_source_66 = mod_consts[162];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[161], tmp_assign_source_66);
    }
    branch_end_5:;
    {
        PyObject *tmp_called_value_22;
        PyObject *tmp_expression_value_16;
        PyObject *tmp_call_result_15;
        PyObject *tmp_kw_call_arg_value_0_11;
        PyObject *tmp_kw_call_arg_value_1_11;
        PyObject *tmp_kw_call_arg_value_2_11;
        PyObject *tmp_kw_call_dict_value_0_11;
        tmp_expression_value_16 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_16 == NULL)) {
            tmp_expression_value_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 389;

            goto try_except_handler_8;
        }
        tmp_called_value_22 = LOOKUP_ATTRIBUTE(tmp_expression_value_16, mod_consts[69]);
        if (tmp_called_value_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 389;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_11 = mod_consts[163];
        tmp_kw_call_arg_value_1_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[161]);

        if (unlikely(tmp_kw_call_arg_value_1_11 == NULL)) {
            tmp_kw_call_arg_value_1_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[161]);
        }

        if (tmp_kw_call_arg_value_1_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 390;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_2_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[84]);

        if (unlikely(tmp_kw_call_arg_value_2_11 == NULL)) {
            tmp_kw_call_arg_value_2_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[84]);
        }

        if (tmp_kw_call_arg_value_2_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 390;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[53]);

        if (unlikely(tmp_kw_call_dict_value_0_11 == NULL)) {
            tmp_kw_call_dict_value_0_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[53]);
        }

        if (tmp_kw_call_dict_value_0_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_22);

            exception_lineno = 390;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 389;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_11, tmp_kw_call_arg_value_1_11, tmp_kw_call_arg_value_2_11};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_11};
            tmp_call_result_15 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_22, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_22);
        if (tmp_call_result_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 389;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_15);
    }
    {
        PyObject *tmp_called_value_23;
        PyObject *tmp_expression_value_17;
        PyObject *tmp_call_result_16;
        PyObject *tmp_kw_call_arg_value_0_12;
        PyObject *tmp_kw_call_arg_value_1_12;
        PyObject *tmp_kw_call_arg_value_2_12;
        PyObject *tmp_kw_call_dict_value_0_12;
        PyObject *tmp_called_value_24;
        PyObject *tmp_call_arg_element_3;
        tmp_expression_value_17 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_17 == NULL)) {
            tmp_expression_value_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 392;

            goto try_except_handler_8;
        }
        tmp_called_value_23 = LOOKUP_ATTRIBUTE(tmp_expression_value_17, mod_consts[69]);
        if (tmp_called_value_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 392;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_12 = mod_consts[164];
        tmp_kw_call_arg_value_1_12 = mod_consts[165];
        tmp_kw_call_arg_value_2_12 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[126]);

        if (unlikely(tmp_kw_call_arg_value_2_12 == NULL)) {
            tmp_kw_call_arg_value_2_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[126]);
        }

        if (tmp_kw_call_arg_value_2_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_23);

            exception_lineno = 395;

            goto try_except_handler_8;
        }
        tmp_called_value_24 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_24 == NULL)) {
            tmp_called_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_24 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_23);

            exception_lineno = 396;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_3 = LIST_COPY(mod_consts[166]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 396;
        tmp_kw_call_dict_value_0_12 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_24, tmp_call_arg_element_3);
        Py_DECREF(tmp_call_arg_element_3);
        if (tmp_kw_call_dict_value_0_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_23);

            exception_lineno = 396;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 392;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_12, tmp_kw_call_arg_value_1_12, tmp_kw_call_arg_value_2_12};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_12};
            tmp_call_result_16 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_23, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_23);
        Py_DECREF(tmp_kw_call_dict_value_0_12);
        if (tmp_call_result_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 392;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_16);
    }
    {
        PyObject *tmp_called_value_25;
        PyObject *tmp_expression_value_18;
        PyObject *tmp_call_result_17;
        PyObject *tmp_kw_call_arg_value_0_13;
        PyObject *tmp_kw_call_arg_value_1_13;
        PyObject *tmp_kw_call_arg_value_2_13;
        PyObject *tmp_kw_call_dict_value_0_13;
        tmp_expression_value_18 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_18 == NULL)) {
            tmp_expression_value_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 398;

            goto try_except_handler_8;
        }
        tmp_called_value_25 = LOOKUP_ATTRIBUTE(tmp_expression_value_18, mod_consts[69]);
        if (tmp_called_value_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 398;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_13 = mod_consts[167];
        tmp_kw_call_arg_value_1_13 = mod_consts[168];
        tmp_kw_call_arg_value_2_13 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[88]);

        if (unlikely(tmp_kw_call_arg_value_2_13 == NULL)) {
            tmp_kw_call_arg_value_2_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[88]);
        }

        if (tmp_kw_call_arg_value_2_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_25);

            exception_lineno = 398;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_13 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52]);

        if (unlikely(tmp_kw_call_dict_value_0_13 == NULL)) {
            tmp_kw_call_dict_value_0_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[52]);
        }

        if (tmp_kw_call_dict_value_0_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_25);

            exception_lineno = 398;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 398;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_13, tmp_kw_call_arg_value_1_13, tmp_kw_call_arg_value_2_13};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_13};
            tmp_call_result_17 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_25, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_25);
        if (tmp_call_result_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 398;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_17);
    }
    {
        PyObject *tmp_called_value_26;
        PyObject *tmp_expression_value_19;
        PyObject *tmp_call_result_18;
        PyObject *tmp_kw_call_arg_value_0_14;
        PyObject *tmp_kw_call_arg_value_1_14;
        PyObject *tmp_kw_call_arg_value_2_14;
        PyObject *tmp_kw_call_dict_value_0_14;
        tmp_expression_value_19 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_19 == NULL)) {
            tmp_expression_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 399;

            goto try_except_handler_8;
        }
        tmp_called_value_26 = LOOKUP_ATTRIBUTE(tmp_expression_value_19, mod_consts[69]);
        if (tmp_called_value_26 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 399;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_14 = mod_consts[169];
        tmp_kw_call_arg_value_1_14 = mod_consts[170];
        tmp_kw_call_arg_value_2_14 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[100]);

        if (unlikely(tmp_kw_call_arg_value_2_14 == NULL)) {
            tmp_kw_call_arg_value_2_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[100]);
        }

        if (tmp_kw_call_arg_value_2_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_26);

            exception_lineno = 400;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_14 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[55]);

        if (unlikely(tmp_kw_call_dict_value_0_14 == NULL)) {
            tmp_kw_call_dict_value_0_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[55]);
        }

        if (tmp_kw_call_dict_value_0_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_26);

            exception_lineno = 400;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 399;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_14, tmp_kw_call_arg_value_1_14, tmp_kw_call_arg_value_2_14};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_14};
            tmp_call_result_18 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_26, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_26);
        if (tmp_call_result_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 399;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_18);
    }
    {
        PyObject *tmp_called_value_27;
        PyObject *tmp_expression_value_20;
        PyObject *tmp_call_result_19;
        PyObject *tmp_kw_call_arg_value_0_15;
        PyObject *tmp_kw_call_arg_value_1_15;
        PyObject *tmp_kw_call_arg_value_2_15;
        PyObject *tmp_kw_call_dict_value_0_15;
        tmp_expression_value_20 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_20 == NULL)) {
            tmp_expression_value_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 402;

            goto try_except_handler_8;
        }
        tmp_called_value_27 = LOOKUP_ATTRIBUTE(tmp_expression_value_20, mod_consts[69]);
        if (tmp_called_value_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 402;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_15 = mod_consts[171];
        tmp_kw_call_arg_value_1_15 = Py_True;
        tmp_kw_call_arg_value_2_15 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[90]);

        if (unlikely(tmp_kw_call_arg_value_2_15 == NULL)) {
            tmp_kw_call_arg_value_2_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[90]);
        }

        if (tmp_kw_call_arg_value_2_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_27);

            exception_lineno = 402;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_15 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_15 == NULL)) {
            tmp_kw_call_dict_value_0_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_27);

            exception_lineno = 402;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 402;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_15, tmp_kw_call_arg_value_1_15, tmp_kw_call_arg_value_2_15};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_15};
            tmp_call_result_19 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_27, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_27);
        if (tmp_call_result_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 402;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_19);
    }
    {
        PyObject *tmp_called_value_28;
        PyObject *tmp_expression_value_21;
        PyObject *tmp_call_result_20;
        PyObject *tmp_kw_call_arg_value_0_16;
        PyObject *tmp_kw_call_arg_value_1_16;
        PyObject *tmp_kw_call_arg_value_2_16;
        PyObject *tmp_kw_call_dict_value_0_16;
        tmp_expression_value_21 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_21 == NULL)) {
            tmp_expression_value_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 403;

            goto try_except_handler_8;
        }
        tmp_called_value_28 = LOOKUP_ATTRIBUTE(tmp_expression_value_21, mod_consts[69]);
        if (tmp_called_value_28 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 403;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_16 = mod_consts[172];
        tmp_kw_call_arg_value_1_16 = mod_consts[173];
        tmp_kw_call_arg_value_2_16 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[92]);

        if (unlikely(tmp_kw_call_arg_value_2_16 == NULL)) {
            tmp_kw_call_arg_value_2_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[92]);
        }

        if (tmp_kw_call_arg_value_2_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_28);

            exception_lineno = 403;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_16 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52]);

        if (unlikely(tmp_kw_call_dict_value_0_16 == NULL)) {
            tmp_kw_call_dict_value_0_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[52]);
        }

        if (tmp_kw_call_dict_value_0_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_28);

            exception_lineno = 403;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 403;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_16, tmp_kw_call_arg_value_1_16, tmp_kw_call_arg_value_2_16};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_16};
            tmp_call_result_20 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_28, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_28);
        if (tmp_call_result_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 403;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_20);
    }
    {
        PyObject *tmp_called_value_29;
        PyObject *tmp_expression_value_22;
        PyObject *tmp_call_result_21;
        PyObject *tmp_kw_call_arg_value_0_17;
        PyObject *tmp_kw_call_arg_value_1_17;
        PyObject *tmp_kw_call_arg_value_2_17;
        PyObject *tmp_kw_call_dict_value_0_17;
        tmp_expression_value_22 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_22 == NULL)) {
            tmp_expression_value_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 404;

            goto try_except_handler_8;
        }
        tmp_called_value_29 = LOOKUP_ATTRIBUTE(tmp_expression_value_22, mod_consts[69]);
        if (tmp_called_value_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 404;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_17 = mod_consts[174];
        tmp_kw_call_arg_value_1_17 = Py_True;
        tmp_kw_call_arg_value_2_17 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[94]);

        if (unlikely(tmp_kw_call_arg_value_2_17 == NULL)) {
            tmp_kw_call_arg_value_2_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[94]);
        }

        if (tmp_kw_call_arg_value_2_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_29);

            exception_lineno = 404;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_17 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_17 == NULL)) {
            tmp_kw_call_dict_value_0_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_29);

            exception_lineno = 404;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 404;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_17, tmp_kw_call_arg_value_1_17, tmp_kw_call_arg_value_2_17};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_17};
            tmp_call_result_21 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_29, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_29);
        if (tmp_call_result_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 404;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_21);
    }
    {
        PyObject *tmp_called_value_30;
        PyObject *tmp_expression_value_23;
        PyObject *tmp_call_result_22;
        PyObject *tmp_args_element_value_5;
        PyObject *tmp_args_element_value_6;
        PyObject *tmp_args_element_value_7;
        tmp_expression_value_23 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_23 == NULL)) {
            tmp_expression_value_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 405;

            goto try_except_handler_8;
        }
        tmp_called_value_30 = LOOKUP_ATTRIBUTE(tmp_expression_value_23, mod_consts[69]);
        if (tmp_called_value_30 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 405;

            goto try_except_handler_8;
        }
        tmp_args_element_value_5 = mod_consts[175];
        tmp_args_element_value_6 = Py_True;
        tmp_args_element_value_7 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[102]);

        if (unlikely(tmp_args_element_value_7 == NULL)) {
            tmp_args_element_value_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[102]);
        }

        if (tmp_args_element_value_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_30);

            exception_lineno = 405;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 405;
        {
            PyObject *call_args[] = {tmp_args_element_value_5, tmp_args_element_value_6, tmp_args_element_value_7};
            tmp_call_result_22 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_30, call_args);
        }

        Py_DECREF(tmp_called_value_30);
        if (tmp_call_result_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 405;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_22);
    }
    {
        PyObject *tmp_called_value_31;
        PyObject *tmp_expression_value_24;
        PyObject *tmp_call_result_23;
        PyObject *tmp_kw_call_arg_value_0_18;
        PyObject *tmp_kw_call_arg_value_1_18;
        PyObject *tmp_kw_call_arg_value_2_18;
        PyObject *tmp_kw_call_dict_value_0_18;
        PyObject *tmp_called_value_32;
        PyObject *tmp_call_arg_element_4;
        tmp_expression_value_24 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_24 == NULL)) {
            tmp_expression_value_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_24 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 406;

            goto try_except_handler_8;
        }
        tmp_called_value_31 = LOOKUP_ATTRIBUTE(tmp_expression_value_24, mod_consts[69]);
        if (tmp_called_value_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 406;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_18 = mod_consts[176];
        tmp_kw_call_arg_value_1_18 = mod_consts[165];
        tmp_kw_call_arg_value_2_18 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[104]);

        if (unlikely(tmp_kw_call_arg_value_2_18 == NULL)) {
            tmp_kw_call_arg_value_2_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[104]);
        }

        if (tmp_kw_call_arg_value_2_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_31);

            exception_lineno = 409;

            goto try_except_handler_8;
        }
        tmp_called_value_32 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_32 == NULL)) {
            tmp_called_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_31);

            exception_lineno = 410;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_4 = LIST_COPY(mod_consts[177]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 410;
        tmp_kw_call_dict_value_0_18 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_32, tmp_call_arg_element_4);
        Py_DECREF(tmp_call_arg_element_4);
        if (tmp_kw_call_dict_value_0_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_31);

            exception_lineno = 410;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 406;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_18, tmp_kw_call_arg_value_1_18, tmp_kw_call_arg_value_2_18};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_18};
            tmp_call_result_23 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_31, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_31);
        Py_DECREF(tmp_kw_call_dict_value_0_18);
        if (tmp_call_result_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 406;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_23);
    }
    {
        PyObject *tmp_called_value_33;
        PyObject *tmp_expression_value_25;
        PyObject *tmp_call_result_24;
        PyObject *tmp_args_element_value_8;
        PyObject *tmp_args_element_value_9;
        PyObject *tmp_args_element_value_10;
        tmp_expression_value_25 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_25 == NULL)) {
            tmp_expression_value_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 412;

            goto try_except_handler_8;
        }
        tmp_called_value_33 = LOOKUP_ATTRIBUTE(tmp_expression_value_25, mod_consts[69]);
        if (tmp_called_value_33 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 412;

            goto try_except_handler_8;
        }
        tmp_args_element_value_8 = mod_consts[178];
        tmp_args_element_value_9 = Py_None;
        tmp_args_element_value_10 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[120]);

        if (unlikely(tmp_args_element_value_10 == NULL)) {
            tmp_args_element_value_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[120]);
        }

        if (tmp_args_element_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_33);

            exception_lineno = 412;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 412;
        {
            PyObject *call_args[] = {tmp_args_element_value_8, tmp_args_element_value_9, tmp_args_element_value_10};
            tmp_call_result_24 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_33, call_args);
        }

        Py_DECREF(tmp_called_value_33);
        if (tmp_call_result_24 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 412;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_24);
    }
    {
        PyObject *tmp_called_value_34;
        PyObject *tmp_expression_value_26;
        PyObject *tmp_call_result_25;
        PyObject *tmp_args_element_value_11;
        PyObject *tmp_args_element_value_12;
        PyObject *tmp_args_element_value_13;
        tmp_expression_value_26 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_26 == NULL)) {
            tmp_expression_value_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_26 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 413;

            goto try_except_handler_8;
        }
        tmp_called_value_34 = LOOKUP_ATTRIBUTE(tmp_expression_value_26, mod_consts[69]);
        if (tmp_called_value_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 413;

            goto try_except_handler_8;
        }
        tmp_args_element_value_11 = mod_consts[179];
        tmp_args_element_value_12 = mod_consts[168];
        tmp_args_element_value_13 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[122]);

        if (unlikely(tmp_args_element_value_13 == NULL)) {
            tmp_args_element_value_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[122]);
        }

        if (tmp_args_element_value_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_34);

            exception_lineno = 413;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 413;
        {
            PyObject *call_args[] = {tmp_args_element_value_11, tmp_args_element_value_12, tmp_args_element_value_13};
            tmp_call_result_25 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_34, call_args);
        }

        Py_DECREF(tmp_called_value_34);
        if (tmp_call_result_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 413;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_25);
    }
    {
        PyObject *tmp_called_value_35;
        PyObject *tmp_expression_value_27;
        PyObject *tmp_call_result_26;
        PyObject *tmp_kw_call_arg_value_0_19;
        PyObject *tmp_kw_call_arg_value_1_19;
        PyObject *tmp_kw_call_arg_value_2_19;
        PyObject *tmp_kw_call_dict_value_0_19;
        PyObject *tmp_called_value_36;
        PyObject *tmp_call_arg_element_5;
        tmp_expression_value_27 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_27 == NULL)) {
            tmp_expression_value_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 414;

            goto try_except_handler_8;
        }
        tmp_called_value_35 = LOOKUP_ATTRIBUTE(tmp_expression_value_27, mod_consts[69]);
        if (tmp_called_value_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 414;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_19 = mod_consts[180];
        tmp_kw_call_arg_value_1_19 = mod_consts[181];
        tmp_kw_call_arg_value_2_19 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[118]);

        if (unlikely(tmp_kw_call_arg_value_2_19 == NULL)) {
            tmp_kw_call_arg_value_2_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[118]);
        }

        if (tmp_kw_call_arg_value_2_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_35);

            exception_lineno = 415;

            goto try_except_handler_8;
        }
        tmp_called_value_36 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[51]);

        if (unlikely(tmp_called_value_36 == NULL)) {
            tmp_called_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[51]);
        }

        if (tmp_called_value_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_35);

            exception_lineno = 415;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_5 = LIST_COPY(mod_consts[155]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 415;
        tmp_kw_call_dict_value_0_19 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_36, tmp_call_arg_element_5);
        Py_DECREF(tmp_call_arg_element_5);
        if (tmp_kw_call_dict_value_0_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_35);

            exception_lineno = 415;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 414;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_19, tmp_kw_call_arg_value_1_19, tmp_kw_call_arg_value_2_19};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_19};
            tmp_call_result_26 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_35, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_35);
        Py_DECREF(tmp_kw_call_dict_value_0_19);
        if (tmp_call_result_26 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 414;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_26);
    }
    {
        PyObject *tmp_called_value_37;
        PyObject *tmp_expression_value_28;
        PyObject *tmp_call_result_27;
        PyObject *tmp_kw_call_arg_value_0_20;
        PyObject *tmp_kw_call_arg_value_1_20;
        PyObject *tmp_kw_call_arg_value_2_20;
        PyObject *tmp_kw_call_dict_value_0_20;
        PyObject *tmp_called_value_38;
        PyObject *tmp_call_arg_element_6;
        tmp_expression_value_28 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_28 == NULL)) {
            tmp_expression_value_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_28 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 417;

            goto try_except_handler_8;
        }
        tmp_called_value_37 = LOOKUP_ATTRIBUTE(tmp_expression_value_28, mod_consts[69]);
        if (tmp_called_value_37 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 417;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_20 = mod_consts[182];
        tmp_kw_call_arg_value_1_20 = Py_True;
        tmp_kw_call_arg_value_2_20 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[128]);

        if (unlikely(tmp_kw_call_arg_value_2_20 == NULL)) {
            tmp_kw_call_arg_value_2_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[128]);
        }

        if (tmp_kw_call_arg_value_2_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_37);

            exception_lineno = 420;

            goto try_except_handler_8;
        }
        tmp_called_value_38 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_38 == NULL)) {
            tmp_called_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_37);

            exception_lineno = 421;

            goto try_except_handler_8;
        }
        tmp_call_arg_element_6 = LIST_COPY(mod_consts[183]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 421;
        tmp_kw_call_dict_value_0_20 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_38, tmp_call_arg_element_6);
        Py_DECREF(tmp_call_arg_element_6);
        if (tmp_kw_call_dict_value_0_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_37);

            exception_lineno = 421;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 417;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_20, tmp_kw_call_arg_value_1_20, tmp_kw_call_arg_value_2_20};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_20};
            tmp_call_result_27 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_37, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_37);
        Py_DECREF(tmp_kw_call_dict_value_0_20);
        if (tmp_call_result_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 417;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_27);
    }
    {
        PyObject *tmp_called_value_39;
        PyObject *tmp_expression_value_29;
        PyObject *tmp_call_result_28;
        PyObject *tmp_kw_call_arg_value_0_21;
        PyObject *tmp_kw_call_arg_value_1_21;
        PyObject *tmp_kw_call_arg_value_2_21;
        PyObject *tmp_kw_call_dict_value_0_21;
        tmp_expression_value_29 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_29 == NULL)) {
            tmp_expression_value_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 423;

            goto try_except_handler_8;
        }
        tmp_called_value_39 = LOOKUP_ATTRIBUTE(tmp_expression_value_29, mod_consts[69]);
        if (tmp_called_value_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 423;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_21 = mod_consts[184];
        tmp_kw_call_arg_value_1_21 = Py_False;
        tmp_kw_call_arg_value_2_21 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[106]);

        if (unlikely(tmp_kw_call_arg_value_2_21 == NULL)) {
            tmp_kw_call_arg_value_2_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[106]);
        }

        if (tmp_kw_call_arg_value_2_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_39);

            exception_lineno = 424;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_21 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_21 == NULL)) {
            tmp_kw_call_dict_value_0_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_39);

            exception_lineno = 424;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 423;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_21, tmp_kw_call_arg_value_1_21, tmp_kw_call_arg_value_2_21};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_21};
            tmp_call_result_28 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_39, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_39);
        if (tmp_call_result_28 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 423;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_28);
    }
    {
        PyObject *tmp_called_value_40;
        PyObject *tmp_expression_value_30;
        PyObject *tmp_call_result_29;
        PyObject *tmp_kw_call_arg_value_0_22;
        PyObject *tmp_kw_call_arg_value_1_22;
        PyObject *tmp_kw_call_arg_value_2_22;
        PyObject *tmp_kw_call_dict_value_0_22;
        tmp_expression_value_30 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_30 == NULL)) {
            tmp_expression_value_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_30 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 426;

            goto try_except_handler_8;
        }
        tmp_called_value_40 = LOOKUP_ATTRIBUTE(tmp_expression_value_30, mod_consts[69]);
        if (tmp_called_value_40 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 426;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_22 = mod_consts[185];
        tmp_kw_call_arg_value_1_22 = Py_False;
        tmp_kw_call_arg_value_2_22 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[106]);

        if (unlikely(tmp_kw_call_arg_value_2_22 == NULL)) {
            tmp_kw_call_arg_value_2_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[106]);
        }

        if (tmp_kw_call_arg_value_2_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_40);

            exception_lineno = 427;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_22 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_22 == NULL)) {
            tmp_kw_call_dict_value_0_22 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_22 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_40);

            exception_lineno = 427;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 426;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_22, tmp_kw_call_arg_value_1_22, tmp_kw_call_arg_value_2_22};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_22};
            tmp_call_result_29 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_40, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_40);
        if (tmp_call_result_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 426;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_29);
    }
    {
        PyObject *tmp_called_value_41;
        PyObject *tmp_expression_value_31;
        PyObject *tmp_call_result_30;
        PyObject *tmp_kw_call_arg_value_0_23;
        PyObject *tmp_kw_call_arg_value_1_23;
        PyObject *tmp_kw_call_arg_value_2_23;
        PyObject *tmp_kw_call_dict_value_0_23;
        tmp_expression_value_31 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_31 == NULL)) {
            tmp_expression_value_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 429;

            goto try_except_handler_8;
        }
        tmp_called_value_41 = LOOKUP_ATTRIBUTE(tmp_expression_value_31, mod_consts[69]);
        if (tmp_called_value_41 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 429;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_23 = mod_consts[186];
        tmp_kw_call_arg_value_1_23 = Py_False;
        tmp_kw_call_arg_value_2_23 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[110]);

        if (unlikely(tmp_kw_call_arg_value_2_23 == NULL)) {
            tmp_kw_call_arg_value_2_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[110]);
        }

        if (tmp_kw_call_arg_value_2_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_41);

            exception_lineno = 429;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_23 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_23 == NULL)) {
            tmp_kw_call_dict_value_0_23 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_23 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_41);

            exception_lineno = 429;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 429;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_23, tmp_kw_call_arg_value_1_23, tmp_kw_call_arg_value_2_23};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_23};
            tmp_call_result_30 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_41, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_41);
        if (tmp_call_result_30 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 429;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_30);
    }
    {
        PyObject *tmp_called_value_42;
        PyObject *tmp_expression_value_32;
        PyObject *tmp_call_result_31;
        PyObject *tmp_kw_call_arg_value_0_24;
        PyObject *tmp_kw_call_arg_value_1_24;
        PyObject *tmp_kw_call_arg_value_2_24;
        PyObject *tmp_kw_call_dict_value_0_24;
        tmp_expression_value_32 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_32 == NULL)) {
            tmp_expression_value_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 430;

            goto try_except_handler_8;
        }
        tmp_called_value_42 = LOOKUP_ATTRIBUTE(tmp_expression_value_32, mod_consts[69]);
        if (tmp_called_value_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 430;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_24 = mod_consts[187];
        tmp_kw_call_arg_value_1_24 = Py_True;
        tmp_kw_call_arg_value_2_24 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[130]);

        if (unlikely(tmp_kw_call_arg_value_2_24 == NULL)) {
            tmp_kw_call_arg_value_2_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[130]);
        }

        if (tmp_kw_call_arg_value_2_24 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_42);

            exception_lineno = 430;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_24 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_24 == NULL)) {
            tmp_kw_call_dict_value_0_24 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_24 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_42);

            exception_lineno = 430;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 430;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_24, tmp_kw_call_arg_value_1_24, tmp_kw_call_arg_value_2_24};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_24};
            tmp_call_result_31 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_42, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_42);
        if (tmp_call_result_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 430;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_31);
    }
    {
        PyObject *tmp_called_value_43;
        PyObject *tmp_expression_value_33;
        PyObject *tmp_call_result_32;
        PyObject *tmp_kw_call_arg_value_0_25;
        PyObject *tmp_kw_call_arg_value_1_25;
        PyObject *tmp_kw_call_arg_value_2_25;
        PyObject *tmp_kw_call_dict_value_0_25;
        tmp_expression_value_33 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_33 == NULL)) {
            tmp_expression_value_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_33 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 431;

            goto try_except_handler_8;
        }
        tmp_called_value_43 = LOOKUP_ATTRIBUTE(tmp_expression_value_33, mod_consts[69]);
        if (tmp_called_value_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 431;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_25 = mod_consts[188];
        tmp_kw_call_arg_value_1_25 = Py_False;
        tmp_kw_call_arg_value_2_25 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[132]);

        if (unlikely(tmp_kw_call_arg_value_2_25 == NULL)) {
            tmp_kw_call_arg_value_2_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[132]);
        }

        if (tmp_kw_call_arg_value_2_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_43);

            exception_lineno = 431;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_25 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_25 == NULL)) {
            tmp_kw_call_dict_value_0_25 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_25 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_43);

            exception_lineno = 431;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 431;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_25, tmp_kw_call_arg_value_1_25, tmp_kw_call_arg_value_2_25};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_25};
            tmp_call_result_32 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_43, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_43);
        if (tmp_call_result_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 431;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_32);
    }
    {
        PyObject *tmp_called_value_44;
        PyObject *tmp_expression_value_34;
        PyObject *tmp_call_result_33;
        PyObject *tmp_kw_call_arg_value_0_26;
        PyObject *tmp_kw_call_arg_value_1_26;
        PyObject *tmp_kw_call_arg_value_2_26;
        PyObject *tmp_kw_call_dict_value_0_26;
        tmp_expression_value_34 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_34 == NULL)) {
            tmp_expression_value_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 432;

            goto try_except_handler_8;
        }
        tmp_called_value_44 = LOOKUP_ATTRIBUTE(tmp_expression_value_34, mod_consts[69]);
        if (tmp_called_value_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 432;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_26 = mod_consts[189];
        tmp_kw_call_arg_value_1_26 = Py_True;
        tmp_kw_call_arg_value_2_26 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[134]);

        if (unlikely(tmp_kw_call_arg_value_2_26 == NULL)) {
            tmp_kw_call_arg_value_2_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[134]);
        }

        if (tmp_kw_call_arg_value_2_26 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_44);

            exception_lineno = 433;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_26 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_26 == NULL)) {
            tmp_kw_call_dict_value_0_26 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_26 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_44);

            exception_lineno = 433;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 432;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_26, tmp_kw_call_arg_value_1_26, tmp_kw_call_arg_value_2_26};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_26};
            tmp_call_result_33 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_44, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_44);
        if (tmp_call_result_33 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 432;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_33);
    }
    {
        PyObject *tmp_called_value_45;
        PyObject *tmp_expression_value_35;
        PyObject *tmp_call_result_34;
        PyObject *tmp_kw_call_arg_value_0_27;
        PyObject *tmp_kw_call_arg_value_1_27;
        PyObject *tmp_kw_call_arg_value_2_27;
        PyObject *tmp_kw_call_dict_value_0_27;
        tmp_expression_value_35 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_35 == NULL)) {
            tmp_expression_value_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 435;

            goto try_except_handler_8;
        }
        tmp_called_value_45 = LOOKUP_ATTRIBUTE(tmp_expression_value_35, mod_consts[69]);
        if (tmp_called_value_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 435;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_27 = mod_consts[190];
        tmp_kw_call_arg_value_1_27 = mod_consts[191];
        tmp_kw_call_arg_value_2_27 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[134]);

        if (unlikely(tmp_kw_call_arg_value_2_27 == NULL)) {
            tmp_kw_call_arg_value_2_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[134]);
        }

        if (tmp_kw_call_arg_value_2_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_45);

            exception_lineno = 436;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_27 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[55]);

        if (unlikely(tmp_kw_call_dict_value_0_27 == NULL)) {
            tmp_kw_call_dict_value_0_27 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[55]);
        }

        if (tmp_kw_call_dict_value_0_27 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_45);

            exception_lineno = 436;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 435;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_27, tmp_kw_call_arg_value_1_27, tmp_kw_call_arg_value_2_27};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_27};
            tmp_call_result_34 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_45, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_45);
        if (tmp_call_result_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 435;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_34);
    }
    {
        PyObject *tmp_called_value_46;
        PyObject *tmp_expression_value_36;
        PyObject *tmp_call_result_35;
        PyObject *tmp_kw_call_arg_value_0_28;
        PyObject *tmp_kw_call_arg_value_1_28;
        PyObject *tmp_kw_call_arg_value_2_28;
        PyObject *tmp_kw_call_dict_value_0_28;
        tmp_expression_value_36 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_36 == NULL)) {
            tmp_expression_value_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 438;

            goto try_except_handler_8;
        }
        tmp_called_value_46 = LOOKUP_ATTRIBUTE(tmp_expression_value_36, mod_consts[69]);
        if (tmp_called_value_46 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 438;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_28 = mod_consts[192];
        tmp_kw_call_arg_value_1_28 = Py_False;
        tmp_kw_call_arg_value_2_28 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[138]);

        if (unlikely(tmp_kw_call_arg_value_2_28 == NULL)) {
            tmp_kw_call_arg_value_2_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[138]);
        }

        if (tmp_kw_call_arg_value_2_28 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_46);

            exception_lineno = 438;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_28 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_28 == NULL)) {
            tmp_kw_call_dict_value_0_28 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_28 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_46);

            exception_lineno = 438;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 438;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_28, tmp_kw_call_arg_value_1_28, tmp_kw_call_arg_value_2_28};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_28};
            tmp_call_result_35 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_46, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_46);
        if (tmp_call_result_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 438;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_35);
    }
    {
        PyObject *tmp_called_value_47;
        PyObject *tmp_expression_value_37;
        PyObject *tmp_call_result_36;
        PyObject *tmp_kw_call_arg_value_0_29;
        PyObject *tmp_kw_call_arg_value_1_29;
        PyObject *tmp_kw_call_arg_value_2_29;
        PyObject *tmp_kw_call_dict_value_0_29;
        PyObject *tmp_kw_call_dict_value_1_5;
        tmp_expression_value_37 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_37 == NULL)) {
            tmp_expression_value_37 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_37 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 439;

            goto try_except_handler_8;
        }
        tmp_called_value_47 = LOOKUP_ATTRIBUTE(tmp_expression_value_37, mod_consts[69]);
        if (tmp_called_value_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 439;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_29 = mod_consts[193];
        tmp_kw_call_arg_value_1_29 = Py_False;
        tmp_kw_call_arg_value_2_29 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[112]);

        if (unlikely(tmp_kw_call_arg_value_2_29 == NULL)) {
            tmp_kw_call_arg_value_2_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[112]);
        }

        if (tmp_kw_call_arg_value_2_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_47);

            exception_lineno = 442;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_29 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_29 == NULL)) {
            tmp_kw_call_dict_value_0_29 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_29 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_47);

            exception_lineno = 443;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_1_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[139]);

        if (unlikely(tmp_kw_call_dict_value_1_5 == NULL)) {
            tmp_kw_call_dict_value_1_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[139]);
        }

        if (tmp_kw_call_dict_value_1_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_47);

            exception_lineno = 444;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 439;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_29, tmp_kw_call_arg_value_1_29, tmp_kw_call_arg_value_2_29};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_29, tmp_kw_call_dict_value_1_5};
            tmp_call_result_36 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_47, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_47);
        if (tmp_call_result_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 439;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_36);
    }
    {
        PyObject *tmp_called_value_48;
        PyObject *tmp_expression_value_38;
        PyObject *tmp_call_result_37;
        PyObject *tmp_kw_call_arg_value_0_30;
        PyObject *tmp_kw_call_arg_value_1_30;
        PyObject *tmp_kw_call_arg_value_2_30;
        PyObject *tmp_kw_call_dict_value_0_30;
        tmp_expression_value_38 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_38 == NULL)) {
            tmp_expression_value_38 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 446;

            goto try_except_handler_8;
        }
        tmp_called_value_48 = LOOKUP_ATTRIBUTE(tmp_expression_value_38, mod_consts[69]);
        if (tmp_called_value_48 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 446;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_30 = mod_consts[194];
        tmp_kw_call_arg_value_1_30 = mod_consts[195];
        tmp_kw_call_arg_value_2_30 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[114]);

        if (unlikely(tmp_kw_call_arg_value_2_30 == NULL)) {
            tmp_kw_call_arg_value_2_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[114]);
        }

        if (tmp_kw_call_arg_value_2_30 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_48);

            exception_lineno = 446;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_30 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[52]);

        if (unlikely(tmp_kw_call_dict_value_0_30 == NULL)) {
            tmp_kw_call_dict_value_0_30 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[52]);
        }

        if (tmp_kw_call_dict_value_0_30 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_48);

            exception_lineno = 446;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 446;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_30, tmp_kw_call_arg_value_1_30, tmp_kw_call_arg_value_2_30};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_30};
            tmp_call_result_37 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_48, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_48);
        if (tmp_call_result_37 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 446;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_37);
    }
    {
        PyObject *tmp_called_value_49;
        PyObject *tmp_expression_value_39;
        PyObject *tmp_call_result_38;
        PyObject *tmp_kw_call_arg_value_0_31;
        PyObject *tmp_kw_call_arg_value_1_31;
        PyObject *tmp_kw_call_arg_value_2_31;
        PyObject *tmp_kw_call_dict_value_0_31;
        tmp_expression_value_39 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_39 == NULL)) {
            tmp_expression_value_39 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 447;

            goto try_except_handler_8;
        }
        tmp_called_value_49 = LOOKUP_ATTRIBUTE(tmp_expression_value_39, mod_consts[69]);
        if (tmp_called_value_49 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 447;

            goto try_except_handler_8;
        }
        tmp_kw_call_arg_value_0_31 = mod_consts[196];
        tmp_kw_call_arg_value_1_31 = Py_True;
        tmp_kw_call_arg_value_2_31 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[116]);

        if (unlikely(tmp_kw_call_arg_value_2_31 == NULL)) {
            tmp_kw_call_arg_value_2_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[116]);
        }

        if (tmp_kw_call_arg_value_2_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_49);

            exception_lineno = 448;

            goto try_except_handler_8;
        }
        tmp_kw_call_dict_value_0_31 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[49]);

        if (unlikely(tmp_kw_call_dict_value_0_31 == NULL)) {
            tmp_kw_call_dict_value_0_31 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[49]);
        }

        if (tmp_kw_call_dict_value_0_31 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_49);

            exception_lineno = 448;

            goto try_except_handler_8;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 447;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_31, tmp_kw_call_arg_value_1_31, tmp_kw_call_arg_value_2_31};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_31};
            tmp_call_result_38 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_49, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_49);
        if (tmp_call_result_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 447;

            goto try_except_handler_8;
        }
        Py_DECREF(tmp_call_result_38);
    }
    goto try_end_6;
    // Exception handler code:
    try_except_handler_8:;
    exception_keeper_type_6 = exception_type;
    exception_keeper_value_6 = exception_value;
    exception_keeper_tb_6 = exception_tb;
    exception_keeper_lineno_6 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 2.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_2, &exception_preserved_value_2, &exception_preserved_tb_2);

    if (exception_keeper_tb_6 == NULL) {
        exception_keeper_tb_6 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_6);
    } else if (exception_keeper_lineno_6 != 0) {
        exception_keeper_tb_6 = ADD_TRACEBACK(exception_keeper_tb_6, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_6);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_6, &exception_keeper_value_6, &exception_keeper_tb_6);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_6, exception_keeper_tb_6);
    PUBLISH_EXCEPTION(&exception_keeper_type_6, &exception_keeper_value_6, &exception_keeper_tb_6);
    // Tried code:
    {
        bool tmp_condition_result_6;
        PyObject *tmp_cmp_expr_left_4;
        PyObject *tmp_cmp_expr_right_4;
        tmp_cmp_expr_left_4 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_4 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_4, tmp_cmp_expr_right_4);
        assert(!(tmp_res == -1));
        tmp_condition_result_6 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_6 != false) {
            goto branch_yes_6;
        } else {
            goto branch_no_6;
        }
    }
    branch_yes_6:;
    {
        nuitka_bool tmp_assign_source_67;
        tmp_assign_source_67 = NUITKA_BOOL_FALSE;
        tmp_with_2__indicator = tmp_assign_source_67;
    }
    {
        bool tmp_condition_result_7;
        PyObject *tmp_operand_value_2;
        PyObject *tmp_called_value_50;
        PyObject *tmp_args_element_value_14;
        PyObject *tmp_args_element_value_15;
        PyObject *tmp_args_element_value_16;
        CHECK_OBJECT(tmp_with_2__exit);
        tmp_called_value_50 = tmp_with_2__exit;
        tmp_args_element_value_14 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_15 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_16 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 448;
        {
            PyObject *call_args[] = {tmp_args_element_value_14, tmp_args_element_value_15, tmp_args_element_value_16};
            tmp_operand_value_2 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_50, call_args);
        }

        if (tmp_operand_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 448;

            goto try_except_handler_9;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_2);
        Py_DECREF(tmp_operand_value_2);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 448;

            goto try_except_handler_9;
        }
        tmp_condition_result_7 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_7 != false) {
            goto branch_yes_7;
        } else {
            goto branch_no_7;
        }
    }
    branch_yes_7:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 448;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_9;
    branch_no_7:;
    goto branch_end_6;
    branch_no_6:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 342;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_9;
    branch_end_6:;
    goto try_end_7;
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

    // Restore previous exception id 2.
    SET_CURRENT_EXCEPTION(exception_preserved_type_2, exception_preserved_value_2, exception_preserved_tb_2);

    // Re-raise.
    exception_type = exception_keeper_type_7;
    exception_value = exception_keeper_value_7;
    exception_tb = exception_keeper_tb_7;
    exception_lineno = exception_keeper_lineno_7;

    goto try_except_handler_7;
    // End of try:
    try_end_7:;
    // Restore previous exception id 2.
    SET_CURRENT_EXCEPTION(exception_preserved_type_2, exception_preserved_value_2, exception_preserved_tb_2);

    goto try_end_6;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_6:;
    goto try_end_8;
    // Exception handler code:
    try_except_handler_7:;
    exception_keeper_type_8 = exception_type;
    exception_keeper_value_8 = exception_value;
    exception_keeper_tb_8 = exception_tb;
    exception_keeper_lineno_8 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_8;
        nuitka_bool tmp_cmp_expr_left_5;
        nuitka_bool tmp_cmp_expr_right_5;
        assert(tmp_with_2__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_5 = tmp_with_2__indicator;
        tmp_cmp_expr_right_5 = NUITKA_BOOL_TRUE;
        tmp_condition_result_8 = (tmp_cmp_expr_left_5 == tmp_cmp_expr_right_5) ? true : false;
        if (tmp_condition_result_8 != false) {
            goto branch_yes_8;
        } else {
            goto branch_no_8;
        }
    }
    branch_yes_8:;
    {
        PyObject *tmp_called_value_51;
        PyObject *tmp_call_result_39;
        CHECK_OBJECT(tmp_with_2__exit);
        tmp_called_value_51 = tmp_with_2__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 448;
        tmp_call_result_39 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_51, mod_consts[74]);

        if (tmp_call_result_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_8);
            Py_XDECREF(exception_keeper_value_8);
            Py_XDECREF(exception_keeper_tb_8);

            exception_lineno = 448;

            goto try_except_handler_6;
        }
        Py_DECREF(tmp_call_result_39);
    }
    branch_no_8:;
    // Re-raise.
    exception_type = exception_keeper_type_8;
    exception_value = exception_keeper_value_8;
    exception_tb = exception_keeper_tb_8;
    exception_lineno = exception_keeper_lineno_8;

    goto try_except_handler_6;
    // End of try:
    try_end_8:;
    {
        bool tmp_condition_result_9;
        nuitka_bool tmp_cmp_expr_left_6;
        nuitka_bool tmp_cmp_expr_right_6;
        assert(tmp_with_2__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_6 = tmp_with_2__indicator;
        tmp_cmp_expr_right_6 = NUITKA_BOOL_TRUE;
        tmp_condition_result_9 = (tmp_cmp_expr_left_6 == tmp_cmp_expr_right_6) ? true : false;
        if (tmp_condition_result_9 != false) {
            goto branch_yes_9;
        } else {
            goto branch_no_9;
        }
    }
    branch_yes_9:;
    {
        PyObject *tmp_called_value_52;
        PyObject *tmp_call_result_40;
        CHECK_OBJECT(tmp_with_2__exit);
        tmp_called_value_52 = tmp_with_2__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 448;
        tmp_call_result_40 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_52, mod_consts[74]);

        if (tmp_call_result_40 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 448;

            goto try_except_handler_6;
        }
        Py_DECREF(tmp_call_result_40);
    }
    branch_no_9:;
    goto try_end_9;
    // Exception handler code:
    try_except_handler_6:;
    exception_keeper_type_9 = exception_type;
    exception_keeper_value_9 = exception_value;
    exception_keeper_tb_9 = exception_tb;
    exception_keeper_lineno_9 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_2__source);
    tmp_with_2__source = NULL;
    Py_XDECREF(tmp_with_2__enter);
    tmp_with_2__enter = NULL;
    Py_XDECREF(tmp_with_2__exit);
    tmp_with_2__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_9;
    exception_value = exception_keeper_value_9;
    exception_tb = exception_keeper_tb_9;
    exception_lineno = exception_keeper_lineno_9;

    goto frame_exception_exit_1;
    // End of try:
    try_end_9:;
    CHECK_OBJECT(tmp_with_2__source);
    Py_DECREF(tmp_with_2__source);
    tmp_with_2__source = NULL;
    CHECK_OBJECT(tmp_with_2__enter);
    Py_DECREF(tmp_with_2__enter);
    tmp_with_2__enter = NULL;
    Py_XDECREF(tmp_with_2__exit);
    tmp_with_2__exit = NULL;
    {
        PyObject *tmp_assign_source_68;
        tmp_assign_source_68 = mod_consts[197];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[198], tmp_assign_source_68);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_69;
        PyObject *tmp_called_instance_3;
        tmp_called_instance_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_3 == NULL)) {
            tmp_called_instance_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 456;

            goto try_except_handler_10;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 456;
        tmp_assign_source_69 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_3,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[199], 0)
        );

        if (tmp_assign_source_69 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 456;

            goto try_except_handler_10;
        }
        assert(tmp_with_3__source == NULL);
        tmp_with_3__source = tmp_assign_source_69;
    }
    {
        PyObject *tmp_assign_source_70;
        PyObject *tmp_called_value_53;
        PyObject *tmp_expression_value_40;
        CHECK_OBJECT(tmp_with_3__source);
        tmp_expression_value_40 = tmp_with_3__source;
        tmp_called_value_53 = LOOKUP_SPECIAL(tmp_expression_value_40, mod_consts[67]);
        if (tmp_called_value_53 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 456;

            goto try_except_handler_10;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 456;
        tmp_assign_source_70 = CALL_FUNCTION_NO_ARGS(tmp_called_value_53);
        Py_DECREF(tmp_called_value_53);
        if (tmp_assign_source_70 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 456;

            goto try_except_handler_10;
        }
        assert(tmp_with_3__enter == NULL);
        tmp_with_3__enter = tmp_assign_source_70;
    }
    {
        PyObject *tmp_assign_source_71;
        PyObject *tmp_expression_value_41;
        CHECK_OBJECT(tmp_with_3__source);
        tmp_expression_value_41 = tmp_with_3__source;
        tmp_assign_source_71 = LOOKUP_SPECIAL(tmp_expression_value_41, mod_consts[68]);
        if (tmp_assign_source_71 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 456;

            goto try_except_handler_10;
        }
        assert(tmp_with_3__exit == NULL);
        tmp_with_3__exit = tmp_assign_source_71;
    }
    {
        nuitka_bool tmp_assign_source_72;
        tmp_assign_source_72 = NUITKA_BOOL_TRUE;
        tmp_with_3__indicator = tmp_assign_source_72;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_54;
        PyObject *tmp_expression_value_42;
        PyObject *tmp_call_result_41;
        PyObject *tmp_args_element_value_17;
        PyObject *tmp_args_element_value_18;
        PyObject *tmp_args_element_value_19;
        tmp_expression_value_42 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_42 == NULL)) {
            tmp_expression_value_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_12;
        }
        tmp_called_value_54 = LOOKUP_ATTRIBUTE(tmp_expression_value_42, mod_consts[69]);
        if (tmp_called_value_54 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_12;
        }
        tmp_args_element_value_17 = mod_consts[200];
        tmp_args_element_value_18 = Py_False;
        tmp_args_element_value_19 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[198]);

        if (unlikely(tmp_args_element_value_19 == NULL)) {
            tmp_args_element_value_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[198]);
        }

        if (tmp_args_element_value_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_54);

            exception_lineno = 457;

            goto try_except_handler_12;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 457;
        {
            PyObject *call_args[] = {tmp_args_element_value_17, tmp_args_element_value_18, tmp_args_element_value_19};
            tmp_call_result_41 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_54, call_args);
        }

        Py_DECREF(tmp_called_value_54);
        if (tmp_call_result_41 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_12;
        }
        Py_DECREF(tmp_call_result_41);
    }
    goto try_end_10;
    // Exception handler code:
    try_except_handler_12:;
    exception_keeper_type_10 = exception_type;
    exception_keeper_value_10 = exception_value;
    exception_keeper_tb_10 = exception_tb;
    exception_keeper_lineno_10 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 3.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_3, &exception_preserved_value_3, &exception_preserved_tb_3);

    if (exception_keeper_tb_10 == NULL) {
        exception_keeper_tb_10 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_10);
    } else if (exception_keeper_lineno_10 != 0) {
        exception_keeper_tb_10 = ADD_TRACEBACK(exception_keeper_tb_10, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_10);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_10, &exception_keeper_value_10, &exception_keeper_tb_10);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_10, exception_keeper_tb_10);
    PUBLISH_EXCEPTION(&exception_keeper_type_10, &exception_keeper_value_10, &exception_keeper_tb_10);
    // Tried code:
    {
        bool tmp_condition_result_10;
        PyObject *tmp_cmp_expr_left_7;
        PyObject *tmp_cmp_expr_right_7;
        tmp_cmp_expr_left_7 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_7 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_7, tmp_cmp_expr_right_7);
        assert(!(tmp_res == -1));
        tmp_condition_result_10 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_10 != false) {
            goto branch_yes_10;
        } else {
            goto branch_no_10;
        }
    }
    branch_yes_10:;
    {
        nuitka_bool tmp_assign_source_73;
        tmp_assign_source_73 = NUITKA_BOOL_FALSE;
        tmp_with_3__indicator = tmp_assign_source_73;
    }
    {
        bool tmp_condition_result_11;
        PyObject *tmp_operand_value_3;
        PyObject *tmp_called_value_55;
        PyObject *tmp_args_element_value_20;
        PyObject *tmp_args_element_value_21;
        PyObject *tmp_args_element_value_22;
        CHECK_OBJECT(tmp_with_3__exit);
        tmp_called_value_55 = tmp_with_3__exit;
        tmp_args_element_value_20 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_21 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_22 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 457;
        {
            PyObject *call_args[] = {tmp_args_element_value_20, tmp_args_element_value_21, tmp_args_element_value_22};
            tmp_operand_value_3 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_55, call_args);
        }

        if (tmp_operand_value_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_13;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_3);
        Py_DECREF(tmp_operand_value_3);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_13;
        }
        tmp_condition_result_11 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_11 != false) {
            goto branch_yes_11;
        } else {
            goto branch_no_11;
        }
    }
    branch_yes_11:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 457;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_13;
    branch_no_11:;
    goto branch_end_10;
    branch_no_10:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 456;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_13;
    branch_end_10:;
    goto try_end_11;
    // Exception handler code:
    try_except_handler_13:;
    exception_keeper_type_11 = exception_type;
    exception_keeper_value_11 = exception_value;
    exception_keeper_tb_11 = exception_tb;
    exception_keeper_lineno_11 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 3.
    SET_CURRENT_EXCEPTION(exception_preserved_type_3, exception_preserved_value_3, exception_preserved_tb_3);

    // Re-raise.
    exception_type = exception_keeper_type_11;
    exception_value = exception_keeper_value_11;
    exception_tb = exception_keeper_tb_11;
    exception_lineno = exception_keeper_lineno_11;

    goto try_except_handler_11;
    // End of try:
    try_end_11:;
    // Restore previous exception id 3.
    SET_CURRENT_EXCEPTION(exception_preserved_type_3, exception_preserved_value_3, exception_preserved_tb_3);

    goto try_end_10;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_10:;
    goto try_end_12;
    // Exception handler code:
    try_except_handler_11:;
    exception_keeper_type_12 = exception_type;
    exception_keeper_value_12 = exception_value;
    exception_keeper_tb_12 = exception_tb;
    exception_keeper_lineno_12 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_12;
        nuitka_bool tmp_cmp_expr_left_8;
        nuitka_bool tmp_cmp_expr_right_8;
        assert(tmp_with_3__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_8 = tmp_with_3__indicator;
        tmp_cmp_expr_right_8 = NUITKA_BOOL_TRUE;
        tmp_condition_result_12 = (tmp_cmp_expr_left_8 == tmp_cmp_expr_right_8) ? true : false;
        if (tmp_condition_result_12 != false) {
            goto branch_yes_12;
        } else {
            goto branch_no_12;
        }
    }
    branch_yes_12:;
    {
        PyObject *tmp_called_value_56;
        PyObject *tmp_call_result_42;
        CHECK_OBJECT(tmp_with_3__exit);
        tmp_called_value_56 = tmp_with_3__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 457;
        tmp_call_result_42 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_56, mod_consts[74]);

        if (tmp_call_result_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_12);
            Py_XDECREF(exception_keeper_value_12);
            Py_XDECREF(exception_keeper_tb_12);

            exception_lineno = 457;

            goto try_except_handler_10;
        }
        Py_DECREF(tmp_call_result_42);
    }
    branch_no_12:;
    // Re-raise.
    exception_type = exception_keeper_type_12;
    exception_value = exception_keeper_value_12;
    exception_tb = exception_keeper_tb_12;
    exception_lineno = exception_keeper_lineno_12;

    goto try_except_handler_10;
    // End of try:
    try_end_12:;
    {
        bool tmp_condition_result_13;
        nuitka_bool tmp_cmp_expr_left_9;
        nuitka_bool tmp_cmp_expr_right_9;
        assert(tmp_with_3__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_9 = tmp_with_3__indicator;
        tmp_cmp_expr_right_9 = NUITKA_BOOL_TRUE;
        tmp_condition_result_13 = (tmp_cmp_expr_left_9 == tmp_cmp_expr_right_9) ? true : false;
        if (tmp_condition_result_13 != false) {
            goto branch_yes_13;
        } else {
            goto branch_no_13;
        }
    }
    branch_yes_13:;
    {
        PyObject *tmp_called_value_57;
        PyObject *tmp_call_result_43;
        CHECK_OBJECT(tmp_with_3__exit);
        tmp_called_value_57 = tmp_with_3__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 457;
        tmp_call_result_43 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_57, mod_consts[74]);

        if (tmp_call_result_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 457;

            goto try_except_handler_10;
        }
        Py_DECREF(tmp_call_result_43);
    }
    branch_no_13:;
    goto try_end_13;
    // Exception handler code:
    try_except_handler_10:;
    exception_keeper_type_13 = exception_type;
    exception_keeper_value_13 = exception_value;
    exception_keeper_tb_13 = exception_tb;
    exception_keeper_lineno_13 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_3__source);
    tmp_with_3__source = NULL;
    Py_XDECREF(tmp_with_3__enter);
    tmp_with_3__enter = NULL;
    Py_XDECREF(tmp_with_3__exit);
    tmp_with_3__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_13;
    exception_value = exception_keeper_value_13;
    exception_tb = exception_keeper_tb_13;
    exception_lineno = exception_keeper_lineno_13;

    goto frame_exception_exit_1;
    // End of try:
    try_end_13:;
    CHECK_OBJECT(tmp_with_3__source);
    Py_DECREF(tmp_with_3__source);
    tmp_with_3__source = NULL;
    CHECK_OBJECT(tmp_with_3__enter);
    Py_DECREF(tmp_with_3__enter);
    tmp_with_3__enter = NULL;
    Py_XDECREF(tmp_with_3__exit);
    tmp_with_3__exit = NULL;
    {
        PyObject *tmp_assign_source_74;
        tmp_assign_source_74 = mod_consts[201];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[202], tmp_assign_source_74);
    }
    {
        PyObject *tmp_assign_source_75;
        tmp_assign_source_75 = mod_consts[203];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[204], tmp_assign_source_75);
    }
    {
        PyObject *tmp_assign_source_76;


        tmp_assign_source_76 = MAKE_FUNCTION_pandas$core$config_init$$$function__7_use_inf_as_na_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[205], tmp_assign_source_76);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_77;
        PyObject *tmp_called_instance_4;
        tmp_called_instance_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_4 == NULL)) {
            tmp_called_instance_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 482;

            goto try_except_handler_14;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 482;
        tmp_assign_source_77 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_4,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[199], 0)
        );

        if (tmp_assign_source_77 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 482;

            goto try_except_handler_14;
        }
        assert(tmp_with_4__source == NULL);
        tmp_with_4__source = tmp_assign_source_77;
    }
    {
        PyObject *tmp_assign_source_78;
        PyObject *tmp_called_value_58;
        PyObject *tmp_expression_value_43;
        CHECK_OBJECT(tmp_with_4__source);
        tmp_expression_value_43 = tmp_with_4__source;
        tmp_called_value_58 = LOOKUP_SPECIAL(tmp_expression_value_43, mod_consts[67]);
        if (tmp_called_value_58 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 482;

            goto try_except_handler_14;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 482;
        tmp_assign_source_78 = CALL_FUNCTION_NO_ARGS(tmp_called_value_58);
        Py_DECREF(tmp_called_value_58);
        if (tmp_assign_source_78 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 482;

            goto try_except_handler_14;
        }
        assert(tmp_with_4__enter == NULL);
        tmp_with_4__enter = tmp_assign_source_78;
    }
    {
        PyObject *tmp_assign_source_79;
        PyObject *tmp_expression_value_44;
        CHECK_OBJECT(tmp_with_4__source);
        tmp_expression_value_44 = tmp_with_4__source;
        tmp_assign_source_79 = LOOKUP_SPECIAL(tmp_expression_value_44, mod_consts[68]);
        if (tmp_assign_source_79 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 482;

            goto try_except_handler_14;
        }
        assert(tmp_with_4__exit == NULL);
        tmp_with_4__exit = tmp_assign_source_79;
    }
    {
        nuitka_bool tmp_assign_source_80;
        tmp_assign_source_80 = NUITKA_BOOL_TRUE;
        tmp_with_4__indicator = tmp_assign_source_80;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_59;
        PyObject *tmp_expression_value_45;
        PyObject *tmp_call_result_44;
        PyObject *tmp_kw_call_arg_value_0_32;
        PyObject *tmp_kw_call_arg_value_1_32;
        PyObject *tmp_kw_call_arg_value_2_32;
        PyObject *tmp_kw_call_dict_value_0_32;
        tmp_expression_value_45 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_45 == NULL)) {
            tmp_expression_value_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 483;

            goto try_except_handler_16;
        }
        tmp_called_value_59 = LOOKUP_ATTRIBUTE(tmp_expression_value_45, mod_consts[69]);
        if (tmp_called_value_59 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 483;

            goto try_except_handler_16;
        }
        tmp_kw_call_arg_value_0_32 = mod_consts[206];
        tmp_kw_call_arg_value_1_32 = Py_False;
        tmp_kw_call_arg_value_2_32 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[204]);

        if (unlikely(tmp_kw_call_arg_value_2_32 == NULL)) {
            tmp_kw_call_arg_value_2_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[204]);
        }

        if (tmp_kw_call_arg_value_2_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_59);

            exception_lineno = 483;

            goto try_except_handler_16;
        }
        tmp_kw_call_dict_value_0_32 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[205]);

        if (unlikely(tmp_kw_call_dict_value_0_32 == NULL)) {
            tmp_kw_call_dict_value_0_32 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[205]);
        }

        if (tmp_kw_call_dict_value_0_32 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_59);

            exception_lineno = 483;

            goto try_except_handler_16;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 483;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_32, tmp_kw_call_arg_value_1_32, tmp_kw_call_arg_value_2_32};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_32};
            tmp_call_result_44 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_59, args, kw_values, mod_consts[207]);
        }

        Py_DECREF(tmp_called_value_59);
        if (tmp_call_result_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 483;

            goto try_except_handler_16;
        }
        Py_DECREF(tmp_call_result_44);
    }
    {
        PyObject *tmp_called_value_60;
        PyObject *tmp_expression_value_46;
        PyObject *tmp_call_result_45;
        PyObject *tmp_kw_call_arg_value_0_33;
        PyObject *tmp_kw_call_arg_value_1_33;
        PyObject *tmp_kw_call_arg_value_2_33;
        PyObject *tmp_kw_call_dict_value_0_33;
        tmp_expression_value_46 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_46 == NULL)) {
            tmp_expression_value_46 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_46 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 484;

            goto try_except_handler_16;
        }
        tmp_called_value_60 = LOOKUP_ATTRIBUTE(tmp_expression_value_46, mod_consts[69]);
        if (tmp_called_value_60 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 484;

            goto try_except_handler_16;
        }
        tmp_kw_call_arg_value_0_33 = mod_consts[208];
        tmp_kw_call_arg_value_1_33 = Py_False;
        tmp_kw_call_arg_value_2_33 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[202]);

        if (unlikely(tmp_kw_call_arg_value_2_33 == NULL)) {
            tmp_kw_call_arg_value_2_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[202]);
        }

        if (tmp_kw_call_arg_value_2_33 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_60);

            exception_lineno = 485;

            goto try_except_handler_16;
        }
        tmp_kw_call_dict_value_0_33 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[205]);

        if (unlikely(tmp_kw_call_dict_value_0_33 == NULL)) {
            tmp_kw_call_dict_value_0_33 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[205]);
        }

        if (tmp_kw_call_dict_value_0_33 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_60);

            exception_lineno = 485;

            goto try_except_handler_16;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 484;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_33, tmp_kw_call_arg_value_1_33, tmp_kw_call_arg_value_2_33};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_33};
            tmp_call_result_45 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_60, args, kw_values, mod_consts[207]);
        }

        Py_DECREF(tmp_called_value_60);
        if (tmp_call_result_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 484;

            goto try_except_handler_16;
        }
        Py_DECREF(tmp_call_result_45);
    }
    goto try_end_14;
    // Exception handler code:
    try_except_handler_16:;
    exception_keeper_type_14 = exception_type;
    exception_keeper_value_14 = exception_value;
    exception_keeper_tb_14 = exception_tb;
    exception_keeper_lineno_14 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 4.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_4, &exception_preserved_value_4, &exception_preserved_tb_4);

    if (exception_keeper_tb_14 == NULL) {
        exception_keeper_tb_14 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_14);
    } else if (exception_keeper_lineno_14 != 0) {
        exception_keeper_tb_14 = ADD_TRACEBACK(exception_keeper_tb_14, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_14);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_14, &exception_keeper_value_14, &exception_keeper_tb_14);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_14, exception_keeper_tb_14);
    PUBLISH_EXCEPTION(&exception_keeper_type_14, &exception_keeper_value_14, &exception_keeper_tb_14);
    // Tried code:
    {
        bool tmp_condition_result_14;
        PyObject *tmp_cmp_expr_left_10;
        PyObject *tmp_cmp_expr_right_10;
        tmp_cmp_expr_left_10 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_10 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_10, tmp_cmp_expr_right_10);
        assert(!(tmp_res == -1));
        tmp_condition_result_14 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_14 != false) {
            goto branch_yes_14;
        } else {
            goto branch_no_14;
        }
    }
    branch_yes_14:;
    {
        nuitka_bool tmp_assign_source_81;
        tmp_assign_source_81 = NUITKA_BOOL_FALSE;
        tmp_with_4__indicator = tmp_assign_source_81;
    }
    {
        bool tmp_condition_result_15;
        PyObject *tmp_operand_value_4;
        PyObject *tmp_called_value_61;
        PyObject *tmp_args_element_value_23;
        PyObject *tmp_args_element_value_24;
        PyObject *tmp_args_element_value_25;
        CHECK_OBJECT(tmp_with_4__exit);
        tmp_called_value_61 = tmp_with_4__exit;
        tmp_args_element_value_23 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_24 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_25 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 485;
        {
            PyObject *call_args[] = {tmp_args_element_value_23, tmp_args_element_value_24, tmp_args_element_value_25};
            tmp_operand_value_4 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_61, call_args);
        }

        if (tmp_operand_value_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 485;

            goto try_except_handler_17;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_4);
        Py_DECREF(tmp_operand_value_4);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 485;

            goto try_except_handler_17;
        }
        tmp_condition_result_15 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_15 != false) {
            goto branch_yes_15;
        } else {
            goto branch_no_15;
        }
    }
    branch_yes_15:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 485;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_17;
    branch_no_15:;
    goto branch_end_14;
    branch_no_14:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 482;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_17;
    branch_end_14:;
    goto try_end_15;
    // Exception handler code:
    try_except_handler_17:;
    exception_keeper_type_15 = exception_type;
    exception_keeper_value_15 = exception_value;
    exception_keeper_tb_15 = exception_tb;
    exception_keeper_lineno_15 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 4.
    SET_CURRENT_EXCEPTION(exception_preserved_type_4, exception_preserved_value_4, exception_preserved_tb_4);

    // Re-raise.
    exception_type = exception_keeper_type_15;
    exception_value = exception_keeper_value_15;
    exception_tb = exception_keeper_tb_15;
    exception_lineno = exception_keeper_lineno_15;

    goto try_except_handler_15;
    // End of try:
    try_end_15:;
    // Restore previous exception id 4.
    SET_CURRENT_EXCEPTION(exception_preserved_type_4, exception_preserved_value_4, exception_preserved_tb_4);

    goto try_end_14;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_14:;
    goto try_end_16;
    // Exception handler code:
    try_except_handler_15:;
    exception_keeper_type_16 = exception_type;
    exception_keeper_value_16 = exception_value;
    exception_keeper_tb_16 = exception_tb;
    exception_keeper_lineno_16 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_16;
        nuitka_bool tmp_cmp_expr_left_11;
        nuitka_bool tmp_cmp_expr_right_11;
        assert(tmp_with_4__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_11 = tmp_with_4__indicator;
        tmp_cmp_expr_right_11 = NUITKA_BOOL_TRUE;
        tmp_condition_result_16 = (tmp_cmp_expr_left_11 == tmp_cmp_expr_right_11) ? true : false;
        if (tmp_condition_result_16 != false) {
            goto branch_yes_16;
        } else {
            goto branch_no_16;
        }
    }
    branch_yes_16:;
    {
        PyObject *tmp_called_value_62;
        PyObject *tmp_call_result_46;
        CHECK_OBJECT(tmp_with_4__exit);
        tmp_called_value_62 = tmp_with_4__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 485;
        tmp_call_result_46 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_62, mod_consts[74]);

        if (tmp_call_result_46 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_16);
            Py_XDECREF(exception_keeper_value_16);
            Py_XDECREF(exception_keeper_tb_16);

            exception_lineno = 485;

            goto try_except_handler_14;
        }
        Py_DECREF(tmp_call_result_46);
    }
    branch_no_16:;
    // Re-raise.
    exception_type = exception_keeper_type_16;
    exception_value = exception_keeper_value_16;
    exception_tb = exception_keeper_tb_16;
    exception_lineno = exception_keeper_lineno_16;

    goto try_except_handler_14;
    // End of try:
    try_end_16:;
    {
        bool tmp_condition_result_17;
        nuitka_bool tmp_cmp_expr_left_12;
        nuitka_bool tmp_cmp_expr_right_12;
        assert(tmp_with_4__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_12 = tmp_with_4__indicator;
        tmp_cmp_expr_right_12 = NUITKA_BOOL_TRUE;
        tmp_condition_result_17 = (tmp_cmp_expr_left_12 == tmp_cmp_expr_right_12) ? true : false;
        if (tmp_condition_result_17 != false) {
            goto branch_yes_17;
        } else {
            goto branch_no_17;
        }
    }
    branch_yes_17:;
    {
        PyObject *tmp_called_value_63;
        PyObject *tmp_call_result_47;
        CHECK_OBJECT(tmp_with_4__exit);
        tmp_called_value_63 = tmp_with_4__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 485;
        tmp_call_result_47 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_63, mod_consts[74]);

        if (tmp_call_result_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 485;

            goto try_except_handler_14;
        }
        Py_DECREF(tmp_call_result_47);
    }
    branch_no_17:;
    goto try_end_17;
    // Exception handler code:
    try_except_handler_14:;
    exception_keeper_type_17 = exception_type;
    exception_keeper_value_17 = exception_value;
    exception_keeper_tb_17 = exception_tb;
    exception_keeper_lineno_17 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_4__source);
    tmp_with_4__source = NULL;
    Py_XDECREF(tmp_with_4__enter);
    tmp_with_4__enter = NULL;
    Py_XDECREF(tmp_with_4__exit);
    tmp_with_4__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_17;
    exception_value = exception_keeper_value_17;
    exception_tb = exception_keeper_tb_17;
    exception_lineno = exception_keeper_lineno_17;

    goto frame_exception_exit_1;
    // End of try:
    try_end_17:;
    CHECK_OBJECT(tmp_with_4__source);
    Py_DECREF(tmp_with_4__source);
    tmp_with_4__source = NULL;
    CHECK_OBJECT(tmp_with_4__enter);
    Py_DECREF(tmp_with_4__enter);
    tmp_with_4__enter = NULL;
    Py_XDECREF(tmp_with_4__exit);
    tmp_with_4__exit = NULL;
    {
        PyObject *tmp_called_value_64;
        PyObject *tmp_expression_value_47;
        PyObject *tmp_call_result_48;
        PyObject *tmp_kw_call_value_0_2;
        PyObject *tmp_kw_call_value_1_1;
        tmp_expression_value_47 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_47 == NULL)) {
            tmp_expression_value_47 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 489;

            goto frame_exception_exit_1;
        }
        tmp_called_value_64 = LOOKUP_ATTRIBUTE(tmp_expression_value_47, mod_consts[209]);
        if (tmp_called_value_64 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 489;

            goto frame_exception_exit_1;
        }
        tmp_kw_call_value_0_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[202]);

        if (unlikely(tmp_kw_call_value_0_2 == NULL)) {
            tmp_kw_call_value_0_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[202]);
        }

        if (tmp_kw_call_value_0_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_64);

            exception_lineno = 490;

            goto frame_exception_exit_1;
        }
        tmp_kw_call_value_1_1 = mod_consts[210];
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 489;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_2, tmp_kw_call_value_1_1};
            tmp_call_result_48 = CALL_FUNCTION_WITH_POSARGS1_KWSPLIT(tmp_called_value_64, mod_consts[211], kw_values, mod_consts[212]);
        }

        Py_DECREF(tmp_called_value_64);
        if (tmp_call_result_48 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 489;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_48);
    }
    {
        PyObject *tmp_assign_source_82;
        tmp_assign_source_82 = mod_consts[213];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[214], tmp_assign_source_82);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_83;
        PyObject *tmp_called_instance_5;
        tmp_called_instance_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_5 == NULL)) {
            tmp_called_instance_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 502;

            goto try_except_handler_18;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 502;
        tmp_assign_source_83 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_5,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[199], 0)
        );

        if (tmp_assign_source_83 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 502;

            goto try_except_handler_18;
        }
        assert(tmp_with_5__source == NULL);
        tmp_with_5__source = tmp_assign_source_83;
    }
    {
        PyObject *tmp_assign_source_84;
        PyObject *tmp_called_value_65;
        PyObject *tmp_expression_value_48;
        CHECK_OBJECT(tmp_with_5__source);
        tmp_expression_value_48 = tmp_with_5__source;
        tmp_called_value_65 = LOOKUP_SPECIAL(tmp_expression_value_48, mod_consts[67]);
        if (tmp_called_value_65 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 502;

            goto try_except_handler_18;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 502;
        tmp_assign_source_84 = CALL_FUNCTION_NO_ARGS(tmp_called_value_65);
        Py_DECREF(tmp_called_value_65);
        if (tmp_assign_source_84 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 502;

            goto try_except_handler_18;
        }
        assert(tmp_with_5__enter == NULL);
        tmp_with_5__enter = tmp_assign_source_84;
    }
    {
        PyObject *tmp_assign_source_85;
        PyObject *tmp_expression_value_49;
        CHECK_OBJECT(tmp_with_5__source);
        tmp_expression_value_49 = tmp_with_5__source;
        tmp_assign_source_85 = LOOKUP_SPECIAL(tmp_expression_value_49, mod_consts[68]);
        if (tmp_assign_source_85 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 502;

            goto try_except_handler_18;
        }
        assert(tmp_with_5__exit == NULL);
        tmp_with_5__exit = tmp_assign_source_85;
    }
    {
        nuitka_bool tmp_assign_source_86;
        tmp_assign_source_86 = NUITKA_BOOL_TRUE;
        tmp_with_5__indicator = tmp_assign_source_86;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_66;
        PyObject *tmp_expression_value_50;
        PyObject *tmp_call_result_49;
        PyObject *tmp_kw_call_arg_value_0_34;
        PyObject *tmp_kw_call_arg_value_1_34;
        PyObject *tmp_called_value_67;
        PyObject *tmp_expression_value_51;
        PyObject *tmp_expression_value_52;
        PyObject *tmp_kw_call_arg_value_2_34;
        PyObject *tmp_kw_call_dict_value_0_34;
        PyObject *tmp_called_value_68;
        PyObject *tmp_call_arg_element_7;
        tmp_expression_value_50 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_50 == NULL)) {
            tmp_expression_value_50 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_50 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 503;

            goto try_except_handler_20;
        }
        tmp_called_value_66 = LOOKUP_ATTRIBUTE(tmp_expression_value_50, mod_consts[69]);
        if (tmp_called_value_66 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 503;

            goto try_except_handler_20;
        }
        tmp_kw_call_arg_value_0_34 = mod_consts[215];
        tmp_expression_value_52 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[44]);

        if (unlikely(tmp_expression_value_52 == NULL)) {
            tmp_expression_value_52 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[44]);
        }

        if (tmp_expression_value_52 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);

            exception_lineno = 507;

            goto try_except_handler_20;
        }
        tmp_expression_value_51 = LOOKUP_ATTRIBUTE(tmp_expression_value_52, mod_consts[216]);
        if (tmp_expression_value_51 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);

            exception_lineno = 507;

            goto try_except_handler_20;
        }
        tmp_called_value_67 = LOOKUP_ATTRIBUTE(tmp_expression_value_51, mod_consts[217]);
        Py_DECREF(tmp_expression_value_51);
        if (tmp_called_value_67 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);

            exception_lineno = 507;

            goto try_except_handler_20;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 507;
        tmp_kw_call_arg_value_1_34 = CALL_FUNCTION_WITH_POSARGS2(tmp_called_value_67, mod_consts[218]);

        Py_DECREF(tmp_called_value_67);
        if (tmp_kw_call_arg_value_1_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);

            exception_lineno = 507;

            goto try_except_handler_20;
        }
        tmp_kw_call_arg_value_2_34 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[214]);

        if (unlikely(tmp_kw_call_arg_value_2_34 == NULL)) {
            tmp_kw_call_arg_value_2_34 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[214]);
        }

        if (tmp_kw_call_arg_value_2_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);
            Py_DECREF(tmp_kw_call_arg_value_1_34);

            exception_lineno = 508;

            goto try_except_handler_20;
        }
        tmp_called_value_68 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_68 == NULL)) {
            tmp_called_value_68 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_68 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);
            Py_DECREF(tmp_kw_call_arg_value_1_34);

            exception_lineno = 509;

            goto try_except_handler_20;
        }
        tmp_call_arg_element_7 = LIST_COPY(mod_consts[219]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 509;
        tmp_kw_call_dict_value_0_34 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_68, tmp_call_arg_element_7);
        Py_DECREF(tmp_call_arg_element_7);
        if (tmp_kw_call_dict_value_0_34 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_66);
            Py_DECREF(tmp_kw_call_arg_value_1_34);

            exception_lineno = 509;

            goto try_except_handler_20;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 503;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_34, tmp_kw_call_arg_value_1_34, tmp_kw_call_arg_value_2_34};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_34};
            tmp_call_result_49 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_66, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_66);
        Py_DECREF(tmp_kw_call_arg_value_1_34);
        Py_DECREF(tmp_kw_call_dict_value_0_34);
        if (tmp_call_result_49 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 503;

            goto try_except_handler_20;
        }
        Py_DECREF(tmp_call_result_49);
    }
    goto try_end_18;
    // Exception handler code:
    try_except_handler_20:;
    exception_keeper_type_18 = exception_type;
    exception_keeper_value_18 = exception_value;
    exception_keeper_tb_18 = exception_tb;
    exception_keeper_lineno_18 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 5.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_5, &exception_preserved_value_5, &exception_preserved_tb_5);

    if (exception_keeper_tb_18 == NULL) {
        exception_keeper_tb_18 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_18);
    } else if (exception_keeper_lineno_18 != 0) {
        exception_keeper_tb_18 = ADD_TRACEBACK(exception_keeper_tb_18, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_18);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_18, &exception_keeper_value_18, &exception_keeper_tb_18);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_18, exception_keeper_tb_18);
    PUBLISH_EXCEPTION(&exception_keeper_type_18, &exception_keeper_value_18, &exception_keeper_tb_18);
    // Tried code:
    {
        bool tmp_condition_result_18;
        PyObject *tmp_cmp_expr_left_13;
        PyObject *tmp_cmp_expr_right_13;
        tmp_cmp_expr_left_13 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_13 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_13, tmp_cmp_expr_right_13);
        assert(!(tmp_res == -1));
        tmp_condition_result_18 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_18 != false) {
            goto branch_yes_18;
        } else {
            goto branch_no_18;
        }
    }
    branch_yes_18:;
    {
        nuitka_bool tmp_assign_source_87;
        tmp_assign_source_87 = NUITKA_BOOL_FALSE;
        tmp_with_5__indicator = tmp_assign_source_87;
    }
    {
        bool tmp_condition_result_19;
        PyObject *tmp_operand_value_5;
        PyObject *tmp_called_value_69;
        PyObject *tmp_args_element_value_26;
        PyObject *tmp_args_element_value_27;
        PyObject *tmp_args_element_value_28;
        CHECK_OBJECT(tmp_with_5__exit);
        tmp_called_value_69 = tmp_with_5__exit;
        tmp_args_element_value_26 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_27 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_28 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 509;
        {
            PyObject *call_args[] = {tmp_args_element_value_26, tmp_args_element_value_27, tmp_args_element_value_28};
            tmp_operand_value_5 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_69, call_args);
        }

        if (tmp_operand_value_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 509;

            goto try_except_handler_21;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_5);
        Py_DECREF(tmp_operand_value_5);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 509;

            goto try_except_handler_21;
        }
        tmp_condition_result_19 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_19 != false) {
            goto branch_yes_19;
        } else {
            goto branch_no_19;
        }
    }
    branch_yes_19:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 509;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_21;
    branch_no_19:;
    goto branch_end_18;
    branch_no_18:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 502;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_21;
    branch_end_18:;
    goto try_end_19;
    // Exception handler code:
    try_except_handler_21:;
    exception_keeper_type_19 = exception_type;
    exception_keeper_value_19 = exception_value;
    exception_keeper_tb_19 = exception_tb;
    exception_keeper_lineno_19 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 5.
    SET_CURRENT_EXCEPTION(exception_preserved_type_5, exception_preserved_value_5, exception_preserved_tb_5);

    // Re-raise.
    exception_type = exception_keeper_type_19;
    exception_value = exception_keeper_value_19;
    exception_tb = exception_keeper_tb_19;
    exception_lineno = exception_keeper_lineno_19;

    goto try_except_handler_19;
    // End of try:
    try_end_19:;
    // Restore previous exception id 5.
    SET_CURRENT_EXCEPTION(exception_preserved_type_5, exception_preserved_value_5, exception_preserved_tb_5);

    goto try_end_18;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_18:;
    goto try_end_20;
    // Exception handler code:
    try_except_handler_19:;
    exception_keeper_type_20 = exception_type;
    exception_keeper_value_20 = exception_value;
    exception_keeper_tb_20 = exception_tb;
    exception_keeper_lineno_20 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_20;
        nuitka_bool tmp_cmp_expr_left_14;
        nuitka_bool tmp_cmp_expr_right_14;
        assert(tmp_with_5__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_14 = tmp_with_5__indicator;
        tmp_cmp_expr_right_14 = NUITKA_BOOL_TRUE;
        tmp_condition_result_20 = (tmp_cmp_expr_left_14 == tmp_cmp_expr_right_14) ? true : false;
        if (tmp_condition_result_20 != false) {
            goto branch_yes_20;
        } else {
            goto branch_no_20;
        }
    }
    branch_yes_20:;
    {
        PyObject *tmp_called_value_70;
        PyObject *tmp_call_result_50;
        CHECK_OBJECT(tmp_with_5__exit);
        tmp_called_value_70 = tmp_with_5__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 509;
        tmp_call_result_50 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_70, mod_consts[74]);

        if (tmp_call_result_50 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_20);
            Py_XDECREF(exception_keeper_value_20);
            Py_XDECREF(exception_keeper_tb_20);

            exception_lineno = 509;

            goto try_except_handler_18;
        }
        Py_DECREF(tmp_call_result_50);
    }
    branch_no_20:;
    // Re-raise.
    exception_type = exception_keeper_type_20;
    exception_value = exception_keeper_value_20;
    exception_tb = exception_keeper_tb_20;
    exception_lineno = exception_keeper_lineno_20;

    goto try_except_handler_18;
    // End of try:
    try_end_20:;
    {
        bool tmp_condition_result_21;
        nuitka_bool tmp_cmp_expr_left_15;
        nuitka_bool tmp_cmp_expr_right_15;
        assert(tmp_with_5__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_15 = tmp_with_5__indicator;
        tmp_cmp_expr_right_15 = NUITKA_BOOL_TRUE;
        tmp_condition_result_21 = (tmp_cmp_expr_left_15 == tmp_cmp_expr_right_15) ? true : false;
        if (tmp_condition_result_21 != false) {
            goto branch_yes_21;
        } else {
            goto branch_no_21;
        }
    }
    branch_yes_21:;
    {
        PyObject *tmp_called_value_71;
        PyObject *tmp_call_result_51;
        CHECK_OBJECT(tmp_with_5__exit);
        tmp_called_value_71 = tmp_with_5__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 509;
        tmp_call_result_51 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_71, mod_consts[74]);

        if (tmp_call_result_51 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 509;

            goto try_except_handler_18;
        }
        Py_DECREF(tmp_call_result_51);
    }
    branch_no_21:;
    goto try_end_21;
    // Exception handler code:
    try_except_handler_18:;
    exception_keeper_type_21 = exception_type;
    exception_keeper_value_21 = exception_value;
    exception_keeper_tb_21 = exception_tb;
    exception_keeper_lineno_21 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_5__source);
    tmp_with_5__source = NULL;
    Py_XDECREF(tmp_with_5__enter);
    tmp_with_5__enter = NULL;
    Py_XDECREF(tmp_with_5__exit);
    tmp_with_5__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_21;
    exception_value = exception_keeper_value_21;
    exception_tb = exception_keeper_tb_21;
    exception_lineno = exception_keeper_lineno_21;

    goto frame_exception_exit_1;
    // End of try:
    try_end_21:;
    CHECK_OBJECT(tmp_with_5__source);
    Py_DECREF(tmp_with_5__source);
    tmp_with_5__source = NULL;
    CHECK_OBJECT(tmp_with_5__enter);
    Py_DECREF(tmp_with_5__enter);
    tmp_with_5__enter = NULL;
    Py_XDECREF(tmp_with_5__exit);
    tmp_with_5__exit = NULL;
    {
        PyObject *tmp_assign_source_88;
        tmp_assign_source_88 = mod_consts[220];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[221], tmp_assign_source_88);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_89;
        PyObject *tmp_called_instance_6;
        tmp_called_instance_6 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_6 == NULL)) {
            tmp_called_instance_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 520;

            goto try_except_handler_22;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 520;
        tmp_assign_source_89 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_6,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[199], 0)
        );

        if (tmp_assign_source_89 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 520;

            goto try_except_handler_22;
        }
        assert(tmp_with_6__source == NULL);
        tmp_with_6__source = tmp_assign_source_89;
    }
    {
        PyObject *tmp_assign_source_90;
        PyObject *tmp_called_value_72;
        PyObject *tmp_expression_value_53;
        CHECK_OBJECT(tmp_with_6__source);
        tmp_expression_value_53 = tmp_with_6__source;
        tmp_called_value_72 = LOOKUP_SPECIAL(tmp_expression_value_53, mod_consts[67]);
        if (tmp_called_value_72 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 520;

            goto try_except_handler_22;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 520;
        tmp_assign_source_90 = CALL_FUNCTION_NO_ARGS(tmp_called_value_72);
        Py_DECREF(tmp_called_value_72);
        if (tmp_assign_source_90 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 520;

            goto try_except_handler_22;
        }
        assert(tmp_with_6__enter == NULL);
        tmp_with_6__enter = tmp_assign_source_90;
    }
    {
        PyObject *tmp_assign_source_91;
        PyObject *tmp_expression_value_54;
        CHECK_OBJECT(tmp_with_6__source);
        tmp_expression_value_54 = tmp_with_6__source;
        tmp_assign_source_91 = LOOKUP_SPECIAL(tmp_expression_value_54, mod_consts[68]);
        if (tmp_assign_source_91 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 520;

            goto try_except_handler_22;
        }
        assert(tmp_with_6__exit == NULL);
        tmp_with_6__exit = tmp_assign_source_91;
    }
    {
        nuitka_bool tmp_assign_source_92;
        tmp_assign_source_92 = NUITKA_BOOL_TRUE;
        tmp_with_6__indicator = tmp_assign_source_92;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_73;
        PyObject *tmp_expression_value_55;
        PyObject *tmp_call_result_52;
        PyObject *tmp_kw_call_arg_value_0_35;
        PyObject *tmp_kw_call_arg_value_1_35;
        PyObject *tmp_kw_call_arg_value_2_35;
        PyObject *tmp_kw_call_dict_value_0_35;
        PyObject *tmp_called_value_74;
        PyObject *tmp_call_arg_element_8;
        tmp_expression_value_55 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_55 == NULL)) {
            tmp_expression_value_55 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_55 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 521;

            goto try_except_handler_24;
        }
        tmp_called_value_73 = LOOKUP_ATTRIBUTE(tmp_expression_value_55, mod_consts[69]);
        if (tmp_called_value_73 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 521;

            goto try_except_handler_24;
        }
        tmp_kw_call_arg_value_0_35 = mod_consts[221];
        tmp_kw_call_arg_value_1_35 = mod_consts[22];
        tmp_kw_call_arg_value_2_35 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[221]);

        if (unlikely(tmp_kw_call_arg_value_2_35 == NULL)) {
            tmp_kw_call_arg_value_2_35 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[221]);
        }

        if (tmp_kw_call_arg_value_2_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_73);

            exception_lineno = 524;

            goto try_except_handler_24;
        }
        tmp_called_value_74 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_74 == NULL)) {
            tmp_called_value_74 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_74 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_73);

            exception_lineno = 525;

            goto try_except_handler_24;
        }
        tmp_call_arg_element_8 = LIST_COPY(mod_consts[222]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 525;
        tmp_kw_call_dict_value_0_35 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_74, tmp_call_arg_element_8);
        Py_DECREF(tmp_call_arg_element_8);
        if (tmp_kw_call_dict_value_0_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_73);

            exception_lineno = 525;

            goto try_except_handler_24;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 521;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_35, tmp_kw_call_arg_value_1_35, tmp_kw_call_arg_value_2_35};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_35};
            tmp_call_result_52 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_73, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_73);
        Py_DECREF(tmp_kw_call_dict_value_0_35);
        if (tmp_call_result_52 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 521;

            goto try_except_handler_24;
        }
        Py_DECREF(tmp_call_result_52);
    }
    goto try_end_22;
    // Exception handler code:
    try_except_handler_24:;
    exception_keeper_type_22 = exception_type;
    exception_keeper_value_22 = exception_value;
    exception_keeper_tb_22 = exception_tb;
    exception_keeper_lineno_22 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 6.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_6, &exception_preserved_value_6, &exception_preserved_tb_6);

    if (exception_keeper_tb_22 == NULL) {
        exception_keeper_tb_22 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_22);
    } else if (exception_keeper_lineno_22 != 0) {
        exception_keeper_tb_22 = ADD_TRACEBACK(exception_keeper_tb_22, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_22);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_22, &exception_keeper_value_22, &exception_keeper_tb_22);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_22, exception_keeper_tb_22);
    PUBLISH_EXCEPTION(&exception_keeper_type_22, &exception_keeper_value_22, &exception_keeper_tb_22);
    // Tried code:
    {
        bool tmp_condition_result_22;
        PyObject *tmp_cmp_expr_left_16;
        PyObject *tmp_cmp_expr_right_16;
        tmp_cmp_expr_left_16 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_16 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_16, tmp_cmp_expr_right_16);
        assert(!(tmp_res == -1));
        tmp_condition_result_22 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_22 != false) {
            goto branch_yes_22;
        } else {
            goto branch_no_22;
        }
    }
    branch_yes_22:;
    {
        nuitka_bool tmp_assign_source_93;
        tmp_assign_source_93 = NUITKA_BOOL_FALSE;
        tmp_with_6__indicator = tmp_assign_source_93;
    }
    {
        bool tmp_condition_result_23;
        PyObject *tmp_operand_value_6;
        PyObject *tmp_called_value_75;
        PyObject *tmp_args_element_value_29;
        PyObject *tmp_args_element_value_30;
        PyObject *tmp_args_element_value_31;
        CHECK_OBJECT(tmp_with_6__exit);
        tmp_called_value_75 = tmp_with_6__exit;
        tmp_args_element_value_29 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_30 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_31 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 525;
        {
            PyObject *call_args[] = {tmp_args_element_value_29, tmp_args_element_value_30, tmp_args_element_value_31};
            tmp_operand_value_6 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_75, call_args);
        }

        if (tmp_operand_value_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 525;

            goto try_except_handler_25;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_6);
        Py_DECREF(tmp_operand_value_6);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 525;

            goto try_except_handler_25;
        }
        tmp_condition_result_23 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_23 != false) {
            goto branch_yes_23;
        } else {
            goto branch_no_23;
        }
    }
    branch_yes_23:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 525;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_25;
    branch_no_23:;
    goto branch_end_22;
    branch_no_22:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 520;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_25;
    branch_end_22:;
    goto try_end_23;
    // Exception handler code:
    try_except_handler_25:;
    exception_keeper_type_23 = exception_type;
    exception_keeper_value_23 = exception_value;
    exception_keeper_tb_23 = exception_tb;
    exception_keeper_lineno_23 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 6.
    SET_CURRENT_EXCEPTION(exception_preserved_type_6, exception_preserved_value_6, exception_preserved_tb_6);

    // Re-raise.
    exception_type = exception_keeper_type_23;
    exception_value = exception_keeper_value_23;
    exception_tb = exception_keeper_tb_23;
    exception_lineno = exception_keeper_lineno_23;

    goto try_except_handler_23;
    // End of try:
    try_end_23:;
    // Restore previous exception id 6.
    SET_CURRENT_EXCEPTION(exception_preserved_type_6, exception_preserved_value_6, exception_preserved_tb_6);

    goto try_end_22;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_22:;
    goto try_end_24;
    // Exception handler code:
    try_except_handler_23:;
    exception_keeper_type_24 = exception_type;
    exception_keeper_value_24 = exception_value;
    exception_keeper_tb_24 = exception_tb;
    exception_keeper_lineno_24 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_24;
        nuitka_bool tmp_cmp_expr_left_17;
        nuitka_bool tmp_cmp_expr_right_17;
        assert(tmp_with_6__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_17 = tmp_with_6__indicator;
        tmp_cmp_expr_right_17 = NUITKA_BOOL_TRUE;
        tmp_condition_result_24 = (tmp_cmp_expr_left_17 == tmp_cmp_expr_right_17) ? true : false;
        if (tmp_condition_result_24 != false) {
            goto branch_yes_24;
        } else {
            goto branch_no_24;
        }
    }
    branch_yes_24:;
    {
        PyObject *tmp_called_value_76;
        PyObject *tmp_call_result_53;
        CHECK_OBJECT(tmp_with_6__exit);
        tmp_called_value_76 = tmp_with_6__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 525;
        tmp_call_result_53 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_76, mod_consts[74]);

        if (tmp_call_result_53 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_24);
            Py_XDECREF(exception_keeper_value_24);
            Py_XDECREF(exception_keeper_tb_24);

            exception_lineno = 525;

            goto try_except_handler_22;
        }
        Py_DECREF(tmp_call_result_53);
    }
    branch_no_24:;
    // Re-raise.
    exception_type = exception_keeper_type_24;
    exception_value = exception_keeper_value_24;
    exception_tb = exception_keeper_tb_24;
    exception_lineno = exception_keeper_lineno_24;

    goto try_except_handler_22;
    // End of try:
    try_end_24:;
    {
        bool tmp_condition_result_25;
        nuitka_bool tmp_cmp_expr_left_18;
        nuitka_bool tmp_cmp_expr_right_18;
        assert(tmp_with_6__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_18 = tmp_with_6__indicator;
        tmp_cmp_expr_right_18 = NUITKA_BOOL_TRUE;
        tmp_condition_result_25 = (tmp_cmp_expr_left_18 == tmp_cmp_expr_right_18) ? true : false;
        if (tmp_condition_result_25 != false) {
            goto branch_yes_25;
        } else {
            goto branch_no_25;
        }
    }
    branch_yes_25:;
    {
        PyObject *tmp_called_value_77;
        PyObject *tmp_call_result_54;
        CHECK_OBJECT(tmp_with_6__exit);
        tmp_called_value_77 = tmp_with_6__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 525;
        tmp_call_result_54 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_77, mod_consts[74]);

        if (tmp_call_result_54 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 525;

            goto try_except_handler_22;
        }
        Py_DECREF(tmp_call_result_54);
    }
    branch_no_25:;
    goto try_end_25;
    // Exception handler code:
    try_except_handler_22:;
    exception_keeper_type_25 = exception_type;
    exception_keeper_value_25 = exception_value;
    exception_keeper_tb_25 = exception_tb;
    exception_keeper_lineno_25 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_6__source);
    tmp_with_6__source = NULL;
    Py_XDECREF(tmp_with_6__enter);
    tmp_with_6__enter = NULL;
    Py_XDECREF(tmp_with_6__exit);
    tmp_with_6__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_25;
    exception_value = exception_keeper_value_25;
    exception_tb = exception_keeper_tb_25;
    exception_lineno = exception_keeper_lineno_25;

    goto frame_exception_exit_1;
    // End of try:
    try_end_25:;
    CHECK_OBJECT(tmp_with_6__source);
    Py_DECREF(tmp_with_6__source);
    tmp_with_6__source = NULL;
    CHECK_OBJECT(tmp_with_6__enter);
    Py_DECREF(tmp_with_6__enter);
    tmp_with_6__enter = NULL;
    Py_XDECREF(tmp_with_6__exit);
    tmp_with_6__exit = NULL;
    {
        PyObject *tmp_assign_source_94;
        tmp_assign_source_94 = mod_consts[223];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[224], tmp_assign_source_94);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_95;
        PyObject *tmp_called_instance_7;
        tmp_called_instance_7 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_7 == NULL)) {
            tmp_called_instance_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 534;

            goto try_except_handler_26;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 534;
        tmp_assign_source_95 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_7,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[199], 0)
        );

        if (tmp_assign_source_95 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 534;

            goto try_except_handler_26;
        }
        assert(tmp_with_7__source == NULL);
        tmp_with_7__source = tmp_assign_source_95;
    }
    {
        PyObject *tmp_assign_source_96;
        PyObject *tmp_called_value_78;
        PyObject *tmp_expression_value_56;
        CHECK_OBJECT(tmp_with_7__source);
        tmp_expression_value_56 = tmp_with_7__source;
        tmp_called_value_78 = LOOKUP_SPECIAL(tmp_expression_value_56, mod_consts[67]);
        if (tmp_called_value_78 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 534;

            goto try_except_handler_26;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 534;
        tmp_assign_source_96 = CALL_FUNCTION_NO_ARGS(tmp_called_value_78);
        Py_DECREF(tmp_called_value_78);
        if (tmp_assign_source_96 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 534;

            goto try_except_handler_26;
        }
        assert(tmp_with_7__enter == NULL);
        tmp_with_7__enter = tmp_assign_source_96;
    }
    {
        PyObject *tmp_assign_source_97;
        PyObject *tmp_expression_value_57;
        CHECK_OBJECT(tmp_with_7__source);
        tmp_expression_value_57 = tmp_with_7__source;
        tmp_assign_source_97 = LOOKUP_SPECIAL(tmp_expression_value_57, mod_consts[68]);
        if (tmp_assign_source_97 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 534;

            goto try_except_handler_26;
        }
        assert(tmp_with_7__exit == NULL);
        tmp_with_7__exit = tmp_assign_source_97;
    }
    {
        nuitka_bool tmp_assign_source_98;
        tmp_assign_source_98 = NUITKA_BOOL_TRUE;
        tmp_with_7__indicator = tmp_assign_source_98;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_79;
        PyObject *tmp_expression_value_58;
        PyObject *tmp_call_result_55;
        PyObject *tmp_kw_call_arg_value_0_36;
        PyObject *tmp_kw_call_arg_value_1_36;
        PyObject *tmp_kw_call_arg_value_2_36;
        PyObject *tmp_kw_call_dict_value_0_36;
        PyObject *tmp_called_value_80;
        PyObject *tmp_call_arg_element_9;
        tmp_expression_value_58 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_58 == NULL)) {
            tmp_expression_value_58 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_58 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 535;

            goto try_except_handler_28;
        }
        tmp_called_value_79 = LOOKUP_ATTRIBUTE(tmp_expression_value_58, mod_consts[69]);
        if (tmp_called_value_79 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 535;

            goto try_except_handler_28;
        }
        tmp_kw_call_arg_value_0_36 = mod_consts[225];
        tmp_kw_call_arg_value_1_36 = mod_consts[226];
        tmp_kw_call_arg_value_2_36 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[224]);

        if (unlikely(tmp_kw_call_arg_value_2_36 == NULL)) {
            tmp_kw_call_arg_value_2_36 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[224]);
        }

        if (tmp_kw_call_arg_value_2_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_79);

            exception_lineno = 538;

            goto try_except_handler_28;
        }
        tmp_called_value_80 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_80 == NULL)) {
            tmp_called_value_80 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_80 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_79);

            exception_lineno = 539;

            goto try_except_handler_28;
        }
        tmp_call_arg_element_9 = LIST_COPY(mod_consts[227]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 539;
        tmp_kw_call_dict_value_0_36 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_80, tmp_call_arg_element_9);
        Py_DECREF(tmp_call_arg_element_9);
        if (tmp_kw_call_dict_value_0_36 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_79);

            exception_lineno = 539;

            goto try_except_handler_28;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 535;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_36, tmp_kw_call_arg_value_1_36, tmp_kw_call_arg_value_2_36};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_36};
            tmp_call_result_55 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_79, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_79);
        Py_DECREF(tmp_kw_call_dict_value_0_36);
        if (tmp_call_result_55 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 535;

            goto try_except_handler_28;
        }
        Py_DECREF(tmp_call_result_55);
    }
    goto try_end_26;
    // Exception handler code:
    try_except_handler_28:;
    exception_keeper_type_26 = exception_type;
    exception_keeper_value_26 = exception_value;
    exception_keeper_tb_26 = exception_tb;
    exception_keeper_lineno_26 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 7.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_7, &exception_preserved_value_7, &exception_preserved_tb_7);

    if (exception_keeper_tb_26 == NULL) {
        exception_keeper_tb_26 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_26);
    } else if (exception_keeper_lineno_26 != 0) {
        exception_keeper_tb_26 = ADD_TRACEBACK(exception_keeper_tb_26, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_26);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_26, &exception_keeper_value_26, &exception_keeper_tb_26);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_26, exception_keeper_tb_26);
    PUBLISH_EXCEPTION(&exception_keeper_type_26, &exception_keeper_value_26, &exception_keeper_tb_26);
    // Tried code:
    {
        bool tmp_condition_result_26;
        PyObject *tmp_cmp_expr_left_19;
        PyObject *tmp_cmp_expr_right_19;
        tmp_cmp_expr_left_19 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_19 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_19, tmp_cmp_expr_right_19);
        assert(!(tmp_res == -1));
        tmp_condition_result_26 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_26 != false) {
            goto branch_yes_26;
        } else {
            goto branch_no_26;
        }
    }
    branch_yes_26:;
    {
        nuitka_bool tmp_assign_source_99;
        tmp_assign_source_99 = NUITKA_BOOL_FALSE;
        tmp_with_7__indicator = tmp_assign_source_99;
    }
    {
        bool tmp_condition_result_27;
        PyObject *tmp_operand_value_7;
        PyObject *tmp_called_value_81;
        PyObject *tmp_args_element_value_32;
        PyObject *tmp_args_element_value_33;
        PyObject *tmp_args_element_value_34;
        CHECK_OBJECT(tmp_with_7__exit);
        tmp_called_value_81 = tmp_with_7__exit;
        tmp_args_element_value_32 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_33 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_34 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 539;
        {
            PyObject *call_args[] = {tmp_args_element_value_32, tmp_args_element_value_33, tmp_args_element_value_34};
            tmp_operand_value_7 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_81, call_args);
        }

        if (tmp_operand_value_7 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 539;

            goto try_except_handler_29;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_7);
        Py_DECREF(tmp_operand_value_7);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 539;

            goto try_except_handler_29;
        }
        tmp_condition_result_27 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_27 != false) {
            goto branch_yes_27;
        } else {
            goto branch_no_27;
        }
    }
    branch_yes_27:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 539;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_29;
    branch_no_27:;
    goto branch_end_26;
    branch_no_26:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 534;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_29;
    branch_end_26:;
    goto try_end_27;
    // Exception handler code:
    try_except_handler_29:;
    exception_keeper_type_27 = exception_type;
    exception_keeper_value_27 = exception_value;
    exception_keeper_tb_27 = exception_tb;
    exception_keeper_lineno_27 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 7.
    SET_CURRENT_EXCEPTION(exception_preserved_type_7, exception_preserved_value_7, exception_preserved_tb_7);

    // Re-raise.
    exception_type = exception_keeper_type_27;
    exception_value = exception_keeper_value_27;
    exception_tb = exception_keeper_tb_27;
    exception_lineno = exception_keeper_lineno_27;

    goto try_except_handler_27;
    // End of try:
    try_end_27:;
    // Restore previous exception id 7.
    SET_CURRENT_EXCEPTION(exception_preserved_type_7, exception_preserved_value_7, exception_preserved_tb_7);

    goto try_end_26;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_26:;
    goto try_end_28;
    // Exception handler code:
    try_except_handler_27:;
    exception_keeper_type_28 = exception_type;
    exception_keeper_value_28 = exception_value;
    exception_keeper_tb_28 = exception_tb;
    exception_keeper_lineno_28 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_28;
        nuitka_bool tmp_cmp_expr_left_20;
        nuitka_bool tmp_cmp_expr_right_20;
        assert(tmp_with_7__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_20 = tmp_with_7__indicator;
        tmp_cmp_expr_right_20 = NUITKA_BOOL_TRUE;
        tmp_condition_result_28 = (tmp_cmp_expr_left_20 == tmp_cmp_expr_right_20) ? true : false;
        if (tmp_condition_result_28 != false) {
            goto branch_yes_28;
        } else {
            goto branch_no_28;
        }
    }
    branch_yes_28:;
    {
        PyObject *tmp_called_value_82;
        PyObject *tmp_call_result_56;
        CHECK_OBJECT(tmp_with_7__exit);
        tmp_called_value_82 = tmp_with_7__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 539;
        tmp_call_result_56 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_82, mod_consts[74]);

        if (tmp_call_result_56 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_28);
            Py_XDECREF(exception_keeper_value_28);
            Py_XDECREF(exception_keeper_tb_28);

            exception_lineno = 539;

            goto try_except_handler_26;
        }
        Py_DECREF(tmp_call_result_56);
    }
    branch_no_28:;
    // Re-raise.
    exception_type = exception_keeper_type_28;
    exception_value = exception_keeper_value_28;
    exception_tb = exception_keeper_tb_28;
    exception_lineno = exception_keeper_lineno_28;

    goto try_except_handler_26;
    // End of try:
    try_end_28:;
    {
        bool tmp_condition_result_29;
        nuitka_bool tmp_cmp_expr_left_21;
        nuitka_bool tmp_cmp_expr_right_21;
        assert(tmp_with_7__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_21 = tmp_with_7__indicator;
        tmp_cmp_expr_right_21 = NUITKA_BOOL_TRUE;
        tmp_condition_result_29 = (tmp_cmp_expr_left_21 == tmp_cmp_expr_right_21) ? true : false;
        if (tmp_condition_result_29 != false) {
            goto branch_yes_29;
        } else {
            goto branch_no_29;
        }
    }
    branch_yes_29:;
    {
        PyObject *tmp_called_value_83;
        PyObject *tmp_call_result_57;
        CHECK_OBJECT(tmp_with_7__exit);
        tmp_called_value_83 = tmp_with_7__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 539;
        tmp_call_result_57 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_83, mod_consts[74]);

        if (tmp_call_result_57 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 539;

            goto try_except_handler_26;
        }
        Py_DECREF(tmp_call_result_57);
    }
    branch_no_29:;
    goto try_end_29;
    // Exception handler code:
    try_except_handler_26:;
    exception_keeper_type_29 = exception_type;
    exception_keeper_value_29 = exception_value;
    exception_keeper_tb_29 = exception_tb;
    exception_keeper_lineno_29 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_7__source);
    tmp_with_7__source = NULL;
    Py_XDECREF(tmp_with_7__enter);
    tmp_with_7__enter = NULL;
    Py_XDECREF(tmp_with_7__exit);
    tmp_with_7__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_29;
    exception_value = exception_keeper_value_29;
    exception_tb = exception_keeper_tb_29;
    exception_lineno = exception_keeper_lineno_29;

    goto frame_exception_exit_1;
    // End of try:
    try_end_29:;
    CHECK_OBJECT(tmp_with_7__source);
    Py_DECREF(tmp_with_7__source);
    tmp_with_7__source = NULL;
    CHECK_OBJECT(tmp_with_7__enter);
    Py_DECREF(tmp_with_7__enter);
    tmp_with_7__enter = NULL;
    Py_XDECREF(tmp_with_7__exit);
    tmp_with_7__exit = NULL;
    {
        PyObject *tmp_assign_source_100;
        tmp_assign_source_100 = mod_consts[228];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229], tmp_assign_source_100);
    }
    {
        PyObject *tmp_assign_source_101;
        tmp_assign_source_101 = LIST_COPY(mod_consts[230]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[231], tmp_assign_source_101);
    }
    {
        PyObject *tmp_assign_source_102;
        tmp_assign_source_102 = LIST_COPY(mod_consts[232]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[233], tmp_assign_source_102);
    }
    {
        PyObject *tmp_assign_source_103;
        tmp_assign_source_103 = LIST_COPY(mod_consts[232]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[234], tmp_assign_source_103);
    }
    {
        PyObject *tmp_assign_source_104;
        tmp_assign_source_104 = LIST_COPY(mod_consts[235]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[236], tmp_assign_source_104);
    }
    {
        PyObject *tmp_assign_source_105;
        tmp_assign_source_105 = LIST_COPY(mod_consts[237]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[238], tmp_assign_source_105);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_106;
        PyObject *tmp_called_instance_8;
        tmp_called_instance_8 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_8 == NULL)) {
            tmp_called_instance_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 556;

            goto try_except_handler_30;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 556;
        tmp_assign_source_106 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_8,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[239], 0)
        );

        if (tmp_assign_source_106 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 556;

            goto try_except_handler_30;
        }
        assert(tmp_with_8__source == NULL);
        tmp_with_8__source = tmp_assign_source_106;
    }
    {
        PyObject *tmp_assign_source_107;
        PyObject *tmp_called_value_84;
        PyObject *tmp_expression_value_59;
        CHECK_OBJECT(tmp_with_8__source);
        tmp_expression_value_59 = tmp_with_8__source;
        tmp_called_value_84 = LOOKUP_SPECIAL(tmp_expression_value_59, mod_consts[67]);
        if (tmp_called_value_84 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 556;

            goto try_except_handler_30;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 556;
        tmp_assign_source_107 = CALL_FUNCTION_NO_ARGS(tmp_called_value_84);
        Py_DECREF(tmp_called_value_84);
        if (tmp_assign_source_107 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 556;

            goto try_except_handler_30;
        }
        assert(tmp_with_8__enter == NULL);
        tmp_with_8__enter = tmp_assign_source_107;
    }
    {
        PyObject *tmp_assign_source_108;
        PyObject *tmp_expression_value_60;
        CHECK_OBJECT(tmp_with_8__source);
        tmp_expression_value_60 = tmp_with_8__source;
        tmp_assign_source_108 = LOOKUP_SPECIAL(tmp_expression_value_60, mod_consts[68]);
        if (tmp_assign_source_108 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 556;

            goto try_except_handler_30;
        }
        assert(tmp_with_8__exit == NULL);
        tmp_with_8__exit = tmp_assign_source_108;
    }
    {
        nuitka_bool tmp_assign_source_109;
        tmp_assign_source_109 = NUITKA_BOOL_TRUE;
        tmp_with_8__indicator = tmp_assign_source_109;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_85;
        PyObject *tmp_expression_value_61;
        PyObject *tmp_call_result_58;
        PyObject *tmp_kw_call_arg_value_0_37;
        PyObject *tmp_kw_call_arg_value_1_37;
        PyObject *tmp_kw_call_arg_value_2_37;
        PyObject *tmp_called_value_86;
        PyObject *tmp_expression_value_62;
        PyObject *tmp_kw_call_value_0_3;
        PyObject *tmp_kw_call_value_1_2;
        PyObject *tmp_str_arg_value_1;
        PyObject *tmp_iterable_value_1;
        PyObject *tmp_kw_call_dict_value_0_37;
        PyObject *tmp_called_value_87;
        PyObject *tmp_args_element_value_35;
        PyObject *tmp_add_expr_left_1;
        PyObject *tmp_add_expr_right_1;
        tmp_expression_value_61 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_61 == NULL)) {
            tmp_expression_value_61 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_61 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 557;

            goto try_except_handler_32;
        }
        tmp_called_value_85 = LOOKUP_ATTRIBUTE(tmp_expression_value_61, mod_consts[69]);
        if (tmp_called_value_85 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 557;

            goto try_except_handler_32;
        }
        tmp_kw_call_arg_value_0_37 = mod_consts[240];
        tmp_kw_call_arg_value_1_37 = mod_consts[241];
        tmp_expression_value_62 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229]);

        if (unlikely(tmp_expression_value_62 == NULL)) {
            tmp_expression_value_62 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[229]);
        }

        if (tmp_expression_value_62 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);

            exception_lineno = 560;

            goto try_except_handler_32;
        }
        tmp_called_value_86 = LOOKUP_ATTRIBUTE(tmp_expression_value_62, mod_consts[242]);
        if (tmp_called_value_86 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);

            exception_lineno = 560;

            goto try_except_handler_32;
        }
        tmp_kw_call_value_0_3 = mod_consts[243];
        tmp_str_arg_value_1 = mod_consts[244];
        tmp_iterable_value_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[231]);

        if (unlikely(tmp_iterable_value_1 == NULL)) {
            tmp_iterable_value_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[231]);
        }

        if (tmp_iterable_value_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_called_value_86);

            exception_lineno = 560;

            goto try_except_handler_32;
        }
        tmp_kw_call_value_1_2 = UNICODE_JOIN(tmp_str_arg_value_1, tmp_iterable_value_1);
        if (tmp_kw_call_value_1_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_called_value_86);

            exception_lineno = 560;

            goto try_except_handler_32;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 560;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_3, tmp_kw_call_value_1_2};

            tmp_kw_call_arg_value_2_37 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_86, kw_values, mod_consts[245]);
        }

        Py_DECREF(tmp_called_value_86);
        Py_DECREF(tmp_kw_call_value_1_2);
        if (tmp_kw_call_arg_value_2_37 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);

            exception_lineno = 560;

            goto try_except_handler_32;
        }
        tmp_called_value_87 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_87 == NULL)) {
            tmp_called_value_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_87 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_kw_call_arg_value_2_37);

            exception_lineno = 561;

            goto try_except_handler_32;
        }
        tmp_add_expr_left_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[231]);

        if (unlikely(tmp_add_expr_left_1 == NULL)) {
            tmp_add_expr_left_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[231]);
        }

        if (tmp_add_expr_left_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_kw_call_arg_value_2_37);

            exception_lineno = 561;

            goto try_except_handler_32;
        }
        tmp_add_expr_right_1 = LIST_COPY(mod_consts[246]);
        tmp_args_element_value_35 = BINARY_OPERATION_ADD_OBJECT_OBJECT_LIST(tmp_add_expr_left_1, tmp_add_expr_right_1);
        Py_DECREF(tmp_add_expr_right_1);
        if (tmp_args_element_value_35 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_kw_call_arg_value_2_37);

            exception_lineno = 561;

            goto try_except_handler_32;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 561;
        tmp_kw_call_dict_value_0_37 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_87, tmp_args_element_value_35);
        Py_DECREF(tmp_args_element_value_35);
        if (tmp_kw_call_dict_value_0_37 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_85);
            Py_DECREF(tmp_kw_call_arg_value_2_37);

            exception_lineno = 561;

            goto try_except_handler_32;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 557;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_37, tmp_kw_call_arg_value_1_37, tmp_kw_call_arg_value_2_37};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_37};
            tmp_call_result_58 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_85, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_85);
        Py_DECREF(tmp_kw_call_arg_value_2_37);
        Py_DECREF(tmp_kw_call_dict_value_0_37);
        if (tmp_call_result_58 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 557;

            goto try_except_handler_32;
        }
        Py_DECREF(tmp_call_result_58);
    }
    goto try_end_30;
    // Exception handler code:
    try_except_handler_32:;
    exception_keeper_type_30 = exception_type;
    exception_keeper_value_30 = exception_value;
    exception_keeper_tb_30 = exception_tb;
    exception_keeper_lineno_30 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 8.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_8, &exception_preserved_value_8, &exception_preserved_tb_8);

    if (exception_keeper_tb_30 == NULL) {
        exception_keeper_tb_30 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_30);
    } else if (exception_keeper_lineno_30 != 0) {
        exception_keeper_tb_30 = ADD_TRACEBACK(exception_keeper_tb_30, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_30);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_30, &exception_keeper_value_30, &exception_keeper_tb_30);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_30, exception_keeper_tb_30);
    PUBLISH_EXCEPTION(&exception_keeper_type_30, &exception_keeper_value_30, &exception_keeper_tb_30);
    // Tried code:
    {
        bool tmp_condition_result_30;
        PyObject *tmp_cmp_expr_left_22;
        PyObject *tmp_cmp_expr_right_22;
        tmp_cmp_expr_left_22 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_22 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_22, tmp_cmp_expr_right_22);
        assert(!(tmp_res == -1));
        tmp_condition_result_30 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_30 != false) {
            goto branch_yes_30;
        } else {
            goto branch_no_30;
        }
    }
    branch_yes_30:;
    {
        nuitka_bool tmp_assign_source_110;
        tmp_assign_source_110 = NUITKA_BOOL_FALSE;
        tmp_with_8__indicator = tmp_assign_source_110;
    }
    {
        bool tmp_condition_result_31;
        PyObject *tmp_operand_value_8;
        PyObject *tmp_called_value_88;
        PyObject *tmp_args_element_value_36;
        PyObject *tmp_args_element_value_37;
        PyObject *tmp_args_element_value_38;
        CHECK_OBJECT(tmp_with_8__exit);
        tmp_called_value_88 = tmp_with_8__exit;
        tmp_args_element_value_36 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_37 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_38 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 561;
        {
            PyObject *call_args[] = {tmp_args_element_value_36, tmp_args_element_value_37, tmp_args_element_value_38};
            tmp_operand_value_8 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_88, call_args);
        }

        if (tmp_operand_value_8 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 561;

            goto try_except_handler_33;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_8);
        Py_DECREF(tmp_operand_value_8);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 561;

            goto try_except_handler_33;
        }
        tmp_condition_result_31 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_31 != false) {
            goto branch_yes_31;
        } else {
            goto branch_no_31;
        }
    }
    branch_yes_31:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 561;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_33;
    branch_no_31:;
    goto branch_end_30;
    branch_no_30:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 556;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_33;
    branch_end_30:;
    goto try_end_31;
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

    // Restore previous exception id 8.
    SET_CURRENT_EXCEPTION(exception_preserved_type_8, exception_preserved_value_8, exception_preserved_tb_8);

    // Re-raise.
    exception_type = exception_keeper_type_31;
    exception_value = exception_keeper_value_31;
    exception_tb = exception_keeper_tb_31;
    exception_lineno = exception_keeper_lineno_31;

    goto try_except_handler_31;
    // End of try:
    try_end_31:;
    // Restore previous exception id 8.
    SET_CURRENT_EXCEPTION(exception_preserved_type_8, exception_preserved_value_8, exception_preserved_tb_8);

    goto try_end_30;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_30:;
    goto try_end_32;
    // Exception handler code:
    try_except_handler_31:;
    exception_keeper_type_32 = exception_type;
    exception_keeper_value_32 = exception_value;
    exception_keeper_tb_32 = exception_tb;
    exception_keeper_lineno_32 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_32;
        nuitka_bool tmp_cmp_expr_left_23;
        nuitka_bool tmp_cmp_expr_right_23;
        assert(tmp_with_8__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_23 = tmp_with_8__indicator;
        tmp_cmp_expr_right_23 = NUITKA_BOOL_TRUE;
        tmp_condition_result_32 = (tmp_cmp_expr_left_23 == tmp_cmp_expr_right_23) ? true : false;
        if (tmp_condition_result_32 != false) {
            goto branch_yes_32;
        } else {
            goto branch_no_32;
        }
    }
    branch_yes_32:;
    {
        PyObject *tmp_called_value_89;
        PyObject *tmp_call_result_59;
        CHECK_OBJECT(tmp_with_8__exit);
        tmp_called_value_89 = tmp_with_8__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 561;
        tmp_call_result_59 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_89, mod_consts[74]);

        if (tmp_call_result_59 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_32);
            Py_XDECREF(exception_keeper_value_32);
            Py_XDECREF(exception_keeper_tb_32);

            exception_lineno = 561;

            goto try_except_handler_30;
        }
        Py_DECREF(tmp_call_result_59);
    }
    branch_no_32:;
    // Re-raise.
    exception_type = exception_keeper_type_32;
    exception_value = exception_keeper_value_32;
    exception_tb = exception_keeper_tb_32;
    exception_lineno = exception_keeper_lineno_32;

    goto try_except_handler_30;
    // End of try:
    try_end_32:;
    {
        bool tmp_condition_result_33;
        nuitka_bool tmp_cmp_expr_left_24;
        nuitka_bool tmp_cmp_expr_right_24;
        assert(tmp_with_8__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_24 = tmp_with_8__indicator;
        tmp_cmp_expr_right_24 = NUITKA_BOOL_TRUE;
        tmp_condition_result_33 = (tmp_cmp_expr_left_24 == tmp_cmp_expr_right_24) ? true : false;
        if (tmp_condition_result_33 != false) {
            goto branch_yes_33;
        } else {
            goto branch_no_33;
        }
    }
    branch_yes_33:;
    {
        PyObject *tmp_called_value_90;
        PyObject *tmp_call_result_60;
        CHECK_OBJECT(tmp_with_8__exit);
        tmp_called_value_90 = tmp_with_8__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 561;
        tmp_call_result_60 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_90, mod_consts[74]);

        if (tmp_call_result_60 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 561;

            goto try_except_handler_30;
        }
        Py_DECREF(tmp_call_result_60);
    }
    branch_no_33:;
    goto try_end_33;
    // Exception handler code:
    try_except_handler_30:;
    exception_keeper_type_33 = exception_type;
    exception_keeper_value_33 = exception_value;
    exception_keeper_tb_33 = exception_tb;
    exception_keeper_lineno_33 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_8__source);
    tmp_with_8__source = NULL;
    Py_XDECREF(tmp_with_8__enter);
    tmp_with_8__enter = NULL;
    Py_XDECREF(tmp_with_8__exit);
    tmp_with_8__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_33;
    exception_value = exception_keeper_value_33;
    exception_tb = exception_keeper_tb_33;
    exception_lineno = exception_keeper_lineno_33;

    goto frame_exception_exit_1;
    // End of try:
    try_end_33:;
    CHECK_OBJECT(tmp_with_8__source);
    Py_DECREF(tmp_with_8__source);
    tmp_with_8__source = NULL;
    CHECK_OBJECT(tmp_with_8__enter);
    Py_DECREF(tmp_with_8__enter);
    tmp_with_8__enter = NULL;
    Py_XDECREF(tmp_with_8__exit);
    tmp_with_8__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_111;
        PyObject *tmp_called_instance_9;
        tmp_called_instance_9 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_9 == NULL)) {
            tmp_called_instance_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 564;

            goto try_except_handler_34;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 564;
        tmp_assign_source_111 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_9,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[247], 0)
        );

        if (tmp_assign_source_111 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 564;

            goto try_except_handler_34;
        }
        assert(tmp_with_9__source == NULL);
        tmp_with_9__source = tmp_assign_source_111;
    }
    {
        PyObject *tmp_assign_source_112;
        PyObject *tmp_called_value_91;
        PyObject *tmp_expression_value_63;
        CHECK_OBJECT(tmp_with_9__source);
        tmp_expression_value_63 = tmp_with_9__source;
        tmp_called_value_91 = LOOKUP_SPECIAL(tmp_expression_value_63, mod_consts[67]);
        if (tmp_called_value_91 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 564;

            goto try_except_handler_34;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 564;
        tmp_assign_source_112 = CALL_FUNCTION_NO_ARGS(tmp_called_value_91);
        Py_DECREF(tmp_called_value_91);
        if (tmp_assign_source_112 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 564;

            goto try_except_handler_34;
        }
        assert(tmp_with_9__enter == NULL);
        tmp_with_9__enter = tmp_assign_source_112;
    }
    {
        PyObject *tmp_assign_source_113;
        PyObject *tmp_expression_value_64;
        CHECK_OBJECT(tmp_with_9__source);
        tmp_expression_value_64 = tmp_with_9__source;
        tmp_assign_source_113 = LOOKUP_SPECIAL(tmp_expression_value_64, mod_consts[68]);
        if (tmp_assign_source_113 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 564;

            goto try_except_handler_34;
        }
        assert(tmp_with_9__exit == NULL);
        tmp_with_9__exit = tmp_assign_source_113;
    }
    {
        nuitka_bool tmp_assign_source_114;
        tmp_assign_source_114 = NUITKA_BOOL_TRUE;
        tmp_with_9__indicator = tmp_assign_source_114;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_92;
        PyObject *tmp_expression_value_65;
        PyObject *tmp_call_result_61;
        PyObject *tmp_kw_call_arg_value_0_38;
        PyObject *tmp_kw_call_arg_value_1_38;
        PyObject *tmp_kw_call_arg_value_2_38;
        PyObject *tmp_called_value_93;
        PyObject *tmp_expression_value_66;
        PyObject *tmp_kw_call_value_0_4;
        PyObject *tmp_kw_call_value_1_3;
        PyObject *tmp_str_arg_value_2;
        PyObject *tmp_iterable_value_2;
        PyObject *tmp_kw_call_dict_value_0_38;
        PyObject *tmp_called_value_94;
        PyObject *tmp_args_element_value_39;
        PyObject *tmp_add_expr_left_2;
        PyObject *tmp_add_expr_right_2;
        tmp_expression_value_65 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_65 == NULL)) {
            tmp_expression_value_65 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_65 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 565;

            goto try_except_handler_36;
        }
        tmp_called_value_92 = LOOKUP_ATTRIBUTE(tmp_expression_value_65, mod_consts[69]);
        if (tmp_called_value_92 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 565;

            goto try_except_handler_36;
        }
        tmp_kw_call_arg_value_0_38 = mod_consts[240];
        tmp_kw_call_arg_value_1_38 = mod_consts[241];
        tmp_expression_value_66 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229]);

        if (unlikely(tmp_expression_value_66 == NULL)) {
            tmp_expression_value_66 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[229]);
        }

        if (tmp_expression_value_66 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 568;

            goto try_except_handler_36;
        }
        tmp_called_value_93 = LOOKUP_ATTRIBUTE(tmp_expression_value_66, mod_consts[242]);
        if (tmp_called_value_93 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 568;

            goto try_except_handler_36;
        }
        tmp_kw_call_value_0_4 = mod_consts[248];
        tmp_str_arg_value_2 = mod_consts[244];
        tmp_iterable_value_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[233]);

        if (unlikely(tmp_iterable_value_2 == NULL)) {
            tmp_iterable_value_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[233]);
        }

        if (tmp_iterable_value_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_called_value_93);

            exception_lineno = 568;

            goto try_except_handler_36;
        }
        tmp_kw_call_value_1_3 = UNICODE_JOIN(tmp_str_arg_value_2, tmp_iterable_value_2);
        if (tmp_kw_call_value_1_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_called_value_93);

            exception_lineno = 568;

            goto try_except_handler_36;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 568;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_4, tmp_kw_call_value_1_3};

            tmp_kw_call_arg_value_2_38 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_93, kw_values, mod_consts[245]);
        }

        Py_DECREF(tmp_called_value_93);
        Py_DECREF(tmp_kw_call_value_1_3);
        if (tmp_kw_call_arg_value_2_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);

            exception_lineno = 568;

            goto try_except_handler_36;
        }
        tmp_called_value_94 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_94 == NULL)) {
            tmp_called_value_94 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_94 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_kw_call_arg_value_2_38);

            exception_lineno = 569;

            goto try_except_handler_36;
        }
        tmp_add_expr_left_2 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[233]);

        if (unlikely(tmp_add_expr_left_2 == NULL)) {
            tmp_add_expr_left_2 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[233]);
        }

        if (tmp_add_expr_left_2 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_kw_call_arg_value_2_38);

            exception_lineno = 569;

            goto try_except_handler_36;
        }
        tmp_add_expr_right_2 = LIST_COPY(mod_consts[246]);
        tmp_args_element_value_39 = BINARY_OPERATION_ADD_OBJECT_OBJECT_LIST(tmp_add_expr_left_2, tmp_add_expr_right_2);
        Py_DECREF(tmp_add_expr_right_2);
        if (tmp_args_element_value_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_kw_call_arg_value_2_38);

            exception_lineno = 569;

            goto try_except_handler_36;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 569;
        tmp_kw_call_dict_value_0_38 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_94, tmp_args_element_value_39);
        Py_DECREF(tmp_args_element_value_39);
        if (tmp_kw_call_dict_value_0_38 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_92);
            Py_DECREF(tmp_kw_call_arg_value_2_38);

            exception_lineno = 569;

            goto try_except_handler_36;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 565;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_38, tmp_kw_call_arg_value_1_38, tmp_kw_call_arg_value_2_38};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_38};
            tmp_call_result_61 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_92, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_92);
        Py_DECREF(tmp_kw_call_arg_value_2_38);
        Py_DECREF(tmp_kw_call_dict_value_0_38);
        if (tmp_call_result_61 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 565;

            goto try_except_handler_36;
        }
        Py_DECREF(tmp_call_result_61);
    }
    goto try_end_34;
    // Exception handler code:
    try_except_handler_36:;
    exception_keeper_type_34 = exception_type;
    exception_keeper_value_34 = exception_value;
    exception_keeper_tb_34 = exception_tb;
    exception_keeper_lineno_34 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 9.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_9, &exception_preserved_value_9, &exception_preserved_tb_9);

    if (exception_keeper_tb_34 == NULL) {
        exception_keeper_tb_34 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_34);
    } else if (exception_keeper_lineno_34 != 0) {
        exception_keeper_tb_34 = ADD_TRACEBACK(exception_keeper_tb_34, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_34);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_34, &exception_keeper_value_34, &exception_keeper_tb_34);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_34, exception_keeper_tb_34);
    PUBLISH_EXCEPTION(&exception_keeper_type_34, &exception_keeper_value_34, &exception_keeper_tb_34);
    // Tried code:
    {
        bool tmp_condition_result_34;
        PyObject *tmp_cmp_expr_left_25;
        PyObject *tmp_cmp_expr_right_25;
        tmp_cmp_expr_left_25 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_25 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_25, tmp_cmp_expr_right_25);
        assert(!(tmp_res == -1));
        tmp_condition_result_34 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_34 != false) {
            goto branch_yes_34;
        } else {
            goto branch_no_34;
        }
    }
    branch_yes_34:;
    {
        nuitka_bool tmp_assign_source_115;
        tmp_assign_source_115 = NUITKA_BOOL_FALSE;
        tmp_with_9__indicator = tmp_assign_source_115;
    }
    {
        bool tmp_condition_result_35;
        PyObject *tmp_operand_value_9;
        PyObject *tmp_called_value_95;
        PyObject *tmp_args_element_value_40;
        PyObject *tmp_args_element_value_41;
        PyObject *tmp_args_element_value_42;
        CHECK_OBJECT(tmp_with_9__exit);
        tmp_called_value_95 = tmp_with_9__exit;
        tmp_args_element_value_40 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_41 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_42 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 569;
        {
            PyObject *call_args[] = {tmp_args_element_value_40, tmp_args_element_value_41, tmp_args_element_value_42};
            tmp_operand_value_9 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_95, call_args);
        }

        if (tmp_operand_value_9 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 569;

            goto try_except_handler_37;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_9);
        Py_DECREF(tmp_operand_value_9);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 569;

            goto try_except_handler_37;
        }
        tmp_condition_result_35 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_35 != false) {
            goto branch_yes_35;
        } else {
            goto branch_no_35;
        }
    }
    branch_yes_35:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 569;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_37;
    branch_no_35:;
    goto branch_end_34;
    branch_no_34:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 564;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_37;
    branch_end_34:;
    goto try_end_35;
    // Exception handler code:
    try_except_handler_37:;
    exception_keeper_type_35 = exception_type;
    exception_keeper_value_35 = exception_value;
    exception_keeper_tb_35 = exception_tb;
    exception_keeper_lineno_35 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 9.
    SET_CURRENT_EXCEPTION(exception_preserved_type_9, exception_preserved_value_9, exception_preserved_tb_9);

    // Re-raise.
    exception_type = exception_keeper_type_35;
    exception_value = exception_keeper_value_35;
    exception_tb = exception_keeper_tb_35;
    exception_lineno = exception_keeper_lineno_35;

    goto try_except_handler_35;
    // End of try:
    try_end_35:;
    // Restore previous exception id 9.
    SET_CURRENT_EXCEPTION(exception_preserved_type_9, exception_preserved_value_9, exception_preserved_tb_9);

    goto try_end_34;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_34:;
    goto try_end_36;
    // Exception handler code:
    try_except_handler_35:;
    exception_keeper_type_36 = exception_type;
    exception_keeper_value_36 = exception_value;
    exception_keeper_tb_36 = exception_tb;
    exception_keeper_lineno_36 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_36;
        nuitka_bool tmp_cmp_expr_left_26;
        nuitka_bool tmp_cmp_expr_right_26;
        assert(tmp_with_9__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_26 = tmp_with_9__indicator;
        tmp_cmp_expr_right_26 = NUITKA_BOOL_TRUE;
        tmp_condition_result_36 = (tmp_cmp_expr_left_26 == tmp_cmp_expr_right_26) ? true : false;
        if (tmp_condition_result_36 != false) {
            goto branch_yes_36;
        } else {
            goto branch_no_36;
        }
    }
    branch_yes_36:;
    {
        PyObject *tmp_called_value_96;
        PyObject *tmp_call_result_62;
        CHECK_OBJECT(tmp_with_9__exit);
        tmp_called_value_96 = tmp_with_9__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 569;
        tmp_call_result_62 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_96, mod_consts[74]);

        if (tmp_call_result_62 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_36);
            Py_XDECREF(exception_keeper_value_36);
            Py_XDECREF(exception_keeper_tb_36);

            exception_lineno = 569;

            goto try_except_handler_34;
        }
        Py_DECREF(tmp_call_result_62);
    }
    branch_no_36:;
    // Re-raise.
    exception_type = exception_keeper_type_36;
    exception_value = exception_keeper_value_36;
    exception_tb = exception_keeper_tb_36;
    exception_lineno = exception_keeper_lineno_36;

    goto try_except_handler_34;
    // End of try:
    try_end_36:;
    {
        bool tmp_condition_result_37;
        nuitka_bool tmp_cmp_expr_left_27;
        nuitka_bool tmp_cmp_expr_right_27;
        assert(tmp_with_9__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_27 = tmp_with_9__indicator;
        tmp_cmp_expr_right_27 = NUITKA_BOOL_TRUE;
        tmp_condition_result_37 = (tmp_cmp_expr_left_27 == tmp_cmp_expr_right_27) ? true : false;
        if (tmp_condition_result_37 != false) {
            goto branch_yes_37;
        } else {
            goto branch_no_37;
        }
    }
    branch_yes_37:;
    {
        PyObject *tmp_called_value_97;
        PyObject *tmp_call_result_63;
        CHECK_OBJECT(tmp_with_9__exit);
        tmp_called_value_97 = tmp_with_9__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 569;
        tmp_call_result_63 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_97, mod_consts[74]);

        if (tmp_call_result_63 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 569;

            goto try_except_handler_34;
        }
        Py_DECREF(tmp_call_result_63);
    }
    branch_no_37:;
    goto try_end_37;
    // Exception handler code:
    try_except_handler_34:;
    exception_keeper_type_37 = exception_type;
    exception_keeper_value_37 = exception_value;
    exception_keeper_tb_37 = exception_tb;
    exception_keeper_lineno_37 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_9__source);
    tmp_with_9__source = NULL;
    Py_XDECREF(tmp_with_9__enter);
    tmp_with_9__enter = NULL;
    Py_XDECREF(tmp_with_9__exit);
    tmp_with_9__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_37;
    exception_value = exception_keeper_value_37;
    exception_tb = exception_keeper_tb_37;
    exception_lineno = exception_keeper_lineno_37;

    goto frame_exception_exit_1;
    // End of try:
    try_end_37:;
    CHECK_OBJECT(tmp_with_9__source);
    Py_DECREF(tmp_with_9__source);
    tmp_with_9__source = NULL;
    CHECK_OBJECT(tmp_with_9__enter);
    Py_DECREF(tmp_with_9__enter);
    tmp_with_9__enter = NULL;
    Py_XDECREF(tmp_with_9__exit);
    tmp_with_9__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_116;
        PyObject *tmp_called_instance_10;
        tmp_called_instance_10 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_10 == NULL)) {
            tmp_called_instance_10 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 573;

            goto try_except_handler_38;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 573;
        tmp_assign_source_116 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_10,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[249], 0)
        );

        if (tmp_assign_source_116 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 573;

            goto try_except_handler_38;
        }
        assert(tmp_with_10__source == NULL);
        tmp_with_10__source = tmp_assign_source_116;
    }
    {
        PyObject *tmp_assign_source_117;
        PyObject *tmp_called_value_98;
        PyObject *tmp_expression_value_67;
        CHECK_OBJECT(tmp_with_10__source);
        tmp_expression_value_67 = tmp_with_10__source;
        tmp_called_value_98 = LOOKUP_SPECIAL(tmp_expression_value_67, mod_consts[67]);
        if (tmp_called_value_98 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 573;

            goto try_except_handler_38;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 573;
        tmp_assign_source_117 = CALL_FUNCTION_NO_ARGS(tmp_called_value_98);
        Py_DECREF(tmp_called_value_98);
        if (tmp_assign_source_117 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 573;

            goto try_except_handler_38;
        }
        assert(tmp_with_10__enter == NULL);
        tmp_with_10__enter = tmp_assign_source_117;
    }
    {
        PyObject *tmp_assign_source_118;
        PyObject *tmp_expression_value_68;
        CHECK_OBJECT(tmp_with_10__source);
        tmp_expression_value_68 = tmp_with_10__source;
        tmp_assign_source_118 = LOOKUP_SPECIAL(tmp_expression_value_68, mod_consts[68]);
        if (tmp_assign_source_118 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 573;

            goto try_except_handler_38;
        }
        assert(tmp_with_10__exit == NULL);
        tmp_with_10__exit = tmp_assign_source_118;
    }
    {
        nuitka_bool tmp_assign_source_119;
        tmp_assign_source_119 = NUITKA_BOOL_TRUE;
        tmp_with_10__indicator = tmp_assign_source_119;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_99;
        PyObject *tmp_expression_value_69;
        PyObject *tmp_call_result_64;
        PyObject *tmp_kw_call_arg_value_0_39;
        PyObject *tmp_kw_call_arg_value_1_39;
        PyObject *tmp_kw_call_arg_value_2_39;
        PyObject *tmp_called_value_100;
        PyObject *tmp_expression_value_70;
        PyObject *tmp_kw_call_value_0_5;
        PyObject *tmp_kw_call_value_1_4;
        PyObject *tmp_str_arg_value_3;
        PyObject *tmp_iterable_value_3;
        PyObject *tmp_kw_call_dict_value_0_39;
        PyObject *tmp_called_value_101;
        PyObject *tmp_args_element_value_43;
        PyObject *tmp_add_expr_left_3;
        PyObject *tmp_add_expr_right_3;
        tmp_expression_value_69 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_69 == NULL)) {
            tmp_expression_value_69 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_69 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 574;

            goto try_except_handler_40;
        }
        tmp_called_value_99 = LOOKUP_ATTRIBUTE(tmp_expression_value_69, mod_consts[69]);
        if (tmp_called_value_99 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 574;

            goto try_except_handler_40;
        }
        tmp_kw_call_arg_value_0_39 = mod_consts[240];
        tmp_kw_call_arg_value_1_39 = mod_consts[241];
        tmp_expression_value_70 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229]);

        if (unlikely(tmp_expression_value_70 == NULL)) {
            tmp_expression_value_70 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[229]);
        }

        if (tmp_expression_value_70 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);

            exception_lineno = 577;

            goto try_except_handler_40;
        }
        tmp_called_value_100 = LOOKUP_ATTRIBUTE(tmp_expression_value_70, mod_consts[242]);
        if (tmp_called_value_100 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);

            exception_lineno = 577;

            goto try_except_handler_40;
        }
        tmp_kw_call_value_0_5 = mod_consts[250];
        tmp_str_arg_value_3 = mod_consts[244];
        tmp_iterable_value_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[234]);

        if (unlikely(tmp_iterable_value_3 == NULL)) {
            tmp_iterable_value_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[234]);
        }

        if (tmp_iterable_value_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_called_value_100);

            exception_lineno = 577;

            goto try_except_handler_40;
        }
        tmp_kw_call_value_1_4 = UNICODE_JOIN(tmp_str_arg_value_3, tmp_iterable_value_3);
        if (tmp_kw_call_value_1_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_called_value_100);

            exception_lineno = 577;

            goto try_except_handler_40;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 577;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_5, tmp_kw_call_value_1_4};

            tmp_kw_call_arg_value_2_39 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_100, kw_values, mod_consts[245]);
        }

        Py_DECREF(tmp_called_value_100);
        Py_DECREF(tmp_kw_call_value_1_4);
        if (tmp_kw_call_arg_value_2_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);

            exception_lineno = 577;

            goto try_except_handler_40;
        }
        tmp_called_value_101 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_101 == NULL)) {
            tmp_called_value_101 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_101 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_kw_call_arg_value_2_39);

            exception_lineno = 578;

            goto try_except_handler_40;
        }
        tmp_add_expr_left_3 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[234]);

        if (unlikely(tmp_add_expr_left_3 == NULL)) {
            tmp_add_expr_left_3 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[234]);
        }

        if (tmp_add_expr_left_3 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_kw_call_arg_value_2_39);

            exception_lineno = 578;

            goto try_except_handler_40;
        }
        tmp_add_expr_right_3 = LIST_COPY(mod_consts[246]);
        tmp_args_element_value_43 = BINARY_OPERATION_ADD_OBJECT_OBJECT_LIST(tmp_add_expr_left_3, tmp_add_expr_right_3);
        Py_DECREF(tmp_add_expr_right_3);
        if (tmp_args_element_value_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_kw_call_arg_value_2_39);

            exception_lineno = 578;

            goto try_except_handler_40;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 578;
        tmp_kw_call_dict_value_0_39 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_101, tmp_args_element_value_43);
        Py_DECREF(tmp_args_element_value_43);
        if (tmp_kw_call_dict_value_0_39 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_99);
            Py_DECREF(tmp_kw_call_arg_value_2_39);

            exception_lineno = 578;

            goto try_except_handler_40;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 574;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_39, tmp_kw_call_arg_value_1_39, tmp_kw_call_arg_value_2_39};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_39};
            tmp_call_result_64 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_99, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_99);
        Py_DECREF(tmp_kw_call_arg_value_2_39);
        Py_DECREF(tmp_kw_call_dict_value_0_39);
        if (tmp_call_result_64 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 574;

            goto try_except_handler_40;
        }
        Py_DECREF(tmp_call_result_64);
    }
    goto try_end_38;
    // Exception handler code:
    try_except_handler_40:;
    exception_keeper_type_38 = exception_type;
    exception_keeper_value_38 = exception_value;
    exception_keeper_tb_38 = exception_tb;
    exception_keeper_lineno_38 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 10.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_10, &exception_preserved_value_10, &exception_preserved_tb_10);

    if (exception_keeper_tb_38 == NULL) {
        exception_keeper_tb_38 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_38);
    } else if (exception_keeper_lineno_38 != 0) {
        exception_keeper_tb_38 = ADD_TRACEBACK(exception_keeper_tb_38, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_38);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_38, &exception_keeper_value_38, &exception_keeper_tb_38);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_38, exception_keeper_tb_38);
    PUBLISH_EXCEPTION(&exception_keeper_type_38, &exception_keeper_value_38, &exception_keeper_tb_38);
    // Tried code:
    {
        bool tmp_condition_result_38;
        PyObject *tmp_cmp_expr_left_28;
        PyObject *tmp_cmp_expr_right_28;
        tmp_cmp_expr_left_28 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_28 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_28, tmp_cmp_expr_right_28);
        assert(!(tmp_res == -1));
        tmp_condition_result_38 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_38 != false) {
            goto branch_yes_38;
        } else {
            goto branch_no_38;
        }
    }
    branch_yes_38:;
    {
        nuitka_bool tmp_assign_source_120;
        tmp_assign_source_120 = NUITKA_BOOL_FALSE;
        tmp_with_10__indicator = tmp_assign_source_120;
    }
    {
        bool tmp_condition_result_39;
        PyObject *tmp_operand_value_10;
        PyObject *tmp_called_value_102;
        PyObject *tmp_args_element_value_44;
        PyObject *tmp_args_element_value_45;
        PyObject *tmp_args_element_value_46;
        CHECK_OBJECT(tmp_with_10__exit);
        tmp_called_value_102 = tmp_with_10__exit;
        tmp_args_element_value_44 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_45 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_46 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 578;
        {
            PyObject *call_args[] = {tmp_args_element_value_44, tmp_args_element_value_45, tmp_args_element_value_46};
            tmp_operand_value_10 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_102, call_args);
        }

        if (tmp_operand_value_10 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 578;

            goto try_except_handler_41;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_10);
        Py_DECREF(tmp_operand_value_10);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 578;

            goto try_except_handler_41;
        }
        tmp_condition_result_39 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_39 != false) {
            goto branch_yes_39;
        } else {
            goto branch_no_39;
        }
    }
    branch_yes_39:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 578;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_41;
    branch_no_39:;
    goto branch_end_38;
    branch_no_38:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 573;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_41;
    branch_end_38:;
    goto try_end_39;
    // Exception handler code:
    try_except_handler_41:;
    exception_keeper_type_39 = exception_type;
    exception_keeper_value_39 = exception_value;
    exception_keeper_tb_39 = exception_tb;
    exception_keeper_lineno_39 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 10.
    SET_CURRENT_EXCEPTION(exception_preserved_type_10, exception_preserved_value_10, exception_preserved_tb_10);

    // Re-raise.
    exception_type = exception_keeper_type_39;
    exception_value = exception_keeper_value_39;
    exception_tb = exception_keeper_tb_39;
    exception_lineno = exception_keeper_lineno_39;

    goto try_except_handler_39;
    // End of try:
    try_end_39:;
    // Restore previous exception id 10.
    SET_CURRENT_EXCEPTION(exception_preserved_type_10, exception_preserved_value_10, exception_preserved_tb_10);

    goto try_end_38;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_38:;
    goto try_end_40;
    // Exception handler code:
    try_except_handler_39:;
    exception_keeper_type_40 = exception_type;
    exception_keeper_value_40 = exception_value;
    exception_keeper_tb_40 = exception_tb;
    exception_keeper_lineno_40 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_40;
        nuitka_bool tmp_cmp_expr_left_29;
        nuitka_bool tmp_cmp_expr_right_29;
        assert(tmp_with_10__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_29 = tmp_with_10__indicator;
        tmp_cmp_expr_right_29 = NUITKA_BOOL_TRUE;
        tmp_condition_result_40 = (tmp_cmp_expr_left_29 == tmp_cmp_expr_right_29) ? true : false;
        if (tmp_condition_result_40 != false) {
            goto branch_yes_40;
        } else {
            goto branch_no_40;
        }
    }
    branch_yes_40:;
    {
        PyObject *tmp_called_value_103;
        PyObject *tmp_call_result_65;
        CHECK_OBJECT(tmp_with_10__exit);
        tmp_called_value_103 = tmp_with_10__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 578;
        tmp_call_result_65 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_103, mod_consts[74]);

        if (tmp_call_result_65 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_40);
            Py_XDECREF(exception_keeper_value_40);
            Py_XDECREF(exception_keeper_tb_40);

            exception_lineno = 578;

            goto try_except_handler_38;
        }
        Py_DECREF(tmp_call_result_65);
    }
    branch_no_40:;
    // Re-raise.
    exception_type = exception_keeper_type_40;
    exception_value = exception_keeper_value_40;
    exception_tb = exception_keeper_tb_40;
    exception_lineno = exception_keeper_lineno_40;

    goto try_except_handler_38;
    // End of try:
    try_end_40:;
    {
        bool tmp_condition_result_41;
        nuitka_bool tmp_cmp_expr_left_30;
        nuitka_bool tmp_cmp_expr_right_30;
        assert(tmp_with_10__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_30 = tmp_with_10__indicator;
        tmp_cmp_expr_right_30 = NUITKA_BOOL_TRUE;
        tmp_condition_result_41 = (tmp_cmp_expr_left_30 == tmp_cmp_expr_right_30) ? true : false;
        if (tmp_condition_result_41 != false) {
            goto branch_yes_41;
        } else {
            goto branch_no_41;
        }
    }
    branch_yes_41:;
    {
        PyObject *tmp_called_value_104;
        PyObject *tmp_call_result_66;
        CHECK_OBJECT(tmp_with_10__exit);
        tmp_called_value_104 = tmp_with_10__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 578;
        tmp_call_result_66 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_104, mod_consts[74]);

        if (tmp_call_result_66 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 578;

            goto try_except_handler_38;
        }
        Py_DECREF(tmp_call_result_66);
    }
    branch_no_41:;
    goto try_end_41;
    // Exception handler code:
    try_except_handler_38:;
    exception_keeper_type_41 = exception_type;
    exception_keeper_value_41 = exception_value;
    exception_keeper_tb_41 = exception_tb;
    exception_keeper_lineno_41 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_10__source);
    tmp_with_10__source = NULL;
    Py_XDECREF(tmp_with_10__enter);
    tmp_with_10__enter = NULL;
    Py_XDECREF(tmp_with_10__exit);
    tmp_with_10__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_41;
    exception_value = exception_keeper_value_41;
    exception_tb = exception_keeper_tb_41;
    exception_lineno = exception_keeper_lineno_41;

    goto frame_exception_exit_1;
    // End of try:
    try_end_41:;
    CHECK_OBJECT(tmp_with_10__source);
    Py_DECREF(tmp_with_10__source);
    tmp_with_10__source = NULL;
    CHECK_OBJECT(tmp_with_10__enter);
    Py_DECREF(tmp_with_10__enter);
    tmp_with_10__enter = NULL;
    Py_XDECREF(tmp_with_10__exit);
    tmp_with_10__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_121;
        PyObject *tmp_called_instance_11;
        tmp_called_instance_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_11 == NULL)) {
            tmp_called_instance_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 582;

            goto try_except_handler_42;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 582;
        tmp_assign_source_121 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_11,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[251], 0)
        );

        if (tmp_assign_source_121 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 582;

            goto try_except_handler_42;
        }
        assert(tmp_with_11__source == NULL);
        tmp_with_11__source = tmp_assign_source_121;
    }
    {
        PyObject *tmp_assign_source_122;
        PyObject *tmp_called_value_105;
        PyObject *tmp_expression_value_71;
        CHECK_OBJECT(tmp_with_11__source);
        tmp_expression_value_71 = tmp_with_11__source;
        tmp_called_value_105 = LOOKUP_SPECIAL(tmp_expression_value_71, mod_consts[67]);
        if (tmp_called_value_105 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 582;

            goto try_except_handler_42;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 582;
        tmp_assign_source_122 = CALL_FUNCTION_NO_ARGS(tmp_called_value_105);
        Py_DECREF(tmp_called_value_105);
        if (tmp_assign_source_122 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 582;

            goto try_except_handler_42;
        }
        assert(tmp_with_11__enter == NULL);
        tmp_with_11__enter = tmp_assign_source_122;
    }
    {
        PyObject *tmp_assign_source_123;
        PyObject *tmp_expression_value_72;
        CHECK_OBJECT(tmp_with_11__source);
        tmp_expression_value_72 = tmp_with_11__source;
        tmp_assign_source_123 = LOOKUP_SPECIAL(tmp_expression_value_72, mod_consts[68]);
        if (tmp_assign_source_123 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 582;

            goto try_except_handler_42;
        }
        assert(tmp_with_11__exit == NULL);
        tmp_with_11__exit = tmp_assign_source_123;
    }
    {
        nuitka_bool tmp_assign_source_124;
        tmp_assign_source_124 = NUITKA_BOOL_TRUE;
        tmp_with_11__indicator = tmp_assign_source_124;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_106;
        PyObject *tmp_expression_value_73;
        PyObject *tmp_call_result_67;
        PyObject *tmp_kw_call_arg_value_0_40;
        PyObject *tmp_kw_call_arg_value_1_40;
        PyObject *tmp_kw_call_arg_value_2_40;
        PyObject *tmp_called_value_107;
        PyObject *tmp_expression_value_74;
        PyObject *tmp_kw_call_value_0_6;
        PyObject *tmp_kw_call_value_1_5;
        PyObject *tmp_str_arg_value_4;
        PyObject *tmp_iterable_value_4;
        PyObject *tmp_kw_call_dict_value_0_40;
        PyObject *tmp_called_value_108;
        PyObject *tmp_args_element_value_47;
        PyObject *tmp_add_expr_left_4;
        PyObject *tmp_add_expr_right_4;
        tmp_expression_value_73 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_73 == NULL)) {
            tmp_expression_value_73 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_73 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 583;

            goto try_except_handler_44;
        }
        tmp_called_value_106 = LOOKUP_ATTRIBUTE(tmp_expression_value_73, mod_consts[69]);
        if (tmp_called_value_106 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 583;

            goto try_except_handler_44;
        }
        tmp_kw_call_arg_value_0_40 = mod_consts[240];
        tmp_kw_call_arg_value_1_40 = mod_consts[241];
        tmp_expression_value_74 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229]);

        if (unlikely(tmp_expression_value_74 == NULL)) {
            tmp_expression_value_74 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[229]);
        }

        if (tmp_expression_value_74 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);

            exception_lineno = 586;

            goto try_except_handler_44;
        }
        tmp_called_value_107 = LOOKUP_ATTRIBUTE(tmp_expression_value_74, mod_consts[242]);
        if (tmp_called_value_107 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);

            exception_lineno = 586;

            goto try_except_handler_44;
        }
        tmp_kw_call_value_0_6 = mod_consts[252];
        tmp_str_arg_value_4 = mod_consts[244];
        tmp_iterable_value_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[236]);

        if (unlikely(tmp_iterable_value_4 == NULL)) {
            tmp_iterable_value_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[236]);
        }

        if (tmp_iterable_value_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_called_value_107);

            exception_lineno = 586;

            goto try_except_handler_44;
        }
        tmp_kw_call_value_1_5 = UNICODE_JOIN(tmp_str_arg_value_4, tmp_iterable_value_4);
        if (tmp_kw_call_value_1_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_called_value_107);

            exception_lineno = 586;

            goto try_except_handler_44;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 586;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_6, tmp_kw_call_value_1_5};

            tmp_kw_call_arg_value_2_40 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_107, kw_values, mod_consts[245]);
        }

        Py_DECREF(tmp_called_value_107);
        Py_DECREF(tmp_kw_call_value_1_5);
        if (tmp_kw_call_arg_value_2_40 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);

            exception_lineno = 586;

            goto try_except_handler_44;
        }
        tmp_called_value_108 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_108 == NULL)) {
            tmp_called_value_108 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_108 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_kw_call_arg_value_2_40);

            exception_lineno = 587;

            goto try_except_handler_44;
        }
        tmp_add_expr_left_4 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[236]);

        if (unlikely(tmp_add_expr_left_4 == NULL)) {
            tmp_add_expr_left_4 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[236]);
        }

        if (tmp_add_expr_left_4 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_kw_call_arg_value_2_40);

            exception_lineno = 587;

            goto try_except_handler_44;
        }
        tmp_add_expr_right_4 = LIST_COPY(mod_consts[246]);
        tmp_args_element_value_47 = BINARY_OPERATION_ADD_OBJECT_OBJECT_LIST(tmp_add_expr_left_4, tmp_add_expr_right_4);
        Py_DECREF(tmp_add_expr_right_4);
        if (tmp_args_element_value_47 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_kw_call_arg_value_2_40);

            exception_lineno = 587;

            goto try_except_handler_44;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 587;
        tmp_kw_call_dict_value_0_40 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_108, tmp_args_element_value_47);
        Py_DECREF(tmp_args_element_value_47);
        if (tmp_kw_call_dict_value_0_40 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_106);
            Py_DECREF(tmp_kw_call_arg_value_2_40);

            exception_lineno = 587;

            goto try_except_handler_44;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 583;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_40, tmp_kw_call_arg_value_1_40, tmp_kw_call_arg_value_2_40};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_40};
            tmp_call_result_67 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_106, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_106);
        Py_DECREF(tmp_kw_call_arg_value_2_40);
        Py_DECREF(tmp_kw_call_dict_value_0_40);
        if (tmp_call_result_67 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 583;

            goto try_except_handler_44;
        }
        Py_DECREF(tmp_call_result_67);
    }
    goto try_end_42;
    // Exception handler code:
    try_except_handler_44:;
    exception_keeper_type_42 = exception_type;
    exception_keeper_value_42 = exception_value;
    exception_keeper_tb_42 = exception_tb;
    exception_keeper_lineno_42 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 11.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_11, &exception_preserved_value_11, &exception_preserved_tb_11);

    if (exception_keeper_tb_42 == NULL) {
        exception_keeper_tb_42 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_42);
    } else if (exception_keeper_lineno_42 != 0) {
        exception_keeper_tb_42 = ADD_TRACEBACK(exception_keeper_tb_42, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_42);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_42, &exception_keeper_value_42, &exception_keeper_tb_42);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_42, exception_keeper_tb_42);
    PUBLISH_EXCEPTION(&exception_keeper_type_42, &exception_keeper_value_42, &exception_keeper_tb_42);
    // Tried code:
    {
        bool tmp_condition_result_42;
        PyObject *tmp_cmp_expr_left_31;
        PyObject *tmp_cmp_expr_right_31;
        tmp_cmp_expr_left_31 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_31 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_31, tmp_cmp_expr_right_31);
        assert(!(tmp_res == -1));
        tmp_condition_result_42 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_42 != false) {
            goto branch_yes_42;
        } else {
            goto branch_no_42;
        }
    }
    branch_yes_42:;
    {
        nuitka_bool tmp_assign_source_125;
        tmp_assign_source_125 = NUITKA_BOOL_FALSE;
        tmp_with_11__indicator = tmp_assign_source_125;
    }
    {
        bool tmp_condition_result_43;
        PyObject *tmp_operand_value_11;
        PyObject *tmp_called_value_109;
        PyObject *tmp_args_element_value_48;
        PyObject *tmp_args_element_value_49;
        PyObject *tmp_args_element_value_50;
        CHECK_OBJECT(tmp_with_11__exit);
        tmp_called_value_109 = tmp_with_11__exit;
        tmp_args_element_value_48 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_49 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_50 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 587;
        {
            PyObject *call_args[] = {tmp_args_element_value_48, tmp_args_element_value_49, tmp_args_element_value_50};
            tmp_operand_value_11 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_109, call_args);
        }

        if (tmp_operand_value_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 587;

            goto try_except_handler_45;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_11);
        Py_DECREF(tmp_operand_value_11);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 587;

            goto try_except_handler_45;
        }
        tmp_condition_result_43 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_43 != false) {
            goto branch_yes_43;
        } else {
            goto branch_no_43;
        }
    }
    branch_yes_43:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 587;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_45;
    branch_no_43:;
    goto branch_end_42;
    branch_no_42:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 582;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_45;
    branch_end_42:;
    goto try_end_43;
    // Exception handler code:
    try_except_handler_45:;
    exception_keeper_type_43 = exception_type;
    exception_keeper_value_43 = exception_value;
    exception_keeper_tb_43 = exception_tb;
    exception_keeper_lineno_43 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 11.
    SET_CURRENT_EXCEPTION(exception_preserved_type_11, exception_preserved_value_11, exception_preserved_tb_11);

    // Re-raise.
    exception_type = exception_keeper_type_43;
    exception_value = exception_keeper_value_43;
    exception_tb = exception_keeper_tb_43;
    exception_lineno = exception_keeper_lineno_43;

    goto try_except_handler_43;
    // End of try:
    try_end_43:;
    // Restore previous exception id 11.
    SET_CURRENT_EXCEPTION(exception_preserved_type_11, exception_preserved_value_11, exception_preserved_tb_11);

    goto try_end_42;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_42:;
    goto try_end_44;
    // Exception handler code:
    try_except_handler_43:;
    exception_keeper_type_44 = exception_type;
    exception_keeper_value_44 = exception_value;
    exception_keeper_tb_44 = exception_tb;
    exception_keeper_lineno_44 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_44;
        nuitka_bool tmp_cmp_expr_left_32;
        nuitka_bool tmp_cmp_expr_right_32;
        assert(tmp_with_11__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_32 = tmp_with_11__indicator;
        tmp_cmp_expr_right_32 = NUITKA_BOOL_TRUE;
        tmp_condition_result_44 = (tmp_cmp_expr_left_32 == tmp_cmp_expr_right_32) ? true : false;
        if (tmp_condition_result_44 != false) {
            goto branch_yes_44;
        } else {
            goto branch_no_44;
        }
    }
    branch_yes_44:;
    {
        PyObject *tmp_called_value_110;
        PyObject *tmp_call_result_68;
        CHECK_OBJECT(tmp_with_11__exit);
        tmp_called_value_110 = tmp_with_11__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 587;
        tmp_call_result_68 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_110, mod_consts[74]);

        if (tmp_call_result_68 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_44);
            Py_XDECREF(exception_keeper_value_44);
            Py_XDECREF(exception_keeper_tb_44);

            exception_lineno = 587;

            goto try_except_handler_42;
        }
        Py_DECREF(tmp_call_result_68);
    }
    branch_no_44:;
    // Re-raise.
    exception_type = exception_keeper_type_44;
    exception_value = exception_keeper_value_44;
    exception_tb = exception_keeper_tb_44;
    exception_lineno = exception_keeper_lineno_44;

    goto try_except_handler_42;
    // End of try:
    try_end_44:;
    {
        bool tmp_condition_result_45;
        nuitka_bool tmp_cmp_expr_left_33;
        nuitka_bool tmp_cmp_expr_right_33;
        assert(tmp_with_11__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_33 = tmp_with_11__indicator;
        tmp_cmp_expr_right_33 = NUITKA_BOOL_TRUE;
        tmp_condition_result_45 = (tmp_cmp_expr_left_33 == tmp_cmp_expr_right_33) ? true : false;
        if (tmp_condition_result_45 != false) {
            goto branch_yes_45;
        } else {
            goto branch_no_45;
        }
    }
    branch_yes_45:;
    {
        PyObject *tmp_called_value_111;
        PyObject *tmp_call_result_69;
        CHECK_OBJECT(tmp_with_11__exit);
        tmp_called_value_111 = tmp_with_11__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 587;
        tmp_call_result_69 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_111, mod_consts[74]);

        if (tmp_call_result_69 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 587;

            goto try_except_handler_42;
        }
        Py_DECREF(tmp_call_result_69);
    }
    branch_no_45:;
    goto try_end_45;
    // Exception handler code:
    try_except_handler_42:;
    exception_keeper_type_45 = exception_type;
    exception_keeper_value_45 = exception_value;
    exception_keeper_tb_45 = exception_tb;
    exception_keeper_lineno_45 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_11__source);
    tmp_with_11__source = NULL;
    Py_XDECREF(tmp_with_11__enter);
    tmp_with_11__enter = NULL;
    Py_XDECREF(tmp_with_11__exit);
    tmp_with_11__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_45;
    exception_value = exception_keeper_value_45;
    exception_tb = exception_keeper_tb_45;
    exception_lineno = exception_keeper_lineno_45;

    goto frame_exception_exit_1;
    // End of try:
    try_end_45:;
    CHECK_OBJECT(tmp_with_11__source);
    Py_DECREF(tmp_with_11__source);
    tmp_with_11__source = NULL;
    CHECK_OBJECT(tmp_with_11__enter);
    Py_DECREF(tmp_with_11__enter);
    tmp_with_11__enter = NULL;
    Py_XDECREF(tmp_with_11__exit);
    tmp_with_11__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_126;
        PyObject *tmp_called_instance_12;
        tmp_called_instance_12 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_12 == NULL)) {
            tmp_called_instance_12 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 590;

            goto try_except_handler_46;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 590;
        tmp_assign_source_126 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_12,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[253], 0)
        );

        if (tmp_assign_source_126 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 590;

            goto try_except_handler_46;
        }
        assert(tmp_with_12__source == NULL);
        tmp_with_12__source = tmp_assign_source_126;
    }
    {
        PyObject *tmp_assign_source_127;
        PyObject *tmp_called_value_112;
        PyObject *tmp_expression_value_75;
        CHECK_OBJECT(tmp_with_12__source);
        tmp_expression_value_75 = tmp_with_12__source;
        tmp_called_value_112 = LOOKUP_SPECIAL(tmp_expression_value_75, mod_consts[67]);
        if (tmp_called_value_112 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 590;

            goto try_except_handler_46;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 590;
        tmp_assign_source_127 = CALL_FUNCTION_NO_ARGS(tmp_called_value_112);
        Py_DECREF(tmp_called_value_112);
        if (tmp_assign_source_127 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 590;

            goto try_except_handler_46;
        }
        assert(tmp_with_12__enter == NULL);
        tmp_with_12__enter = tmp_assign_source_127;
    }
    {
        PyObject *tmp_assign_source_128;
        PyObject *tmp_expression_value_76;
        CHECK_OBJECT(tmp_with_12__source);
        tmp_expression_value_76 = tmp_with_12__source;
        tmp_assign_source_128 = LOOKUP_SPECIAL(tmp_expression_value_76, mod_consts[68]);
        if (tmp_assign_source_128 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 590;

            goto try_except_handler_46;
        }
        assert(tmp_with_12__exit == NULL);
        tmp_with_12__exit = tmp_assign_source_128;
    }
    {
        nuitka_bool tmp_assign_source_129;
        tmp_assign_source_129 = NUITKA_BOOL_TRUE;
        tmp_with_12__indicator = tmp_assign_source_129;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_113;
        PyObject *tmp_expression_value_77;
        PyObject *tmp_call_result_70;
        PyObject *tmp_kw_call_arg_value_0_41;
        PyObject *tmp_kw_call_arg_value_1_41;
        PyObject *tmp_kw_call_arg_value_2_41;
        PyObject *tmp_called_value_114;
        PyObject *tmp_expression_value_78;
        PyObject *tmp_kw_call_value_0_7;
        PyObject *tmp_kw_call_value_1_6;
        PyObject *tmp_str_arg_value_5;
        PyObject *tmp_iterable_value_5;
        PyObject *tmp_kw_call_dict_value_0_41;
        PyObject *tmp_called_value_115;
        PyObject *tmp_args_element_value_51;
        PyObject *tmp_add_expr_left_5;
        PyObject *tmp_add_expr_right_5;
        tmp_expression_value_77 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_77 == NULL)) {
            tmp_expression_value_77 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_77 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 591;

            goto try_except_handler_48;
        }
        tmp_called_value_113 = LOOKUP_ATTRIBUTE(tmp_expression_value_77, mod_consts[69]);
        if (tmp_called_value_113 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 591;

            goto try_except_handler_48;
        }
        tmp_kw_call_arg_value_0_41 = mod_consts[240];
        tmp_kw_call_arg_value_1_41 = mod_consts[241];
        tmp_expression_value_78 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[229]);

        if (unlikely(tmp_expression_value_78 == NULL)) {
            tmp_expression_value_78 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[229]);
        }

        if (tmp_expression_value_78 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);

            exception_lineno = 594;

            goto try_except_handler_48;
        }
        tmp_called_value_114 = LOOKUP_ATTRIBUTE(tmp_expression_value_78, mod_consts[242]);
        if (tmp_called_value_114 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);

            exception_lineno = 594;

            goto try_except_handler_48;
        }
        tmp_kw_call_value_0_7 = mod_consts[254];
        tmp_str_arg_value_5 = mod_consts[244];
        tmp_iterable_value_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[238]);

        if (unlikely(tmp_iterable_value_5 == NULL)) {
            tmp_iterable_value_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[238]);
        }

        if (tmp_iterable_value_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_called_value_114);

            exception_lineno = 594;

            goto try_except_handler_48;
        }
        tmp_kw_call_value_1_6 = UNICODE_JOIN(tmp_str_arg_value_5, tmp_iterable_value_5);
        if (tmp_kw_call_value_1_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_called_value_114);

            exception_lineno = 594;

            goto try_except_handler_48;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 594;
        {
            PyObject *kw_values[2] = {tmp_kw_call_value_0_7, tmp_kw_call_value_1_6};

            tmp_kw_call_arg_value_2_41 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_114, kw_values, mod_consts[245]);
        }

        Py_DECREF(tmp_called_value_114);
        Py_DECREF(tmp_kw_call_value_1_6);
        if (tmp_kw_call_arg_value_2_41 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);

            exception_lineno = 594;

            goto try_except_handler_48;
        }
        tmp_called_value_115 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_115 == NULL)) {
            tmp_called_value_115 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_115 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_kw_call_arg_value_2_41);

            exception_lineno = 595;

            goto try_except_handler_48;
        }
        tmp_add_expr_left_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[238]);

        if (unlikely(tmp_add_expr_left_5 == NULL)) {
            tmp_add_expr_left_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[238]);
        }

        if (tmp_add_expr_left_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_kw_call_arg_value_2_41);

            exception_lineno = 595;

            goto try_except_handler_48;
        }
        tmp_add_expr_right_5 = LIST_COPY(mod_consts[246]);
        tmp_args_element_value_51 = BINARY_OPERATION_ADD_OBJECT_OBJECT_LIST(tmp_add_expr_left_5, tmp_add_expr_right_5);
        Py_DECREF(tmp_add_expr_right_5);
        if (tmp_args_element_value_51 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_kw_call_arg_value_2_41);

            exception_lineno = 595;

            goto try_except_handler_48;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 595;
        tmp_kw_call_dict_value_0_41 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_115, tmp_args_element_value_51);
        Py_DECREF(tmp_args_element_value_51);
        if (tmp_kw_call_dict_value_0_41 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_113);
            Py_DECREF(tmp_kw_call_arg_value_2_41);

            exception_lineno = 595;

            goto try_except_handler_48;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 591;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_41, tmp_kw_call_arg_value_1_41, tmp_kw_call_arg_value_2_41};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_41};
            tmp_call_result_70 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_113, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_113);
        Py_DECREF(tmp_kw_call_arg_value_2_41);
        Py_DECREF(tmp_kw_call_dict_value_0_41);
        if (tmp_call_result_70 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 591;

            goto try_except_handler_48;
        }
        Py_DECREF(tmp_call_result_70);
    }
    goto try_end_46;
    // Exception handler code:
    try_except_handler_48:;
    exception_keeper_type_46 = exception_type;
    exception_keeper_value_46 = exception_value;
    exception_keeper_tb_46 = exception_tb;
    exception_keeper_lineno_46 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 12.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_12, &exception_preserved_value_12, &exception_preserved_tb_12);

    if (exception_keeper_tb_46 == NULL) {
        exception_keeper_tb_46 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_46);
    } else if (exception_keeper_lineno_46 != 0) {
        exception_keeper_tb_46 = ADD_TRACEBACK(exception_keeper_tb_46, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_46);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_46, &exception_keeper_value_46, &exception_keeper_tb_46);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_46, exception_keeper_tb_46);
    PUBLISH_EXCEPTION(&exception_keeper_type_46, &exception_keeper_value_46, &exception_keeper_tb_46);
    // Tried code:
    {
        bool tmp_condition_result_46;
        PyObject *tmp_cmp_expr_left_34;
        PyObject *tmp_cmp_expr_right_34;
        tmp_cmp_expr_left_34 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_34 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_34, tmp_cmp_expr_right_34);
        assert(!(tmp_res == -1));
        tmp_condition_result_46 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_46 != false) {
            goto branch_yes_46;
        } else {
            goto branch_no_46;
        }
    }
    branch_yes_46:;
    {
        nuitka_bool tmp_assign_source_130;
        tmp_assign_source_130 = NUITKA_BOOL_FALSE;
        tmp_with_12__indicator = tmp_assign_source_130;
    }
    {
        bool tmp_condition_result_47;
        PyObject *tmp_operand_value_12;
        PyObject *tmp_called_value_116;
        PyObject *tmp_args_element_value_52;
        PyObject *tmp_args_element_value_53;
        PyObject *tmp_args_element_value_54;
        CHECK_OBJECT(tmp_with_12__exit);
        tmp_called_value_116 = tmp_with_12__exit;
        tmp_args_element_value_52 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_53 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_54 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 595;
        {
            PyObject *call_args[] = {tmp_args_element_value_52, tmp_args_element_value_53, tmp_args_element_value_54};
            tmp_operand_value_12 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_116, call_args);
        }

        if (tmp_operand_value_12 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 595;

            goto try_except_handler_49;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_12);
        Py_DECREF(tmp_operand_value_12);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 595;

            goto try_except_handler_49;
        }
        tmp_condition_result_47 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_47 != false) {
            goto branch_yes_47;
        } else {
            goto branch_no_47;
        }
    }
    branch_yes_47:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 595;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_49;
    branch_no_47:;
    goto branch_end_46;
    branch_no_46:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 590;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_49;
    branch_end_46:;
    goto try_end_47;
    // Exception handler code:
    try_except_handler_49:;
    exception_keeper_type_47 = exception_type;
    exception_keeper_value_47 = exception_value;
    exception_keeper_tb_47 = exception_tb;
    exception_keeper_lineno_47 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 12.
    SET_CURRENT_EXCEPTION(exception_preserved_type_12, exception_preserved_value_12, exception_preserved_tb_12);

    // Re-raise.
    exception_type = exception_keeper_type_47;
    exception_value = exception_keeper_value_47;
    exception_tb = exception_keeper_tb_47;
    exception_lineno = exception_keeper_lineno_47;

    goto try_except_handler_47;
    // End of try:
    try_end_47:;
    // Restore previous exception id 12.
    SET_CURRENT_EXCEPTION(exception_preserved_type_12, exception_preserved_value_12, exception_preserved_tb_12);

    goto try_end_46;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_46:;
    goto try_end_48;
    // Exception handler code:
    try_except_handler_47:;
    exception_keeper_type_48 = exception_type;
    exception_keeper_value_48 = exception_value;
    exception_keeper_tb_48 = exception_tb;
    exception_keeper_lineno_48 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_48;
        nuitka_bool tmp_cmp_expr_left_35;
        nuitka_bool tmp_cmp_expr_right_35;
        assert(tmp_with_12__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_35 = tmp_with_12__indicator;
        tmp_cmp_expr_right_35 = NUITKA_BOOL_TRUE;
        tmp_condition_result_48 = (tmp_cmp_expr_left_35 == tmp_cmp_expr_right_35) ? true : false;
        if (tmp_condition_result_48 != false) {
            goto branch_yes_48;
        } else {
            goto branch_no_48;
        }
    }
    branch_yes_48:;
    {
        PyObject *tmp_called_value_117;
        PyObject *tmp_call_result_71;
        CHECK_OBJECT(tmp_with_12__exit);
        tmp_called_value_117 = tmp_with_12__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 595;
        tmp_call_result_71 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_117, mod_consts[74]);

        if (tmp_call_result_71 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_48);
            Py_XDECREF(exception_keeper_value_48);
            Py_XDECREF(exception_keeper_tb_48);

            exception_lineno = 595;

            goto try_except_handler_46;
        }
        Py_DECREF(tmp_call_result_71);
    }
    branch_no_48:;
    // Re-raise.
    exception_type = exception_keeper_type_48;
    exception_value = exception_keeper_value_48;
    exception_tb = exception_keeper_tb_48;
    exception_lineno = exception_keeper_lineno_48;

    goto try_except_handler_46;
    // End of try:
    try_end_48:;
    {
        bool tmp_condition_result_49;
        nuitka_bool tmp_cmp_expr_left_36;
        nuitka_bool tmp_cmp_expr_right_36;
        assert(tmp_with_12__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_36 = tmp_with_12__indicator;
        tmp_cmp_expr_right_36 = NUITKA_BOOL_TRUE;
        tmp_condition_result_49 = (tmp_cmp_expr_left_36 == tmp_cmp_expr_right_36) ? true : false;
        if (tmp_condition_result_49 != false) {
            goto branch_yes_49;
        } else {
            goto branch_no_49;
        }
    }
    branch_yes_49:;
    {
        PyObject *tmp_called_value_118;
        PyObject *tmp_call_result_72;
        CHECK_OBJECT(tmp_with_12__exit);
        tmp_called_value_118 = tmp_with_12__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 595;
        tmp_call_result_72 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_118, mod_consts[74]);

        if (tmp_call_result_72 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 595;

            goto try_except_handler_46;
        }
        Py_DECREF(tmp_call_result_72);
    }
    branch_no_49:;
    goto try_end_49;
    // Exception handler code:
    try_except_handler_46:;
    exception_keeper_type_49 = exception_type;
    exception_keeper_value_49 = exception_value;
    exception_keeper_tb_49 = exception_tb;
    exception_keeper_lineno_49 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_12__source);
    tmp_with_12__source = NULL;
    Py_XDECREF(tmp_with_12__enter);
    tmp_with_12__enter = NULL;
    Py_XDECREF(tmp_with_12__exit);
    tmp_with_12__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_49;
    exception_value = exception_keeper_value_49;
    exception_tb = exception_keeper_tb_49;
    exception_lineno = exception_keeper_lineno_49;

    goto frame_exception_exit_1;
    // End of try:
    try_end_49:;
    CHECK_OBJECT(tmp_with_12__source);
    Py_DECREF(tmp_with_12__source);
    tmp_with_12__source = NULL;
    CHECK_OBJECT(tmp_with_12__enter);
    Py_DECREF(tmp_with_12__enter);
    tmp_with_12__enter = NULL;
    Py_XDECREF(tmp_with_12__exit);
    tmp_with_12__exit = NULL;
    {
        PyObject *tmp_assign_source_131;
        tmp_assign_source_131 = mod_consts[255];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[256], tmp_assign_source_131);
    }
    {
        PyObject *tmp_assign_source_132;
        tmp_assign_source_132 = LIST_COPY(mod_consts[257]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[231], tmp_assign_source_132);
    }
    {
        PyObject *tmp_assign_source_133;
        tmp_assign_source_133 = LIST_COPY(mod_consts[258]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[233], tmp_assign_source_133);
    }
    {
        PyObject *tmp_assign_source_134;
        tmp_assign_source_134 = LIST_COPY(mod_consts[259]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[234], tmp_assign_source_134);
    }
    {
        PyObject *tmp_assign_source_135;
        tmp_assign_source_135 = LIST_COPY(mod_consts[235]);
        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[236], tmp_assign_source_135);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_136;
        PyObject *tmp_called_instance_13;
        tmp_called_instance_13 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_13 == NULL)) {
            tmp_called_instance_13 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 611;

            goto try_except_handler_50;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 611;
        tmp_assign_source_136 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_13,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[239], 0)
        );

        if (tmp_assign_source_136 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 611;

            goto try_except_handler_50;
        }
        assert(tmp_with_13__source == NULL);
        tmp_with_13__source = tmp_assign_source_136;
    }
    {
        PyObject *tmp_assign_source_137;
        PyObject *tmp_called_value_119;
        PyObject *tmp_expression_value_79;
        CHECK_OBJECT(tmp_with_13__source);
        tmp_expression_value_79 = tmp_with_13__source;
        tmp_called_value_119 = LOOKUP_SPECIAL(tmp_expression_value_79, mod_consts[67]);
        if (tmp_called_value_119 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 611;

            goto try_except_handler_50;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 611;
        tmp_assign_source_137 = CALL_FUNCTION_NO_ARGS(tmp_called_value_119);
        Py_DECREF(tmp_called_value_119);
        if (tmp_assign_source_137 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 611;

            goto try_except_handler_50;
        }
        assert(tmp_with_13__enter == NULL);
        tmp_with_13__enter = tmp_assign_source_137;
    }
    {
        PyObject *tmp_assign_source_138;
        PyObject *tmp_expression_value_80;
        CHECK_OBJECT(tmp_with_13__source);
        tmp_expression_value_80 = tmp_with_13__source;
        tmp_assign_source_138 = LOOKUP_SPECIAL(tmp_expression_value_80, mod_consts[68]);
        if (tmp_assign_source_138 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 611;

            goto try_except_handler_50;
        }
        assert(tmp_with_13__exit == NULL);
        tmp_with_13__exit = tmp_assign_source_138;
    }
    {
        nuitka_bool tmp_assign_source_139;
        tmp_assign_source_139 = NUITKA_BOOL_TRUE;
        tmp_with_13__indicator = tmp_assign_source_139;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_120;
        PyObject *tmp_expression_value_81;
        PyObject *tmp_call_result_73;
        PyObject *tmp_args_value_1;
        PyObject *tmp_tuple_element_1;
        PyObject *tmp_kwargs_value_1;
        tmp_expression_value_81 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_81 == NULL)) {
            tmp_expression_value_81 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_81 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 612;

            goto try_except_handler_52;
        }
        tmp_called_value_120 = LOOKUP_ATTRIBUTE(tmp_expression_value_81, mod_consts[69]);
        if (tmp_called_value_120 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 612;

            goto try_except_handler_52;
        }
        tmp_tuple_element_1 = mod_consts[260];
        tmp_args_value_1 = PyTuple_New(3);
        {
            PyObject *tmp_called_value_121;
            PyObject *tmp_expression_value_82;
            PyObject *tmp_kw_call_value_0_8;
            PyObject *tmp_kw_call_value_1_7;
            PyObject *tmp_str_arg_value_6;
            PyObject *tmp_iterable_value_6;
            PyTuple_SET_ITEM0(tmp_args_value_1, 0, tmp_tuple_element_1);
            tmp_tuple_element_1 = mod_consts[241];
            PyTuple_SET_ITEM0(tmp_args_value_1, 1, tmp_tuple_element_1);
            tmp_expression_value_82 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[256]);

            if (unlikely(tmp_expression_value_82 == NULL)) {
                tmp_expression_value_82 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[256]);
            }

            if (tmp_expression_value_82 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 615;

                goto tuple_build_exception_1;
            }
            tmp_called_value_121 = LOOKUP_ATTRIBUTE(tmp_expression_value_82, mod_consts[242]);
            if (tmp_called_value_121 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 615;

                goto tuple_build_exception_1;
            }
            tmp_kw_call_value_0_8 = mod_consts[243];
            tmp_str_arg_value_6 = mod_consts[244];
            tmp_iterable_value_6 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[231]);

            if (unlikely(tmp_iterable_value_6 == NULL)) {
                tmp_iterable_value_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[231]);
            }

            if (tmp_iterable_value_6 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_121);

                exception_lineno = 615;

                goto tuple_build_exception_1;
            }
            tmp_kw_call_value_1_7 = UNICODE_JOIN(tmp_str_arg_value_6, tmp_iterable_value_6);
            if (tmp_kw_call_value_1_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_121);

                exception_lineno = 615;

                goto tuple_build_exception_1;
            }
            frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 615;
            {
                PyObject *kw_values[2] = {tmp_kw_call_value_0_8, tmp_kw_call_value_1_7};

                tmp_tuple_element_1 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_121, kw_values, mod_consts[245]);
            }

            Py_DECREF(tmp_called_value_121);
            Py_DECREF(tmp_kw_call_value_1_7);
            if (tmp_tuple_element_1 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 615;

                goto tuple_build_exception_1;
            }
            PyTuple_SET_ITEM(tmp_args_value_1, 2, tmp_tuple_element_1);
        }
        goto tuple_build_noexception_1;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_1:;
        Py_DECREF(tmp_called_value_120);
        Py_DECREF(tmp_args_value_1);
        goto try_except_handler_52;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_1:;
        tmp_kwargs_value_1 = PyDict_Copy(mod_consts[261]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 612;
        tmp_call_result_73 = CALL_FUNCTION(tmp_called_value_120, tmp_args_value_1, tmp_kwargs_value_1);
        Py_DECREF(tmp_called_value_120);
        Py_DECREF(tmp_args_value_1);
        Py_DECREF(tmp_kwargs_value_1);
        if (tmp_call_result_73 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 612;

            goto try_except_handler_52;
        }
        Py_DECREF(tmp_call_result_73);
    }
    goto try_end_50;
    // Exception handler code:
    try_except_handler_52:;
    exception_keeper_type_50 = exception_type;
    exception_keeper_value_50 = exception_value;
    exception_keeper_tb_50 = exception_tb;
    exception_keeper_lineno_50 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 13.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_13, &exception_preserved_value_13, &exception_preserved_tb_13);

    if (exception_keeper_tb_50 == NULL) {
        exception_keeper_tb_50 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_50);
    } else if (exception_keeper_lineno_50 != 0) {
        exception_keeper_tb_50 = ADD_TRACEBACK(exception_keeper_tb_50, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_50);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_50, &exception_keeper_value_50, &exception_keeper_tb_50);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_50, exception_keeper_tb_50);
    PUBLISH_EXCEPTION(&exception_keeper_type_50, &exception_keeper_value_50, &exception_keeper_tb_50);
    // Tried code:
    {
        bool tmp_condition_result_50;
        PyObject *tmp_cmp_expr_left_37;
        PyObject *tmp_cmp_expr_right_37;
        tmp_cmp_expr_left_37 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_37 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_37, tmp_cmp_expr_right_37);
        assert(!(tmp_res == -1));
        tmp_condition_result_50 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_50 != false) {
            goto branch_yes_50;
        } else {
            goto branch_no_50;
        }
    }
    branch_yes_50:;
    {
        nuitka_bool tmp_assign_source_140;
        tmp_assign_source_140 = NUITKA_BOOL_FALSE;
        tmp_with_13__indicator = tmp_assign_source_140;
    }
    {
        bool tmp_condition_result_51;
        PyObject *tmp_operand_value_13;
        PyObject *tmp_called_value_122;
        PyObject *tmp_args_element_value_55;
        PyObject *tmp_args_element_value_56;
        PyObject *tmp_args_element_value_57;
        CHECK_OBJECT(tmp_with_13__exit);
        tmp_called_value_122 = tmp_with_13__exit;
        tmp_args_element_value_55 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_56 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_57 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 616;
        {
            PyObject *call_args[] = {tmp_args_element_value_55, tmp_args_element_value_56, tmp_args_element_value_57};
            tmp_operand_value_13 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_122, call_args);
        }

        if (tmp_operand_value_13 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 616;

            goto try_except_handler_53;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_13);
        Py_DECREF(tmp_operand_value_13);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 616;

            goto try_except_handler_53;
        }
        tmp_condition_result_51 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_51 != false) {
            goto branch_yes_51;
        } else {
            goto branch_no_51;
        }
    }
    branch_yes_51:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 616;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_53;
    branch_no_51:;
    goto branch_end_50;
    branch_no_50:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 611;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_53;
    branch_end_50:;
    goto try_end_51;
    // Exception handler code:
    try_except_handler_53:;
    exception_keeper_type_51 = exception_type;
    exception_keeper_value_51 = exception_value;
    exception_keeper_tb_51 = exception_tb;
    exception_keeper_lineno_51 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 13.
    SET_CURRENT_EXCEPTION(exception_preserved_type_13, exception_preserved_value_13, exception_preserved_tb_13);

    // Re-raise.
    exception_type = exception_keeper_type_51;
    exception_value = exception_keeper_value_51;
    exception_tb = exception_keeper_tb_51;
    exception_lineno = exception_keeper_lineno_51;

    goto try_except_handler_51;
    // End of try:
    try_end_51:;
    // Restore previous exception id 13.
    SET_CURRENT_EXCEPTION(exception_preserved_type_13, exception_preserved_value_13, exception_preserved_tb_13);

    goto try_end_50;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_50:;
    goto try_end_52;
    // Exception handler code:
    try_except_handler_51:;
    exception_keeper_type_52 = exception_type;
    exception_keeper_value_52 = exception_value;
    exception_keeper_tb_52 = exception_tb;
    exception_keeper_lineno_52 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_52;
        nuitka_bool tmp_cmp_expr_left_38;
        nuitka_bool tmp_cmp_expr_right_38;
        assert(tmp_with_13__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_38 = tmp_with_13__indicator;
        tmp_cmp_expr_right_38 = NUITKA_BOOL_TRUE;
        tmp_condition_result_52 = (tmp_cmp_expr_left_38 == tmp_cmp_expr_right_38) ? true : false;
        if (tmp_condition_result_52 != false) {
            goto branch_yes_52;
        } else {
            goto branch_no_52;
        }
    }
    branch_yes_52:;
    {
        PyObject *tmp_called_value_123;
        PyObject *tmp_call_result_74;
        CHECK_OBJECT(tmp_with_13__exit);
        tmp_called_value_123 = tmp_with_13__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 616;
        tmp_call_result_74 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_123, mod_consts[74]);

        if (tmp_call_result_74 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_52);
            Py_XDECREF(exception_keeper_value_52);
            Py_XDECREF(exception_keeper_tb_52);

            exception_lineno = 616;

            goto try_except_handler_50;
        }
        Py_DECREF(tmp_call_result_74);
    }
    branch_no_52:;
    // Re-raise.
    exception_type = exception_keeper_type_52;
    exception_value = exception_keeper_value_52;
    exception_tb = exception_keeper_tb_52;
    exception_lineno = exception_keeper_lineno_52;

    goto try_except_handler_50;
    // End of try:
    try_end_52:;
    {
        bool tmp_condition_result_53;
        nuitka_bool tmp_cmp_expr_left_39;
        nuitka_bool tmp_cmp_expr_right_39;
        assert(tmp_with_13__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_39 = tmp_with_13__indicator;
        tmp_cmp_expr_right_39 = NUITKA_BOOL_TRUE;
        tmp_condition_result_53 = (tmp_cmp_expr_left_39 == tmp_cmp_expr_right_39) ? true : false;
        if (tmp_condition_result_53 != false) {
            goto branch_yes_53;
        } else {
            goto branch_no_53;
        }
    }
    branch_yes_53:;
    {
        PyObject *tmp_called_value_124;
        PyObject *tmp_call_result_75;
        CHECK_OBJECT(tmp_with_13__exit);
        tmp_called_value_124 = tmp_with_13__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 616;
        tmp_call_result_75 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_124, mod_consts[74]);

        if (tmp_call_result_75 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 616;

            goto try_except_handler_50;
        }
        Py_DECREF(tmp_call_result_75);
    }
    branch_no_53:;
    goto try_end_53;
    // Exception handler code:
    try_except_handler_50:;
    exception_keeper_type_53 = exception_type;
    exception_keeper_value_53 = exception_value;
    exception_keeper_tb_53 = exception_tb;
    exception_keeper_lineno_53 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_13__source);
    tmp_with_13__source = NULL;
    Py_XDECREF(tmp_with_13__enter);
    tmp_with_13__enter = NULL;
    Py_XDECREF(tmp_with_13__exit);
    tmp_with_13__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_53;
    exception_value = exception_keeper_value_53;
    exception_tb = exception_keeper_tb_53;
    exception_lineno = exception_keeper_lineno_53;

    goto frame_exception_exit_1;
    // End of try:
    try_end_53:;
    CHECK_OBJECT(tmp_with_13__source);
    Py_DECREF(tmp_with_13__source);
    tmp_with_13__source = NULL;
    CHECK_OBJECT(tmp_with_13__enter);
    Py_DECREF(tmp_with_13__enter);
    tmp_with_13__enter = NULL;
    Py_XDECREF(tmp_with_13__exit);
    tmp_with_13__exit = NULL;
    {
        PyObject *tmp_called_value_125;
        PyObject *tmp_expression_value_83;
        PyObject *tmp_call_result_76;
        tmp_expression_value_83 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_83 == NULL)) {
            tmp_expression_value_83 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_83 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 618;

            goto frame_exception_exit_1;
        }
        tmp_called_value_125 = LOOKUP_ATTRIBUTE(tmp_expression_value_83, mod_consts[209]);
        if (tmp_called_value_125 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 618;

            goto frame_exception_exit_1;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 618;
        tmp_call_result_76 = CALL_FUNCTION_WITH_ARGS1_VECTORCALL(tmp_called_value_125, &PyTuple_GET_ITEM(mod_consts[262], 0), mod_consts[263]);
        Py_DECREF(tmp_called_value_125);
        if (tmp_call_result_76 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 618;

            goto frame_exception_exit_1;
        }
        Py_DECREF(tmp_call_result_76);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_141;
        PyObject *tmp_called_instance_14;
        tmp_called_instance_14 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_14 == NULL)) {
            tmp_called_instance_14 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 626;

            goto try_except_handler_54;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 626;
        tmp_assign_source_141 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_14,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[247], 0)
        );

        if (tmp_assign_source_141 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 626;

            goto try_except_handler_54;
        }
        assert(tmp_with_14__source == NULL);
        tmp_with_14__source = tmp_assign_source_141;
    }
    {
        PyObject *tmp_assign_source_142;
        PyObject *tmp_called_value_126;
        PyObject *tmp_expression_value_84;
        CHECK_OBJECT(tmp_with_14__source);
        tmp_expression_value_84 = tmp_with_14__source;
        tmp_called_value_126 = LOOKUP_SPECIAL(tmp_expression_value_84, mod_consts[67]);
        if (tmp_called_value_126 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 626;

            goto try_except_handler_54;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 626;
        tmp_assign_source_142 = CALL_FUNCTION_NO_ARGS(tmp_called_value_126);
        Py_DECREF(tmp_called_value_126);
        if (tmp_assign_source_142 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 626;

            goto try_except_handler_54;
        }
        assert(tmp_with_14__enter == NULL);
        tmp_with_14__enter = tmp_assign_source_142;
    }
    {
        PyObject *tmp_assign_source_143;
        PyObject *tmp_expression_value_85;
        CHECK_OBJECT(tmp_with_14__source);
        tmp_expression_value_85 = tmp_with_14__source;
        tmp_assign_source_143 = LOOKUP_SPECIAL(tmp_expression_value_85, mod_consts[68]);
        if (tmp_assign_source_143 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 626;

            goto try_except_handler_54;
        }
        assert(tmp_with_14__exit == NULL);
        tmp_with_14__exit = tmp_assign_source_143;
    }
    {
        nuitka_bool tmp_assign_source_144;
        tmp_assign_source_144 = NUITKA_BOOL_TRUE;
        tmp_with_14__indicator = tmp_assign_source_144;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_127;
        PyObject *tmp_expression_value_86;
        PyObject *tmp_call_result_77;
        PyObject *tmp_args_value_2;
        PyObject *tmp_tuple_element_2;
        PyObject *tmp_kwargs_value_2;
        tmp_expression_value_86 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_86 == NULL)) {
            tmp_expression_value_86 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_86 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 627;

            goto try_except_handler_56;
        }
        tmp_called_value_127 = LOOKUP_ATTRIBUTE(tmp_expression_value_86, mod_consts[69]);
        if (tmp_called_value_127 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 627;

            goto try_except_handler_56;
        }
        tmp_tuple_element_2 = mod_consts[260];
        tmp_args_value_2 = PyTuple_New(3);
        {
            PyObject *tmp_called_value_128;
            PyObject *tmp_expression_value_87;
            PyObject *tmp_kw_call_value_0_9;
            PyObject *tmp_kw_call_value_1_8;
            PyObject *tmp_str_arg_value_7;
            PyObject *tmp_iterable_value_7;
            PyTuple_SET_ITEM0(tmp_args_value_2, 0, tmp_tuple_element_2);
            tmp_tuple_element_2 = mod_consts[241];
            PyTuple_SET_ITEM0(tmp_args_value_2, 1, tmp_tuple_element_2);
            tmp_expression_value_87 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[256]);

            if (unlikely(tmp_expression_value_87 == NULL)) {
                tmp_expression_value_87 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[256]);
            }

            if (tmp_expression_value_87 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 630;

                goto tuple_build_exception_2;
            }
            tmp_called_value_128 = LOOKUP_ATTRIBUTE(tmp_expression_value_87, mod_consts[242]);
            if (tmp_called_value_128 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 630;

                goto tuple_build_exception_2;
            }
            tmp_kw_call_value_0_9 = mod_consts[248];
            tmp_str_arg_value_7 = mod_consts[244];
            tmp_iterable_value_7 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[233]);

            if (unlikely(tmp_iterable_value_7 == NULL)) {
                tmp_iterable_value_7 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[233]);
            }

            if (tmp_iterable_value_7 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_128);

                exception_lineno = 630;

                goto tuple_build_exception_2;
            }
            tmp_kw_call_value_1_8 = UNICODE_JOIN(tmp_str_arg_value_7, tmp_iterable_value_7);
            if (tmp_kw_call_value_1_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_128);

                exception_lineno = 630;

                goto tuple_build_exception_2;
            }
            frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 630;
            {
                PyObject *kw_values[2] = {tmp_kw_call_value_0_9, tmp_kw_call_value_1_8};

                tmp_tuple_element_2 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_128, kw_values, mod_consts[245]);
            }

            Py_DECREF(tmp_called_value_128);
            Py_DECREF(tmp_kw_call_value_1_8);
            if (tmp_tuple_element_2 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 630;

                goto tuple_build_exception_2;
            }
            PyTuple_SET_ITEM(tmp_args_value_2, 2, tmp_tuple_element_2);
        }
        goto tuple_build_noexception_2;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_2:;
        Py_DECREF(tmp_called_value_127);
        Py_DECREF(tmp_args_value_2);
        goto try_except_handler_56;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_2:;
        tmp_kwargs_value_2 = PyDict_Copy(mod_consts[261]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 627;
        tmp_call_result_77 = CALL_FUNCTION(tmp_called_value_127, tmp_args_value_2, tmp_kwargs_value_2);
        Py_DECREF(tmp_called_value_127);
        Py_DECREF(tmp_args_value_2);
        Py_DECREF(tmp_kwargs_value_2);
        if (tmp_call_result_77 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 627;

            goto try_except_handler_56;
        }
        Py_DECREF(tmp_call_result_77);
    }
    goto try_end_54;
    // Exception handler code:
    try_except_handler_56:;
    exception_keeper_type_54 = exception_type;
    exception_keeper_value_54 = exception_value;
    exception_keeper_tb_54 = exception_tb;
    exception_keeper_lineno_54 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 14.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_14, &exception_preserved_value_14, &exception_preserved_tb_14);

    if (exception_keeper_tb_54 == NULL) {
        exception_keeper_tb_54 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_54);
    } else if (exception_keeper_lineno_54 != 0) {
        exception_keeper_tb_54 = ADD_TRACEBACK(exception_keeper_tb_54, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_54);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_54, &exception_keeper_value_54, &exception_keeper_tb_54);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_54, exception_keeper_tb_54);
    PUBLISH_EXCEPTION(&exception_keeper_type_54, &exception_keeper_value_54, &exception_keeper_tb_54);
    // Tried code:
    {
        bool tmp_condition_result_54;
        PyObject *tmp_cmp_expr_left_40;
        PyObject *tmp_cmp_expr_right_40;
        tmp_cmp_expr_left_40 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_40 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_40, tmp_cmp_expr_right_40);
        assert(!(tmp_res == -1));
        tmp_condition_result_54 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_54 != false) {
            goto branch_yes_54;
        } else {
            goto branch_no_54;
        }
    }
    branch_yes_54:;
    {
        nuitka_bool tmp_assign_source_145;
        tmp_assign_source_145 = NUITKA_BOOL_FALSE;
        tmp_with_14__indicator = tmp_assign_source_145;
    }
    {
        bool tmp_condition_result_55;
        PyObject *tmp_operand_value_14;
        PyObject *tmp_called_value_129;
        PyObject *tmp_args_element_value_58;
        PyObject *tmp_args_element_value_59;
        PyObject *tmp_args_element_value_60;
        CHECK_OBJECT(tmp_with_14__exit);
        tmp_called_value_129 = tmp_with_14__exit;
        tmp_args_element_value_58 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_59 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_60 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 631;
        {
            PyObject *call_args[] = {tmp_args_element_value_58, tmp_args_element_value_59, tmp_args_element_value_60};
            tmp_operand_value_14 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_129, call_args);
        }

        if (tmp_operand_value_14 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 631;

            goto try_except_handler_57;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_14);
        Py_DECREF(tmp_operand_value_14);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 631;

            goto try_except_handler_57;
        }
        tmp_condition_result_55 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_55 != false) {
            goto branch_yes_55;
        } else {
            goto branch_no_55;
        }
    }
    branch_yes_55:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 631;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_57;
    branch_no_55:;
    goto branch_end_54;
    branch_no_54:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 626;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_57;
    branch_end_54:;
    goto try_end_55;
    // Exception handler code:
    try_except_handler_57:;
    exception_keeper_type_55 = exception_type;
    exception_keeper_value_55 = exception_value;
    exception_keeper_tb_55 = exception_tb;
    exception_keeper_lineno_55 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 14.
    SET_CURRENT_EXCEPTION(exception_preserved_type_14, exception_preserved_value_14, exception_preserved_tb_14);

    // Re-raise.
    exception_type = exception_keeper_type_55;
    exception_value = exception_keeper_value_55;
    exception_tb = exception_keeper_tb_55;
    exception_lineno = exception_keeper_lineno_55;

    goto try_except_handler_55;
    // End of try:
    try_end_55:;
    // Restore previous exception id 14.
    SET_CURRENT_EXCEPTION(exception_preserved_type_14, exception_preserved_value_14, exception_preserved_tb_14);

    goto try_end_54;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_54:;
    goto try_end_56;
    // Exception handler code:
    try_except_handler_55:;
    exception_keeper_type_56 = exception_type;
    exception_keeper_value_56 = exception_value;
    exception_keeper_tb_56 = exception_tb;
    exception_keeper_lineno_56 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_56;
        nuitka_bool tmp_cmp_expr_left_41;
        nuitka_bool tmp_cmp_expr_right_41;
        assert(tmp_with_14__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_41 = tmp_with_14__indicator;
        tmp_cmp_expr_right_41 = NUITKA_BOOL_TRUE;
        tmp_condition_result_56 = (tmp_cmp_expr_left_41 == tmp_cmp_expr_right_41) ? true : false;
        if (tmp_condition_result_56 != false) {
            goto branch_yes_56;
        } else {
            goto branch_no_56;
        }
    }
    branch_yes_56:;
    {
        PyObject *tmp_called_value_130;
        PyObject *tmp_call_result_78;
        CHECK_OBJECT(tmp_with_14__exit);
        tmp_called_value_130 = tmp_with_14__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 631;
        tmp_call_result_78 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_130, mod_consts[74]);

        if (tmp_call_result_78 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_56);
            Py_XDECREF(exception_keeper_value_56);
            Py_XDECREF(exception_keeper_tb_56);

            exception_lineno = 631;

            goto try_except_handler_54;
        }
        Py_DECREF(tmp_call_result_78);
    }
    branch_no_56:;
    // Re-raise.
    exception_type = exception_keeper_type_56;
    exception_value = exception_keeper_value_56;
    exception_tb = exception_keeper_tb_56;
    exception_lineno = exception_keeper_lineno_56;

    goto try_except_handler_54;
    // End of try:
    try_end_56:;
    {
        bool tmp_condition_result_57;
        nuitka_bool tmp_cmp_expr_left_42;
        nuitka_bool tmp_cmp_expr_right_42;
        assert(tmp_with_14__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_42 = tmp_with_14__indicator;
        tmp_cmp_expr_right_42 = NUITKA_BOOL_TRUE;
        tmp_condition_result_57 = (tmp_cmp_expr_left_42 == tmp_cmp_expr_right_42) ? true : false;
        if (tmp_condition_result_57 != false) {
            goto branch_yes_57;
        } else {
            goto branch_no_57;
        }
    }
    branch_yes_57:;
    {
        PyObject *tmp_called_value_131;
        PyObject *tmp_call_result_79;
        CHECK_OBJECT(tmp_with_14__exit);
        tmp_called_value_131 = tmp_with_14__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 631;
        tmp_call_result_79 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_131, mod_consts[74]);

        if (tmp_call_result_79 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 631;

            goto try_except_handler_54;
        }
        Py_DECREF(tmp_call_result_79);
    }
    branch_no_57:;
    goto try_end_57;
    // Exception handler code:
    try_except_handler_54:;
    exception_keeper_type_57 = exception_type;
    exception_keeper_value_57 = exception_value;
    exception_keeper_tb_57 = exception_tb;
    exception_keeper_lineno_57 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_14__source);
    tmp_with_14__source = NULL;
    Py_XDECREF(tmp_with_14__enter);
    tmp_with_14__enter = NULL;
    Py_XDECREF(tmp_with_14__exit);
    tmp_with_14__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_57;
    exception_value = exception_keeper_value_57;
    exception_tb = exception_keeper_tb_57;
    exception_lineno = exception_keeper_lineno_57;

    goto frame_exception_exit_1;
    // End of try:
    try_end_57:;
    CHECK_OBJECT(tmp_with_14__source);
    Py_DECREF(tmp_with_14__source);
    tmp_with_14__source = NULL;
    CHECK_OBJECT(tmp_with_14__enter);
    Py_DECREF(tmp_with_14__enter);
    tmp_with_14__enter = NULL;
    Py_XDECREF(tmp_with_14__exit);
    tmp_with_14__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_146;
        PyObject *tmp_called_instance_15;
        tmp_called_instance_15 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_15 == NULL)) {
            tmp_called_instance_15 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 635;

            goto try_except_handler_58;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 635;
        tmp_assign_source_146 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_15,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[249], 0)
        );

        if (tmp_assign_source_146 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 635;

            goto try_except_handler_58;
        }
        assert(tmp_with_15__source == NULL);
        tmp_with_15__source = tmp_assign_source_146;
    }
    {
        PyObject *tmp_assign_source_147;
        PyObject *tmp_called_value_132;
        PyObject *tmp_expression_value_88;
        CHECK_OBJECT(tmp_with_15__source);
        tmp_expression_value_88 = tmp_with_15__source;
        tmp_called_value_132 = LOOKUP_SPECIAL(tmp_expression_value_88, mod_consts[67]);
        if (tmp_called_value_132 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 635;

            goto try_except_handler_58;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 635;
        tmp_assign_source_147 = CALL_FUNCTION_NO_ARGS(tmp_called_value_132);
        Py_DECREF(tmp_called_value_132);
        if (tmp_assign_source_147 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 635;

            goto try_except_handler_58;
        }
        assert(tmp_with_15__enter == NULL);
        tmp_with_15__enter = tmp_assign_source_147;
    }
    {
        PyObject *tmp_assign_source_148;
        PyObject *tmp_expression_value_89;
        CHECK_OBJECT(tmp_with_15__source);
        tmp_expression_value_89 = tmp_with_15__source;
        tmp_assign_source_148 = LOOKUP_SPECIAL(tmp_expression_value_89, mod_consts[68]);
        if (tmp_assign_source_148 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 635;

            goto try_except_handler_58;
        }
        assert(tmp_with_15__exit == NULL);
        tmp_with_15__exit = tmp_assign_source_148;
    }
    {
        nuitka_bool tmp_assign_source_149;
        tmp_assign_source_149 = NUITKA_BOOL_TRUE;
        tmp_with_15__indicator = tmp_assign_source_149;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_133;
        PyObject *tmp_expression_value_90;
        PyObject *tmp_call_result_80;
        PyObject *tmp_args_value_3;
        PyObject *tmp_tuple_element_3;
        PyObject *tmp_kwargs_value_3;
        tmp_expression_value_90 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_90 == NULL)) {
            tmp_expression_value_90 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_90 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 636;

            goto try_except_handler_60;
        }
        tmp_called_value_133 = LOOKUP_ATTRIBUTE(tmp_expression_value_90, mod_consts[69]);
        if (tmp_called_value_133 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 636;

            goto try_except_handler_60;
        }
        tmp_tuple_element_3 = mod_consts[260];
        tmp_args_value_3 = PyTuple_New(3);
        {
            PyObject *tmp_called_value_134;
            PyObject *tmp_expression_value_91;
            PyObject *tmp_kw_call_value_0_10;
            PyObject *tmp_kw_call_value_1_9;
            PyObject *tmp_str_arg_value_8;
            PyObject *tmp_iterable_value_8;
            PyTuple_SET_ITEM0(tmp_args_value_3, 0, tmp_tuple_element_3);
            tmp_tuple_element_3 = mod_consts[241];
            PyTuple_SET_ITEM0(tmp_args_value_3, 1, tmp_tuple_element_3);
            tmp_expression_value_91 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[256]);

            if (unlikely(tmp_expression_value_91 == NULL)) {
                tmp_expression_value_91 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[256]);
            }

            if (tmp_expression_value_91 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 639;

                goto tuple_build_exception_3;
            }
            tmp_called_value_134 = LOOKUP_ATTRIBUTE(tmp_expression_value_91, mod_consts[242]);
            if (tmp_called_value_134 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 639;

                goto tuple_build_exception_3;
            }
            tmp_kw_call_value_0_10 = mod_consts[250];
            tmp_str_arg_value_8 = mod_consts[244];
            tmp_iterable_value_8 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[234]);

            if (unlikely(tmp_iterable_value_8 == NULL)) {
                tmp_iterable_value_8 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[234]);
            }

            if (tmp_iterable_value_8 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_134);

                exception_lineno = 639;

                goto tuple_build_exception_3;
            }
            tmp_kw_call_value_1_9 = UNICODE_JOIN(tmp_str_arg_value_8, tmp_iterable_value_8);
            if (tmp_kw_call_value_1_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_134);

                exception_lineno = 639;

                goto tuple_build_exception_3;
            }
            frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 639;
            {
                PyObject *kw_values[2] = {tmp_kw_call_value_0_10, tmp_kw_call_value_1_9};

                tmp_tuple_element_3 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_134, kw_values, mod_consts[245]);
            }

            Py_DECREF(tmp_called_value_134);
            Py_DECREF(tmp_kw_call_value_1_9);
            if (tmp_tuple_element_3 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 639;

                goto tuple_build_exception_3;
            }
            PyTuple_SET_ITEM(tmp_args_value_3, 2, tmp_tuple_element_3);
        }
        goto tuple_build_noexception_3;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_3:;
        Py_DECREF(tmp_called_value_133);
        Py_DECREF(tmp_args_value_3);
        goto try_except_handler_60;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_3:;
        tmp_kwargs_value_3 = PyDict_Copy(mod_consts[261]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 636;
        tmp_call_result_80 = CALL_FUNCTION(tmp_called_value_133, tmp_args_value_3, tmp_kwargs_value_3);
        Py_DECREF(tmp_called_value_133);
        Py_DECREF(tmp_args_value_3);
        Py_DECREF(tmp_kwargs_value_3);
        if (tmp_call_result_80 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 636;

            goto try_except_handler_60;
        }
        Py_DECREF(tmp_call_result_80);
    }
    goto try_end_58;
    // Exception handler code:
    try_except_handler_60:;
    exception_keeper_type_58 = exception_type;
    exception_keeper_value_58 = exception_value;
    exception_keeper_tb_58 = exception_tb;
    exception_keeper_lineno_58 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 15.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_15, &exception_preserved_value_15, &exception_preserved_tb_15);

    if (exception_keeper_tb_58 == NULL) {
        exception_keeper_tb_58 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_58);
    } else if (exception_keeper_lineno_58 != 0) {
        exception_keeper_tb_58 = ADD_TRACEBACK(exception_keeper_tb_58, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_58);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_58, &exception_keeper_value_58, &exception_keeper_tb_58);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_58, exception_keeper_tb_58);
    PUBLISH_EXCEPTION(&exception_keeper_type_58, &exception_keeper_value_58, &exception_keeper_tb_58);
    // Tried code:
    {
        bool tmp_condition_result_58;
        PyObject *tmp_cmp_expr_left_43;
        PyObject *tmp_cmp_expr_right_43;
        tmp_cmp_expr_left_43 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_43 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_43, tmp_cmp_expr_right_43);
        assert(!(tmp_res == -1));
        tmp_condition_result_58 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_58 != false) {
            goto branch_yes_58;
        } else {
            goto branch_no_58;
        }
    }
    branch_yes_58:;
    {
        nuitka_bool tmp_assign_source_150;
        tmp_assign_source_150 = NUITKA_BOOL_FALSE;
        tmp_with_15__indicator = tmp_assign_source_150;
    }
    {
        bool tmp_condition_result_59;
        PyObject *tmp_operand_value_15;
        PyObject *tmp_called_value_135;
        PyObject *tmp_args_element_value_61;
        PyObject *tmp_args_element_value_62;
        PyObject *tmp_args_element_value_63;
        CHECK_OBJECT(tmp_with_15__exit);
        tmp_called_value_135 = tmp_with_15__exit;
        tmp_args_element_value_61 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_62 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_63 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 640;
        {
            PyObject *call_args[] = {tmp_args_element_value_61, tmp_args_element_value_62, tmp_args_element_value_63};
            tmp_operand_value_15 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_135, call_args);
        }

        if (tmp_operand_value_15 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 640;

            goto try_except_handler_61;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_15);
        Py_DECREF(tmp_operand_value_15);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 640;

            goto try_except_handler_61;
        }
        tmp_condition_result_59 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_59 != false) {
            goto branch_yes_59;
        } else {
            goto branch_no_59;
        }
    }
    branch_yes_59:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 640;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_61;
    branch_no_59:;
    goto branch_end_58;
    branch_no_58:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 635;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_61;
    branch_end_58:;
    goto try_end_59;
    // Exception handler code:
    try_except_handler_61:;
    exception_keeper_type_59 = exception_type;
    exception_keeper_value_59 = exception_value;
    exception_keeper_tb_59 = exception_tb;
    exception_keeper_lineno_59 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 15.
    SET_CURRENT_EXCEPTION(exception_preserved_type_15, exception_preserved_value_15, exception_preserved_tb_15);

    // Re-raise.
    exception_type = exception_keeper_type_59;
    exception_value = exception_keeper_value_59;
    exception_tb = exception_keeper_tb_59;
    exception_lineno = exception_keeper_lineno_59;

    goto try_except_handler_59;
    // End of try:
    try_end_59:;
    // Restore previous exception id 15.
    SET_CURRENT_EXCEPTION(exception_preserved_type_15, exception_preserved_value_15, exception_preserved_tb_15);

    goto try_end_58;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_58:;
    goto try_end_60;
    // Exception handler code:
    try_except_handler_59:;
    exception_keeper_type_60 = exception_type;
    exception_keeper_value_60 = exception_value;
    exception_keeper_tb_60 = exception_tb;
    exception_keeper_lineno_60 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_60;
        nuitka_bool tmp_cmp_expr_left_44;
        nuitka_bool tmp_cmp_expr_right_44;
        assert(tmp_with_15__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_44 = tmp_with_15__indicator;
        tmp_cmp_expr_right_44 = NUITKA_BOOL_TRUE;
        tmp_condition_result_60 = (tmp_cmp_expr_left_44 == tmp_cmp_expr_right_44) ? true : false;
        if (tmp_condition_result_60 != false) {
            goto branch_yes_60;
        } else {
            goto branch_no_60;
        }
    }
    branch_yes_60:;
    {
        PyObject *tmp_called_value_136;
        PyObject *tmp_call_result_81;
        CHECK_OBJECT(tmp_with_15__exit);
        tmp_called_value_136 = tmp_with_15__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 640;
        tmp_call_result_81 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_136, mod_consts[74]);

        if (tmp_call_result_81 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_60);
            Py_XDECREF(exception_keeper_value_60);
            Py_XDECREF(exception_keeper_tb_60);

            exception_lineno = 640;

            goto try_except_handler_58;
        }
        Py_DECREF(tmp_call_result_81);
    }
    branch_no_60:;
    // Re-raise.
    exception_type = exception_keeper_type_60;
    exception_value = exception_keeper_value_60;
    exception_tb = exception_keeper_tb_60;
    exception_lineno = exception_keeper_lineno_60;

    goto try_except_handler_58;
    // End of try:
    try_end_60:;
    {
        bool tmp_condition_result_61;
        nuitka_bool tmp_cmp_expr_left_45;
        nuitka_bool tmp_cmp_expr_right_45;
        assert(tmp_with_15__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_45 = tmp_with_15__indicator;
        tmp_cmp_expr_right_45 = NUITKA_BOOL_TRUE;
        tmp_condition_result_61 = (tmp_cmp_expr_left_45 == tmp_cmp_expr_right_45) ? true : false;
        if (tmp_condition_result_61 != false) {
            goto branch_yes_61;
        } else {
            goto branch_no_61;
        }
    }
    branch_yes_61:;
    {
        PyObject *tmp_called_value_137;
        PyObject *tmp_call_result_82;
        CHECK_OBJECT(tmp_with_15__exit);
        tmp_called_value_137 = tmp_with_15__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 640;
        tmp_call_result_82 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_137, mod_consts[74]);

        if (tmp_call_result_82 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 640;

            goto try_except_handler_58;
        }
        Py_DECREF(tmp_call_result_82);
    }
    branch_no_61:;
    goto try_end_61;
    // Exception handler code:
    try_except_handler_58:;
    exception_keeper_type_61 = exception_type;
    exception_keeper_value_61 = exception_value;
    exception_keeper_tb_61 = exception_tb;
    exception_keeper_lineno_61 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_15__source);
    tmp_with_15__source = NULL;
    Py_XDECREF(tmp_with_15__enter);
    tmp_with_15__enter = NULL;
    Py_XDECREF(tmp_with_15__exit);
    tmp_with_15__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_61;
    exception_value = exception_keeper_value_61;
    exception_tb = exception_keeper_tb_61;
    exception_lineno = exception_keeper_lineno_61;

    goto frame_exception_exit_1;
    // End of try:
    try_end_61:;
    CHECK_OBJECT(tmp_with_15__source);
    Py_DECREF(tmp_with_15__source);
    tmp_with_15__source = NULL;
    CHECK_OBJECT(tmp_with_15__enter);
    Py_DECREF(tmp_with_15__enter);
    tmp_with_15__enter = NULL;
    Py_XDECREF(tmp_with_15__exit);
    tmp_with_15__exit = NULL;
    // Tried code:
    {
        PyObject *tmp_assign_source_151;
        PyObject *tmp_called_instance_16;
        tmp_called_instance_16 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_16 == NULL)) {
            tmp_called_instance_16 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 644;

            goto try_except_handler_62;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 644;
        tmp_assign_source_151 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_16,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[251], 0)
        );

        if (tmp_assign_source_151 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 644;

            goto try_except_handler_62;
        }
        assert(tmp_with_16__source == NULL);
        tmp_with_16__source = tmp_assign_source_151;
    }
    {
        PyObject *tmp_assign_source_152;
        PyObject *tmp_called_value_138;
        PyObject *tmp_expression_value_92;
        CHECK_OBJECT(tmp_with_16__source);
        tmp_expression_value_92 = tmp_with_16__source;
        tmp_called_value_138 = LOOKUP_SPECIAL(tmp_expression_value_92, mod_consts[67]);
        if (tmp_called_value_138 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 644;

            goto try_except_handler_62;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 644;
        tmp_assign_source_152 = CALL_FUNCTION_NO_ARGS(tmp_called_value_138);
        Py_DECREF(tmp_called_value_138);
        if (tmp_assign_source_152 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 644;

            goto try_except_handler_62;
        }
        assert(tmp_with_16__enter == NULL);
        tmp_with_16__enter = tmp_assign_source_152;
    }
    {
        PyObject *tmp_assign_source_153;
        PyObject *tmp_expression_value_93;
        CHECK_OBJECT(tmp_with_16__source);
        tmp_expression_value_93 = tmp_with_16__source;
        tmp_assign_source_153 = LOOKUP_SPECIAL(tmp_expression_value_93, mod_consts[68]);
        if (tmp_assign_source_153 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 644;

            goto try_except_handler_62;
        }
        assert(tmp_with_16__exit == NULL);
        tmp_with_16__exit = tmp_assign_source_153;
    }
    {
        nuitka_bool tmp_assign_source_154;
        tmp_assign_source_154 = NUITKA_BOOL_TRUE;
        tmp_with_16__indicator = tmp_assign_source_154;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_139;
        PyObject *tmp_expression_value_94;
        PyObject *tmp_call_result_83;
        PyObject *tmp_args_value_4;
        PyObject *tmp_tuple_element_4;
        PyObject *tmp_kwargs_value_4;
        tmp_expression_value_94 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_94 == NULL)) {
            tmp_expression_value_94 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_94 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 645;

            goto try_except_handler_64;
        }
        tmp_called_value_139 = LOOKUP_ATTRIBUTE(tmp_expression_value_94, mod_consts[69]);
        if (tmp_called_value_139 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 645;

            goto try_except_handler_64;
        }
        tmp_tuple_element_4 = mod_consts[260];
        tmp_args_value_4 = PyTuple_New(3);
        {
            PyObject *tmp_called_value_140;
            PyObject *tmp_expression_value_95;
            PyObject *tmp_kw_call_value_0_11;
            PyObject *tmp_kw_call_value_1_10;
            PyObject *tmp_str_arg_value_9;
            PyObject *tmp_iterable_value_9;
            PyTuple_SET_ITEM0(tmp_args_value_4, 0, tmp_tuple_element_4);
            tmp_tuple_element_4 = mod_consts[241];
            PyTuple_SET_ITEM0(tmp_args_value_4, 1, tmp_tuple_element_4);
            tmp_expression_value_95 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[256]);

            if (unlikely(tmp_expression_value_95 == NULL)) {
                tmp_expression_value_95 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[256]);
            }

            if (tmp_expression_value_95 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 648;

                goto tuple_build_exception_4;
            }
            tmp_called_value_140 = LOOKUP_ATTRIBUTE(tmp_expression_value_95, mod_consts[242]);
            if (tmp_called_value_140 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 648;

                goto tuple_build_exception_4;
            }
            tmp_kw_call_value_0_11 = mod_consts[252];
            tmp_str_arg_value_9 = mod_consts[244];
            tmp_iterable_value_9 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[236]);

            if (unlikely(tmp_iterable_value_9 == NULL)) {
                tmp_iterable_value_9 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[236]);
            }

            if (tmp_iterable_value_9 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_140);

                exception_lineno = 648;

                goto tuple_build_exception_4;
            }
            tmp_kw_call_value_1_10 = UNICODE_JOIN(tmp_str_arg_value_9, tmp_iterable_value_9);
            if (tmp_kw_call_value_1_10 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
                Py_DECREF(tmp_called_value_140);

                exception_lineno = 648;

                goto tuple_build_exception_4;
            }
            frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 648;
            {
                PyObject *kw_values[2] = {tmp_kw_call_value_0_11, tmp_kw_call_value_1_10};

                tmp_tuple_element_4 = CALL_FUNCTION_WITH_NO_ARGS_KWSPLIT(tmp_called_value_140, kw_values, mod_consts[245]);
            }

            Py_DECREF(tmp_called_value_140);
            Py_DECREF(tmp_kw_call_value_1_10);
            if (tmp_tuple_element_4 == NULL) {
                assert(ERROR_OCCURRED());

                FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


                exception_lineno = 648;

                goto tuple_build_exception_4;
            }
            PyTuple_SET_ITEM(tmp_args_value_4, 2, tmp_tuple_element_4);
        }
        goto tuple_build_noexception_4;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_4:;
        Py_DECREF(tmp_called_value_139);
        Py_DECREF(tmp_args_value_4);
        goto try_except_handler_64;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_4:;
        tmp_kwargs_value_4 = PyDict_Copy(mod_consts[261]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 645;
        tmp_call_result_83 = CALL_FUNCTION(tmp_called_value_139, tmp_args_value_4, tmp_kwargs_value_4);
        Py_DECREF(tmp_called_value_139);
        Py_DECREF(tmp_args_value_4);
        Py_DECREF(tmp_kwargs_value_4);
        if (tmp_call_result_83 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 645;

            goto try_except_handler_64;
        }
        Py_DECREF(tmp_call_result_83);
    }
    goto try_end_62;
    // Exception handler code:
    try_except_handler_64:;
    exception_keeper_type_62 = exception_type;
    exception_keeper_value_62 = exception_value;
    exception_keeper_tb_62 = exception_tb;
    exception_keeper_lineno_62 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 16.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_16, &exception_preserved_value_16, &exception_preserved_tb_16);

    if (exception_keeper_tb_62 == NULL) {
        exception_keeper_tb_62 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_62);
    } else if (exception_keeper_lineno_62 != 0) {
        exception_keeper_tb_62 = ADD_TRACEBACK(exception_keeper_tb_62, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_62);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_62, &exception_keeper_value_62, &exception_keeper_tb_62);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_62, exception_keeper_tb_62);
    PUBLISH_EXCEPTION(&exception_keeper_type_62, &exception_keeper_value_62, &exception_keeper_tb_62);
    // Tried code:
    {
        bool tmp_condition_result_62;
        PyObject *tmp_cmp_expr_left_46;
        PyObject *tmp_cmp_expr_right_46;
        tmp_cmp_expr_left_46 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_46 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_46, tmp_cmp_expr_right_46);
        assert(!(tmp_res == -1));
        tmp_condition_result_62 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_62 != false) {
            goto branch_yes_62;
        } else {
            goto branch_no_62;
        }
    }
    branch_yes_62:;
    {
        nuitka_bool tmp_assign_source_155;
        tmp_assign_source_155 = NUITKA_BOOL_FALSE;
        tmp_with_16__indicator = tmp_assign_source_155;
    }
    {
        bool tmp_condition_result_63;
        PyObject *tmp_operand_value_16;
        PyObject *tmp_called_value_141;
        PyObject *tmp_args_element_value_64;
        PyObject *tmp_args_element_value_65;
        PyObject *tmp_args_element_value_66;
        CHECK_OBJECT(tmp_with_16__exit);
        tmp_called_value_141 = tmp_with_16__exit;
        tmp_args_element_value_64 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_65 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_66 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 649;
        {
            PyObject *call_args[] = {tmp_args_element_value_64, tmp_args_element_value_65, tmp_args_element_value_66};
            tmp_operand_value_16 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_141, call_args);
        }

        if (tmp_operand_value_16 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 649;

            goto try_except_handler_65;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_16);
        Py_DECREF(tmp_operand_value_16);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 649;

            goto try_except_handler_65;
        }
        tmp_condition_result_63 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_63 != false) {
            goto branch_yes_63;
        } else {
            goto branch_no_63;
        }
    }
    branch_yes_63:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 649;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_65;
    branch_no_63:;
    goto branch_end_62;
    branch_no_62:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 644;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_65;
    branch_end_62:;
    goto try_end_63;
    // Exception handler code:
    try_except_handler_65:;
    exception_keeper_type_63 = exception_type;
    exception_keeper_value_63 = exception_value;
    exception_keeper_tb_63 = exception_tb;
    exception_keeper_lineno_63 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 16.
    SET_CURRENT_EXCEPTION(exception_preserved_type_16, exception_preserved_value_16, exception_preserved_tb_16);

    // Re-raise.
    exception_type = exception_keeper_type_63;
    exception_value = exception_keeper_value_63;
    exception_tb = exception_keeper_tb_63;
    exception_lineno = exception_keeper_lineno_63;

    goto try_except_handler_63;
    // End of try:
    try_end_63:;
    // Restore previous exception id 16.
    SET_CURRENT_EXCEPTION(exception_preserved_type_16, exception_preserved_value_16, exception_preserved_tb_16);

    goto try_end_62;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_62:;
    goto try_end_64;
    // Exception handler code:
    try_except_handler_63:;
    exception_keeper_type_64 = exception_type;
    exception_keeper_value_64 = exception_value;
    exception_keeper_tb_64 = exception_tb;
    exception_keeper_lineno_64 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_64;
        nuitka_bool tmp_cmp_expr_left_47;
        nuitka_bool tmp_cmp_expr_right_47;
        assert(tmp_with_16__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_47 = tmp_with_16__indicator;
        tmp_cmp_expr_right_47 = NUITKA_BOOL_TRUE;
        tmp_condition_result_64 = (tmp_cmp_expr_left_47 == tmp_cmp_expr_right_47) ? true : false;
        if (tmp_condition_result_64 != false) {
            goto branch_yes_64;
        } else {
            goto branch_no_64;
        }
    }
    branch_yes_64:;
    {
        PyObject *tmp_called_value_142;
        PyObject *tmp_call_result_84;
        CHECK_OBJECT(tmp_with_16__exit);
        tmp_called_value_142 = tmp_with_16__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 649;
        tmp_call_result_84 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_142, mod_consts[74]);

        if (tmp_call_result_84 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_64);
            Py_XDECREF(exception_keeper_value_64);
            Py_XDECREF(exception_keeper_tb_64);

            exception_lineno = 649;

            goto try_except_handler_62;
        }
        Py_DECREF(tmp_call_result_84);
    }
    branch_no_64:;
    // Re-raise.
    exception_type = exception_keeper_type_64;
    exception_value = exception_keeper_value_64;
    exception_tb = exception_keeper_tb_64;
    exception_lineno = exception_keeper_lineno_64;

    goto try_except_handler_62;
    // End of try:
    try_end_64:;
    {
        bool tmp_condition_result_65;
        nuitka_bool tmp_cmp_expr_left_48;
        nuitka_bool tmp_cmp_expr_right_48;
        assert(tmp_with_16__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_48 = tmp_with_16__indicator;
        tmp_cmp_expr_right_48 = NUITKA_BOOL_TRUE;
        tmp_condition_result_65 = (tmp_cmp_expr_left_48 == tmp_cmp_expr_right_48) ? true : false;
        if (tmp_condition_result_65 != false) {
            goto branch_yes_65;
        } else {
            goto branch_no_65;
        }
    }
    branch_yes_65:;
    {
        PyObject *tmp_called_value_143;
        PyObject *tmp_call_result_85;
        CHECK_OBJECT(tmp_with_16__exit);
        tmp_called_value_143 = tmp_with_16__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 649;
        tmp_call_result_85 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_143, mod_consts[74]);

        if (tmp_call_result_85 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 649;

            goto try_except_handler_62;
        }
        Py_DECREF(tmp_call_result_85);
    }
    branch_no_65:;
    goto try_end_65;
    // Exception handler code:
    try_except_handler_62:;
    exception_keeper_type_65 = exception_type;
    exception_keeper_value_65 = exception_value;
    exception_keeper_tb_65 = exception_tb;
    exception_keeper_lineno_65 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_16__source);
    tmp_with_16__source = NULL;
    Py_XDECREF(tmp_with_16__enter);
    tmp_with_16__enter = NULL;
    Py_XDECREF(tmp_with_16__exit);
    tmp_with_16__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_65;
    exception_value = exception_keeper_value_65;
    exception_tb = exception_keeper_tb_65;
    exception_lineno = exception_keeper_lineno_65;

    goto frame_exception_exit_1;
    // End of try:
    try_end_65:;
    CHECK_OBJECT(tmp_with_16__source);
    Py_DECREF(tmp_with_16__source);
    tmp_with_16__source = NULL;
    CHECK_OBJECT(tmp_with_16__enter);
    Py_DECREF(tmp_with_16__enter);
    tmp_with_16__enter = NULL;
    Py_XDECREF(tmp_with_16__exit);
    tmp_with_16__exit = NULL;
    {
        PyObject *tmp_assign_source_156;
        tmp_assign_source_156 = mod_consts[264];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[265], tmp_assign_source_156);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_157;
        PyObject *tmp_called_instance_17;
        tmp_called_instance_17 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_17 == NULL)) {
            tmp_called_instance_17 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 660;

            goto try_except_handler_66;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 660;
        tmp_assign_source_157 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_17,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[266], 0)
        );

        if (tmp_assign_source_157 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 660;

            goto try_except_handler_66;
        }
        assert(tmp_with_17__source == NULL);
        tmp_with_17__source = tmp_assign_source_157;
    }
    {
        PyObject *tmp_assign_source_158;
        PyObject *tmp_called_value_144;
        PyObject *tmp_expression_value_96;
        CHECK_OBJECT(tmp_with_17__source);
        tmp_expression_value_96 = tmp_with_17__source;
        tmp_called_value_144 = LOOKUP_SPECIAL(tmp_expression_value_96, mod_consts[67]);
        if (tmp_called_value_144 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 660;

            goto try_except_handler_66;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 660;
        tmp_assign_source_158 = CALL_FUNCTION_NO_ARGS(tmp_called_value_144);
        Py_DECREF(tmp_called_value_144);
        if (tmp_assign_source_158 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 660;

            goto try_except_handler_66;
        }
        assert(tmp_with_17__enter == NULL);
        tmp_with_17__enter = tmp_assign_source_158;
    }
    {
        PyObject *tmp_assign_source_159;
        PyObject *tmp_expression_value_97;
        CHECK_OBJECT(tmp_with_17__source);
        tmp_expression_value_97 = tmp_with_17__source;
        tmp_assign_source_159 = LOOKUP_SPECIAL(tmp_expression_value_97, mod_consts[68]);
        if (tmp_assign_source_159 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 660;

            goto try_except_handler_66;
        }
        assert(tmp_with_17__exit == NULL);
        tmp_with_17__exit = tmp_assign_source_159;
    }
    {
        nuitka_bool tmp_assign_source_160;
        tmp_assign_source_160 = NUITKA_BOOL_TRUE;
        tmp_with_17__indicator = tmp_assign_source_160;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_145;
        PyObject *tmp_expression_value_98;
        PyObject *tmp_call_result_86;
        PyObject *tmp_kw_call_arg_value_0_42;
        PyObject *tmp_kw_call_arg_value_1_42;
        PyObject *tmp_kw_call_arg_value_2_42;
        PyObject *tmp_kw_call_dict_value_0_42;
        PyObject *tmp_called_value_146;
        PyObject *tmp_call_arg_element_10;
        tmp_expression_value_98 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_98 == NULL)) {
            tmp_expression_value_98 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_98 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 661;

            goto try_except_handler_68;
        }
        tmp_called_value_145 = LOOKUP_ATTRIBUTE(tmp_expression_value_98, mod_consts[69]);
        if (tmp_called_value_145 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 661;

            goto try_except_handler_68;
        }
        tmp_kw_call_arg_value_0_42 = mod_consts[267];
        tmp_kw_call_arg_value_1_42 = mod_consts[241];
        tmp_kw_call_arg_value_2_42 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[265]);

        if (unlikely(tmp_kw_call_arg_value_2_42 == NULL)) {
            tmp_kw_call_arg_value_2_42 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[265]);
        }

        if (tmp_kw_call_arg_value_2_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_145);

            exception_lineno = 664;

            goto try_except_handler_68;
        }
        tmp_called_value_146 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_146 == NULL)) {
            tmp_called_value_146 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_146 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_145);

            exception_lineno = 665;

            goto try_except_handler_68;
        }
        tmp_call_arg_element_10 = LIST_COPY(mod_consts[268]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 665;
        tmp_kw_call_dict_value_0_42 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_146, tmp_call_arg_element_10);
        Py_DECREF(tmp_call_arg_element_10);
        if (tmp_kw_call_dict_value_0_42 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_145);

            exception_lineno = 665;

            goto try_except_handler_68;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 661;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_42, tmp_kw_call_arg_value_1_42, tmp_kw_call_arg_value_2_42};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_42};
            tmp_call_result_86 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_145, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_145);
        Py_DECREF(tmp_kw_call_dict_value_0_42);
        if (tmp_call_result_86 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 661;

            goto try_except_handler_68;
        }
        Py_DECREF(tmp_call_result_86);
    }
    goto try_end_66;
    // Exception handler code:
    try_except_handler_68:;
    exception_keeper_type_66 = exception_type;
    exception_keeper_value_66 = exception_value;
    exception_keeper_tb_66 = exception_tb;
    exception_keeper_lineno_66 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 17.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_17, &exception_preserved_value_17, &exception_preserved_tb_17);

    if (exception_keeper_tb_66 == NULL) {
        exception_keeper_tb_66 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_66);
    } else if (exception_keeper_lineno_66 != 0) {
        exception_keeper_tb_66 = ADD_TRACEBACK(exception_keeper_tb_66, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_66);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_66, &exception_keeper_value_66, &exception_keeper_tb_66);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_66, exception_keeper_tb_66);
    PUBLISH_EXCEPTION(&exception_keeper_type_66, &exception_keeper_value_66, &exception_keeper_tb_66);
    // Tried code:
    {
        bool tmp_condition_result_66;
        PyObject *tmp_cmp_expr_left_49;
        PyObject *tmp_cmp_expr_right_49;
        tmp_cmp_expr_left_49 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_49 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_49, tmp_cmp_expr_right_49);
        assert(!(tmp_res == -1));
        tmp_condition_result_66 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_66 != false) {
            goto branch_yes_66;
        } else {
            goto branch_no_66;
        }
    }
    branch_yes_66:;
    {
        nuitka_bool tmp_assign_source_161;
        tmp_assign_source_161 = NUITKA_BOOL_FALSE;
        tmp_with_17__indicator = tmp_assign_source_161;
    }
    {
        bool tmp_condition_result_67;
        PyObject *tmp_operand_value_17;
        PyObject *tmp_called_value_147;
        PyObject *tmp_args_element_value_67;
        PyObject *tmp_args_element_value_68;
        PyObject *tmp_args_element_value_69;
        CHECK_OBJECT(tmp_with_17__exit);
        tmp_called_value_147 = tmp_with_17__exit;
        tmp_args_element_value_67 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_68 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_69 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 665;
        {
            PyObject *call_args[] = {tmp_args_element_value_67, tmp_args_element_value_68, tmp_args_element_value_69};
            tmp_operand_value_17 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_147, call_args);
        }

        if (tmp_operand_value_17 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 665;

            goto try_except_handler_69;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_17);
        Py_DECREF(tmp_operand_value_17);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 665;

            goto try_except_handler_69;
        }
        tmp_condition_result_67 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_67 != false) {
            goto branch_yes_67;
        } else {
            goto branch_no_67;
        }
    }
    branch_yes_67:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 665;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_69;
    branch_no_67:;
    goto branch_end_66;
    branch_no_66:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 660;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_69;
    branch_end_66:;
    goto try_end_67;
    // Exception handler code:
    try_except_handler_69:;
    exception_keeper_type_67 = exception_type;
    exception_keeper_value_67 = exception_value;
    exception_keeper_tb_67 = exception_tb;
    exception_keeper_lineno_67 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 17.
    SET_CURRENT_EXCEPTION(exception_preserved_type_17, exception_preserved_value_17, exception_preserved_tb_17);

    // Re-raise.
    exception_type = exception_keeper_type_67;
    exception_value = exception_keeper_value_67;
    exception_tb = exception_keeper_tb_67;
    exception_lineno = exception_keeper_lineno_67;

    goto try_except_handler_67;
    // End of try:
    try_end_67:;
    // Restore previous exception id 17.
    SET_CURRENT_EXCEPTION(exception_preserved_type_17, exception_preserved_value_17, exception_preserved_tb_17);

    goto try_end_66;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_66:;
    goto try_end_68;
    // Exception handler code:
    try_except_handler_67:;
    exception_keeper_type_68 = exception_type;
    exception_keeper_value_68 = exception_value;
    exception_keeper_tb_68 = exception_tb;
    exception_keeper_lineno_68 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_68;
        nuitka_bool tmp_cmp_expr_left_50;
        nuitka_bool tmp_cmp_expr_right_50;
        assert(tmp_with_17__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_50 = tmp_with_17__indicator;
        tmp_cmp_expr_right_50 = NUITKA_BOOL_TRUE;
        tmp_condition_result_68 = (tmp_cmp_expr_left_50 == tmp_cmp_expr_right_50) ? true : false;
        if (tmp_condition_result_68 != false) {
            goto branch_yes_68;
        } else {
            goto branch_no_68;
        }
    }
    branch_yes_68:;
    {
        PyObject *tmp_called_value_148;
        PyObject *tmp_call_result_87;
        CHECK_OBJECT(tmp_with_17__exit);
        tmp_called_value_148 = tmp_with_17__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 665;
        tmp_call_result_87 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_148, mod_consts[74]);

        if (tmp_call_result_87 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_68);
            Py_XDECREF(exception_keeper_value_68);
            Py_XDECREF(exception_keeper_tb_68);

            exception_lineno = 665;

            goto try_except_handler_66;
        }
        Py_DECREF(tmp_call_result_87);
    }
    branch_no_68:;
    // Re-raise.
    exception_type = exception_keeper_type_68;
    exception_value = exception_keeper_value_68;
    exception_tb = exception_keeper_tb_68;
    exception_lineno = exception_keeper_lineno_68;

    goto try_except_handler_66;
    // End of try:
    try_end_68:;
    {
        bool tmp_condition_result_69;
        nuitka_bool tmp_cmp_expr_left_51;
        nuitka_bool tmp_cmp_expr_right_51;
        assert(tmp_with_17__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_51 = tmp_with_17__indicator;
        tmp_cmp_expr_right_51 = NUITKA_BOOL_TRUE;
        tmp_condition_result_69 = (tmp_cmp_expr_left_51 == tmp_cmp_expr_right_51) ? true : false;
        if (tmp_condition_result_69 != false) {
            goto branch_yes_69;
        } else {
            goto branch_no_69;
        }
    }
    branch_yes_69:;
    {
        PyObject *tmp_called_value_149;
        PyObject *tmp_call_result_88;
        CHECK_OBJECT(tmp_with_17__exit);
        tmp_called_value_149 = tmp_with_17__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 665;
        tmp_call_result_88 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_149, mod_consts[74]);

        if (tmp_call_result_88 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 665;

            goto try_except_handler_66;
        }
        Py_DECREF(tmp_call_result_88);
    }
    branch_no_69:;
    goto try_end_69;
    // Exception handler code:
    try_except_handler_66:;
    exception_keeper_type_69 = exception_type;
    exception_keeper_value_69 = exception_value;
    exception_keeper_tb_69 = exception_tb;
    exception_keeper_lineno_69 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_17__source);
    tmp_with_17__source = NULL;
    Py_XDECREF(tmp_with_17__enter);
    tmp_with_17__enter = NULL;
    Py_XDECREF(tmp_with_17__exit);
    tmp_with_17__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_69;
    exception_value = exception_keeper_value_69;
    exception_tb = exception_keeper_tb_69;
    exception_lineno = exception_keeper_lineno_69;

    goto frame_exception_exit_1;
    // End of try:
    try_end_69:;
    CHECK_OBJECT(tmp_with_17__source);
    Py_DECREF(tmp_with_17__source);
    tmp_with_17__source = NULL;
    CHECK_OBJECT(tmp_with_17__enter);
    Py_DECREF(tmp_with_17__enter);
    tmp_with_17__enter = NULL;
    Py_XDECREF(tmp_with_17__exit);
    tmp_with_17__exit = NULL;
    {
        PyObject *tmp_assign_source_162;
        tmp_assign_source_162 = mod_consts[269];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[270], tmp_assign_source_162);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_163;
        PyObject *tmp_called_instance_18;
        tmp_called_instance_18 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_18 == NULL)) {
            tmp_called_instance_18 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 676;

            goto try_except_handler_70;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 676;
        tmp_assign_source_163 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_18,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[271], 0)
        );

        if (tmp_assign_source_163 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 676;

            goto try_except_handler_70;
        }
        assert(tmp_with_18__source == NULL);
        tmp_with_18__source = tmp_assign_source_163;
    }
    {
        PyObject *tmp_assign_source_164;
        PyObject *tmp_called_value_150;
        PyObject *tmp_expression_value_99;
        CHECK_OBJECT(tmp_with_18__source);
        tmp_expression_value_99 = tmp_with_18__source;
        tmp_called_value_150 = LOOKUP_SPECIAL(tmp_expression_value_99, mod_consts[67]);
        if (tmp_called_value_150 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 676;

            goto try_except_handler_70;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 676;
        tmp_assign_source_164 = CALL_FUNCTION_NO_ARGS(tmp_called_value_150);
        Py_DECREF(tmp_called_value_150);
        if (tmp_assign_source_164 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 676;

            goto try_except_handler_70;
        }
        assert(tmp_with_18__enter == NULL);
        tmp_with_18__enter = tmp_assign_source_164;
    }
    {
        PyObject *tmp_assign_source_165;
        PyObject *tmp_expression_value_100;
        CHECK_OBJECT(tmp_with_18__source);
        tmp_expression_value_100 = tmp_with_18__source;
        tmp_assign_source_165 = LOOKUP_SPECIAL(tmp_expression_value_100, mod_consts[68]);
        if (tmp_assign_source_165 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 676;

            goto try_except_handler_70;
        }
        assert(tmp_with_18__exit == NULL);
        tmp_with_18__exit = tmp_assign_source_165;
    }
    {
        nuitka_bool tmp_assign_source_166;
        tmp_assign_source_166 = NUITKA_BOOL_TRUE;
        tmp_with_18__indicator = tmp_assign_source_166;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_151;
        PyObject *tmp_expression_value_101;
        PyObject *tmp_call_result_89;
        PyObject *tmp_kw_call_arg_value_0_43;
        PyObject *tmp_kw_call_arg_value_1_43;
        PyObject *tmp_kw_call_arg_value_2_43;
        PyObject *tmp_kw_call_dict_value_0_43;
        PyObject *tmp_called_value_152;
        PyObject *tmp_call_arg_element_11;
        tmp_expression_value_101 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_101 == NULL)) {
            tmp_expression_value_101 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_101 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 677;

            goto try_except_handler_72;
        }
        tmp_called_value_151 = LOOKUP_ATTRIBUTE(tmp_expression_value_101, mod_consts[69]);
        if (tmp_called_value_151 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 677;

            goto try_except_handler_72;
        }
        tmp_kw_call_arg_value_0_43 = mod_consts[267];
        tmp_kw_call_arg_value_1_43 = mod_consts[241];
        tmp_kw_call_arg_value_2_43 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[270]);

        if (unlikely(tmp_kw_call_arg_value_2_43 == NULL)) {
            tmp_kw_call_arg_value_2_43 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[270]);
        }

        if (tmp_kw_call_arg_value_2_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_151);

            exception_lineno = 680;

            goto try_except_handler_72;
        }
        tmp_called_value_152 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_152 == NULL)) {
            tmp_called_value_152 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_152 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_151);

            exception_lineno = 681;

            goto try_except_handler_72;
        }
        tmp_call_arg_element_11 = LIST_COPY(mod_consts[272]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 681;
        tmp_kw_call_dict_value_0_43 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_152, tmp_call_arg_element_11);
        Py_DECREF(tmp_call_arg_element_11);
        if (tmp_kw_call_dict_value_0_43 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_151);

            exception_lineno = 681;

            goto try_except_handler_72;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 677;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_43, tmp_kw_call_arg_value_1_43, tmp_kw_call_arg_value_2_43};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_43};
            tmp_call_result_89 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_151, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_151);
        Py_DECREF(tmp_kw_call_dict_value_0_43);
        if (tmp_call_result_89 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 677;

            goto try_except_handler_72;
        }
        Py_DECREF(tmp_call_result_89);
    }
    goto try_end_70;
    // Exception handler code:
    try_except_handler_72:;
    exception_keeper_type_70 = exception_type;
    exception_keeper_value_70 = exception_value;
    exception_keeper_tb_70 = exception_tb;
    exception_keeper_lineno_70 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 18.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_18, &exception_preserved_value_18, &exception_preserved_tb_18);

    if (exception_keeper_tb_70 == NULL) {
        exception_keeper_tb_70 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_70);
    } else if (exception_keeper_lineno_70 != 0) {
        exception_keeper_tb_70 = ADD_TRACEBACK(exception_keeper_tb_70, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_70);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_70, &exception_keeper_value_70, &exception_keeper_tb_70);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_70, exception_keeper_tb_70);
    PUBLISH_EXCEPTION(&exception_keeper_type_70, &exception_keeper_value_70, &exception_keeper_tb_70);
    // Tried code:
    {
        bool tmp_condition_result_70;
        PyObject *tmp_cmp_expr_left_52;
        PyObject *tmp_cmp_expr_right_52;
        tmp_cmp_expr_left_52 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_52 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_52, tmp_cmp_expr_right_52);
        assert(!(tmp_res == -1));
        tmp_condition_result_70 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_70 != false) {
            goto branch_yes_70;
        } else {
            goto branch_no_70;
        }
    }
    branch_yes_70:;
    {
        nuitka_bool tmp_assign_source_167;
        tmp_assign_source_167 = NUITKA_BOOL_FALSE;
        tmp_with_18__indicator = tmp_assign_source_167;
    }
    {
        bool tmp_condition_result_71;
        PyObject *tmp_operand_value_18;
        PyObject *tmp_called_value_153;
        PyObject *tmp_args_element_value_70;
        PyObject *tmp_args_element_value_71;
        PyObject *tmp_args_element_value_72;
        CHECK_OBJECT(tmp_with_18__exit);
        tmp_called_value_153 = tmp_with_18__exit;
        tmp_args_element_value_70 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_71 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_72 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 681;
        {
            PyObject *call_args[] = {tmp_args_element_value_70, tmp_args_element_value_71, tmp_args_element_value_72};
            tmp_operand_value_18 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_153, call_args);
        }

        if (tmp_operand_value_18 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 681;

            goto try_except_handler_73;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_18);
        Py_DECREF(tmp_operand_value_18);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 681;

            goto try_except_handler_73;
        }
        tmp_condition_result_71 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_71 != false) {
            goto branch_yes_71;
        } else {
            goto branch_no_71;
        }
    }
    branch_yes_71:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 681;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_73;
    branch_no_71:;
    goto branch_end_70;
    branch_no_70:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 676;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_73;
    branch_end_70:;
    goto try_end_71;
    // Exception handler code:
    try_except_handler_73:;
    exception_keeper_type_71 = exception_type;
    exception_keeper_value_71 = exception_value;
    exception_keeper_tb_71 = exception_tb;
    exception_keeper_lineno_71 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 18.
    SET_CURRENT_EXCEPTION(exception_preserved_type_18, exception_preserved_value_18, exception_preserved_tb_18);

    // Re-raise.
    exception_type = exception_keeper_type_71;
    exception_value = exception_keeper_value_71;
    exception_tb = exception_keeper_tb_71;
    exception_lineno = exception_keeper_lineno_71;

    goto try_except_handler_71;
    // End of try:
    try_end_71:;
    // Restore previous exception id 18.
    SET_CURRENT_EXCEPTION(exception_preserved_type_18, exception_preserved_value_18, exception_preserved_tb_18);

    goto try_end_70;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_70:;
    goto try_end_72;
    // Exception handler code:
    try_except_handler_71:;
    exception_keeper_type_72 = exception_type;
    exception_keeper_value_72 = exception_value;
    exception_keeper_tb_72 = exception_tb;
    exception_keeper_lineno_72 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_72;
        nuitka_bool tmp_cmp_expr_left_53;
        nuitka_bool tmp_cmp_expr_right_53;
        assert(tmp_with_18__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_53 = tmp_with_18__indicator;
        tmp_cmp_expr_right_53 = NUITKA_BOOL_TRUE;
        tmp_condition_result_72 = (tmp_cmp_expr_left_53 == tmp_cmp_expr_right_53) ? true : false;
        if (tmp_condition_result_72 != false) {
            goto branch_yes_72;
        } else {
            goto branch_no_72;
        }
    }
    branch_yes_72:;
    {
        PyObject *tmp_called_value_154;
        PyObject *tmp_call_result_90;
        CHECK_OBJECT(tmp_with_18__exit);
        tmp_called_value_154 = tmp_with_18__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 681;
        tmp_call_result_90 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_154, mod_consts[74]);

        if (tmp_call_result_90 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_72);
            Py_XDECREF(exception_keeper_value_72);
            Py_XDECREF(exception_keeper_tb_72);

            exception_lineno = 681;

            goto try_except_handler_70;
        }
        Py_DECREF(tmp_call_result_90);
    }
    branch_no_72:;
    // Re-raise.
    exception_type = exception_keeper_type_72;
    exception_value = exception_keeper_value_72;
    exception_tb = exception_keeper_tb_72;
    exception_lineno = exception_keeper_lineno_72;

    goto try_except_handler_70;
    // End of try:
    try_end_72:;
    {
        bool tmp_condition_result_73;
        nuitka_bool tmp_cmp_expr_left_54;
        nuitka_bool tmp_cmp_expr_right_54;
        assert(tmp_with_18__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_54 = tmp_with_18__indicator;
        tmp_cmp_expr_right_54 = NUITKA_BOOL_TRUE;
        tmp_condition_result_73 = (tmp_cmp_expr_left_54 == tmp_cmp_expr_right_54) ? true : false;
        if (tmp_condition_result_73 != false) {
            goto branch_yes_73;
        } else {
            goto branch_no_73;
        }
    }
    branch_yes_73:;
    {
        PyObject *tmp_called_value_155;
        PyObject *tmp_call_result_91;
        CHECK_OBJECT(tmp_with_18__exit);
        tmp_called_value_155 = tmp_with_18__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 681;
        tmp_call_result_91 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_155, mod_consts[74]);

        if (tmp_call_result_91 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 681;

            goto try_except_handler_70;
        }
        Py_DECREF(tmp_call_result_91);
    }
    branch_no_73:;
    goto try_end_73;
    // Exception handler code:
    try_except_handler_70:;
    exception_keeper_type_73 = exception_type;
    exception_keeper_value_73 = exception_value;
    exception_keeper_tb_73 = exception_tb;
    exception_keeper_lineno_73 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_18__source);
    tmp_with_18__source = NULL;
    Py_XDECREF(tmp_with_18__enter);
    tmp_with_18__enter = NULL;
    Py_XDECREF(tmp_with_18__exit);
    tmp_with_18__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_73;
    exception_value = exception_keeper_value_73;
    exception_tb = exception_keeper_tb_73;
    exception_lineno = exception_keeper_lineno_73;

    goto frame_exception_exit_1;
    // End of try:
    try_end_73:;
    CHECK_OBJECT(tmp_with_18__source);
    Py_DECREF(tmp_with_18__source);
    tmp_with_18__source = NULL;
    CHECK_OBJECT(tmp_with_18__enter);
    Py_DECREF(tmp_with_18__enter);
    tmp_with_18__enter = NULL;
    Py_XDECREF(tmp_with_18__exit);
    tmp_with_18__exit = NULL;
    {
        PyObject *tmp_assign_source_168;
        tmp_assign_source_168 = mod_consts[273];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[274], tmp_assign_source_168);
    }
    {
        PyObject *tmp_assign_source_169;


        tmp_assign_source_169 = MAKE_FUNCTION_pandas$core$config_init$$$function__8_register_plotting_backend_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[275], tmp_assign_source_169);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_170;
        PyObject *tmp_called_instance_19;
        tmp_called_instance_19 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_19 == NULL)) {
            tmp_called_instance_19 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 705;

            goto try_except_handler_74;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 705;
        tmp_assign_source_170 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_19,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[276], 0)
        );

        if (tmp_assign_source_170 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 705;

            goto try_except_handler_74;
        }
        assert(tmp_with_19__source == NULL);
        tmp_with_19__source = tmp_assign_source_170;
    }
    {
        PyObject *tmp_assign_source_171;
        PyObject *tmp_called_value_156;
        PyObject *tmp_expression_value_102;
        CHECK_OBJECT(tmp_with_19__source);
        tmp_expression_value_102 = tmp_with_19__source;
        tmp_called_value_156 = LOOKUP_SPECIAL(tmp_expression_value_102, mod_consts[67]);
        if (tmp_called_value_156 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 705;

            goto try_except_handler_74;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 705;
        tmp_assign_source_171 = CALL_FUNCTION_NO_ARGS(tmp_called_value_156);
        Py_DECREF(tmp_called_value_156);
        if (tmp_assign_source_171 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 705;

            goto try_except_handler_74;
        }
        assert(tmp_with_19__enter == NULL);
        tmp_with_19__enter = tmp_assign_source_171;
    }
    {
        PyObject *tmp_assign_source_172;
        PyObject *tmp_expression_value_103;
        CHECK_OBJECT(tmp_with_19__source);
        tmp_expression_value_103 = tmp_with_19__source;
        tmp_assign_source_172 = LOOKUP_SPECIAL(tmp_expression_value_103, mod_consts[68]);
        if (tmp_assign_source_172 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 705;

            goto try_except_handler_74;
        }
        assert(tmp_with_19__exit == NULL);
        tmp_with_19__exit = tmp_assign_source_172;
    }
    {
        nuitka_bool tmp_assign_source_173;
        tmp_assign_source_173 = NUITKA_BOOL_TRUE;
        tmp_with_19__indicator = tmp_assign_source_173;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_157;
        PyObject *tmp_expression_value_104;
        PyObject *tmp_call_result_92;
        PyObject *tmp_kw_call_value_0_12;
        PyObject *tmp_kw_call_value_1_11;
        PyObject *tmp_kw_call_value_2_1;
        tmp_expression_value_104 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_104 == NULL)) {
            tmp_expression_value_104 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_104 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 706;

            goto try_except_handler_76;
        }
        tmp_called_value_157 = LOOKUP_ATTRIBUTE(tmp_expression_value_104, mod_consts[69]);
        if (tmp_called_value_157 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 706;

            goto try_except_handler_76;
        }
        tmp_kw_call_value_0_12 = mod_consts[29];
        tmp_kw_call_value_1_11 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[274]);

        if (unlikely(tmp_kw_call_value_1_11 == NULL)) {
            tmp_kw_call_value_1_11 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[274]);
        }

        if (tmp_kw_call_value_1_11 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_157);

            exception_lineno = 709;

            goto try_except_handler_76;
        }
        tmp_kw_call_value_2_1 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[275]);

        if (unlikely(tmp_kw_call_value_2_1 == NULL)) {
            tmp_kw_call_value_2_1 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[275]);
        }

        if (tmp_kw_call_value_2_1 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_157);

            exception_lineno = 710;

            goto try_except_handler_76;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 706;
        {
            PyObject *kw_values[3] = {tmp_kw_call_value_0_12, tmp_kw_call_value_1_11, tmp_kw_call_value_2_1};
            tmp_call_result_92 = CALL_FUNCTION_WITH_POSARGS1_KWSPLIT(tmp_called_value_157, mod_consts[277], kw_values, mod_consts[278]);
        }

        Py_DECREF(tmp_called_value_157);
        if (tmp_call_result_92 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 706;

            goto try_except_handler_76;
        }
        Py_DECREF(tmp_call_result_92);
    }
    goto try_end_74;
    // Exception handler code:
    try_except_handler_76:;
    exception_keeper_type_74 = exception_type;
    exception_keeper_value_74 = exception_value;
    exception_keeper_tb_74 = exception_tb;
    exception_keeper_lineno_74 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 19.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_19, &exception_preserved_value_19, &exception_preserved_tb_19);

    if (exception_keeper_tb_74 == NULL) {
        exception_keeper_tb_74 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_74);
    } else if (exception_keeper_lineno_74 != 0) {
        exception_keeper_tb_74 = ADD_TRACEBACK(exception_keeper_tb_74, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_74);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_74, &exception_keeper_value_74, &exception_keeper_tb_74);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_74, exception_keeper_tb_74);
    PUBLISH_EXCEPTION(&exception_keeper_type_74, &exception_keeper_value_74, &exception_keeper_tb_74);
    // Tried code:
    {
        bool tmp_condition_result_74;
        PyObject *tmp_cmp_expr_left_55;
        PyObject *tmp_cmp_expr_right_55;
        tmp_cmp_expr_left_55 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_55 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_55, tmp_cmp_expr_right_55);
        assert(!(tmp_res == -1));
        tmp_condition_result_74 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_74 != false) {
            goto branch_yes_74;
        } else {
            goto branch_no_74;
        }
    }
    branch_yes_74:;
    {
        nuitka_bool tmp_assign_source_174;
        tmp_assign_source_174 = NUITKA_BOOL_FALSE;
        tmp_with_19__indicator = tmp_assign_source_174;
    }
    {
        bool tmp_condition_result_75;
        PyObject *tmp_operand_value_19;
        PyObject *tmp_called_value_158;
        PyObject *tmp_args_element_value_73;
        PyObject *tmp_args_element_value_74;
        PyObject *tmp_args_element_value_75;
        CHECK_OBJECT(tmp_with_19__exit);
        tmp_called_value_158 = tmp_with_19__exit;
        tmp_args_element_value_73 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_74 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_75 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 710;
        {
            PyObject *call_args[] = {tmp_args_element_value_73, tmp_args_element_value_74, tmp_args_element_value_75};
            tmp_operand_value_19 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_158, call_args);
        }

        if (tmp_operand_value_19 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 710;

            goto try_except_handler_77;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_19);
        Py_DECREF(tmp_operand_value_19);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 710;

            goto try_except_handler_77;
        }
        tmp_condition_result_75 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_75 != false) {
            goto branch_yes_75;
        } else {
            goto branch_no_75;
        }
    }
    branch_yes_75:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 710;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_77;
    branch_no_75:;
    goto branch_end_74;
    branch_no_74:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 705;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_77;
    branch_end_74:;
    goto try_end_75;
    // Exception handler code:
    try_except_handler_77:;
    exception_keeper_type_75 = exception_type;
    exception_keeper_value_75 = exception_value;
    exception_keeper_tb_75 = exception_tb;
    exception_keeper_lineno_75 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 19.
    SET_CURRENT_EXCEPTION(exception_preserved_type_19, exception_preserved_value_19, exception_preserved_tb_19);

    // Re-raise.
    exception_type = exception_keeper_type_75;
    exception_value = exception_keeper_value_75;
    exception_tb = exception_keeper_tb_75;
    exception_lineno = exception_keeper_lineno_75;

    goto try_except_handler_75;
    // End of try:
    try_end_75:;
    // Restore previous exception id 19.
    SET_CURRENT_EXCEPTION(exception_preserved_type_19, exception_preserved_value_19, exception_preserved_tb_19);

    goto try_end_74;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_74:;
    goto try_end_76;
    // Exception handler code:
    try_except_handler_75:;
    exception_keeper_type_76 = exception_type;
    exception_keeper_value_76 = exception_value;
    exception_keeper_tb_76 = exception_tb;
    exception_keeper_lineno_76 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_76;
        nuitka_bool tmp_cmp_expr_left_56;
        nuitka_bool tmp_cmp_expr_right_56;
        assert(tmp_with_19__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_56 = tmp_with_19__indicator;
        tmp_cmp_expr_right_56 = NUITKA_BOOL_TRUE;
        tmp_condition_result_76 = (tmp_cmp_expr_left_56 == tmp_cmp_expr_right_56) ? true : false;
        if (tmp_condition_result_76 != false) {
            goto branch_yes_76;
        } else {
            goto branch_no_76;
        }
    }
    branch_yes_76:;
    {
        PyObject *tmp_called_value_159;
        PyObject *tmp_call_result_93;
        CHECK_OBJECT(tmp_with_19__exit);
        tmp_called_value_159 = tmp_with_19__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 710;
        tmp_call_result_93 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_159, mod_consts[74]);

        if (tmp_call_result_93 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_76);
            Py_XDECREF(exception_keeper_value_76);
            Py_XDECREF(exception_keeper_tb_76);

            exception_lineno = 710;

            goto try_except_handler_74;
        }
        Py_DECREF(tmp_call_result_93);
    }
    branch_no_76:;
    // Re-raise.
    exception_type = exception_keeper_type_76;
    exception_value = exception_keeper_value_76;
    exception_tb = exception_keeper_tb_76;
    exception_lineno = exception_keeper_lineno_76;

    goto try_except_handler_74;
    // End of try:
    try_end_76:;
    {
        bool tmp_condition_result_77;
        nuitka_bool tmp_cmp_expr_left_57;
        nuitka_bool tmp_cmp_expr_right_57;
        assert(tmp_with_19__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_57 = tmp_with_19__indicator;
        tmp_cmp_expr_right_57 = NUITKA_BOOL_TRUE;
        tmp_condition_result_77 = (tmp_cmp_expr_left_57 == tmp_cmp_expr_right_57) ? true : false;
        if (tmp_condition_result_77 != false) {
            goto branch_yes_77;
        } else {
            goto branch_no_77;
        }
    }
    branch_yes_77:;
    {
        PyObject *tmp_called_value_160;
        PyObject *tmp_call_result_94;
        CHECK_OBJECT(tmp_with_19__exit);
        tmp_called_value_160 = tmp_with_19__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 710;
        tmp_call_result_94 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_160, mod_consts[74]);

        if (tmp_call_result_94 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 710;

            goto try_except_handler_74;
        }
        Py_DECREF(tmp_call_result_94);
    }
    branch_no_77:;
    goto try_end_77;
    // Exception handler code:
    try_except_handler_74:;
    exception_keeper_type_77 = exception_type;
    exception_keeper_value_77 = exception_value;
    exception_keeper_tb_77 = exception_tb;
    exception_keeper_lineno_77 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_19__source);
    tmp_with_19__source = NULL;
    Py_XDECREF(tmp_with_19__enter);
    tmp_with_19__enter = NULL;
    Py_XDECREF(tmp_with_19__exit);
    tmp_with_19__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_77;
    exception_value = exception_keeper_value_77;
    exception_tb = exception_keeper_tb_77;
    exception_lineno = exception_keeper_lineno_77;

    goto frame_exception_exit_1;
    // End of try:
    try_end_77:;
    CHECK_OBJECT(tmp_with_19__source);
    Py_DECREF(tmp_with_19__source);
    tmp_with_19__source = NULL;
    CHECK_OBJECT(tmp_with_19__enter);
    Py_DECREF(tmp_with_19__enter);
    tmp_with_19__enter = NULL;
    Py_XDECREF(tmp_with_19__exit);
    tmp_with_19__exit = NULL;
    {
        PyObject *tmp_assign_source_175;
        tmp_assign_source_175 = mod_consts[279];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[280], tmp_assign_source_175);
    }
    {
        PyObject *tmp_assign_source_176;


        tmp_assign_source_176 = MAKE_FUNCTION_pandas$core$config_init$$$function__9_register_converter_cb();

        UPDATE_STRING_DICT1(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[281], tmp_assign_source_176);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_177;
        PyObject *tmp_called_instance_20;
        tmp_called_instance_20 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_20 == NULL)) {
            tmp_called_instance_20 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 734;

            goto try_except_handler_78;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 734;
        tmp_assign_source_177 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_20,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[282], 0)
        );

        if (tmp_assign_source_177 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 734;

            goto try_except_handler_78;
        }
        assert(tmp_with_20__source == NULL);
        tmp_with_20__source = tmp_assign_source_177;
    }
    {
        PyObject *tmp_assign_source_178;
        PyObject *tmp_called_value_161;
        PyObject *tmp_expression_value_105;
        CHECK_OBJECT(tmp_with_20__source);
        tmp_expression_value_105 = tmp_with_20__source;
        tmp_called_value_161 = LOOKUP_SPECIAL(tmp_expression_value_105, mod_consts[67]);
        if (tmp_called_value_161 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 734;

            goto try_except_handler_78;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 734;
        tmp_assign_source_178 = CALL_FUNCTION_NO_ARGS(tmp_called_value_161);
        Py_DECREF(tmp_called_value_161);
        if (tmp_assign_source_178 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 734;

            goto try_except_handler_78;
        }
        assert(tmp_with_20__enter == NULL);
        tmp_with_20__enter = tmp_assign_source_178;
    }
    {
        PyObject *tmp_assign_source_179;
        PyObject *tmp_expression_value_106;
        CHECK_OBJECT(tmp_with_20__source);
        tmp_expression_value_106 = tmp_with_20__source;
        tmp_assign_source_179 = LOOKUP_SPECIAL(tmp_expression_value_106, mod_consts[68]);
        if (tmp_assign_source_179 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 734;

            goto try_except_handler_78;
        }
        assert(tmp_with_20__exit == NULL);
        tmp_with_20__exit = tmp_assign_source_179;
    }
    {
        nuitka_bool tmp_assign_source_180;
        tmp_assign_source_180 = NUITKA_BOOL_TRUE;
        tmp_with_20__indicator = tmp_assign_source_180;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_162;
        PyObject *tmp_expression_value_107;
        PyObject *tmp_call_result_95;
        PyObject *tmp_kw_call_arg_value_0_44;
        PyObject *tmp_kw_call_arg_value_1_44;
        PyObject *tmp_kw_call_arg_value_2_44;
        PyObject *tmp_kw_call_dict_value_0_44;
        PyObject *tmp_called_value_163;
        PyObject *tmp_call_arg_element_12;
        PyObject *tmp_kw_call_dict_value_1_6;
        tmp_expression_value_107 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_107 == NULL)) {
            tmp_expression_value_107 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_107 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 735;

            goto try_except_handler_80;
        }
        tmp_called_value_162 = LOOKUP_ATTRIBUTE(tmp_expression_value_107, mod_consts[69]);
        if (tmp_called_value_162 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 735;

            goto try_except_handler_80;
        }
        tmp_kw_call_arg_value_0_44 = mod_consts[283];
        tmp_kw_call_arg_value_1_44 = mod_consts[241];
        tmp_kw_call_arg_value_2_44 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[280]);

        if (unlikely(tmp_kw_call_arg_value_2_44 == NULL)) {
            tmp_kw_call_arg_value_2_44 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[280]);
        }

        if (tmp_kw_call_arg_value_2_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_162);

            exception_lineno = 738;

            goto try_except_handler_80;
        }
        tmp_called_value_163 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[54]);

        if (unlikely(tmp_called_value_163 == NULL)) {
            tmp_called_value_163 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[54]);
        }

        if (tmp_called_value_163 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_162);

            exception_lineno = 739;

            goto try_except_handler_80;
        }
        tmp_call_arg_element_12 = LIST_COPY(mod_consts[284]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 739;
        tmp_kw_call_dict_value_0_44 = CALL_FUNCTION_WITH_SINGLE_ARG(tmp_called_value_163, tmp_call_arg_element_12);
        Py_DECREF(tmp_call_arg_element_12);
        if (tmp_kw_call_dict_value_0_44 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_162);

            exception_lineno = 739;

            goto try_except_handler_80;
        }
        tmp_kw_call_dict_value_1_6 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[281]);

        if (unlikely(tmp_kw_call_dict_value_1_6 == NULL)) {
            tmp_kw_call_dict_value_1_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[281]);
        }

        if (tmp_kw_call_dict_value_1_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_162);
            Py_DECREF(tmp_kw_call_dict_value_0_44);

            exception_lineno = 740;

            goto try_except_handler_80;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 735;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_44, tmp_kw_call_arg_value_1_44, tmp_kw_call_arg_value_2_44};
            PyObject *kw_values[2] = {tmp_kw_call_dict_value_0_44, tmp_kw_call_dict_value_1_6};
            tmp_call_result_95 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_162, args, kw_values, mod_consts[71]);
        }

        Py_DECREF(tmp_called_value_162);
        Py_DECREF(tmp_kw_call_dict_value_0_44);
        if (tmp_call_result_95 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 735;

            goto try_except_handler_80;
        }
        Py_DECREF(tmp_call_result_95);
    }
    goto try_end_78;
    // Exception handler code:
    try_except_handler_80:;
    exception_keeper_type_78 = exception_type;
    exception_keeper_value_78 = exception_value;
    exception_keeper_tb_78 = exception_tb;
    exception_keeper_lineno_78 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 20.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_20, &exception_preserved_value_20, &exception_preserved_tb_20);

    if (exception_keeper_tb_78 == NULL) {
        exception_keeper_tb_78 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_78);
    } else if (exception_keeper_lineno_78 != 0) {
        exception_keeper_tb_78 = ADD_TRACEBACK(exception_keeper_tb_78, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_78);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_78, &exception_keeper_value_78, &exception_keeper_tb_78);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_78, exception_keeper_tb_78);
    PUBLISH_EXCEPTION(&exception_keeper_type_78, &exception_keeper_value_78, &exception_keeper_tb_78);
    // Tried code:
    {
        bool tmp_condition_result_78;
        PyObject *tmp_cmp_expr_left_58;
        PyObject *tmp_cmp_expr_right_58;
        tmp_cmp_expr_left_58 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_58 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_58, tmp_cmp_expr_right_58);
        assert(!(tmp_res == -1));
        tmp_condition_result_78 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_78 != false) {
            goto branch_yes_78;
        } else {
            goto branch_no_78;
        }
    }
    branch_yes_78:;
    {
        nuitka_bool tmp_assign_source_181;
        tmp_assign_source_181 = NUITKA_BOOL_FALSE;
        tmp_with_20__indicator = tmp_assign_source_181;
    }
    {
        bool tmp_condition_result_79;
        PyObject *tmp_operand_value_20;
        PyObject *tmp_called_value_164;
        PyObject *tmp_args_element_value_76;
        PyObject *tmp_args_element_value_77;
        PyObject *tmp_args_element_value_78;
        CHECK_OBJECT(tmp_with_20__exit);
        tmp_called_value_164 = tmp_with_20__exit;
        tmp_args_element_value_76 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_77 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_78 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 740;
        {
            PyObject *call_args[] = {tmp_args_element_value_76, tmp_args_element_value_77, tmp_args_element_value_78};
            tmp_operand_value_20 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_164, call_args);
        }

        if (tmp_operand_value_20 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 740;

            goto try_except_handler_81;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_20);
        Py_DECREF(tmp_operand_value_20);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 740;

            goto try_except_handler_81;
        }
        tmp_condition_result_79 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_79 != false) {
            goto branch_yes_79;
        } else {
            goto branch_no_79;
        }
    }
    branch_yes_79:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 740;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_81;
    branch_no_79:;
    goto branch_end_78;
    branch_no_78:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 734;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_81;
    branch_end_78:;
    goto try_end_79;
    // Exception handler code:
    try_except_handler_81:;
    exception_keeper_type_79 = exception_type;
    exception_keeper_value_79 = exception_value;
    exception_keeper_tb_79 = exception_tb;
    exception_keeper_lineno_79 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 20.
    SET_CURRENT_EXCEPTION(exception_preserved_type_20, exception_preserved_value_20, exception_preserved_tb_20);

    // Re-raise.
    exception_type = exception_keeper_type_79;
    exception_value = exception_keeper_value_79;
    exception_tb = exception_keeper_tb_79;
    exception_lineno = exception_keeper_lineno_79;

    goto try_except_handler_79;
    // End of try:
    try_end_79:;
    // Restore previous exception id 20.
    SET_CURRENT_EXCEPTION(exception_preserved_type_20, exception_preserved_value_20, exception_preserved_tb_20);

    goto try_end_78;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_78:;
    goto try_end_80;
    // Exception handler code:
    try_except_handler_79:;
    exception_keeper_type_80 = exception_type;
    exception_keeper_value_80 = exception_value;
    exception_keeper_tb_80 = exception_tb;
    exception_keeper_lineno_80 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_80;
        nuitka_bool tmp_cmp_expr_left_59;
        nuitka_bool tmp_cmp_expr_right_59;
        assert(tmp_with_20__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_59 = tmp_with_20__indicator;
        tmp_cmp_expr_right_59 = NUITKA_BOOL_TRUE;
        tmp_condition_result_80 = (tmp_cmp_expr_left_59 == tmp_cmp_expr_right_59) ? true : false;
        if (tmp_condition_result_80 != false) {
            goto branch_yes_80;
        } else {
            goto branch_no_80;
        }
    }
    branch_yes_80:;
    {
        PyObject *tmp_called_value_165;
        PyObject *tmp_call_result_96;
        CHECK_OBJECT(tmp_with_20__exit);
        tmp_called_value_165 = tmp_with_20__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 740;
        tmp_call_result_96 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_165, mod_consts[74]);

        if (tmp_call_result_96 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_80);
            Py_XDECREF(exception_keeper_value_80);
            Py_XDECREF(exception_keeper_tb_80);

            exception_lineno = 740;

            goto try_except_handler_78;
        }
        Py_DECREF(tmp_call_result_96);
    }
    branch_no_80:;
    // Re-raise.
    exception_type = exception_keeper_type_80;
    exception_value = exception_keeper_value_80;
    exception_tb = exception_keeper_tb_80;
    exception_lineno = exception_keeper_lineno_80;

    goto try_except_handler_78;
    // End of try:
    try_end_80:;
    {
        bool tmp_condition_result_81;
        nuitka_bool tmp_cmp_expr_left_60;
        nuitka_bool tmp_cmp_expr_right_60;
        assert(tmp_with_20__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_60 = tmp_with_20__indicator;
        tmp_cmp_expr_right_60 = NUITKA_BOOL_TRUE;
        tmp_condition_result_81 = (tmp_cmp_expr_left_60 == tmp_cmp_expr_right_60) ? true : false;
        if (tmp_condition_result_81 != false) {
            goto branch_yes_81;
        } else {
            goto branch_no_81;
        }
    }
    branch_yes_81:;
    {
        PyObject *tmp_called_value_166;
        PyObject *tmp_call_result_97;
        CHECK_OBJECT(tmp_with_20__exit);
        tmp_called_value_166 = tmp_with_20__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 740;
        tmp_call_result_97 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_166, mod_consts[74]);

        if (tmp_call_result_97 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 740;

            goto try_except_handler_78;
        }
        Py_DECREF(tmp_call_result_97);
    }
    branch_no_81:;
    goto try_end_81;
    // Exception handler code:
    try_except_handler_78:;
    exception_keeper_type_81 = exception_type;
    exception_keeper_value_81 = exception_value;
    exception_keeper_tb_81 = exception_tb;
    exception_keeper_lineno_81 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_20__source);
    tmp_with_20__source = NULL;
    Py_XDECREF(tmp_with_20__enter);
    tmp_with_20__enter = NULL;
    Py_XDECREF(tmp_with_20__exit);
    tmp_with_20__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_81;
    exception_value = exception_keeper_value_81;
    exception_tb = exception_keeper_tb_81;
    exception_lineno = exception_keeper_lineno_81;

    goto frame_exception_exit_1;
    // End of try:
    try_end_81:;
    CHECK_OBJECT(tmp_with_20__source);
    Py_DECREF(tmp_with_20__source);
    tmp_with_20__source = NULL;
    CHECK_OBJECT(tmp_with_20__enter);
    Py_DECREF(tmp_with_20__enter);
    tmp_with_20__enter = NULL;
    Py_XDECREF(tmp_with_20__exit);
    tmp_with_20__exit = NULL;
    {
        PyObject *tmp_assign_source_182;
        tmp_assign_source_182 = mod_consts[285];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[286], tmp_assign_source_182);
    }
    {
        PyObject *tmp_assign_source_183;
        tmp_assign_source_183 = mod_consts[287];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[288], tmp_assign_source_183);
    }
    {
        PyObject *tmp_assign_source_184;
        tmp_assign_source_184 = mod_consts[289];
        UPDATE_STRING_DICT0(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[290], tmp_assign_source_184);
    }
    // Tried code:
    {
        PyObject *tmp_assign_source_185;
        PyObject *tmp_called_instance_21;
        tmp_called_instance_21 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_called_instance_21 == NULL)) {
            tmp_called_instance_21 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_called_instance_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 765;

            goto try_except_handler_82;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 765;
        tmp_assign_source_185 = CALL_METHOD_WITH_SINGLE_ARG(
            tmp_called_instance_21,
            mod_consts[65],
            PyTuple_GET_ITEM(mod_consts[291], 0)
        );

        if (tmp_assign_source_185 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 765;

            goto try_except_handler_82;
        }
        assert(tmp_with_21__source == NULL);
        tmp_with_21__source = tmp_assign_source_185;
    }
    {
        PyObject *tmp_assign_source_186;
        PyObject *tmp_called_value_167;
        PyObject *tmp_expression_value_108;
        CHECK_OBJECT(tmp_with_21__source);
        tmp_expression_value_108 = tmp_with_21__source;
        tmp_called_value_167 = LOOKUP_SPECIAL(tmp_expression_value_108, mod_consts[67]);
        if (tmp_called_value_167 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 765;

            goto try_except_handler_82;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 765;
        tmp_assign_source_186 = CALL_FUNCTION_NO_ARGS(tmp_called_value_167);
        Py_DECREF(tmp_called_value_167);
        if (tmp_assign_source_186 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 765;

            goto try_except_handler_82;
        }
        assert(tmp_with_21__enter == NULL);
        tmp_with_21__enter = tmp_assign_source_186;
    }
    {
        PyObject *tmp_assign_source_187;
        PyObject *tmp_expression_value_109;
        CHECK_OBJECT(tmp_with_21__source);
        tmp_expression_value_109 = tmp_with_21__source;
        tmp_assign_source_187 = LOOKUP_SPECIAL(tmp_expression_value_109, mod_consts[68]);
        if (tmp_assign_source_187 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 765;

            goto try_except_handler_82;
        }
        assert(tmp_with_21__exit == NULL);
        tmp_with_21__exit = tmp_assign_source_187;
    }
    {
        nuitka_bool tmp_assign_source_188;
        tmp_assign_source_188 = NUITKA_BOOL_TRUE;
        tmp_with_21__indicator = tmp_assign_source_188;
    }
    // Tried code:
    // Tried code:
    {
        PyObject *tmp_called_value_168;
        PyObject *tmp_expression_value_110;
        PyObject *tmp_call_result_98;
        PyObject *tmp_args_value_5;
        PyObject *tmp_tuple_element_5;
        PyObject *tmp_kwargs_value_5;
        tmp_expression_value_110 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_110 == NULL)) {
            tmp_expression_value_110 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_110 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 766;

            goto try_except_handler_84;
        }
        tmp_called_value_168 = LOOKUP_ATTRIBUTE(tmp_expression_value_110, mod_consts[69]);
        if (tmp_called_value_168 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 766;

            goto try_except_handler_84;
        }
        tmp_tuple_element_5 = mod_consts[292];
        tmp_args_value_5 = PyTuple_New(3);
        PyTuple_SET_ITEM0(tmp_args_value_5, 0, tmp_tuple_element_5);
        tmp_tuple_element_5 = Py_True;
        PyTuple_SET_ITEM0(tmp_args_value_5, 1, tmp_tuple_element_5);
        tmp_tuple_element_5 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[286]);

        if (unlikely(tmp_tuple_element_5 == NULL)) {
            tmp_tuple_element_5 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[286]);
        }

        if (tmp_tuple_element_5 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 766;

            goto tuple_build_exception_5;
        }
        PyTuple_SET_ITEM0(tmp_args_value_5, 2, tmp_tuple_element_5);
        goto tuple_build_noexception_5;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_5:;
        Py_DECREF(tmp_called_value_168);
        Py_DECREF(tmp_args_value_5);
        goto try_except_handler_84;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_5:;
        tmp_kwargs_value_5 = PyDict_Copy(mod_consts[293]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 766;
        tmp_call_result_98 = CALL_FUNCTION(tmp_called_value_168, tmp_args_value_5, tmp_kwargs_value_5);
        Py_DECREF(tmp_called_value_168);
        Py_DECREF(tmp_args_value_5);
        Py_DECREF(tmp_kwargs_value_5);
        if (tmp_call_result_98 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 766;

            goto try_except_handler_84;
        }
        Py_DECREF(tmp_call_result_98);
    }
    {
        PyObject *tmp_called_value_169;
        PyObject *tmp_expression_value_111;
        PyObject *tmp_call_result_99;
        PyObject *tmp_args_value_6;
        PyObject *tmp_tuple_element_6;
        PyObject *tmp_kwargs_value_6;
        tmp_expression_value_111 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_111 == NULL)) {
            tmp_expression_value_111 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_111 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 768;

            goto try_except_handler_84;
        }
        tmp_called_value_169 = LOOKUP_ATTRIBUTE(tmp_expression_value_111, mod_consts[69]);
        if (tmp_called_value_169 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 768;

            goto try_except_handler_84;
        }
        tmp_tuple_element_6 = mod_consts[294];
        tmp_args_value_6 = PyTuple_New(3);
        PyTuple_SET_ITEM0(tmp_args_value_6, 0, tmp_tuple_element_6);
        tmp_tuple_element_6 = Py_True;
        PyTuple_SET_ITEM0(tmp_args_value_6, 1, tmp_tuple_element_6);
        tmp_tuple_element_6 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[288]);

        if (unlikely(tmp_tuple_element_6 == NULL)) {
            tmp_tuple_element_6 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[288]);
        }

        if (tmp_tuple_element_6 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 769;

            goto tuple_build_exception_6;
        }
        PyTuple_SET_ITEM0(tmp_args_value_6, 2, tmp_tuple_element_6);
        goto tuple_build_noexception_6;
        // Exception handling pass through code for tuple_build:
        tuple_build_exception_6:;
        Py_DECREF(tmp_called_value_169);
        Py_DECREF(tmp_args_value_6);
        goto try_except_handler_84;
        // Finished with no exception for tuple_build:
        tuple_build_noexception_6:;
        tmp_kwargs_value_6 = PyDict_Copy(mod_consts[293]);
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 768;
        tmp_call_result_99 = CALL_FUNCTION(tmp_called_value_169, tmp_args_value_6, tmp_kwargs_value_6);
        Py_DECREF(tmp_called_value_169);
        Py_DECREF(tmp_args_value_6);
        Py_DECREF(tmp_kwargs_value_6);
        if (tmp_call_result_99 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 768;

            goto try_except_handler_84;
        }
        Py_DECREF(tmp_call_result_99);
    }
    {
        PyObject *tmp_called_value_170;
        PyObject *tmp_expression_value_112;
        PyObject *tmp_call_result_100;
        PyObject *tmp_kw_call_arg_value_0_45;
        PyObject *tmp_kw_call_arg_value_1_45;
        PyObject *tmp_kw_call_arg_value_2_45;
        PyObject *tmp_kw_call_dict_value_0_45;
        tmp_expression_value_112 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[5]);

        if (unlikely(tmp_expression_value_112 == NULL)) {
            tmp_expression_value_112 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[5]);
        }

        if (tmp_expression_value_112 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 772;

            goto try_except_handler_84;
        }
        tmp_called_value_170 = LOOKUP_ATTRIBUTE(tmp_expression_value_112, mod_consts[69]);
        if (tmp_called_value_170 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 772;

            goto try_except_handler_84;
        }
        tmp_kw_call_arg_value_0_45 = mod_consts[295];
        tmp_kw_call_arg_value_1_45 = mod_consts[296];
        tmp_kw_call_arg_value_2_45 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[290]);

        if (unlikely(tmp_kw_call_arg_value_2_45 == NULL)) {
            tmp_kw_call_arg_value_2_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[290]);
        }

        if (tmp_kw_call_arg_value_2_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_170);

            exception_lineno = 775;

            goto try_except_handler_84;
        }
        tmp_kw_call_dict_value_0_45 = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)mod_consts[53]);

        if (unlikely(tmp_kw_call_dict_value_0_45 == NULL)) {
            tmp_kw_call_dict_value_0_45 = GET_MODULE_VARIABLE_VALUE_FALLBACK(mod_consts[53]);
        }

        if (tmp_kw_call_dict_value_0_45 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);
            Py_DECREF(tmp_called_value_170);

            exception_lineno = 776;

            goto try_except_handler_84;
        }
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 772;
        {
            PyObject *args[] = {tmp_kw_call_arg_value_0_45, tmp_kw_call_arg_value_1_45, tmp_kw_call_arg_value_2_45};
            PyObject *kw_values[1] = {tmp_kw_call_dict_value_0_45};
            tmp_call_result_100 = CALL_FUNCTION_WITH_ARGS3_KWSPLIT(tmp_called_value_170, args, kw_values, mod_consts[145]);
        }

        Py_DECREF(tmp_called_value_170);
        if (tmp_call_result_100 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 772;

            goto try_except_handler_84;
        }
        Py_DECREF(tmp_call_result_100);
    }
    goto try_end_82;
    // Exception handler code:
    try_except_handler_84:;
    exception_keeper_type_82 = exception_type;
    exception_keeper_value_82 = exception_value;
    exception_keeper_tb_82 = exception_tb;
    exception_keeper_lineno_82 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Preserve existing published exception id 21.
    GET_CURRENT_EXCEPTION(&exception_preserved_type_21, &exception_preserved_value_21, &exception_preserved_tb_21);

    if (exception_keeper_tb_82 == NULL) {
        exception_keeper_tb_82 = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_82);
    } else if (exception_keeper_lineno_82 != 0) {
        exception_keeper_tb_82 = ADD_TRACEBACK(exception_keeper_tb_82, frame_929860c9d36c161b6d170f2111d32473, exception_keeper_lineno_82);
    }

    NORMALIZE_EXCEPTION(&exception_keeper_type_82, &exception_keeper_value_82, &exception_keeper_tb_82);
    ATTACH_TRACEBACK_TO_EXCEPTION_VALUE(exception_keeper_value_82, exception_keeper_tb_82);
    PUBLISH_EXCEPTION(&exception_keeper_type_82, &exception_keeper_value_82, &exception_keeper_tb_82);
    // Tried code:
    {
        bool tmp_condition_result_82;
        PyObject *tmp_cmp_expr_left_61;
        PyObject *tmp_cmp_expr_right_61;
        tmp_cmp_expr_left_61 = EXC_TYPE(PyThreadState_GET());
        tmp_cmp_expr_right_61 = PyExc_BaseException;
        tmp_res = EXCEPTION_MATCH_BOOL(tmp_cmp_expr_left_61, tmp_cmp_expr_right_61);
        assert(!(tmp_res == -1));
        tmp_condition_result_82 = (tmp_res != 0) ? true : false;
        if (tmp_condition_result_82 != false) {
            goto branch_yes_82;
        } else {
            goto branch_no_82;
        }
    }
    branch_yes_82:;
    {
        nuitka_bool tmp_assign_source_189;
        tmp_assign_source_189 = NUITKA_BOOL_FALSE;
        tmp_with_21__indicator = tmp_assign_source_189;
    }
    {
        bool tmp_condition_result_83;
        PyObject *tmp_operand_value_21;
        PyObject *tmp_called_value_171;
        PyObject *tmp_args_element_value_79;
        PyObject *tmp_args_element_value_80;
        PyObject *tmp_args_element_value_81;
        CHECK_OBJECT(tmp_with_21__exit);
        tmp_called_value_171 = tmp_with_21__exit;
        tmp_args_element_value_79 = EXC_TYPE(PyThreadState_GET());
        tmp_args_element_value_80 = EXC_VALUE(PyThreadState_GET());
        tmp_args_element_value_81 = EXC_TRACEBACK(PyThreadState_GET());
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 776;
        {
            PyObject *call_args[] = {tmp_args_element_value_79, tmp_args_element_value_80, tmp_args_element_value_81};
            tmp_operand_value_21 = CALL_FUNCTION_WITH_ARGS3(tmp_called_value_171, call_args);
        }

        if (tmp_operand_value_21 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 776;

            goto try_except_handler_85;
        }
        tmp_res = CHECK_IF_TRUE(tmp_operand_value_21);
        Py_DECREF(tmp_operand_value_21);
        if (tmp_res == -1) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 776;

            goto try_except_handler_85;
        }
        tmp_condition_result_83 = (tmp_res == 0) ? true : false;
        if (tmp_condition_result_83 != false) {
            goto branch_yes_83;
        } else {
            goto branch_no_83;
        }
    }
    branch_yes_83:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 776;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_85;
    branch_no_83:;
    goto branch_end_82;
    branch_no_82:;
    tmp_result = RERAISE_EXCEPTION(&exception_type, &exception_value, &exception_tb);
    if (unlikely(tmp_result == false)) {
        exception_lineno = 765;
    }

    if (exception_tb && exception_tb->tb_frame == &frame_929860c9d36c161b6d170f2111d32473->m_frame) frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = exception_tb->tb_lineno;

    goto try_except_handler_85;
    branch_end_82:;
    goto try_end_83;
    // Exception handler code:
    try_except_handler_85:;
    exception_keeper_type_83 = exception_type;
    exception_keeper_value_83 = exception_value;
    exception_keeper_tb_83 = exception_tb;
    exception_keeper_lineno_83 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    // Restore previous exception id 21.
    SET_CURRENT_EXCEPTION(exception_preserved_type_21, exception_preserved_value_21, exception_preserved_tb_21);

    // Re-raise.
    exception_type = exception_keeper_type_83;
    exception_value = exception_keeper_value_83;
    exception_tb = exception_keeper_tb_83;
    exception_lineno = exception_keeper_lineno_83;

    goto try_except_handler_83;
    // End of try:
    try_end_83:;
    // Restore previous exception id 21.
    SET_CURRENT_EXCEPTION(exception_preserved_type_21, exception_preserved_value_21, exception_preserved_tb_21);

    goto try_end_82;
    NUITKA_CANNOT_GET_HERE("exception handler codes exits in all cases");
    return NULL;
    // End of try:
    try_end_82:;
    goto try_end_84;
    // Exception handler code:
    try_except_handler_83:;
    exception_keeper_type_84 = exception_type;
    exception_keeper_value_84 = exception_value;
    exception_keeper_tb_84 = exception_tb;
    exception_keeper_lineno_84 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
        bool tmp_condition_result_84;
        nuitka_bool tmp_cmp_expr_left_62;
        nuitka_bool tmp_cmp_expr_right_62;
        assert(tmp_with_21__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_62 = tmp_with_21__indicator;
        tmp_cmp_expr_right_62 = NUITKA_BOOL_TRUE;
        tmp_condition_result_84 = (tmp_cmp_expr_left_62 == tmp_cmp_expr_right_62) ? true : false;
        if (tmp_condition_result_84 != false) {
            goto branch_yes_84;
        } else {
            goto branch_no_84;
        }
    }
    branch_yes_84:;
    {
        PyObject *tmp_called_value_172;
        PyObject *tmp_call_result_101;
        CHECK_OBJECT(tmp_with_21__exit);
        tmp_called_value_172 = tmp_with_21__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 776;
        tmp_call_result_101 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_172, mod_consts[74]);

        if (tmp_call_result_101 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);

            Py_DECREF(exception_keeper_type_84);
            Py_XDECREF(exception_keeper_value_84);
            Py_XDECREF(exception_keeper_tb_84);

            exception_lineno = 776;

            goto try_except_handler_82;
        }
        Py_DECREF(tmp_call_result_101);
    }
    branch_no_84:;
    // Re-raise.
    exception_type = exception_keeper_type_84;
    exception_value = exception_keeper_value_84;
    exception_tb = exception_keeper_tb_84;
    exception_lineno = exception_keeper_lineno_84;

    goto try_except_handler_82;
    // End of try:
    try_end_84:;
    {
        bool tmp_condition_result_85;
        nuitka_bool tmp_cmp_expr_left_63;
        nuitka_bool tmp_cmp_expr_right_63;
        assert(tmp_with_21__indicator != NUITKA_BOOL_UNASSIGNED);
        tmp_cmp_expr_left_63 = tmp_with_21__indicator;
        tmp_cmp_expr_right_63 = NUITKA_BOOL_TRUE;
        tmp_condition_result_85 = (tmp_cmp_expr_left_63 == tmp_cmp_expr_right_63) ? true : false;
        if (tmp_condition_result_85 != false) {
            goto branch_yes_85;
        } else {
            goto branch_no_85;
        }
    }
    branch_yes_85:;
    {
        PyObject *tmp_called_value_173;
        PyObject *tmp_call_result_102;
        CHECK_OBJECT(tmp_with_21__exit);
        tmp_called_value_173 = tmp_with_21__exit;
        frame_929860c9d36c161b6d170f2111d32473->m_frame.f_lineno = 776;
        tmp_call_result_102 = CALL_FUNCTION_WITH_POSARGS3(tmp_called_value_173, mod_consts[74]);

        if (tmp_call_result_102 == NULL) {
            assert(ERROR_OCCURRED());

            FETCH_ERROR_OCCURRED(&exception_type, &exception_value, &exception_tb);


            exception_lineno = 776;

            goto try_except_handler_82;
        }
        Py_DECREF(tmp_call_result_102);
    }
    branch_no_85:;
    goto try_end_85;
    // Exception handler code:
    try_except_handler_82:;
    exception_keeper_type_85 = exception_type;
    exception_keeper_value_85 = exception_value;
    exception_keeper_tb_85 = exception_tb;
    exception_keeper_lineno_85 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    Py_XDECREF(tmp_with_21__source);
    tmp_with_21__source = NULL;
    Py_XDECREF(tmp_with_21__enter);
    tmp_with_21__enter = NULL;
    Py_XDECREF(tmp_with_21__exit);
    tmp_with_21__exit = NULL;
    // Re-raise.
    exception_type = exception_keeper_type_85;
    exception_value = exception_keeper_value_85;
    exception_tb = exception_keeper_tb_85;
    exception_lineno = exception_keeper_lineno_85;

    goto frame_exception_exit_1;
    // End of try:
    try_end_85:;

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION(frame_929860c9d36c161b6d170f2111d32473);
#endif
    popFrameStack();

    assertFrameObject(frame_929860c9d36c161b6d170f2111d32473);

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION(frame_929860c9d36c161b6d170f2111d32473);
#endif

    if (exception_tb == NULL) {
        exception_tb = MAKE_TRACEBACK(frame_929860c9d36c161b6d170f2111d32473, exception_lineno);
    } else if (exception_tb->tb_frame != &frame_929860c9d36c161b6d170f2111d32473->m_frame) {
        exception_tb = ADD_TRACEBACK(exception_tb, frame_929860c9d36c161b6d170f2111d32473, exception_lineno);
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;
    CHECK_OBJECT(tmp_with_21__source);
    Py_DECREF(tmp_with_21__source);
    tmp_with_21__source = NULL;
    CHECK_OBJECT(tmp_with_21__enter);
    Py_DECREF(tmp_with_21__enter);
    tmp_with_21__enter = NULL;
    Py_XDECREF(tmp_with_21__exit);
    tmp_with_21__exit = NULL;

    // Report to PGO about leaving the module without error.
    PGO_onModuleExit("pandas.core.config_init", false);

    Py_INCREF(module_pandas$core$config_init);
    return module_pandas$core$config_init;
    module_exception_exit:

#if defined(_NUITKA_MODULE) && 0
    {
        PyObject *module_name = GET_STRING_DICT_VALUE(moduledict_pandas$core$config_init, (Nuitka_StringObject *)const_str_plain___name__);

        if (module_name != NULL) {
            Nuitka_DelModule(module_name);
        }
    }
#endif
    PGO_onModuleExit("pandas$core$config_init", false);

    RESTORE_ERROR_OCCURRED(exception_type, exception_value, exception_tb);
    return NULL;
}
