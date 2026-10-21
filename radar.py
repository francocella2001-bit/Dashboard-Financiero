# ⚙️ CONFIGURACIÓN — cambiá los valores y guardá (commit). La próxima corrida los usa.
# **Identidad**
NOMBRE_DASHBOARD = "Radar de rupturas"
LEMA = ""
AVATAR_URL = ""  # link a una imagen cuadrada para el ícono; vacío = logo del radar
# **Requisitos**
PRECIO_MINIMO = 10
ADR_MINIMO = 1.5
ADR_MINIMO_ETF = 1.0  # los ETFs se mueven menos que una acción (EWZ ronda 2%, SPY 1%)
ADR_PERIODO = 20
MIN_CRITERIOS_MINERVINI = 6
EXIGIR_RS = False  # True: además del X/8, exige RS Rating de RS_MINIMO o más
PCT_SOBRE_MINIMO_52S = 25
PCT_SOBRE_MINIMO_52S_ETF = 15  # índices y ETFs rara vez suben 25% desde su mínimo anual
PCT_DEBAJO_MAXIMO_52S = 30
RS_MINIMO = 70
EXIGIR_AVWAP = False  # False: las AVWAP suman puntos y se muestran, pero no son requisito para entrar
ANCLAS_FUERTES = "Earnings, Episodic pivot, Máx. estructural, Máx. histórico, Mín. estructural, Mín. mensual, Mín. histórico, IPO"
# **AVWAP**
DIST_POR_ROMPER_DIARIO = 3.0
DIST_POR_ROMPER_SEMANAL = 5.0
VELAS_RUPTURA_DIARIO = 3
VELAS_RUPTURA_SEMANAL = 2
BUSCAR_EARNINGS = True
# **Compresión e intradía**
VOL_RUPTURA = 1.3
CERCA_GATILLO = 2.0
ANALIZAR_30M = True
EMAS_DIARIO_PIVOT = "8, 10, 20, 50"
TOLERANCIA_TOQUE_EMA = 0.5
DIAS_TOQUE_EMA = 2
# **Compresión**
EMAS_ASCENSO = "10, 20, 50"
# **Seleccionadas** (las mejores dentro de las que cumplen todo)
SEL_RS_MIN = 80
SEL_MINERVINI_MIN = 7
SEL_SCORE_MIN = 70
SEL_HISTORIA_RUEDAS = 20  # track record: ingresos a Seleccionadas de las últimas N ruedas
# **Alertas por Telegram** (el token y el chat van como secretos de GitHub, nunca acá)
ALERTAS_TELEGRAM = True
URL_DASHBOARD = "https://francocella2001-bit.github.io/Dashboard-Financiero/"
RESUMEN_DIARIO = True   # un resumen por Telegram con la primera corrida desde las 18 h (Argentina), ya con la vela cerrada
RESUMEN_CERCA = 2.0     # % máximo hasta el pivot o la AVWAP para figurar como "armada para mañana"
# **Lista de foco y score**
FOCO_MAXIMO = 10
FOCO_RS_MINIMO = 80
FOCO_RIESGO_MAX = 8.0
ZONA_COMPRA_MAX = 5.0  # % máximo sobre la entrada para seguir en Lista de foco / Crème (más arriba ya está extendida)
SCORE_CASTIGO_BANDERA = 5
# **Pesos del score** (tienen que sumar 100)
PUNTOS_TENDENCIA = 20
PUNTOS_RS = 25
PUNTOS_COMPRESION = 35
PUNTOS_SETUP = 20
PUNTOS_FUNDAMENTALES = 0  # 0 = como Warren: los fundamentales se muestran pero no suman ni restan al score
# **Fundamentales CAN SLIM** (suman puntos, nunca excluyen)
BUSCAR_FUNDAMENTALES = True
CRECIMIENTO_FUERTE = 25  # % interanual: acelerando y sobre este valor suma todo; solo una de las dos, la mitad
# **Bases VCP**
VCP_MIN_CONTRACCIONES = 2
VCP_ULTIMA_MAX = 10.0
VCP_FORMANDO_MAX = 20.0
VCP_PIVOT_ARRIBA = 60
VCP_TOLERANCIA = 1.5
VCP_PRIMERA_MAX = 35.0
VCP_PRIMERA_MIN = 8.0
VCP_VOL_SECO = 1.0
VCP_DIST_PIVOT = 5.0
VCP_SEMANAS_MIN = 3
VCP_SEMANAS_MAX = 65
VCP_TENDENCIA_PREVIA = 30
VCP_DIAS_RUPTURA = 3
VCP_DIAS_SEGUIMIENTO = 15
# **Cierres semanales apretados (TC)**
TC_MIN_CIERRES = 3      # cierres semanales consecutivos (completos) dentro del rango
TC_RANGO_MAX = 1.5      # % entre el cierre más alto y el más bajo de esas semanas
TC_VOL_SECO = 1.0       # volumen promedio de esas semanas contra el de las 10 previas: por debajo = seco
TC_CERCA_PIVOT = 5.0    # % máximo debajo del pivot (o del máximo de 10 semanas) para sumar el extra
TC_PUNTOS = 3           # puntos de setup (sobre 20) por tener TC; +2 si además está seco y cerca del pivot
# **Gatillos semanales** (filtros de la vista Gatillos)
CRUCE_SEMANAS = 4  # un cruce de RSI o MACD semanal cuenta si pasó en las últimas N semanas
# **Retorno del Top del score** (track record entre corridas)
TOP_N = 10        # cuántas del ranking se siguen
TOP_RUEDAS = 10   # ventana en ruedas para medir el retorno desde que entraron
# **Régimen de mercado**
REG_PESO_INDICES = 80     # pesos de cada capa (como Warren: 80 / 30 / 15)
REG_PESO_AMPLITUD = 30
REG_PESO_VIX = 15
REG_DISTRIBUCION_TOPE = 5 # con esta cantidad de días de distribución o más, el índice no puede pasar del 50% de su puntaje
FTD_SUBA_MIN = 1.25       # % mínimo de suba del índice para contar como follow-through day
FTD_CORRECCION_MIN = 5.0  # % de caída desde el máximo de 60 ruedas para considerar que hubo corrección
MOSTRAR_FEAR_GREED = True # Fear & Greed de CNN como dato aparte (no suma al score)
# **Eventos de la semana** (calendario macro de EE.UU.; solo alto y medio impacto, sin discursos menores)
EVENTOS_DIAS = 7
EVENTOS_EARN_MCAP_MIN = 10_000_000_000  # earnings que se muestran: empresas de este tamaño o más, y todas las del radar
# **Módulos de Inicio y Sectores**
RSI_SOBRECOMPRA = 70     # RSI 14 diario: desde acá cuenta como sobrecomprada
RSI_SOBREVENTA = 30      # y hasta acá como sobrevendida
CARTELERA_N = 6          # cuántas suben y cuántas bajan en la cartelera del día (acciones líquidas)
ROTACION_SEMANAS = 16    # semanas de historia en los cuadrantes de rotación
# **Episodic pivots y banderas**
EP_MIN_SUBA = 4.0
EP_MIN_VOL = 2.0
EXTENDIDO_SMA50 = 25
ESTIRADA_EMA10_ADR = 2.0
ESTIRADA_EMA20_ADR = 3.0
# **Tamaño y liquidez** (promedios de 50 ruedas; 0 = desactivado; no aplica a ETFs ni cripto)
MARKET_CAP_MIN = 1_000_000_000
VOLUMEN_DOLARES_MIN = 20_000_000
VOLUMEN_ACCIONES_MIN = 0
LIQUIDEZ_ALCANZA_UNO = True  # True: pasa si cumple el volumen en acciones O en dólares; False: tiene que cumplir los dos
# **Universo**
UNIVERSO = "completo"  # "completo": todas las acciones y ADRs de EE.UU. (NASDAQ, NYSE, NYSE American, Arca); "indices": los índices de abajo
INCLUIR_SP500 = True
INCLUIR_NASDAQ100 = True
INCLUIR_MIDCAP400 = True
INCLUIR_ETFS = True
INCLUIR_CRIPTO = True
TICKERS_EXTRA = "NBIS, CLS, HOOD"


# ---- Motor del radar (no hace falta tocar nada de acá para abajo) ----
import warnings, json, math, time, io, zlib, base64, datetime as dt
import numpy as np
import pandas as pd
warnings.filterwarnings("ignore")
try:
    import yfinance as yf
except ImportError:
    yf = None

# ---------------------------------------------------------------- universo
SECTORES_ES = {
    "Information Technology": "Tecnología", "Technology": "Tecnología",
    "Health Care": "Salud", "Financials": "Financiero", "Consumer Discretionary": "Consumo discrecional",
    "Consumer Staples": "Consumo básico", "Industrials": "Industria", "Energy": "Energía",
    "Materials": "Materiales", "Utilities": "Servicios públicos", "Real Estate": "Inmobiliario",
    "Communication Services": "Comunicaciones", "Telecommunications": "Comunicaciones",
    "Healthcare": "Salud", "Financial Services": "Financiero", "Consumer Cyclical": "Consumo discrecional",
    "Consumer Defensive": "Consumo básico", "Basic Materials": "Materiales",
}
ETFS = {
    "SPY": "S&P 500", "QQQ": "Nasdaq 100", "IWM": "Russell 2000", "DIA": "Dow Jones", "XLK": "Tecnología",
    "XLF": "Financiero", "XLE": "Energía", "XLV": "Salud", "XLI": "Industria", "XLY": "Consumo discrecional",
    "XLP": "Consumo básico", "XLU": "Servicios públicos", "XLB": "Materiales", "XLRE": "Inmobiliario",
    "XLC": "Comunicaciones", "SMH": "Semiconductores", "SOXX": "Semiconductores", "IGV": "Software",
    "CIBR": "Ciberseguridad", "ARKK": "Innovación", "XBI": "Biotecnología", "KRE": "Bancos regionales",
    "ITB": "Constructoras", "GDX": "Mineras de oro", "GLD": "Oro", "SLV": "Plata", "USO": "Petróleo",
    "TLT": "Bonos 20+ años", "EEM": "Emergentes", "IEMG": "Emergentes core", "EWZ": "Brasil",
    "FXI": "China", "EWJ": "Japón", "INDA": "India", "URA": "Uranio", "TAN": "Solar", "IBIT": "Bitcoin spot",
}
CRIPTO = {
    "BTC-USD": "Bitcoin", "ETH-USD": "Ethereum", "SOL-USD": "Solana", "BNB-USD": "BNB", "XRP-USD": "XRP",
    "ADA-USD": "Cardano", "AVAX-USD": "Avalanche", "LINK-USD": "Chainlink", "DOGE-USD": "Dogecoin",
    "DOT-USD": "Polkadot", "LTC-USD": "Litecoin", "TRX-USD": "Tron", "NEAR-USD": "Near", "ATOM-USD": "Cosmos",
    "UNI7083-USD": "Uniswap", "AAVE-USD": "Aave", "XLM-USD": "Stellar", "HBAR-USD": "Hedera",
}
# ETF de referencia: primero por industria (más específico), si no por sector
ETF_INDUSTRIA = {"Semiconductors": "SMH", "Semiconductor Equipment & Materials": "SMH", "Software - Infrastructure": "IGV",
                 "Software - Application": "IGV", "Biotechnology": "XBI", "Banks - Regional": "KRE", "Residential Construction": "ITB",
                 "Gold": "GDX", "Solar": "TAN", "Uranium": "URA"}
ETF_SECTOR = {"Tecnología": "XLK", "Financiero": "XLF", "Energía": "XLE", "Salud": "XLV", "Industria": "XLI",
              "Consumo discrecional": "XLY", "Consumo básico": "XLP", "Servicios públicos": "XLU", "Materiales": "XLB",
              "Inmobiliario": "XLRE", "Comunicaciones": "XLC"}
ETF_PALABRAS = (("Semiconductor", "SMH"), ("Software", "IGV"), ("Biotechnology", "XBI"), ("Regional", "KRE"),
                ("Savings Institutions", "KRE"), ("Homebuilding", "ITB"), ("Residential Construction", "ITB"),
                ("Precious Metals", "GDX"), ("Gold", "GDX"), ("Solar", "TAN"), ("Uranium", "URA"))

def etf_de(industria, sector):
    ind = industria or ""
    if ind in ETF_INDUSTRIA: return ETF_INDUSTRIA[ind]
    for palabra, etf in ETF_PALABRAS:
        if palabra in ind: return etf
    return ETF_SECTOR.get(sector)

RESPALDO = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA","AVGO","AMD","NFLX","CRM","ORCL","ADBE","NOW","PLTR",
            "ANET","TSM","MU","AMAT","LRCX","KLAC","SHOP","UBER","COIN","HOOD","JPM","GS","MS","V","MA","LLY","ABBV",
            "UNH","ISRG","XOM","CVX","CAT","GE","DE","BA","COST","WMT","HD","NKE","DIS","TWLO","NBIS","CLS","GRMN","BIIB"]

def _tablas_wiki(url):
    import requests
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).text
    return pd.read_html(io.StringIO(html))

def _extraer(tablas):
    for t in tablas:
        t = t.copy()
        t.columns = [" ".join(map(str, c)) if isinstance(c, tuple) else str(c) for c in t.columns]
        tick = next((c for c in t.columns if c.strip().lower() in ("symbol", "ticker", "ticker symbol")), None)
        sec = next((c for c in t.columns if "sector" in c.lower()), None)
        nom = next((c for c in t.columns if c.strip().lower() in ("security", "company", "name")), None)
        if tick and sec and len(t) > 50:
            filas = []
            for _, r in t.iterrows():
                s = str(r[tick]).strip().replace(".", "-")
                if s and s.lower() != "nan":
                    filas.append((s, str(r[nom]) if nom else s, SECTORES_ES.get(str(r[sec]).strip(), str(r[sec]).strip()), "accion", ""))
            return filas
    return []

_NO_COMUNES = (r"\b(warrants?|rights?|preferred|pfd|perpetual|debentures?|subordinated|notes? due|etns?|exchange traded notes?)\b"
               r"|(?<!common )\bunits?\b|\d% |depositary shares,? each representing (a |one )?\d*/\d+")

BOLSAS_TV = {"N": "NYSE", "A": "AMEX", "P": "AMEX", "Z": "CBOE", "V": "IEX"}  # código de NASDAQ Trader → prefijo de TradingView

def listado_eeuu():
    """Acciones comunes y ADRs de NASDAQ, NYSE, NYSE American y Arca según NASDAQ Trader (sin ETFs, warrants, units, rights ni preferidas)."""
    import requests, re
    base = "https://www.nasdaqtrader.com/dynamic/SymDir/"
    partes = []
    for arch, col in (("nasdaqlisted.txt", "Symbol"), ("otherlisted.txt", "ACT Symbol")):
        txt = requests.get(base + arch, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).text
        d = pd.read_csv(io.StringIO(txt), sep="|", dtype=str)
        d = d[~d.iloc[:, 0].str.startswith("File Creation", na=True)]
        bolsa = "NASDAQ" if arch.startswith("nasdaq") else d["Exchange"].map(BOLSAS_TV).fillna("")
        partes.append(pd.DataFrame({"s": d[col], "n": d["Security Name"], "etf": d["ETF"], "test": d["Test Issue"], "bolsa": bolsa}))
    d = pd.concat(partes)
    d = d[(d.etf != "Y") & (d.test != "Y") & d.s.notna() & d.n.notna()]
    d = d[~d.n.str.contains(_NO_COMUNES, flags=re.I, regex=True)]
    d = d[~d.s.str.contains(r"[$^\s=]", regex=True)]
    limpiar = lambda n: re.sub(r"\s*[-,]?\s*(Class [A-Z] )?(Common (Stock|Shares|Units)|Ordinary Shares?|American Depositary (Shares|Receipts)).*$", "", n, flags=re.I).strip() or n
    return [(s.replace(".", "-").replace("/", "-"), limpiar(n), "Sin clasificar", "accion", b) for s, n, b in zip(d.s, d.n, d.bolsa)]

def obtener_universo():
    filas = []
    fuentes = []
    if UNIVERSO == "completo":
        try:
            filas = listado_eeuu()
            print(f"  {len(filas)} acciones y ADRs de NASDAQ Trader")
        except Exception as e:
            print(f"  ⚠️ No pude leer NASDAQ Trader ({e}); uso los índices")
    if not filas:
        if INCLUIR_SP500: fuentes.append("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
        if INCLUIR_NASDAQ100: fuentes.append("https://en.wikipedia.org/wiki/Nasdaq-100")
        if INCLUIR_MIDCAP400: fuentes.append("https://en.wikipedia.org/wiki/List_of_S%26P_400_companies")
    for url in fuentes:
        try:
            f = _extraer(_tablas_wiki(url)); filas += f
            print(f"  {len(f)} acciones de {url.split('/')[-1]}")
        except Exception as e:
            print(f"  ⚠️ No pude leer {url}: {e}")
    if fuentes and not filas:
        print("  ⚠️ Uso la lista de respaldo de acciones")
        filas += [(t, t, "Sin clasificar", "accion", "") for t in RESPALDO]
    extra = [t.strip().upper() for t in str(TICKERS_EXTRA).replace(";", ",").split(",") if t.strip()]
    filas += [(t, t, "Tu lista", "accion", "") for t in extra]
    if INCLUIR_ETFS: filas += [(t, n, "ETF", "etf", "") for t, n in ETFS.items()]
    if INCLUIR_CRIPTO: filas += [(t, n, "Cripto", "cripto", "CRYPTO") for t, n in CRIPTO.items()]
    u = pd.DataFrame(filas, columns=["ticker", "nombre", "sector", "tipo", "bolsa"]).drop_duplicates("ticker", keep="first")
    return u.reset_index(drop=True)

# ---------------------------------------------------------------- datos
def descargar(tickers, period, interval, chunk=80, reintento=True):
    """Baja velas en lotes. Si Yahoo corta o limita, espera y reintenta; al final vuelve a pedir una vez los que faltan."""
    datos = {}
    tickers = list(dict.fromkeys(tickers))
    for i in range(0, len(tickers), chunk):
        grupo = tickers[i:i + chunk]
        df = None
        for intento in range(3):
            try:
                df = yf.download(grupo, period=period, interval=interval, group_by="ticker",
                                 auto_adjust=True, threads=True, progress=False)
                break
            except Exception as e:
                print(f"  ⚠️ lote {i // chunk + 1}: {e}; espero {15 * (intento + 1)} s")
                time.sleep(15 * (intento + 1))
        if df is None: continue
        for t in grupo:
            try:
                sub = df[t] if isinstance(df.columns, pd.MultiIndex) else df
                sub = sub[["Open", "High", "Low", "Close", "Volume"]].dropna(subset=["Close", "High", "Low"])
                sub = sub[sub["Close"] > 0]
                if interval == "1d" and getattr(sub.index, "tz", None) is not None:
                    sub.index = sub.index.tz_localize(None)
                if len(sub): datos[t] = sub.astype(float)
            except Exception:
                pass
        hechos = min(i + chunk, len(tickers))
        if len(tickers) <= 10 * chunk or hechos % (10 * chunk) == 0 or hechos == len(tickers):
            print(f"  {hechos}/{len(tickers)}")
    faltan = [t for t in tickers if t not in datos]
    # Si faltan muchos suele ser un límite de Yahoo, no tickers muertos: una segunda pasada los recupera
    if reintento and faltan and len(faltan) > max(5, 0.03 * len(tickers)):
        print(f"  Reintento {len(faltan)} que no bajaron…")
        time.sleep(20)
        datos.update(descargar(faltan, period, interval, chunk=max(20, chunk // 2), reintento=False))
    return datos

_CACHE_EARN = None
def fechas_earnings(t):
    """(últimos earnings, próximos earnings) o (None, None). Guarda caché de 1 día en earnings_cache.json."""
    global _CACHE_EARN
    import os
    if _CACHE_EARN is None:
        try: _CACHE_EARN = json.load(open("earnings_cache.json"))
        except Exception: _CACHE_EARN = {}
    hoy = dt.date.today().isoformat()
    e = _CACHE_EARN.get(t)
    if e and e.get("dia") == hoy:
        return (pd.Timestamp(e["u"]) if e["u"] else None, pd.Timestamp(e["p"]) if e["p"] else None)
    u, p = _earnings_yahoo(t)
    _CACHE_EARN[t] = {"dia": hoy, "u": u.isoformat() if u is not None else None, "p": p.isoformat() if p is not None else None}
    try: json.dump(_CACHE_EARN, open("earnings_cache.json", "w"))
    except Exception: pass
    return u, p

def momento_earnings(p):
    if p is None or (p.hour == 0 and p.minute == 0): return None
    return "antes de la apertura" if p.hour < 12 else ("después del cierre" if p.hour >= 16 else None)

def _earnings_yahoo(t):
    try:
        ed = yf.Ticker(t).get_earnings_dates(limit=12)
        if ed is None or ed.empty: return None, None
        idx = pd.DatetimeIndex(ed.index)
        if idx.tz is not None: idx = idx.tz_localize(None)
        ahora = pd.Timestamp.now()
        pas, fut = idx[idx <= ahora], idx[idx > ahora]
        return (pas.max().normalize() if len(pas) else None, fut.min() if len(fut) else None)
    except Exception:
        return None, None

# ---------------------------------------------------------------- perfil: market cap, sector, industria
ARCHIVO_PERFILES = "sectores_cache.json"
PERFIL_DIAS = 30        # cada cuánto se vuelve a pedir un perfil (el market cap se ajusta por precio entre medio)
PERFIL_MAX_CORRIDA = 2500  # tope de consultas nuevas por corrida; las que quedan se piden en la siguiente

def _perfil_yahoo(t):
    try:
        i = yf.Ticker(t).info or {}
    except Exception:
        return None
    if not i: return None
    px = i.get("currentPrice") or i.get("regularMarketPrice") or i.get("previousClose")
    return {"dia": dt.date.today().isoformat(), "mcap": i.get("marketCap"), "px": px,
            "sector": i.get("sector"), "ind": i.get("industry"), "nom": i.get("shortName") or i.get("longName")}

SECTORES_NASDAQ = {"Finance": "Financiero", "Health Care": "Salud", "Technology": "Tecnología", "Consumer Discretionary": "Consumo discrecional",
                   "Industrials": "Industria", "Real Estate": "Inmobiliario", "Energy": "Energía", "Utilities": "Servicios públicos",
                   "Basic Materials": "Materiales", "Consumer Staples": "Consumo básico", "Telecommunications": "Comunicaciones",
                   "Miscellaneous": "Otros"}

def nasdaq_screener():
    """Market cap, sector e industria de todas las acciones de EE.UU. en una sola consulta al screener de NASDAQ.
    Desde GitHub Actions Yahoo no devuelve estos datos, así que esta es la fuente principal."""
    import requests
    try:
        r = requests.get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&download=true",
                         headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}, timeout=60)
        filas = r.json()["data"]["rows"]
    except Exception as e:
        print(f"   ⚠️ No pude leer el screener de NASDAQ ({e}); uso Yahoo")
        return {}
    out = {}
    for f in filas:
        try: mcap = float(f.get("marketCap") or 0) or None
        except ValueError: mcap = None
        t = str(f.get("symbol", "")).strip().replace("/", "-").replace(".", "-")
        sec = (f.get("sector") or "").strip()
        out[t] = {"mcap": mcap, "sector": SECTORES_NASDAQ.get(sec, sec) or None, "industria": (f.get("industry") or "").strip() or None}
    print(f"   Screener de NASDAQ: {len(out)} acciones")
    return out

def perfiles(tickers, precios):
    """{ticker: {mcap, sector, industria, nombre}}. Market cap del screener de NASDAQ (o Yahoo si falta); sector e industria
    de Yahoo cuando hay caché válido (clasificación más fina), si no de NASDAQ. Yahoo solo se consulta para las que NASDAQ no cubre."""
    from concurrent.futures import ThreadPoolExecutor
    nq = nasdaq_screener()
    try: cache = json.load(open(ARCHIVO_PERFILES))
    except Exception: cache = {}
    # Un perfil sin market cap ni sector no sirve (Yahoo a veces responde vacío): se vuelve a pedir
    cache = {t: c for t, c in cache.items() if c.get("mcap") or c.get("sector")}
    limite = (dt.date.today() - dt.timedelta(days=PERFIL_DIAS)).isoformat()
    falta_nq = lambda t: not (nq.get(t) or {}).get("mcap") or not (nq.get(t) or {}).get("sector")
    pedir = [t for t in tickers if falta_nq(t) and (t not in cache or cache[t].get("dia", "") < limite)][:PERFIL_MAX_CORRIDA]
    if pedir:
        print(f"   Perfil de {len(pedir)} acciones (market cap, sector e industria)…")
        hechos = 0
        # Yahoo responde "Invalid Crumb" si muchas consultas arrancan juntas: la primera va sola para fijar la sesión,
        # después pocos hilos, y una segunda pasada más lenta para las que fallaron
        for pasada, hilos in ((1, 4), (2, 2)):
            if pasada == 2:
                if not pedir: break
                print(f"   Reintento {len(pedir)} perfiles…"); time.sleep(10)
            _perfil_yahoo(pedir[0])
            with ThreadPoolExecutor(max_workers=hilos) as ex:
                res = list(ex.map(_perfil_yahoo, pedir))
            ok = lambda p: p and (p.get("mcap") or p.get("sector"))
            for t, p in zip(pedir, res):
                if ok(p): cache[t] = p; hechos += 1
            pedir = [t for t, p in zip(pedir, res) if not ok(p)]
        print(f"   {hechos} perfiles nuevos ({len(pedir)} sin respuesta, se reintentan la próxima corrida)")
        try: json.dump(cache, open(ARCHIVO_PERFILES, "w"))
        except Exception: pass
    out = {}
    for t in tickers:
        c, n = cache.get(t) or {}, nq.get(t) or {}
        mcap = n.get("mcap")
        if not mcap and c.get("mcap"):
            mcap = c["mcap"] * precios[t] / c["px"] if c.get("px") and precios.get(t) else c["mcap"]
        sec = c.get("sector")
        sec = SECTORES_ES.get(sec, sec) if sec else n.get("sector")
        if not (mcap or sec): continue
        out[t] = {"mcap": mcap, "sector": sec, "industria": c.get("ind") or n.get("industria"), "nombre": c.get("nom")}
    return out

def liquida(df):
    """Volumen promedio de 50 ruedas en acciones y en dólares contra los mínimos de CONFIGURACIÓN."""
    u = df.iloc[-50:]
    v50, d50 = u.Volume.mean(), (u.Close * u.Volume).mean()
    pruebas = [x for x in ((VOLUMEN_ACCIONES_MIN, v50), (VOLUMEN_DOLARES_MIN, d50)) if x[0] > 0]
    if not pruebas: return True, v50, d50
    ok = [v >= m for m, v in pruebas]
    return (any(ok) if LIQUIDEZ_ALCANZA_UNO else all(ok)), v50, d50

# ---------------------------------------------------------------- fundamentales CAN SLIM
ARCHIVO_FUNDAMENTALES = "fundamentales_cache.json"
FUND_DIAS = 7  # se refrescan cada semana o apenas hay un reporte nuevo

def _fecha(x):
    x = pd.Timestamp(x)
    return (x.tz_localize(None) if x.tzinfo else x).strftime("%Y-%m-%d")

def _fund_yahoo(t):
    """EPS trimestral (reportado y estimado), ventas trimestrales, EPS y ventas anuales, EPS 12 meses e institucionales."""
    try:
        tk = yf.Ticker(t)
        ed = tk.get_earnings_dates(limit=28)
        eps = []
        if ed is not None and not ed.empty:
            for f, r in ed.iterrows():
                if pd.notna(r.get("Reported EPS")):
                    eps.append([_fecha(f), float(r["Reported EPS"]), float(r["EPS Estimate"]) if pd.notna(r.get("EPS Estimate")) else None])
        def fila(d, k):
            if d is None or d.empty or k not in d.index: return []
            return [[_fecha(c), float(v)] for c, v in d.loc[k].items() if pd.notna(v)]
        q, a = tk.quarterly_income_stmt, tk.income_stmt
        i = tk.info or {}
        return {"dia": dt.date.today().isoformat(), "eps": sorted(eps), "ventas": sorted(fila(q, "Total Revenue")),
                "eps_anual": sorted(fila(a, "Diluted EPS")), "ventas_anual": sorted(fila(a, "Total Revenue")),
                "eps_ttm": i.get("trailingEps"), "inst": i.get("heldPercentInstitutions"), "moneda": i.get("financialCurrency")}
    except Exception:
        return None

def _hace_un_anio(serie, k):
    """Valor del mismo trimestre del año anterior (fecha entre 10 y 14 meses antes)."""
    f = pd.Timestamp(serie[k][0])
    for fila in serie[:k][::-1]:
        dias = (f - pd.Timestamp(fila[0])).days
        if 300 <= dias <= 430: return fila[1]
    return None

def _crec(act, ant):
    return (act / ant - 1) * 100 if act is not None and ant is not None and ant > 0 else None

def _yoy(serie):
    """Crecimientos interanuales de cada trimestre, del más nuevo al más viejo."""
    return [_crec(serie[k][1], _hace_un_anio(serie, k)) for k in range(len(serie) - 1, -1, -1)]

def _pts_crec(g0, g1, maximo):
    """Acelera (contra el trimestre o el año anterior) y crece fuerte: todo; solo una de las dos: la mitad."""
    if g0 is None or g0 <= 0: return 0.0
    acel = g1 is not None and g0 > g1
    fuerte = g0 >= CRECIMIENTO_FUERTE
    return maximo if (acel and fuerte) else maximo / 2 if (acel or fuerte) else 0.0

def fundamentales(tickers, ultimo_reporte):
    """{ticker: datos para la ficha y puntos CAN SLIM}, con caché en fundamentales_cache.json."""
    from concurrent.futures import ThreadPoolExecutor
    try: cache = json.load(open(ARCHIVO_FUNDAMENTALES))
    except Exception: cache = {}
    limite = (dt.date.today() - dt.timedelta(days=FUND_DIAS)).isoformat()
    def vencido(t):
        c = cache.get(t)
        if not c or c.get("dia", "") < limite: return True
        u = ultimo_reporte.get(t)
        return bool(u is not None and u.strftime("%Y-%m-%d") > c["dia"])
    pedir = [t for t in tickers if vencido(t)]
    if pedir:
        print(f"   Fundamentales de {len(pedir)} candidatas…")
        for pasada, hilos in ((1, 4), (2, 2)):
            if not pedir: break
            if pasada == 2: time.sleep(10)
            with ThreadPoolExecutor(max_workers=hilos) as ex:
                res = list(ex.map(_fund_yahoo, pedir))
            for t, r in zip(pedir, res):
                if not r: continue
                # Yahoo da solo 5 trimestres de ventas: se suman a los ya guardados para ir armando historia
                ventas = {f: v for f, v in (cache.get(t) or {}).get("ventas", [])}
                ventas.update({f: v for f, v in r["ventas"]})
                r["ventas"] = sorted([f, v] for f, v in ventas.items())
                cache[t] = r
            pedir = [t for t, r in zip(pedir, res) if not r]
        try: json.dump(cache, open(ARCHIVO_FUNDAMENTALES, "w"))
        except Exception: pass
    out = {}
    for t in tickers:
        c = cache.get(t)
        if not c: continue
        ge, gv = _yoy(c["eps"]), _yoy(c["ventas"])
        va = c.get("ventas_anual") or []
        anual_v = _crec(va[-1][1], va[-2][1]) if len(va) >= 2 else None
        e0, e1 = (ge + [None, None])[:2]
        v0, v1 = (gv + [None, None])[:2]
        if v1 is None: v1 = anual_v  # sin el trimestre anterior, se compara contra el crecimiento del último año
        mitad = (PUNTOS_FUNDAMENTALES or 10) / 2  # si no suman al score, se calculan igual sobre 10 para el sello CAN SLIM
        trim = []
        for k in range(len(c["eps"]) - 1, max(-1, len(c["eps"]) - 5), -1):
            f, rep_, est = c["eps"][k]
            trim.append({"f": f, "eps": rep_, "ant": _hace_un_anio(c["eps"], k), "supero": est is not None and rep_ > est})
        ea = c.get("eps_anual") or []
        ult4 = [x[1] for x in c["eps"][-4:]]
        eps12 = sum(ult4) if len(ult4) == 4 else c.get("eps_ttm")
        out[t] = {"eps_g": num(e0, 0) if e0 is not None else None, "eps_g_ant": num(e1, 0) if e1 is not None else None,
                  "ventas_g": num(v0, 0) if v0 is not None else None, "ventas_g_ant": num(v1, 0) if v1 is not None else None,
                  "pts_eps": _pts_crec(e0, e1, mitad), "pts_ventas": _pts_crec(v0, v1, mitad),
                  "eps_ttm": eps12, "inst": num(c["inst"] * 100, 0) if c.get("inst") is not None else None,
                  "trim": trim[::-1], "anual": [[f[:4], num(v, 2)] for f, v in ea[-4:]], "moneda": c.get("moneda")}
    return out

# ---------------------------------------------------------------- indicadores
def sma(s, n): return s.rolling(n).mean()
def ema(s, n): return s.ewm(span=n, adjust=False).mean()
def atr(df, n):
    pc = df.Close.shift()
    tr = pd.concat([df.High - df.Low, (df.High - pc).abs(), (df.Low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n).mean()

def semanal(df, cripto=False):
    return df.resample("W-SUN" if cripto else "W-FRI").agg(
        {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"}).dropna(subset=["Close"])

def ahora_ar():
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("America/Argentina/Buenos_Aires"))
    except Exception:
        return dt.datetime.now()

def num(x, d=2):
    try:
        x = float(x)
        return None if not math.isfinite(x) else round(x, d)
    except Exception:
        return None

def rs_bruto(c):
    def r(n): return c.iloc[-1] / c.iloc[-n - 1] - 1 if len(c) > n else c.iloc[-1] / c.iloc[0] - 1
    return 0.4 * r(63) + 0.2 * r(126) + 0.2 * r(189) + 0.2 * r(252)

def adr_pct(df, n=None):
    n = n or ADR_PERIODO
    r = (df.High / df.Low).iloc[-n:]
    return (r.mean() - 1) * 100 if len(r) else 0.0

def pendiente(s, n):
    """Como el indicador de TradingView: 2 sube y sostenida (vs hace n velas), 1 sube solo hoy, -1 baja solo hoy, -2 baja y sostenida."""
    s = s.dropna()
    if len(s) <= n: return None
    if s.iloc[-1] > s.iloc[-2]: return 2 if s.iloc[-1] > s.iloc[-1 - n] else 1
    return -2 if s.iloc[-1] < s.iloc[-1 - n] else -1

def minervini(df, spy, fondo=False):
    """Los 8 criterios del "Minervini Trend Compact v2.3" de TradingView: EMAs, extremos de 252 velas y línea de RS vs SPY."""
    c = df.Close; p = c.iloc[-1]
    e = {n: ema(c, n) for n in (10, 20, 50, 150, 200)}
    g = lambda n: e[n].iloc[-1]
    u = df.iloc[-252:]
    hi, lo = u.High.max(), u.Low.min()
    v200 = e[200]
    # ta.rising(v200, 22): la EMA200 de hoy es mayor que cada uno de los 22 valores anteriores
    sube200 = len(v200) > 22 and v200.iloc[-1] > v200.iloc[-23:-1].max()
    rs_linea = False
    if spy is not None:
        lin = c / spy.reindex(c.index).ffill()
        m = lin.rolling(50).mean().iloc[-1]
        rs_linea = not pd.isna(m) and lin.iloc[-1] > m
    checks = [
        p > g(150) and p > g(200),
        g(150) > g(200),
        sube200,
        g(50) > g(150) and g(50) > g(200),
        p > g(50),
        p >= lo * (1 + (PCT_SOBRE_MINIMO_52S_ETF if fondo else PCT_SOBRE_MINIMO_52S) / 100),
        p >= hi * (1 - PCT_DEBAJO_MAXIMO_52S / 100),
        rs_linea,
    ]
    return [bool(x) for x in checks], hi, lo, e

def pasa_minervini(checks, rs):
    return sum(checks) >= MIN_CRITERIOS_MINERVINI and (rs >= RS_MINIMO or not EXIGIR_RS)

def rsi(c, n=14):
    d = c.diff()
    up, dn = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean(), (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))

def _ultimo_cruce(a, b):
    """Semanas desde el último cruce de a sobre b (positivo = cruzó hacia arriba, negativo = hacia abajo)."""
    dif = (a - b).dropna()
    if len(dif) < 3: return None, None
    signo = np.sign(dif.values)
    for k in range(len(signo) - 1, 0, -1):
        if signo[k] != signo[k - 1] and signo[k] != 0:
            return len(signo) - 1 - k, "arriba" if signo[k] > 0 else "abajo"
    return None, None

def semanales(wk):
    """RSI semanal contra su SMA14 y cruces del MACD semanal (12, 26, 9)."""
    if len(wk) < 40: return None
    c = wk.Close
    r = rsi(c); rm = r.rolling(14).mean()
    macd = ema(c, 12) - ema(c, 26); senal = ema(macd, 9)
    hr, dr = _ultimo_cruce(r, rm)
    hm, dm = _ultimo_cruce(macd, senal)
    return {"rsi": num(r.iloc[-1], 0), "rsi_sma": num(rm.iloc[-1], 0), "rsi_hace": hr, "rsi_dir": dr,
            "macd_hace": hm, "macd_dir": dm, "macd_cero": "bajo cero" if macd.iloc[-1] < 0 else "sobre cero"}

def tecnico(df, wk, e):
    """Pendientes de EMAs, momentum 35-5 diario y semanal, y volumen estilo MarketSmith."""
    c, v = df.Close, df.Volume
    mom = lambda x: ema(x, 5) - ema(x, 35)
    v50 = v.rolling(50).mean().iloc[-1]
    u = df.iloc[-51:]; ch = u.Close.diff().iloc[1:]; vv = u.Volume.iloc[1:]
    up, dn = vv[ch > 0].sum(), vv[ch < 0].sum()
    return {
        "pend": [pendiente(e[n], k) for n, k in ((10, 3), (20, 5), (50, 10), (150, 20), (200, 22))],
        "m1d": pendiente(mom(c), 5), "m1w": pendiente(mom(wk.Close), 4) if len(wk) > 40 else None,
        "vol_hoy": num(v.iloc[-1], 0), "vol_pct": num((v.iloc[-1] / v50 - 1) * 100, 0) if v50 > 0 else None,
        "ud50": num(up / dn, 2) if dn > 0 else None,
        "d200": num((c.iloc[-1] / e[200].iloc[-1] - 1) * 100, 1), "sem": semanales(wk),
    }

# ---------------------------------------------------------------- episodic pivots, banderas, estadio
def episodic(df, ventana=10):
    """Último día de las últimas `ventana` velas con suba >= EP_MIN_SUBA% y volumen >= EP_MIN_VOL x promedio 50."""
    if len(df) < 60: return None
    c, v = df.Close, df.Volume
    prom = sma(v, 50).shift(1)
    ch = c.pct_change() * 100
    n = len(df)
    for k in range(1, ventana + 1):
        i = n - k
        if prom.iloc[i] > 0 and ch.iloc[i] >= EP_MIN_SUBA and v.iloc[i] >= EP_MIN_VOL * prom.iloc[i]:
            return {"dias": k - 1, "fecha": df.index[i].strftime("%d-%m-%y"), "suba": num(ch.iloc[i], 1),
                    "vol_x": num(v.iloc[i] / prom.iloc[i], 1), "desde": num((c.iloc[-1] / c.iloc[i] - 1) * 100, 1),
                    "_idx": i, "_ts": df.index[i]}
    return None

def estadio(df):
    c = df.Close
    if len(c) < 221: return None
    e = ema(c, 200)
    arriba, sube = c.iloc[-1] > e.iloc[-1], e.iloc[-1] > e.iloc[-21]
    return 2 if arriba and sube else 3 if arriba else 1 if sube else 4

def estiramiento(df):
    """Distancia % del cierre a la EMA10 y a la EMA20, y el ADR% para medirla en ADRs."""
    c = df.Close
    if len(c) < 30: return 0.0, 0.0, 0.0
    d10 = (c.iloc[-1] / ema(c, 10).iloc[-1] - 1) * 100
    d20 = (c.iloc[-1] / ema(c, 20).iloc[-1] - 1) * 100
    return float(d10), float(d20), float(adr_pct(df))

def banderas(df, sav_d, earn_dias):
    f = []
    if len(df) < 60: return f
    c, h, l = df.Close.iloc[-1], df.High.iloc[-1], df.Low.iloc[-1]
    prev = df.iloc[:-1]
    hi_prev = prev[prev.index >= df.index[-1] - pd.Timedelta(days=365)].High.max()
    prom = sma(df.Volume, 50).iloc[-2]
    vol_x = df.Volume.iloc[-1] / prom if prom > 0 else 1
    rng = h - l
    if rng > 0 and h >= hi_prev * 0.98 and (h - c) / rng >= 0.6:
        f.append({"k": "rechazo", "c": "rechazo", "t": "Rechazo en máximos: mecha superior larga cerca del máximo de 52 semanas", "tipo": "bad"})
    if c > hi_prev and vol_x >= 1.5:
        f.append({"k": "maxvol", "c": "máx. + vol", "t": f"Rompió el máximo de 52 semanas con {vol_x:.1f}x de volumen", "tipo": "good"})
    rompe_hoy = c > df.High.iloc[-21:-1].max()
    if (rompe_hoy or (sav_d and sav_d["estado"] == "rompe")) and vol_x < 1.0:
        f.append({"k": "sinvol", "c": "sin volumen", "t": f"Ruptura con volumen bajo ({vol_x:.1f}x el promedio)", "tipo": "bad"})
    s50 = sma(df.Close, 50).iloc[-1]
    if s50 > 0 and c / s50 - 1 > EXTENDIDO_SMA50 / 100:
        f.append({"k": "ext", "c": "extendido", "t": f"Extendido: {(c / s50 - 1) * 100:.0f}% sobre la SMA50", "tipo": "warn"})
    d10, d20, adr = estiramiento(df)
    if adr > 0 and (d10 / adr > ESTIRADA_EMA10_ADR or d20 / adr > ESTIRADA_EMA20_ADR):
        f.append({"k": "estirada", "c": "estirada", "tipo": "warn",
                  "t": f"Estirada: {d10:.1f}% sobre la EMA10 ({d10 / adr:.1f} ADR) y {d20:.1f}% sobre la EMA20 ({d20 / adr:.1f} ADR)"})
    if earn_dias is not None and 0 <= earn_dias <= 7:
        f.append({"k": "earn", "c": "earnings " + ("hoy" if earn_dias == 0 else f"{earn_dias}d"),
                  "t": "Reporta earnings " + ("hoy" if earn_dias == 0 else f"en {earn_dias} días"), "tipo": "warn"})
    return f

# ---------------------------------------------------------------- régimen de mercado
def regimen(indices, vix, acciones):
    capas = []
    pts = mx = 0; det = []
    for t in ("SPY", "QQQ"):
        df = indices.get(t)
        if df is None or len(df) < 220: continue
        c = df.Close; p = c.iloc[-1]; e21, e50, e200 = ema(c, 21), ema(c, 50), ema(c, 200)
        # Tendencia (10): corto, medio y largo plazo; no alcanza con estar sobre la EMA200
        s_t = 2 * (p > e21.iloc[-1]) + 3 * (p > e50.iloc[-1]) + 3 * (p > e200.iloc[-1]) \
            + 2 * (e50.iloc[-1] > e200.iloc[-1] and e200.iloc[-1] > e200.iloc[-21])
        ch, vv = c.pct_change(), df.Volume
        dd = int(((ch <= -0.002) & (vv > vv.shift(1))).iloc[-25:].sum())
        s_d = {0: 8, 1: 8, 2: 7, 3: 5, 4: 3}.get(dd, 0)
        ext = (p - e50.iloc[-1]) / atr(df, 14).iloc[-1]
        s_e = 7 if 0 <= ext <= 3 else 4 if 0 < ext <= 5 else 1 if ext > 5 else 2
        sub = s_t + s_d + s_e
        if dd >= REG_DISTRIBUCION_TOPE: sub = min(sub, 12.5)  # distribución activa: tope al 50%
        pts += sub; mx += 25
        det.append(f"{t}: tendencia {int(s_t)}/10, {dd} días de distribución en 25 ruedas{' (tope por distribución)' if dd >= REG_DISTRIBUCION_TOPE else ''}, {ext:+.1f} ATR de la EMA50")
    if mx: capas.append({"nombre": "Índices SPY y QQQ", "pts": num(pts / mx * REG_PESO_INDICES, 1), "max": REG_PESO_INDICES, "det": det})
    acc = [d for d in acciones if len(d) >= 220]
    hist200 = []
    if len(acc) >= 50:
        try:
            cierres = pd.concat({i: d.Close for i, d in enumerate(acc)}, axis=1).sort_index()
            sobre = (cierres > cierres.ewm(span=200, adjust=False).mean()).where(cierres.notna())
            serie = sobre.mean(axis=1).iloc[-42:] * 100
            hist200 = [[f.strftime("%d-%m"), num(v, 1)] for f, v in serie.items() if pd.notna(v)]
        except Exception:
            hist200 = []
        pe200 = np.mean([d.Close.iloc[-1] > ema(d.Close, 200).iloc[-1] for d in acc])
        ps200 = np.mean([d.Close.iloc[-1] > d.Close.iloc[-200:].mean() for d in acc])
        p50 = np.mean([d.Close.iloc[-1] > ema(d.Close, 50).iloc[-1] for d in acc])
        p200 = (pe200 + ps200) / 2
        nh = sum(d.High.iloc[-1] >= d.High.iloc[-253:-1].max() for d in acc)
        nl = sum(d.Low.iloc[-1] <= d.Low.iloc[-253:-1].min() for d in acc)
        s1 = float(np.clip((p200 - 0.3) / 0.4, 0, 1) * 10)
        s2 = float(np.clip((p50 - 0.3) / 0.4, 0, 1) * 10)
        s3 = nh / (nh + nl) * 10 if nh + nl else 5.0
        capas.append({"nombre": "Amplitud del universo", "pts": num((s1 + s2 + s3) / 30 * REG_PESO_AMPLITUD, 1), "max": REG_PESO_AMPLITUD,
                      "det": [f"{pe200:.0%} de las acciones sobre la EMA200 y {ps200:.0%} sobre la SMA200", f"{p50:.0%} sobre la EMA50",
                              f"{nh} nuevos máximos de 52 semanas contra {nl} nuevos mínimos"]})
    if vix is not None and len(vix):
        v = float(vix.Close.iloc[-1])
        # Escala gradual por nivel y castigo si el VIX salta sobre su media de 50 ruedas (miedo en aumento)
        if v < 12: s = 14
        elif v <= 15: s = 20
        elif v <= 20: s = 20 - (v - 15) * 1.2
        elif v <= 25: s = 14 - (v - 20) * 1.2
        elif v <= 30: s = 8 - (v - 25) * 0.8
        else: s = 2
        m50 = float(vix.Close.iloc[-50:].mean()) if len(vix) >= 50 else v
        rel = v / m50 if m50 else 1
        if rel > 1.3: s -= 8
        elif rel > 1.15: s -= 4
        s = max(0.0, s)
        lect = "complacencia" if v < 12 else "calma" if v <= 16 else "normal" if v <= 20 else "tensión" if v <= 30 else "pánico"
        capas.append({"nombre": "Sentimiento (VIX)", "pts": num(s / 20 * REG_PESO_VIX, 1), "max": REG_PESO_VIX,
                      "det": [f"VIX en {v:.1f}: {lect} · {'+' if rel >= 1 else ''}{(rel - 1) * 100:.0f}% contra su media de 50 ruedas"]})
    if not capas: return None
    total = sum(c["pts"] for c in capas) / sum(c["max"] for c in capas) * 100
    # La exposición es una lectura del mercado, no un tamaño de posición
    if total < 40: et, rec, expo = "Defensivo", "Priorizá liquidez; solo seguimiento.", "0–25%"
    elif total < 60: et, rec, expo = "Cauteloso", "Posiciones chicas y solo los mejores setups.", "25–50%"
    elif total < 80: et, rec, expo = "Favorable", "Mercado acompaña: setups A+ con tamaño normal.", "50–75%"
    else: et, rec, expo = "Expansión", "Viento a favor: exposición plena en los líderes.", "75–100%"
    return {"score": num(total, 0), "etiqueta": et, "rec": rec, "expo": expo, "capas": capas, "hist200": hist200,
            "ftd": follow_through(indices), "fng": fear_greed() if MOSTRAR_FEAR_GREED else None}

def follow_through(indices):
    """Estado de O'Neil en SPY y QQQ: corrección, intento de rally (día N) o follow-through day (suba fuerte con más volumen desde el día 4)."""
    out = {}
    for t in ("SPY", "QQQ"):
        df = indices.get(t)
        if df is None or len(df) < 80: continue
        c, v = df.Close.values, df.Volume.values
        n = len(c)
        h = n - 60 + int(np.argmax(c[-60:]))           # máximo de cierre de las últimas 60 ruedas
        lo = h + int(np.argmin(c[h:]))                 # mínimo posterior a ese máximo
        tope = c[h]
        caida = (1 - c[lo] / tope) * 100
        est = {"t": t, "caida": num(caida, 1), "minimo": df.index[lo].strftime("%d-%m"), "dia": n - 1 - lo}
        if caida < FTD_CORRECCION_MIN:
            est["estado"] = "sin corrección"
        else:
            est["estado"] = "intento de rally" if n - 1 > lo else "corrección"
            for i in range(lo + 4, n):
                sube = (c[i] / c[i - 1] - 1) * 100
                if sube >= FTD_SUBA_MIN and v[i] > v[i - 1] and c[lo + 1:i + 1].min() > c[lo]:
                    est.update({"estado": "follow-through", "ftd": df.index[i].strftime("%Y-%m-%d"), "ftd_dia": i - lo, "suba": num(sube, 2)})
                    break
        out[t] = est
    return out

def fear_greed():
    """Fear & Greed de CNN (fuente no oficial; si falla queda s/d)."""
    import requests
    try:
        r = requests.get("https://production.dataviz.cnn.io/index/fearandgreed/graphdata", timeout=20, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*", "Origin": "https://edition.cnn.com", "Referer": "https://edition.cnn.com/"})
        f = r.json()["fear_and_greed"]
        es = {"extreme fear": "miedo extremo", "fear": "miedo", "neutral": "neutral", "greed": "codicia", "extreme greed": "codicia extrema"}
        return {"score": num(f["score"], 0), "rating": es.get(f.get("rating"), f.get("rating")),
                "semana": num(f.get("previous_1_week"), 0), "mes": num(f.get("previous_1_month"), 0)}
    except Exception as e:
        print(f"   ⚠️ Fear & Greed: {e}")
        return None

# ---------------------------------------------------------------- AVWAP
def avwap_desde(df, i):
    sub = df.iloc[i:]
    tp = (sub.High + sub.Low + sub.Close) / 3
    v = sub.Volume.fillna(0)
    return (tp * v).cumsum() / v.cumsum().replace(0, np.nan)

def anclas(df, tf, earn=None, es_ipo=False, ep_ts=None):
    n = len(df)
    if n < 10: return []
    L, k, lim_ath = (126, 5, 756) if tf == "d" else (52, 2, 156)
    ini = max(0, n - L)
    res = []
    if earn is not None:
        i = int(df.index.searchsorted(earn))
        if tf == "d" and i + 1 < n and df.Volume.iloc[i + 1] > df.Volume.iloc[i]:
            i += 1  # earnings después del cierre: la reacción es al día siguiente
        if i < n - 2: res.append(("Earnings", i))
    if ep_ts is not None:
        i = int(df.index.searchsorted(ep_ts))
        if i < n - 2: res.append(("Episodic pivot", i))
    seg = df.iloc[ini:n - k]
    if len(seg) and seg.Volume.max() > 0:
        res.append(("Alto volumen", df.index.get_loc(seg.Volume.idxmax())))
    seg = df.iloc[ini:n - k]
    if len(seg):
        res.append(("Máx. estructural", df.index.get_loc(seg.High.idxmax())))
    if n > k:
        i = int(np.argmax(df.High.values[:n - k]))
        if i < ini and i >= n - lim_ath: res.append(("Máx. histórico", i))
    seg = df.iloc[ini:n - k]
    if len(seg):
        res.append(("Mín. estructural", df.index.get_loc(seg.Low.idxmin())))
    # mínimo del último mes (21 ruedas o 4 semanas), sin contar las 2 últimas velas
    seg = df.iloc[max(0, n - (21 if tf == "d" else 4) - 2):n - 2]
    if len(seg):
        res.append(("Mín. mensual", df.index.get_loc(seg.Low.idxmin())))
    if n > k:
        i = int(np.argmin(df.Low.values[:n - k]))
        if i < ini and i >= n - lim_ath: res.append(("Mín. histórico", i))
    if es_ipo: res.append(("IPO", 0))
    vistos, out = set(), []
    for nom, i in res:
        if i not in vistos and i < n - 1:
            vistos.add(i); out.append((nom, int(i)))
    return out

def estado_avwap(df, nom, i, tf):
    av = avwap_desde(df, i)
    if av.isna().all() or len(av) < 2: return None
    c = df.Close.iloc[i:]
    val, precio = av.iloc[-1], c.iloc[-1]
    if not np.isfinite(val): return None
    dist = (precio / val - 1) * 100
    nb = VELAS_RUPTURA_DIARIO if tf == "d" else VELAS_RUPTURA_SEMANAL
    tope = DIST_POR_ROMPER_DIARIO if tf == "d" else DIST_POR_ROMPER_SEMANAL
    previas_abajo = bool((c.iloc[-nb - 1:-1] <= av.iloc[-nb - 1:-1]).any()) if len(c) > 1 else False
    vol_x = None
    if dist > 0 and previas_abajo:
        est = "rompe"
        # vela de la ruptura: la primera que cerró arriba después del último cierre debajo
        abajo = np.where((c.values[:-1] <= av.values[:-1]))[0]
        k = i + int(abajo[-1]) + 1 if len(abajo) else len(df) - 1
        prom = sma(df.Volume, 50 if tf == "d" else 20).shift(1).iloc[k]
        vol_x = float(df.Volume.iloc[k] / prom) if prom and prom > 0 else None
    elif dist <= 0 and dist >= -tope: est = "por romper"
    elif dist > 0: est = "arriba"
    else: est = "abajo"
    obj = df.High.iloc[i:len(df) - 1].max()
    obj = obj if obj > precio else None
    fuerte = nom in anclas_fuertes()
    cuenta = (est == "rompe" and vol_x is not None and vol_x >= VOL_RUPTURA) or (est == "por romper" and fuerte)
    return {"ancla": nom, "fecha": df.index[i].strftime("%d-%m-%y"), "valor": num(val, 4), "dist": num(dist),
            "estado": est, "objetivo": num(obj, 4), "vol_x": num(vol_x, 1) if vol_x is not None else None,
            "fuerte": fuerte, "cuenta": bool(cuenta)}

def _norm(x):
    import unicodedata
    x = unicodedata.normalize("NFKD", str(x).strip().lower()).encode("ascii", "ignore").decode()
    return x.replace("maximo", "max").replace("minimo", "min").replace(".", "").replace(" ", "")

def anclas_fuertes():
    """Nombres de ancla (como los arma el motor) que figuran en ANCLAS_FUERTES, sin importar tildes ni puntos."""
    pedidas = {_norm(x) for x in str(ANCLAS_FUERTES).split(",") if x.strip()}
    return {n for n in ("Earnings", "Episodic pivot", "Alto volumen", "Máx. estructural", "Máx. histórico",
                           "Mín. estructural", "Mín. mensual", "Mín. histórico", "IPO")
            if _norm(n) in pedidas}

def setup_avwap(df, avs):
    cand = [a for a in avs if a["cuenta"] and a["estado"] == "rompe"] or [a for a in avs if a["cuenta"] and a["estado"] == "por romper"]
    if not cand: return None
    b = min(cand, key=lambda a: abs(a["dist"]))
    precio = df.Close.iloc[-1]
    entrada = precio if b["estado"] == "rompe" else b["valor"] * 1.002
    stop = df.Low.iloc[-1]
    if stop >= entrada: stop = df.Low.iloc[-3:].min()
    obj = b["objetivo"]
    rr = (obj - entrada) / (entrada - stop) if obj and entrada > stop and obj > entrada else None
    return {"estado": b["estado"], "ancla": b["ancla"], "entrada": num(entrada, 4), "stop": num(stop, 4),
            "objetivo": obj, "rr": num(rr, 2)}

# ---------------------------------------------------------------- compresión / inside
def _met_comp(df, tf):
    a, b, bb, vs, vl, rg, look = (10, 50, 20, 10, 50, 10, 126) if tf == "d" else (4, 20, 10, 4, 20, 6, 104)
    if len(df) < b + 5: return None
    c = df.Close
    atr_r = atr(df, a).iloc[-1] / atr(df, b).iloc[-1]
    bw = (4 * c.rolling(bb).std() / sma(c, bb)).dropna().iloc[-look:]
    bb_pct = float((bw < bw.iloc[-1]).mean() * 100) if len(bw) > 10 else 50.0
    vol_r = sma(df.Volume, vs).iloc[-1] / sma(df.Volume, vl).iloc[-1] if sma(df.Volume, vl).iloc[-1] > 0 else 1.0
    rango = (df.High.iloc[-rg:].max() - df.Low.iloc[-rg:].min()) / c.iloc[-1] * 100
    s = 100 * (0.35 * np.clip((1.2 - atr_r) / 0.6, 0, 1) + 0.35 * np.clip(1 - bb_pct / 100, 0, 1)
               + 0.30 * np.clip((1.2 - vol_r) / 0.6, 0, 1))
    es = atr_r < 0.85 and bb_pct <= 30 and vol_r < 0.95
    return {"atr_r": atr_r, "bb_pct": bb_pct, "vol_r": vol_r, "rango": rango, "score": s, "es": bool(es),
            "gatillo": df.High.iloc[-rg:].max(), "piso": df.Low.iloc[-rg:].min(), "rg": rg, "vl": vl}

def emas_en_ascenso(df):
    """True si las EMAs de EMAS_ASCENSO vienen subiendo (hoy más alto que hace 5 velas)."""
    ns = [int(x) for x in str(EMAS_ASCENSO).replace(";", ",").split(",") if x.strip().isdigit()]
    if not ns or len(df) < max(ns) + 6: return False
    return all(ema(df.Close, n).iloc[-1] > ema(df.Close, n).iloc[-6] for n in ns)

def compresion(df, tf):
    m = _met_comp(df, tf)
    if m is None: return None
    ant = _met_comp(df.iloc[:-1], tf)
    vol_hoy = df.Volume.iloc[-1] / sma(df.Volume, m["vl"]).iloc[-2] if sma(df.Volume, m["vl"]).iloc[-2] > 0 else 0
    ruptura = bool(ant and ant["es"] and df.Close.iloc[-1] > ant["gatillo"] and vol_hoy >= VOL_RUPTURA)
    gat = ant["gatillo"] if ruptura else m["gatillo"]
    piso = ant["piso"] if ruptura else m["piso"]
    return {"score": num(m["score"], 1), "es": m["es"], "atr_r": num(m["atr_r"]), "bb_pct": num(m["bb_pct"], 0),
            "vol_r": num(m["vol_r"]), "rango": num(m["rango"], 1), "gatillo": num(gat, 4),
            "dist_gatillo": num((gat / df.Close.iloc[-1] - 1) * 100), "ruptura": ruptura, "vol_hoy": num(vol_hoy, 2),
            "piso": num(piso, 4), "riesgo": num((gat - piso) / gat * 100, 1) if gat > 0 else None,
            "emas": emas_en_ascenso(df)}

def inside(df):
    h, l = df.High.values, df.Low.values
    n, i = 0, len(df) - 1
    while i > 0 and h[i] <= h[i - 1] and l[i] >= l[i - 1] and n < 6:
        n += 1; i -= 1
    if n == 0: return {"n": 0}
    return {"n": n, "madre_hi": num(h[i], 4), "madre_lo": num(l[i], 4),
            "dist_hi": num((h[i] / df.Close.iloc[-1] - 1) * 100)}

# ---------------------------------------------------------------- pivot 30 min sobre EMA diaria
def lista_emas():
    return [int(x) for x in str(EMAS_DIARIO_PIVOT).replace(";", ",").replace("/", ",").split(",") if x.strip().isdigit()]

def toque_ema_diaria(dd):
    """Busca en las últimas DIAS_TOQUE_EMA velas diarias un toque o undercut a alguna EMA diaria.
    Devuelve (fecha, ema, valor de la EMA, cuántas ruedas atrás) o None."""
    emas = lista_emas()
    if dd is None or not emas or len(dd) < max(emas) + 5: return None
    tol = TOLERANCIA_TOQUE_EMA / 100
    series = {n: ema(dd.Close, n) for n in emas}
    for k in range(1, DIAS_TOQUE_EMA + 1):
        i = len(dd) - k
        lo, hi = dd.Low.iloc[i], dd.High.iloc[i]
        tocadas = [(n, series[n].iloc[i]) for n in emas
                   if lo <= series[n].iloc[i] * (1 + tol) and hi >= series[n].iloc[i]]
        if tocadas:
            n, v = min(tocadas, key=lambda x: abs(lo - x[1]))
            return dd.index[i], n, v, k - 1
    return None

def pivot_30m(m30, dd):
    """30 Min Pivot: tras el toque/undercut de una EMA diaria, la primera vela verde de 30 min
    después del mínimo marca la entrada (su máximo) y el stop (su mínimo)."""
    t = toque_ema_diaria(dd)
    if t is None or m30 is None or len(m30) < 5: return None
    dia, ne, ve, hace = t
    idx = m30.index.tz_localize(None) if getattr(m30.index, "tz", None) is not None else m30.index
    ini = int(np.searchsorted(idx.normalize(), pd.Timestamp(dia).normalize()))
    if ini >= len(m30): return None
    tol = TOLERANCIA_TOQUE_EMA / 100
    o, h, l, c = m30.Open.values, m30.High.values, m30.Low.values, m30.Close.values
    n = len(m30)
    toque = next((j for j in range(ini, n) if l[j] <= ve * (1 + tol)), None)
    if toque is None: return None
    piso = toque + int(np.argmin(l[toque:]))
    base = {"ema_n": ne, "ema": num(ve, 4), "toque": "hoy" if hace == 0 else ("ayer" if hace == 1 else f"hace {hace} ruedas"),
            "minimo": num(l[piso], 4)}
    verde = next((j for j in range(piso, n) if c[j] > o[j]), None)
    if verde is None:
        return {**base, "estado": "esperando", "entrada": None, "stop": None, "riesgo": None, "dist": None}
    entrada, stop = h[verde], l[verde]
    cruce = next((k for k in range(verde + 1, n) if h[k] > entrada), None)
    if cruce is not None:
        if cruce < n - 6: return None  # se disparó hace más de 3 horas
        est = "disparado"
    else:
        est = "armado"
    return {**base, "estado": est, "entrada": num(entrada, 4), "stop": num(stop, 4),
            "riesgo": num((entrada - stop) / entrada * 100), "dist": num((c[-1] / entrada - 1) * 100)}

# ---------------------------------------------------------------- bases VCP
def _zigzag(hi, lo, u):
    """Vaivenes de precio: alterna máximos (H) y mínimos (L) que se dan vuelta al menos `u` (fracción).
    Devuelve [(índice, precio, tipo)]; el último punto es el extremo en curso."""
    n = len(hi); piv = []
    if n < 3: return piv
    ih = il = 0; dirc = 0
    for i in range(1, n):
        if dirc == 0:
            if hi[i] > hi[ih]: ih = i
            if lo[i] < lo[il]: il = i
            if il < ih and hi[ih] >= lo[il] * (1 + u): piv.append((il, lo[il], "L")); dirc = 1
            elif ih < il and lo[il] <= hi[ih] * (1 - u): piv.append((ih, hi[ih], "H")); dirc = -1
        elif dirc == 1:
            if hi[i] >= hi[ih]: ih = i
            elif lo[i] <= hi[ih] * (1 - u): piv.append((ih, hi[ih], "H")); dirc = -1; il = i
        else:
            if lo[i] <= lo[il]: il = i
            elif hi[i] >= lo[il] * (1 + u): piv.append((il, lo[il], "L")); dirc = 1; ih = i
    if dirc == 1: piv.append((ih, hi[ih], "H"))
    elif dirc == -1: piv.append((il, lo[il], "L"))
    return piv

def _vcp_desde(j, piv, hi, lo):
    """Arma las contracciones a partir del máximo de la base piv[j]. Devuelve (contracciones, índice de ruptura o None)."""
    H0 = piv[j][1]
    contr, cur = [], (piv[j][0], H0)
    k = j + 1
    while k < len(piv):
        i, p, tp = piv[k]
        if tp == "L":
            if contr and p < contr[-1]["lo"] * (1 - VCP_TOLERANCIA / 100):   # perfora el mínimo anterior: misma contracción
                contr[-1].update(lo_i=i, lo=p)
            else:
                contr.append({"hi_i": cur[0], "hi": cur[1], "lo_i": i, "lo": p})
        else:
            if p > H0 * 1.005: break            # superó el máximo de la base
            if contr and p > contr[-1]["hi"] and _vcp_valida(contr):
                break                            # rompió el pivot con la base ya armada
            cur = (i, p)
        k += 1
    return contr

def _depth(c): return (c["hi"] - c["lo"]) / c["hi"] * 100

def _vcp_valida(contr):
    if len(contr) < VCP_MIN_CONTRACCIONES: return False
    d = [_depth(c) for c in contr]
    if d[0] > VCP_PRIMERA_MAX or d[0] < VCP_PRIMERA_MIN or any(d[x + 1] >= d[x] for x in range(len(d) - 1)): return False
    # techos planos o bajando: si los máximos de las contracciones suben, es una cuña, no una VCP
    if any(contr[x + 1]["hi"] > contr[x]["hi"] * (1 + VCP_TOLERANCIA / 100) for x in range(len(contr) - 1)): return False
    # el pivot tiene que estar en la parte alta de la base, no en el medio del rango
    alto, bajo = contr[0]["hi"], min(c["lo"] for c in contr)
    return alto > bajo and (contr[-1]["hi"] - bajo) / (alto - bajo) * 100 >= VCP_PIVOT_ARRIBA

def detectar_vcp(df):
    """Detecta una base VCP en velas diarias y su estado."""
    n = len(df)
    if n < 160: return None
    ventana = min(n - 1, VCP_SEMANAS_MAX * 5 + 30)
    d = df.iloc[-ventana:]
    hi, lo, cl, vo = d.High.values, d.Low.values, d.Close.values, d.Volume.values
    m = len(d)
    adr = adr_pct(df)
    piv = _zigzag(hi, lo, max(0.03, 0.8 * adr / 100))
    if len(piv) < 4: return None
    mejor = None
    for j, (i0, p0, tp) in enumerate(piv):
        if tp != "H" or m - 1 - i0 > VCP_SEMANAS_MAX * 5 or m - 1 - i0 < VCP_SEMANAS_MIN * 5: continue
        # tendencia previa: el máximo de la base tiene que estar lejos del mínimo de los 6 meses anteriores
        g = n - m + i0
        previo = df.Low.iloc[max(0, g - 126):g]
        if len(previo) < 40 or p0 / previo.min() - 1 < VCP_TENDENCIA_PREVIA / 100: continue
        contr = _vcp_desde(j, piv, hi, lo)
        if not contr: continue
        # contracción chica en curso desde el último máximo (bandera final apretada)
        ult = contr[-1]
        hs = [q for q in piv if q[2] == "H" and q[0] > ult["lo_i"]]
        if hs and hs[-1][0] == piv[-1][0] and all(q[1] < ult["hi"] for q in hs):
            h_i, h_p = hs[-1][0], hs[-1][1]
            if h_i < m - 1:
                l_i = h_i + 1 + int(np.argmin(lo[h_i + 1:]))
                if (h_p - lo[l_i]) / h_p * 100 >= 2:
                    contr = contr + [{"hi_i": h_i, "hi": h_p, "lo_i": l_i, "lo": lo[l_i]}]
        if not _vcp_valida(contr): continue
        if mejor is None or len(contr) > len(mejor[1]) or (len(contr) == len(mejor[1]) and i0 < mejor[0]):
            mejor = (i0, contr)
    if mejor is None: return None
    i0, contr = mejor
    ult = contr[-1]
    pivot, stop = ult["hi"], ult["lo"]
    vol50 = pd.Series(vo).rolling(50).mean().values
    # ruptura: el PRIMER cierre sobre el pivot después del mínimo de la última contracción (con o sin volumen).
    # El volumen de ruptura se mira en ese día y los 2 siguientes; si no aparece, es una ruptura sin volumen.
    b = next((x for x in range(ult["lo_i"] + 1, m) if cl[x] > pivot), None)
    sin_vol_rup = False
    if b is not None:
        vx = [vo[x] / vol50[x - 1] for x in range(b, min(m, b + 3)) if vol50[x - 1]]
        sin_vol_rup = not vx or max(vx) < VOL_RUPTURA
    # secado de volumen: promedio desde el inicio de la última contracción vs. promedio de 50 ruedas previo
    fin_c = (b - 1) if b is not None else m - 1
    ref = vol50[ult["hi_i"]] if not np.isnan(vol50[ult["hi_i"]]) else np.nanmean(vo[:ult["hi_i"] + 1])
    seco = float(np.mean(vo[ult["hi_i"]:fin_c + 1]) / ref) if ref and fin_c >= ult["hi_i"] else None
    dias = vol_b = None
    if b is not None:
        dias = m - 1 - b
        vx = [float(vo[x] / vol50[x - 1]) for x in range(b, min(m, b + 3)) if vol50[x - 1]]
        vol_b = max(vx) if vx else None
        if dias > VCP_DIAS_SEGUIMIENTO: return None
        if any(cl[x] < pivot for x in range(b + 1, m)): est = "fallo"
        elif sin_vol_rup and dias >= 1: est = "sinvol"  # si rompió hoy, el volumen del día todavía se está formando
        elif dias < VCP_DIAS_RUPTURA: est = "recien"
        else: est = "confirmo"
    else:
        dist = (pivot / cl[-1] - 1) * 100
        if cl[-1] < stop: return None
        if cl[-1] > pivot and _depth(ult) <= VCP_FORMANDO_MAX:
            est = "sinvol"   # cerró sobre el pivot pero sin el volumen de ruptura
        elif _depth(ult) <= VCP_ULTIMA_MAX and seco is not None and seco < VCP_VOL_SECO and dist <= VCP_DIST_PIVOT:
            est = "armada"
        elif _depth(ult) <= VCP_FORMANDO_MAX:
            est = "formandose"
        else:
            return None
    fin = b if b is not None else m - 1
    semanas = (fin - i0) / 5
    if semanas < VCP_SEMANAS_MIN: return None
    # serie para el gráfico de la ficha (desde un poco antes de la base)
    s0 = max(0, i0 - 10)
    serie = cl[s0:]
    paso = max(1, len(serie) // 140)
    fecha = lambda x: d.index[x].strftime("%d-%m-%y")
    return {
        "estado": est, "contr": [num(_depth(c), 1) for c in contr], "semanas": num(semanas, 0),
        "pivot": num(pivot, 4), "stop": num(stop, 4), "riesgo": num((pivot - stop) / pivot * 100, 1),
        "dist": num((cl[-1] / pivot - 1) * 100), "seco": num(seco, 2) if seco is not None else None,
        "vol_rup": num(vol_b, 1) if vol_b is not None else None, "dias_rup": dias,
        "inicio": fecha(i0), "maximo": num(contr[0]["hi"], 4),
        "serie": [num(x, 4) for x in serie[::paso]] + ([num(serie[-1], 4)] if (len(serie) - 1) % paso else []),
        "marcas": [[round((c["hi_i"] - s0) / max(1, len(serie) - 1), 4), round((c["lo_i"] - s0) / max(1, len(serie) - 1), 4)] for c in contr],
    }

# ---------------------------------------------------------------- cierres semanales apretados
def cierres_apretados(df, wk, vcp=None):
    """Cierres semanales consecutivos (solo semanas terminadas) dentro de TC_RANGO_MAX %, contando desde la última."""
    if len(wk) < 12: return None
    w = wk if df.index[-1] >= wk.index[-1] else wk.iloc[:-1]  # la semana en curso todavía no cerró
    c = w.Close.values
    n, hi, lo = 1, c[-1], c[-1]
    for x in c[-2::-1]:
        h, l = max(hi, x), min(lo, x)
        if (h - l) / l * 100 > TC_RANGO_MAX: break
        n, hi, lo = n + 1, h, l
    if n < TC_MIN_CIERRES: return None
    previas = w.Volume.iloc[-n - 10:-n]
    vol_x = w.Volume.iloc[-n:].mean() / previas.mean() if len(previas) and previas.mean() > 0 else None
    ref = vcp["pivot"] if vcp and vcp.get("pivot") else w.High.iloc[-10:].max()
    dist = (df.Close.iloc[-1] / ref - 1) * 100 if ref else None
    seco = vol_x is not None and vol_x < TC_VOL_SECO
    cerca = dist is not None and -TC_CERCA_PIVOT <= dist <= 0.5
    return {"n": n, "rango": num((hi - lo) / lo * 100, 2), "vol_x": num(vol_x, 2) if vol_x is not None else None,
            "dist": num(dist, 1) if dist is not None else None, "seco": bool(seco), "cerca": bool(cerca),
            "desde": w.index[-n].strftime("%d-%m-%y")}

# ---------------------------------------------------------------- retorno del top del score
ARCHIVO_HISTORIAL = "historial_top.json"

def cargar_historial(archivo):
    """Historial guardado entre corridas, completado con la semilla del repo (semillas/) para los días que falten."""
    import os
    try: hist = json.load(open(archivo))
    except Exception: hist = {}
    try:
        try: semilla = json.load(open(os.path.join("semillas", archivo)))
        except Exception: semilla = json.loads(zlib.decompress(base64.b64decode(SEMILLAS[archivo])).decode())
        ult = max(semilla)
        # La semilla manda en los días reconstruidos; su último día solo completa si la corrida en vivo no lo tiene
        for f, v in semilla.items():
            if f < ult: hist[f] = v
            else: hist.setdefault(f, v)
    except Exception:
        pass
    return hist

def top_retorno(activos, fecha, spy, diario=None):
    """Guarda el top del día y mide el retorno de las TOP_N actuales desde que entraron (dentro de TOP_RUEDAS) contra el SPY."""
    hist = cargar_historial(ARCHIVO_HISTORIAL)
    rank = sorted(activos, key=lambda a: -a["score"])
    hist[fecha] = {a["t"]: [a["score"], a["precio"]] for a in rank[:max(30, TOP_N)]}
    fechas = sorted(hist)[-60:]
    hist = {f: hist[f] for f in fechas}
    try: json.dump(hist, open(ARCHIVO_HISTORIAL, "w"))
    except Exception: pass
    ventana = fechas[-TOP_RUEDAS:]
    tops = {f: [t for t, _ in sorted(hist[f].items(), key=lambda x: -x[1][0])[:TOP_N]] for f in ventana}
    filas = []
    for a in rank[:TOP_N]:
        # Entrada = primera vez que figuró en el Top dentro de la ventana (aunque haya salido y vuelto)
        entro = next((f for f in ventana if a["t"] in tops[f]), fecha)
        base = hist[entro][a["t"]][1]
        filas.append({"t": a["t"], "score": a["score"], "entro": entro, "ret": num((a["precio"] / base - 1) * 100, 2) if base else None,
                      "spark": a["spark_d"][-max(TOP_RUEDAS, 10):]})
    r_spy = None
    if spy is not None and len(ventana):
        ini = spy[spy.index <= pd.Timestamp(ventana[0])]
        if len(ini): r_spy = num((spy.iloc[-1] / ini.iloc[-1] - 1) * 100, 2)
    rets = [f["ret"] for f in filas if f["ret"] is not None]
    # Segunda lectura (estilo Warren): de todas las que pasaron por el Top en la ventana, las TOP_N que más ganaron desde que entraron.
    # Es optimista: elige las mejores sabiendo el resultado.
    mejores = []
    hoy_top = set(tops[fecha]) if fecha in tops else set()
    for t in {t for f in ventana for t in tops[f]}:
        entro = next(f for f in ventana if t in tops[f])
        base = hist[entro][t][1]
        d = diario.get(t) if diario else None
        ahora = float(d.Close.iloc[-1]) if d is not None and len(d) else None
        if not base or not ahora: continue
        ult = max(f for f in ventana if t in hist[f])
        mejores.append({"t": t, "score": hist[ult][t][0], "entro": entro, "ret": num((ahora / base - 1) * 100, 2), "sigue": t in hoy_top,
                        "spark": [num(x, 4) for x in d.Close.iloc[-max(TOP_RUEDAS, 10):].values]})
    mejores = sorted(mejores, key=lambda x: -x["ret"])[:TOP_N]
    rm = [x["ret"] for x in mejores]
    hoy30 = [a["t"] for a in rank[:30]]
    ant30 = set(sorted(hist[fechas[-2]], key=lambda t: -hist[fechas[-2]][t][0])[:30]) if len(fechas) >= 2 else None
    nuevos = [t for t in hoy30 if ant30 is not None and t not in ant30]
    return {"nuevos": nuevos, "nuevos_desde": fechas[-2] if len(fechas) >= 2 else None, "ruedas": len(ventana), "desde": ventana[0] if ventana else fecha, "spy": r_spy,
            "medio": num(sum(rets) / len(rets), 2) if rets else None, "filas": filas,
            "mejores": mejores, "medio_mejores": num(sum(rm) / len(rm), 2) if rm else None}

# ---------------------------------------------------------------- seleccionadas: track record y alertas
ARCHIVO_SEL = "historial_sel.json"
ARCHIVO_ALERTAS = "alertas_enviadas.json"

def es_seleccionada(a):
    return not a["sin_av"] and a["rs"] >= SEL_RS_MIN and a["mv"] >= SEL_MINERVINI_MIN and a["score"] >= SEL_SCORE_MIN

def track_seleccionadas(activos, fecha, diario, spy):
    """Guarda las Seleccionadas del día y mide el retorno de cada ingreso de las últimas SEL_HISTORIA_RUEDAS ruedas vs el SPY."""
    hist = cargar_historial(ARCHIVO_SEL)
    hist[fecha] = {a["t"]: a["precio"] for a in activos if es_seleccionada(a)}
    fechas = sorted(hist)[-120:]
    hist = {f: hist[f] for f in fechas}
    try: json.dump(hist, open(ARCHIVO_SEL, "w"))
    except Exception: pass
    ventana = fechas[-SEL_HISTORIA_RUEDAS:]
    hoy = set(hist[fecha])
    filas = []
    for k, f in enumerate(ventana):
        previo = set(hist[ventana[k - 1]]) if k > 0 else set(hist[fechas[fechas.index(f) - 1]]) if fechas.index(f) > 0 else set()
        for t, px in hist[f].items():
            if t in previo or not px: continue  # solo el día que entró
            d = diario.get(t)
            if d is None: continue
            ahora = float(d.Close.iloc[-1])
            r_spy = None
            if spy is not None:
                ini = spy[spy.index <= pd.Timestamp(f)]
                if len(ini): r_spy = num((spy.iloc[-1] / ini.iloc[-1] - 1) * 100, 2)
            filas.append({"t": t, "entro": f, "px": num(px, 2), "ahora": num(ahora, 2), "ret": num((ahora / px - 1) * 100, 2),
                          "spy": r_spy, "sigue": t in hoy})
    rets = [x["ret"] for x in filas]; spys = [x["spy"] for x in filas if x["spy"] is not None]
    viejas = [x["ret"] for x in filas if x["entro"] < fecha]  # las que entraron hoy todavía no tienen resultado
    gan = sum(1 for x in viejas if x > 0)
    previo_hoy = set(hist[fechas[-2]]) if len(fechas) >= 2 else None
    nuevas = sorted(hoy - previo_hoy) if previo_hoy is not None else []
    return {"nuevas": nuevas, "ruedas": len(ventana), "desde": ventana[0] if ventana else fecha, "n": len(filas),
            "medio": num(sum(rets) / len(rets), 2) if rets else None, "spy": num(sum(spys) / len(spys), 2) if spys else None,
            "aciertos": num(gan / len(viejas) * 100, 0) if viejas else None,
            "filas": sorted(filas, key=lambda x: x["entro"], reverse=True)[:40]}

def armar_resumen(activos, fecha, reg, selh, rot, diario, macro=None):
    """Panorama del mercado y plan para la rueda siguiente, en HTML de Telegram."""
    f2 = lambda x, d=1: f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    sg = lambda x: ("+" if x > 0 else "") + f2(x, 2) + "%"
    L = [f"📊 <b>{NOMBRE_DASHBOARD} · resumen del {pd.Timestamp(fecha).strftime('%d-%m')}</b>", ""]
    if reg:
        L.append(f"<b>Mercado: {reg['etiqueta']} ({reg['score']:.0f}/100)</b> · exposición sugerida {reg.get('expo', '')}")
        idx = []
        for t in ("SPY", "QQQ", "IWM"):
            d = diario.get(t)
            if d is not None and len(d) > 1: idx.append(f"{t} {sg((d.Close.iloc[-1] / d.Close.iloc[-2] - 1) * 100)}")
        if idx: L.append(" · ".join(idx))
        for c in reg["capas"]:
            for x in c["det"]: L.append(f"• {x}")
        h = reg.get("hist200") or []
        if len(h) > 10:
            a, b = h[-1][1], h[-11][1]
            L.append(f"• Amplitud {'mejorando' if a > b + 2 else 'empeorando' if a < b - 2 else 'estable'}: {f2(a, 0)}% sobre la EMA200 (hace 10 ruedas {f2(b, 0)}%)")
        # Sentimiento en una línea: miedo por VIX, presión vendedora por días de distribución y tendencia de la amplitud
        import re
        txt = " ".join(x for c in reg["capas"] for x in c["det"])
        vix = re.search(r"VIX en ([\d.]+): (\w+)(?: · ([+-]?\d+)% contra)?", txt)
        dd = [int(x) for x in re.findall(r"(\d+) días de distribución", txt)]
        partes = []
        if vix: partes.append({"complacencia": "complacencia (cuidado con el exceso de confianza)", "calma": "calma", "normal": "volatilidad normal",
                               "tensión": "tensión", "pánico": "pánico"}.get(vix.group(2), vix.group(2)) + f" (VIX {f2(float(vix.group(1)))}" + (", subiendo fuerte" if vix.group(3) and int(vix.group(3)) >= 15 else "") + ")")
        if dd: partes.append("presión vendedora en los índices" if max(dd) >= 6 else "distribución moderada" if max(dd) >= 4 else "sin distribución relevante")
        if len(h) > 10: partes.append("la amplitud acompaña" if h[-1][1] >= h[-11][1] else "la amplitud se deteriora")
        fg = reg.get("fng")
        if fg: partes.append(f"Fear & Greed de CNN en {fg['score']:.0f} ({fg['rating']}; hace una semana {fg['semana']:.0f})")
        if partes: L.append("<b>Sentimiento:</b> " + ", ".join(partes) + ".")
        for t, e in (reg.get("ftd") or {}).items():
            if e["estado"] == "follow-through": L.append(f"• {t}: follow-through day el {pd.Timestamp(e['ftd']).strftime('%d-%m')} (día {e['ftd_dia']} del rally, +{f2(e['suba'], 2)}%)")
            elif e["estado"] == "intento de rally": L.append(f"• {t}: intento de rally, día {e['dia']} desde el mínimo del {e['minimo']} (cayó {f2(e['caida'], 1)}%); falta el follow-through")
        if fg and fg["score"] <= 25:
            L.append("<i>Miedo extremo: buen momento para armar la lista de seguimiento; para comprar rupturas conviene esperar el follow-through.</i>")
        L.append(f"<i>{reg['rec']}</i>")
    if rot and rot.get("etfs"):
        lid, mej, deb = [], [], []
        for e in rot["etfs"]:
            x, y = e["x"][-1], e["y"][-1]
            (lid if x >= 0 and y >= 0 else mej if x < 0 and y >= 0 else deb if x >= 0 else []).append(e["t"])
        L += ["", f"<b>Rotación:</b> liderando {', '.join(lid[:8]) or 'ninguno'} · mejorando {', '.join(mej[:6]) or 'ninguno'} · se debilitan {', '.join(deb[:6]) or 'ninguno'}"]
    sel = sorted([a for a in activos if es_seleccionada(a)], key=lambda a: -a["score"])
    L += ["", f"<b>Seleccionadas: {len(sel)}</b>" + (f" · nuevas hoy: {', '.join(selh.get('nuevas', [])[:12])}" if selh and selh.get("nuevas") else "")]
    if sel: L.append("Top 5: " + ", ".join(f"{a['t']} ({a['score']:.0f})" for a in sel[:5]))
    armadas = []
    for a in sel:
        v, s_ = a.get("vcp"), (a.get("setup_av") or {}).get("d")
        if v and v.get("pivot") and (v["estado"] == "armada" or (v.get("dist") is not None and -RESUMEN_CERCA <= v["dist"] <= 0)):
            armadas.append(f"• <b>{a['t']}</b> VCP {v['estado']} · pivot {f2(v['pivot'], 2)} · stop {f2(v['stop'], 2)} · a {f2(abs(v['dist']), 1)}%")
        elif s_ and s_["estado"] == "por romper" and s_.get("entrada"):
            dist = (s_["entrada"] / a["precio"] - 1) * 100
            if dist <= RESUMEN_CERCA:
                armadas.append(f"• <b>{a['t']}</b> AVWAP {s_['ancla'].lower()} · entrada {f2(s_['entrada'], 2)} · stop {f2(s_['stop'], 2)} · a {f2(dist, 1)}%")
    L += ["", f"<b>Armadas para mañana ({len(armadas)}):</b>"] + (armadas[:12] or ["Ninguna a menos de " + f2(RESUMEN_CERCA, 0) + "% del gatillo."])
    if macro:
        man = (ahora_ar().date() + dt.timedelta(days=1)).isoformat()
        prox = [m for m in macro if m["fecha"] == man] or [m for m in macro if m["fecha"] > ahora_ar().date().isoformat()][:4]
        if prox:
            L += ["", "<b>Macro próxima rueda:</b>"] + [f"• {pd.Timestamp(m['fecha']).strftime('%d-%m')} {m['hora']} {m['titulo']}"
                                                     + (f" (est. {m['est']}, ant. {m['ant']})" if m['est'] or m['ant'] else "") for m in prox[:6]]
    ev = sorted([a for a in sel if a.get("earn_dias") is not None and 0 <= a["earn_dias"] <= 3], key=lambda a: a["earn_dias"])
    if ev:
        cuando = lambda d: "hoy" if d == 0 else "mañana" if d == 1 else f"en {d} días"
        L += ["", "<b>Earnings (3 días):</b> " + ", ".join(f"{a['t']} {cuando(a['earn_dias'])}" for a in ev)]
    return "\n".join(L)[:3900]

def alertas_telegram(activos, fecha, resumen=None, regimen_ftd=None):
    """Manda por Telegram las Seleccionadas que hoy rompen su pivot VCP o su AVWAP con volumen (una vez por día y ticker)."""
    import os, requests
    token = os.environ.get("TELEGRAM_TOKEN", "").strip()
    if not ALERTAS_TELEGRAM or not token: return 0
    chat = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    api = f"https://api.telegram.org/bot{token}"
    try:
        if not chat:
            # Sin chat configurado: se usa el último chat que le escribió al bot
            j = requests.get(api + "/getUpdates", timeout=20).json()
            if not j.get("ok"):
                print(f"   ⚠️ Telegram rechazó el token: {j.get('description')}"); return 0
            res = j.get("result", [])
            chats = [(u.get("message") or u.get("my_chat_member") or {}).get("chat", {}).get("id") for u in res]
            chats = [c for c in chats if c]
            chat = str(chats[-1]) if chats and chats[-1] else ""
        if not chat:
            print("   ⚠️ Telegram: mandale cualquier mensaje al bot para que sepa a qué chat escribir"); return 0
        try: env = json.load(open(ARCHIVO_ALERTAS))
        except Exception: env = {}
        conectado = env.get("_conectado")
        env = {k: v for k, v in env.items() if v >= (dt.date.today() - dt.timedelta(days=7)).isoformat()}
        msgs = []
        if not conectado:
            # Primer uso: un mensaje de prueba para confirmar que el bot llega
            msgs.append(f"✅ <b>{NOMBRE_DASHBOARD}</b> conectado. Te aviso acá cuando una Seleccionada rompa su pivot VCP o una AVWAP con volumen.")
        env["_conectado"] = "9999-12-31"
        for t, e in ((regimen_ftd or {}).items()):
            if e.get("estado") == "follow-through" and e.get("ftd") == fecha and f"_ftd:{t}:{fecha}" not in env:
                msgs.append(f"🟢 <b>Follow-through day en {t}</b>: +{e['suba']:.2f}% con más volumen, día {e['ftd_dia']} del rally. "
                            "Señal clásica de O'Neil para volver a comprar rupturas.")
                env[f"_ftd:{t}:{fecha}"] = fecha
        if resumen and f"_resumen:{fecha}" not in env:
            msgs.append(resumen); env[f"_resumen:{fecha}"] = fecha
        for a in activos:
            if not es_seleccionada(a): continue
            v, s_ = a.get("vcp"), (a.get("setup_av") or {}).get("d")
            motivo = None
            if v and v["estado"] == "recien" and (v.get("vol_rup") or 0) >= VOL_RUPTURA:
                motivo = f"rompió el pivot VCP {v['pivot']:.2f} con {v['vol_rup']:.1f}x de volumen"
            elif s_ and s_["estado"] == "rompe":
                motivo = f"rompió la AVWAP {s_['ancla'].lower()} (entrada {s_['entrada']:.2f}, stop {s_['stop']:.2f})"
            # Una ruptura sigue "activa" varias velas: el mismo ticker y tipo no se repite por 7 días
            clave = f"{a['t']}:{'vcp' if motivo and motivo.startswith('rompió el pivot') else 'avwap'}"
            if motivo and clave not in env:
                msgs.append(f"🚀 <b>{a['t']}</b> {motivo}\nScore {a['score']:.0f} · RS {a['rs']:.0f} · {a['mv']}/8 · ${a['precio']:.2f}")
                env[clave] = fecha
        enviados = 0
        for m in msgs:
            r = requests.post(api + "/sendMessage", timeout=20, data={"chat_id": chat, "parse_mode": "HTML", "disable_web_page_preview": "true",
                                                                     "text": m + f"\n<a href=\"{URL_DASHBOARD}\">Abrir dashboard</a>"}).json()
            if r.get("ok"): enviados += 1
            else: print(f"   ⚠️ Telegram no mandó el mensaje: {r.get('description')}")
        if enviados or not msgs: json.dump(env, open(ARCHIVO_ALERTAS, "w"))
        return enviados
    except Exception as e:
        print(f"   ⚠️ Telegram: {e}"); return 0

# ---------------------------------------------------------------- rotación (cuadrantes tipo RRG)
def rs_semanas(diario):
    """RS (percentil del universo) de cada activo en las últimas ROTACION_SEMANAS + 1 semanas, de la más vieja a la más nueva."""
    sem = ROTACION_SEMANAS + 1
    arr = {t: df.Close.values for t, df in diario.items() if len(df) >= 60}
    def rsb(c, e):
        def r(n): return c[e] / c[e - n] - 1 if e - n >= 0 else c[e] / c[0] - 1
        return 0.4 * r(63) + 0.2 * r(126) + 0.2 * r(189) + 0.2 * r(252)
    por_semana = []
    for k in range(sem - 1, -1, -1):
        crudo = {t: rsb(c, len(c) - 1 - 5 * k) for t, c in arr.items() if len(c) - 1 - 5 * k >= 60}
        por_semana.append(pd.Series(crudo).rank(pct=True) * 98 + 1)
    return por_semana

def rotacion(diario, etfs, por_semana=None):
    """Cuadrantes tipo RRG contra el SPY, en semanal.
    X = fuerza relativa: % de la línea ETF/SPY sobre su media de 10 semanas (0 = igual que el SPY).
    Y = momentum de esa fuerza: cambio de X en las últimas 4 semanas (positivo = acelera)."""
    sem = ROTACION_SEMANAS + 1
    spy = diario.get("SPY")
    if spy is None: return None
    w_spy = spy.Close.resample("W-FRI").last()
    out = []
    for t, n in etfs.items():
        if t == "SPY" or t not in diario: continue
        w = diario[t].Close.resample("W-FRI").last()
        rs = (w / w_spy).dropna()
        if len(rs) < sem + 16: continue
        x = (rs / rs.rolling(10).mean() - 1) * 100
        y = x - x.shift(4)
        out.append({"t": t, "n": n, "x": [num(v, 2) for v in x.iloc[-sem:]], "y": [num(v, 2) for v in y.iloc[-sem:]]})
    return {"fechas": [f.strftime("%d-%m") for f in w_spy.index[-sem:]], "etfs": out}

MACRO_ES = {
    "Unemployment Claims": "Pedidos de desempleo", "Non-Farm Employment Change": "Nóminas no agrícolas (NFP)",
    "Unemployment Rate": "Tasa de desempleo", "Average Hourly Earnings m/m": "Salarios por hora m/m",
    "ADP Non-Farm Employment Change": "Empleo privado ADP", "JOLTS Job Openings": "Vacantes laborales (JOLTS)",
    "CPI m/m": "Inflación (IPC) m/m", "CPI y/y": "Inflación (IPC) a/a", "Core CPI m/m": "IPC núcleo m/m",
    "PPI m/m": "Precios mayoristas (IPP) m/m", "Core PPI m/m": "IPP núcleo m/m",
    "Core PCE Price Index m/m": "PCE núcleo m/m", "PCE Price Index m/m": "PCE m/m",
    "Federal Funds Rate": "Decisión de tasa de la Fed", "FOMC Statement": "Comunicado de la Fed",
    "FOMC Press Conference": "Conferencia de prensa de Powell", "FOMC Meeting Minutes": "Minutas de la Fed",
    "Fed Chair Powell Speaks": "Habla Powell", "Advance GDP q/q": "PIB (adelanto) t/t", "Prelim GDP q/q": "PIB (preliminar) t/t",
    "Final GDP q/q": "PIB (final) t/t", "Retail Sales m/m": "Ventas minoristas m/m", "Core Retail Sales m/m": "Ventas minoristas núcleo m/m",
    "ISM Manufacturing PMI": "ISM manufacturero", "ISM Services PMI": "ISM servicios",
    "Flash Manufacturing PMI": "PMI manufacturero (S&P, flash)", "Flash Services PMI": "PMI de servicios (S&P, flash)",
    "Prelim UoM Consumer Sentiment": "Confianza del consumidor Michigan (prelim.)",
    "Revised UoM Consumer Sentiment": "Confianza del consumidor Michigan (final)",
    "Prelim UoM Inflation Expectations": "Expectativas de inflación Michigan (prelim.)",
    "Revised UoM Inflation Expectations": "Expectativas de inflación Michigan (final)",
    "CB Consumer Confidence": "Confianza del consumidor (Conference Board)", "Durable Goods Orders m/m": "Bienes durables m/m",
    "Core Durable Goods Orders m/m": "Bienes durables núcleo m/m", "Empire State Manufacturing Index": "Índice manufacturero Empire State",
    "Philly Fed Manufacturing Index": "Índice manufacturero Fed de Filadelfia",
}

def eventos_macro():
    """Datos macro de EE.UU. de alto y medio impacto (calendario de Forex Factory), en hora de Argentina."""
    import requests
    hdr = {"User-Agent": "Mozilla/5.0"}
    filas = []
    for sem in ("thisweek", "nextweek"):
        try:
            r = requests.get(f"https://nfs.faireconomy.media/ff_calendar_{sem}.json", headers=hdr, timeout=20)
            if r.ok: filas += r.json()
        except Exception as e:
            print(f"   ⚠️ Calendario macro ({sem}): {e}")
    hoy = ahora_ar().date()
    out, vistos = [], set()
    for f in filas:
        if f.get("country") != "USD" or f.get("impact") not in ("High", "Medium"): continue
        tit = f.get("title", "")
        # Discursos de miembros de la Fed, subastas y similares: ruido para operar
        if f["impact"] == "Medium" and any(x in tit for x in ("Speaks", "Auction", "Bond", "Treasury", "Holiday")): continue
        try: cuando = pd.Timestamp(f["date"]).tz_convert("America/Argentina/Buenos_Aires")
        except Exception: continue
        if not (0 <= (cuando.date() - hoy).days <= EVENTOS_DIAS): continue
        clave = (tit, cuando.isoformat())
        if clave in vistos: continue
        vistos.add(clave)
        out.append({"fecha": cuando.strftime("%Y-%m-%d"), "hora": cuando.strftime("%H:%M"), "titulo": MACRO_ES.get(tit, tit),
                    "impacto": "alto" if f["impact"] == "High" else "medio", "est": f.get("forecast") or "", "ant": f.get("previous") or ""})
    return sorted(out, key=lambda x: (x["fecha"], x["hora"]))

def calendario_earnings(radar):
    """Earnings de la semana desde el calendario de NASDAQ (una consulta por día): empresas grandes y todas las del radar."""
    import requests
    out = []
    hoy = ahora_ar().date()
    for k in range(EVENTOS_DIAS + 1):
        d = hoy + dt.timedelta(days=k)
        if d.weekday() >= 5: continue
        try:
            r = requests.get(f"https://api.nasdaq.com/api/calendar/earnings?date={d.isoformat()}", timeout=20,
                             headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
            filas = ((r.json() or {}).get("data") or {}).get("rows") or []
        except Exception as e:
            print(f"   ⚠️ Calendario de earnings {d}: {e}"); continue
        for f in filas:
            t = str(f.get("symbol", "")).strip().replace("/", "-").replace(".", "-")
            try: mcap = float(str(f.get("marketCap", "")).replace("$", "").replace(",", "") or 0)
            except ValueError: mcap = 0
            if mcap < EVENTOS_EARN_MCAP_MIN and t not in radar: continue
            tm = f.get("time") or ""
            out.append({"fecha": d.isoformat(), "t": t, "n": (f.get("name") or t).strip(), "mcap": mcap,
                        "mom": "PRE" if "pre" in tm else "POST" if "after" in tm else "", "eps": f.get("epsForecast") or ""})
    return out

def cartelera(diario, tickers, nombres, mcaps=None):
    """Las que más suben y más bajan hoy entre las acciones líquidas."""
    ch = {t: (diario[t].Close.iloc[-1] / diario[t].Close.iloc[-2] - 1) * 100 for t in tickers if len(diario[t]) > 1}
    orden = sorted(ch, key=lambda t: -ch[t])
    mc = lambda t: num((mcaps or {}).get(t), 0) if (mcaps or {}).get(t) else None
    fila = lambda t: {"t": t, "n": nombres.get(t, t), "chg": num(ch[t], 2), "precio": num(diario[t].Close.iloc[-1], 2), "mcap": mc(t)}
    N = CARTELERA_N * 8  # de más, para que el dashboard pueda filtrar por grandes y seguir mostrando CARTELERA_N
    r = {t: float(rsi(diario[t].Close).iloc[-1]) for t in tickers if len(diario[t]) > 30}
    r = {t: v for t, v in r.items() if np.isfinite(v)}
    fr = lambda t: {"t": t, "n": nombres.get(t, t), "rsi": num(r[t], 1), "chg": num(ch.get(t), 2), "mcap": mc(t)}
    caro = sorted([t for t in r if r[t] >= RSI_SOBRECOMPRA], key=lambda t: -r[t])[:N]
    barato = sorted([t for t in r if r[t] <= RSI_SOBREVENTA], key=lambda t: r[t])[:N]
    return {"suben": [fila(t) for t in orden[:N]], "bajan": [fila(t) for t in orden[::-1][:N]],
            "sobrecompra": [fr(t) for t in caro], "sobreventa": [fr(t) for t in barato]}

# ---------------------------------------------------------------- score
def partes_score(mv, rs, comp_d, sav_d, comp_d_rup, ins_d, piv, vcp=None, fund=None, tc=None):
    tend = mv / 8 * PUNTOS_TENDENCIA
    fuer = rs / 99 * PUNTOS_RS
    contr = (comp_d["score"] if comp_d else 0) / 100 * PUNTOS_COMPRESION
    setup = 0.0
    if sav_d:
        setup += 12 if sav_d["estado"] == "rompe" else 7
    if comp_d_rup: setup += 6
    if ins_d and ins_d.get("n", 0) >= 1: setup += 3 if ins_d["n"] == 1 else 5
    if piv and piv.get("estado") != "esperando": setup += 4
    if vcp:
        e = vcp["estado"]
        if e == "armada": setup += 6
        elif e == "recien": setup += 8 if (vcp["vol_rup"] or 0) >= VOL_RUPTURA else 4
        elif e == "confirmo": setup += 4
    if tc: setup += TC_PUNTOS + (2 if tc["seco"] and tc["cerca"] else 0)
    fu = (fund["pts_eps"] + fund["pts_ventas"]) if (fund and PUNTOS_FUNDAMENTALES > 0) else 0.0
    return {"tend": num(tend, 1), "rs": num(fuer, 1), "contr": num(contr, 1),
            "setup": num(min(setup, 20) / 20 * PUNTOS_SETUP, 1), "fund": num(fu, 1)}

def spark(s, n): return [num(x, 4) for x in s.iloc[-n:].values]

def _comprimida(a):
    return any(a["comp"][k] and (a["comp"][k]["es"] or a["comp"][k]["ruptura"]) for k in ("d", "w"))

def lista_foco(activos):
    """Hasta FOCO_MAXIMO activos con un setup concreto para operar, sin banderas malas, por score."""
    out = []
    for a in activos:
        if a["rs"] < FOCO_RS_MINIMO: continue
        if any(f["k"] in ("rechazo", "sinvol", "ext", "estirada", "earn") for f in a["flags"]): continue
        precio, op = a["precio"], []
        v = a["vcp"]
        if v and v["estado"] in ("armada", "recien"):
            op.append(("VCP " + ("armada" if v["estado"] == "armada" else "recién rota"), v["pivot"], v["stop"]))
        c = a["comp"]["d"]
        if c and c["emas"] and (c["ruptura"] or (c["es"] and c["dist_gatillo"] is not None and c["dist_gatillo"] <= CERCA_GATILLO)):
            op.append(("Compresión " + ("rota" if c["ruptura"] else "preparada"), c["gatillo"], c["piso"]))
        s = a["setup_av"]["d"]
        if s and s["estado"] == "rompe":
            op.append((f"Ruptura AVWAP {s['ancla'].lower()}", s["entrada"], s["stop"]))
        for nombre, ent, stop in op:
            if not ent or not stop or ent <= stop: continue
            riesgo = (ent - stop) / ent * 100
            if riesgo > FOCO_RIESGO_MAX: continue
            if (precio / ent - 1) * 100 > ZONA_COMPRA_MAX: continue  # ya se fue de la zona de compra
            out.append({"t": a["t"], "setup": nombre, "entrada": num(ent, 4), "stop": num(stop, 4),
                        "riesgo": num(riesgo, 1), "dist": num((precio / ent - 1) * 100), "score": a["score"]})
            break
    out.sort(key=lambda x: -x["score"])
    return out[:FOCO_MAXIMO]

# ---------------------------------------------------------------- principal
def correr():
    t0 = time.time()
    print("1/5 Armando el universo…")
    uni = obtener_universo()
    info = uni.set_index("ticker")
    print(f"   {len(uni)} activos")
    print("2/5 Descargando 2 años de velas diarias…")
    diario = descargar(list(uni.ticker), "2y", "1d")
    rs_raw, ret21 = {}, {}
    for t, df in diario.items():
        if len(df) >= 60:
            rs_raw[t] = rs_bruto(df.Close)
            ret21[t] = df.Close.iloc[-1] / df.Close.iloc[-22] - 1
    rs_pct = pd.Series(rs_raw).rank(pct=True) * 98 + 1
    r21_pct = pd.Series(ret21).rank(pct=True) * 100
    print("3/5 Embudo: precio, liquidez, market cap, ADR y Minervini…")
    es_acc = lambda t: info.at[t, "tipo"] == "accion"
    paso = [t for t in diario if t in rs_pct.index]
    embudo = [("Con datos", len(paso))]
    paso = [t for t in paso if info.at[t, "tipo"] == "cripto" or diario[t].Close.iloc[-1] >= PRECIO_MINIMO]
    embudo.append((f"Precio ≥ {PRECIO_MINIMO}", len(paso)))
    liq = {}
    for t in paso:
        if es_acc(t): liq[t] = liquida(diario[t])
    paso = [t for t in paso if not es_acc(t) or liq[t][0]]
    embudo.append(("Liquidez", len(paso)))
    perf = perfiles([t for t in paso if es_acc(t)], {t: float(diario[t].Close.iloc[-1]) for t in paso})
    if MARKET_CAP_MIN > 0:
        # Sin dato de market cap no se descarta (se muestra s/d)
        paso = [t for t in paso if not es_acc(t) or not (perf.get(t) or {}).get("mcap") or perf[t]["mcap"] >= MARKET_CAP_MIN]
        embudo.append((f"Market cap ≥ {MARKET_CAP_MIN / 1e9:g} B", len(paso)))
    print("   Régimen de mercado…")
    extra = descargar(["SPY", "QQQ", "^VIX"], "2y", "1d")
    # La amplitud se mide sobre las acciones líquidas, no sobre las micro caps del listado completo
    reg = regimen({t: diario.get(t, extra.get(t)) for t in ("SPY", "QQQ")}, extra.get("^VIX"),
                  [diario[t] for t in paso if es_acc(t)])
    liquidas = [t for t in paso if es_acc(t)]
    paso = [t for t in paso if adr_pct(diario[t]) >= (ADR_MINIMO_ETF if info.at[t, "tipo"] == "etf" else ADR_MINIMO)]
    embudo.append((f"ADR ≥ {ADR_MINIMO:g}%", len(paso)))
    spy = diario.get("SPY")
    if spy is None: spy = extra.get("SPY")
    spy_c = spy.Close if spy is not None else None
    cand = {}
    for t in paso:
        checks, hi, lo, _ = minervini(diario[t], spy_c, info.at[t, "tipo"] == "etf")
        if pasa_minervini(checks, rs_pct[t]):
            cand[t] = True
    embudo.append((f"Minervini {MIN_CRITERIOS_MINERVINI}/8", len(cand)))
    print("   " + " → ".join(f"{n} {k}" for k, n in embudo))
    print("4/5 Historia completa, earnings y AVWAP de los candidatos…")
    hist = descargar(list(cand), "max", "1d") if cand else {}
    activos = []
    dfs_d = {}
    hoy = pd.Timestamp.now()
    for t in cand:
        tipo = info.at[t, "tipo"]
        df = hist.get(t)
        if df is None or len(df) < len(diario[t]): df = diario[t]
        # Con la historia completa las EMA150/200 quedan iguales a las de TradingView; se vuelve a chequear el X/8
        checks, hi, lo, e = minervini(df, spy_c, tipo == "etf")
        if not pasa_minervini(checks, rs_pct[t]): continue
        wk = semanal(df, tipo == "cripto")
        dfs_d[t] = df
        earn, prox = (fechas_earnings(t) if (BUSCAR_EARNINGS and tipo == "accion") else (None, None))
        es_ipo = tipo == "accion" and df.index[0] > hoy - pd.Timedelta(days=3 * 365)
        ep = episodic(df)
        earn_dias = (prox.normalize() - hoy.normalize()).days if prox is not None else None
        av = {}
        for tf, d in (("d", df), ("w", wk)):
            lst = [estado_avwap(d, nom, i, tf) for nom, i in anclas(d, tf, earn, es_ipo, ep["_ts"] if ep else None)]
            av[tf] = [x for x in lst if x]
        activo_av = any(x["cuenta"] for tf in av for x in av[tf])
        vcp = detectar_vcp(df)
        tc = cierres_apretados(df, wk, vcp)
        comp = {"d": compresion(df, "d"), "w": compresion(wk, "w")}
        comprimida = any(comp[k] and (comp[k]["es"] or comp[k]["ruptura"]) for k in comp)
        # Sin AVWAP activa: igual entra si tiene VCP, compresión o tocó una EMA diaria (se muestra solo en esas secciones)
        sin_av = bool(EXIGIR_AVWAP and not activo_av)
        if sin_av and not vcp and not tc and not comprimida and not (ANALIZAR_30M and toque_ema_diaria(df)): continue
        ins = {"d": inside(df), "w": inside(wk)}
        sav = {"d": setup_avwap(df, av["d"]), "w": setup_avwap(wk, av["w"])}
        rs = float(rs_pct[t]); c = df.Close; pf = perf.get(t) or {}
        activos.append({
            "t": t, "nombre": str(pf.get("nombre") or info.at[t, "nombre"]), "sector": str(pf.get("sector") or info.at[t, "sector"]),
            "industria": pf.get("industria"), "tipo": tipo, "bolsa": str(info.at[t, "bolsa"] or ""), "mcap": num(pf["mcap"], 0) if pf.get("mcap") else None,
            "vol50": num(liq[t][1], 0) if t in liq else None, "dvol50": num(liq[t][2], 0) if t in liq else None,
            "precio": num(c.iloc[-1], 4), "chg": num((c.iloc[-1] / c.iloc[-2] - 1) * 100),
            "ret21": num(ret21[t] * 100, 1), "rs": num(rs, 0), "mv": sum(checks), "mv_checks": checks, **tecnico(df, wk, e),
            "off_hi": num((c.iloc[-1] / hi - 1) * 100, 1),
            "hi52": num(hi, 4), "lo52": num(lo, 4), "pos52": num((c.iloc[-1] - lo) / (hi - lo) * 100 if hi > lo else 100, 0),
            "avwap": av, "comp": comp, "inside": ins, "setup_av": sav, "pivot30": None, "vcp": vcp, "tc": tc, "sin_av": sin_av,
            "earn_prox": prox.strftime("%d-%m-%Y") if prox is not None else None,
            "adr": num(adr_pct(df), 2), "earn_dias": earn_dias,
            "d10": num(estiramiento(df)[0], 1), "d20": num(estiramiento(df)[1], 1), "earn_momento": momento_earnings(prox),
            "ep": {k: v for k, v in ep.items() if not k.startswith("_")} if ep else None,
            "estadio": estadio(df), "flags": banderas(df, sav["d"], earn_dias),
            "spark_d": spark(c, 63), "spark_w": spark(wk.Close, 30), "_r21p": float(r21_pct.get(t, 50)), "_earn_u": earn,
        })
    for a in activos:
        etf = etf_de(a.get("industria"), a["sector"])
        d = diario.get(etf) if etf else None
        a["etf"] = {"t": etf, "rs": num(rs_pct.get(etf), 0) if etf in rs_pct.index else None,
                    "chg": num((d.Close.iloc[-1] / d.Close.iloc[-2] - 1) * 100) if d is not None and len(d) > 1 else None} if etf else None
        if a["etf"] and d is not None:
            c_a = diario[a["t"]].Close
            ret = lambda c, n: (c.iloc[-1] / c.iloc[-n - 1] - 1) * 100 if len(c) > n else None
            for n, k in ((21, "vs1m"), (63, "vs3m")):
                x, y = ret(c_a, n), ret(d.Close, n)
                a["etf"][k] = num(x - y, 1) if x is not None and y is not None else None
    n_req = sum(1 for a in activos if not a["sin_av"])
    if EXIGIR_AVWAP: embudo.append(("Con AVWAP activa", n_req))
    print(f"   {n_req} cumplen todos los requisitos")
    con30 = bool(ANALIZAR_30M and activos)
    if con30:
        print(f"5/5 Buscando pivots de 30 minutos (incluye las que no tienen AVWAP activa)…")
        m30 = descargar([a["t"] for a in activos], "5d", "30m")
        for a in activos:
            a["pivot30"] = pivot_30m(m30.get(a["t"]), dfs_d.get(a["t"]))
        activos = [a for a in activos if not a["sin_av"] or a["pivot30"] or a["vcp"] or a["tc"] or _comprimida(a)]
    else:
        print("5/5 Intradía desactivado")
        activos = [a for a in activos if not a["sin_av"] or a["vcp"] or a["tc"] or _comprimida(a)]
    print(f"   {sum(1 for a in activos if a['vcp'])} con base VCP y {sum(1 for a in activos if a['tc'])} con cierres apretados")
    acc = [a for a in activos if a["tipo"] == "accion"]
    fund = fundamentales([a["t"] for a in acc], {a["t"]: a["_earn_u"] for a in acc}) if BUSCAR_FUNDAMENTALES else {}
    print(f"   {len(fund)} con fundamentales")
    for a in activos:
        a.pop("_earn_u", None)
        a["fund"] = fund.get(a["t"])
        if a["fund"] and a["fund"]["eps_ttm"] and a["fund"]["eps_ttm"] > 0:
            a["fund"]["pe"] = num(a["precio"] / a["fund"]["eps_ttm"], 1)
        p = partes_score(a["mv"], a["rs"], a["comp"]["d"], a["setup_av"]["d"],
                         a["comp"]["d"] and a["comp"]["d"]["ruptura"], a["inside"]["d"], a["pivot30"], a["vcp"], a["fund"], a["tc"])
        if a["tipo"] != "accion" and 0 < PUNTOS_FUNDAMENTALES < 100:
            # ETFs y cripto no tienen balances: el pilar no aplica y los otros cuatro se reescalan a 100
            k = 100 / (100 - PUNTOS_FUNDAMENTALES)
            p = {c: (num(v * k, 1) if c != "fund" else None) for c, v in p.items()}
        a["partes"] = p
        malas = [f for f in a["flags"] if f["k"] in ("rechazo", "sinvol", "ext", "estirada")]
        a["castigo"] = num(len(malas) * SCORE_CASTIGO_BANDERA, 1)
        a["score"] = num(max(0, sum(v for v in p.values() if v) - a["castigo"]), 1)
        a["calor"] = num(0.6 * a["score"] + 0.4 * a.pop("_r21p"), 1)
    foco = lista_foco(activos)
    # El embudo termina en lo accionable: score alto y Seleccionadas
    embudo.append((f"Score ≥ {SEL_SCORE_MIN}", sum(1 for a in activos if not a["sin_av"] and a["score"] >= SEL_SCORE_MIN)))
    embudo.append(("Seleccionadas", sum(1 for a in activos if es_seleccionada(a))))
    fecha_iso = max(df.index[-1] for t, df in diario.items() if info.at[t, "tipo"] != "cripto").strftime("%Y-%m-%d")
    top = top_retorno(activos, fecha_iso, spy_c, diario)
    nombres = {t: str((perf.get(t) or {}).get("nombre") or info.at[t, "nombre"]) for t in liquidas}
    cart = cartelera(diario, liquidas, nombres, {t: (perf.get(t) or {}).get("mcap") for t in liquidas})
    macro = eventos_macro()
    earn_cal = calendario_earnings({a["t"] for a in activos})
    print(f"   Eventos macro: {len(macro)} · earnings de la semana: {len(earn_cal)}")
    por_semana = rs_semanas(diario)
    rot = rotacion(diario, ETFS, por_semana) if INCLUIR_ETFS else None
    for a in activos:
        a["rs16"] = [num(x.get(a["t"]), 0) if a["t"] in x.index else None for x in por_semana]
    selh = track_seleccionadas(activos, fecha_iso, diario, spy_c)
    resumen = None
    if RESUMEN_DIARIO and ahora_ar().hour >= 18:
        try: resumen = armar_resumen(activos, fecha_iso, reg, selh, rot, diario, macro)
        except Exception as e: print(f"   ⚠️ Resumen: {e}")
    n_al = alertas_telegram(activos, fecha_iso, resumen, (reg or {}).get("ftd"))
    print(f"   Seleccionadas: {sum(es_seleccionada(a) for a in activos)} · alertas enviadas: {n_al}")
    print(f"   Top {TOP_N}: {top['medio']}% promedio en {top['ruedas']} ruedas vs SPY {top['spy']}%")
    print(f"   Lista de foco: {len(foco)}")
    fechas = [df.index[-1] for t, df in diario.items() if info.at[t, "tipo"] != "cripto"] or [hoy]
    datos = {"meta": {
        "fecha_datos": max(fechas).strftime("%d-%m-%Y"), "generado": ahora_ar().strftime("%d-%m-%Y %H:%M"),
        "n_universo": len(diario), "top": top, "selh": selh, "macro": macro, "earn_cal": earn_cal, "cartelera": cart, "rotacion": rot, "nombre": NOMBRE_DASHBOARD, "lema": LEMA, "avatar": AVATAR_URL, "embudo": [[k, n] for k, n in embudo], "n_extra": sum(1 for a in activos if a["sin_av"]), "con30m": con30, "regimen": reg, "demo": bool(globals().get("MODO_DEMO", False)),
        "params": {"min_mv": MIN_CRITERIOS_MINERVINI, "sobre_min": PCT_SOBRE_MINIMO_52S, "sobre_min_etf": PCT_SOBRE_MINIMO_52S_ETF, "bajo_max": PCT_DEBAJO_MAXIMO_52S,
                   "rs_min": RS_MINIMO, "precio_min": PRECIO_MINIMO, "exigir_av": EXIGIR_AVWAP,
                   "dist_d": DIST_POR_ROMPER_DIARIO, "dist_w": DIST_POR_ROMPER_SEMANAL,
                   "velas_d": VELAS_RUPTURA_DIARIO, "velas_w": VELAS_RUPTURA_SEMANAL, "emas_30m": lista_emas(),
                   "vol_ruptura": VOL_RUPTURA, "adr_min": ADR_MINIMO, "cerca_gatillo": CERCA_GATILLO,
                   "ep_suba": EP_MIN_SUBA, "ep_vol": EP_MIN_VOL,
                   "vcp_min": VCP_MIN_CONTRACCIONES, "vcp_ult": VCP_ULTIMA_MAX, "vcp_form": VCP_FORMANDO_MAX, "vcp_dist": VCP_DIST_PIVOT,
                   "vcp_seco": VCP_VOL_SECO, "vcp_dias": VCP_DIAS_RUPTURA, "vcp_seg": VCP_DIAS_SEGUIMIENTO,
                   "vcp_smin": VCP_SEMANAS_MIN, "vcp_smax": VCP_SEMANAS_MAX, "emas_asc": EMAS_ASCENSO,
                   "fuertes": ANCLAS_FUERTES, "exigir_rs": EXIGIR_RS, "castigo": SCORE_CASTIGO_BANDERA, "fuerte": CRECIMIENTO_FUERTE, "tc_min": TC_MIN_CIERRES, "tc_rango": TC_RANGO_MAX, "tc_cerca": TC_CERCA_PIVOT, "cruce_sem": CRUCE_SEMANAS, "rsi_alto": RSI_SOBRECOMPRA, "zona_compra": ZONA_COMPRA_MAX, "resumen_cerca": RESUMEN_CERCA, "cart_n": CARTELERA_N, "rsi_bajo": RSI_SOBREVENTA, "sel": {"rs": SEL_RS_MIN, "mv": SEL_MINERVINI_MIN, "score": SEL_SCORE_MIN}, "top_ruedas": TOP_RUEDAS, "top_n": TOP_N,
                   "pts": {"tend": PUNTOS_TENDENCIA, "rs": PUNTOS_RS, "contr": PUNTOS_COMPRESION, "setup": PUNTOS_SETUP, "fund": PUNTOS_FUNDAMENTALES}, "est10": ESTIRADA_EMA10_ADR, "est20": ESTIRADA_EMA20_ADR,
                   "foco_rs": FOCO_RS_MINIMO, "foco_riesgo": FOCO_RIESGO_MAX, "foco_max": FOCO_MAXIMO}},
        "foco": foco, "activos": sorted(activos, key=lambda a: -a["score"])}
    iconos = f'<link rel="apple-touch-icon" href="{AVATAR_URL}">\n<link rel="icon" href="{AVATAR_URL}">' if AVATAR_URL else ""
    html = PLANTILLA.replace("__NOMBRE__", NOMBRE_DASHBOARD).replace("__ICONOS__", iconos).replace("__AVATAR__", AVATAR_URL).replace("__DATA__", json.dumps(datos, ensure_ascii=False, allow_nan=False, default=str))
    print(f"Listo en {time.time() - t0:.0f} s")
    return html, datos

PLANTILLA = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<title>__NOMBRE__</title>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#050607">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="__NOMBRE__">
__ICONOS__
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#050607; --rail:#08090b; --card:#0c0e11; --card2:#0c0e11; --line:#1a1e23; --line2:#262b31;
  --text:#e8eaed; --muted:#858c96; --faint:#59606a;
  --acc:#3ddc97; --acc2:#1f9f69; --accsoft:rgba(61,220,151,.12); --oninv:#ffffff;
  --up:#3ddc97; --down:#f0626e; --warn:#f4b740; --blue:#6ea8fe; --violet:#a78bfa;
  --sombra:0 10px 30px rgba(0,0,0,.35);
  --ui:"Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  color-scheme:dark; box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: light){
  :root:not([data-theme="dark"]){
    --bg:#f1f3f5; --rail:#ffffff; --card:#ffffff; --card2:#f6f8f9; --line:#e2e5e9; --line2:#d3d8de;
    --text:#111418; --muted:#5b636e; --faint:#8a919a;
    --acc:#12a366; --acc2:#0c8451; --accsoft:rgba(18,163,102,.11);
    --up:#12a366; --down:#d6384b; --warn:#b37b08; --blue:#2e6bd0; --violet:#6c4fd0; --sombra:0 8px 24px rgba(20,30,40,.08); color-scheme:light;
  }
}
:root[data-theme="light"]{
  --bg:#f1f3f5; --rail:#ffffff; --card:#ffffff; --card2:#f6f8f9; --line:#e2e5e9; --line2:#d3d8de;
  --text:#111418; --muted:#5b636e; --faint:#8a919a;
  --acc:#12a366; --acc2:#0c8451; --accsoft:rgba(18,163,102,.11);
  --up:#12a366; --down:#d6384b; --warn:#b37b08; --blue:#2e6bd0; --violet:#6c4fd0; --sombra:0 8px 24px rgba(20,30,40,.08); color-scheme:light;
}
:root[data-theme="dark"]{
  --bg:#050607; --rail:#08090b; --card:#0c0e11; --card2:#0c0e11; --line:#1a1e23; --line2:#262b31;
  --text:#e8eaed; --muted:#858c96; --faint:#59606a;
  --acc:#3ddc97; --acc2:#1f9f69; --accsoft:rgba(61,220,151,.13);
  --up:#3ddc97; --down:#f0626e; --warn:#f4b740; --blue:#6ea8fe; --violet:#a78bfa; --sombra:0 10px 30px rgba(0,0,0,.35); color-scheme:dark;
}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*,*::before,*::after{box-sizing:inherit}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--ui);font-size:15px;line-height:1.45;font-variant-numeric:tabular-nums}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.app{display:grid;grid-template-columns:96px minmax(0,1fr);min-height:100vh}

/* Barra de navegación */
nav.rail{position:sticky;top:0;height:100vh;background:var(--rail);border-right:1px solid var(--line);display:flex;flex-direction:column;align-items:center;gap:4px;padding:18px 0}
.logo{width:46px;height:46px;border-radius:14px;background:linear-gradient(140deg,var(--acc),var(--acc2));display:grid;place-items:center;margin-bottom:16px;box-shadow:0 6px 18px rgba(61,220,151,.25)}
.logo svg{width:24px;height:24px;stroke:#fff}
.logo img{width:100%;height:100%;border-radius:inherit;object-fit:cover}
.rail button{width:78px;padding:10px 0 8px;border-radius:14px;background:none;border:0;color:var(--muted);display:flex;flex-direction:column;align-items:center;gap:5px;font-size:11.5px;font-weight:600;cursor:pointer}
.rail button svg{width:21px;height:21px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.rail button:hover{color:var(--text)}
.rail .ct{display:none}
.rail button[aria-current="page"]{background:var(--accsoft);color:var(--acc)}
main{padding:24px 30px 70px;min-width:0;max-width:1440px}

/* Encabezado */
header.top{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:14px 20px;margin-bottom:22px}
header.top h1{margin:0;font-size:28px;font-weight:700;letter-spacing:-.02em;line-height:1.1}
header.top p{margin:6px 0 0;color:var(--muted);font-size:14px;max-width:70ch}
.controles{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.seg{display:inline-flex;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:3px}
.seg button{background:none;border:0;padding:6px 13px;border-radius:999px;cursor:pointer;color:var(--muted);font-weight:600;font-size:13.5px}
.seg button[aria-pressed="true"]{background:linear-gradient(140deg,var(--acc),var(--acc2));color:#fff}
input[type=search]{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:8px 14px;color:var(--text);font:inherit;font-size:14px;width:170px}
.chipmeta{font-size:12.5px;color:var(--muted);padding:6px 12px;border:1px solid var(--line);border-radius:999px;background:var(--card)}
.demo{color:var(--warn);font-weight:700;margin-left:6px}
.chipmeta{display:inline-flex;align-items:center;gap:8px}
.refr{font:inherit;font-size:12.5px;font-weight:700;color:var(--acc);background:none;border:0;padding:0;cursor:pointer;display:inline-flex;align-items:center;gap:4px}
.refr svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.refr.gira svg{animation:gira .8s linear infinite}
@keyframes gira{to{transform:rotate(360deg)}}
.viejo{display:none;margin:-8px 0 18px;padding:10px 14px;border-radius:12px;font-size:13.5px;border:1px solid color-mix(in srgb,var(--warn) 45%,transparent);background:color-mix(in srgb,var(--warn) 12%,transparent)}
.viejo.on{display:block}
.sin_av{font-size:11px;font-weight:700;color:var(--muted);border:1px solid var(--line2);border-radius:6px;padding:1px 5px;margin-left:6px;white-space:nowrap}

/* Tarjetas */
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;min-width:0}
.card h3,h2.sec,.ficha h4{font-family:var(--mono);text-transform:uppercase;letter-spacing:.14em;font-weight:500}
.card h3{margin:0 0 14px;font-size:12.5px;color:var(--acc);display:flex;justify-content:space-between;align-items:baseline;gap:10px;position:relative;padding-left:12px}
.card h3::before,h2.sec::before,.ficha h4::before{content:"";position:absolute;left:0;top:1px;bottom:1px;width:3px;border-radius:2px;background:var(--acc)}
.card h3 small{color:var(--muted);font-family:var(--ui);text-transform:none;letter-spacing:0;font-size:12.5px}
.kpi b,.embudo .paso b,.gauge .v b,.ring b,.precio,.fh h2,.x8,.rkg{font-family:var(--mono)}
.rkg{display:inline-block;margin-left:10px;padding:2px 9px;border-radius:999px;font-size:12px;font-weight:700;color:var(--blue);border:1px solid color-mix(in srgb,var(--blue) 45%,transparent);vertical-align:6px}
.gate{display:flex;justify-content:space-between;gap:10px;font-size:14px;padding:4px 0}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.gauto{grid-template-columns:repeat(auto-fill,minmax(560px,1fr))}
.inicio{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}
@media (max-width:1100px){.inicio,.g2{grid-template-columns:1fr}.gauto{grid-template-columns:1fr}}
@media (max-width:760px){.g3{grid-template-columns:1fr}}
h2.sec{font-size:13px;margin:30px 0 12px;color:var(--acc);display:flex;align-items:baseline;gap:10px;position:relative;padding-left:12px}
h2.sec small{color:var(--muted);font-family:var(--ui);text-transform:none;letter-spacing:0;font-size:12.5px}
.subnav{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 10px}
.subnav .chip{font-size:14px}
.chips2{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px;padding-top:10px;border-top:1px dashed var(--line2)}
.nota{color:var(--muted);font-size:13.5px;margin:-4px 0 14px;max-width:85ch}
.tend{display:inline-flex;align-items:center;gap:6px;white-space:nowrap}
.x8{font-weight:800;font-variant-numeric:tabular-nums}.x8.warn{color:#EF6C00}
.ars{display:inline-flex;gap:2px;align-items:center}.ars i{width:4px}
.ar{display:inline-block;width:15px;text-align:center;border-radius:4px;font-size:9px;line-height:15px;color:var(--muted)}
.ar.s2{color:#fff;background:#1B5E20}.ar.s1{color:#81C784;background:rgba(129,199,132,.18)}
.ar.b1{color:#E57373;background:rgba(229,115,115,.18)}.ar.b2{color:#fff;background:#B71C1C}
.adr0{color:var(--muted)}.adr1{color:#81C784}.adr2{color:#2fa65a;font-weight:700}.adr3{color:#EF6C00;font-weight:700}.adr4{color:#E5484D;font-weight:700}
.tv{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:3px;margin-top:6px;text-align:center;font-size:11px}
.tv span{color:var(--muted)}.tv b{display:block;border-radius:4px;padding:2px 0;font-size:11px}
.tv b.ok{color:#2fa65a;background:rgba(129,199,132,.18)}.tv b.no{color:#E57373;background:rgba(229,115,115,.18)}
.tv .ar{width:100%;font-size:11px;line-height:18px}
.fgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.fbox{border:1px solid var(--line2);border-radius:12px;padding:8px 10px;display:flex;flex-direction:column;gap:2px}
.fbox span{color:var(--muted);font-size:12px}.fbox b{font-size:18px}.fbox small{color:var(--muted);font-size:11px}
.fbox.up{border-color:var(--up)}.fbox.up b{color:var(--up)}.fbox.warn b{color:var(--warn)}.fbox.down b{color:var(--down)}
.ebars{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin-top:12px;text-align:center}
.eq em{font-style:normal;font-weight:700;font-size:12px;display:block;min-height:16px}
.eq em.up{color:var(--up)}.eq em.warn{color:var(--warn)}.eq em.down{color:var(--down)}.eq em.mut{color:var(--muted)}
.eq .par{display:flex;align-items:flex-end;justify-content:center;gap:4px;height:74px;border-bottom:1px solid var(--line2)}
.eq .par i{width:14px;border-radius:3px 3px 0 0}.eq .vie{background:var(--line2)}
.eq .nue.up{background:var(--up)}.eq .nue.warn{background:var(--warn)}.eq .nue.down,.eq .nue.mut{background:var(--down)}
.eq span{font-size:11px;color:var(--muted);display:block;margin-top:4px}
.dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--up);margin-right:4px;vertical-align:middle}
.tc{display:inline-block;padding:2px 8px;border-radius:999px;font-size:12px;font-weight:700;color:var(--warn);background:rgba(244,183,64,.14);white-space:nowrap}
.ins{display:inline-block;padding:1px 6px;border-radius:6px;font-size:11.5px;font-weight:700;color:var(--blue);background:rgba(110,168,254,.14);white-space:nowrap}
.tc.ok{color:var(--up);background:var(--accsoft)}
.tbigs{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));border:1px solid var(--line);border-radius:12px;margin-bottom:12px}
.tbig{padding:14px 16px;text-align:center}.tbig+.tbig{border-left:1px solid var(--line)}
.tbig span{display:block;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--warn)}
.tbig+.tbig span{color:var(--blue)}
.tbig b{display:block;font-family:var(--mono);font-size:34px;line-height:1.2;text-shadow:0 0 18px currentColor}
.scp{display:inline-block;min-width:38px;text-align:center;padding:2px 8px;border-radius:999px;border:1px solid color-mix(in srgb,var(--acc) 45%,transparent);color:var(--acc);font-family:var(--mono)}
.rbar{display:inline-block;width:110px;height:8px;border-radius:4px;background:var(--line);overflow:hidden}
.rbar i{display:block;height:100%;border-radius:4px;background:var(--acc)}.rbar i.neg{background:var(--down)}
b.warn,span.warn{color:var(--warn)}
.ci em.rc{color:#EF6C00}.ci em.rv{color:var(--blue)}
.expo{color:var(--warn)}
.evs{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}
.evd{border:1px solid var(--line);border-radius:12px;padding:10px;min-width:0}.evd.hoy{border-color:var(--acc)}
.evh{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px;font-family:var(--mono)}
.evm{border-left:3px solid var(--warn);padding:4px 8px;margin-bottom:6px;font-size:12.5px;background:var(--card2);border-radius:0 8px 8px 0}
.evm.alto{border-left-color:var(--down)}.evm div{display:flex;justify-content:space-between;gap:6px}.evm small{color:var(--muted)}
.eve{display:flex;flex-wrap:wrap;gap:5px}.evt{font-size:12px;font-weight:700;padding:2px 7px;border:1px solid var(--line2);border-radius:7px;cursor:pointer;font-family:var(--mono)}
.eve{flex-direction:column;flex-wrap:nowrap}
.evr{display:grid;grid-template-columns:52px 1fr auto;gap:6px;align-items:center;font-size:12px;padding:3px 6px;border:1px solid var(--line);border-radius:7px}
.evr b{font-family:var(--mono)}.evr.rad{border-color:var(--blue);cursor:pointer}.evr.sel{border-color:var(--acc);cursor:pointer}.evr.sel b{color:var(--acc)}
.evr i{font-style:normal;font-size:10px;font-weight:700;padding:1px 6px;border-radius:999px}.evr i.pre{color:var(--warn);background:rgba(244,183,64,.14)}.evr i.post{color:#a78bfa;background:rgba(167,139,250,.16)}
.evmas{margin-top:4px;padding:3px 10px;font-size:12px;align-self:flex-start}
.evt.rad{border-color:var(--blue)}.evt.sel{border-color:var(--acc);color:var(--acc)}.evt i{font-style:normal;font-size:9.5px;color:var(--muted);margin-left:4px}
.cartsel{display:inline-flex;gap:6px}.cartsel .chip{padding:3px 10px;font-size:12px}
.ambas{font-size:11px;font-weight:700;color:var(--warn);white-space:nowrap}
.dos .card{min-width:0}
.lema{display:flex;align-items:center;gap:14px;margin-top:10px;padding:8px 12px;border:1px solid var(--line);border-radius:12px;background:var(--card);width:max-content;max-width:100%;flex-wrap:wrap}
.lema .lt{display:flex;flex-direction:column;gap:3px;font-size:13px}.lema .lt b{font-family:var(--mono);letter-spacing:.08em;text-transform:uppercase;font-size:12px;color:var(--acc)}
.lema code{font-family:var(--mono);margin-left:6px}.lema em{font-style:normal;font-weight:800;padding:0 4px;border-radius:4px}
.lema em.up{background:var(--accsoft)}.lema em.down{background:color-mix(in srgb,var(--down) 15%,transparent)}
.ern{display:inline-block;margin-left:4px;font-size:11px;font-weight:700;color:var(--warn);white-space:nowrap}
.cs{display:inline-block;margin-left:4px;padding:0 5px;border-radius:5px;font-size:10.5px;font-weight:800;color:#e879a6;border:1px solid color-mix(in srgb,#e879a6 50%,transparent);vertical-align:1px}
.tvexp{font-size:13px;padding:7px 12px}
.h200{margin-top:14px}.h200 small{display:block;margin-bottom:4px;font-size:12px}
svg .ax{font-size:11px;fill:var(--muted);font-family:var(--mono)}
.g2c{display:grid;grid-template-columns:1fr 1fr;gap:14px}
h5{margin:0 0 8px;font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
h5.up{color:var(--up)}h5.down{color:var(--down)}
.cart{display:grid;gap:6px}.ci{display:grid;grid-template-columns:auto 1fr auto;gap:8px;align-items:baseline;font-size:13px;padding:5px 8px;border-radius:8px;border:1px solid var(--line)}
.ci span{color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.ci em{font-style:normal;font-weight:700;font-family:var(--mono)}
.ci.en{cursor:pointer;border-color:color-mix(in srgb,var(--acc) 45%,transparent)}.ci.en b{color:var(--acc)}
.g2r{grid-template-columns:minmax(0,1.6fr) minmax(0,1fr)}
@media (max-width:1100px){.g2r{grid-template-columns:1fr}}
.rrg .ej{stroke:var(--line2)}.rrg .qd{font-family:var(--mono);font-size:11px;letter-spacing:.12em}
.rrg .et{font-size:11px;fill:var(--text);font-family:var(--mono)}
.rrgc{display:flex;gap:10px;align-items:center;margin-top:8px}.rrgc input{flex:1;accent-color:var(--acc)}
@media (max-width:560px){.g2c{grid-template-columns:1fr}}
.embudo{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px}
.embudo .paso{display:flex;flex-direction:column;min-width:0}
.embudo .paso b{font-size:20px;font-variant-numeric:tabular-nums}
.embudo .paso span{color:var(--muted);font-size:12.5px}
.embudo i{color:var(--muted);font-style:normal}

/* KPIs */
.kpis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media (max-width:560px){.kpis{grid-template-columns:repeat(2,minmax(0,1fr))}}
.kpi{text-align:left;cursor:pointer;display:flex;flex-direction:column;gap:10px;padding:16px}
.kpi .ic{width:36px;height:36px;border-radius:11px;background:var(--accsoft);display:grid;place-items:center;color:var(--acc)}
.kpi .ic svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.kpi b{font-size:26px;font-weight:700;line-height:1}
.kpi span{color:var(--muted);font-size:13px;line-height:1.3}
.kpi:hover{border-color:var(--line2)}

/* Régimen */
.reg{display:grid;grid-template-columns:210px 1fr;gap:20px;align-items:center}
@media (max-width:560px){.reg{grid-template-columns:1fr}}
.gauge{position:relative;width:210px;margin:0 auto}
.gauge .v{position:absolute;left:0;right:0;bottom:6px;text-align:center}
.gauge .v b{display:block;font-size:40px;font-weight:800;line-height:1}
.gauge .v span{font-size:14px;font-weight:700}
.capas{display:grid;gap:12px}
.capa .fila{display:flex;justify-content:space-between;font-size:14px;font-weight:600}
.capa .fila span:last-child{color:var(--muted);font-weight:500}
.pbar{height:7px;background:var(--line);border-radius:4px;overflow:hidden;margin:6px 0 4px}
.pbar i{display:block;height:100%;border-radius:4px;background:linear-gradient(90deg,var(--acc2),var(--acc))}
.capa small{display:block;color:var(--muted);font-size:12.5px}
.rec{margin-top:14px;padding:10px 14px;border-radius:12px;background:var(--accsoft);font-size:14px}

/* Spotlight */
.spot{display:flex;flex-direction:column;gap:12px;cursor:pointer}
.spot .cab{display:flex;align-items:center;gap:14px}
.ring{position:relative;width:70px;height:70px;flex:none}
.ring b{position:absolute;inset:0;display:grid;place-items:center;font-size:20px;font-weight:800}
.spot h4{margin:0;font-size:18px}
.spot p{margin:2px 0 0;color:var(--muted);font-size:13px}
.partes{display:grid;grid-template-columns:auto 1fr auto;gap:6px 10px;align-items:center;font-size:13px}
.partes .pbar{margin:0}

/* Earnings */
.earn{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.eitem{border:1px solid var(--line);border-radius:14px;padding:10px 12px;background:var(--card);cursor:pointer}
.eitem b{font-size:15px}
.eitem span{display:block;color:var(--muted);font-size:12.5px}
.eitem em{display:inline-block;margin-top:6px;font-style:normal;font-size:11.5px;font-weight:700;padding:2px 8px;border-radius:999px;background:color-mix(in srgb,var(--warn) 16%,transparent);color:var(--warn)}
.eitem em.bmo{background:color-mix(in srgb,var(--blue) 16%,transparent);color:var(--blue)}

/* Franja de sectores */
.franja{display:grid;grid-template-columns:repeat(auto-fill,minmax(165px,1fr));gap:10px;margin-bottom:20px}
.sec-t{text-align:left;border:1px solid var(--line);border-radius:16px;padding:12px 14px;cursor:pointer;
  background:linear-gradient(155deg,color-mix(in srgb,var(--acc) calc(var(--h)*30%),var(--card2)) 0%,var(--card) 80%)}
.sec-t[aria-pressed="true"]{border-color:var(--acc)}
.sec-t strong{display:block;font-size:14.5px}
.sec-t small{color:var(--muted);font-size:12.5px;display:block}
.sec-t em{font-style:normal;font-size:12.5px;font-weight:700;color:var(--acc)}

/* Tablas */
.tw{overflow-x:auto;margin:0 -4px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{color:var(--muted);font-weight:600;font-size:12.5px;text-align:left;padding:8px;border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:9px 8px;border-bottom:1px solid color-mix(in srgb,var(--line) 70%,transparent);white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
tbody tr{cursor:pointer}
tbody tr:hover td{background:color-mix(in srgb,var(--acc) 5%,transparent)}
.n{text-align:right}
.up{color:var(--up)} .down{color:var(--down)} .mut{color:var(--muted)}
.tk{display:inline-block;background:var(--card2);border:1px solid var(--line2);border-radius:8px;padding:2px 8px;font-weight:700;font-size:13px;letter-spacing:.01em}
.rk{color:var(--faint);font-size:13px}
.est{display:inline-block;padding:2px 9px;border-radius:999px;font-size:12px;font-weight:700}
.est.rompe,.est.disparado,.est.rompio{background:color-mix(in srgb,var(--up) 15%,transparent);color:var(--up)}
.est.porromper,.est.armado,.est.preparada{background:color-mix(in srgb,var(--warn) 15%,transparent);color:var(--warn)}
.est.otro{color:var(--muted)}
.est.falla{background:color-mix(in srgb,var(--down) 15%,transparent);color:var(--down)}
.contr{display:inline-flex;align-items:center;gap:4px;white-space:nowrap;font-variant-numeric:tabular-nums}
.contr i{font-style:normal;color:var(--faint)}
.contr b{font-weight:600}
.contr b:last-child{color:var(--acc)}
.vcpg{width:100%;height:auto;display:block;margin-top:8px}
.foco{margin-bottom:18px}
.foco table td:nth-child(2){font-weight:600}
.fuerte{font-size:10.5px;font-weight:700;color:var(--acc);margin-left:4px}
.fl{display:inline-block;margin-left:5px;padding:1px 7px;border-radius:999px;font-size:11px;font-weight:700;vertical-align:1px}
.fl.bad{background:color-mix(in srgb,var(--down) 15%,transparent);color:var(--down)}
.fl.good{background:color-mix(in srgb,var(--up) 15%,transparent);color:var(--up)}
.fl.warn{background:color-mix(in srgb,var(--warn) 15%,transparent);color:var(--warn)}
.sc{display:inline-flex;align-items:center;gap:7px}
.barra{display:inline-block;width:58px;height:6px;background:var(--line);border-radius:3px;overflow:hidden}
.barra i{display:block;height:100%;background:var(--violet)}
.chip{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 14px;cursor:pointer;color:var(--muted);font-weight:600;font-size:13.5px}
.chip[aria-pressed="true"]{color:var(--acc);border-color:var(--acc);background:var(--accsoft)}
.filtros{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}
.vacio{color:var(--muted);padding:12px 0;margin:0}
svg.spark{display:block}

/* Ficha */
.velo{position:fixed;inset:0;background:rgba(0,0,0,.5);opacity:0;pointer-events:none;transition:opacity .2s;z-index:30}
.velo.open{opacity:1;pointer-events:auto}
aside.ficha{position:fixed;top:0;right:0;height:100%;width:min(470px,100%);background:var(--card);border-left:1px solid var(--line);z-index:31;
  transform:translateX(100%);transition:transform .22s ease;overflow-y:auto;padding:calc(20px + env(safe-area-inset-top,0px)) 22px calc(34px + env(safe-area-inset-bottom,0px))}
aside.ficha.open{transform:none}
@media (prefers-reduced-motion:reduce){aside.ficha,.velo{transition:none}}
.fh{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.fh h2{margin:0;font-size:30px;line-height:1;font-weight:800}
.fh p{margin:5px 0 0;color:var(--muted);font-size:14px}
.cerrar{background:var(--card2);border:1px solid var(--line);border-radius:10px;width:36px;height:36px;cursor:pointer;font-size:17px;line-height:1}
.precio{font-size:22px;font-weight:700;margin-top:12px}
.ficha h4{margin:24px 0 10px;font-size:12px;color:var(--acc);position:relative;padding-left:12px}
.checks{list-style:none;margin:0;padding:0;font-size:14px}
.checks li{padding:3px 0;display:flex;gap:8px}
.checks li b{width:16px;text-align:center}
.rango{position:relative;height:6px;border-radius:3px;background:linear-gradient(90deg,var(--down),var(--warn),var(--up));margin:10px 0 6px}
.rango i{position:absolute;top:-5px;width:4px;height:16px;background:var(--text);border-radius:2px;transform:translateX(-2px)}
.rl{display:flex;justify-content:space-between;color:var(--muted);font-size:12.5px}
.kv{display:grid;grid-template-columns:1fr auto;gap:5px 12px;font-size:14px}
.kv span:nth-child(odd){color:var(--muted)}
.kv span:nth-child(even){text-align:right;font-weight:600}
.flist{display:grid;gap:6px}
.flist div{font-size:13.5px;padding:7px 10px;border-radius:10px}
.flist .bad{background:color-mix(in srgb,var(--down) 12%,transparent)}
.flist .good{background:color-mix(in srgb,var(--up) 12%,transparent)}
.flist .warn{background:color-mix(in srgb,var(--warn) 12%,transparent)}
.ficha td,.ficha th{padding:6px 5px;white-space:normal}
.ficha td .mut{display:block;font-size:12.5px}
.enlace{display:inline-block;margin-top:18px;color:var(--acc);font-weight:600}
footer{color:var(--faint);font-size:12.5px;margin-top:40px;max-width:95ch}

/* Móvil: barra abajo */
@media (max-width:820px){
  .app{grid-template-columns:1fr}
  nav.rail{position:fixed;top:auto;bottom:0;left:0;right:0;height:auto;flex-direction:row;justify-content:space-between;gap:0;overflow-x:auto;
    padding:6px 6px calc(6px + env(safe-area-inset-bottom,0px));border-right:0;border-top:1px solid var(--line);z-index:20}
  .logo{display:none}
  .rail button{width:auto;min-width:48px;flex:1;padding:6px 1px;font-size:10.5px;gap:3px}
  .rail .lg{display:none} .rail .ct{display:inline}
  main{padding:16px 14px 110px}
  header.top h1{font-size:24px}
  .reg .gauge{width:190px}
}
.regmini{display:flex;align-items:center;gap:16px;width:100%;text-align:left;cursor:pointer;color:var(--text);font:inherit;margin-bottom:18px;padding:14px 18px}
.regmini .rgv{display:flex;flex-direction:column;align-items:center;min-width:76px}
.regmini .rgv b{font-size:34px;font-weight:800;line-height:1}
.regmini .rgv span{font-size:12.5px;font-weight:700}
.regmini .rgt{display:flex;flex-direction:column;gap:4px;font-size:13.5px;flex:1;min-width:0}
.regmini .mono{font-family:var(--mono);text-transform:uppercase;letter-spacing:.14em;font-size:11.5px;color:var(--acc)}
.regmini .ver{font-size:12.5px;color:var(--acc);font-weight:700;white-space:nowrap}
@media (max-width:560px){.regmini{flex-wrap:wrap}.regmini .ver{width:100%;text-align:right}}
.selb{font-size:10px;font-weight:800;letter-spacing:.06em;color:var(--acc);border:1px solid var(--acc);border-radius:5px;padding:0 4px;margin-left:5px;vertical-align:1px}
details.ayuda{margin-top:14px;color:var(--muted);font-size:13.5px;max-width:85ch}
details.ayuda summary{cursor:pointer;color:var(--acc);font-weight:700;margin-bottom:6px}
details.ayuda p{margin:8px 0}
main{min-width:0;overflow-x:clip}
.gl{display:flex;flex-direction:column}
.gr{padding:11px 2px;border-top:1px solid var(--line);cursor:pointer}
.gr:first-child{border-top:0}
.gr:hover{background:color-mix(in srgb,var(--acc) 5%,transparent)}
.gx1{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.gx1 .gs{font-weight:700;font-size:14px;margin-left:4px}
.gx1 .ge{margin-left:auto}
.gx2{display:flex;gap:6px 16px;flex-wrap:wrap;font-size:13.5px;margin-top:6px;font-variant-numeric:tabular-nums}
.gx2 i{font-style:normal;color:var(--muted);font-size:12px;margin-right:2px}
.gx3{font-size:12.5px;margin-top:4px;color:var(--muted)}
</style>
</head>
<body>
<div class="app">
  <nav class="rail" id="rail" aria-label="Secciones"></nav>
  <main>
    <header class="top">
      <div><h1 id="titulo"></h1><p id="sub"></p><div id="lema"></div></div>
      <div class="controles">
        <span class="chipmeta" id="meta"></span>
        <div class="seg" id="tf" role="group" aria-label="Temporalidad">
          <button data-v="d" aria-pressed="true">Diario</button>
          <button data-v="w" aria-pressed="false">Semanal</button>
        </div>
        <div class="seg" id="tipo" role="group" aria-label="Tipo de activo">
          <button data-v="todo" aria-pressed="true">Todo</button>
          <button data-v="accion" aria-pressed="false">Acciones</button>
          <button data-v="etf" aria-pressed="false">ETF</button>
          <button data-v="cripto" aria-pressed="false">Cripto</button>
        </div>
        <input type="search" id="q" placeholder="Buscar ticker" aria-label="Buscar ticker">
        <button class="chip tvexp" id="grandes" aria-pressed="false" title="Solo acciones con market cap de 10.000 M o más (más parecido al universo de Warren y a lo que ofrecen Quantfury/eToro)">Grandes ≥10 B</button>
        <button class="chip tvexp" id="tvexp" title="Baja un .txt con los tickers de esta vista para importar como watchlist en TradingView">Watchlist TV</button>
      </div>
    </header>
    <div class="viejo" id="viejo" role="status"></div>
    <div id="vista"></div>
    <footer id="pie"></footer>
  </main>
</div>
<div class="velo" id="velo"></div>
<aside class="ficha" id="ficha" aria-hidden="true" aria-label="Ficha del activo"></aside>

<script>
const D = __DATA__;
const S = {gTipo:'', gListos:true, gSel:false, gEmas:false, rsiF:false, macdF:false, pag:'inicio', tf:'d', tipo:'todo', q:'', insideMin:1, soloComp:true, sector:null, emaF:0, epHoy:false};
const P = D.meta.params;
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt = (v,d=2) => (v==null||isNaN(v)) ? '–' : Number(v).toLocaleString('es-AR',{minimumFractionDigits:d,maximumFractionDigits:d});
const big = v => v==null ? 's/d' : v>=1e12 ? fmt(v/1e12,2)+' T' : v>=1e9 ? fmt(v/1e9,1)+' B' : v>=1e6 ? fmt(v/1e6,1)+' M' : fmt(v/1e3,0)+' k';
const pr = v => v==null ? '–' : fmt(v, v<1 ? 4 : 2);
const pct = (v,d=2) => (v==null||isNaN(v)) ? '–' : (v>0?'+':'')+fmt(v,d)+'%';
const cls = v => v>0 ? 'up' : v<0 ? 'down' : 'mut';
const TFN = {d:'diario', w:'semanal'};
const EST = {'rompe':['rompe','Rompiendo'],'por romper':['porromper','Por romper'],'arriba':['otro','Arriba'],'abajo':['otro','Abajo'],
  'disparado':['disparado','Disparado'],
  'armada':['armado','Armada'],'recien':['rompio','Recién rompió'],'confirmo':['rompe','Confirmó'],'formandose':['otro','Formándose'],'sinvol':['otro','Rompió sin volumen'],'fallo':['falla','Falló'],'armado':['armado','Armado'],'esperando':['otro','Esperando'],'rompio':['rompio','Rompió'],'preparada':['preparada','Preparada']};
const badge = e => { const x = EST[e] || ['otro', e]; return `<span class="est ${x[0]}">${x[1]}</span>`; };
const ESTADIOS = {1:'Estadio 1 · base',2:'Estadio 2 · tendencia alcista',3:'Estadio 3 · techo',4:'Estadio 4 · tendencia bajista'};

const IC = {
  inicio:'<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
  sectores:'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
  avwap:'<path d="M3 17c3-1 5-6 8-6s4 3 7 1 3-5 3-5"/><path d="M3 12h18" stroke-dasharray="2 3"/>',
  comp:'<path d="M4 7h16M7 12h10M10 17h4"/>',
  vcp:'<path d="M2 8l4 9 4-7 3 5 3-3 2 2 4-8"/>',
  inside:'<rect x="3" y="3" width="18" height="18" rx="3"/><rect x="8" y="8" width="8" height="8" rx="2"/>',
  ep:'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
  setups:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
  req:'<path d="M20 6L9 17l-5-5"/>'
};
IC.gatillos = '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>';
const ico = k => `<svg viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
const PAGS = [
  ['inicio','Hoy','Lo que hay que mirar para la próxima rueda.'],
  ['gatillos','Gatillos','Todos los setups en una tabla: VCP, AVWAP, compresión, inside, episodic y 30 min.'],
  ['ranking','Ranking','Las mejores del radar y si los filtros están funcionando.'],
  ['mercado','Mercado','Régimen, rotación, sectores y cartelera del día.'],
];
IC.ranking = '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M17 5h3a3 3 0 0 1-3 4M7 5H4a3 3 0 0 0 3 4"/>';
IC.mercado = '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>';
IC.inicio = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>';

function spark(arr, w=84, h=24){
  if(!arr || arr.length < 2) return '';
  const mn = Math.min(...arr), mx = Math.max(...arr), r = (mx-mn) || 1;
  const pts = arr.map((v,i) => `${(i/(arr.length-1)*w).toFixed(1)},${(h-2-(v-mn)/r*(h-4)).toFixed(1)}`).join(' ');
  const c = arr[arr.length-1] >= arr[0] ? 'var(--up)' : 'var(--down)';
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" aria-hidden="true"><polyline points="${pts}" fill="none" stroke="${c}" stroke-width="1.6" stroke-linejoin="round"/></svg>`;
}
const flags = (a, max=2) => (a.flags||[]).filter(f=>f.k!=='earn').slice(0,max).map(f=>`<span class="fl ${f.tipo}" title="${esc(f.t)}">${esc(f.c)}</span>`).join('');
const canslim = a => a.fund && ((a.fund.pts_eps||0)+(a.fund.pts_ventas||0)) >= 5 ? '<span class="cs" title="EPS y/o ventas creciendo fuerte o acelerando (CAN SLIM)">C</span>' : '';
// 📅 = presenta balance en los próximos 7 días (en todas las listas)
const earnD = a => { if(a.earn_dias!=null) return a.earn_dias; const x = (D.meta.earn_cal||[]).find(e=>e.t===a.t); return x ? Math.round((Date.parse(x.fecha+'T12:00:00') - Date.now())/864e5) : null; };
const earnB = a => { const d = earnD(a); return d!=null && d>=0 && d<=7 ? `<span class="ern" title="Presenta balance ${d===0?'hoy':d===1?'mañana':'en '+d+' días'}">📅 ${d===0?'hoy':d+'d'}</span>` : ''; };
const tk = (a, fl=true) => `<span class="tk">${esc(a.t)}</span>${canslim(a)}${earnB(a)}${fl ? flags(a) : ''}`;
const ARR = {2:['▲','s2'],1:['▲','s1'],'-1':['▼','b1'],'-2':['▼','b2']};
const flecha = (v, t='') => { const x = ARR[v]; return x ? `<span class="ar ${x[1]}" title="${t}">${x[0]}</span>` : `<span class="ar" title="${t}">–</span>`; };
const xo8 = a => `<span class="x8 ${a.mv>=7?'up':a.mv>=5?'warn':'down'}">${a.mv}/8</span>`;
const EMAS_N = ['E10','E20','E50','E150','E200'];
const tend = a => `<span class="tend">${xo8(a)}<span class="ars">${(a.pend||[]).map((v,i)=>flecha(v,EMAS_N[i])).join('')}<i></i>${flecha(a.m1d,'Momentum diario')}${flecha(a.m1w,'Momentum semanal')}</span></span>`;
const adrC = v => v==null ? '<span class="mut">s/d</span>' : `<span class="adr${v<1.5?0:v<2.5?1:v<4.5?2:v<6?3:4}">${fmt(v,2)}%</span>`;
const volx = a => a.vol_pct==null ? '–' : `<span class="${a.vol_pct>0?'up':'mut'}">${pct(a.vol_pct,0)}</span>`;
const PILARES = [['Tendencia','tend',P.pts.tend,'var(--blue)'],['Fuerza RS','rs',P.pts.rs,'var(--acc)'],['Contracción','contr',P.pts.contr,'var(--violet)'],['Setup','setup',P.pts.setup,'var(--warn)'],['Fundamentales','fund',P.pts.fund,'#e879a6']];
const PIL = PILARES.filter(x => x[1]!=='fund' || P.pts.fund > 0);
const pilares = a => P.pts.fund <= 0 ? PIL : (a.partes && a.partes.fund==null && a.tipo!=='accion')
  ? PILARES.filter(x=>x[1]!=='fund').map(([n,k,m,c])=>[n, k, +(m*100/(100-P.pts.fund)).toFixed(1), c]) : PILARES;
const TEND = {h:'Tendencia', f:r=>tend(r.a)};
const VOLX = {h:'Vol. vs prom. 50', n:1, f:r=>volx(r.a)};
const insB = a => { const b = [['d','D'],['w','W']].filter(([k])=>a.inside[k]&&a.inside[k].n).map(([k,l])=>{ const n=a.inside[k].n; return `<span class="ins" title="${n} inside ${k==='d'?'day':'week'}${n>1?' seguidos':''}">${n>1?n:''}I${l}</span>`; }); return b.length ? b.join(' ') : '<span class="mut">–</span>'; };
const INSC = {h:'Inside', f:r=>insB(r.a)};
const barra = v => `<span class="sc"><span class="barra"><i style="width:${Math.max(0,Math.min(100,v))}%"></i></span><span>${fmt(v,0)}</span></span>`;
function ring(v, size=70, col='var(--acc)'){
  const r = size/2-6, c = 2*Math.PI*r;
  return `<div class="ring" style="width:${size}px;height:${size}px"><svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" aria-hidden="true">
    <circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="var(--line)" stroke-width="6"/>
    <circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="${col}" stroke-width="6" stroke-linecap="round"
      stroke-dasharray="${(c*v/100).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 ${size/2} ${size/2})"/></svg><b>${fmt(v,0)}</b></div>`;
}
const rsiOk = a => a.sem && a.sem.rsi_dir==='arriba' && a.sem.rsi_hace!=null && a.sem.rsi_hace < P.cruce_sem;
const macdOk = a => a.sem && a.sem.macd_dir==='arriba' && a.sem.macd_hace!=null && a.sem.macd_hace < P.cruce_sem;
const pasaSem = a => true;
const hace = n => n===0 ? 'esta semana' : n===1 ? 'hace 1 semana' : `hace ${n} semanas`;
function visibles(conSolo30=false){
  const q = S.q.trim().toLowerCase();
  return D.activos.filter(a => (conSolo30 || !a.sin_av) && (S.tipo==='todo' || a.tipo===S.tipo) && pasaSem(a) &&
    (!S.grandes || a.tipo!=='accion' || (a.mcap||0) >= 1e10) &&
    (!q || a.t.toLowerCase().includes(q) || (a.nombre||'').toLowerCase().includes(q)));
}
function mejorAv(a, tf){
  const l = (a.avwap[tf]||[]).filter(x => x.cuenta);
  const r = l.filter(x => x.estado==='rompe').sort((x,y)=>Math.abs(x.dist)-Math.abs(y.dist));
  if(r.length) return r[0];
  return l.filter(x => x.estado==='por romper').sort((x,y)=>Math.abs(x.dist)-Math.abs(y.dist))[0] || null;
}
function tabla(cols, rows, vacio){
  if(!rows.length) return `<p class="vacio">${vacio}</p>`;
  return `<div class="tw"><table><thead><tr>${cols.map(c=>`<th class="${c.n?'n':''}">${c.h}</th>`).join('')}</tr></thead><tbody>${
    rows.map(r=>`<tr data-t="${esc(r.a.t)}" tabindex="0">${cols.map(c=>`<td class="${c.n?'n':''}">${c.f(r)}</td>`).join('')}</tr>`).join('')
  }</tbody></table></div>`;
}
// Fila compacta: ticker + setup + estado arriba; entrada, stop, riesgo y distancia abajo
function filasLista(items, vacio){
  if(!items.length) return `<p class="vacio">${vacio}</p>`;
  return `<div class="gl">${items.map(x=>`<div class="gr" data-t="${esc(x.a.t)}" tabindex="0">
    <div class="gx1">${x.pre||''}${tk(x.a)}${x.extra||''}<span class="gs">${x.setup}</span>${x.est?`<span class="ge">${x.est}</span>`:''}</div>
    <div class="gx2"><span><i>Entrada</i> ${pr(x.e)}</span><span><i>Stop</i> ${pr(x.st)}</span><span><i>Riesgo</i> ${x.r!=null?`<b class="${x.r>P.foco_riesgo?'warn':''}">${fmt(x.r,1)}%</b>`:'–'}</span><span><i>vs. entrada</i> ${x.d!=null?`<b class="${cls(x.d)}">${pct(x.d,1)}</b>`:'–'}</span><span><i>Score</i> <b>${fmt(x.a.score,0)}</b></span></div>
    ${x.det?`<div class="gx3">${x.det}</div>`:''}</div>`).join('')}</div>`;
}
const card = (titulo, sub, cuerpo) => `<div class="card"><h3>${titulo}${sub!=null?` <small>${sub}</small>`:''}</h3>${cuerpo}</div>`;

/* ---------- Inicio ---------- */
function regExtra(R){
  const fg = R.fng, F = R.ftd || {};
  const fgC = !fg ? '' : fg.score<=25 ? 'down' : fg.score<45 ? 'warn' : fg.score<=55 ? 'mut' : 'up';
  const ftdTxt = Object.values(F).map(e => e.estado==='follow-through' ? `<span class="up">${esc(e.t)}: follow-through el ${esc(fechaCorta(e.ftd))} (día ${e.ftd_dia}, +${fmt(e.suba,2)}%)</span>`
    : e.estado==='intento de rally' ? `<span class="warn">${esc(e.t)}: intento de rally, día ${e.dia} desde el ${esc(e.minimo)} (−${fmt(e.caida,1)}%)</span>`
    : `<span class="mut">${esc(e.t)}: ${esc(e.estado)}</span>`).join(' · ');
  return `<div class="kv" style="margin-top:12px">
    <span>Fear &amp; Greed (CNN)</span><span>${fg ? `<b class="${fgC}">${fmt(fg.score,0)} · ${esc(fg.rating)}</b> <span class="mut">semana ${fmt(fg.semana,0)} · mes ${fmt(fg.mes,0)}</span>` : 's/d'}</span>
    <span>Follow-through (O'Neil)</span><span>${ftdTxt || 's/d'}</span></div>
    ${fg && fg.score<=25 ? '<p class="nota" style="margin:8px 0 0">Miedo extremo: dato contrario, no suma al score. Buen momento para armar la lista; para comprar rupturas conviene esperar el follow-through.</p>' : ''}`;
}
function area(h){
  const w = 600, ht = 90, v = h.map(x=>x[1]), mn = Math.max(0, Math.min(...v) - 5), mx = Math.min(100, Math.max(...v) + 5);
  const X = i => i/(h.length-1)*w, Y = x => ht - (x-mn)/(mx-mn||1)*ht;
  const pts = v.map((x,i)=>`${X(i).toFixed(1)},${Y(x).toFixed(1)}`).join(' ');
  const ult = v[v.length-1], col = ult>=60?'var(--up)':ult>=40?'var(--warn)':'var(--down)';
  return `<svg viewBox="0 0 ${w} ${ht+18}" width="100%" preserveAspectRatio="none" aria-hidden="true">
    <polygon points="0,${ht} ${pts} ${w},${ht}" fill="${col}" opacity=".12"/><polyline points="${pts}" fill="none" stroke="${col}" stroke-width="2" vector-effect="non-scaling-stroke"/>
    <text x="0" y="${ht+14}" class="ax">${esc(h[0][0])}</text><text x="${w}" y="${ht+14}" text-anchor="end" class="ax">${esc(h[h.length-1][0])} · ${fmt(ult,0)}%</text></svg>`;
}
function gauge(v){
  const L = Math.PI*90, col = v<40?'var(--down)':v<60?'var(--warn)':'var(--acc)';
  return `<svg viewBox="0 0 200 110" width="100%" aria-hidden="true">
    <path d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>
    <path d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke="${col}" stroke-width="14" stroke-linecap="round" stroke-dasharray="${(L*v/100).toFixed(1)} ${L.toFixed(1)}"/></svg>`;
}
const m0 = E => E.length ? E[0][1] : 0;
const symTV = t => { const a = D.activos.find(x=>x.t===t);
  if(a && a.tipo==='cripto') return 'CRYPTO:' + t.replace('-','');
  const s = t.replace('-','.'); return a && a.bolsa ? a.bolsa + ':' + s : s; };
function exportarTV(){
  // Una sección por tarjeta de la vista actual, en el orden en que se ven (formato de importación de TradingView)
  const partes = [], vistos = new Set();
  document.querySelectorAll('#vista .card').forEach(c => {
    const h = c.querySelector('h3'); const ts = [...c.querySelectorAll('[data-t]')].map(x=>x.dataset.t).filter(t=>!vistos.has(t));
    if(!ts.length) return;
    ts.forEach(t=>vistos.add(t));
    const titulo = h ? (h.childNodes[0].textContent || '').trim().replace(/[,#]/g,'') : 'Lista';
    partes.push('###' + titulo, ...ts.map(symTV));
  });
  if(!partes.length){ alert('No hay tickers en esta vista.'); return; }
  const pg = PAGS.find(x=>x[0]===S.pag), nombre = (D.meta.nombre||'radar').replace(/\s+/g,'_') + '_' + (S.pag==='gatillos' && S.gTipo ? S.gTipo : S.pag) + '.txt';
  const b = new Blob([partes.join(',\n')], {type:'text/plain'}), u = URL.createObjectURL(b);
  const l = document.createElement('a'); l.href = u; l.download = nombre; document.body.appendChild(l); l.click(); l.remove(); setTimeout(()=>URL.revokeObjectURL(u), 1000);
}
const fechaCorta = f => { const x = /(\d{4})-(\d{2})-(\d{2})/.exec(f||''); return x ? `${+x[3]}-${MES[+x[2]-1]}` : (f||''); };
function eventosSemana(nd=6){
  const DIAS = ['DOM','LUN','MAR','MIÉ','JUE','VIE','SÁB'];
  const hoy = new Date(); const iso = d => `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  const dias = []; for(let i=0; i<10 && dias.length<nd; i++){ const d = new Date(hoy.getTime() + i*864e5); if(d.getDay()>0 && d.getDay()<6) dias.push(iso(d)); }
  const mac = D.meta.macro || [];
  const idxE = Object.fromEntries(D.activos.map(a=>[a.t,a]));
  // Calendario de NASDAQ (grandes + radar); si no vino, se usa la fecha de earnings de cada acción del radar
  const ear = (D.meta.earn_cal && D.meta.earn_cal.length)
    ? D.meta.earn_cal.map(x=>({f:x.fecha, t:x.t, n:x.n, mom:x.mom, eps:x.eps, mcap:x.mcap, a:idxE[x.t]}))
    : D.activos.filter(a=>a.tipo==='accion' && a.earn_prox).map(a=>{ const [dd,mm,yy] = a.earn_prox.split('-');
        return {f:`${yy}-${mm}-${dd}`, t:a.t, n:a.nombre, mom:a.earn_momento?(a.earn_momento.startsWith('antes')?'PRE':'POST'):'', eps:'', mcap:a.mcap||0, a}; });
  const SL = P.sel || {rs:80, mv:7, score:70};
  const esSel = a => !!a && !a.sin_av && a.rs>=SL.rs && a.mv>=SL.mv && a.score>=SL.score;
  const col = f => {
    const m = mac.filter(x=>x.fecha===f), e = ear.filter(x=>x.f===f).sort((x,y)=>esSel(y.a)-esSel(x.a) || (y.mcap||0)-(x.mcap||0));
    const d = new Date(f+'T12:00:00');
    return `<div class="evd ${f===iso(hoy)?'hoy':''}"><div class="evh"><b>${DIAS[d.getDay()]} ${d.getDate()}</b><span class="mut">${m.length+e.length} eventos</span></div>
      ${m.length ? `<h5>Economía EE.UU.</h5>${m.map(x=>`<div class="evm ${x.impacto}"><div><b>${esc(x.titulo)}</b><span class="mut">${esc(x.hora)}</span></div>
        ${x.est||x.ant ? `<small>${x.est?'est. '+esc(x.est):''}${x.est&&x.ant?' · ':''}${x.ant?'ant. '+esc(x.ant):''}</small>` : ''}</div>`).join('')}` : ''}
      ${e.length ? `<h5>Earnings · ${e.length}</h5><div class="eve">${e.slice(0, (S.evMas||{})[f] ? e.length : 15).map(x=>`<div class="evr ${esSel(x.a)?'sel':x.a?'rad':''}" ${x.a?`data-t="${esc(x.t)}" tabindex="0"`:''} title="${esc(x.n)}${x.a?' · en el radar':''}"><b>${esc(x.t)}</b><span class="mut">${x.eps?'EPS est '+esc(x.eps.replace('$','')):''}</span>${x.mom?`<i class="${x.mom==='PRE'?'pre':'post'}">${x.mom}</i>`:'<i></i>'}</div>`).join('')}${e.length>15?`<button class="chip evmas" data-evmas="${f}">${(S.evMas||{})[f] ? 'Ver menos' : `Ver las ${e.length-15} restantes`}</button>`:''}</div>` : ''}
      ${!m.length && !e.length ? '<p class="vacio">Sin eventos relevantes.</p>' : ''}</div>`;
  };
  if(nd<=2){ const hay = dias.filter(f => mac.some(x=>x.fecha===f) || ear.some(x=>x.f===f));
    return hay.length ? `<div class="card"><div class="evs">${hay.map(col).join('')}</div></div>` : '<p class="vacio">Sin datos macro ni earnings relevantes para hoy y mañana.</p>'; }
  return `<div class="card"><div class="evs">${dias.map(col).join('')}</div>
    <p class="nota" style="margin:10px 0 0">Macro de alto (rojo) y medio (ámbar) impacto, sin discursos menores. Earnings de empresas de 10.000 M o más y de todas las del radar (borde verde = Seleccionada, borde azul = en el radar). PRE = antes de la apertura, POST = después del cierre; EPS est = estimado por los analistas.</p></div>`;
}
function lemaHTML(){
  // El poder de las pequeñas mejoras: 1% por día durante un año (interés compuesto)
  const n = 365, w = 230, h = 92, alto = h - 16, base0 = h - 10, linea1 = base0 - alto*0.35;
  // Escala partida: de 0 a 1 ocupa la franja de abajo y de 1 a 38 la de arriba, para que se vean las dos curvas
  const y1 = v => v <= 1 ? base0 - v*(base0 - linea1) : linea1 - (Math.min(v, 38) - 1)/37*(linea1 - 6);
  const sube = [], baja = [];
  for(let d=0; d<=n; d+=5){ const x = 26 + d/n*(w-36); sube.push(`${x.toFixed(1)},${y1(Math.pow(1.01,d)).toFixed(1)}`); baja.push(`${x.toFixed(1)},${y1(Math.pow(0.99,d)*1).toFixed(1)}`); }
  const base = y1(1);
  return `<div class="lema"><div class="lt"><b>The Power of Tiny Gains</b>
      <span>1% better every day <code>1.01<sup>365</sup> = <em class="up">${fmt(Math.pow(1.01,365),2)}</em></code></span>
      <span>1% worse every day <code>0.99<sup>365</sup> = <em class="down">${fmt(Math.pow(0.99,365),2)}</em></code></span></div>
    <svg viewBox="0 0 ${w} ${h+14}" width="${w}" height="${h+14}" aria-label="Mejorar 1% por día durante un año">
      <line x1="26" y1="6" x2="26" y2="${h-10}" stroke="var(--line2)"/><line x1="26" y1="${h-10}" x2="${w-6}" y2="${h-10}" stroke="var(--line2)"/>
      <line x1="26" y1="${base}" x2="${w-6}" y2="${base}" stroke="var(--muted)" stroke-dasharray="3 3"/>
      <text x="20" y="${base+3}" text-anchor="end" class="ax">1</text>
      <polyline points="${sube.join(' ')}" fill="none" stroke="var(--up)" stroke-width="2"/>
      <polyline points="${baja.join(' ')}" fill="none" stroke="var(--down)" stroke-width="2"/>
      <text x="${w-6}" y="${h+4}" text-anchor="end" class="ax">1 año</text></svg></div>`;
}
function bloques(){
  const act = visibles(), tf = 'd', R = D.meta.regimen;
  let rom=0; act.forEach(a => { const m = mejorAv(a, tf); if(m && m.estado==='rompe') rom++; });
  const k = [
    ['req', act.length, 'cumplen los requisitos', 'sectores'],
    ['avwap', rom, `rompiendo AVWAP (${TFN[tf]})`, 'setups'],
    ['comp', visibles(true).filter(a=>a.comp[tf]&&a.comp[tf].es&&a.comp[tf].emas).length, `comprimidos con EMAs en ascenso (${TFN[tf]})`, 'comp'],
    ['inside', act.filter(a=>a.inside[tf]&&a.inside[tf].n>=1).length, `con inside ${tf==='d'?'day':'week'}`, 'inside'],
    ['ep', act.filter(a=>a.ep).length, 'episodic pivots (10 ruedas)', 'ep'],
    ['setups', visibles(true).filter(a=>(!a.sin_av&&a.setup_av[tf]) || (a.pivot30&&a.pivot30.estado!=='esperando') || (a.vcp&&['armada','recien'].includes(a.vcp.estado))).length, 'con algún setup activo', 'setups'],
  ];
  const kpis = `<div class="kpis">${k.map(([ic,v,l,p])=>`<button class="card kpi" data-ir="${p}"><span class="ic">${ico(ic)}</span><b>${v}</b><span>${l}</span></button>`).join('')}</div>`;
  const reg = R ? `<div class="card"><h3>Régimen de mercado <small>contexto para dimensionar</small></h3>
    <div class="reg"><div class="gauge">${gauge(R.score)}<div class="v"><b>${fmt(R.score,0)}</b><span style="color:${R.score<40?'var(--down)':R.score<60?'var(--warn)':'var(--acc)'}">${esc(R.etiqueta)}</span></div></div>
      <div class="capas">${R.capas.map(c=>`<div class="capa"><div class="fila"><span>${esc(c.nombre)}</span><span>${fmt(c.pts,0)} / ${c.max}</span></div>
        <div class="pbar"><i style="width:${c.pts/c.max*100}%"></i></div>${c.det.map(d=>`<small>${esc(d)}</small>`).join('')}</div>`).join('')}</div></div>
    ${regExtra(R)}
    ${(R.hist200||[]).length>2 ? `<div class="h200"><small class="mut">% de acciones líquidas sobre su EMA200 · últimas ${R.hist200.length} ruedas</small>${area(R.hist200)}</div>` : ''}
    <div class="rec">${R.expo ? `<b class="expo">Exposición sugerida: ${esc(R.expo)}</b> · ` : ''}${esc(R.rec)} <span class="mut">(lectura del mercado, no tamaño de posición)</span></div></div>` : card('Régimen de mercado', null, '<p class="vacio">No se pudo calcular en esta corrida.</p>');
  const top = act.slice().sort((x,y)=>y.score-x.score).slice(0,3);
  const idx = Object.fromEntries(D.activos.map(a=>[a.t,a]));
  const fl = (D.foco||[]).filter(f=>idx[f.t] && visibles(true).includes(idx[f.t]));
  let AMBAS = new Set();
  const ambas = t => AMBAS.has(t) ? ' <span class="ambas" title="Está en la Lista de foco y en la Crème de la crème">⭐ ambas</span>' : '';
  const cFo = [
    {h:'Ticker', f:r=>tk(idx[r.t])+ambas(r.t)},
    {h:'Setup', f:r=>esc(r.setup)},
    {h:'Entrada', n:1, f:r=>pr(r.entrada)},
    {h:'Stop', n:1, f:r=>pr(r.stop)},
    {h:'Riesgo', n:1, f:r=>fmt(r.riesgo,1)+'%'},
    {h:'Precio vs. entrada', n:1, f:r=>`<span class="${cls(r.dist)}">${pct(r.dist)}</span>`},
    {h:'Score', n:1, f:r=>fmt(r.score,0)},
  ];
  const focoF = () => card('Lista de foco', fl.length ? fl.length+' para operar' : null,
    `<p class="nota" style="margin:0 0 6px">VCP, compresión o AVWAP con volumen · RS ${P.foco_rs}+ · riesgo ≤${fmt(P.foco_riesgo,0)}% · sin banderas ni earnings.${R && R.score<40 ? ' <b>Régimen defensivo: tamaño chico o esperar.</b>' : ''}</p>`
    + filasLista(fl.map(r=>({a:idx[r.t], extra:ambas(r.t), setup:esc(r.setup), e:r.entrada, st:r.stop, r:r.riesgo, d:r.dist})), 'Ningún setup cumple todo hoy. Mejor esperar que forzar.'));
  const spot = top.length ? `<div class="grid g3">${top.map(a=>`<div class="card spot" data-t="${esc(a.t)}" tabindex="0">
      <div class="cab">${ring(a.score)}<div><h4>${esc(a.t)}</h4><p>${esc(a.sector)}${a.estadio?' · estadio '+a.estadio:''}</p><p>${flags(a,3)}</p></div></div>
      <div class="partes">${pilares(a).map(([n,k,m,c])=>`<span class="mut">${n}</span><span class="pbar"><i style="width:${(a.partes[k]||0)/m*100}%;background:${c}"></i></span><span>${fmt(a.partes[k]||0,0)}</span>`).join('')}</div></div>`).join('')}</div>`
    : '<p class="vacio">Sin activos con estos filtros.</p>';
  const ev = act.filter(a=>a.earn_dias!=null && a.earn_dias>=0 && a.earn_dias<=7).sort((x,y)=>x.earn_dias-y.earn_dias);
  const earn = ev.length ? `<div class="earn">${ev.map(a=>`<div class="eitem" data-t="${esc(a.t)}" tabindex="0"><b>${esc(a.t)}</b>
      <span>${esc(a.earn_prox)} · ${a.earn_dias===0?'hoy':a.earn_dias===1?'mañana':'en '+a.earn_dias+' días'}</span>
      ${a.earn_momento?`<em class="${a.earn_momento.startsWith('antes')?'bmo':''}">${esc(a.earn_momento)}</em>`:''}</div>`).join('')}</div>`
    : '<p class="vacio">Ningún activo de la lista reporta en los próximos 7 días.</p>';
  const E = D.meta.embudo || [];
  const emb = E.length ? card('Embudo de filtros', `${fmt(m0(E),0)} activos analizados`,
    `<div class="embudo">${E.map(([k,n],i)=>`<div class="paso"><b>${fmt(n,0)}</b><span>${esc(k)}</span></div>${i<E.length-1?'<i>→</i>':''}`).join('')}</div>`
    + (D.meta.n_extra ? `<p class="nota" style="margin:10px 0 0">Además, ${D.meta.n_extra} sin AVWAP activa aparecen solo en Gatillos (VCP, compresión o 30 min).</p>` : '')) : '';
  const T = D.meta.top;
  let topOpt = '';
  const topH = T && T.filas.length ? (() => {
    const mx = Math.max(...T.filas.map(f=>Math.abs(f.ret||0)), 0.01);
    const big = (t, v, c) => `<div class="tbig"><span>${t}</span><b class="${cls(v)}">${pct(v)}</b></div>`;
    const cols = [
      {h:'', f:r=>`<span class="rk">${r.i+1}</span>`},
      {h:'Ticker', f:r=>tk(r.a, false)},
      {h:'Evolución', f:r=>spark(r.f.spark)},
      {h:'Score', n:1, f:r=>`<span class="scp">${fmt(r.f.score,0)}</span>`},
      {h:'Entró', n:1, f:r=>`<span class="mut">${esc(fechaCorta(r.f.entro))}</span>`},
      {h:'', f:r=>`<span class="rbar"><i class="${r.f.ret<0?'neg':''}" style="width:${Math.abs(r.f.ret||0)/mx*100}%"></i></span>`},
      {h:'Retorno', n:1, f:r=>`<b class="${cls(r.f.ret)}">${pct(r.f.ret)}</b>`},
    ];
    const idx = Object.fromEntries(D.activos.map(a=>[a.t,a]));
    const M = T.mejores || [];
    const mxM = Math.max(...M.map(f=>Math.abs(f.ret||0)), 0.01);
    const colsM = cols.map(c => c.h==='' && String(c.f).includes('rbar') ? {h:'', f:r=>`<span class="rbar"><i class="${r.f.ret<0?'neg':''}" style="width:${Math.abs(r.f.ret||0)/mxM*100}%"></i></span>`} : c)
      .concat([{h:'Sigue', f:r=>r.f.sigue?'<span class="up">sí</span>':'<span class="mut">no</span>'}]);
    topOpt = M.length ? `${card(`Top ${M.length} por retorno`, `las que más ganaron entre todas las que pasaron por el Top ${P.top_n} en ${T.ruedas} ${T.ruedas===1?'rueda':'ruedas'} · estilo Warren`,
      `<div class="tbigs">${big(`Retorno medio`, T.medio_mejores)}${big('SPY', T.spy)}</div>`
      + tabla(colsM, M.map((f,i)=>({f, i, a: idx[f.t] || {t:f.t}})), '')
      + `<p class="nota" style="margin:10px 0 0">Lectura optimista: elige las mejores sabiendo el resultado. La medición honesta es el Top actual por score.</p>`)}` : '';
    return `<div class="foco">${card(`Top ${T.filas.length} actual por score`, `retorno desde que entraron · últimas ${T.ruedas} ${T.ruedas===1?'rueda':'ruedas'} desde ${esc(fechaCorta(T.desde))}`,
      `<div class="tbigs">${big(`Retorno medio Top ${T.filas.length}`, T.medio)}${big('SPY', T.spy)}</div>`
      + tabla(cols, T.filas.filter(f=>idx[f.t]).map((f,i)=>({f, i, a:idx[f.t]})), '')
      + (T.ruedas < P.top_ruedas ? `<p class="nota" style="margin:10px 0 0">El historial arrancó hace ${T.ruedas} ${T.ruedas===1?'rueda':'ruedas'}: hasta juntar ${P.top_ruedas}, la ventana es más corta.</p>` : ''))}</div>`;
  })() : '';
  const idx2 = Object.fromEntries(D.activos.map(a=>[a.t,a]));
  const nv = (T && T.nuevos || []).filter(t=>idx2[t]).map(t=>idx2[t]);
  const cNv = [
    {h:'Ticker', f:r=>tk(r.a, false)},
    {h:'3 meses', f:r=>spark(r.a.spark_d)},
    {h:'Score', n:1, f:r=>`<span class="scp">${fmt(r.a.score,0)}</span>`},
    {h:'RS', n:1, f:r=>fmt(r.a.rs,0)},
    {h:'vs EMA200', n:1, f:r=>`<span class="${cls(r.a.d200)}">${pct(r.a.d200,1)}</span>`},
  ];
  const nuevos = card('Nuevos ingresos al Top 30', T && T.nuevos_desde ? 'contra el '+esc(fechaCorta(T.nuevos_desde)) : null,
    T && T.nuevos_desde ? tabla(cNv, nv.map(a=>({a})), 'Ninguna entró al Top 30 desde la rueda anterior.') : '<p class="vacio">Aparece desde la próxima rueda (hace falta el historial de ayer).</p>');
  const C = D.meta.cartelera;
  const cartG = S.cartG ?? S.grandes;
  const filt = l => (l||[]).filter(x => !cartG || (x.mcap||0) >= 1e10).slice(0, P.cart_n || 6);
  const lista = (l, c) => `<div class="cart">${filt(l).map(x=>`<div class="ci ${idx2[x.t]?'en':''}" ${idx2[x.t]?`data-t="${esc(x.t)}" tabindex="0"`:''}><b>${esc(x.t)}</b><span>${esc(x.n)}</span><em class="${c}">${pct(x.chg,1)}</em></div>`).join('')}</div>`;
  const listaR = (l, c) => filt(l).length ? `<div class="cart">${filt(l).map(x=>`<div class="ci ${idx2[x.t]?'en':''}" ${idx2[x.t]?`data-t="${esc(x.t)}" tabindex="0"`:''}><b>${esc(x.t)}</b><span>${esc(x.n)}</span><em class="${c}">${fmt(x.rsi,1)}</em></div>`).join('')}</div>` : '<p class="vacio">Ninguna hoy.</p>';
  const cart = C ? card('Cartelera del día', `<span class="cartsel"><button class="chip" data-cartg="0" aria-pressed="${!cartG}">≥1 B</button><button class="chip" data-cartg="1" aria-pressed="${!!cartG}">≥10 B</button></span>`,
    `<div class="g2c"><div><h5 class="up">Más suben</h5>${lista(C.suben,'up')}</div><div><h5 class="down">Más bajan</h5>${lista(C.bajan,'down')}</div></div>`
    + (C.sobrecompra ? `<div class="g2c" style="margin-top:14px"><div><h5 style="color:#EF6C00">Sobrecompradas · RSI ${P.rsi_alto}+</h5>${listaR(C.sobrecompra,'rc')}</div><div><h5 style="color:var(--blue)">Sobrevendidas · RSI ${P.rsi_bajo} o menos</h5>${listaR(C.sobreventa,'rv')}</div></div>` : '')) : '';
  const SL = P.sel || {rs:80, mv:7, score:70};
  const sel = act.filter(a=>!a.sin_av && a.rs>=SL.rs && a.mv>=SL.mv && a.score>=SL.score).sort((x,y)=>y.score-x.score);
  const estSel = a => a.vcp && ['armada','recien'].includes(a.vcp.estado) ? badge(a.vcp.estado)
    : (mejorAv(a,'d') ? badge(mejorAv(a,'d').estado) : '<span class="mut">–</span>');
  const cSel = [
    {h:'', f:r=>`<span class="rk">${r.i+1}</span>`},
    {h:'Ticker', f:r=>tk(r.a)},
    TEND,
    {h:'3 meses', f:r=>spark(r.a.spark_d)},
    {h:'Score', n:1, f:r=>`<span class="scp">${fmt(r.a.score,0)}</span>`},
    {h:'RS', n:1, f:r=>fmt(r.a.rs,0)},
    {h:'ADR', n:1, f:r=>adrC(r.a.adr)},
    VOLX,
    INSC,
    {h:'TC', f:r=>tcBadge(r.a.tc)},
    {h:'VCP / AVWAP', f:r=>estSel(r.a)},
    {h:'Sector', f:r=>`<span class="mut">${esc(r.a.sector)}</span>`},
  ];
  const selH = `<div class="foco">${card('Seleccionadas', `${sel.length} · RS ${SL.rs}+, ${SL.mv}/8 o más y score ${SL.score}+`,
    tabla(cSel, sel.map((a,i)=>({a,i})), 'Ninguna cumple los tres filtros hoy.'))}</div>`;
  const H = D.meta.selh;
  const trackH = H ? `<div class="foco">${card('Track record de Seleccionadas', `ingresos de las últimas ${H.ruedas} ${H.ruedas===1?'rueda':'ruedas'}`,
    `<div class="tbigs">${['Retorno medio','SPY mismo período','Positivas'].map((t,i)=>`<div class="tbig"><span>${t}</span><b class="${i<2?cls([H.medio,H.spy][i]):''}">${i<2?pct([H.medio,H.spy][i]):(H.aciertos!=null?fmt(H.aciertos,0)+'%':'–')}</b></div>`).join('')}</div>`
    + tabla([
        {h:'Ticker', f:r=>tk(r.a||{t:r.f.t}, false)},
        {h:'Entró', n:1, f:r=>`<span class="mut">${esc(fechaCorta(r.f.entro))}</span>`},
        {h:'Precio entrada', n:1, f:r=>pr(r.f.px)},
        {h:'Actual', n:1, f:r=>pr(r.f.ahora)},
        {h:'Retorno', n:1, f:r=>`<b class="${cls(r.f.ret)}">${pct(r.f.ret)}</b>`},
        {h:'SPY', n:1, f:r=>`<span class="${cls(r.f.spy)}">${pct(r.f.spy)}</span>`},
        {h:'Sigue', f:r=>r.f.sigue?'<span class="up">sí</span>':'<span class="mut">no</span>'},
      ], H.filas.slice(0, S.trackMas ? H.filas.length : 10).map(f=>({f, a: idx2[f.t] || {t:f.t}})), 'Todavía no hay ingresos registrados: se van sumando desde hoy.')
    + (H.filas.length > 10 ? `<button class="chip" data-trackmas="1" style="margin-top:10px">${S.trackMas ? 'Ver menos' : 'Ver los '+(H.filas.length-10)+' restantes'}</button>` : '')
    + (H.ruedas < 5 ? `<p class="nota" style="margin:10px 0 0">El registro arrancó hace ${H.ruedas} ${H.ruedas===1?'rueda':'ruedas'}; se vuelve útil con algunas semanas de historia.</p>` : ''))}</div>` : '';
  // Crème: Seleccionadas con un gatillo concreto cerca (mismo criterio que "armadas" del resumen de Telegram)
  const CERCA = P.resumen_cerca || 2;
  const gatillo = a => {
    const v = a.vcp, s = a.setup_av && a.setup_av.d, c = a.comp && a.comp.d, i = a.inside && a.inside.d;
    if(v && v.estado==='recien') return {m:'VCP recién rota', e:v.pivot, st:v.stop, d:v.dist};
    if(v && (v.estado==='armada' || (v.dist!=null && v.dist>=-CERCA && v.dist<=0))) return {m:'VCP '+v.estado, e:v.pivot, st:v.stop, d:v.dist};
    if(s && s.estado==='rompe') return {m:'Ruptura AVWAP '+s.ancla.toLowerCase(), e:s.entrada, st:s.stop, d:(a.precio/s.entrada-1)*100};
    if(s && s.estado==='por romper' && (s.entrada/a.precio-1)*100 <= CERCA) return {m:'AVWAP '+s.ancla.toLowerCase()+' por romper', e:s.entrada, st:s.stop, d:(a.precio/s.entrada-1)*100};
    if(c && c.ruptura) return {m:'Ruptura de compresión', e:c.gatillo, st:c.piso, d:c.dist_gatillo!=null?-c.dist_gatillo:null};
    if(c && c.es && c.dist_gatillo!=null && c.dist_gatillo <= CERCA) return {m:'Compresión cerca del gatillo', e:c.gatillo, st:c.piso, d:-c.dist_gatillo};
    if(i && i.n>=1 && i.dist_hi!=null && i.dist_hi <= CERCA) return {m:(i.n>1?i.n+' ':'')+'inside day', e:i.madre_hi, st:i.madre_lo, d:-i.dist_hi};
    if(a.tc && a.tc.cerca) return {m:a.tc.n+' cierres apretados (TC)', e:null, st:null, d:a.tc.dist};
    return null;
  };
  const crema = sel.map(a=>({a, g:gatillo(a)})).filter(x=>x.g && (x.g.d==null || x.g.d <= (P.zona_compra||5)));
  const cCr = [
    {h:'', f:r=>`<span class="rk">${r.i+1}</span>`},
    {h:'Ticker', f:r=>tk(r.a)+ambas(r.a.t)},
    {h:'Gatillo', f:r=>`<b>${esc(r.g.m)}</b>`},
    {h:'Entrada', n:1, f:r=>pr(r.g.e)},
    {h:'Stop', n:1, f:r=>pr(r.g.st)},
    {h:'Riesgo', n:1, f:r=>r.g.e&&r.g.st&&r.g.e>r.g.st ? fmt((r.g.e-r.g.st)/r.g.e*100,1)+'%' : '–'},
    {h:'Precio vs. gatillo', n:1, f:r=>r.g.d!=null ? `<span class="${cls(r.g.d)}">${pct(r.g.d)}</span>` : '–'},
    {h:'Score', n:1, f:r=>`<span class="scp">${fmt(r.a.score,0)}</span>`},
  ];
  AMBAS = new Set(crema.map(x=>x.a.t).filter(t=>fl.some(f=>f.t===t)));
  const cremaF = () => card('Crème de la crème', crema.length ? crema.length+' con gatillo cerca' : null,
    `<p class="nota" style="margin:0 0 6px">Seleccionadas (RS ${(P.sel||{}).rs||80}+, ${(P.sel||{}).mv||7}/8+, score ${(P.sel||{}).score||70}+) con un gatillo cerca o recién roto. vs. entrada negativo = falta; positivo = ya rompió.</p>`
    + filasLista(crema.map(x=>({a:x.a, extra:ambas(x.a.t), setup:esc(x.g.m), e:x.g.e, st:x.g.st, r:x.g.e&&x.g.st&&x.g.e>x.g.st?(x.g.e-x.g.st)/x.g.e*100:null, d:x.g.d})), 'Ninguna Seleccionada tiene un gatillo cerca hoy.'));
  const dosH = `<div class="grid g2 dos foco">${focoF()}${cremaF()}</div>${AMBAS.size ? `<p class="nota" style="margin:-8px 0 16px">⭐ ambas = está en las dos listas: ${[...AMBAS].map(esc).join(', ')}.</p>` : ''}`;
  return {reg, dosH, selH, trackH, topH, topOpt, nuevos, cart, emb: emb ? `<div class="foco">${emb}</div>` : ''};
}

function regMini(R){
  if(!R) return '';
  const c = R.score<40?'var(--down)':R.score<60?'var(--warn)':'var(--acc)';
  const F = R.ftd || {};
  const ftd = Object.values(F).filter(e=>e.estado==='follow-through' || e.estado==='intento de rally')
    .map(e=>e.estado==='follow-through' ? `${esc(e.t)}: follow-through el ${esc(fechaCorta(e.ftd))}` : `${esc(e.t)}: intento de rally, día ${e.dia}`).join(' · ');
  const fg = R.fng;
  return `<button class="card regmini" data-ir="mercado" aria-label="Ver el detalle del mercado">
    <div class="rgv"><b style="color:${c}">${fmt(R.score,0)}</b><span style="color:${c}">${esc(R.etiqueta)}</span></div>
    <div class="rgt"><span class="mono">Régimen de mercado</span>
      <span>${R.expo ? `<b>Exposición sugerida ${esc(R.expo)}.</b> ` : ''}${esc(R.rec)}</span>
      <span class="mut">${R.capas.map(x=>`${esc(x.nombre.split(' (')[0])} ${fmt(x.pts,0)}/${x.max}`).join(' · ')}${fg ? ` · Fear &amp; Greed ${fmt(fg.score,0)}` : ''}${ftd ? ' · '+ftd : ''}</span></div>
    <span class="ver">Mercado →</span></button>`;
}
function vInicio(){
  const B = bloques(), R = D.meta.regimen;
  return `${regMini(R)}${B.dosH}
    <h2 class="sec">Próximas ruedas <small>macro de impacto y earnings · hora Argentina</small></h2>${eventosSemana(2)}`;
}
function vRanking(){
  const B = bloques();
  return `${B.selH}${B.topH}${B.trackH}<div class="grid g2" style="margin-bottom:18px">${B.nuevos}${B.topOpt || ''}</div>${B.emb}`;
}
function vMercado(){
  const B = bloques();
  return `<div class="foco">${B.reg}</div>${rotacionHTML()}
    <h2 class="sec">Sectores <small>calor = score (60%) + retorno del último mes (40%) · tocá un sector</small></h2>${vSectores()}
    <div style="margin-top:18px">${B.cart}</div>
    <h2 class="sec">Eventos de la semana <small>macro de EE.UU. de impacto y earnings · hora Argentina</small></h2>${eventosSemana(6)}`;
}

/* ---------- Sectores ---------- */
const CUAD = {lid:['Liderando','var(--up)'], deb:['Debilitándose','var(--warn)'], rez:['Rezagados','var(--down)'], mej:['Mejorando','var(--blue)']};
const cuad = (x, y) => x>=0 ? (y>=0?'lid':'deb') : (y>=0?'mej':'rez');
function rotPuntos(k){
  // k = índice de la semana; la cola une con la semana anterior
  return (D.meta.rotacion.etfs||[]).filter(e=>e.x[k]!=null && e.y[k]!=null)
    .map(e=>({t:e.t, n:e.n, x:e.x[k], y:e.y[k], prev: k>0 && e.x[k-1]!=null && e.y[k-1]!=null ? [e.x[k-1], e.y[k-1]] : null}));
}
function rotSvg(k){
  const R = D.meta.rotacion, pts = rotPuntos(k);
  const ax = Math.max(2, ...R.etfs.flatMap(e=>e.x.filter(v=>v!=null).map(Math.abs))) * 1.08;
  const ay = Math.max(1, ...R.etfs.flatMap(e=>e.y.filter(v=>v!=null).map(Math.abs))) * 1.08;
  const w = 640, h = 380, X = x => w/2 + x/ax*(w/2 - 30), Y = y => h/2 - y/ay*(h/2 - 26);
  const q = (x, y, txt, c) => `<text x="${x}" y="${y}" class="qd" fill="${c}">${txt}</text>`;
  return `<svg viewBox="0 0 ${w} ${h}" width="100%" class="rrg" aria-label="Cuadrantes de rotación contra el SPY">
    <rect x="${w/2}" y="0" width="${w/2}" height="${h/2}" fill="var(--up)" opacity=".05"/><rect x="0" y="0" width="${w/2}" height="${h/2}" fill="var(--blue)" opacity=".05"/>
    <rect x="0" y="${h/2}" width="${w/2}" height="${h/2}" fill="var(--down)" opacity=".05"/><rect x="${w/2}" y="${h/2}" width="${w/2}" height="${h/2}" fill="var(--warn)" opacity=".05"/>
    <line x1="${w/2}" y1="0" x2="${w/2}" y2="${h}" class="ej"/><line x1="0" y1="${h/2}" x2="${w}" y2="${h/2}" class="ej"/>
    ${q(10,18,'MEJORANDO','var(--blue)')}${q(w-10,18,'LIDERANDO','var(--up)').replace('<text','<text text-anchor="end"')}
    ${q(10,h-8,'REZAGADOS','var(--down)')}${q(w-10,h-8,'DEBILITÁNDOSE','var(--warn)').replace('<text','<text text-anchor="end"')}
    ${pts.map(p=>{ const c = CUAD[cuad(p.x,p.y)][1];
      return `${p.prev?`<line x1="${X(p.prev[0])}" y1="${Y(p.prev[1])}" x2="${X(p.x)}" y2="${Y(p.y)}" stroke="${c}" stroke-width="2" opacity=".45"/>`:''}
      <circle cx="${X(p.x)}" cy="${Y(p.y)}" r="6" fill="${c}" opacity=".9"><title>${esc(p.t)} · ${esc(p.n)} · ${p.x>=0?'+':''}${fmt(p.x,1)}% vs SPY · momentum ${p.y>=0?'+':''}${fmt(p.y,1)}</title></circle>
      <text x="${X(p.x)+8}" y="${Y(p.y)+4}" class="et">${esc(p.t)}</text>`; }).join('')}
    <text x="${w-4}" y="${h/2-4}" text-anchor="end" class="ax">más fuerte que SPY →</text><text x="4" y="${h/2-4}" class="ax">← más débil</text>
    <text x="${w/2+4}" y="12" class="ax">acelera ↑</text><text x="${w/2+4}" y="${h-22}" class="ax">frena ↓</text></svg>`;
}
function rotacionHTML(){
  const R = D.meta.rotacion; if(!R || !(R.etfs||[]).length) return '';
  const n = R.etfs[0].x.length - 1, k = S.rotK ?? n;
  const ahora = rotPuntos(n), antes = Object.fromEntries(rotPuntos(n-1).map(p=>[p.t, cuad(p.x,p.y)]));
  const g = {lid:[],deb:[],rez:[],mej:[]}; ahora.forEach(p=>g[cuad(p.x,p.y)].push(p.t));
  const recien = ahora.filter(p=>cuad(p.x,p.y)==='lid' && antes[p.t] && antes[p.t]!=='lid').map(p=>p.t);
  const acel = ahora.slice().sort((a,b)=>b.y-a.y).slice(0,5);
  const lect = `Liderando: ${g.lid.length ? g.lid.join(', ') : 'ninguno'}. Mejorando: ${g.mej.length ? g.mej.join(', ') : 'ninguno'}. `
    + `Se debilitan: ${g.deb.length ? g.deb.join(', ') : 'ninguno'}. ${g.lid.length + g.mej.length > g.deb.length + g.rez.length ? 'Más ETFs ganando fuerza que perdiéndola.' : 'Más ETFs perdiendo fuerza que ganándola.'}`;
  return `<div class="grid g2r" style="margin-bottom:20px">${card('Cuadrantes de rotación', 'ETFs contra el SPY · fuerza relativa (X) y su momentum (Y), semanal',
      `<div id="rrg">${rotSvg(k)}</div>
       <div class="rrgc"><button class="chip" id="rplay">${S.rotPlay?'Pausa':'Play'}</button>
       <input type="range" id="rk" min="1" max="${n}" value="${k}" aria-label="Semana"><span class="mut" id="rkf">${esc((R.fechas||[])[k]||'')}</span></div>`)}
    ${card('Lectura de rotación', null, `<p style="margin:0 0 12px">${esc(lect)}</p>
      <h5>Recién a Líderes</h5><p class="mut" style="margin:0 0 12px">${recien.length ? recien.map(esc).join(', ') : 'Ninguno esta semana.'}</p>
      <h5>Aceleración inusual</h5><div class="kv">${acel.map(p=>`<span>${esc(p.t)} · ${esc(p.n)}</span><span class="${cls(p.y)}">${p.y>0?'+':''}${fmt(p.y,1)}</span>`).join('')}</div>`)}</div>`;
}
function vSectores(){
  const act = visibles(), tf = S.tf, g = {};
  act.forEach(a => (g[a.sector] = g[a.sector] || []).push(a));
  const secs0 = Object.entries(g).map(([s,l]) => ({s, l: l.slice().sort((x,y)=>y.calor-x.calor), prom: l.reduce((t,a)=>t+a.calor,0)/l.length}))
    .sort((a,b) => b.prom - a.prom);
  const secs = secs0;
  if(!secs.length) return `<p class="vacio">Ningún activo cumple los requisitos con estos filtros.</p>`;
  const franja = `<div class="franja">${secs.map(x => `<button class="sec-t" data-sec="${esc(x.s)}" aria-pressed="${(S.sector||(secs[0]&&secs[0].s))===x.s}" style="--h:${(x.prom/100).toFixed(2)}">
      <strong>${esc(x.s)}</strong><small>${x.l.length} activos · líder ${esc(x.l[0].t)}</small><em>calor ${fmt(x.prom,0)}</em></button>`).join('')}</div>`;
  if(!S.sector && secs.length) S.secAuto = secs[0].s;
  const cols = [
    {h:'', f:r=>`<span class="rk">${r.i+1}</span>`},
    {h:'Ticker', f:r=>tk(r.a)},
    TEND,
    {h:'3 meses', f:r=>spark(r.a.spark_d)},
    {h:'Calor', n:1, f:r=>fmt(r.a.calor,0)},
    {h:'Score', n:1, f:r=>fmt(r.a.score,0)},
    {h:'RS', n:1, f:r=>fmt(r.a.rs,0)},
    {h:'ADR', n:1, f:r=>adrC(r.a.adr)},
    VOLX,
    INSC,
    {h:'AVWAP', f:r=>{const m=mejorAv(r.a,tf); return m ? `${badge(m.estado)} <span class="mut">${esc(m.ancla)}</span>` : '<span class="mut">–</span>';}},
    {h:'1 mes', n:1, f:r=>`<span class="${cls(r.a.ret21)}">${pct(r.a.ret21,1)}</span>`},
  ];
  const lista = S.sector ? secs.filter(x=>x.s===S.sector) : secs.slice(0,1);
  return `${franja}<div class="grid gauto">${lista.map(x => card(esc(x.s), x.l.length+' en total', tabla(cols, x.l.slice(0,5).map((a,i)=>({a,i})), ''))).join('')}</div>`;
}

/* ---------- VCP ---------- */
const sinAv = a => a.sin_av ? '<span class="sin_av" title="No cumple el requisito de AVWAP: aparece solo por este setup">sin AVWAP</span>' : '';
const tcBadge = t => t ? `<span class="tc ${t.seco&&t.cerca?'ok':''}" title="${t.n} cierres semanales desde ${esc(t.desde)} en ${fmt(t.rango,2)}%${t.vol_x!=null?' · volumen '+fmt(t.vol_x,2)+'x':''}">${t.n} TC</span>` : '<span class="mut">–</span>';
const contrTxt = v => `<span class="contr">${(v.contr||[]).map(x=>`<b>${fmt(x,0)}%</b>`).join('<i>→</i>')}</span>`;
function graficoVcp(v){
  const s = v.serie||[]; if(s.length<2) return '';
  const W=420, H=150, pad=6;
  const mn = Math.min(...s, v.stop)*0.99, mx = Math.max(...s, v.pivot)*1.01, r = mx-mn||1;
  const X = f => (pad + f*(W-2*pad)).toFixed(1), Y = y => (H-pad-(y-mn)/r*(H-2*pad)).toFixed(1);
  const pts = s.map((y,i)=>`${X(i/(s.length-1))},${Y(y)}`).join(' ');
  const at = f => s[Math.min(s.length-1, Math.round(f*(s.length-1)))];
  const dots = (v.marcas||[]).map(([h,l])=>`<circle cx="${X(h)}" cy="${Y(at(h))}" r="3" fill="var(--muted)"/><circle cx="${X(l)}" cy="${Y(at(l))}" r="3" fill="var(--violet)"/>`).join('');
  return `<svg class="vcpg" viewBox="0 0 ${W} ${H}" role="img" aria-label="Base VCP con pivot y stop">
    <line x1="0" x2="${W}" y1="${Y(v.pivot)}" y2="${Y(v.pivot)}" stroke="var(--acc)" stroke-dasharray="4 4" stroke-width="1.2"/>
    <line x1="0" x2="${W}" y1="${Y(v.stop)}" y2="${Y(v.stop)}" stroke="var(--down)" stroke-dasharray="4 4" stroke-width="1.2"/>
    <polyline points="${pts}" fill="none" stroke="var(--text)" stroke-width="1.5" stroke-linejoin="round"/>${dots}
    <text x="${W-4}" y="${+Y(v.pivot)-5}" text-anchor="end" font-size="11" fill="var(--acc)">pivot ${pr(v.pivot)}</text>
    <text x="${W-4}" y="${+Y(v.stop)+14}" text-anchor="end" font-size="11" fill="var(--down)">stop ${pr(v.stop)}</text></svg>`;
}

/* ---------- Gatillos: todos los setups en una sola tabla ---------- */
const TIPOS_G = [['','Todos'],['vcp','VCP'],['avwap','AVWAP'],['comp','Compresión'],['inside','Inside'],['ep','Episodic'],['m30','30 min']];
// Orden: lo que ya disparó primero, después lo que está listo para disparar
const PRIO = {recien:0, rompio:0, disparado:0, rompe:0, armada:1, armado:1, preparada:1, 'por romper':1, ep0:1, confirmo:2, inside2:2, inside1:3, tc:3, comprimida:4, ep:4, esperando:5, formandose:5, sinvol:6, fallo:7};
const LISTOS = new Set(['recien','rompio','disparado','rompe','armada','armado','preparada','por romper','ep0']);
const esSelA = a => { const SL = P.sel || {rs:80, mv:7, score:70}; return !a.sin_av && a.rs>=SL.rs && a.mv>=SL.mv && a.score>=SL.score; };
const selB = a => esSelA(a) ? '<span class="selb" title="Seleccionada: RS, X/8 y score sobre el umbral">SEL</span>' : '';
function filasGatillos(tf){
  const out = [];
  const add = (a, tipo, nombre, est, badgeTxt, det, e, st, d) => out.push({a, tipo, nombre, est, badgeTxt, det, e, st, d,
    r: e && st && e>st ? (e-st)/e*100 : null});
  visibles(true).forEach(a => {
    // VCP y cierres apretados (solo diario)
    if(tf==='d' && a.vcp){ const v = a.vcp;
      add(a, 'vcp', 'VCP', v.estado, null, `${contrTxt(v)}${a.tc?' '+tcBadge(a.tc):''} <span class="mut">${fmt(v.semanas,0)} sem.${v.seco!=null?' · vol '+fmt(v.seco,2)+'x':''}${v.vol_rup!=null?' · ruptura '+fmt(v.vol_rup,1)+'x':''}</span>`, v.pivot, v.stop, v.dist); }
    else if(tf==='d' && a.tc){ const t = a.tc;
      add(a, 'vcp', 'Cierres apretados', 'tc', `${t.n} TC`, `<span class="mut">${t.n} cierres semanales en ${fmt(t.rango,1)}%${t.vol_x!=null?' · vol '+fmt(t.vol_x,2)+'x':''}</span>`, null, null, t.dist); }
    // AVWAP: rompiendo con volumen o por romper un ancla fuerte
    const s = !a.sin_av && a.setup_av && a.setup_av[tf];
    if(s){ const m = mejorAv(a, tf);
      add(a, 'avwap', 'AVWAP '+s.ancla.toLowerCase(), s.estado, null, `<span class="mut">${m && m.fuerte ? '★ ancla fuerte' : 'ancla'}${m && m.vol_x!=null ? ' · vol '+fmt(m.vol_x,1)+'x' : ''}${s.rr!=null ? ' · R:R '+fmt(s.rr,1) : ''}</span>`,
        s.entrada, s.stop, s.entrada ? (a.precio/s.entrada-1)*100 : null); }
    // Compresión
    const c = a.comp && a.comp[tf];
    if(c && (c.es || c.ruptura)){
      const est = c.ruptura ? 'rompio' : (c.dist_gatillo!=null && c.dist_gatillo<=P.cerca_gatillo ? 'preparada' : 'comprimida');
      add(a, 'comp', 'Compresión', est, est==='comprimida' ? 'Comprimida' : null,
        `${c.emas ? '<span class="up">EMAs ↑</span>' : '<span class="mut">EMAs sin subir</span>'} <span class="mut">· vol ${fmt(c.vol_r,2)} · rango ${fmt(c.rango,1)}%</span>`,
        c.gatillo, c.piso, c.dist_gatillo!=null ? -c.dist_gatillo : null); }
    // Inside day / week
    const i = a.inside && a.inside[tf];
    if(i && i.n>=1 && !a.sin_av){ const l = tf==='d' ? 'D' : 'W';
      add(a, 'inside', 'Inside '+(tf==='d'?'day':'week'), i.n>=2 ? 'inside2' : 'inside1', i.n>=2 ? (i.n>2?i.n:2)+'I'+l : 'I'+l,
        `<span class="mut">vela madre ${pr(i.madre_lo)} – ${pr(i.madre_hi)}</span>`, i.madre_hi, i.madre_lo, i.dist_hi!=null ? -i.dist_hi : null); }
    // Episodic pivot (diario)
    if(tf==='d' && a.ep && !a.sin_av){ const e = a.ep, x = (a.avwap.d||[]).find(z=>z.ancla==='Episodic pivot');
      add(a, 'ep', 'Episodic pivot', e.dias===0 ? 'ep0' : 'ep', e.dias===0 ? 'Hoy' : `Hace ${e.dias}d`,
        `<span class="up">${pct(e.suba,1)}</span> <span class="mut">· vol ${fmt(e.vol_x,1)}x · desde el EP ${pct(e.desde,1)}${x?' · AVWAP del EP '+pct(x.dist,1):''}</span>`, null, null, null); }
    // 30 Min Pivot (intradía, no depende de diario/semanal)
    const p = a.pivot30;
    if(p) add(a, 'm30', '30 Min Pivot', p.estado, null, `<span class="tk">EMA${p.ema_n}</span> <span class="mut">${esc(p.toque)}</span>`, p.entrada, p.stop, p.dist);
  });
  return out;
}
function vGatillos(){
  const tf = S.tf, todas = filasGatillos(tf);
  const pasa = r => (!S.gListos || LISTOS.has(r.est)) && (!S.gSel || esSelA(r.a)) && (!S.gEmas || (r.a.comp[tf] && r.a.comp[tf].emas))
    && (!S.rsiF || rsiOk(r.a)) && (!S.macdF || macdOk(r.a));
  const base = todas.filter(pasa);
  const l = base.filter(r => !S.gTipo || r.tipo===S.gTipo)
    .sort((x,y) => ((PRIO[x.est]??9)-(PRIO[y.est]??9)) || (y.a.score-x.a.score));
  const cnt = k => base.filter(r => !k || r.tipo===k).length;
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)+selB(r.a)+sinAv(r.a)},
    {h:'Setup', f:r=>`<b>${esc(r.nombre)}</b>`},
    {h:'Estado', f:r=>r.badgeTxt ? `<span class="est ${LISTOS.has(r.est)?'rompe':'otro'}">${esc(r.badgeTxt)}</span>` : badge(r.est)},
    {h:'Entrada', n:1, f:r=>pr(r.e)},
    {h:'Stop', n:1, f:r=>pr(r.st)},
    {h:'Riesgo', n:1, f:r=>r.r!=null ? `<span class="${r.r>P.foco_riesgo?'warn':''}">${fmt(r.r,1)}%</span>` : '–'},
    {h:'Precio vs. entrada', n:1, f:r=>r.d!=null ? `<span class="${cls(r.d)}">${pct(r.d)}</span>` : '–'},
    {h:'Score', n:1, f:r=>`<span class="scp">${fmt(r.a.score,0)}</span>`},
    {h:'Detalle', f:r=>r.det},
  ];
  const chip = (attr, k, txt, on, n) => `<button class="chip" ${attr}="${k}" aria-pressed="${on}">${txt}${n!=null?` <span class="mut">${n}</span>`:''}</button>`;
  return `<div class="subnav">${TIPOS_G.map(([k,n])=>chip('data-gt', k, n, (S.gTipo||'')===k, cnt(k))).join('')}</div>
    <div class="chips2">
      ${chip('data-gf','gListos','Solo listos', !!S.gListos)}
      ${chip('data-gf','gSel','Solo Seleccionadas', !!S.gSel)}
      ${chip('data-gf','gEmas','EMAs en ascenso', !!S.gEmas)}
      ${chip('data-gf','rsiF','RSI semanal cruzó al alza', !!S.rsiF)}
      ${chip('data-gf','macdF','MACD semanal alcista', !!S.macdF)}
    </div>
    ${card('Gatillos · '+TFN[tf], l.length, filasLista(l.map(r=>({a:r.a, extra:selB(r.a)+sinAv(r.a), setup:esc(r.nombre), est:cols[2].f(r), e:r.e, st:r.st, r:r.r, d:r.d, det:r.det})), S.gListos ? 'Nada listo para disparar con estos filtros. Probá sacando “Solo listos”.' : 'Ningún gatillo con estos filtros.'))}
    <details class="ayuda"><summary>Cómo leer cada setup</summary>
      <p><b>VCP</b> (diario): contracciones cada vez más chicas, de la más vieja a la más nueva. Armada = última de ${fmt(P.vcp_ult,0)}% o menos, volumen seco y precio a ${fmt(P.vcp_dist,0)}% o menos del pivot. Recién rompió = cerró sobre el pivot con volumen de ${fmt(P.vol_ruptura,1)}x en las últimas ${P.vcp_dias} ruedas. TC = ${P.tc_min}+ cierres semanales seguidos dentro de ${fmt(P.tc_rango,1)}%.</p>
      <p><b>AVWAP</b>: rompiendo = cerró arriba con volumen de ${fmt(P.vol_ruptura,1)}x o más; por romper = hasta ${tf==='d'?P.dist_d:P.dist_w}% debajo de un ancla fuerte ★. Stop en el mínimo ${tf==='d'?'del día':'de la semana'}.</p>
      <p><b>Compresión</b>: ATR y ancho de Bollinger bajos con volumen secándose. Preparada = a ${P.cerca_gatillo}% o menos del gatillo (máximo reciente); stop en el piso del rango. Vos las operás con EMAs en ascenso: usá ese filtro.</p>
      <p><b>Inside</b>: vela dentro de la anterior; gatillo en el máximo de la vela madre y stop en su mínimo.</p>
      <p><b>Episodic pivot</b>: suba de ${fmt(P.ep_suba,0)}%+ con volumen ${fmt(P.ep_vol,1)}x en las últimas 10 ruedas. No siempre es para entrar ya: suele convenir esperar una consolidación.</p>
      <p><b>30 Min Pivot</b> (intradía): tocó una EMA diaria (${P.emas_30m.join(', ')}) y en 30 min la primera vela verde marca entrada (su máximo) y stop (su mínimo). Armado = no superó el máximo; disparado = lo superó en las últimas 3 horas.${D.meta.con30m ? '' : ' El intradía estaba desactivado en esta corrida.'}</p>
      <p><b>SEL</b> = Seleccionada (RS ${(P.sel||{}).rs||80}+, ${(P.sel||{}).mv||7}/8+, score ${(P.sel||{}).score||70}+). <b>Solo listos</b> deja lo que ya disparó o está a punto.</p>
    </details>`;
}

/* ---------- Ficha ---------- */
const MV = ['Precio sobre EMA150 y EMA200','EMA150 sobre EMA200','EMA200 subiendo (22 velas)','EMA50 sobre EMA150 y EMA200','Precio sobre EMA50',
  `${P.sobre_min}% o más sobre el mínimo de 252 velas (${P.sobre_min_etf}% en ETFs)`, `Dentro del ${P.bajo_max}% del máximo de 252 velas`, 'Línea de RS vs SPY sobre su media de 50'];
const MES = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'];
const mesAnio = f => MES[+f.slice(5,7)-1] + ' ' + f.slice(2,4);
const crecC = v => v==null ? 'mut' : v>=P.fuerte ? 'up' : v>0 ? 'warn' : 'down';
function bloqueFund(a){
  const F = a.fund;
  if(a.tipo!=='accion') return '';
  if(!F) return `<h4>Análisis fundamental</h4><p class="vacio">s/d</p>`;
  const caja = (t, v, sub, c) => `<div class="fbox ${c||''}"><span>${t}</span><b>${v}</b>${sub?`<small>${sub}</small>`:''}</div>`;
  const ant = v => v!=null ? 'antes '+pct(v,0) : '';
  const tr = F.trim || [];
  const mx = Math.max(...tr.flatMap(x=>[Math.abs(x.eps), Math.abs(x.ant||0)]), 0.0001);
  const g = x => x.ant>0 ? (x.eps/x.ant-1)*100 : null;
  const barras = tr.length ? `<div class="ebars">${tr.map(x=>{ const v=g(x); return `<div class="eq">
      <em class="${crecC(v)}">${v!=null?pct(v,0):'s/d'}</em>
      <div class="par"><i class="vie" style="height:${Math.max(2,Math.abs(x.ant||0)/mx*70)}px"></i><i class="nue ${crecC(v)}" style="height:${Math.max(2,Math.abs(x.eps)/mx*70)}px"></i></div>
      <span>${x.supero?'<b class="dot"></b>':''}${mesAnio(x.f)}</span></div>`; }).join('')}</div>
    <p class="nota" style="margin:6px 0 0">Barra gris: mismo trimestre del año anterior. <b class="dot"></b> superó lo estimado por los analistas.</p>` : '';
  const an = F.anual || [];
  let cagr = null;
  if(an.length>=2 && an[0][1]>0 && an[an.length-1][1]>0) cagr = (Math.pow(an[an.length-1][1]/an[0][1], 1/(an.length-1))-1)*100;
  const anual = an.length ? `<div class="kv" style="margin-top:10px"><span>EPS anual${F.moneda&&F.moneda!=='USD'?' ('+esc(F.moneda)+')':''}</span><span>${an.map(([y,v])=>`${y}: ${fmt(v,2)}`).join(' · ')}</span>
      <span>Crecimiento compuesto</span><span class="${crecC(cagr)}">${cagr!=null?pct(cagr,0)+' por año':'s/d'} <span class="mut">· CAN SLIM pide ${P.fuerte}%</span></span></div>` : '';
  const pf = (F.pts_eps||0)+(F.pts_ventas||0);
  return `<h4>Análisis fundamental · ${P.pts.fund > 0 ? fmt(pf,1)+'/'+P.pts.fund+' pts' : (pf>=5 ? 'CAN SLIM ✓' : 'informativo, no suma al score')}</h4>
    <div class="fgrid">${caja('Crecim. EPS (trim.)', F.eps_g!=null?pct(F.eps_g,0):'s/d', ant(F.eps_g_ant), crecC(F.eps_g))}
      ${caja('Crecim. ventas (trim.)', F.ventas_g!=null?pct(F.ventas_g,0):'s/d', ant(F.ventas_g_ant), crecC(F.ventas_g))}
      ${caja('P/E', F.pe!=null?fmt(F.pe,1)+'x':'s/d')}${caja('% institucional', F.inst!=null?fmt(F.inst,0)+'%':'s/d')}</div>
    ${barras}${anual}`;
}
function rsLinea(v){
  const w = 420, h = 70, pts = v.map((x,i)=>x==null?null:[i/(v.length-1)*w, h - x/100*h]).filter(Boolean);
  const ult = v[v.length-1], ant = v.length>4 ? v[v.length-5] : null, col = ult>=80?'var(--up)':ult>=50?'var(--warn)':'var(--down)';
  return `<svg viewBox="0 0 ${w} ${h+16}" width="100%" aria-hidden="true"><line x1="0" y1="${h-0.8*h}" x2="${w}" y2="${h-0.8*h}" stroke="var(--line2)" stroke-dasharray="3 4"/>
    <polyline points="${pts.map(p=>p.map(x=>x.toFixed(1)).join(',')).join(' ')}" fill="none" stroke="${col}" stroke-width="2"/>
    <text x="0" y="${h+13}" class="ax">línea punteada = RS 80</text><text x="${w}" y="${h+13}" text-anchor="end" class="ax">hoy ${fmt(ult,0)}${ant!=null?' · hace un mes '+fmt(ant,0):''}</text></svg>`;
}
function ficha(t){
  const a = D.activos.find(x=>x.t===t); if(!a) return;
  const PT = pilares(a);
  const tvSym = a.tipo==='cripto' ? a.t.replace('-','') : a.t.replace('-','.');
  const avt = tf => (a.avwap[tf]||[]).length ? `<div class="tw"><table><thead><tr><th>Ancla</th><th class="n">AVWAP</th><th class="n">Dist.</th><th class="n">Vol.</th><th>Estado</th></tr></thead><tbody>${
      a.avwap[tf].map(x=>`<tr><td>${esc(x.ancla)}${x.fuerte?'<span class="fuerte">★</span>':''} <span class="mut">${esc(x.fecha)}</span></td><td class="n">${pr(x.valor)}</td><td class="n ${cls(x.dist)}">${pct(x.dist)}</td><td class="n">${x.vol_x!=null?fmt(x.vol_x,1)+'x':'–'}</td><td>${badge(x.estado)}${(x.estado==='rompe'||x.estado==='por romper')&&!x.cuenta?' <span class="mut" title="No cuenta: rompió sin volumen o ancla débil">no cuenta</span>':''}</td></tr>`).join('')}</tbody></table></div>` : '<p class="vacio">Sin anclas.</p>';
  const cmp = tf => a.comp[tf] ? `<span>Compresión ${TFN[tf]}</span><span>${fmt(a.comp[tf].score,0)}${a.comp[tf].es?' · comprimida':''}</span>` : '';
  const ins = tf => `<span>Inside ${tf==='d'?'day':'week'}</span><span>${a.inside[tf] && a.inside[tf].n ? a.inside[tf].n : 'no'}</span>`;
  $('#ficha').innerHTML = `
    <div class="fh"><div><h2>${esc(a.t)}<span class="rkg">#${D.activos.indexOf(a)+1} de ${D.activos.length}</span></h2><p>${esc(a.nombre)} · ${esc(a.sector)}${a.industria?' · '+esc(a.industria):''}</p></div><button class="cerrar" id="cerrar" aria-label="Cerrar ficha">✕</button></div>
    <div class="precio">${pr(a.precio)} <span class="${cls(a.chg)}">${pct(a.chg)}</span></div>
    <div style="margin-top:12px">${spark(a.spark_d, 420, 72)}</div>
    ${a.sin_av ? `<p class="nota" style="margin-top:12px">No está rompiendo ni por romper ninguna AVWAP: cumple Minervini, precio y ADR, y aparece solo en Gatillos (VCP, compresión o 30 min).</p>` : ''}
    ${(a.flags||[]).length ? `<h4>Avisos</h4><div class="flist">${a.flags.map(f=>`<div class="${f.tipo}">${esc(f.t)}</div>`).join('')}</div>` : ''}
    <h4>Score</h4>
    <div style="display:flex;gap:18px;align-items:center">${ring(a.score, 84)}
      <div class="partes" style="flex:1">${PT.map(([n,k,m,c])=>`<span class="mut">${n}</span><span class="pbar"><i style="width:${(a.partes[k]||0)/m*100}%;background:${c}"></i></span><span>${fmt(a.partes[k]||0,1)}/${m}</span>`).join('')}</div></div>
    ${a.castigo>0 ? `<p class="nota" style="margin-top:8px">Descuento de ${fmt(a.castigo,0)} puntos por banderas (estirada, extendido, sin volumen o rechazo).</p>` : ''}
    <h4>Gates Stage 2</h4>
    <div class="gate"><span><b class="${a.mv_checks[0]&&(a.pend||[])[4]>0?'up':'down'}">${a.mv_checks[0]&&(a.pend||[])[4]>0?'✓':'✗'}</b> Precio sobre la EMA200 con pendiente positiva</span><span class="${cls(a.d200)}">${pct(a.d200,1)}</span></div>
    ${a.sem ? `<div class="kv" style="margin-top:6px"><span>RSI semanal / su SMA14</span><span>${fmt(a.sem.rsi,0)} / ${fmt(a.sem.rsi_sma,0)}${a.sem.rsi_hace!=null?' · cruzó '+(a.sem.rsi_dir==='arriba'?'al alza ':'a la baja ')+hace(a.sem.rsi_hace):''}</span>
      <span>MACD semanal</span><span>${a.sem.macd_hace!=null?'cruce '+(a.sem.macd_dir==='arriba'?'alcista':'bajista')+' '+hace(a.sem.macd_hace)+' · ':''}${a.sem.macd_cero}</span></div>` : ''}
    <h4>Tendencia · ${xo8(a)}</h4>
    <div class="tv">${EMAS_N.map((n,i)=>`<div><span>${n}</span>${flecha((a.pend||[])[i],n)}</div>`).join('')}<div><span>M1D</span>${flecha(a.m1d,'Momentum diario')}</div><div><span>M1W</span>${flecha(a.m1w,'Momentum semanal')}</div><div><span>ADR%</span><b>${adrC(a.adr)}</b></div></div>
    <div class="tv">${a.mv_checks.map((ok,i)=>`<div><span>${i+1}</span><b class="${ok?'ok':'no'}" title="${esc(MV[i])}">${ok?'✓':'✗'}</b></div>`).join('')}</div>
    <div class="kv" style="margin-top:12px">
      ${a.tipo==='accion' ? `<span>Market cap</span><span>${big(a.mcap)}</span>` : ''}
      <span>Desde el máx. de 52 semanas</span><span class="${cls(a.off_hi)}">${pct(a.off_hi,1)}</span>
      <span>Vol. prom. 50 ruedas</span><span>${a.dvol50!=null?'USD '+big(a.dvol50)+' · ':''}${big(a.vol50)} acciones</span>
      <span>Volumen hoy</span><span>${big(a.vol_hoy)} · ${volx(a)} vs prom. 50</span>
      <span>Up/Down volume 50 días</span><span class="${a.ud50>=1?'up':'down'}">${a.ud50!=null?fmt(a.ud50,2):'s/d'}${a.ud50!=null?(a.ud50>=1?' · acumulación':' · distribución'):''}</span>
      <span>RS Rating</span><span>${fmt(a.rs,0)}</span>
      ${a.etf ? `<span>ETF del sector</span><span>${esc(a.etf.t)}${a.etf.rs!=null?' · RS '+fmt(a.etf.rs,0):''} · <span class="${cls(a.etf.chg)}">${pct(a.etf.chg)}</span></span>
        <span>Vs. ${esc(a.etf.t)} a 1 / 3 meses</span><span><span class="${cls(a.etf.vs1m)}">${pct(a.etf.vs1m,1)}</span> / <span class="${cls(a.etf.vs3m)}">${pct(a.etf.vs3m,1)}</span></span>` : ''}
    </div>
    ${(a.rs16||[]).filter(x=>x!=null).length > 2 ? `<h4>RS · últimas ${a.rs16.length-1} semanas</h4>${rsLinea(a.rs16)}` : ''}
    <h4>Criterios de Minervini · ${a.mv}/8</h4>
    <ul class="checks">${MV.map((l,i)=>`<li><b class="${a.mv_checks[i]?'up':'down'}">${a.mv_checks[i]?'✓':'✗'}</b>${l}</li>`).join('')}</ul>
    ${bloqueFund(a)}
    <h4>Rango de 52 semanas · ${fmt(a.pos52,0)}%</h4>
    <div class="rango"><i style="left:${Math.max(0,Math.min(100,a.pos52))}%"></i></div>
    <div class="rl"><span>${pr(a.lo52)}</span><span>${pr(a.hi52)}</span></div>
    ${a.tc ? `<h4>Cierres semanales apretados · ${tcBadge(a.tc)}</h4><div class="kv"><span>Desde</span><span>${esc(a.tc.desde)} · rango ${fmt(a.tc.rango,2)}%</span>
      <span>Volumen de esas semanas</span><span class="${a.tc.seco?'up':''}">${a.tc.vol_x!=null?fmt(a.tc.vol_x,2)+'x las 10 previas':'s/d'}</span>
      <span>Precio vs. ${a.vcp?'pivot':'máx. 10 semanas'}</span><span class="${cls(a.tc.dist)}">${pct(a.tc.dist,1)}</span></div>` : ''}
    ${a.vcp ? `<h4>Base VCP · ${badge(a.vcp.estado)}</h4>${graficoVcp(a.vcp)}
      <div class="kv" style="margin-top:10px"><span>Contracciones</span><span>${contrTxt(a.vcp)}</span>
      <span>Base</span><span>${fmt(a.vcp.semanas,0)} semanas desde ${esc(a.vcp.inicio)}</span>
      <span>Pivot / stop</span><span>${pr(a.vcp.pivot)} / ${pr(a.vcp.stop)} · riesgo ${fmt(a.vcp.riesgo,1)}%</span>
      <span>Volumen en la última</span><span>${a.vcp.seco!=null?fmt(a.vcp.seco,2)+'x el promedio':'–'}</span>
      ${a.vcp.vol_rup!=null?`<span>Volumen de ruptura</span><span>${fmt(a.vcp.vol_rup,1)}x · hace ${a.vcp.dias_rup} ruedas</span>`:''}</div>` : ''}
    <h4>AVWAP diario</h4>${avt('d')}
    <h4>AVWAP semanal</h4>${avt('w')}
    <h4>Estructura</h4>
    <div class="kv">
      ${a.estadio ? `<span>Estadio</span><span>${esc(ESTADIOS[a.estadio])}</span>` : ''}
      ${cmp('d')}${cmp('w')}${ins('d')}${ins('w')}
      ${a.ep ? `<span>Episodic pivot</span><span>${a.ep.dias===0?'hoy':'hace '+a.ep.dias+' ruedas'} · ${pct(a.ep.suba,1)} · ${fmt(a.ep.vol_x,1)}x</span>` : ''}
      <span>Distancia a EMA10 / EMA20</span><span class="${a.adr>0 && (a.d10/a.adr>P.est10 || a.d20/a.adr>P.est20) ? 'down' : ''}">${pct(a.d10,1)} / ${pct(a.d20,1)} · ${a.adr>0?fmt(a.d10/a.adr,1)+' / '+fmt(a.d20/a.adr,1)+' ADR':''}</span>
      <span>Retorno 1 mes</span><span class="${cls(a.ret21)}">${pct(a.ret21,1)}</span>
      ${a.earn_prox ? `<span>Próximos earnings</span><span>${esc(a.earn_prox)}${a.earn_momento?' · '+esc(a.earn_momento):''}</span>` : ''}
    </div>
    <a class="enlace" href="https://www.tradingview.com/chart/?symbol=${encodeURIComponent(tvSym)}" target="_blank" rel="noopener">Abrir en TradingView</a>`;
  $('#ficha').classList.add('open'); $('#velo').classList.add('open'); $('#ficha').setAttribute('aria-hidden','false');
  $('#cerrar').focus();
}
function cerrarFicha(){ $('#ficha').classList.remove('open'); $('#velo').classList.remove('open'); $('#ficha').setAttribute('aria-hidden','true'); }

/* ---------- Navegación y eventos ---------- */
const CORTO = {};
const VISTAS = {inicio:vInicio, gatillos:vGatillos, ranking:vRanking, mercado:vMercado};
const LOGO_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>';
$('#rail').innerHTML = `<div class="logo">${D.meta.avatar ? `<img src="${esc(D.meta.avatar)}" alt="" referrerpolicy="no-referrer" onerror="this.parentNode.innerHTML=LOGO_SVG">` : LOGO_SVG}</div>` +
  PAGS.map(([k,n])=>`<button data-pag="${k}" aria-current="${S.pag===k?'page':'false'}">${ico(k)}<span class="lg">${n}</span><span class="ct">${CORTO[k]||n}</span></button>`).join('');
function ir(p){
  S.pag = p; document.querySelectorAll('#rail button').forEach(b=>b.setAttribute('aria-current', b.dataset.pag===p ? 'page' : 'false'));
  render(); window.scrollTo(0,0);
}
function render(){
  const pg = PAGS.find(x=>x[0]===S.pag);
  $('#titulo').textContent = pg[0]==='inicio' ? (D.meta.nombre || 'Radar') : pg[1];
  $('#sub').textContent = pg[2];
  $('#lema').innerHTML = '';
  $('#tf').style.display = S.pag==='gatillos' ? '' : 'none';
  $('#vista').innerHTML = VISTAS[S.pag]();
}
function seg(id, key){
  document.querySelectorAll(`#${id} button`).forEach(b => b.addEventListener('click', () => {
    S[key] = b.dataset.v; document.querySelectorAll(`#${id} button`).forEach(x=>x.setAttribute('aria-pressed', x===b)); render();
  }));
}
seg('tf','tf'); seg('tipo','tipo');
$('#rail').addEventListener('click', e => { const b = e.target.closest('[data-pag]'); if(b) ir(b.dataset.pag); });
$('#q').addEventListener('input', e => { S.q = e.target.value; render(); });
$('#tvexp').addEventListener('click', exportarTV);
$('#grandes').addEventListener('click', e => { S.grandes = !S.grandes; e.currentTarget.setAttribute('aria-pressed', S.grandes); render(); });
$('#vista').addEventListener('click', e => {
  const k = e.target.closest('[data-ir]'); if(k){ ir(k.dataset.ir); return; }
  const gt = e.target.closest('[data-gt]'); if(gt){ S.gTipo = gt.dataset.gt; render(); return; }
  if(e.target.closest('[data-trackmas]')){ S.trackMas = !S.trackMas; render(); return; }
  const gf = e.target.closest('[data-gf]'); if(gf){ S[gf.dataset.gf] = !S[gf.dataset.gf]; render(); return; }
  const em2 = e.target.closest('[data-evmas]'); if(em2){ S.evMas = S.evMas || {}; S.evMas[em2.dataset.evmas] = !S.evMas[em2.dataset.evmas]; render(); return; }
  const cg = e.target.closest('[data-cartg]'); if(cg){ S.cartG = cg.dataset.cartg==='1'; render(); return; }
  const sec = e.target.closest('.sec-t'); if(sec){ S.sector = S.sector===sec.dataset.sec ? null : sec.dataset.sec; render(); return; }
  if(e.target.closest('#rplay')){
    S.rotPlay = !S.rotPlay; e.target.closest('#rplay').textContent = S.rotPlay ? 'Pausa' : 'Play';
    clearInterval(S.rotTimer);
    if(S.rotPlay){ const n = D.meta.rotacion.etfs[0].x.length - 1; if((S.rotK ?? n) >= n) S.rotK = 1;
      S.rotTimer = setInterval(()=>{ const n2 = D.meta.rotacion.etfs[0].x.length - 1; S.rotK = Math.min(n2, (S.rotK ?? n2) + 1); pintarRot(); if(S.rotK>=n2){ S.rotPlay=false; clearInterval(S.rotTimer); const b=$('#rplay'); if(b) b.textContent='Play'; } }, 700); }
    return;
  }
  const tr = e.target.closest('[data-t]'); if(tr) ficha(tr.dataset.t);
});
function pintarRot(){ const r = $('#rrg'); if(!r) return; const k = S.rotK; r.innerHTML = rotSvg(k); const i = $('#rk'); if(i) i.value = k; const f = $('#rkf'); if(f) f.textContent = (D.meta.rotacion.fechas||[])[k]||''; }
$('#vista').addEventListener('input', e => { if(e.target.id==='rk'){ S.rotK = +e.target.value; pintarRot(); } });
$('#vista').addEventListener('keydown', e => { const tr = e.target.closest('[data-t]'); if(tr && (e.key==='Enter'||e.key===' ')){ e.preventDefault(); ficha(tr.dataset.t); } });
$('#ficha').addEventListener('click', e => { if(e.target.closest('#cerrar')) cerrarFicha(); });
$('#velo').addEventListener('click', cerrarFicha);
document.addEventListener('keydown', e => { if(e.key==='Escape') cerrarFicha(); });

const m = D.meta;
$('#meta').innerHTML = `<span>Actualizado ${esc(m.generado)}</span>${m.demo ? '<span class="demo">· datos simulados</span>' : ''}<button class="refr" id="refr" aria-label="Actualizar"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a9 9 0 1 1-2.6-6.4"/><path d="M21 4v5h-5"/></svg>Actualizar</button>`;

/* ---------- Recarga y aviso de datos viejos ---------- */
// "dd-mm-aaaa hh:mm" en hora de Argentina (UTC-3) -> fecha real
function fechaAR(t){ const x = /(\d+)-(\d+)-(\d+) (\d+):(\d+)/.exec(t||''); return x ? new Date(Date.UTC(+x[3], x[2]-1, +x[1], +x[4]+3, +x[5])) : null; }
function recargar(){ $('#refr').classList.add('gira'); location.replace(location.pathname + '?v=' + Date.now()); }
async function hayNueva(){
  try{
    const r = await fetch(location.pathname + '?v=' + Date.now(), {cache:'no-store'});
    const x = /"generado":\s*"([^"]+)"/.exec(await r.text());
    const nueva = x && fechaAR(x[1]), actual = fechaAR(m.generado);
    return !!(nueva && actual && nueva > actual);
  }catch(e){ return false; }
}
async function chequear(){ if(!m.demo && await hayNueva()) recargar(); }
function avisoViejo(){
  const g = fechaAR(m.generado); if(!g || m.demo) return;
  const ar = new Date(Date.now() - 3*3600e3), dia = ar.getUTCDay(), mins = ar.getUTCHours()*60 + ar.getUTCMinutes();
  const horas = (Date.now() - g) / 3600e3;
  const enRueda = dia>=1 && dia<=5 && mins>=12*60+30 && mins<=20*60;
  const el = $('#viejo');
  if(enRueda && horas > 2){
    el.innerHTML = `<b>Datos de hace ${horas<24 ? Math.floor(horas)+' horas' : Math.floor(horas/24)+' días'}.</b> En horario de mercado debería actualizarse cada hora: tocá Actualizar y, si sigue igual, revisá la pestaña Actions en GitHub por si falló una corrida.`;
    el.classList.add('on');
  } else el.classList.remove('on');
}
$('#refr').addEventListener('click', recargar);
avisoViejo();
setTimeout(chequear, 1500);
let ultimo = Date.now();
document.addEventListener('visibilitychange', () => {
  if(document.visibilityState !== 'visible') return;
  avisoViejo();
  if(Date.now() - ultimo > 60e3){ ultimo = Date.now(); chequear(); }
});
window.addEventListener('pageshow', e => { if(e.persisted){ avisoViejo(); chequear(); } });
setInterval(() => { if(document.visibilityState==='visible'){ avisoViejo(); chequear(); } }, 5*60e3);
$('#pie').innerHTML = `${m.n_universo} activos analizados. Requisitos: al menos ${P.min_mv} de 8 criterios de Minervini como en el indicador de TradingView (EMAs, ${P.sobre_min}% sobre el mínimo y dentro del ${P.bajo_max}% del máximo de 252 velas, línea de RS vs SPY sobre su media de 50), precio de ${P.precio_min} USD o más en acciones y ETF, ADR de ${fmt(P.adr_min,1)}% o más${P.exigir_rs ? `, RS Rating de ${P.rs_min} o más` : ''}${P.exigir_av ? ', y una AVWAP rota con volumen o por romper en un ancla fuerte. Los setups de Gatillos (VCP, compresión y 30 min) no exigen AVWAP' : ''}. Horarios en hora de Argentina. Esto es un filtro técnico, no una recomendación de compra.`;
render();
</script>
</body>
</html>
'''


# Semilla del historial (Top del score y Seleccionadas, 21-09 al 16-10-2026) para que el track record arranque con datos.
# Si existe la carpeta semillas/ en el repo, se usa esa.
SEMILLAS = {"historial_top.json": "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", "historial_sel.json": "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"}


if __name__ == "__main__":
    import os
    html, datos = correr()
    os.makedirs("site", exist_ok=True)
    with open("site/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    # Para instalarlo en el celular como app ("Agregar a pantalla de inicio")
    json.dump({"name": NOMBRE_DASHBOARD, "short_name": NOMBRE_DASHBOARD[:12], "start_url": "./", "display": "standalone",
               "background_color": "#050607", "theme_color": "#050607",
               "icons": [{"src": AVATAR_URL, "sizes": "400x400", "type": "image/jpeg", "purpose": "any"}] if AVATAR_URL else []},
              open("site/manifest.webmanifest", "w", encoding="utf-8"), ensure_ascii=False)
    print("Dashboard escrito en site/index.html")
