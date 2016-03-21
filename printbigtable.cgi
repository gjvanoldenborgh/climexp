#!/bin/sh
#
# print an ensemble of time series
. ./init.cgi
. ./getargs.cgi

# no ensemble member selection yet

echo "Content-type: text/html"
echo
. ./myvinkhead.cgi "ASCII table"

echo "Preparing table...<p>"
if [ -z "$FORM_listname" ]; then
    table=data/$FORM_TYPE${FORM_wmo}_table.txt
    ( ./bin/printbigtable data/$FORM_TYPE$FORM_wmo.dat > $table ) 2>&1
else
    prog=$FORM_prog
    if [ -n "$FORM_extraargs" ]; then
        prog=${prog}_$FORM_extraargs
    fi
    table=data/`basename $FORM_listname .txt`_table.txt
    (./bin/printbigtable file $FORM_listname $prog > $table ) 2>&1
fi
echo "<p>The table is available <a href=\"$table\">here</a>"

. ./myvinkfoot.cgi