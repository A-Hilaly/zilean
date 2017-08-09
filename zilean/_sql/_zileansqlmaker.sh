#!/bin/bash

source $ZILEAN_SQL/_mysqltools.sh

function make_zilean_mysql () {
  mysql_read $zuser "-p$zpassword" < $zilean_cache
  mysql_read $zilean_sys
}

function clear_zilean_mysql () {
  mysql_read $zilean_clear
}

function backupzilean_mysql () {
  mysql_dump_database zs $1
  mysql_dump_database zc $2
}

function zilean_mysql_frombackup () {
    sysbackup=$1
    cachebackup=$2
    mysql_read $sysbackup
    mysql_read $cachebackup
}

function zilean_mysql_maker () {
    option=$1
    mode=$2
    bu1=$3
    bu2=$4
    if [ "$option" = "make" ]; then
        make_zilean_mysql
    if [ "$mode" = "--with-bu" ]; then
        zilean_mysql_frombackup $bu1
        zilean_mysql_frombackup $bu2
    elif [ "$option" = "remake" ] && [ -d $zilean_temp]; then
        mkdir $zilean_temp
        bu1=$zilean_temp/t1.sql
        bu2=$zilean_temp/t2.sql
        backupzilean_mysql $bu1 $bu2
        clear_zilean_mysql
        zilean_mysql_maker make --with-bu $bu1 $bu2
        clear_temp
    elif [ "$option" = "clear" ]; then
        clear_zilean_mysql
    fi
}

$@