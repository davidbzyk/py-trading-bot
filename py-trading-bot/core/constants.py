 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:27:07 2021

@author: maxime
"""

BEAR_PATTERNS={
    "CDLLONGLINE":-100,
    "CDLENGULFING":-100,
    "CDLCLOSINGMARUBOZU":-100,
    "CDLBELTHOLD":-100,
    "CDLHIKKAKE":-200,
    "CDLRISEFALL3METHODS":-100,   #very rare
    "CDL3LINESTRIKE":100,         #very rare
    "CDLBREAKAWAY":-100,
    "CDLABANDONEDBABY":-100,      #very rare
    "CDLEVENINGSTAR":-100,
    "CDLSEPARATINGLINES":-100,    #very rare
    "CDLEVENINGDOJISTAR":-100,
    "CDL3BLACKCROWS":-100,
    "CDLDARKCLOUDCOVER":-100,
    "CDLMARUBOZU":-100
    }

BULL_PATTERNS={
    "CDLKICKINGBYLENGTH":100,
    "CDLKICKING":100,
    "CDLMARUBOZU":100,
    "CDLCLOSINGMARUBOZU":100,
    "CDL3WHITESOLDIERS":100,      #very rare
    "CDLLONGLINE":100,
    "CDLENGULFING":100,
    "CDLDRAGONFLYDOJI":100,
    "CDLTAKURI":100,
    "CDLMORNINGDOJISTAR":100,
    "CDLMORNINGSTAR":100,
    "CDLHANGINGMAN":-100,
    "CDL3INSIDE":100,
    "CDLKICKINGBYLENGTH_INV":100,
    "CDLKICKING_INV":100,
    }

#Selected according to strategy D, bear
BEAR_PATTERNS_LIGHT={
    "CDLBREAKAWAY":-100,
    "CDLEVENINGDOJISTAR":-100,
    "CDLDARKCLOUDCOVER":-100,
    }

BULL_PATTERNS_LIGHT={
    "CDLKICKING":100,
    "CDLMARUBOZU":100,
    "CDLDRAGONFLYDOJI":100,
    "CDLMORNINGSTAR":100,
    "CDLHANGINGMAN":-100,
    }

CAC40=[
    "AC.PA",
    "ACA.PA",
    "AI.PA",
    "AIR.PA",
    "ALO.PA",
    "ATO.PA",
    "BN.PA",
    "BNP.PA",
    "CA.PA",
    "CAP.PA",
    "CS.PA",
    "DG.PA",
    "DSY.PA",
    "EL.PA",
    "EN.PA",
    "ENGI.PA",
    "ERF.PA",
    "GLE.PA",
    "HO.PA",
    "KER.PA",
    "LR.PA",
    "MC.PA",
    "ML.PA",
    "OR.PA",
    "ORA.PA", 
    "PUB.PA",
    "RI.PA",   
    "RMS.PA",
    "RNO.PA",
    "SAF.PA",
    "SAN.PA",
    "SGO.PA",
    "SLB.PA",
    "STLA.PA", 
    "STMPA.PA",
    "SU.PA",
    "SW.PA",
    "TEP.PA", 
    "TTE.PA",
    "VIE.PA",
    "VIV.PA",
    "WLN.PA",
    ]

CAC40_INTRO={
    "STLA.PA":"2021-01-18",
    "LR.PA":"2006-06-01", #from YF
    "WLN.PA":"2014-07-02",
    "ACA.PA":"2007-01-22", #for some inexplicable reason on YF #"ACA.PA":"2002-01-01",
    "SW.PA":"2000-03-01",
    }

CAC40_DELIST={}

DAX=[
    "1COV.DE",
    "ADS.DE",
    "AIR.DE",
    "ALV.DE",
    "BAS.DE",
    "BAYN.DE",
    "BEI.DE", 
    "BMW.DE",
    "BNR.DE",
    "CBK.DE",
    "CON.DE",
    "DB1.DE",
    "DBK.DE", #=DB
    "DHER.DE",
    "DPW.DE",
    "DTE.DE", 
    "DTG.DE", 
    "ENR.DE", 
    "FME.DE",
    "FRE.DE",
    "HEI.DE",
    "HEN3.DE",
    "HFG.DE",
    "HNR1.DE",
    "IFX.DE",
    "LIN.DE",
    "MBG.DE",
    "MRK.DE", 
    "MTX.DE",
    "MUV2.DE",
    "PAH3.DE",
    "PUM.DE",
    "QIA.DE",
    "RWE.DE",
    "SAP.DE",
    "SHL.DE",
    "SIE.DE",
    "SRT.DE",
    "SY1.DE",
    "VNA.DE",
    "VOW3.DE",
    "ZAL.DE",
    ]

DAX_INTRO={
    "DTG.DE":"2021-12-10",
    "ENR.DE":"2020-09-28",
    "LIN.DE":"2018-11-01", #buggy before
    "DHER.DE":"2017-07-01", 
    "HFG.DE":"2017-11-01",
    "1COV.DE":"2015-11-01",
    "SHL.DE":"2018-05-01",
    "ZAL.DE":"2014-10-01",
    "PAH3.DE":"2009-02-01",
    "BNR.DE":"2010-05-01",
    "VNA.DE":"2013-08-01"
    }

DAX_DELIST={}
  
NASDAQ=[
    "AAPL",  
    "ABNB", 
    "ADBE", 
    "ADI",
    "ADP",
    "ADSK", 
    "AEP", 
    "ALGN", 
    "AMAT",
    "AMD",
    "AMGN",
    "AMZN", 
    "ANSS",
    "ASML",
    "ATVI",
    "AVGO",
    "BIDU",
    "BIIB",
    "BKNG",
    "CDNS",
    "CHTR",
    "CMCSA",
    "COST",
    "CPRT",
    "CRWD", 
    "CSCO",
    "CSX",
    "CTAS",
    "CTSH",
    "DB",
    "DDOG", 
    "DLTR",
    "DOCU",
    "DXCM",
    "EA",
    "EBAY",
    "EXC",
    "FAST",
    "META",
    #"FISV",
    "FTNT",
    "GILD",
    "GOOG", 
    "HON",
    "IDXX",
    "ILMN",
    "INTC",
    "INTU",
    "ISRG",
    "JD",
    "KDP",
    "KHC",
    "KLAC",
    "LCID", 
    "LRCX",
    "LULU",
    "MAR",
    "MCHP",
    "MDLZ",
    "MELI",
    "MNST",
    "MRNA",
    "MRVL",
    "MSFT", 
    "MTCH",
    "MU",
    "NFLX",
    "NTES",
    "NVDA",
    "NXPI",
    "OKTA",
    "ORLY",
    "PANW",
    "PAYX",
    "PCAR",
    "PDD",
    "PEP",
    "PTON", 
    "PYPL",
    "QCOM",
    "REGN",
    "ROST",
    "SBUX",
    "SGEN",
    "SIRI",
    "SNPS",
    "SPLK",
    "SWKS",
    "TEAM",
    "TMUS",
    "TSLA",
    "TXN",
    "VRSK",
    "VRSN",
    "VRTX",
    "WBA",
    "WDAY",
    "XEL",
    "ZM",
    "ZS"
    ]

NASDAQ_INTRO={
    "AAPL":"1982-12-12",
    "ABNB":"2020-12-01",
    "AVGO":"2009-09-01",
    "CHTR":"2010-02-01",
    "CRWD":"2019-07-01",
    "DDOG":"2019-10-01",
    "DOCU":"2018-05-01",
    "FTNT":"2008-12-01",
    "JD":"2014-05-19",
    "KDP":"2008-06-01",
    "KHC":"2015-07-06",
    "LCID":"2021-10-01",
    "LULU":"2007-08-01",
    "MELI":"2007-09-01",
    "META":"2012-07-01",
    "MRNA":"2019-01-01",
    "NXPI":"2010-09-01",
    "OKTA":"2017-05-01",
    "PANW":"2012-08-01",
    "PDD":"2018-07-01",
    "PTON":"2019-10-01",
    "PYPL":"2015-07-06",
    "SPLK":"2012-05-01",
    "TEAM":"2016-01-01",
    "TMUS":"2007-05-01",
    "TSLA":"2010-07-01",
    "VRSK":"2009-11-01",
    "WDAY":"2012-11-01",
    "ZS":"2018-06-01",
    "ZM":"2019-05-01",
    }

NASDAQ_DELIST={}

NYSE=["MMM",
      "AOS",
      "ABT",
      "ABBV",
      "ABMD",
      "ACN",
      "ATVI",
      "AAP",
      "AES",
      "AFL",
      "A",
      "ALK",
      "ALB",
      "ARE",
      "ALLE",
      "LNT",
      "ALL",
      "MO",
      "AMCR",
      "AEE",
      "AAL",
      "AEP",
      "AXP",
      "AIG",
      "AMT",
      "AWK",
      "AMP",
      "ABC",
      "AME",
      "APH",
      "AON",
      "APA",
      "APTV",
      "ANET",
      "AJG",
      "AIZ",
      "T",
      "ATO",
      "ADSK",
      "AZO",
      "AVB",
      "AVY",
      "BKR",
      "BALL",
      "BAC",
      "BBWI",
      "BAX",
      "BDX",
      "WRB",
      "BRK-B",
      "BBY",
      "BIO",
      "TECH",
      "BIIB",
      "BLK",
      "BK",
      "BA",
      "BWA",
      "BXP",
      "BSX",
      "BMY",
      "BR",
      "BRO",
      "BF-B",
      "CHRW",
      "CPT",
      "CPB",
      "COF",
      "CAH",
      "KMX",
      "CCL",
      "CARR",
      "CTLT",
      "CAT",
      "CBOE",
      "CBRE",
      "CDW",
      "CE",
      "CNC",
      "CNP",
      "CF",
      "CDAY",
      "CRL",
      "SCHW",
      "CVX",
      "CMG",
      "CB",
      "CHD",
      "CI",
      "CINF",
      "CTAS",
      "C",
      "CFG",
      "CLX",
      "CME",
      "CMS",
      "KO",
      "CL",
      "CMA",
      "CAG",
      "COP",
      "ED",
      "STZ",
      "CEG",
      "COO",
      "GLW",
      "CTVA",
      "CTRA",
      "CCI",
      "CMI",
      "CVS",
      "DHI",
      "DHR",
      "DVA",
      "DE",
      "DAL",
      "DVN",
      "FANG",
      "DLR",
      "DFS",
      "DISH",
      "DIS",
      "DG",
      "D",
      "DPZ",
      "DOV",
      "DOW",
      "DTE",
      "DUK",
      "DD",
      "DXC",
      "EMN",
      "ETN",
      "ECL",
      "EIX",
      "EW",
      "ELV",
      "LLY",
      "EMR",
      "ETR",
      "EOG",
      "EPAM",
      "EFX",
      "EQIX",
      "EQR",
      "ESS",
      "EL",
      "ETSY",
      "ES",
      "EXPE",
      "EXPD",
      "EXR",
      "XOM",
      "FDS",
      "FRT",
      "FDX",
      "FITB",
      #"FRC",
      "FE",
      "FIS",
      "FLT",
      "FMC",
      "F",
      "FTV",
      "FBHS",
      "BEN",
      "FCX",
      "GRMN",
      "GNRC",
      "GD",
      "GE",
      "GIS",
      "GM",
      "GPC",
      "GL",
      "GPN",
      "GS",
      "HAL",
      "HIG", 
      "HAS",
      "HCA",
      "PEAK",
      "HSIC",
      "HSY",
      "HES",
      "HPE",
      "HLT",
      "HOLX",
      "HD",
      "HRL",
      "HST", 
      "HWM",
      "HPQ",
      "HUM",
      "HBAN",
      "HII",
      "IBM",
      "IEX",
      "ITW",
      "IR",
      "ICE",
      "IP",  
      "IPG",
      "IFF",
      "IQV",
      "IRM",
      "JBHT",
      "JKHY",
      "J",
      "JNJ",
      "JCI",
      "JPM",
      "JNPR",
      "K",
      "KEY",
      "KEYS",
      "KMB",
      "KIM",
      "KMI",
      "KLAC",
      "KR",
      "LHX",
      "LH",
      "LW",   
      "LVS",
      "LDOS",
      "LEN",
      "LNC",
      "LIN",
      "LYV",
      "LKQ",
      "LMT",
      "L",
      "LOW",
      "LUMN",   
      "LYB",
      "MTB",
      "MRO",
      "MPC",
      "MKTX",
      "MAR",
      "MMC",
      "MLM",
      "MAS",
      "MA",    
      "MKC",
      "MDT",
      "MRK",
      "MET",
      "MTD",
      "MGM",
      "MAA",
      "MHK",
      "MOH",     
      "TAP",
      "MPWR",
      "MCO",
      "MS",
      "MOS",
      "MSI",
      "MSCI",
      "NWL",
      "NEM",
      "NEE",
      "NLSN",
      "NKE", 
      "NI",
      "NDSN",
      "NSC",
      "NTRS",
      "NOC",
      "NLOK",
      "NCLH",
      "NRG",
      "NUE",
      "NVR",
      "OXY",
      "ODFL",
      "OMC",
      "OKE",
      "ORCL",
      "OGN",
      "OTIS",
      "PKG",
      "PARA",
      "PH",
      "PAYC",
      "PENN",
      "PNR",  
      "PKI",
      "PFE",
      "PM",
      "PSX",
      "PNW",
      "PXD",
      "PNC",
      "POOL",
      "PPG",
      "PPL",
      "PFG",
      "PG",      
      "PGR",
      "PLD",
      "PRU",
      "PEG",
      "PTC",
      "PSA",
      "PHM",
      "PVH",
      "PWR",
      "RL",
      "RJF",    
      "RTX",
      "O",
      "REG",
      "RF",
      "RSG",
      "RMD",
      "RHI",
      "ROK",
      "ROL",
      "ROP",
      "RCL",   
      "SPGI",
      "CRM",
      "SBAC",
      "SLB",
      "STX",
      "SEE",
      "SRE",
      "NOW",
      "SHW",
      "SBNY",
      "SPG", 
      "SJM",
      "SNA",
      "SO",
      "LUV",
      "SWK",
      "STT",
      "STE",
      "SYK",
      "SIVBQ",
      "SYF",
      "SNPS",   
      "SYY",
      "TROW",
      "TPR",
      "TGT",
      "TEL",
      "TDY",
      "TFX",
      "TER",
      "TXT",
      "TMO",
      "TJX",      
      "TSCO",
      "TT",
      "TDG",
      "TRV",
      "TRMB",
      "TFC",
      "TWTR",
      "TYL",
      "TSN",
      "USB",
      "UDR",
      "ULTA",
      "UNP",
      "UAL",
      "UPS",
      "URI",
      "UNH",
      "UHS",
      "VLO",
      "VTR",
      "VZ",
      "VFC",
      "VTRS",      
      "VICI",
      "V",
      "VNO",
      "VMC",
      "WAB",
      "WMT",
      "WBD",
      "WM",
      "WAT",
      "WEC",
      "WFC",
      "WELL",    
      "WST",
      "WDC",
      "WRK",
      "WY",
      "WHR",
      "WMB",
      "WTW",
      "GWW",
      "WYNN",
      "XYL",
      "YUM",
      "ZBH",
      "ZTS"
    ]

NYSE_INTRO={
    "ABBV":"2013-02-01",
    "ALLE":"2013-12-01",
    "AMCR":"2012-06-01",
    "ANET":"2014-07-01",
    "APTV":"2011-12-01",
    "AWK":"2008-05-01",
    "BR":"2007-04-01",
    "CARR":"2020-04-01",
    "CBOE":"2010-07-01",
    "CDW":"2013-07-01",
    "CTLT":"2014-08-01",
    "CFG":"2014-10-01",
    "CDAY":"2018-05-01",
    "CEG":"2022-02-01",
    "CTVA":"2019-06-01",
    "CZR":"2014-10-01",
    "FANG":"2012-11-01",
    "DAL":"2007-06-01",
    "DG":"2009-12-01",
    "DFS":"2007-07-01",
    "DOW":"2019-04-01",
    "ENPH":"2012-04-01",
    "EPAM":"2012-03-01",
    "ETSY":"2015-05-01",
    "FLT":"2011-01-01",
    "FRC":"2011-01-01",
    "FBHS":"2011-10-01",
    "GM":"2010-12-01",
    "GNRC":"2010-03-01",
    "FOX":"2019-06-01",
    "FTV":"2016-08-01",
    "HLT":"2014-01-01",
    "HPE":"2015-11-01",
    "HCA":"2011-04-01",
    "HII":"2011-04-01",
    "HWM":"2016-11-01",
    "IR":"2017-06-01",
    "IQV":"2013-06-01",
    "KEYS":"2014-11-01",
    "KMI":"2011-03-01",
    "LW":"2016-12-01",
    "LYB":"2010-03-01",
    "MPC":"2011-07-01",
    "MSCI":"2007-12-01",
    "NCLH":"2013-02-01",
    "NLSN":"2011-02-01",
    "NFLX":"2002-06-01",
    "NWS":"2013-07-01",
    "OGN":"2021-06-01",
    "OTIS":"2020-04-01",
    "PAYC":"2014-05-01",
    "PM":"2008-04-01",
    "PSX":"2012-05-01",
    "QRVO":"2015-01-01",
    "NOW":"2012-07-01",
    "SEDG":"2015-06-01",
    "SYF":"2014-08-01",
    "TEL":"2007-07-01",
    "ULTA":"2007-11-01",
    "STLA":"2010-07-01",
    "TWTR":"2013-12-01",
    "V":"2008-04-01",
    "VICI":"2018-01-01",
    "WRK":"2015-07-01",
    "XYL":"2011-11-01",
    "ZTS":"2013-02-01",
    }

NYSE_DELIST={
    "CTXS":"2022-10-01",
    "FBHS":"2022-10-15",
    "FISV":"2023-05-01",
    "FRC":"2023-05-01",
    "NLOK":"2023-09-01",
    "NLSN":"2023-10-01",
    "SIVBQ":"2023-03-27",
    "SBNY":"2023-03-24",
    "TWTR":"2022-11-01"
    }

#S&P by sector, no distinction between NYSE and NASDAQ
REALESTATE=["ARE","AMT","AVB","BXP","CPT","CBRE","CCI","DLR","DRE","EQIX","EQR","ESS","EXR","FRT","PEAK",
            "HST","IRM","KIM","MAA","PLD","PSA","O","REG","SBAC","SPG","UDR","VTR","VICI","VNO","WELL",
            "WY"]
INDUSTRY=["MMM","AOS","ALK","ALLE","AAL","AME","BA","CHRW","CARR","CAT","CTAS","CPRT","CSX","CMI","DE",
          "DAL","DOV","ETN","EMR","EFX","EXPD","FAST","FDX","FTV","GNRC","GD","GE","HON","HWM", "FBHS",
          "HII","IEX","ITW","IR","JBHT","J","JCI","LHX","LDOS","LMT","MAS","NLSN","NDSN","NSC","NOC",
          "ODFL","OTIS","PCAR","PH","PNR","PWR","RTX","RSG","RHI","ROK","ROL","SNA","LUV","SWK","TXT",
          "TT","TDG","UNP","UAL","UPS","URI","VRSK","WAB","WM","GWW","XYL"]
IT=["ACN","ADBE","ADP","AKAM","AMD","APH","ADI","ANSS","AAPL","AMAT","ANET","ADSK","AVGO","BR","CDNS",
    "CDW","CDAY","CSCO","CTSH","GLW","DXC","ENPH","EPAM","FFIV","FIS","FLT","FTNT","IT",          "FISV", "CTXS",
    "GPN","HPE","HPQ","IBM","INTC","INTU","JKHY","JNPR","KEYS","KLAC","LRCX","MA","MCHP","MU","MSFT",
    "MPWR","MSI","NTAP","NVDA","NXPI","ON","ORCL","PAYX","PAYC","PYPL","PTC","QRVO","QCOM","ROP", "NLOK",
    "CRM","STX","NOW","SWKS","SEDG","SNPS","TEL","TDY","TER","TXN","TRMB","TYL","VRSN","V","WDC","ZBRA"]
COM=["ATVI","GOOGL","T","CHTR","CMCSA","DISH","DIS","EA","FOX","IPG","LYV","LUMN","MTCH","META","NFLX",
     "NWS","OMC","PARA","TMUS","TTWO","TWTR","VZ","WBD"]
STAPLES=["ADM","MO","BF-B","CPB","CHD","CLX","KO","CL","CAG","STZ","COST","EL","GIS","HSY","HRL","K",
        "KMB","KHC","KR","LW","MKC","TAP","MDLZ","MNST","PEP","PM","SJM","SYY","TSN","WBA","WMT"]
CONSUMER=["AAP","AMZN","APTV","AZO","BBWI","BBY","BKNG","BWA","CZR","KMX","CCL","CMG","DHI","DRI","DG",
          "DLTR","DPZ","EBAY","ETSY","EXPE","F","GRMN","GM","GPC","HAS","HLT","HD","LVS","LEN","LKQ",
          "LOW","MAR","MCD","MGM","MHK","NWL","NKE","NCLH","NVR","ORLY","PENN","POOL","PG","PHM","PVH",
          "RL","ROST","RCL","SBUX","TPR","TGT","TSLA","TJX","TSCO","ULTA","VFC","WHR","WYNN","YUM",
          "ABNB"]
ENERGY=["APA","BKR","CVX","COP","CTRA","DVN","FANG","EOG","XOM","HAL","HES","KMI","MRO","MPC","OXY",
        "OKE","PSX","PXD","SLB","VLO","WMB"]
UTILITIES=["AES","LNT","AEE","AEP","AWK","ATO","CNP","CMS","ED","CEG","D","DTE","DUK","EIX","ETR","EVRG",
           "ES","EXC","FE","NEE","NI","NRG","PNW","PPL","PEG","SRE","SO","WEC","XEL"]
FIN=["AFL","ALL","AXP","AIG","AMP","AON","AJG","AIZ","BAC","WRB","BRK-B","BLK","BK","BRO","COF","CBOE",
    "SCHW","CB","CINF","C","CFG","CME","CMA","DFS","RE","FDS","FITB","BEN","GL","GS","HIG","HBAN",
    "ICE","IVZ","JPM","KEY","LNC","L","MTB","MKTX","MMC","MET","MCO","MS","MSCI","NDAQ","NTRS","PNC",
    "PFG","PGR","PRU","RJF","RF","SPGI","SBNY","STT","SYF","TROW","TRV","TFC","USB","WFC","WTW", "SIVBQ"
    "ZION"]
MATERIALS=["APD","ALB","AMCR","AVY","BALL","CE","CF","CTVA","DOW","DD","EMN","ECL","FMC","FCX","IP",
           "IFF","LIN","LYB","MLM","MOS","NEM","NUE","PKG","PPG","SEE","SHW","VMC","WRK"]
HEALTHCARE=["ABT","ABBV","ABMD","A","ALGN","ABC","AMGN","BAX","BDX","BIO","TECH","BIIB","BSX","BMY","CAH",
   "CTLT","CNC","CRL","CI", "COO", "CVS", "DHR","DVA","XRAY","DXCM","EW","ELV","LLY","GILD","HCA","HSIC",
   "HOLX","HUM","IDXX","ILMN","INCY","ISRG","IQV","JNJ","LH","MCK","MDT","MRK","MTD","MRNA","MOH","OGN",
   "PKI","PFE","DGX","REGN","RMD","STE","SYK","TFX","TMO","UNH","UHS","VRTX","VTRS","WAT","WST","ZBH",
   "ZTS" ]


INTRO={**CAC40_INTRO,**DAX_INTRO,**NASDAQ_INTRO,**NYSE_INTRO}
DELIST={**CAC40_DELIST,**DAX_DELIST,**NASDAQ_DELIST,**NYSE_DELIST} #the issue with delist is that YF cannot retrieve delisted symbol even in for a period when they were listed

INDEXES=["^GSPC", #SP500
         "^FCHI", #cac40 
         "^IXIC", #NASDAQ
         "^GDAXI", #DAX
         "^N225", #Nikkei
         "^FTSE",
         "^DJI"
    ]
RAW=["BZ=F", #brent
     "CL=F",  #crude
     "GC=F", #gold
     ]

mode_to_int={
    "bull":0,
    "bear":1,
    "uncertain":2
    }

short_to_str={True: "short", False: "long"}
short_to_sign={True:-1, False:1}

strategy_to_presel={
    "hist_vol":"PreselHistVolSlow",
    "realmadrid":"PreselRealMadrid",
    "retard":"PreselRetard",
    }


    
    