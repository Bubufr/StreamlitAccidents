def AppliquerFiltres(_df,
_stDep = None
,_stAtm = None
,_stLum = None
,_stAgg = None
,_stCatr = None
,_stCol = None ):
    if _stDep != None:
        _df = _df.loc[(_df['dep'] == _stDep)]
    if _stAtm != None:
        _df = _df.loc[(_df['atm'] == _stAtm)]
    if _stLum != None:
        _df = _df.loc[(_df['lum'] == _stLum)]
    if _stAgg != None:
        _df = _df.loc[(_df['agg'] == _stAgg)]
    if _stCatr != None:
        _df = _df.loc[(_df['catr'] == _stCatr)]
    if _stCol != None:
        _df = _df.loc[(_df['col'] == _stCol)]
    return _df




