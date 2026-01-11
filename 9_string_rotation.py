class StringRotation:
    def is_rotation(self, s1, s2):
        if len(s1) != len(s2):
            return False

        return s2 in (s1 + s1)


# Runtime input
obj = StringRotation()
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("Rotation" if obj.is_rotation(s1, s2) else "Not Rotation")
