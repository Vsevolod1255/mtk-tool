# huge thanks to bkerler, cyrozap, Chaosmaster for this information in the database
from types import MappingProxyType

_CHIPS = {
    "0x717": {
        "official_name": "MT6761/MT6762G/MT6762",
        "name": "helio A20/P22/A22/A25/G25",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XFLASH",
        "watchdog": "0x10007000",
    },
    "0x788": {
        "official_name": "MT6771/MT8385/MT8183/MT8666",
        "name": "helio P60/P70/G80",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XFLASH",
        "watchdog": "0x10007000",
    },
    "0x707": {
        "official_name": "MT6769Z/MT6768",
        "name": "helio G85",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XFLASH",
        "watchdog": "0x10007000",
    },
    "0x813": {
        "official_name": "MT6785/MT6785V/MT6785T",
        "name": "helio G90/G90T/G95",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XFLASH",
        "watchdog": "0x10007000",
    },
    "0x766": {
        "official_name": "MT6765/MT8768T",
        "name": "helio P35/G35",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XFLASH",
        "watchdog": "0x10007000",
    },
    "0x1208": {
        "official_name": "MT6789/MT8781V",
        "name": "helio G99",
        "sla_required": True,
        "daa_required": True,
        "arch": "ARM64",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.XML",
        "watchdog": "0x10007000",
    },
    "0x6580": {
        "official_name": "MT6580",
        "name": "MT6580",
        "sla_required": False,
        "daa_required": False,
        "arch": "ARM32",
        "brom_payload_addr": "0x100A00",
        "da_payload_addr": "0x201000",
        "damode": "DAmodes.LEGACY",
        "watchdog": "0x10007000",
    },
}

CHIP_DATABASE = MappingProxyType(
    {hw: MappingProxyType(info) for hw, info in _CHIPS.items()}
)


def print_chip_card(hw_code: str, info: dict | MappingProxyType):
    print("----------------------------------------")
    print(f"🔑 HW_CODE:            {hw_code}")
    print(f"📱 Official Name:      {info.get('official_name', 'N/A')}")
    print(f"🏷️ Market Name:        {info.get('name', 'N/A')}")
    print(f"🏗️ Arch:               {info.get('arch', 'N/A')}")
    print(
        f"🔒 SLA/DAA Required:   SLA={info.get('sla_required')}, DAA={info.get('daa_required')}"
    )
    print(f"📍 BROM Payload Addr: {info.get('brom_payload_addr', 'N/A')}")
    print(f"📍 DA Payload Addr:   {info.get('da_payload_addr', 'N/A')}")
    print(f"⚡ DA Mode:           {info.get('damode', 'N/A')}")
    print(f"⏱️ Watchdog:          {info.get('watchdog', 'N/A')}")
    print("----------------------------------------")


def print_all_chips():
    print(f"\n The total number of chips in the database: {len(CHIP_DATABASE)}")
    for hw_code, info in CHIP_DATABASE.items():
        print_chip_card(hw_code, info)


def search_chips(query: str) -> dict:
    clean_query = query.strip().lower()
    if not clean_query:
        return {}

    short_query = clean_query.replace("0x", "").replace("mt", "").strip()
    results = {}

    for hw_code, info in CHIP_DATABASE.items():
        hw_clean = hw_code.lower().replace("0x", "")
        official_raw = info.get("official_name", "").lower()
        official_clean = official_raw.replace("mt", "")
        name_clean = info.get("name", "").lower()

        match_hw = bool(short_query) and (short_query in hw_clean)
        match_official = (bool(short_query) and (short_query in official_clean)) or (
            clean_query in official_raw
        )
        match_name = clean_query in name_clean

        if match_hw or match_official or match_name:
            results[hw_code] = dict(info)

    return results


def get_chip_info(hw_code: str | int) -> dict | None:
    if isinstance(hw_code, int):
        hw_code = hex(hw_code)

    clean_code = str(hw_code).lower().strip()

    if not clean_code.startswith("0x"):
        clean_code = "0x" + clean_code

    if clean_code.startswith("0x0") and len(clean_code) > 4:
        clean_code = "0x" + clean_code[3:]

    info = CHIP_DATABASE.get(clean_code)
    return dict(info) if info else None
