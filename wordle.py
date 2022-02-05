import copy
import numpy as np


class Wordle:
    def __init__(self, filename: str = "data/english_dict5.txt", verbose: bool = True):
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

    def infer_rules(self, word, target):
        for i, letter in enumerate(word):
            if word[i] == target[i]:
                self.add_hard_constraint(word[i], i)
            elif word[i] in target:
                self.add_soft_constraint(word[i])
            else:
                self.add_negative_constraint(word[i])

    def optimize(self):
        if len(self.data) > 500:
            dictionnary = self.dict[::10]
            data = self.data[::5]
        if len(self.data) > 200:
            dictionnary = self.dict[::5]
            data = self.data[::5]
        else:
            dictionnary = self.dict
            data = self.data
        values = [[] for word in dictionnary]
        cWordle = Wordle(self.filename)
        for j, target in enumerate(data):
            if (j % 10 == 0):
                print("Currently", j/len(data), "% done")
            for i, word in enumerate(dictionnary):
                cWordle.data = copy.copy(data)
                cWordle.hard_constraints = copy.copy(self.hard_constraints)
                cWordle.soft_constraints = copy.copy(self.soft_constraints)
                cWordle.negative_constraints = copy.copy(
                    self.negative_constraints)
                cWordle.infer_rules(word, target)
                cWordle.apply_constraints(verbose=False)
                values[i].append(len(cWordle.data))
        return sorted([(dictionnary[i], np.mean(values[i])) for i in range(len(values))], key=lambda x: x[1])[0:10]

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
            if constraint != '':
                self.data = [
                    word for word in self.data if word[ind] == constraint]
                if verbose:
                    print("Mots restants:", len(self.data))

    def apply_soft_constraints(self, verbose: bool = True):
        for constraint in self.soft_constraints:
            # if constraint in self.hard_constraints:
            #     self.data = [
            #         word for word in self.data if word.count(constraint) >= 2]
            #     if verbose:
            #         print("Mots restants:", len(self.data))
            # else:
            self.data = [
                word for word in self.data if word.count(constraint)]
            if verbose:
                print("Mots restants:", len(self.data))

    def apply_negative_constraints(self, verbose: bool = True):
        for constraint in self.negative_constraints:
            if constraint != '':
                self.data = [
                    word for word in self.data if not word.count(constraint)]
                if verbose:
                    print("Mots restants:", len(self.data))

    def apply_constraints(self, verbose: bool = True):
        self.apply_hard_constraints(verbose)
        self.apply_soft_constraints(verbose)
        self.apply_negative_constraints(verbose)
