echo $(wc -l tropes_20-06-2016.json | grep -o -E [0-9]\{5,\}) / 279990 \* 100 | bc -l

