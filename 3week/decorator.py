from abc import ABC, abstractmethod
# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
        
#         self.stats = {
#             "HP": 128,
#             "MP": 42,
#             "SP": 100,
            
#             "Strength": 15,
#             "Perception": 4,
#             "Endurance": 8,
#             "Charisma": 2,
#             "Intelligence": 3,
#             "Agility": 8,
#             "Luck": 1
#         } 
        
#     def get_positive_effects(self):
#         return self.positive_effects.copy()
    
#     def get_negative_effects(self):
#         return self.negative_effects.copy()
    
#     def get_stats(self):
#         return self.stats.copy()


class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base
    
    @abstractmethod
    def get_stats(self):
        pass
    
    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects
    
    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects
    

class AbstractPositive(AbstractEffect):

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):

    def __init__(self, base):
        self.base = base
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        stats["HP"] += 50
        return stats.copy()

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]
    

class Blessing(AbstractPositive):

    def __init__(self, base):
        self.base = base
        
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats.copy()

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


class AbstractNegative(AbstractEffect):
    
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Weakness(AbstractNegative):

    def __init__(self, base):
        self.base = base
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats.copy()

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class EvilEye(AbstractNegative):

    def __init__(self, base):
        self.base = base
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats.copy()

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]


class Curse(AbstractNegative):

    def __init__(self, base):
        self.base = base
    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats.copy()
        
    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]

