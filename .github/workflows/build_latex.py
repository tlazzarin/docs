import glob
import subprocess
import os

repo_dir = os.environ['GITHUB_WORKSPACE']
subprocess.run(["ls", "-lh", repo_dir])
print("-----")
subprocess.run(["ls", "-lh", repo_dir+"/.."])
exit(1)

sources = glob.glob("{}/**/*.tex".format(repo_dir), recursive=True)

# Do not build template
sources_to_compile = []
for source in sources:
    if "template" not in source:
        sources_to_compile.append(source)
        print(source)

build_dir = "{}/build/".format(repo_dir)

if not os.path.exists(build_dir):
    os.makedirs("{}candidatura/documenti_interni/verbali".format(build_dir))
    os.makedirs("{}candidatura/documenti_esterni/verbali".format(build_dir))
    os.makedirs("{}candidatura/documenti_esterni/presentazione_candidatura".format(build_dir))

for source in sources_to_compile:
    res = subprocess.run(["pdflatex", "-output-directory", build_dir+os.path.dirname(source), "-halt-on-error", source])
    if res.returncode != 0:
        exit(1)
