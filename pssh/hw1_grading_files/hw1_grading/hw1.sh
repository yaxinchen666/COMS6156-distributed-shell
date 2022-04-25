cp ../hw1/hw1.py .

passed=0

for f in test_cases/*.in
do
  python3 hw1.py < $f > hw1.out
  result=`diff hw1.out ${f%%.*}.out | wc -l`
  if [[ $result -eq 0 ]]
  then
    ((passed+=1))
  fi
done

echo $passed
