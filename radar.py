# ⚙️ CONFIGURACIÓN — cambiá los valores y guardá (commit). La próxima corrida los usa.
# **Requisitos**
PRECIO_MINIMO = 10
ADR_MINIMO = 2.0
ADR_PERIODO = 20
MIN_CRITERIOS_MINERVINI = 7
EXIGIR_RS = True
PCT_SOBRE_MINIMO_52S = 30
PCT_DEBAJO_MAXIMO_52S = 30
RS_MINIMO = 70
EXIGIR_AVWAP = True
ANCLAS_FUERTES = "Earnings, Episodic pivot, Máx. estructural, Máx. histórico"
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
# **Lista de foco y score**
FOCO_MAXIMO = 10
FOCO_RS_MINIMO = 80
FOCO_RIESGO_MAX = 8.0
SCORE_CASTIGO_BANDERA = 5
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
# **Episodic pivots y banderas**
EP_MIN_SUBA = 4.0
EP_MIN_VOL = 2.0
EXTENDIDO_SMA50 = 25
ESTIRADA_EMA10_ADR = 2.0
ESTIRADA_EMA20_ADR = 3.0
# **Universo**
INCLUIR_SP500 = True
INCLUIR_NASDAQ100 = True
INCLUIR_MIDCAP400 = True
INCLUIR_ETFS = True
INCLUIR_CRIPTO = True
TICKERS_EXTRA = "NBIS, CLS, HOOD"


# ---- Motor del radar (no hace falta tocar nada de acá para abajo) ----
import warnings, json, math, time, io, datetime as dt
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
                    filas.append((s, str(r[nom]) if nom else s, SECTORES_ES.get(str(r[sec]).strip(), str(r[sec]).strip()), "accion"))
            return filas
    return []

def obtener_universo():
    filas = []
    fuentes = []
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
        filas += [(t, t, "Sin clasificar", "accion") for t in RESPALDO]
    extra = [t.strip().upper() for t in str(TICKERS_EXTRA).replace(";", ",").split(",") if t.strip()]
    filas += [(t, t, "Tu lista", "accion") for t in extra]
    if INCLUIR_ETFS: filas += [(t, n, "ETF", "etf") for t, n in ETFS.items()]
    if INCLUIR_CRIPTO: filas += [(t, n, "Cripto", "cripto") for t, n in CRIPTO.items()]
    u = pd.DataFrame(filas, columns=["ticker", "nombre", "sector", "tipo"]).drop_duplicates("ticker", keep="first")
    return u.reset_index(drop=True)

# ---------------------------------------------------------------- datos
def descargar(tickers, period, interval, chunk=80):
    datos = {}
    tickers = list(dict.fromkeys(tickers))
    for i in range(0, len(tickers), chunk):
        grupo = tickers[i:i + chunk]
        try:
            df = yf.download(grupo, period=period, interval=interval, group_by="ticker",
                             auto_adjust=True, threads=True, progress=False)
        except Exception as e:
            print("  ⚠️", e); continue
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
        print(f"  {min(i + chunk, len(tickers))}/{len(tickers)}")
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

def minervini(df, rs):
    c = df.Close; p = c.iloc[-1]
    s50, s150, s200 = sma(c, 50), sma(c, 150), sma(c, 200)
    ult = df[df.index >= df.index[-1] - pd.Timedelta(days=365)]
    hi, lo = ult.High.max(), ult.Low.min()
    g = lambda s, i=-1: s.iloc[i] if len(s) >= abs(i) else np.nan
    checks = [
        p > g(s150) and p > g(s200),
        g(s150) > g(s200),
        g(s200) > g(s200, -22),
        g(s50) > g(s150) and g(s50) > g(s200),
        p > g(s50),
        p >= lo * (1 + PCT_SOBRE_MINIMO_52S / 100),
        p >= hi * (1 - PCT_DEBAJO_MAXIMO_52S / 100),
        rs >= RS_MINIMO,
    ]
    return [bool(x) for x in checks], hi, lo

def pasa_minervini(checks):
    return sum(checks) >= MIN_CRITERIOS_MINERVINI and (checks[7] or not EXIGIR_RS)

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
        c = df.Close; p = c.iloc[-1]; e50, e200 = ema(c, 50), ema(c, 200)
        s_t = 4 * (p > e50.iloc[-1]) + 4 * (p > e200.iloc[-1]) + 2 * (e50.iloc[-1] > e200.iloc[-1] and e200.iloc[-1] > e200.iloc[-21])
        ch, vv = c.pct_change(), df.Volume
        dd = int(((ch <= -0.002) & (vv > vv.shift(1))).iloc[-25:].sum())
        s_d = max(0, 8 - 2 * max(0, dd - 3))
        ext = (p - e50.iloc[-1]) / atr(df, 14).iloc[-1]
        s_e = 7 if 0 <= ext <= 3 else 4 if 0 < ext <= 5 else 1 if ext > 5 else 3
        pts += s_t + s_d + s_e; mx += 25
        det.append(f"{t}: tendencia {int(s_t)}/10, {dd} días de distribución en 25 ruedas, {ext:+.1f} ATR de la EMA50")
    if mx: capas.append({"nombre": "Índices SPY y QQQ", "pts": num(pts, 1), "max": mx, "det": det})
    acc = [d for d in acciones if len(d) >= 220]
    if len(acc) >= 50:
        pe200 = np.mean([d.Close.iloc[-1] > ema(d.Close, 200).iloc[-1] for d in acc])
        ps200 = np.mean([d.Close.iloc[-1] > d.Close.iloc[-200:].mean() for d in acc])
        p50 = np.mean([d.Close.iloc[-1] > ema(d.Close, 50).iloc[-1] for d in acc])
        p200 = (pe200 + ps200) / 2
        nh = sum(d.High.iloc[-1] >= d.High.iloc[-253:-1].max() for d in acc)
        nl = sum(d.Low.iloc[-1] <= d.Low.iloc[-253:-1].min() for d in acc)
        s1 = float(np.clip((p200 - 0.3) / 0.4, 0, 1) * 10)
        s2 = float(np.clip((p50 - 0.3) / 0.4, 0, 1) * 10)
        s3 = nh / (nh + nl) * 10 if nh + nl else 5.0
        capas.append({"nombre": "Amplitud del universo", "pts": num(s1 + s2 + s3, 1), "max": 30,
                      "det": [f"{pe200:.0%} de las acciones sobre la EMA200 y {ps200:.0%} sobre la SMA200", f"{p50:.0%} sobre la EMA50",
                              f"{nh} nuevos máximos de 52 semanas contra {nl} nuevos mínimos"]})
    if vix is not None and len(vix):
        v = float(vix.Close.iloc[-1])
        s = 20 if 13 <= v <= 20 else 14 if v < 13 else 12 if v <= 25 else 6 if v <= 30 else 4
        lect = "zona sana" if 13 <= v <= 20 else "complacencia" if v < 13 else "tensión" if v <= 30 else "pánico"
        capas.append({"nombre": "Sentimiento (VIX)", "pts": s, "max": 20, "det": [f"VIX en {v:.1f}: {lect}"]})
    if not capas: return None
    total = sum(c["pts"] for c in capas) / sum(c["max"] for c in capas) * 100
    if total < 40: et, rec = "Defensivo", "Priorizá liquidez; solo seguimiento."
    elif total < 60: et, rec = "Cauteloso", "Posiciones chicas y solo los mejores setups."
    elif total < 80: et, rec = "Favorable", "Mercado acompaña: setups A+ con tamaño normal."
    else: et, rec = "Expansión", "Viento a favor: exposición plena en los líderes."
    return {"score": num(total, 0), "etiqueta": et, "rec": rec, "capas": capas}

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
    return x.replace("maximo", "max").replace(".", "").replace(" ", "")

def anclas_fuertes():
    """Nombres de ancla (como los arma el motor) que figuran en ANCLAS_FUERTES, sin importar tildes ni puntos."""
    pedidas = {_norm(x) for x in str(ANCLAS_FUERTES).split(",") if x.strip()}
    return {n for n in ("Earnings", "Episodic pivot", "Alto volumen", "Máx. estructural", "Máx. histórico", "IPO")
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
    # ruptura: primer cierre sobre el pivot después del mínimo de la última contracción
    b = next((x for x in range(ult["lo_i"] + 1, m)
              if cl[x] > pivot and vol50[x - 1] and vo[x] >= VOL_RUPTURA * vol50[x - 1]), None)
    # secado de volumen: promedio desde el inicio de la última contracción vs. promedio de 50 ruedas previo
    fin_c = (b - 1) if b is not None else m - 1
    ref = vol50[ult["hi_i"]] if not np.isnan(vol50[ult["hi_i"]]) else np.nanmean(vo[:ult["hi_i"] + 1])
    seco = float(np.mean(vo[ult["hi_i"]:fin_c + 1]) / ref) if ref and fin_c >= ult["hi_i"] else None
    dias = vol_b = None
    if b is not None:
        dias = m - 1 - b
        vol_b = float(vo[b] / vol50[b - 1]) if b > 0 and vol50[b - 1] else None
        if dias > VCP_DIAS_SEGUIMIENTO: return None
        if any(cl[x] < pivot for x in range(b + 1, m)): est = "fallo"
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

# ---------------------------------------------------------------- score
def partes_score(mv, rs, comp_d, sav_d, comp_d_rup, ins_d, piv, vcp=None):
    tend = mv / 8 * 20
    fuer = rs / 99 * 25
    contr = (comp_d["score"] if comp_d else 0) / 100 * 35
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
    return {"tend": num(tend, 1), "rs": num(fuer, 1), "contr": num(contr, 1), "setup": num(min(setup, 20), 1)}

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
    print("   Régimen de mercado…")
    extra = descargar(["SPY", "QQQ", "^VIX"], "2y", "1d")
    reg = regimen({t: diario.get(t, extra.get(t)) for t in ("SPY", "QQQ")}, extra.get("^VIX"),
                  [d for t, d in diario.items() if info.at[t, "tipo"] == "accion"])
    r21_pct = pd.Series(ret21).rank(pct=True) * 100
    print("3/5 Aplicando Minervini, precio mínimo y ADR…")
    cand = {}
    for t, df in diario.items():
        if t not in rs_pct.index: continue
        tipo = info.at[t, "tipo"]
        if tipo != "cripto" and df.Close.iloc[-1] < PRECIO_MINIMO: continue
        if adr_pct(df) < ADR_MINIMO: continue
        checks, hi, lo = minervini(df, rs_pct[t])
        if pasa_minervini(checks):
            cand[t] = (checks, hi, lo)
    print(f"   {len(cand)} pasan Minervini ({MIN_CRITERIOS_MINERVINI}/8), precio y ADR")
    print("4/5 Historia completa, earnings y AVWAP de los candidatos…")
    hist = descargar(list(cand), "max", "1d") if cand else {}
    activos = []
    dfs_d = {}
    hoy = pd.Timestamp.now()
    for t, (checks, hi, lo) in cand.items():
        tipo = info.at[t, "tipo"]
        df = hist.get(t)
        if df is None or len(df) < len(diario[t]): df = diario[t]
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
        comp = {"d": compresion(df, "d"), "w": compresion(wk, "w")}
        comprimida = any(comp[k] and (comp[k]["es"] or comp[k]["ruptura"]) for k in comp)
        # Sin AVWAP activa: igual entra si tiene VCP, compresión o tocó una EMA diaria (se muestra solo en esas secciones)
        sin_av = bool(EXIGIR_AVWAP and not activo_av)
        if sin_av and not vcp and not comprimida and not (ANALIZAR_30M and toque_ema_diaria(df)): continue
        ins = {"d": inside(df), "w": inside(wk)}
        sav = {"d": setup_avwap(df, av["d"]), "w": setup_avwap(wk, av["w"])}
        rs = float(rs_pct[t]); c = df.Close
        activos.append({
            "t": t, "nombre": str(info.at[t, "nombre"]), "sector": str(info.at[t, "sector"]), "tipo": tipo,
            "precio": num(c.iloc[-1], 4), "chg": num((c.iloc[-1] / c.iloc[-2] - 1) * 100),
            "ret21": num(ret21[t] * 100, 1), "rs": num(rs, 0), "mv": sum(checks), "mv_checks": checks,
            "hi52": num(hi, 4), "lo52": num(lo, 4), "pos52": num((c.iloc[-1] - lo) / (hi - lo) * 100 if hi > lo else 100, 0),
            "avwap": av, "comp": comp, "inside": ins, "setup_av": sav, "pivot30": None, "vcp": vcp, "sin_av": sin_av,
            "earn_prox": prox.strftime("%d-%m-%Y") if prox is not None else None,
            "adr": num(adr_pct(df), 2), "earn_dias": earn_dias,
            "d10": num(estiramiento(df)[0], 1), "d20": num(estiramiento(df)[1], 1), "earn_momento": momento_earnings(prox),
            "ep": {k: v for k, v in ep.items() if not k.startswith("_")} if ep else None,
            "estadio": estadio(df), "flags": banderas(df, sav["d"], earn_dias),
            "spark_d": spark(c, 63), "spark_w": spark(wk.Close, 30), "_r21p": float(r21_pct.get(t, 50)),
        })
    n_req = sum(1 for a in activos if not a["sin_av"])
    print(f"   {n_req} cumplen todos los requisitos")
    con30 = bool(ANALIZAR_30M and activos)
    if con30:
        print(f"5/5 Buscando pivots de 30 minutos (incluye las que no tienen AVWAP activa)…")
        m30 = descargar([a["t"] for a in activos], "5d", "30m")
        for a in activos:
            a["pivot30"] = pivot_30m(m30.get(a["t"]), dfs_d.get(a["t"]))
        activos = [a for a in activos if not a["sin_av"] or a["pivot30"] or a["vcp"] or _comprimida(a)]
    else:
        print("5/5 Intradía desactivado")
        activos = [a for a in activos if not a["sin_av"] or a["vcp"] or _comprimida(a)]
    print(f"   {sum(1 for a in activos if a['vcp'])} con base VCP")
    for a in activos:
        p = partes_score(a["mv"], a["rs"], a["comp"]["d"], a["setup_av"]["d"],
                         a["comp"]["d"] and a["comp"]["d"]["ruptura"], a["inside"]["d"], a["pivot30"], a["vcp"])
        a["partes"] = p
        malas = [f for f in a["flags"] if f["k"] in ("rechazo", "sinvol", "ext", "estirada")]
        a["castigo"] = num(len(malas) * SCORE_CASTIGO_BANDERA, 1)
        a["score"] = num(max(0, sum(v for v in p.values() if v) - a["castigo"]), 1)
        a["calor"] = num(0.6 * a["score"] + 0.4 * a.pop("_r21p"), 1)
    foco = lista_foco(activos)
    print(f"   Lista de foco: {len(foco)}")
    fechas = [df.index[-1] for t, df in diario.items() if info.at[t, "tipo"] != "cripto"] or [hoy]
    datos = {"meta": {
        "fecha_datos": max(fechas).strftime("%d-%m-%Y"), "generado": ahora_ar().strftime("%d-%m-%Y %H:%M"),
        "n_universo": len(diario), "con30m": con30, "regimen": reg, "demo": bool(globals().get("MODO_DEMO", False)),
        "params": {"min_mv": MIN_CRITERIOS_MINERVINI, "sobre_min": PCT_SOBRE_MINIMO_52S, "bajo_max": PCT_DEBAJO_MAXIMO_52S,
                   "rs_min": RS_MINIMO, "precio_min": PRECIO_MINIMO, "exigir_av": EXIGIR_AVWAP,
                   "dist_d": DIST_POR_ROMPER_DIARIO, "dist_w": DIST_POR_ROMPER_SEMANAL,
                   "velas_d": VELAS_RUPTURA_DIARIO, "velas_w": VELAS_RUPTURA_SEMANAL, "emas_30m": lista_emas(),
                   "vol_ruptura": VOL_RUPTURA, "adr_min": ADR_MINIMO, "cerca_gatillo": CERCA_GATILLO,
                   "ep_suba": EP_MIN_SUBA, "ep_vol": EP_MIN_VOL,
                   "vcp_min": VCP_MIN_CONTRACCIONES, "vcp_ult": VCP_ULTIMA_MAX, "vcp_form": VCP_FORMANDO_MAX, "vcp_dist": VCP_DIST_PIVOT,
                   "vcp_seco": VCP_VOL_SECO, "vcp_dias": VCP_DIAS_RUPTURA, "vcp_seg": VCP_DIAS_SEGUIMIENTO,
                   "vcp_smin": VCP_SEMANAS_MIN, "vcp_smax": VCP_SEMANAS_MAX, "emas_asc": EMAS_ASCENSO,
                   "fuertes": ANCLAS_FUERTES, "exigir_rs": EXIGIR_RS, "castigo": SCORE_CASTIGO_BANDERA, "est10": ESTIRADA_EMA10_ADR, "est20": ESTIRADA_EMA20_ADR,
                   "foco_rs": FOCO_RS_MINIMO, "foco_riesgo": FOCO_RIESGO_MAX, "foco_max": FOCO_MAXIMO}},
        "foco": foco, "activos": sorted(activos, key=lambda a: -a["score"])}
    html = PLANTILLA.replace("__DATA__", json.dumps(datos, ensure_ascii=False, allow_nan=False, default=str))
    print(f"Listo en {time.time() - t0:.0f} s")
    return html, datos

PLANTILLA = r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<title>Radar de rupturas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0b0c0e; --rail:#0f1013; --card:#141619; --card2:#1c1f24; --line:#23262c; --line2:#30343b;
  --text:#eceef1; --muted:#8a9099; --faint:#5f656e;
  --acc:#3ddc97; --acc2:#1f9f69; --accsoft:rgba(61,220,151,.13); --oninv:#ffffff;
  --up:#3ddc97; --down:#f0626e; --warn:#f4b740; --blue:#6ea8fe; --violet:#a78bfa;
  --sombra:0 10px 30px rgba(0,0,0,.35);
  --ui:"Plus Jakarta Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
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
  --bg:#0b0c0e; --rail:#0f1013; --card:#141619; --card2:#1c1f24; --line:#23262c; --line2:#30343b;
  --text:#eceef1; --muted:#8a9099; --faint:#5f656e;
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
.card{background:linear-gradient(155deg,var(--card2) 0%,var(--card) 60%);border:1px solid var(--line);border-radius:20px;padding:18px 20px;box-shadow:var(--sombra);min-width:0}
.card h3{margin:0 0 12px;font-size:16px;font-weight:700;display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.card h3 small{color:var(--muted);font-weight:500;font-size:13px}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.gauto{grid-template-columns:repeat(auto-fill,minmax(560px,1fr))}
.inicio{grid-template-columns:minmax(0,1.05fr) minmax(0,1fr)}
@media (max-width:1100px){.inicio,.g2{grid-template-columns:1fr}.gauto{grid-template-columns:1fr}}
@media (max-width:760px){.g3{grid-template-columns:1fr}}
h2.sec{font-size:18px;margin:28px 0 12px;font-weight:700;display:flex;align-items:baseline;gap:10px}
h2.sec small{color:var(--muted);font-weight:500;font-size:13px}
.nota{color:var(--muted);font-size:13.5px;margin:-4px 0 14px;max-width:85ch}

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
.ficha h4{margin:22px 0 10px;font-size:15px}
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
</style>
</head>
<body>
<div class="app">
  <nav class="rail" id="rail" aria-label="Secciones"></nav>
  <main>
    <header class="top">
      <div><h1 id="titulo"></h1><p id="sub"></p></div>
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
const S = {vcpF:'', pag:'inicio', tf:'d', tipo:'todo', q:'', insideMin:1, soloComp:true, sector:null, emaF:0, epHoy:false};
const P = D.meta.params;
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt = (v,d=2) => (v==null||isNaN(v)) ? '–' : Number(v).toLocaleString('es-AR',{minimumFractionDigits:d,maximumFractionDigits:d});
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
const ico = k => `<svg viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
const PAGS = [
  ['inicio','Inicio','Panorama del mercado y lo más destacado del día.'],
  ['sectores','Sectores','Las 5 más calientes de cada sector. El calor combina el score (60%) con el retorno del último mes relativo al universo (40%).'],
  ['avwap','AVWAP','AVWAP ancladas a earnings, episodic pivots, días de alto volumen, máximo estructural, máximo histórico e IPO reciente.'],
  ['vcp','VCP','Bases con contracciones de volatilidad cada vez más chicas y volumen que se seca (Minervini). El pivot es el máximo de la última contracción.'],
  ['comp','Compresión','Activos apretados en precio (ATR y ancho de Bollinger) y en volumen.'],
  ['inside','Inside','Velas con máximo y mínimo dentro de la vela anterior. El gatillo alcista es el máximo de la vela madre.'],
  ['ep','Episodic','Días con suba fuerte y volumen explosivo: posible entrada institucional y nuevo ancla de AVWAP.'],
  ['setups','Setups','Tus setups: ruptura de AVWAP, ruptura de compresión y 30 Min Pivot sobre EMA diaria.'],
];

function spark(arr, w=84, h=24){
  if(!arr || arr.length < 2) return '';
  const mn = Math.min(...arr), mx = Math.max(...arr), r = (mx-mn) || 1;
  const pts = arr.map((v,i) => `${(i/(arr.length-1)*w).toFixed(1)},${(h-2-(v-mn)/r*(h-4)).toFixed(1)}`).join(' ');
  const c = arr[arr.length-1] >= arr[0] ? 'var(--up)' : 'var(--down)';
  return `<svg class="spark" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" aria-hidden="true"><polyline points="${pts}" fill="none" stroke="${c}" stroke-width="1.6" stroke-linejoin="round"/></svg>`;
}
const flags = (a, max=2) => (a.flags||[]).slice(0,max).map(f=>`<span class="fl ${f.tipo}" title="${esc(f.t)}">${esc(f.c)}</span>`).join('');
const tk = (a, fl=true) => `<span class="tk">${esc(a.t)}</span>${fl ? flags(a) : ''}`;
const barra = v => `<span class="sc"><span class="barra"><i style="width:${Math.max(0,Math.min(100,v))}%"></i></span><span>${fmt(v,0)}</span></span>`;
function ring(v, size=70, col='var(--acc)'){
  const r = size/2-6, c = 2*Math.PI*r;
  return `<div class="ring" style="width:${size}px;height:${size}px"><svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" aria-hidden="true">
    <circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="var(--line)" stroke-width="6"/>
    <circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="${col}" stroke-width="6" stroke-linecap="round"
      stroke-dasharray="${(c*v/100).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 ${size/2} ${size/2})"/></svg><b>${fmt(v,0)}</b></div>`;
}
function visibles(conSolo30=false){
  const q = S.q.trim().toLowerCase();
  return D.activos.filter(a => (conSolo30 || !a.sin_av) && (S.tipo==='todo' || a.tipo===S.tipo) &&
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
const card = (titulo, sub, cuerpo) => `<div class="card"><h3>${titulo}${sub!=null?` <small>${sub}</small>`:''}</h3>${cuerpo}</div>`;

/* ---------- Inicio ---------- */
function gauge(v){
  const L = Math.PI*90, col = v<40?'var(--down)':v<60?'var(--warn)':'var(--acc)';
  return `<svg viewBox="0 0 200 110" width="100%" aria-hidden="true">
    <path d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>
    <path d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke="${col}" stroke-width="14" stroke-linecap="round" stroke-dasharray="${(L*v/100).toFixed(1)} ${L.toFixed(1)}"/></svg>`;
}
function vInicio(){
  const act = visibles(), tf = S.tf, R = D.meta.regimen;
  let rom=0; act.forEach(a => { const m = mejorAv(a, tf); if(m && m.estado==='rompe') rom++; });
  const k = [
    ['req', act.length, 'cumplen los requisitos', 'sectores'],
    ['avwap', rom, `rompiendo AVWAP (${TFN[tf]})`, 'avwap'],
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
    <div class="rec">${esc(R.rec)}</div></div>` : card('Régimen de mercado', null, '<p class="vacio">No se pudo calcular en esta corrida.</p>');
  const top = act.slice().sort((x,y)=>y.score-x.score).slice(0,3);
  const idx = Object.fromEntries(D.activos.map(a=>[a.t,a]));
  const fl = (D.foco||[]).filter(f=>idx[f.t] && visibles(true).includes(idx[f.t]));
  const cFo = [
    {h:'Ticker', f:r=>tk(idx[r.t])},
    {h:'Setup', f:r=>esc(r.setup)},
    {h:'Entrada', n:1, f:r=>pr(r.entrada)},
    {h:'Stop', n:1, f:r=>pr(r.stop)},
    {h:'Riesgo', n:1, f:r=>fmt(r.riesgo,1)+'%'},
    {h:'Precio vs. entrada', n:1, f:r=>`<span class="${cls(r.dist)}">${pct(r.dist)}</span>`},
    {h:'Score', n:1, f:r=>fmt(r.score,0)},
  ];
  const foco = `<div class="foco">${card('Lista de foco', fl.length ? fl.length+' para hoy' : null,
    `<p class="nota" style="margin:0 0 10px">Hasta ${P.foco_max} activos con un setup listo (VCP armada o recién rota, compresión con EMAs en ascenso cerca del gatillo o rota, ruptura de AVWAP con volumen), RS ${P.foco_rs}+, riesgo de ${fmt(P.foco_riesgo,0)}% o menos y sin banderas (estirada de la EMA10/20, extendido, sin volumen, rechazo, earnings en 7 días). Ordenados por score.${R && R.score<40 ? ' <b>Régimen defensivo: tamaño chico o esperar.</b>' : ''}</p>`
    + tabla(cFo, fl.map(r=>({...r, a:idx[r.t]})), 'Ningún setup cumple todo hoy. Mejor esperar que forzar.'))}</div>`;
  const PT = [['Tendencia','tend',20,'var(--blue)'],['Fuerza RS','rs',25,'var(--acc)'],['Contracción','contr',35,'var(--violet)'],['Setup','setup',20,'var(--warn)']];
  const spot = top.length ? `<div class="grid g3">${top.map(a=>`<div class="card spot" data-t="${esc(a.t)}" tabindex="0">
      <div class="cab">${ring(a.score)}<div><h4>${esc(a.t)}</h4><p>${esc(a.sector)}${a.estadio?' · estadio '+a.estadio:''}</p><p>${flags(a,3)}</p></div></div>
      <div class="partes">${PT.map(([n,k,m,c])=>`<span class="mut">${n}</span><span class="pbar"><i style="width:${a.partes[k]/m*100}%;background:${c}"></i></span><span>${fmt(a.partes[k],0)}</span>`).join('')}</div></div>`).join('')}</div>`
    : '<p class="vacio">Sin activos con estos filtros.</p>';
  const ev = act.filter(a=>a.earn_dias!=null && a.earn_dias>=0 && a.earn_dias<=7).sort((x,y)=>x.earn_dias-y.earn_dias);
  const earn = ev.length ? `<div class="earn">${ev.map(a=>`<div class="eitem" data-t="${esc(a.t)}" tabindex="0"><b>${esc(a.t)}</b>
      <span>${esc(a.earn_prox)} · ${a.earn_dias===0?'hoy':a.earn_dias===1?'mañana':'en '+a.earn_dias+' días'}</span>
      ${a.earn_momento?`<em class="${a.earn_momento.startsWith('antes')?'bmo':''}">${esc(a.earn_momento)}</em>`:''}</div>`).join('')}</div>`
    : '<p class="vacio">Ningún activo de la lista reporta en los próximos 7 días.</p>';
  return `${foco}<div class="grid inicio">${reg}${kpis}</div>
    <h2 class="sec">Top 3 del score</h2>${spot}
    <h2 class="sec">Earnings próximos <small>7 días · activos que cumplen los requisitos</small></h2>
    ${card('Calendario', ev.length+(ev.length===1?' reporte':' reportes'), earn)}`;
}

/* ---------- Sectores ---------- */
function vSectores(){
  const act = visibles(), tf = S.tf, g = {};
  act.forEach(a => (g[a.sector] = g[a.sector] || []).push(a));
  const secs = Object.entries(g).map(([s,l]) => ({s, l: l.slice().sort((x,y)=>y.calor-x.calor), prom: l.reduce((t,a)=>t+a.calor,0)/l.length}))
    .sort((a,b) => b.prom - a.prom);
  if(!secs.length) return `<p class="vacio">Ningún activo cumple los requisitos con estos filtros.</p>`;
  const franja = `<div class="franja">${secs.map(x => `<button class="sec-t" data-sec="${esc(x.s)}" aria-pressed="${S.sector===x.s}" style="--h:${(x.prom/100).toFixed(2)}">
      <strong>${esc(x.s)}</strong><small>${x.l.length} activos · líder ${esc(x.l[0].t)}</small><em>calor ${fmt(x.prom,0)}</em></button>`).join('')}</div>`;
  const cols = [
    {h:'', f:r=>`<span class="rk">${r.i+1}</span>`},
    {h:'Ticker', f:r=>tk(r.a)},
    {h:'3 meses', f:r=>spark(r.a.spark_d)},
    {h:'Calor', n:1, f:r=>fmt(r.a.calor,0)},
    {h:'Score', n:1, f:r=>fmt(r.a.score,0)},
    {h:'RS', n:1, f:r=>fmt(r.a.rs,0)},
    {h:'ADR', n:1, f:r=>fmt(r.a.adr,1)+'%'},
    {h:'AVWAP', f:r=>{const m=mejorAv(r.a,tf); return m ? `${badge(m.estado)} <span class="mut">${esc(m.ancla)}</span>` : '<span class="mut">–</span>';}},
    {h:'1 mes', n:1, f:r=>`<span class="${cls(r.a.ret21)}">${pct(r.a.ret21,1)}</span>`},
  ];
  const lista = S.sector ? secs.filter(x=>x.s===S.sector) : secs;
  return `${franja}<div class="grid gauto">${lista.map(x => card(esc(x.s), x.l.length+' en total', tabla(cols, x.l.slice(0,5).map((a,i)=>({a,i})), ''))).join('')}</div>`;
}

/* ---------- AVWAP ---------- */
function vAvwap(){
  const tf = S.tf, rows = [];
  visibles().forEach(a => (a.avwap[tf]||[]).filter(x=>x.cuenta).forEach(x => rows.push({a, x})));
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)},
    {h:'Anclada en', f:r=>`${esc(r.x.ancla)}${r.x.fuerte?'<span class="fuerte">★</span>':''} <span class="mut">${esc(r.x.fecha)}</span>`},
    {h:'AVWAP', n:1, f:r=>pr(r.x.valor)},
    {h:'Precio', n:1, f:r=>pr(r.a.precio)},
    {h:'Distancia', n:1, f:r=>`<span class="${cls(r.x.dist)}">${pct(r.x.dist)}</span>`},
    {h:'Vol. ruptura', n:1, f:r=>r.x.vol_x!=null ? fmt(r.x.vol_x,1)+'x' : '–'},
    {h:'Objetivo', n:1, f:r=>r.x.objetivo ? pr(r.x.objetivo) : '<span class="mut">sin techo</span>'},
    {h:'Score', n:1, f:r=>fmt(r.a.score,0)},
  ];
  const rom = rows.filter(r=>r.x.estado==='rompe').sort((p,q)=>p.x.dist-q.x.dist);
  const por = rows.filter(r=>r.x.estado==='por romper').sort((p,q)=>q.x.dist-p.x.dist);
  return `<p class="nota">Solo cuentan dos casos: "rompiendo" = cerró arriba en las últimas ${tf==='d'?P.velas_d:P.velas_w} velas <b>con volumen de ${fmt(P.vol_ruptura,1)}x o más</b> (cualquier ancla); "por romper" = hasta ${tf==='d'?P.dist_d:P.dist_w}% debajo de un <b>ancla fuerte</b> ★ (${esc(P.fuertes)}). El objetivo es el máximo desde donde sale la AVWAP.</p>
  <div class="grid g2">${card('Rompiendo', rom.length, tabla(cols, rom, 'Nada rompiendo en '+TFN[tf]+'.'))}${card('Por romper', por.length, tabla(cols, por, 'Nada a punto de romper en '+TFN[tf]+'.'))}</div>`;
}

/* ---------- VCP ---------- */
const sinAv = a => a.sin_av ? '<span class="sin_av" title="No cumple el requisito de AVWAP: aparece solo por este setup">sin AVWAP</span>' : '';
const contrTxt = v => `<span class="contr">${(v.contr||[]).map(x=>`<b>${fmt(x,0)}%</b>`).join('<i>→</i>')}</span>`;
function vVcp(){
  const ORD = {recien:0, armada:1, confirmo:2, sinvol:3, formandose:4, fallo:5};
  const todos = visibles(true).filter(a=>a.vcp);
  const l = todos.filter(a=>!S.vcpF || a.vcp.estado===S.vcpF)
    .sort((x,y)=>(ORD[x.vcp.estado]-ORD[y.vcp.estado]) || (Math.abs(x.vcp.dist)-Math.abs(y.vcp.dist)));
  const F = [['','Todas'],['recien','Recién rompió'],['armada','Armada'],['confirmo','Confirmó'],['sinvol','Sin volumen'],['formandose','Formándose'],['fallo','Falló']];
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)+sinAv(r.a)},
    {h:'Estado', f:r=>badge(r.a.vcp.estado)},
    {h:'Contracciones', f:r=>contrTxt(r.a.vcp)},
    {h:'Base', n:1, f:r=>fmt(r.a.vcp.semanas,0)+' sem.'},
    {h:'Pivot', n:1, f:r=>pr(r.a.vcp.pivot)},
    {h:'Stop', n:1, f:r=>pr(r.a.vcp.stop)},
    {h:'Riesgo', n:1, f:r=>fmt(r.a.vcp.riesgo,1)+'%'},
    {h:'Precio vs. pivot', n:1, f:r=>`<span class="${cls(r.a.vcp.dist)}">${pct(r.a.vcp.dist)}</span>`},
    {h:'Volumen en la última', n:1, f:r=>r.a.vcp.seco!=null ? `<span class="${r.a.vcp.seco<P.vcp_seco?'up':'mut'}">${fmt(r.a.vcp.seco,2)}x</span>` : '–'},
    {h:'Vol. ruptura', n:1, f:r=>r.a.vcp.vol_rup!=null ? `<span class="${r.a.vcp.vol_rup>=P.vol_ruptura?'up':'down'}">${fmt(r.a.vcp.vol_rup,1)}x</span>` : '–'},
  ];
  return `<div class="filtros">${F.map(([k,n])=>`<button class="chip" data-vcp="${k}" aria-pressed="${S.vcpF===k}">${n} <span class="mut">${k?todos.filter(a=>a.vcp.estado===k).length:todos.length}</span></button>`).join('')}</div>
  <p class="nota">Contracciones: cuánto cayó el precio en cada retroceso de la base, de la más vieja a la más nueva; tienen que ser cada vez más chicas (al menos ${P.vcp_min}). El pivot tiene que estar en la parte alta de la base. "Formándose" = la última contracción es de ${fmt(P.vcp_form,0)}% o menos, pero todavía no está apretada o el precio está lejos del pivot. "Armada" = última contracción de ${fmt(P.vcp_ult,0)}% o menos, volumen por debajo del promedio de 50 ruedas y precio a ${fmt(P.vcp_dist,0)}% o menos del pivot. "Recién rompió" = cerró sobre el pivot con volumen de ${fmt(P.vol_ruptura,1)}x o más en las últimas ${P.vcp_dias} ruedas; "confirmó" = se sostiene arriba; "falló" = volvió a cerrar debajo del pivot; "rompió sin volumen" = cerró arriba del pivot sin el volumen necesario (no cuenta como ruptura). Solo en diario.</p>
  ${card('Bases VCP', l.length, tabla(cols, l.map(a=>({a})), 'Ninguna base VCP con este filtro.'))}`;
}
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

/* ---------- Compresión ---------- */
function vComp(){
  const tf = S.tf;
  let l = visibles(true).filter(a=>a.comp[tf] && (!a.sin_av || a.comp[tf].es || a.comp[tf].ruptura));
  if(S.soloComp) l = l.filter(a=>a.comp[tf].es || a.comp[tf].ruptura);
  l.sort((x,y)=>y.comp[tf].score-x.comp[tf].score);
  const k = tf==='d' ? ['ATR 10/50','Vol 10/50','Rango 10'] : ['ATR 4/20','Vol 4/20','Rango 6'];
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)+sinAv(r.a)},
    {h:tf==='d'?'3 meses':'30 semanas', f:r=>spark(tf==='d'?r.a.spark_d:r.a.spark_w)},
    {h:'Compresión', f:r=>barra(r.a.comp[tf].score)+(r.a.comp[tf].ruptura?' '+badge('rompio'):'')},
    {h:k[0], n:1, f:r=>fmt(r.a.comp[tf].atr_r)},
    {h:'Ancho BB pctil', n:1, f:r=>fmt(r.a.comp[tf].bb_pct,0)},
    {h:k[1], n:1, f:r=>`<span class="${r.a.comp[tf].vol_r<1?'up':'mut'}">${fmt(r.a.comp[tf].vol_r)}</span>`},
    {h:k[2], n:1, f:r=>fmt(r.a.comp[tf].rango,1)+'%'},
    {h:'Gatillo', n:1, f:r=>pr(r.a.comp[tf].gatillo)},
    {h:'Al gatillo', n:1, f:r=>pct(r.a.comp[tf].dist_gatillo)},
  ];
  const sube = l.filter(a=>a.comp[tf].emas), resto = l.filter(a=>!a.comp[tf].emas);
  const vac = S.soloComp ? 'Ninguna en '+TFN[tf]+'.' : 'Sin datos.';
  return `<div class="filtros"><button class="chip" id="solo" aria-pressed="${S.soloComp}">Solo comprimidas</button></div>
  <p class="nota">"Comprimida" = ATR corto bajo el largo, ancho de Bollinger en el 30% más bajo y <b>volumen secándose</b> (${k[1]} debajo de 0,95; en verde si está bajo 1). Separadas según las EMAs ${esc(P.emas_asc)} ${tf==='d'?'diarias':'semanales'} vengan subiendo (hoy más altas que hace 5 velas).</p>
  <div class="grid">${card('Con EMAs en ascenso', sube.length, tabla(cols, sube.map(a=>({a})), vac))}
  ${card('Sin EMAs en ascenso', resto.length, tabla(cols, resto.map(a=>({a})), vac))}</div>`;
}

/* ---------- Inside ---------- */
function vInside(){
  const tf = S.tf, nom = tf==='d' ? 'day' : 'week';
  const l = visibles().filter(a=>a.inside[tf] && a.inside[tf].n>=S.insideMin)
    .sort((x,y)=>(y.inside[tf].n-x.inside[tf].n) || (y.comp[tf].score-x.comp[tf].score));
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)},
    {h:'Inside', f:r=>`<span class="est ${r.a.inside[tf].n>=2?'rompe':'porromper'}">${r.a.inside[tf].n>=2?'Doble':'Simple'}${r.a.inside[tf].n>2?' ('+r.a.inside[tf].n+')':''}</span>`},
    {h:'Madre máx.', n:1, f:r=>pr(r.a.inside[tf].madre_hi)},
    {h:'Madre mín.', n:1, f:r=>pr(r.a.inside[tf].madre_lo)},
    {h:'Al gatillo', n:1, f:r=>pct(r.a.inside[tf].dist_hi)},
    {h:'Compresión', f:r=>barra(r.a.comp[tf].score)},
    {h:'AVWAP', f:r=>{const m=mejorAv(r.a,tf); return m ? badge(m.estado) : '<span class="mut">–</span>';}},
  ];
  return `${tf==='w'?'<p class="nota">La vela semanal incluye la semana en curso.</p>':''}
  <div class="filtros">
    <button class="chip" data-in="1" aria-pressed="${S.insideMin===1}">Inside ${nom}</button>
    <button class="chip" data-in="2" aria-pressed="${S.insideMin===2}">Doble inside ${nom}</button>
  </div>
  ${card(S.insideMin===2?'Doble inside '+nom:'Inside '+nom, l.length, tabla(cols, l.map(a=>({a})), S.insideMin===2 ? 'Ningún doble inside '+nom+' hoy.' : 'Ningún inside '+nom+' hoy.'))}`;
}

/* ---------- Episodic pivots ---------- */
function vEp(){
  const l = visibles().filter(a=>a.ep && (!S.epHoy || a.ep.dias===0)).sort((x,y)=>(x.ep.dias-y.ep.dias) || (y.ep.vol_x-x.ep.vol_x));
  const avEp = a => (a.avwap.d||[]).find(x=>x.ancla==='Episodic pivot');
  const cols = [
    {h:'Ticker', f:r=>tk(r.a)},
    {h:'Cuándo', f:r=>r.a.ep.dias===0 ? '<span class="est rompe">Hoy</span>' : `hace ${r.a.ep.dias} ${r.a.ep.dias===1?'rueda':'ruedas'} <span class="mut">${esc(r.a.ep.fecha)}</span>`},
    {h:'Suba del día', n:1, f:r=>`<span class="up">${pct(r.a.ep.suba,1)}</span>`},
    {h:'Volumen', n:1, f:r=>fmt(r.a.ep.vol_x,1)+'x'},
    {h:'Desde el EP', n:1, f:r=>`<span class="${cls(r.a.ep.desde)}">${pct(r.a.ep.desde,1)}</span>`},
    {h:'AVWAP del EP', n:1, f:r=>{const x=avEp(r.a); return x ? `<span class="${cls(x.dist)}">${pct(x.dist)}</span>` : '<span class="mut">–</span>';}},
    {h:'Sector', f:r=>`<span class="mut">${esc(r.a.sector)}</span>`},
    {h:'Score', n:1, f:r=>fmt(r.a.score,0)},
  ];
  return `<p class="nota">Suba de ${fmt(P.ep_suba,0)}% o más con volumen de ${fmt(P.ep_vol,1)}x o más el promedio de 50 ruedas, en las últimas 10 ruedas (solo diario). Un EP no siempre es para entrar ya: suele convenir esperar una consolidación o un pullback ordenado. "AVWAP del EP" es la distancia del precio a la AVWAP anclada en ese día.</p>
  <div class="filtros">
    <button class="chip" data-ephoy="0" aria-pressed="${!S.epHoy}">Últimas 10 ruedas</button>
    <button class="chip" data-ephoy="1" aria-pressed="${S.epHoy}">Solo hoy</button>
  </div>
  ${card('Episodic pivots', l.length, tabla(cols, l.map(a=>({a})), S.epHoy ? 'Ningún episodic pivot hoy.' : 'Ningún episodic pivot en las últimas 10 ruedas.'))}`;
}

/* ---------- Setups ---------- */
function vSetups(){
  const tf = S.tf, act = visibles();
  const av = act.filter(a=>a.setup_av[tf]).map(a=>({a, s:a.setup_av[tf]}))
    .sort((p,q)=> (p.s.estado===q.s.estado ? (q.s.rr||0)-(p.s.rr||0) : (p.s.estado==='rompe'?-1:1)));
  const cAv = [
    {h:'Ticker', f:r=>tk(r.a)},
    {h:'Estado', f:r=>badge(r.s.estado)},
    {h:'Anclada en', f:r=>esc(r.s.ancla)},
    {h:'Entrada', n:1, f:r=>pr(r.s.entrada)},
    {h:'Stop', n:1, f:r=>pr(r.s.stop)},
    {h:'Objetivo', n:1, f:r=>r.s.objetivo ? pr(r.s.objetivo) : '<span class="mut">sin techo</span>'},
    {h:'R:R', n:1, f:r=>r.s.rr!=null ? fmt(r.s.rr,1) : '–'},
  ];
  const cb = visibles(true).filter(a=>a.comp[tf] && (a.comp[tf].ruptura || (a.comp[tf].es && a.comp[tf].dist_gatillo!=null && a.comp[tf].dist_gatillo<=P.cerca_gatillo)))
    .map(a=>({a, e: a.comp[tf].ruptura ? 'rompio' : 'preparada'}))
    .sort((p,q)=> (p.e===q.e ? q.a.comp[tf].score-p.a.comp[tf].score : (p.e==='rompio'?-1:1)));
  const cCb = [
    {h:'Ticker', f:r=>tk(r.a)+sinAv(r.a)},
    {h:'EMAs', f:r=>r.a.comp[tf].emas ? '<span class="up">en ascenso</span>' : '<span class="mut">no</span>'},
    {h:'Estado', f:r=>badge(r.e)},
    {h:'Gatillo', n:1, f:r=>pr(r.a.comp[tf].gatillo)},
    {h:'Precio', n:1, f:r=>pr(r.a.precio)},
    {h:'Al gatillo', n:1, f:r=>pct(r.a.comp[tf].dist_gatillo)},
    {h:'Vol. relativo', n:1, f:r=>fmt(r.a.comp[tf].vol_hoy,1)+'x'},
    {h:'Compresión', f:r=>barra(r.a.comp[tf].score)},
  ];
  const ORD = {disparado:0, armado:1, esperando:2};
  const pv = visibles(true).filter(a=>a.pivot30 && (!S.emaF || a.pivot30.ema_n===S.emaF)).map(a=>({a, p:a.pivot30}))
    .sort((p,q)=> (ORD[p.p.estado]-ORD[q.p.estado]) || ((p.p.riesgo??99)-(q.p.riesgo??99)));
  const cPv = [
    {h:'Ticker', f:r=>tk(r.a)+(r.a.sin_av?'<span class="sin_av" title="No cumple el requisito de AVWAP: aparece solo por este setup">sin AVWAP</span>':'')},
    {h:'Estado', f:r=>badge(r.p.estado)},
    {h:'EMA diaria', f:r=>`<span class="tk">EMA${r.p.ema_n}</span> <span class="mut">${esc(r.p.toque)} · ${pr(r.p.ema)}</span>`},
    {h:'Entrada (máx. vela verde)', n:1, f:r=>pr(r.p.entrada)},
    {h:'Stop (mín. vela verde)', n:1, f:r=>pr(r.p.stop)},
    {h:'Riesgo', n:1, f:r=>r.p.riesgo!=null ? fmt(r.p.riesgo,1)+'%' : '–'},
    {h:'Precio vs. entrada', n:1, f:r=>r.p.dist!=null ? `<span class="${cls(r.p.dist)}">${pct(r.p.dist)}</span>` : '–'},
    {h:'AVWAP diario', f:r=>{const m=mejorAv(r.a,'d'); return m ? badge(m.estado) : '<span class="mut">–</span>';}},
  ];
  return `<h2 class="sec" style="margin-top:0">Ruptura de AVWAP <small>${TFN[tf]}</small></h2>
  <p class="nota">Entrada al superar la AVWAP (confirmala con una vela de 30 min), stop en el mínimo ${tf==='d'?'del día':'de la semana'} y objetivo en el máximo desde donde sale la AVWAP.</p>
  ${card('Setups de AVWAP', av.length, tabla(cAv, av, 'Ningún setup de AVWAP en '+TFN[tf]+'.'))}
  <h2 class="sec">Ruptura de compresión <small>${TFN[tf]}</small></h2>
  <p class="nota">"Rompió" = venía comprimida, cerró sobre el gatillo y con volumen de al menos ${fmt(P.vol_ruptura,1)}x el promedio. "Preparada" = comprimida y a ${P.cerca_gatillo}% o menos del gatillo.</p>
  ${card('Compresiones', cb.length, tabla(cCb, cb, 'Ninguna ruptura de compresión en '+TFN[tf]+'.'))}
  <h2 class="sec">30 Min Pivot <small>undercut de EMA diaria + primera vela verde</small></h2>
  <div class="filtros">${[0].concat(P.emas_30m).map(e=>`<button class="chip" data-ema="${e}" aria-pressed="${S.emaF===e}">${e?'EMA'+e:'Todas las EMA'}</button>`).join('')}</div>
  <p class="nota">En diario, el precio tocó o perforó (undercut) alguna de las EMA ${P.emas_30m.join(', ')}, hoy o ayer. En 30 min, la primera vela verde después del mínimo marca la entrada (su máximo) y el stop (su mínimo). "Esperando" = tocó la EMA pero todavía no hay vela verde; "armado" = hay vela verde y no superó su máximo; "disparado" = superó el máximo en las últimas 3 horas. Acá entran también las que cumplen Minervini, precio y ADR aunque no estén rompiendo ni por romper una AVWAP (marcadas "sin AVWAP"); esas aparecen solo acá, en VCP y en Compresión.${D.meta.con30m ? '' : ' El análisis intradía estaba desactivado en esta corrida.'}</p>
  ${card('30 Min Pivot', pv.length, tabla(cPv, pv, 'Ninguna acción tocó sus EMAs diarias hoy o ayer.'))}`;
}

/* ---------- Ficha ---------- */
const MV = ['Precio sobre SMA150 y SMA200','SMA150 sobre SMA200','SMA200 subiendo hace 1 mes','SMA50 sobre SMA150 y SMA200','Precio sobre SMA50',
  `${P.sobre_min}% o más sobre el mínimo 52s`, `Dentro del ${P.bajo_max}% del máximo 52s`, `RS ${P.rs_min} o más`];
function ficha(t){
  const a = D.activos.find(x=>x.t===t); if(!a) return;
  const PT = [['Tendencia','tend',20,'var(--blue)'],['Fuerza RS','rs',25,'var(--acc)'],['Contracción','contr',35,'var(--violet)'],['Setup','setup',20,'var(--warn)']];
  const tvSym = a.tipo==='cripto' ? a.t.replace('-','') : a.t.replace('-','.');
  const avt = tf => (a.avwap[tf]||[]).length ? `<div class="tw"><table><thead><tr><th>Ancla</th><th class="n">AVWAP</th><th class="n">Dist.</th><th class="n">Vol.</th><th>Estado</th></tr></thead><tbody>${
      a.avwap[tf].map(x=>`<tr><td>${esc(x.ancla)}${x.fuerte?'<span class="fuerte">★</span>':''} <span class="mut">${esc(x.fecha)}</span></td><td class="n">${pr(x.valor)}</td><td class="n ${cls(x.dist)}">${pct(x.dist)}</td><td class="n">${x.vol_x!=null?fmt(x.vol_x,1)+'x':'–'}</td><td>${badge(x.estado)}${(x.estado==='rompe'||x.estado==='por romper')&&!x.cuenta?' <span class="mut" title="No cuenta: rompió sin volumen o ancla débil">no cuenta</span>':''}</td></tr>`).join('')}</tbody></table></div>` : '<p class="vacio">Sin anclas.</p>';
  const cmp = tf => a.comp[tf] ? `<span>Compresión ${TFN[tf]}</span><span>${fmt(a.comp[tf].score,0)}${a.comp[tf].es?' · comprimida':''}</span>` : '';
  const ins = tf => `<span>Inside ${tf==='d'?'day':'week'}</span><span>${a.inside[tf] && a.inside[tf].n ? a.inside[tf].n : 'no'}</span>`;
  $('#ficha').innerHTML = `
    <div class="fh"><div><h2>${esc(a.t)}</h2><p>${esc(a.nombre)} · ${esc(a.sector)}</p></div><button class="cerrar" id="cerrar" aria-label="Cerrar ficha">✕</button></div>
    <div class="precio">${pr(a.precio)} <span class="${cls(a.chg)}">${pct(a.chg)}</span></div>
    <div style="margin-top:12px">${spark(a.spark_d, 420, 72)}</div>
    ${a.sin_av ? `<p class="nota" style="margin-top:12px">No está rompiendo ni por romper ninguna AVWAP: cumple Minervini, precio y ADR, y aparece solo en VCP, Compresión y 30 Min Pivot.</p>` : ''}
    ${(a.flags||[]).length ? `<h4>Avisos</h4><div class="flist">${a.flags.map(f=>`<div class="${f.tipo}">${esc(f.t)}</div>`).join('')}</div>` : ''}
    <h4>Score</h4>
    <div style="display:flex;gap:18px;align-items:center">${ring(a.score, 84)}
      <div class="partes" style="flex:1">${PT.map(([n,k,m,c])=>`<span class="mut">${n}</span><span class="pbar"><i style="width:${a.partes[k]/m*100}%;background:${c}"></i></span><span>${fmt(a.partes[k],1)}/${m}</span>`).join('')}</div></div>
    ${a.castigo>0 ? `<p class="nota" style="margin-top:8px">Descuento de ${fmt(a.castigo,0)} puntos por banderas (estirada, extendido, sin volumen o rechazo).</p>` : ''}
    <h4>Criterios de Minervini · ${a.mv}/8</h4>
    <ul class="checks">${MV.map((l,i)=>`<li><b class="${a.mv_checks[i]?'up':'down'}">${a.mv_checks[i]?'✓':'✗'}</b>${l}</li>`).join('')}</ul>
    <h4>Rango de 52 semanas · ${fmt(a.pos52,0)}%</h4>
    <div class="rango"><i style="left:${Math.max(0,Math.min(100,a.pos52))}%"></i></div>
    <div class="rl"><span>${pr(a.lo52)}</span><span>${pr(a.hi52)}</span></div>
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
      <span>RS</span><span>${fmt(a.rs,0)}</span>
      <span>ADR% (20 días)</span><span>${fmt(a.adr,2)}%</span>
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
const CORTO = {comp:'Compr.', sectores:'Sectores', episodic:'EP'};
const VISTAS = {inicio:vInicio, sectores:vSectores, avwap:vAvwap, vcp:vVcp, comp:vComp, inside:vInside, ep:vEp, setups:vSetups};
$('#rail').innerHTML = `<div class="logo">${'<svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>'}</div>` +
  PAGS.map(([k,n])=>`<button data-pag="${k}" aria-current="${S.pag===k?'page':'false'}">${ico(k)}<span class="lg">${n}</span><span class="ct">${CORTO[k]||n}</span></button>`).join('');
function ir(p){
  S.pag = p; document.querySelectorAll('#rail button').forEach(b=>b.setAttribute('aria-current', b.dataset.pag===p ? 'page' : 'false'));
  render(); window.scrollTo(0,0);
}
function render(){
  const pg = PAGS.find(x=>x[0]===S.pag);
  $('#titulo').textContent = {inicio:'Radar de rupturas', ep:'Episodic pivots', setups:'Mis setups', inside:'Inside days'}[pg[0]] || pg[1];
  $('#sub').textContent = pg[2];
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
$('#vista').addEventListener('click', e => {
  const k = e.target.closest('[data-ir]'); if(k){ ir(k.dataset.ir); return; }
  const sec = e.target.closest('.sec-t'); if(sec){ S.sector = S.sector===sec.dataset.sec ? null : sec.dataset.sec; render(); return; }
  if(e.target.closest('#solo')){ S.soloComp = !S.soloComp; render(); return; }
  const vf = e.target.closest('[data-vcp]'); if(vf){ S.vcpF = vf.dataset.vcp; render(); return; }
  const em = e.target.closest('[data-ema]'); if(em){ S.emaF = +em.dataset.ema; render(); return; }
  const eh = e.target.closest('[data-ephoy]'); if(eh){ S.epHoy = eh.dataset.ephoy==='1'; render(); return; }
  const ch = e.target.closest('[data-in]'); if(ch){ S.insideMin = +ch.dataset.in; render(); return; }
  const tr = e.target.closest('[data-t]'); if(tr) ficha(tr.dataset.t);
});
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
$('#pie').innerHTML = `${m.n_universo} activos analizados. Requisitos: al menos ${P.min_mv} de 8 criterios de Minervini (${P.sobre_min}% sobre el mínimo y dentro del ${P.bajo_max}% del máximo de 52 semanas, RS ${P.rs_min}+), precio de ${P.precio_min} USD o más en acciones y ETF, ADR de ${fmt(P.adr_min,1)}% o más${P.exigir_rs ? ' (el RS es obligatorio)' : ''}${P.exigir_av ? ', y una AVWAP rota con volumen o por romper en un ancla fuerte. VCP, Compresión y 30 Min Pivot no exigen AVWAP' : ''}. Horarios en hora de Argentina. Esto es un filtro técnico, no una recomendación de compra.`;
render();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    import os
    html, datos = correr()
    os.makedirs("site", exist_ok=True)
    with open("site/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Dashboard escrito en site/index.html")
