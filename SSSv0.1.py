"""
in order to do have the program run, you need to enter for following string of code:
the rulsets, initial string, and number of iterations. currenlty SSSSize and NetSize currently do nothing.

Example:
SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGen()
will output:

AB
ABAB
AABB
ABAABB
AABABB
ABAABABB
AABABABB
ABAABABABB
AABABABABB
ABAABABABABB
AABABABABABB
ABAABABABABABB
AABABABABABABB
ABAABABABABABABB
AABABABABABABABB
ABAABABABABABABABB
AABABABABABABABABB
ABAABABABABABABABABB
AABABABABABABABABABB
ABAABABABABABABABABABB

7/10/2025 8:00 PM - started making the letter generator.
7/10/2025 8:52 PM - finished the letter generator.
7/10/2025 9:55 PM - began refining code
7/11/2025 10:00 PM - finished refining code
7/15/2025 8:00 PM - started making tags based generator
7/15/2025 10:22 PM - stopped working on tags based generator. will resumes on return.
    """

class SSS(object):
    def __init__(self, ruleSet,  Init: str, n: int, SSSSize: int = 100, NetSize: int = 300):
        self.ruleSet = self._transform(ruleSet)
        self.Init= Init
        self.n = n
        self.SSSSize = SSSSize
        self.NetSize = NetSize
        self.world = self.Init

    def __str__(self) -> str:
        return f"{self.world}"
    def  __repr__(self) -> str:
        return f"SSS('{self.world}')"
    def _transform(self, rules: list) -> dict:
        rule_dict = {}
        for rule in rules:
            if "->" in rule:
                src, dst = rule.split("->")
                rule_dict[src.strip()] = dst.strip()
        return rule_dict

    def worldGen(self):
        print(self.world)
        for i in range(self.n):
            for x, y in self.ruleSet.items():
                if x in self.world:
                    self.world = self.world.replace(x,y,1)
                    print(self.world)
        pass
    def worldGenNested(self):
        world = self.Init
        print(f"{world}")
        print(self._nested_map(world))
        for i in range(self.n):
            for x, y in self.ruleSet.items():
                if x in world:
                    world = world.replace(x, y, 1)
                    print(f"{world}")
                    print(self._nested_map(world))
        return

    def _nested_map(self, world: str):
        letter_order = []
        counts = {}
        nested = []
        global_index = 1
        for c in world: 
            if c not in letter_order:
                letter_order.append(c)
            type_idx = letter_order.index(c)
            counts.setdefault(c, global_index)
            counts[c] += 1
            nested.append([type_idx, global_index])
            # for x in nested:
            #     if nested[][1]:

            global_index += 1
        return nested

# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet)
# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet['A'])
SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGen()
print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGenNested())