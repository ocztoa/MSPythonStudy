print("-"*40)
print("  cm  mm  m  inch")
print("-"*40)

for cm in range (1,51):
    mm=cm*10.0
    m=cm*0.01
    inch=cm*0.3937
    print("%d cm %.1f mm %.2f m %.2f inch"%(cm,mm,m,inch))