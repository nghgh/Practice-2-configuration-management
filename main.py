import argparse
import os

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

print("\n" + "=" * 50)
print("СТАРТ ЭТАПА 2: СБОР ДАННЫХ О ЗАВИСИМОСТЯХ")
print("=" * 50)


def get_dependencies_from_test_file(package_name, package_version):
    """Получение зависимостей из тестового файла"""
    test_file = "test_apkindex.txt"

    if not os.path.exists(test_file):
        print(f"Тестовый файл {test_file} не найден")
        return None

    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()

        packages = content.split('\n\n')

        for pkg in packages:
            if f"P:{package_name}" in pkg and f"V:{package_version}" in pkg:
                for line in pkg.split('\n'):
                    if line.startswith('D:'):
                        dependencies = line[2:].strip().split()
                        return dependencies
        return None

    except Exception as e:
        print(f"Ошибка чтения тестового файла: {e}")
        return None


print(f"Поиск зависимостей для пакета: {args.packet_name} версии {args.packet_version}")

if args.repo_work_mode == "test":
    dependencies = get_dependencies_from_test_file(args.packet_name, args.packet_version)

    if dependencies is None:
        print(f"Пакет {args.packet_name} версии {args.packet_version} не найден в тестовом репозитории")
        exit(1)

    print("\nПРЯМЫЕ ЗАВИСИМОСТИ:")
    for dep in dependencies:
        print(f"  - {dep}")

    print(f"\nВсего прямых зависимостей: {len(dependencies)}")

else:
    print("Режим работы с реальным репозиторием будет реализован в следующих этапах")
    print("Сейчас используется тестовый режим")

print("\nЭТАП 2 ЗАВЕРШЕН УСПЕШНО")