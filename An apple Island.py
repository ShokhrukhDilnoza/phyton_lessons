# -*Logical Operators -*-
"""
Created on Fri Aug 23 10:04:37 2024

@author: Shokhrukh
"""

print(''' 
      .@, 
     .@a@a,. 
     S@@ss@@@@a,. 
    sS@@@ss@@@@@Ss,  , 
 , SSSSS@@@ss@@@SSSs @, 
 @sSSSSSSSS@@ss@SSSSs@@s, , 
 `@@@@@SSSSSSSSssSSS@@@@@sSs, 
   @@@@@@@@@@@@@@ss@@@@@@@@SSs , 
 , `@@@@@@@@@@@@@@ss@@@@@@@SSSs@, 
  SsSSSS@@@@@@@@@@@ss@@@@@@SSSSS@, 
  `SSSSSSSSS@@@@@@@@@ss@@@@SSSSS@@ 
   `SSSSSSSSSSSS@@@@@@ss@@SSSSSS@@','', 
   , `SSSSSSSSSSSSSSS@@ss@SSSSS@@@;%,.,,` 
    @aSSSSSSSSSSSSSSSSSSssSSSS@@@@;%;%%' 
     `@@@@@@@SSSSSSSSSSSSssSSS@@@@;%;%' 
        `@@@@@@@@@@@@@@@SSSssS@@@@;%;% 
           `@@@@@@@@@@@@@@@@@ss@@@;%;%    ...,,,,,,,,,,.. 
               `@@@@@@@@@@@@@@@ssS;%;%  .;;%%;%%;%%%;%%;%%%,. 
         .,::;;;;;;;;`SSSSSSSSSSSss;%%,::;%;%%%%%%%;%%%%%%;%%%%,. 
      .:::;;;;;%;;;;;;;,;;,;;,;;,::,.,::;%%%%%;%%%%%%%%%%%%%%%;%%%;, 
    .:::;;;%;;;;;%;%;%;%;%;%;%%%%;%%%%%;%%%%%%%%%%;%%%%%;%%%%%%%%;%%;. 
   :::;%;;;;%;;%;;;%;%;;%%%;%%%%%%%;%%%%%%%;%%%%%%%%%x%x%%%%%%%%;%%;%;, 
  :::;;;;;%;;%;;;%;;%;%%%%%%%%;%%%%%%%%%%%%%%%%%%%%%%%x%x%%%%%%%%%%%;%;, 
 :::;;;;;%;;;;;;%;%%;%xx%;%%%%%%%;%%%%%%%x%%%%%%%%%%%%%x%x%x%%%%%%%;%;%; 
,:::;%;;%;;;%;%;;%;%%x%;%%%%%%%%%%%%%x%x%%x%%%%%%%%%%%%%x%%x%x%%%%%%;%%;, 
:::;;;;%;;%;;%;;%%%;x%x%%%;%%%%%%%%%%%%%x%%x%%%%%%%%%%%xx%x%x%%%%%%%%;;%; 
:::%;;;;;%;;%;;%%;%%;%;%%%%%%%%%%%%;%%x%%x%%x%;%%%%%%%%%x%x%%%%%%%%%;%;%; 
:::;;;%;;;;%;%;%;%%;%%%%%%%;%%%%%%%%%%%x%%x%%%%%%%%%%%%x%x%%x%%%%%%;%;%%; 
`:::;;;;%;%;%;%;%%;%%;%%%%%%%%%%%%%%%%%%%x%x%%%%%%%%%%xx%x%%%%%%%%%;%;%;' 
 `:::;;%;%;;%;;%%;%%;%;%%;%%%%%;%%%%%%%%%%%%%%%%%%;%%%%x%%%%%%%%%;%%;%;' 
  `:::;;;;;%;;%%;%%;%%%%%%%;%%%%%%%%%%;%%%%%%%%;%%%%%;%%%%%%%%%;%%;%%;' 
   `:::;;%;;;%;;;%%%;%%;%%%%%%%%%%;%%%%%%%%%%;%%%%%%%%%%%%%%;%;%;%%%;' 
     `:::;;%;;;%%;%;%;%%;%;%%%%%%%%%%%%%%%%%%%%%%;%%;%%%%;%%%;%;%;%;' 
       `:::;;;%;;%;;%%;%;%%%%%%%%%%%%%%%%%%;%%%%%%%%%%%;%%%;%%;%%;' 
         `:::;;;%;;%;%;%%%%;%%%%%%;%%%%%%%%%%%%;%%%;%%;%%;%%;%%;' 
           `:::;;%;;%;;%;%%%%%%;%%%%%%%%%%%%;%%%%%%%%%%%;%;%%;' 
             `:::;%;;;%;;%;%x%%%%%;%%%%%%%%x%%%%%%;%%%;%%;%;' 
               `:::;;;%;%;;%;x%x%x%%x%;%x%x%%%%;%%%%%;%;%;' 
                 `:::%;%;;%:%:,xx%%x%%x%xx,:%%%%;%%;%%%;' 
                   `:::%;;;;:%:`xx%x%xx%x':%%%;%%%%%%;' 
                    `:::;;%;;%:,`%x%xx%x',:%;%%%%;%%;' 
                      `:::;;;;;:::'   `:::;;;;;;:::'
''')
print("Welcome to An Apple Island!")
answer=input("Where would you go? Left or Right?>>>").title()
if not answer=='Left':
    print("Game over.")
else:
    answer2=input('Would you want to swim or wait?>>>').title()
    if not answer2=='Wait':
        print("Game over.")
    else:
        answer3=input('Which door? Red, Blue or Yellow?>>').title()
        if not answer3=='Yellow':
            print('Game over.')
        else:
            print("You win!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    