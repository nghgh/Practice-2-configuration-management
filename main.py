import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--packet_name', type=str)
parser.add_argument('-u', '--url_link_repo', type=str)
parser.add_argument('-m', '--repo_work_mode', type=str)
parser.add_argument('-v', '--packet_version', type=str)
parser.add_argument('-o', '--output_file', type=str)
parser.add_argument('-d', '--max_depth', type=int)
parser.add_argument('-f', '--packet_filter', type=str)

args = parser.parse_args()

print("Arguments: \n")
print(f"packet_name = {args.packet_name}")
print(f"url_link_repo = {args.url_link_repo}")
print(f"repo_work_mode = {args.repo_work_mode}")
print(f"packet_version = {args.packet_version}")
print(f"output_file = {args.output_file}")
print(f"max_depth = {args.max_depth}")
print(f"packet_filter = {args.packet_filter}")

if args.packet_name == None:
    print("no packet name")
    exit()

if args.url_link_repo == None:
    print("no repo link")
    exit()

if args.repo_work_mode == None:
    print("no repo work mode")
    exit()

if args.packet_version == None:
    print("no packet version")
    exit()

if args.output_file == None:
    print("no output file")
    exit()

if args.max_depth == None:
    print("no max depth")
    exit()

if args.packet_filter == None:
    print("no packet filter")
    exit()

# Проверка значений
if args.max_depth <= 0:
    print("max depth must be positive")
    exit()

print("all parameters are valid")