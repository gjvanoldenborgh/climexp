#!/bin/bash
[ -z "$prog" ] && prog=$FORM_prog
[ -z "$shortclinate" ] && shortclimate=$FORM_shortclimate
[ -z "$shortclimate" ] && shortclimate=$FORM_climate
[ -z "$shortclimate" ] && shortclimate=$climate
[ -z "$shortclimate" ] && shortclimate=$STATION
[ -z "$listname" ] && listname=$FORM_listname
[ -z "$extraargs" ] && extraargs=$FORM_extraargs
shortclimate=`echo "$shortclimate" | tr '_' ' '`
cat << EOF
<div class="menukopje">Investigate this set of time series spatially</div>
<div class="menulink"><a href="plotbox.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Make a map</a>/<a href="box2kml.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">export kml</a></div>
<div class="menulink"><a href="plotboxval.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Plot $shortclimate</a></div>
<div class="menulink"><a href="plotboxcorr.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Correlate with a time series</a></div>
<div class="menulink"><a href="plotboxautocorr.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Autocorrelations</a></div>
<div class="menulink"><a href="plotboxhist.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Statistical properties</a></div>
<div class="menulink"><a href="plotboxfieldcorr.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&nperyear=${NPERYEAR}&extraargs=${extraargs}">Correlate with a field</a></div>
<div class="menulink"><a href="attributeform.cgi?id=$EMAIL&TYPE=setmap&WMO=${listname}&STATION=${shortclimate}&NAME=${prog}&NPERYEAR=${NPERYEAR}&extraargs=${extraargs}">Trends in return times of extremes</a></div><div class="menulink"><a href="listbox.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&extraargs=${extraargs}">Make a list suitable for uploading</a></div>
<div class="menukopje">Investigate this set of time series together</div>
<div class="menulink"><a href="printbigtable.cgi?listname=$listname&prog=$prog&extraargs=$extraargs">Download as big ascii table</a></div>
<div class="menulink"><a href="attributeform.cgi?id=$EMAIL&TYPE=set&WMO=${listname}&STATION=${shortclimate}&NAME=${prog}&NPERYEAR=${NPERYEAR}&extraargs=${extraargs}">Trends in return times of extremes</a></div>
<div class="menulink"><a href="histogramform.cgi?id=${EMAIL}&TYPE=set&WMO=${listname}&STATION=${shortclimate}&NAME=${prog}&NPERYEAR=${NPERYEAR}&extraargs=${extraargs}">Plot and fit combined distribution</a></div>
EOF
###  echo "<div class="menulink"><a href=\"averageseries.cgi?id=${EMAIL}&climate=${shortclimate}&prog=${prog}&listname=${listname}&location=${location}\">Compute a simple scaled average</a> (no area-weighting)"
