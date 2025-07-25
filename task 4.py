import pkg_resources

packages = pkg_resources.working_set
installed = sorted([f"{pkg.project_name}=={pkg.version}" for pkg in packages])

print("Installed Packages:")
for package in installed:
    print(package)
