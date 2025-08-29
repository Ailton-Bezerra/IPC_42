from person import Person

def test_person() -> None:
    p = Person("Ailton", 24)
    assert p.name == "Ailton"
    assert p.age == 24
    p.birthday()
    assert p.age == 25
    p.birthday()
    assert p.age == 26
