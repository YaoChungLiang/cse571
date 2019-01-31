#!/bin/bash
echo $1

python3 localization.py $1 --seed 0
# python3 localization.py --plot ekf --seed 0
# python3 localization.py --plot ekf --data-factor 0.25 --filter-factor 0.25
# python3 localization.py --plot ekf --data-factor 0.0625 --filter-factor 0.0625
# python3 localization.py --plot ekf --data-factor 0.001 --filter-factor 0.1
# python3 localization.py --plot pf --data-factor 0.25 --filter-factor 0.25 
