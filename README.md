# Python-AST-Tutorial
## Hand-in by dgod@itu.dk, nivs@itu.dk and thtj@itu.dk

### Solution description.
The goal of this assignment was to create metrics for calculating complexity.
Out solution favours nested functionality and function calls.

As such, condition and loops are calculated similar to the fibonaci sequence. 
A single occuren assign the value 1, a nested 2, another 3, 5, 8 etc.

For functions call, both internal and external of the files a single digit is added.

Uniquely for our implementation, only functions with function calls are calculated. 

### Not implemented consideration
We considered, but did not manage to complete also implement a condition of a certain amount, line of codes.
Also adding cross statement consideration, so an if-statement nested inside a while loop would also increase complexity. 

Adding a normalization of complexity could also had been a consideration as well as scoring different type of data structures.

### Results
Results are alphabetical sorted by file name.

|File | Function | (Complexity, Method calls)|
|-----|----------|---------------------------|
|airflow/api/auth/backend/default.py| decorated| (2, ['function', 'wraps'])|
|airflow/api/auth/backend/deny_all.py| decorated| (2, ['Response', 'wraps'])|
|airflow/api/client/api_client.py| create_pool| (1, ['NotImplementedError'])|
|airflow/api/client/api_client.py| delete_dag| (1, ['NotImplementedError'])|
|airflow/api/client/api_client.py| delete_pool| (1, ['NotImplementedError'])|
|airflow/api/client/api_client.py| get_pool| (1, ['NotImplementedError'])|
|airflow/api/client/api_client.py| get_pools| (1, ['NotImplementedError'])|
|airflow/api/client/api_client.py| trigger_dag| (1, ['NotImplementedError'])|
|airflow/contrib/example_dags/example_azure_container_instances_operator.py| | (4, ['datetime', 'timedelta', 'DAG', 'AzureContainerInstancesOperator'])|
|airflow/contrib/example_dags/libs/helper.py| print_stuff| (1, ['print'])|
|airflow/dag/base_dag.py| concurrency| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| dag_id| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| dag_ids| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| full_filepath| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| get_dag| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| is_paused| (1, ['NotImplementedError'])|
|airflow/dag/base_dag.py| task_ids| (1, ['NotImplementedError'])|
|airflow/dag/serialization/json_schema.py| make_dag_schema| (1, ['make_object_schema'])|
|airflow/dag/serialization/json_schema.py| make_operator_schema| (1, ['make_object_schema'])|
|airflow/example_dags/example_latest_only.py| | (3, ['DAG', 'LatestOnlyOperator', 'DummyOperator'])|
|airflow/example_dags/example_latest_only_with_trigger.py| | (6, ['DAG', 'LatestOnlyOperator', 'DummyOperator', 'DummyOperator', 'DummyOperator', 'DummyOperator'])|
|airflow/example_dags/example_passing_params_via_test_command.py| | (3, ['DAG', 'PythonOperator', 'BashOperator'])|
|airflow/example_dags/example_passing_params_via_test_command.py| my_py_command| (2, ['print', 'print'])|
|airflow/example_dags/subdags/subdag.py| subdag| (3, ['DAG', 'range', 'DummyOperator'])|
|airflow/example_dags/test_utils.py| | (2, ['DAG', 'BashOperator'])|
|airflow/hooks/\_\_init\_\_.py| _integrate_plugins| (1, ['globals'])|
|airflow/kubernetes/k8s_model.py| append_to_pod| (1, ['reduce'])|
|airflow/lineage/backend/\_\_init\_\_.py| send_lineage| (1, ['NotImplementedError'])|
|airflow/models/dagpickle.py| | (4, ['Column', 'Column', 'Column', 'Column'])|
|airflow/models/dagpickle.py| \_\_init\_\_| (2, ['hasattr', 'hash'])|
|airflow/models/errors.py| | (4, ['Column', 'Column', 'Column', 'Column'])|
|airflow/models/slamiss.py| | (8, ['Column', 'Column', 'Column', 'Column', 'Column', 'Column', 'Column', 'Index'])|
|airflow/models/slamiss.py| \_\_repr\_\_| (1, ['str'])|
|airflow/models/taskfail.py| | (8, ['Column', 'Column', 'Column', 'Column', 'Column', 'Column', 'Column', 'Index'])|
|airflow/models/taskfail.py| \_\_init\_\_| (1, ['int'])|
|airflow/operators/\_\_init\_\_.py| _integrate_plugins| (1, ['globals'])|
|airflow/sensors/\_\_init\_\_.py| _integrate_plugins| (1, ['globals'])|
|airflow/ti_deps/dep_context.py| | (22, ['RunnableExecDateDep', 'ValidStateDep', 'DagTISlotsAvailableDep', 'TaskConcurrencyDep', 'PoolSlotsAvailableDep', 'RunnableExecDateDep', 'ValidStateDep', 'DagTISlotsAvailableDep', 'TaskConcurrencyDep', 'PoolSlotsAvailableDep', 'RunnableExecDateDep', 'ValidStateDep', 'DagrunRunningDep', 'RunnableExecDateDep', 'ValidStateDep', 'DagTISlotsAvailableDep', 'TaskConcurrencyDep', 'PoolSlotsAvailableDep', 'DagrunRunningDep', 'DagrunIdDep', 'DagUnpausedDep', 'ExecDateAfterStartDateDep'])|
|airflow/ti_deps/dep_context.py| \_\_init\_\_| (1, ['set'])

### Findings
Using our complexity_visitor, we only found the following three `dep_context.py`, `taskfail.py` & `slamiss.py` diverging from the rest with especially `dep_context.py`, all three due to the amount of function calls. 
In general, nothing suggest a high amount of nested statements and instead many functioncal calls.  