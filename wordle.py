import copy


class Wordle:
    def __init__(self, filename: str, verbose: bool = True):
        """
        Standard constructor for the Wordle class.

        Args:
            filename (str): The name of the file containing the dictionary.
            verbose (bool, optional): Log if True. Defaults to True.
        """
        self.hard_constraints = ['']*5
        self.soft_constraints = []
        self.negative_constraints = []
        self.filename = filename

        self.load(verbose)
        self.data = copy.deepcopy(self.dict)

    def get_data(self):
        return self.data

    def reset(self):
        """ Reset the plausible words. """
        self.data = self.dict

    def load(self, verbose: bool = True):
        """
        Loads the dictionary in self.dict

        Args:
            verbose (bool, optional): Log if True. Defaults to True.
        """
        f = open(self.filename, "r")
        self.dict = f.read().split("\n")
        if verbose:
            print("Mots chargés:", len(self.dict))

    def add_hard_constraint(self, constraint: str, index: int):
        self.hard_constraints[index] = constraint

    def add_soft_constraint(self, constraint: str):
        self.soft_constraints.append(constraint)

    def add_negative_constraint(self, constraint: str):
        self.negative_constraints.append(constraint)

    def apply_hard_constraints(self, verbose: bool = True):
        for ind, constraint in enumerate(self.hard_constraints):
            print(ind, constraint)
            if constraint != '':
                self.data = [
                    word for word in self.data if word[ind] == constraint]
                if verbose:
                    print("Mots restants:", len(self.data))

    def apply_soft_constraints(self, verbose: bool = True):
        for constraint in self.soft_constraints:
            print(constraint)
            if constraint in self.hard_constraints:
                self.data = [
                    word for word in self.data if word.count(constraint) >= 2]
                if verbose:
                    print("Mots restants:", len(self.data))
            else:
                self.data = [
                    word for word in self.data if word.count(constraint)]
                if verbose:
                    print("Mots restants:", len(self.data))

    def apply_negative_constraints(self, verbose: bool = True):
        for constraint in self.negative_constraints:
            print(constraint)
            if constraint != '':
                self.data = [
                    word for word in self.data if not word.count(constraint)]
                if verbose:
                    print("Mots restants:", len(self.data))
