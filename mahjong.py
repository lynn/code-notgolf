import sys

starts = set("🀇🀈🀉🀊🀋🀌🀍🀐🀑🀒🀓🀔🀕🀖🀙🀚🀛🀜🀝🀞🀟")
orphans = set("🀀🀁🀂🀃🀄🀅🀆🀇🀏🀐🀘🀙🀡")


def removals(hand):
    """Yield ways to remove a meld from a hand."""
    for c in set(hand):
        if c in starts:
            # Try removing a sequence:
            d = chr(ord(c) + 1)
            e = chr(ord(c) + 2)
            if d in hand and e in hand:
                yield hand.replace(c, "", 1).replace(d, "", 1).replace(e, "", 1)
        # Try removing a triplet:
        if hand.count(c) >= 3:
            yield hand.replace(c, "", 3)


def is_melds_and_a_pair(hand):
    assert len(hand) in {14, 11, 8, 5, 2}
    if len(hand) == 2:
        return hand[0] == hand[1]
    else:
        return any(is_melds_and_a_pair(r) for r in removals(hand))


for hand in sys.argv[1:]:
    if (
        is_melds_and_a_pair(hand)
        or [hand.count(c) for c in set(hand)] == [2] * 7
        or set(hand) == orphans
    ):
        print(hand)
