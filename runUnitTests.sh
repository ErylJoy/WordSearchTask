cd Tests
echo Solution 1
python unitTests1.py &> temp1.txt
if grep -q OK temp1.txt; then
    echo Solution 1 passed all tests
else
    echo Solution 1 failed all tests
fi

echo
echo Solution 2
python unitTests2.py &> temp2.txt
if grep -q OK temp2.txt; then
    echo Solution 2 passed all tests
else
    echo Solution 2 failed all tests
fi

echo
echo Solution 3
python unitTests3.py &> temp3.txt
if grep -q OK temp3.txt; then
    echo Solution 3 passed all tests
else
    echo Solution 3 failed all tests
fi

echo
echo Solution 4
python unitTests4.py &> temp4.txt
if grep -q OK temp4.txt; then
    echo Solution 4 passed all tests
else
    echo Solution 4 failed all tests
fi

rm temp1.txt
rm temp2.txt
rm temp3.txt
rm temp4.txt
