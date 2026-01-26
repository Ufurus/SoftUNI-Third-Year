def sum_nums(*args):

     negs = sum([x for x in args if x < 0])
     pos = sum([x for x in args if x > 0])

     if abs(negs) > pos:
          print(f"{negs}\n{pos}\nThe negatives are stronger than the positives")
     else:
         print(f"{negs}\n{pos}\nThe positives are stronger than the negatives")

sum_nums(*[int(x) for x in input().split()])