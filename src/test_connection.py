import fastf1

fastf1.Cache.enable_cache('data/raw')

session = fastf1.get_session(2026, 1, 'R')

session.load()

print(session.laps[['Driver', 'LapNumber', 'LapTime', 'Compound', 'TyreLife', 'Stint']].head(20))