#!/bin/bash
rm -rf different_cacheline.txt
# get gem5 mess 
/home/dushuai/study/Cache/x86/gem5.opt --debug-flags=Exec,Cache,CacheRepl,TLB,PageTableWalker,MMU --debug-file=trace.txt ./system.py --binary=./test --l1i_size=1kB
# use python to deal with gem5 mess
python ./gem5Mess.py --binary=./m5out/trace.txt --outputfile_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_sort/out/ --name=icache_1kB --cacheline_miss_hit_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_sort
# visual every func
python ../diffent_env/visual_singlefunc_zhexian.py --path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_sort/out/func_miss_hit_total.txt --name=icache_1kB
# delete usefulless file
rm -rf out/ __pycache__/ m5out/
