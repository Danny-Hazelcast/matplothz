import matplotlib
matplotlib.use('Agg')

import sys
import BenchDrivers as bds


if len(sys.argv) == 1:
    sys.exit('Error path to csv files needed')

benchDrivers_list = []

dirs = sys.argv
dirs.pop(0)

for base_dir in dirs:
    benchDrivers_list.append(bds.BenchDrivers(base_dir))


while bds.BenchDrivers.has_any_bench(benchDrivers_list):

    out_dir = ''
    title = ''

    for benchDriver in benchDrivers_list:
        if benchDriver.next_benchmark():
            benchDriver.drop(5)
            benchDriver.plot_data()
        title += benchDriver.get_bench_name()+" Vs "
        out_dir += benchDriver.get_cluster_id()+"-vs-"

    title = title[:-4]
    out_dir = out_dir[:-4]

    if len(benchDrivers_list) > 1:
        bds.BenchDrivers.plot_comparison(title, out_dir, benchDrivers_list)
