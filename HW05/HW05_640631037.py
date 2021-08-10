fresh_milk = 10
dolls = 30
vanilla_profit = 2
strawberry_profit = 3
vanilla_use = 0.5 # Vanilla ice cream use 0.5 liter fresh milk
strawberry_use = 0.2 # Strawberry ice cream use 0.2 liter fresh milk
min_fresh_milk_use = min([vanilla_use, strawberry_use]) # Find minumum fresh milk use

if fresh_milk >= min_fresh_milk_use:
    
    if strawberry_profit > vanilla_profit:
        
        if strawberry_use <= vanilla_use:
            
            # Make Strawberry ice cream
            strawberry_ice = int(fresh_milk / strawberry_use)
            print('Make', strawberry_ice, 'Strawberry ice cream boxes')
            
            fresh_milk = fresh_milk - (strawberry_ice * strawberry_use)
            print('Fresh Milk:', fresh_milk, 'lites remaining')
            # Dolls remaining
            if strawberry_ice >= dolls:
                promotion = 1 * dolls
                print('Promotion:', promotion, 'Dolls')
                dolls = dolls - dolls
                print('Dolls:', dolls, 'remaining')
            else:
                promotion = 1 * strawberry_ice
                print('Promotion:', promotion, 'Dolls')
                dolls
            
            # Strawberry Profit
            strawberry_ice_profit = strawberry_ice * strawberry_profit
            print('Profit($):', strawberry_ice_profit)
    
    else:
        # Make Vanilla ice cream
        vanilla_ice = int(fresh_milk / vanilla_use)
        print('Make', vanilla_ice, 'Vanilla ice cream boxes')
         
        # Fresh milk remaining
        fresh_milk = fresh_milk - (vanilla_ice * vanilla_use)
        print('Fresh Milk:', fresh_milk, 'lites remaining')
        
        if fresh_milk > min_fresh_milk_use:
            # Make Strawberry ice cream
            strawberry_ice = int(fresh_milk / strawberry_use)
            print('Make', strawberry_ice, 'Strawberry ice cream boxes')
        
        ice_cream_make = vanilla_ice + strawberry_ice
        # print(ice_cream_make)
        
        # Dolls remaining
        if ice_cream_make >= dolls:
            promotion = 1 * dolls
            print('Promotion:', promotion, 'Dolls')
            dolls = dolls - dolls
            print('Dolls:', dolls, 'remaining')
        else:
            promotion = 1 * ice_cream_make
            print('Promotion:', promotion, 'Dolls')
            dolls
        
        # Profit
        ice_cream_profit = (vanilla_ice * vanilla_profit) + (strawberry_ice * strawberry_profit)
        print('Profit($):', ice_cream_profit)

else:
    print('Fresh milk not enough')