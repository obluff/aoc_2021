paste -d"<" input.txt <(cat input.txt | tail -n+2) | head -n-1 | bc | paste -sd+ | bc
paste -d"<" input.txt <(cat input.txt | tail -n+4) | head -n-3 | bc | paste -sd+ | bc
