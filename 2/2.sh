paste -d"*" <(paste -sd+ <(rg ^f input.txt | rev | cut -c 1) | bc) <(paste -sd+ <(rg '^[du]' input.txt  | sed 's/down/1\*/;s/up/-1\*/g'  | bc) | bc) | bc

paste -d"*" <(paste -sd+ <(paste -d* <(cut -c 1 input.txt) <(rev input.txt | cut -c -1) <(sed 's/down/1\*/;s/up/-1\*/;s/forward/0\*/g' input.txt | bc | awk '{total += $0; $0 = total}1') | rg f | tr f 1 | bc ) | bc) <(paste -sd+ <(rg ^f input.txt | rev | cut -c 1) | bc) | bc
