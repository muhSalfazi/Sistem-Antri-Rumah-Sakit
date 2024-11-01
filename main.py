# main.py
from interface import proses_input
from antrian import AntrianRumahSakit

def main():
    antrian = AntrianRumahSakit()
    proses_input(antrian)

if __name__ == "__main__":
    main()
