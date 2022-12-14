import rlcompleter
my_completer = rlcompleter.Completer()
phrase_list = ['co', 'sys.m', 'cal','brea','excep','finall']
for phrase in phrase_list:
   print(phrase + ' (TAB): ', end='')
   try:
       for i in range(50):
             terms = my_completer.complete(phrase, i)
             if terms is None:
                 break
             print(terms, end='\t')
       print()
   except:
       pass



