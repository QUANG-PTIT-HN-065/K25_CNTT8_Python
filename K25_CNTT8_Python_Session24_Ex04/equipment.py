from abc import ABC, abstractmethod


class Equipment(ABC):
    """
    Lớp trừu tượng đại diện cho trang bị.
    """

    @abstractmethod
    def calculate_total_damage(self):
        """Tính sát thương tổng."""
        pass


class Weapon(Equipment):
    """
    Vũ khí vật lý.
    """

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        """Tính sát thương của Weapon."""
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        """
        So sánh hai trang bị.
        """
        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return False

        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        """
        Dung hợp hai vũ khí.
        """
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return None

        return Weapon(
            name=f"Fusion({self.name} + {other.name})",
            base_damage=self.base_damage + other.base_damage,
            upgrade_level=self.upgrade_level + other.upgrade_level,
        )


class MagicMixin:
    """
    Mixin bổ sung thuộc tính phép thuật.
    """

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} phát sáng bởi ma thuật!")


class MagicSword(Weapon, MagicMixin):
    """
    Kiếm ma thuật.
    """

    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        """Tính sát thương tổng của kiếm ma thuật."""
        return self.base_damage + self.upgrade_level * 10 + self.magic_power
