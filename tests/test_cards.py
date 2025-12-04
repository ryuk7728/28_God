from src.cards import Cards

def test_identity():
    c1 = Cards("Hearts","Eight",0,1)
    c2 = Cards("Spades","Ace",1,5)
    c3 = Cards("Clubs","Nine",2,6)
    c4 = Cards("Diamonds","Jack",3,7)
    assert c1.identity() == "Eight of Hearts"
    assert c2.identity() == "Ace of Spades"
    assert c3.identity() == "Nine of Clubs"
    assert c4.identity() == "Jack of Diamonds"

def test_packOf28():
    pack = Cards.packOf28()
    assert len(pack)==32
    assert pack[0].points==0 and pack[0].order==0 #Seven of Hearts confirmation
    assert pack[11].points==0 and pack[11].order==3 #King of Clubs
    assert pack[18].points==0 and pack[18].order==2 #Queen of Diamonds
    assert pack[31].points==3 and pack[31].order==7 #Jack of Spades
