cat input.txt | sed 's/\ ->\ / /;s/\,/\ /g' | awk '{if(($1 == $3) || ($2 == $4)) {print}}' | xargs -I_ sh -c 'join <(echo _ | seq $(cut -d " " -f 1,3 | xargs -n1 | sort -g | xargs) | sed "s/^/1\ /") <(echo _ | seq $(cut -d " " -f 2,4 | xargs -n1 | sort -g | xargs) | sed "s/^/1\ /")' | sort | uniq -c | sed s/\ //g | rg ^1 --invert-match | wc -l

