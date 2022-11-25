import random

x = 0
while x < 1:
    print(
          "West Province 1 = 0\n" 
          "West Province 2 = 1\n"
          "West Province 3 = 2\n"
          "Asado Desert = 3\n"
          "West Paldean Sea = 4         \n"
          "East Province Area 1 = 5 \n"
          "East Province Area 2 = 6\n"
          "East Province Area 3 = 7\n"
          "East Paldean Sea = 8     \n"
          "North Province Area 1 = 9\n"
          "North Province Area 2 = 10\n"      
          "North Province Area 3 = 11\n"
          "North Paldean Sea = 12       \n"
          "South Province Area 1 = 13 \n"
          "South Province Area 2 = 14\n"
          "South Province Area 3 = 15\n"
          "South Province Area 4 = 16\n"
          "South Province Area 5 = 17\n"
          "South Province Area 6 = 18\n"
          "South Paldean Sea = 19\n"
          "Tagtree Thicket = 20\n"
          "Casseroya Lake = 21\n"
          "Glaseado Mountain = 22\n"  
          "Pokemon League = 23\n"
          "Area Zero = 24\n"
          "Poco Path  = 25\n"
          )
    regionSelect = input("Choose your Area: ")
    encounterNo = int(input("Choose Number of Encounters: "))

    ## Encounter index
    westPA1 =["Nymble","Yungoos","Combee","Happiny","Buizel","Floatzel","Psyduck","Chewtle","Gastly","Rockruff","Petilil","Lilligant","Misdreavus","Makuhita","Crabrawler","Salandit","Phanpy","Gible","Nacli","Wingull","Pelipper","Magikarp","Arrokuda","Basculin","Drifloon","Flabebe","Diglett","Numel","Bronzor","Mankey","Charcadet","Tadbulb","Wattrel","Swablu","Skiddo","Capsakid","Flittle","Mudbray","Wiglett","Bombirdier","Sableye","Falinks","Larvitar","Tynamo","Eelektrik","Rufflet","Gimmighoul (Chest Form)"]
    westPA2 =["Lechonk","Oinkologne","Tarountula","Spidops","Lokix","Pawmo","Yungoos","Gumshoos","Chansey","Azumarill","Buizel","Floatzel","Psyduck","Chewtle","Kirlia","Arboliva","Starly","Staravia","Staraptor","Flaaffy","Petilil","Lilligant","Makuhita","Hariyama","Crabrawler","Salandit","Donphan","Gible","Nacli","Wingull","Pelipper","Magikarp","Arrokuda","Barraskewda","Basculin","Meowth","Drifloon","Drifblim","Diglett","Dugtrio","Meditite","Medicham","Charcadet","Tadbulb","Bellibolt","Croagunk","Toxicroak","Wattrel","Girafarig","Grimer","Maschiff","Mabosstiff","Ditto","Skiddo","Paldean Tauros","Stunky","Murkrow","Toedscool","Wiglett","Wugtrio","Varoom","Cyclizar","Sableye","Noibat","Dreepy","Glimmet","Rotom","Pincurchin","Sandygast","Palossand","Slowpoke","Slowbro","Shellos","Gastrodon","Glalie","Gimmighoul (Chest Form)"]
    westPA3 =["Lechonk","Oinkologne","Tarountula","Spidops","Lokix","Jumpluff","Fletchinder","Pawmo","Gumshoos","Greedent","Chansey","Azumarill","Floatzel","Clodsire","Psyduck","Drednaw","Jigglypuff","Gallade","Pikachu","Fidough","Dachsbun","Vigoroth","Arboliva","Sudowoodo","Starly","Staravia","Staraptor","Petilil","Lilligant","Shroomish","Breloom","Applin","Misdreavus","Hariyama","Nacli","Magikarp","Arrokuda","Barraskewda","Basculin","Meowth","Persian","Drifloon","Drifblim","Bronzong","Primeape","Charcadet","Barboach","Whiscash","Tadbulb","Goomy","Eevee","Sylveon","Maschiff","Mabosstiff","Dedenne","Pachirisu","Shroodle","Foongus","Voltorb","Electrode","Ditto","Skiddo","Gogoat","Zorua","Zoroark","Murkrow","Toedscool","Tropius","Pineco","Scyther","Espathra","Mudbray","Mudsdale","Hatenna","Bombirdier","Sableye","Dreepy","Greavard","Komala","Snom","Glalie","Rufflet","Deino","Gimmighoul (Chest Form)"]
    asado = ["Lokix","Pawmo","Yungoos","Gumshoos","Combee","Chansey","Gastly","Rockruff","Makuhita","Phanpy","Donphan","Floette","Bronzor","Charcadet","Murkrow","Bramblin","Toedscool","Capsakid","Cacnea","Rellor","Flittle","Hippopotas","Sandile","Silicobra","Mudbray","Larvesta","Tinkatink","Orthworm","Falinks","Stonjourner"]
    westSea =["Buizel","Floatzel","Wingull","Pelipper","Magikarp","Gyarados","Barraskewda","Kilowattrel","Bombirdier","Finizen","Orthworm","Shellder","Cloyster","Qwilfish","Luvdisc","Finneon","Lumineon","Bruxish","Skrelp","Clauncher","Tynamo","Eelektrik","Froslass","Veluza"]
    eastPA1 =["Lechonk","Oinkologne","Spidops","Skiploom","Pawmo","Yungoos","Rookidee","Corvisquire","Azurill","Buizel","Psyduck","Chewtle","Chewtle","Drednaw","Gastly","Pikachu","Steenee","Rockruff","Oricorio (Baile Style)","Applin","Squawkabilly","Makuhita","Crabrawler","Nacli","Magikarp","Arrokuda","Basculin","Gulpin","Drifloon","Charcadet","Tadbulb","Umbreon","Shroodle","Teddiursa","Skiddo","Paldean Tauros","Litleo","Pyroar","Murkrow","Toedscool","Fomantis","Lurantis","Venonat","Venomoth","Pineco","Flittle","Mudbray","Wiglett","Shuppet","Dreepy","Komala","Pincurchin","Sandygast","Palossand","Slowpoke","Shellos","Gastrodon","Mareanie"]
    eastPA2 =["Oinkologne","Spidops","Skiploom","Pawmo","Yungoos","Rookidee","Corvisquire","Chansey","Marill","Surskit","Buizel","Chewtle","Chewtle","Drednaw","Kirlia","Gastly","Tandemaus","Bounsweet","Dolliv","Arboliva","Squawkabilly","Makuhita","Crabrawler","Cufant","Nacli","Magikarp","Arrokuda","Basculin","Drifloon","Bronzor","Charcadet","Tadbulb","Wattrel","Grimer","Shroodle","Magnemite","Skiddo","Paldean Tauros","Murkrow","Mimikyu","Toedscool","Fomantis","Lurantis","Venonat","Venomoth","Pineco","Mudbray","Tinkatink","Wiglett","Wugtrio","Cyclizar","Sableye","Shuppet","Dreepy","Rotom","Komala","Pincurchin","Sandygast","Palossand","Slowpoke","Mareanie","Froslass","Rufflet","Gimmighoul (Chest Form)"]
    eastPA3 =["Lokix","Pawmo","Yungoos","Gumshoos","Rookidee","Corvisquire","Buizel","Floatzel","Clodsire","Psyduck","Chewtle","Chewtle","Drednaw","Gastly","Fidough","Dachsbun","Rolycoly","Carkol","Squawkabilly","Makuhita","Hariyama","Salandit","Cufant","Nacli","Magikarp","Arrokuda","Barraskewda","Basculin","Meowth","Drifloon","Drifblim","Diglett","Dugtrio","Torkoal","Charcadet","Barboach","Tadbulb","Goomy","Voltorb","Electrode","Magnemite","Growlithe","Skiddo","Murkrow","Gothita","Sinistea","Bramblin","Toedscool","Silicobra","Mudsdale","Varoom","Revavroom","Orthworm","Sableye","Shuppet","Dreepy","Glimmet","Larvitar","Pawniard","Gimmighoul (Chest Form)"]
    eastSea =["Bruxish","Clauncher","Mareanie","Toxapex"]
    northPA1 =["Lokix","Jumpluff","Pawmo","Greedent","Kricketune","Vivillon","Vespiquen","Chansey","Blissey","Floatzel","Golduck","Wigglytuff","Gallade","Haunter","Arboliva","Lycanroc","Ampharos","Applin","Grumpig","Mismagius","Salazzle","Copperajah","Naclstack","Barraskewda","Drifblim","Floette","Bronzong","Axew","Fraxure","Primeape","Lucario","Barboach","Whiscash","Umbreon","Ursaring","Altaria","Gogoat","Sneasel","Weavile","Honchkrow","Indeedee","Brambleghast","Fomantis","Lurantis","Scovillain","Venonat","Venomoth","Espathra","Mudsdale","Tinkatuff","Wugtrio","Revavroom","Hawlucha","Noibat","Noivern","Drakloak","Greavard","Houndstone","Eiscue","Pincurchin","Shellos","Gastrodon","Shellder","Alomomola","Dratini","Delibird","Cubchoo","Snorunt","Cetoddle","Cetitan","Rufflet","Braviary","Deino","Zweilous","Arctibax","Gimmighoul (Chest Form)"]
    northPA2 =["Spidops","Lokix","Jumpluff","Houndoom","Kricketot","Vivillon","Vespiquen","Chansey","Blissey","Floatzel","Clodsire","Arboliva","Luxray","Grumpig","Mismagius","Hariyama","Copperajah","Gabite","Naclstack","Floette","Dugtrio","Camerupt","Bronzong","Primeape","Lucario","Foongus","Amoonguss","Arcanine","Ursaring","Gogoat","Honchkrow","Indeedee","Fomantis","Lurantis","Venonat","Venomoth","Scyther","Heracross","Espathra","Tinkatuff","Sableye","Falinks","Hawlucha","Noibat","Noivern","Drakloak","Glimmet","Houndstone","Oranguru","Passimian","Dratini","Rufflet","Braviary","Bisharp","Deino","Zweilous"]
    northPA3 =["Jumpluff","Pawmo","Gumshoos","Sunflora","Vivillon","Combee","Vespiquen","Chansey","Blissey","Floatzel","Golduck","Dolliv","Petilil","Lilligant","Copperajah","Naclstack","Magikarp","Barraskewda","Floette","Florges","Bellibolt","Umbreon","Dedenne","Gogoat","Fomantis","Lurantis","Wugtrio","Sableye","Hawlucha","Drakloak","Greavard","Houndstone","Eiscue","Pincurchin","Alomomola","Delibird","Cubchoo","Beartic","Cetoddle","Rufflet","Deino","Arctibax"]
    northSea =["Floatzel","Pelipper","Gyarados","Barraskewda","Kilowattrel","Finizen","Orthworm","Eiscue","Shellder","Cloyster","Qwilfish","Finneon","Lumineon","Alomomola","Skrelp","Dragalge","Clauncher","Clawitzer","Tynamo","Eelektrik","Bergmite","Avalugg"]
    southPA1 =["Lechonk","Oinkologne","Tarountula","Spidops","Hoppip","Fletchling","Pawmi","Houndour","Scatterbug","Spewpa","Surskit","Paldean Wooper","Ralts","Fidough","Dachsbun","Oricorio (Pom-Pom Style)","Wingull","Pelipper","Charcadet","Deerling","Sawsbuck","Toedscool"]
    southPA2 =["Hoppip","Fletchling","Yungoos","Skwovet","Sunkern","Kricketot","Combee","Happiny","Azurill","Buizel","Paldean Wooper","Psyduck","Chewtle","Chewtle","Igglybuff","Jigglypuff","Drowzee","Gastly","Pichu","Pikachu","Fidough","Dachsbun","Smoliv","Bonsly","Rockruff","Starly","Staravia","Staraptor","Mareep","Petilil","Lilligant","Applin","Nacli","Arrokuda","Basculin","Diglett","Bronzor","Charcadet","Barboach","Tadbulb","Eevee","Maschiff","Mabosstiff","Shroodle","Tinkatink","Rufflet","Gimmighoul (Chest Form)"]
    southPA3 =["Nymble","Pawmi","Pawmo","Yungoos","Rookidee","Happiny","Buizel","Paldean Wooper","Psyduck","Chewtle","Drowzee","Gastly","Fidough","Dachsbun","Slakoth","Rockruff","Shinx","Oricorio (Baile Style)","Spoink","Misdreavus","Makuhita","Crabrawler","Nacli","Arrokuda","Basculin","Gulpin","Bronzor","Charcadet","Barboach","Goomy","Growlithe","Seviper","Swablu","Skiddo","Murkrow","Toedscool","Klawf","Pineco","Flittle","Mudbray","Tinkatink","Shuppet","Larvitar","Rufflet","Gimmighoul (Chest Form)"]
    southPA4 =["Lechonk","Tarountula","Fletchinder","Pawmo","Houndour","Yungoos","Skwovet","Spewpa","Combee","Masquerain","Buizel","Paldean Wooper","Psyduck","Chewtle","Chewtle","Drowzee","Gastly","Pikachu","Bounsweet","Rockruff","Starly","Staravia","Staraptor","Petilil","Lilligant","Applin","Misdreavus","Makuhita","Phanpy","Nacli","Magikarp","Arrokuda","Basculin","Drifloon","Drifblim","Flabebe","Meditite","Medicham","Riolu","Lucario","Charcadet","Barboach","Tadbulb","Goomy","Wattrel","Dunsparce","Deerling","Sawsbuck","Maschiff","Mabosstiff","Toxel","Toxtricity","Pachirisu","Shroodle","Swablu","Skiddo","Murkrow","Toedscool","Pineco","Scyther","Flittle","Espathra","Mudbray","Tinkatink","Hatenna","Dreepy","Komala","Shellos","Gastrodon","Tynamo","Eelektrik","Glalie","Rufflet"]
    southPA5 =["Lechonk","Oinkologne","Tarountula","Spidops","Skiploom","Fletchinder","Pawmo","Yungoos","Gumshoos","Spewpa","Rookidee","Corvisquire","Surskit","Masquerain","Buizel","Paldean Wooper","Clodsire","Psyduck","Chewtle","Chewtle","Drednaw","Gastly","Slakoth","Vigoroth","Bounsweet","Rockruff","Luxio","Shroomish","Misdreavus","Makuhita","Nacli","Magikarp","Arrokuda","Basculin","Drifloon","Flabebe","Floette","Axew","Fraxure","Mankey","Charcadet","Barboach","Tadbulb","Goomy","Croagunk","Toxicroak","Deerling","Sawsbuck","Pachirisu","Stantler","Teddiursa","Zangoose","Seviper","Swablu","Skiddo","Litleo","Pyroar","Stunky","Murkrow","Toedscool","Fomantis","Lurantis","Flittle","Mudbray","Bagon","Wiglett","Dreepy","Larvitar","Pincurchin","Sandygast","Palossand","Slowpoke","Shellos","Gastrodon","Froslass","Pawniard"]
    southPA6 =["Lokix","Jumpluff","Pawmo","Yungoos","Gumshoos","Greedent","Sunflora","Vivillon","Vespiquen","Chansey","Buizel","Floatzel","Clodsire","Psyduck","Drednaw","Gallade","Fidough","Dachsbun","Arboliva","Lycanroc","Flaaffy","Ampharos","Petilil","Lilligant","Misdreavus","Mismagius","Hariyama","Salandit","Salazzle","Donphan","Copperajah","Gible","Gabite","Naclstack","Arrokuda","Barraskewda","Drifblim","Floette","Diglett","Dugtrio","Bronzong","Meditite","Medicham","Lucario","Whiscash","Goomy","Wattrel","Umbreon","Sylveon","Toxel","Toxtricity","Altaria","Skiddo","Murkrow","Honchkrow","Gothorita","Gothitelle","Sinistea","Scovillain","Flittle","Espathra","Mudbray","Mudsdale","Shelgon","Hattrem","Bombirdier","Sableye","Banette","Glimmet","Houndstone","Larvitar","Pupitar","Shellos","Gastrodon","Tynamo","Eelektrik","Dratini","Rufflet","Deino","Gimmighoul (Chest Form)"]
    southSea =["Buizel","Wingull","Pelipper","Magikarp","Gyarados","Finizen","Orthworm","Shellder","Qwilfish","Luvdisc","Bruxish","Skrelp","Clawitzer","Tynamo","Eelektrik"]
    tagThick =["Lechonk","Oinkologne","Tarountula","Spidops","Pawmo","Gumshoos","Greedent","Sunflora","Clodsire","Dolliv","Arboliva","Lycanroc","Applin","Misdreavus","Dugtrio","Charcadet","Barboach","Whiscash","Bellibolt","Goomy","Shroodle","Grafaiai","Foongus","Gogoat","Zorua","Zoroark","Murkrow","Mimikyu","Fomantis","Lurantis","Scovillain","Venonat","Venomoth","Pineco","Flittle","Espathra","Silicobra","Hattrem","Impidimp","Morgrem","Orthworm","Oranguru","Passimian","Komala","Larvitar","Snom","Rufflet","Pawniard"]
    casseLake =["Oinkologne","Tarountula","Spidops","Azumarill","Golduck","Drednaw","Raichu","Vigoroth","Slaking","Arboliva","Sudowoodo","Starly","Staravia","Staraptor","Petilil","Lilligant","Mismagius","Copperajah","Naclstack","Pelipper","Swalot","Bronzong","Sliggoo","Croagunk","Toxicroak","Mabosstiff","Amoonguss","Altaria","Gogoat","Skuntank","Zoroark","Honchkrow","Brambleghast","Toedscool","Toedscruel","Tropius","Lurantis","Scovillain","Venomoth","Forretress","Scyther","Heracross","Flittle","Hawlucha","Drakloak","Houndstone","Oranguru","Passimian","Palossand","Slowpoke","Slowbro","Gastrodon","Flamigo","Dratini","Dragonair","Frosmoth","Cetitan","Veluza","Dondozo","Tatsugiri"]
    glaseado =["Pawmo","Vespiquen","Chansey","Clodsire","Psyduck","Kirlia","Gardevoir","Gallade","Haunter","Vigoroth","Lycanroc","Grumpig","Misdreavus","Mismagius","Crabrawler","Crabominable","Salandit","Copperajah","Gabite","Naclstack","Barraskewda","Drifloon","Drifblim","Dugtrio","Bronzong","Axew","Fraxure","Whiscash","Goomy","Vaporeon","Flareon","Espeon","Umbreon","Glaceon","Magneton","Ursaring","Gogoat","Litleo","Pyroar","Sneasel","Murkrow","Honchkrow","Gothita","Mimikyu","Klefki","Toedscool","Fomantis","Lurantis","Flittle","Espathra","Mudbray","Mudsdale","Tinkatuff","Hattrem","Wugtrio","Revavroom","Sableye","Banette","Hawlucha","Drakloak","Glimmet","Greavard","Houndstone","Larvitar","Pincurchin","Snom","Frosmoth","Snover","Delibird","Cubchoo","Beartic","Snorunt","Cryogonal","Cetoddle","Cetitan","Bergmite","Avalugg","Rufflet","Zweilous","Frigibax"]
    pkmnLeague =["Lechonk","Oinkologne","Tarountula","Spidops","Tandemaus","Fidough","Dachsbun","Makuhita"]
    areaZero =["Jumpluff","Talonflame","Corviknight","Masquerain","Hypno","Lycanroc","Donphan","Garganacl","Camerupt","Medicham","Bellibolt","Dunsparce","Girafarig","Farigiraf","Swablu","Sneasel","Weavile","Venomoth","Volcarona","Glimmora","Flamigo","Braviary","Bisharp","Great Tusk","Scream Tail","Brute Bonnet","Flutter Mane","Slither Wing","Sandy Shocks","Iron Treads","Iron Bundle","Iron Hands","Iron Jugulis","Iron Moth","Iron Thorns","Roaring Moon","Iron Valiant"]
    pocoPath =["Lechonk","Tarountula","Skwovet"]

    ## Dict region index
    regionList = {
        '0':westPA1,
        '1':westPA2,
        '2':westPA3,
        '3':asado,
        '4':westSea,
        '5':eastPA1,
        '6':eastPA2,
        '7':eastPA3,
        '8':eastSea,
        '9':northPA1,
        '10':northPA2,
        '11':northPA3,
        '12':northSea,
        '13':southPA1,
        '14':southPA2,
        '15':southPA3,
        '16':southPA4,
        '17':southPA5,
        '18':southPA6,
        '19':southSea,
        '20':tagThick,
        '21':casseLake,
        '22':glaseado,
        '23':pkmnLeague,
        '24':areaZero,
        '25':pocoPath
    }
    count = 0
    while count < encounterNo:
        pokemon = random.choice((regionList[regionSelect]))
        count = count + 1
        print(pokemon)
    input("Press Enter to roll again.")

