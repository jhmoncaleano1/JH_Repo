import pandas as pd

# Datos iniciales de precios estimados (pueden ajustarse con datos reales)
crypto_data = {
    "Moderado": {
        "Bitcoin (BTC)": {"%": 30, "precio_inicial": 65000},
        "Ethereum (ETH)": {"%": 20, "precio_inicial": 3200},
        "Solana (SOL)": {"%": 18, "precio_inicial": 140},
        "Chainlink (LINK)": {"%": 16, "precio_inicial": 15},
        "Polygon (MATIC)": {"%": 5, "precio_inicial": 1},
        "Stablecoins": {"%": 8, "precio_inicial": 1},
        "XRT (Robonomics)": {"%": 3, "precio_inicial": 3.5}
    },
    "Agresivo": {
        "Ethereum (ETH)": {"%": 22, "precio_inicial": 3200},
        "Solana (SOL)": {"%": 18, "precio_inicial": 140},
        "Avalanche (AVAX)": {"%": 10, "precio_inicial": 38},
        "Arbitrum (ARB)": {"%": 10, "precio_inicial": 1.1},
        "Chainlink (LINK)": {"%": 10, "precio_inicial": 15},
        "Aptos/SUI": {"%": 10, "precio_inicial": 9},
        "Stablecoins": {"%": 5, "precio_inicial": 1},
        "XRT (Robonomics)": {"%": 5, "precio_inicial": 3.5},
        "Token especulativo": {"%": 10, "precio_inicial": 2}
    }
}

# Crear DataFrames
df_moderado = pd.DataFrame(crypto_data["Moderado"]).T.reset_index().rename(columns={"index": "Criptomoneda"})
df_agresivo = pd.DataFrame(crypto_data["Agresivo"]).T.reset_index().rename(columns={"index": "Criptomoneda"})

df_moderado["Perfil"] = "Moderado"
df_agresivo["Perfil"] = "Agresivo"

# Combinar ambos
df_portafolios = pd.concat([df_moderado, df_agresivo], ignore_index=True)
df_portafolios
