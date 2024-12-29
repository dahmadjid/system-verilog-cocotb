import sys
from cocotb.runner import get_runner, get_results
from pathlib import Path
import os 
import tabulate
os.environ.setdefault("COCOTB_ANSI_OUTPUT", "1")

proj_path = Path(__file__).resolve().parent
src = proj_path / "src"

runner = get_runner("icarus") # or "verilator"

sources = [
]

files_to_exclude = [
]


for file in list(src.rglob("*.sv")):
    if not file in sources and not file in files_to_exclude:
        sources.append(file)

print(sources)

test_benches = list(src.rglob("*_tb.py"))
if len(sys.argv) > 1:
    filtered_tbs = []
    for tb in test_benches:
        if sys.argv[1] in str(tb):
            filtered_tbs.append(tb)
    test_benches = filtered_tbs
results = []

#Color
R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset

for tb in test_benches:
    path = str(tb.relative_to(proj_path)).split("_tb.py")[0].split("/")
    runner.build(
        hdl_toplevel=path[-1], 
        sources=sources,
        always=True,
        hdl_library="work",
        build_dir="build",
    )

    res_path = runner.test(
        hdl_toplevel=path[-1], 
        test_module=".".join(path) + "_tb",
        hdl_toplevel_library="work",
        build_dir="build",
        test_dir="build",
    )
    res = get_results(res_path)
    results.append(('.'.join(path) + "_tb", G + "PASS" + N if res[1] == 0 else R + "FAIL" + N , *res))
    
print()
print(tabulate.tabulate(results, headers=["Testbench", "","Total", "Failed"], tablefmt='orgtbl'))