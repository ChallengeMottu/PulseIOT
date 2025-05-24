import asyncio
import binascii
from bleak import BleakScanner

def format_uuid(raw_bytes):
    uuid = raw_bytes.hex()
    return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:32]}"

def extract_uuid_from_bytes(raw_bytes):
    if len(raw_bytes) >= 18:
        uuid_bytes = raw_bytes[2:18]  
        return format_uuid(uuid_bytes)
    return None

def decode_manufacturer_data(data_dict):
    decoded = []
    for manufacturer_id, raw_bytes in data_dict.items():
        hex_data = binascii.hexlify(raw_bytes).decode()
        desc = f"Fabricante ID: {manufacturer_id} | Hex: {hex_data}"

        # Nordic Semiconductor (nRF52810) custom decoding - fabricante ID 89
        if manufacturer_id == 89:
            desc += "\n    📡 Tipo: Nordic Semiconductor (nRF52810 provável)"
            desc += f"\n    Dados crus: {hex_data}"
            desc += f"\n    Byte 0: {raw_bytes[0]} | Byte 1: {raw_bytes[1]}"

            uuid = extract_uuid_from_bytes(raw_bytes)
            if uuid:
                desc += f"\n    🔑 UUID extraído: {uuid}"
            else:
                desc += "\n    ❌ UUID não encontrado (dados insuficientes ou formato inesperado)."
        else:
            desc += "\n    📡 Tipo: Não identificado ou não tratado"

        decoded.append(desc)
    return decoded

async def scan_ble():
    print("🔍 Escaneando dispositivos BLE por 10 segundos...\n")
    devices = await BleakScanner.discover(timeout=10)

    for d in devices:
        if d.metadata and "manufacturer_data" in d.metadata:
            manu_data = d.metadata["manufacturer_data"]
            if 89 in manu_data:
                print(f"📡 Nome: {d.name or '[Sem nome]'}")
                print(f"🔗 Endereço: {d.address}")
                print(f"📶 RSSI: {d.rssi}")
                print("  🏷 Manufacturer Data:")
                for line in decode_manufacturer_data(manu_data):
                    print("   ", line)
                print("-" * 60)

asyncio.run(scan_ble())
