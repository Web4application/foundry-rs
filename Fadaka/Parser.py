import binascii

def satoshi_to_btc(value):
    return value / 100_000_000

def parse_tx(tx_json):
    print("=== TRANSACTION SUMMARY ===")
    print(f"TXID: {tx_json['txid']}")
    print(f"Confirmations: {tx_json['tx']['confirmations']}")
    print(f"Size: {tx_json['tx']['size']} bytes\n")

    # INPUTS
    print("=== INPUTS ===")
    total_in = 0
    for vin in tx_json["tx"]["vin"]:
        addr = vin["vout_data"]["scriptPubKey"]["address"]
        value = vin["vout_data"]["value"]
        total_in += value
        print(f"From: {addr} → {value} BTC")

    # OUTPUTS
    print("\n=== OUTPUTS ===")
    total_out = 0
    for vout in tx_json["tx"]["vout"]:
        addr = vout["scriptPubKey"].get("address", "UNKNOWN")
        value = vout["value"]
        total_out += value
        print(f"To: {addr} → {value} BTC")

    # FEES
    fee = total_in - total_out
    print("\n=== FEES ===")
    print(f"Input Total: {total_in} BTC")
    print(f"Output Total: {total_out} BTC")
    print(f"Fee: {fee:.8f} BTC")

    return {
        "input_total": total_in,
        "output_total": total_out,
        "fee": fee
    }
