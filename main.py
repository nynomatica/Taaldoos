from Taaldoos.jongens_naam_generator import jongens_naam_generator
from Taaldoos.stads_naam_generator import stads_naam_generator
from Taaldoos.vrouw_naam_generator import vrouw_naam_generator

def test_generators():
    naam_vrouw = vrouw_naam_generator()
    naam_man = jongens_naam_generator()
    naam_stad = stads_naam_generator()
    print(f"Testing Generators")
    print(f"    vrouwen naam = {naam_vrouw}")
    print(f"    mannen naam = {naam_man}")
    print(f"    stads naam = {naam_stad}")


if __name__ == '__main__':
    test_generators()
