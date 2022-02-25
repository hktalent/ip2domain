#!/bin/bash
function doMasscan {
   szFileName=$( sha1sum <<<$1 | sed 's/ .*$//g' )
   szFileName=`echo "${szFileName}.xml"`
   find . -type f -empty -name ${szFileName} -delete
   if [[ -f $szFileName ]] ; then
        return 1
    else
        masscan --rate=5000 --offline --top-ports 1000 -oX $szFileName $1
    fi
}

