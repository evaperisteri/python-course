sym = {
  "key1":"value1",
  "key2":10,
  3: [100, 200, 300],
  4: {1:"one", 2:"two"},
  # [1,2]: 10 key cant be a list becaause it need to be hashable -->type error
  (1, 2): 10, #πλειαδα ως key επειδή ειναι unbmodifiable not immutable
  #{1, 2}: "set" --> error
  frozenset({1, }):"set" #--> set becomes immutable
}

print(sym)