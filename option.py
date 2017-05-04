import argparse
import datetime

def get_date_str(offset):
    if(offset is None):
        offset = 0
    date_str = (datetime.datetime.today()+datetime.timedelta(days=offset)).strftime("%Y-%m-%d")
    return date_str

_default = dict(
    reload_data='Y',
    gen_portfolio='N',
    output_type='json',
    charset='utf-8',
    test_data_range=60
)