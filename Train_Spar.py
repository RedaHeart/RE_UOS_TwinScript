weap = 0x13F6 ##Use Inspect Entities to get weapon ID

def equip():
    for w in Player.Backpack.Contains:            ##  Cycles your backpack for any item with ID = weap (set at beggining)
       if w.ItemID == weap:                       ##  return as Serial for the first one it founds
         return w.Serial                          ##  it needs to get a serial, because EquipItem needs a Serial to equip
                                                  ##  doesn't work for IDs

while True:            
    if not Player.CheckLayer("RightHand"):        ##  Check if Character doesnt have anything on his Right Hand, meaning it doesn't have a weapon equiped
      Player.EquipItem(equip())                   ##  Equip the weapon returned on previous function that is now called equip()  
      Misc.Pause(1000)
      