import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chips_db import print_all_chips, print_chip_card, search_chips
from utils import make_backup, validate_dump_file

VERSION = "Alpha-v.0.0.1.1 (build date: 2026-08-15)"


def main():
    print("=== MTK-TOOL Initiated ===")
    print(VERSION)

    try:
        while True:
            print("\n=== Main menu ===")
            print("0 - exit")
            print("1 - search for a processor")
            print("2 - show all processors in the local database")
            print("3 - make a dump")
            print("4 - check the dump's directory")
            choice = input("Choose from 0 to 4: ").strip()

            if choice == "1":
                user_input = input(
                    "\nEnter the HWID code, name or the model of the processor (for example: 717, MT6761, P22, G95): "
                ).strip()
                found_chips = search_chips(user_input)

                if not found_chips:
                    print(f"\n No results found for: {user_input}")
                else:
                    print(f"\n Matches found: {len(found_chips)}")
                    for hw_code, info in found_chips.items():
                        print_chip_card(hw_code, info)
            elif choice == "2":
                print_all_chips()
            elif choice == "3":
                make_backup()
            elif choice == "4":
                raw_path = input("Input the directory of the dump/backup: ").strip(
                    "'\" "
                )

                if raw_path:
                    validate_dump_file(raw_path)
                else:
                    print("The directory can't be empty!")
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("\nInvalid choice! Please select a number from 0 to 4.")

    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting MTK-TOOL....")
        sys.exit(0)


if __name__ == "__main__":
    main()
