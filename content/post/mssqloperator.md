---
title: "Mssqloperator"
date: 2021-02-03T06:07:27-06:00
draft: true
---

# MS SQL Server Operator on Airflow

## Introduction 

Now days multicloud idea is becoming more common than ever so it's not weird to wondering how to use Airflow to connect MS SQL Server relational database.

Of course, you can use GKEPodOperator and setup a docker image to support this operation but guess what? There is an straighforward way to do it using `MsSqlOperator` operator and I will try to show you how-to.

[Apache documentation](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-mssql/stable/_api/airflow/providers/microsoft/mssql/operators/mssql/index.html)

This is how will looks like in your DAG script

## Motivation

This is how your task will look in action
{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=1" >}}

{{< / highlight >}}

### Break-down
Cool! isn't it? 
So we have following class header for `MsSqlOperator`
{{< highlight python "linenos=table,hl_lines=8 15-17,linenostart=1" >}}
class airflow.providers.microsoft.mssql.operators.mssql.MsSqlOperator(
    *, 
    sql: str, 
    mssql_conn_id: str = 'mssql_default', 
    parameters: Optional[Union[Mapping, Iterable]] = None, 
    autocommit: bool = False, 
    database: Optional[str] = None, 
    **kwargs
)
{{< / highlight >}}

### Create a connection reference

Let's talk about `mssql_con_id` parameter, you can create a `conn_id` using Airflow UI
( `Menu -> Admin -> Connections` ). You should add a hostname / login / password information attached to it. Airflow pipelines retrieve centrally-managed connections information by specifying the relevant conn_id.


## Setup Airflow

In ordert to use `MsSQLOperator` you should install following modules (tested in `Airflow 10.1.14`)

{{< highlight bash "linenos=table,hl_lines=8 15-17,linenostart=1" >}}
{{< / highlight >}}