from __future__ import print_function
from zilean.utils.mysql_access import (execute_only,
                                       execute_and_fetch)
from zilean.sys.models.zilean_rtype import _refetch_filter
from .mysql_query import (_SHOW_DATABASES,
                          _CREATE_DATABASE,
                          _DELETE_DATABASE,
                          _SHOW_TABLES,
                          _TABLE_FIELDS,
                          _CREATE_TABLE,
                          _USE_DATABASE,
                          _DELETE_TABLE,
                          _IE_QUERY,
                          _DL_QUERY,
                          _SL_QUERY,
                          _CT_QUERY,
                          _UE_QUERY,
                          _AUTOINCR,
                          _ADD_COLUMN,
                          _DELETE_COLUMN,
                          _CHANGE_COLUMN,
                          _SELECT_OPTI)

@_refetch_filter([0])
def databases():
    """
    return a list of strings containing msql databases
    =======================================================
    >>> from zilean.zilean import databases
    >>> databases()
    ["sys", "mysql"]
    =======================================================
    """
    return execute_and_fetch(_SHOW_DATABASES)

def make_database(dbname):
    """
    make a mysql database
    =======================================================
    >>> _make_database('Table')
    =======================================================
    """
    return execute_only(_CREATE_DATABASE.format(dbname))

def remove_database(dbname):
    """
    Remove a mysql database
    =======================================================
    >>>
    """
    return execute_only(_DELETE_DATABASE.format(dbname))

@_refetch_filter([0])
def tables(dbname):
    """
    return a list of strings containing mysql tables at one
    given database
    =======================================================
    >>> _tables("sys")
    ["host_ip", "host_kappa" ... ""]
    =======================================================
    """
    return execute_and_fetch(_SHOW_TABLES.format(dbname))

@_refetch_filter([0])
def table_fields(dbname, table):
    """
    Not Implemented
    =======================================================
    """
    return execute_and_fetch(_TABLE_FIELDS.format(dbname, table))

def table_content(db, table):
    """
    return a 2 dimentioanl array containing all table values
    ========================================================
    >>> _table_content("sys", "host_ip")
    [[]]
    ========================================================
    """
    #XXX: uses : `select * from table`
    return execute_and_fetch(_SHOW_TABLE_VALUES.format(db, table))

def make_table(db, table, **kwargs):
    """
    Create a table at database with kwargs as fields
    =======================================================
    """
    return execute_only(_CT_QUERY(db, table, **kwargs))

def remove_table(db, table):
    """
    Drop table at db
    =======================================================
    """
    return execute_only(_DELETE_TABLE.format(db, table))

def table_primary_start(db, table, start):
    """
    Set table starting point for AUTO_INCREMENT PRIMARY Key
    """
    return execute_only(_AUTOINCR.format(db, table, start))

def copy_table(db, table):
    """
    Not Implemented
    =======================================================
    """
    pass

def add_field(db, table, field_name, field_type):
    """
    Add field to table at db
    =======================================================
    """
    return execute_only(_ADD_COLUMN.format(db, table, field_name, field_type))

def remove_field(db, table, field_name):
    """
    Remove field from table at db
    =======================================================
    """
    return execute_only(_DELETE_COLUMN.format(db, table, field_name))

def change_field(db, table, field_name, new_field, field_type):
    """
    Change field in table at db
    =======================================================
    """
    return execute_only(_CHANGE_COLUMN.format(db,
                                              table,
                                              field_name,
                                              new_field,
                                              field_type))

def add_element(db, table, **kwargs):
    """
    add element to table at db
    =======================================================
    """
    return execute_only(_IE_QUERY(db, table, **kwargs), commit=True)

def remove_elements(db, table, with_limit=-1, where=None):
    """
    Remove Element from table at db
    =======================================================
    """
    return execute_only(_DL_QUERY(db, table, where, with_limit), commit=True)

def select_elements(db, table, with_limit=-1, selection=None, where=None):
    """
    Select elements that satisfy kwargs from table at db
    =======================================================
    """
    return execute_and_fetch(_SL_QUERY(db, table, where, with_limit, selection))

def update_element(db, table, with_limit=-1, sets=None, where=None):
    """
    """
    return execute_only(_UE_QUERY(db, table, where, with_limit, sets), commit=True)

def select_optimised(db,
                     table,
                     with_limit=1,
                     selection="*",
                     kind="ASC",
                     sorted_by=None):
    """
    Not Implemented
    =======================================================
    """
    return execute_and_fetch(_SELECT_OPTI.format(selection,
                                                 db,
                                                 table,
                                                 sorted_by,
                                                 kind,
                                                 with_limit))
