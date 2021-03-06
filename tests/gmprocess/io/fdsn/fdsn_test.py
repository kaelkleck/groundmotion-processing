#!/usr/bin/env python

import os.path
from gmprocess.io.fdsn.core import read_fdsn
from gmprocess.io.test_utils import read_data_dir
from gmprocess.streamcollection import StreamCollection
from gmprocess.processing import process_streams


def test():
    datafiles, origin = read_data_dir('fdsn', 'nc72282711', 'BK.CMB*.mseed')
    streams = []
    for datafile in datafiles:
        streams += read_fdsn(datafile)

    assert streams[0].get_id() == 'BK.CMB.HN'

    datafiles, origin = read_data_dir('fdsn', 'nc72282711', 'TA.M04C*.mseed')
    streams = []
    for datafile in datafiles:
        streams += read_fdsn(datafile)

    assert streams[0].get_id() == 'TA.M04C.HN'

    # DEBUGGING
    sc = StreamCollection(streams)
    psc = process_streams(sc, origin)


if __name__ == '__main__':
    os.environ['CALLED_FROM_PYTEST'] = 'True'
    test()
