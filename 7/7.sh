paste -sd+ <(cat input.txt | sed s/\,/\\n/g | xargs -I_ sh -c 'echo _ - $(sed s/\,/\\n/g input.txt | datamash median 1)' | bc | sed s/\-//g) | bc
paste -sd+ <(cat input.txt | sed s/\,/\\n/g | xargs -I_ sh -c 'seq 0 $(echo _ - $(sed s/\,/\\n/g input.txt | datamash mean 1 | sed s/\\..*//g) | bc | sed s/\-//g)') | bc
