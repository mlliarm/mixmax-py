#/usr/bin/python3
import subprocess

def run_shit(N):
    "To produce some interesting examples"
    for i in [10000000000000, 20000000000000, 30000000000000, 40000000000000, 50000000000000, 60000000000000, 70000000000000, 80000000000000, 90000000000000, 99999999999999]:
        subprocess.call(['python3', 'create_matrix_new.py', '{}'.format(N), str(i), str(1)])


if __name__ == "__main__":
    run_shit(512)
