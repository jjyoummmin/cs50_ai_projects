from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

people = {"A":(AKnight, AKnave), 
        "B":(BKnight, BKnave),
        "C":(CKnight,CKnave)}

def player(person):
    knight, knave = people[person]
    return And( Or(knight, knave), Not(And(knight, knave)))

def speaks(person, speech):
    knight, knave = people[person]
    return And(Implication(knight, speech), Implication(knave, Not(speech)))

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    player("A"),
    speaks("A", And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    player("A"),
    player("B"),
    speaks("A", And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    player("A"),
    player("B"),
    speaks("A", Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    speaks("B", Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    player("A"),
    player("B"),
    player("C"),
    speaks("A", Or(AKnight, AKnave)),
    speaks("B", speaks("A", AKnave)),
    speaks("B", CKnave),
    speaks("C", AKnight)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
