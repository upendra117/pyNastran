import os

from pyNastran.converters.tecplot.tecplot import read_tecplot
from pyNastran.utils.log import get_logger2

def main():
    dirnames = ['ascii', 'binary']
    log = get_logger2(debug=False)
    for dirname in dirnames:
        fnames = [os.path.join(dirname, fname) for fname in os.listdir(dirname)
                  if not fname.endswith('.png')]
        for fname in fnames:
            try:
                read_tecplot(fname, log=log)
                log.info('read %r' % fname)
            except Exception as e:
                log.warning('failed reading %r' % fname)
                log.error(e)
                print('')

if __name__ == '__main__':  # pragma: no cover
    main()

