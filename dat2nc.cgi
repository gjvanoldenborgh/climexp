#!/bin/sh
. ./nosearchenginewithheader.cgi
echo "Content-type: text/html"
echo

. ./getargs.cgi

datafile=data/`basename "$FORM_datafile"`
type="$FORM_type"
station=`echo "$FORM_station" | tr '/' '_'`

tmpfile=data/ncseries.nc
i=0
while [ -s $tmpfile ]; do
    tmpfile=data/ncseries$((i++)).nc
done
logfile=/tmp/dat2nc$$.log

. ./myvinkhead.cgi "Download netcdf time series" "$station" "$type"
echo "Generating $filetype file.  Just a moment.<p>"

export UDUNITS_PATH=`pwd`/etc/udunits.dat
bin/dat2nc "$datafile" "$type" "$station" $tmpfile > $logfile 2>&1
if [ ! -s $tmpfile ]; then
    echo "Something went wrong."
    echo
    cat $logfile
else
    echo "<a href=\"$tmpfile\">Download netcdf file</a>"
    echo
fi
/bin/rm $logfile
. ./myvinkfoot.cgi
