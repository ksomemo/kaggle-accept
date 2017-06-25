import argparse
from kaggle_accept.acception import accept


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--competion-name", require=True)
    
    args = parser.parse_args()
    accept(args.competion_name)

if __name__ == "__main__":
    _main()
