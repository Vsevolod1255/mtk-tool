import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chips_db import print_all_chips, print_chip_card, search_chips
from utils import make_backup, validate_dump_file


def main():
    print("=== MTK-TOOL Initiated ===")
    print("Alpha-v.0.0.1 (a build from 14.08.2026)")

    while True:
        print("The main menu")
        print("0 - exit")
        print("1 - find a processor")
        print("2 - show all processors in the local database")
        print("3 - make a dump")
        print("4 - check the dump's directory")
        choice = input("Выберите действие (0-4) ")

        if choice == "1":
            user_input = input(
                "\nWrite the HWID code, name or the model of the processor (for example: 717, MT6761, P22, G95):"
            )
            found_chips = search_chips(user_input)

            if not found_chips:
                print(f"\n Nothing was found under the input: {'user_input'}")
            else:
                print(f"\n Found exact data: {len(found_chips)}")
                for hw_code, info in found_chips.items():
                    print_chip_card(hw_code, info)
        elif choice == "2":
            print_all_chips()
        elif choice == "0":
            print("Exiting...")
            break
        elif choice == "3":
            make_backup()
        elif choice == "4":
            raw_path = input("Input the directory of the dump/backup:").strip("'\" ")

            if raw_path:
                validate_dump_file(raw_path)
            else:
                print("The directory mustn't be empty!")


if __name__ == "__main__":
    main()
