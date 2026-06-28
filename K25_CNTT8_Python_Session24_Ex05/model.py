from abc import ABC, abstractmethod


class Companion(ABC):
    """
    Lớp trừu tượng đại diện cho sinh vật đồng hành.
    """

    def __init__(self, name, level=1, **kwargs):
        self.name = name
        self.level = level
        super().__init__()

    @abstractmethod
    def unleash_skill(self):
        """
        Kỹ năng đặc trưng của sinh vật.
        """
        pass

    def __add__(self, other):
        """
        Lai tạo hai sinh vật cùng loại.
        """
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")

        if isinstance(self, Dragon):
            return Dragon(
                name=f"{self.name} {other.name}",
                level=self.level + 1,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed,
            )

        elif isinstance(self, Pet):
            return Pet(
                name=f"{self.name} {other.name}",
                level=self.level + 1,
                bonus_atk=self.bonus_atk + other.bonus_atk,
            )

        elif isinstance(self, Mount):
            return Mount(
                name=f"{self.name} {other.name}",
                level=self.level + 1,
                bonus_speed=self.bonus_speed + other.bonus_speed,
            )


class Pet(Companion):
    """
    Thú cưng hỗ trợ chiến đấu.
    """

    def __init__(self, name, bonus_atk, level=1, **kwargs):
        self.bonus_atk = bonus_atk
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(f"{self.name}: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")


class Mount(Companion):
    """
    Thú cưỡi hỗ trợ di chuyển.
    """

    def __init__(self, name, bonus_speed, level=1, **kwargs):
        self.bonus_speed = bonus_speed
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(f"{self.name}: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")


class Dragon(Pet, Mount):
    """
    Rồng vừa là Pet vừa là Mount.
    """

    def __init__(self, name, bonus_atk, bonus_speed, level=1):
        super().__init__(
            name=name, level=level, bonus_atk=bonus_atk, bonus_speed=bonus_speed
        )

    def unleash_skill(self):
        print(f"{self.name} thị uy:")
        print(f"- Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")
        print(f"- Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")
