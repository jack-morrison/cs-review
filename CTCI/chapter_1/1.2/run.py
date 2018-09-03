from isPermutation import *

# True -- these are permutations of each other
inputT1 = "jackmorrison"
inputT2 = "nkmorcrijaso"

# False -- these are not permutations of each other
inputF1 = "lksjdf"
inputF2 = "kjhsfkjasfef"

dict1 = string_to_dict_of_counts(inputF1)
dict2 = string_to_dict_of_counts(inputF2)

answer = check_dict_equivalence(dict1, dict2)

print(answer)
