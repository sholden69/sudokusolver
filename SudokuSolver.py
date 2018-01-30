import sys

# hard
#000000000000003085001020000000507000004000100090000000500000073002010000000040009
# easy
#100004030000300984900600070000009750006000800017200000050006002679003000040500007

def same_row(i,j): return (i//9) == (j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)

def r(a):
 #find the index of the first blank. Zero offset.
  i = a.find('0')
  if i == -1:
    #we're done, so exit and print out answer, breaking out of the recursion
    sys.exit("answer:"+a)

  excluded_numbers = set()
  for j in range(81):
    #print(a[j])
    #check if checking is in the same row,column or block as the blank we are looking at.
    if same_row(i,j)or same_col(i, j) or same_block(i, j):
      excluded_numbers.add(a[j])

  for m in '123456789':
    if m not in excluded_numbers:
     # try each successive non-excluded number recursively into r()
      r(a[:i]+m+a[i+1:])
    else:
      print("backtrack on square",i,":",a)

  #if it doesnt find an answer exits the function and returns back up to higher level. Need to understand backtracking

if __name__ == '__main__':
  if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
    r(sys.argv[1])
  else:
    print ('Usage: python sudoku.py puzzle')
    print ('  where puzzle is an 81 character string  representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank')