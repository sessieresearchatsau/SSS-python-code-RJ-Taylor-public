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
7/18/2025 8:00 PM - started working on tags based generator again.
7/28/2025 11:51 PM - finally made the tags based generator work (to an extent).
    """

class SSS(object):
    def __init__(self, ruleSet,  Init: str, n: int, SSSSize: int = 10, NetSize: int = 300):
        self.ruleSet = self._transform(ruleSet)
        self.Init= Init
        self.n = n
        self.SSSSize = SSSSize
        self.NetSize = NetSize
        self.world = self.Init
        self.letter_order = {}
        self.global_index = 1
        self.count = 0

        for c in self.world: 
            if c not in self.letter_order:
                self.letter_order[c] = self.count
                self.count += 1
        self.converted_ruleSet = {}
        self.before = []
        self.after = []
        self.nested = []


    def __str__(self) -> str:
        return f"{self.world}"
    def  __repr__(self) -> str:
        return f"SSS('{self.world}')"
    def _count(self, entry):
        self.global_index += 1
        return entry
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

        print(self._nested_map(world))
        stop = 0
        while True:
            for x in self.converted_ruleSet.items():
                for z in range(len(self.before)):
                    for y in range(0, len(self.nested), len(self.before[z])):
                # Get the first element of each sublist in the current slice
                        if stop == self.n:
                            return None
                        if len(self.before[z]) <= len(self.nested):
                            slice_firsts = [str(sublist[0]) for sublist in self.nested[y:y+len(self.before[z])]]
                            joined = ''.join(slice_firsts)
                            if joined == self.before[z]:
                                # print(f"Found at index {y}: {slice_firsts}")
                                # print(f"Location: {self.nested[z:z+len(self.before[z])]}")
                                self.nested[y:y+len(self.before[z])] = [[int(self.after[z][sublist]), self._count(self.global_index)] for sublist in range(len(self.after[z]))]
                                # print(f"{self.nested}\n")
                                stop += 1
                            
                        else:
                            print(f"no action taken. len used was {len(self.before[z])}")

    def _nested_map(self, world: str):
        # list of converted rulets
        for entry in sorted(self.ruleSet.keys(), reverse=True):
            self.before.append("".join(str(self.letter_order[g]) for g in entry)) if "".join(str(self.letter_order[g]) for g in entry) not in self.before else None
            self.after.append("".join(str(self.letter_order[g]) for g in self.ruleSet[entry])) if "".join(str(self.letter_order[g]) for g in self.ruleSet[entry]) not in self.after else None
        for key, value in zip(self.before, self.after):
            self.converted_ruleSet[key] = value       
        for c in world: 
            if c not in self.letter_order:
                self.letter_order[c] = self.count
                self.count += 1
            self.nested.append([self.letter_order[c], self._count(self.global_index)])
        return self.nested


# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet)
# print(SSS(["ABA->AAB", "A->ABA"], "AB", 10).ruleSet['A'])
SSS(["ABA->AAB", "A->ABA"], "AB", 10).worldGen()
SSS(["A->ABA", "ABA->AAB",], "AB", 10).worldGenNested()