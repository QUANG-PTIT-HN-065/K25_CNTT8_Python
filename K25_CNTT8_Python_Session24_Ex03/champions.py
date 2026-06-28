from abc import ABC, abstractmethod

class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Tính sát thương kỹ năng.
        """
        pass

    def get_combat_power(self):
        """
        Tính chiến lực của quân cờ.
        """
        return self.base_hp + self.calculate_skill_damage() * 1.5

    def __add__(self, other):
        """
        Cộng chiến lực giữa hai quân cờ hoặc với số.
        """
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """
        Hỗ trợ sum() hoặc cộng từ số 0.
        """
        return self.__add__(other)

    def __gt__(self, other):
        """
        So sánh chiến lực giữa hai quân cờ.
        """
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented


class Warrior(Champion):
    """
    Lớp Chiến binh.
    """

    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        """
        Sát thương = ATK * 2 + Armor
        """
        return self.base_atk * 2 + self.shield_bonus

    def __str__(self):
        return (
            f"{self.champion_id:<7} | {self.name:<20} | Warrior | "
            f"{self.base_hp:<5} | {self.base_atk:<5} | "
            f"Armor: {self.shield_bonus:<5} | "
            f"{self.get_combat_power():.0f}"
        )


class Mage(Champion):
    """
    Lớp Pháp sư.
    """

    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        """
        Sát thương = ATK * Ability Power
        """
        return self.base_atk * self.ability_power

    def __str__(self):
        return (
            f"{self.champion_id:<7} | {self.name:<20} | Mage     | "
            f"{self.base_hp:<5} | {self.base_atk:<5} | "
            f"Mana: {self.ability_power:<6} | "
            f"{self.get_combat_power():.0f}"
        )
