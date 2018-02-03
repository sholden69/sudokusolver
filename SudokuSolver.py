import sys

# hard
#000000000000003085001020000000507000004000100090000000500000073002010000000040009
# easy
#100004030000300984900600070000009750006000800017200000050006002679003000040500007

def same_row(i,j): return (i//9) == (j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)


def r_apply_heuristics (a):
    #Next time: get around immutable string problem. Turn this into an array of numbers
    #loop is testing 'a' every time rather than a with the fixes applied to it.
    # initialise an array with every possibility

    cand_sets = [set({1,2,3,4,5,6,7,8,9}) for _ in range(81)]
    fixes=[0 for _ in range(81)] #keep track of which cells are fixed
    fixes_to_do=True
    while fixes_to_do:
      # build a set of possible values and check for any cells that only have 1 entry and fix those
      fixes_to_do=False
      for i, c in enumerate(a):
         if a[i]=='0':  ## blank square so need to find candidates
             incs=set({'1','2','3','4','5','6','7','8','9'})
             for j in range(81):
                 # print(a[j])
                 # check if checking is in the same row,column or block as the blank we are looking at.
                 if  same_row(i, j) or  same_col(i, j) or  same_block(i, j):
                     incs.discard(a[j])
             if len(incs)==1:
                 fixes[i]=int(incs[0])
                 print("eureka")
             cand_sets[i]=incs
         else:
             cand_sets[i]=a[i]
  # zero out those already fixed in some subsequent step
  # Look for unique options
      for row in range(9):
         scores=[0 for _ in range(9)] #an array for scoring each value ie how many times it occurs
         for col in range(9):
             for num_str in cand_sets[row*9+col] :
                 num=int(num_str)
                 scores[num-1]=scores[num-1]+1

         #iterate through scores and where it's 1 fix that square in a
         print(scores)
         for i,res in enumerate(scores):
              if res==1:
                  num_str=str(i+1)
                  for col in range(9):
                      if num_str in cand_sets[row*9+col] and fixes[row*9+col]==0:
                        print("fixing",i+1," on row ",row+1," col ", col+1)
                        fixes[row*9+col]=i+1
                        fixes_to_do=True   #send it round the loop again
                       # a[row*9+col]=num_str
                  # find which cell i is in
      print("fixes ",fixes)
    return a

def r_simple(a):
# Very basic brute force algorithm that starts at the first blank square, finds excluded numbers
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
      r_simple(a[:i]+m+a[i+1:])
    else:
      print("backtrack on square",i,":",a)

  #if it doesnt find an answer exits the function and returns back up to higher level. Need to understand backtracking

if __name__ == '__main__':
  if len(sys.argv) == 2 and len(sys.argv[1]) == 81:
    # run some pre-heuristics to see what we can solve
    a=r_apply_heuristics(sys.argv[1])
    print(a)
   # r_simple(sys.argv[1])
  else:
    print ('Usage: python sudoku.py puzzle')
    print ('  where puzzle is an 81 character string  representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank')