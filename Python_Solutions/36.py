def common_skill(set1,set2):
    common = set1 & set2 #set1.intersection(set2)
    return common
set1 = {"python" , "java", "c"}
set2 = {"python" , "javascript" , "c++"}
common = common_skill(set1,set2)
print(f"Common skills between set1 and set2: {common}")