from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Date, Numeric, ForeignKey
import datetime

engine = create_engine('sqlite:///clean_stations.db')

meta = MetaData()

stations = Table(
    'stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude', Numeric),
    Column('longitude', Numeric),
    Column('elevation', Numeric),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String, ForeignKey('stations.station')),
    Column('date', Date),
    Column('precip', Numeric),
    Column('tobs', Integer)
)

if __name__ == "__main__":
    meta.create_all(engine)

    conn = engine.connect()
    ins_stat = stations.insert()
    conn.execute(ins_stat, [
        {'station': 'USC00519397', 'latitude': 21.2716, 'longitude': -157.8168,
            'elevation': 3.0, 'name': 'WAIKIKI 717.2', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00513117', 'latitude': 21.4234, 'longitude': -157.8015,
            'elevation': 14.6, 'name': 'KANEOHE 838.1', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00514830', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7.0,
            'name': 'KUALOA RANCH HEADQUARTERS 886.9', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00517948', 'latitude': 21.3934, 'longitude': -157.9751,
            'elevation': 11.9, 'name': 'PEARL CITY', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00518838', 'latitude': 21.4992, 'longitude': -158.0111,
            'elevation': 306.6, 'name': 'UPPER WAHIAWA 874.3', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00519523', 'latitude': 21.33556, 'longitude': -157.71139,
            'elevation': 19.5, 'name': 'WAIMANALO EXPERIMENTAL FARM', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00519281', 'latitude': 21.45167, 'longitude': -157.84888999999998,
            'elevation': 32.9, 'name': 'WAIHEE 837.5', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00511918', 'latitude': 21.3152, 'longitude': -157.9992, 'elevation': 0.9,
            'name': 'HONOLULU OBSERVATORY 702.2', 'country': 'US', 'state': 'HI'},
        {'station': 'USC00516128', 'latitude': 21.3331, 'longitude': -157.8025,
            'elevation': 152.4, 'name': 'MANOA LYON ARBO 785.2', 'country': 'US', 'state': 'HI'}
    ])

    ins_clean_meas = clean_measure.insert()
    conn.execute(ins_clean_meas, [
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 1), 'precip': 0.08, 'tobs': 65},
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 2), 'precip': 0.0, 'tobs': 63},
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 3), 'precip': 0.0, 'tobs': 74},
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 4), 'precip': 0.0, 'tobs': 76},
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 6), 'precip': 0.0, 'tobs': 73},
        {'station': 'USC00519397', 'date': datetime.datetime(
            2010, 1, 7), 'precip': 0.06, 'tobs': 70},
        {'station': 'USC00519523', 'date': datetime.datetime(
            2016, 3, 28), 'precip': 0.0, 'tobs': 73},
        {'station': 'USC00519523', 'date': datetime.datetime(
            2016, 3, 29), 'precip': 0.04, 'tobs': 75},
        {'station': 'USC00519281', 'date': datetime.datetime(
            2012, 9, 25), 'precip': 0.05, 'tobs': 74},
        {'station': 'USC00519281', 'date': datetime.datetime(
            2012, 9, 26), 'precip': 0.02, 'tobs': 74}
    ])

    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    print(result)
