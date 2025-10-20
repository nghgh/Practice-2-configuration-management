import subprocess
import sys

def get_package_info(package_name="matplotlib"):
    try:
        pip_command = [sys.executable, "-m", "pip", "show", package_name]
        result = subprocess.run(pip_command, capture_output=True, text=True, check=True)
        return result.stdout

    except FileNotFoundError:
        return "Ошибка: Команда 'pip' не найдена. Убедитесь, что Python установлен и добавлен в PATH."

    except subprocess.CalledProcessError as e:
        return f"Ошибка при выполнении команды pip show:\n{e.stderr}"


if __name__ == "__main__":
    package_name = "matplotlib"
    info = get_package_info(package_name)
    print(info)