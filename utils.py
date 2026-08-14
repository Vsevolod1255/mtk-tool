import os

from chips_db import search_chips


def make_backup():
    folder_name = input(
        "Write the name of the folder which will contain the dump:"
    ).strip()

    if not folder_name:
        print("Error: a folder can't exist with an empty name!")
        return

    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' has been successfully created!!")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists!")
    except OSError as err:
        print(
            f" Couldn't create the folder (most likely no access or wrong symbols in the name): {err}"
        )

    answer = (
        input("Do you want to write the processor's data in this folder? (y/n): ")
        .strip()
        .lower()
    )
    if answer == "y":
        query = input("Input the NWID code or the name of the processor:")
        found_chips = search_chips(query)

        if not found_chips:
            print("The processor couldn't be found so the folder is empty.")
        else:
            hw_code, info = next(iter(found_chips.items()))

            file_path = os.path.join(folder_name, "info.txt")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("=== BROM BACKUP INFO ===\n")
                f.write(f"HW_CODE:           {hw_code}\n")
                f.write(f"Official Name:     {info.get('official_name', 'N/A')}\n")
                f.write(f"Market Name:       {info.get('name', 'N/A')}\n")
                f.write(f"BROM Payload Addr: {info.get('brom_payload_addr', 'N/A')}\n")
                f.write(f"DA Payload Addr:   {info.get('da_payload_addr', 'N/A')}\n")
                f.write(f"Watchdog:          {info.get('watchdog', 'N/A')}\n")

            print(f"'info.txt' has been saved in '{folder_name}'!")


def create_dump_folder():
    folder_name = input(
        "Write the dump's folder name (it mustn't coincide with mtk-tool's directories): "
    ).strip()

    if not folder_name:
        print("Error! The name of the folder can't be empty! ")
        return None

    os.makedirs(folder_name, exist_ok=True)
    print("The folder has been created!")
    return folder_name


def validate_dump_file(file_path: str) -> bool:

    if not os.path.exists(file_path):
        print(f"Error! Directory '{file_path}' doesn't exist!")
        return False

    if not os.path.isfile(file_path):
        print(f"Error! '{file_path}' is a folder not a dump!")
        return False

    try:
        file_size_bytes = os.path.getsize(file_path)

        if file_size_bytes == 0:
            print(f"Warning! File '{file_path}' is empty (0 bites)!")
            return False

        file_size_mb = file_size_bytes / (1024 * 1024)
        print(
            f"The dump: '{file_path}' ({file_size_mb:.2f} MB / {file_size_bytes} Bites)"
        )
        return True

    except OSError as err:
        print(f"Error when reading '{file_path}': {err}")
        return False
