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
7/17/2025 8:35 PM - started working on tags based generator again.
7/17/2025 10:33 PM - made partial progress on tags based generator. will resumes on return.
    """

class SSS(object):
    def __init__(self, ruleSet,  Init: str, n: int, SSSSize: int = 10, NetSize: int = 300):
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
                before, after = rule.split("->")
                rule_dict[before.strip()] = after.strip()
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
        letter_order = {}
        count = 0
        counts = {}
        nested = []
        global_index = 1
        for c in world: 
            if c not in letter_order:
                letter_order[c] = count
                count += 1
            type_idx = letter_order[c]
            counts.setdefault(c, global_index)
            counts[c] += 1
            nested.append([type_idx, global_index])
            global_index += 1

#  ################################################
        # currently working on the code below

        # out = [row[:] for row in nested]
        # length = len(nested)
        # used_indexes = set()
        # for pattern, replacement in self.ruleSet.items():
        #     pattern_list = [int(ch) for ch in pattern]
        #     replacement_list = [int(ch) for ch in replacement]
        #     plen = len(pattern_list)

        #     for start in range(length - plen + 1):
        #         match = True
        #         for i in range(plen):
        #             if nested[start + i][0] != pattern_list[i]:
        #                 match = False
        #                 break
        #             if (start + i) in used_indexes:
        #                 match = False
        #                 break
        #         if match:
        #             for i in range(plen):
        #                 out[start + i][0] = replacement_list[i]

        #                 out[start + i][1] = start + i + 7
        #                 used_indexes.add(start + i)
        #             break
            
        return nested

# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet)
# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet['A'])
SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGen()
print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGenNested())