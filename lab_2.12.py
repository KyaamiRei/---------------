import re

s1 = '9217gd1927g1272g120d1fg012f8g130fg31f'
s2 = '97fryevuo80refhic8fhepidskc93-ruq[fj'
s3 = '2o84gv2048v2-49vohw[voihv9-wevhq['

for i in s1:
    result = re.search(r'\d', i)

    print(result)

