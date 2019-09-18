# PartCuttingOptimizer

Made without online help, theres probably a better way to do it but I wanted to do it on my own.
You need many different parts of different lengths, which will be cut from a long, single length part that you can buy.
What is the minimum number of the single length parts you could buy and still get all your parts?
 
Example Run of CutParts.py:
```
Length of buyable part: 10
Add part length, or "end" to finish adding parts: 10
Add part length, or "end" to finish adding parts: 9
Add part length, or "end" to finish adding parts: 8
Add part length, or "end" to finish adding parts: 7
Add part length, or "end" to finish adding parts: 6
Add part length, or "end" to finish adding parts: 5
Add part length, or "end" to finish adding parts: 4
Add part length, or "end" to finish adding parts: 3
Add part length, or "end" to finish adding parts: 2
Add part length, or "end" to finish adding parts: 1
Add part length, or "end" to finish adding parts: end
buys: 6
sets:
[Decimal('10')]
[Decimal('9'), Decimal('1')]
[Decimal('8'), Decimal('2')]
[Decimal('7'), Decimal('3')]
[Decimal('6'), Decimal('4')]
[Decimal('5')]
excess:
0
0
0
0
0
5
```
