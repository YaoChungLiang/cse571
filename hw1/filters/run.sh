#!/bin/bash
# echo $1

# python3 localization.py $1 --seed 0
# python3 localization.py --plot pf --seed 0
# # python3 localization.py --plot ekf --data-factor 0.25 --filter-factor 0.25
# # python3 localization.py --plot ekf --data-factor 0.0625 --filter-factor 0.0625
# # python3 localization.py --plot ekf --data-factor 0.001 --filter-factor 0.1
# # python3 localization.py --plot pf --data-factor 0.25 --filter-factor 0.25 

# python localization.py ekf --data-factor 4 --filter-factor 4

# function sum()
# {
# 	x=$1
# 	sum=0
# 	for k in x
# 	do 
# 		sum=sum+k
# 	done
# 	return $sum
# }

max=10
len=6
factor=(0.015625 0.0625 0.25 4 16 64)

for j in `seq 1 $len`
do
	echo round $j : "factor is " ${factor[j-1]}
	for i in `seq 1 $max`
	do
		a=$(python localization.py ekf --data-factor ${factor[j-1]} --filter-factor ${factor[j-1]})
		# echo $a
		b[${i}]=$a
		echo ${b[i]},
	done
	echo "finished"
done

# for i in `seq 1 $max`
# do 
# 	echo ${b[i]}
# done

# sum=0
# for k in `seq 1 $len`
# do 
# 	echo $k
# 	sum=$(( $sum+${factor[k]} ))
# done
# echo $sum
# l=0
# l=(1+1)
# echo $l

# total=0
# for((i=0;i<10;i++))  #直接数值求和
# do
#         total=$(($total+$i))
# done
# echo $total

# | awk '{sum+=$1} END {print "Average = ", sum/NR}'


