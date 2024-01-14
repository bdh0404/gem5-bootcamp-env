from gem5.resources.resource import obtain_resource
from gem5.resources.resource import BinaryResource

resource = obtain_resource("riscv-disk-img")

BinaryResource(local_path="tests/test-progs/hello/bin/x86/linux/hello")

print(f"The resource is available at {resource.get_local_path()}")
