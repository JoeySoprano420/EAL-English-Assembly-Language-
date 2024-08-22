import subprocess

def package_and_publish():
    subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"])
    subprocess.run(["twine", "upload", "dist/*"])

if __name__ == "__main__":
    package_and_publish()
