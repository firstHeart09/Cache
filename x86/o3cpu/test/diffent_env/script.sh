#!/bin/bash
rm -rf different_cacheline.txt
echo "icache_1kB"
# get gem5 mess 
/home/dushuai/study/Cache/x86/gem5.opt --debug-flags=Exec,Cache,CacheRepl,TLB,PageTableWalker,MMU --debug-file=trace.txt ./system.py --binary=./test --l1i_size=1kB
# use python to deal with gem5 mess
python ./gem5Mess.py --binary=./m5out/trace.txt --outputfile_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/ --name=icache_1kB --cacheline_miss_hit_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env
# visual every func
python ./visual_singlefunc_zhexian.py --path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/func_miss_hit_total.txt --name=icache_1kB
# delete usefulless file
rm -rf out/ __pycache__/ m5out/

echo "icache_2kB"
# get gem5 mess 
/home/dushuai/study/Cache/x86/gem5.opt --debug-flags=Exec,Cache,CacheRepl,TLB,PageTableWalker,MMU --debug-file=trace.txt ./system.py --binary=./test --l1i_size=2kB
# use python to deal with gem5 mess
python ./gem5Mess.py --binary=./m5out/trace.txt --outputfile_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/ --name=icache_2kB --cacheline_miss_hit_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env
# visual every func
python ./visual_singlefunc_zhexian.py --path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/func_miss_hit_total.txt --name=icache_2kB
# delete usefulless file
rm -rf out/ __pycache__/ m5out/

echo "icache_4kB"
# get gem5 mess 
/home/dushuai/study/Cache/x86/gem5.opt --debug-flags=Exec,Cache,CacheRepl,TLB,PageTableWalker,MMU --debug-file=trace.txt ./system.py --binary=./test --l1i_size=4kB
# use python to deal with gem5 mess
python ./gem5Mess.py --binary=./m5out/trace.txt --outputfile_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/ --name=icache_4kB --cacheline_miss_hit_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env
# visual every func
python ./visual_singlefunc_zhexian.py --path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/func_miss_hit_total.txt --name=icache_4kB
# delete usefulless file
rm -rf out/ __pycache__/ m5out/

echo "icache_8kB"
# get gem5 mess 
/home/dushuai/study/Cache/x86/gem5.opt --debug-flags=Exec,Cache,CacheRepl,TLB,PageTableWalker,MMU --debug-file=trace.txt ./system.py --binary=./test --l1i_size=8kB
# use python to deal with gem5 mess
python ./gem5Mess.py --binary=./m5out/trace.txt --outputfile_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/ --name=icache_8kB --cacheline_miss_hit_path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env
# visual every func
python ./visual_singlefunc_zhexian.py --path=/home/dushuai/study/Cache/x86/o3cpu/test/diffent_env/out/func_miss_hit_total.txt --name=icache_8kB
# delete usefulless file
rm -rf out/ __pycache__/ m5out/

# cache's miss and hit mess
python visual_single_zhuzhuang.py
