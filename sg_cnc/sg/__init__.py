import os
import sg_cnc

VCP_DIR = os.path.realpath(os.path.dirname(__file__))
VCP_CONFIG_FILE = os.path.join(VCP_DIR, 'config.yml')


def main(opts=None):
    sg_cnc.main('sg', opts)


if __name__ == '__main__':
    main()
