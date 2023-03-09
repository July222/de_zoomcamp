import pandas
import sys

print(f"Pandas version is {pandas.__version__}")

print(sys.argv)

day = sys.argv[1]

print(f"Job finished succesfully for day {day}")
