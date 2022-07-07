import sys
from _typeshed import Self
from collections.abc import Callable, Iterable, Iterator
from contextlib import AbstractContextManager
from typing import Any
from typing_extensions import TypeAlias

from ._common import (
    AIX as AIX,
    BSD as BSD,
    CONN_CLOSE as CONN_CLOSE,
    CONN_CLOSE_WAIT as CONN_CLOSE_WAIT,
    CONN_CLOSING as CONN_CLOSING,
    CONN_ESTABLISHED as CONN_ESTABLISHED,
    CONN_FIN_WAIT1 as CONN_FIN_WAIT1,
    CONN_FIN_WAIT2 as CONN_FIN_WAIT2,
    CONN_LAST_ACK as CONN_LAST_ACK,
    CONN_LISTEN as CONN_LISTEN,
    CONN_NONE as CONN_NONE,
    CONN_SYN_RECV as CONN_SYN_RECV,
    CONN_SYN_SENT as CONN_SYN_SENT,
    CONN_TIME_WAIT as CONN_TIME_WAIT,
    FREEBSD as FREEBSD,
    LINUX as LINUX,
    MACOS as MACOS,
    NETBSD as NETBSD,
    NIC_DUPLEX_FULL as NIC_DUPLEX_FULL,
    NIC_DUPLEX_HALF as NIC_DUPLEX_HALF,
    NIC_DUPLEX_UNKNOWN as NIC_DUPLEX_UNKNOWN,
    OPENBSD as OPENBSD,
    OSX as OSX,
    POSIX as POSIX,
    POWER_TIME_UNKNOWN as POWER_TIME_UNKNOWN,
    POWER_TIME_UNLIMITED as POWER_TIME_UNLIMITED,
    STATUS_DEAD as STATUS_DEAD,
    STATUS_DISK_SLEEP as STATUS_DISK_SLEEP,
    STATUS_IDLE as STATUS_IDLE,
    STATUS_LOCKED as STATUS_LOCKED,
    STATUS_PARKED as STATUS_PARKED,
    STATUS_RUNNING as STATUS_RUNNING,
    STATUS_SLEEPING as STATUS_SLEEPING,
    STATUS_STOPPED as STATUS_STOPPED,
    STATUS_TRACING_STOP as STATUS_TRACING_STOP,
    STATUS_WAITING as STATUS_WAITING,
    STATUS_WAKING as STATUS_WAKING,
    STATUS_ZOMBIE as STATUS_ZOMBIE,
    SUNOS as SUNOS,
    WINDOWS as WINDOWS,
    AccessDenied as AccessDenied,
    Error as Error,
    NoSuchProcess as NoSuchProcess,
    TimeoutExpired as TimeoutExpired,
    ZombieProcess as ZombieProcess,
    _Status,
    pconn,
    pcputimes,
    pctxsw,
    pgids,
    pionice,
    popenfile,
    pthread,
    puids,
    sbattery,
    sconn,
    scpufreq,
    scpustats,
    sdiskio,
    sdiskpart,
    sdiskusage,
    sfan,
    shwtemp,
    snetio,
    snicaddr,
    snicstats,
    sswap,
    suser,
)

if sys.platform == "linux":
    from ._pslinux import (
        IOPRIO_CLASS_BE as IOPRIO_CLASS_BE,
        IOPRIO_CLASS_IDLE as IOPRIO_CLASS_IDLE,
        IOPRIO_CLASS_NONE as IOPRIO_CLASS_NONE,
        IOPRIO_CLASS_RT as IOPRIO_CLASS_RT,
    )
if sys.platform == "win32":
    from ._psutil_windows import (
        ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
        BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
        HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
        IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
        NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
        REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
    )
    from ._pswindows import (
        CONN_DELETE_TCB as CONN_DELETE_TCB,
        IOPRIO_HIGH as IOPRIO_HIGH,
        IOPRIO_LOW as IOPRIO_LOW,
        IOPRIO_NORMAL as IOPRIO_NORMAL,
        IOPRIO_VERYLOW as IOPRIO_VERYLOW,
        win_service_get as win_service_get,
        win_service_iter as win_service_iter,
    )

if sys.platform == "linux":
    from ._pslinux import pfullmem, pmem
elif sys.platform == "darwin":
    from ._psosx import pfullmem, pmem
elif sys.platform == "win32":
    from ._pswindows import pfullmem, pmem
else:
    pmem: TypeAlias = Any  # noqa: Y042
    pfullmem: TypeAlias = Any  # noqa: Y042

if sys.platform == "linux":
    PROCFS_PATH: str
AF_LINK: int
version_info: tuple[int, int, int]
__version__: str
__author__: str

class Process:
    def __init__(self, pid: int | None = ...) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def pid(self) -> int: ...
    def oneshot(self) -> AbstractContextManager[None]: ...
    def as_dict(
        self, attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = ..., ad_value: Any | None = ...
    ) -> dict[str, Any]: ...
    def parent(self) -> Process: ...
    def parents(self) -> list[Process]: ...
    def is_running(self) -> bool: ...
    def ppid(self) -> int: ...
    def name(self) -> str: ...
    def exe(self) -> str: ...
    def cmdline(self) -> list[str]: ...
    def status(self) -> _Status: ...
    def username(self) -> str: ...
    def create_time(self) -> float: ...
    def cwd(self) -> str: ...
    def nice(self, value: int | None = ...) -> int: ...
    if sys.platform != "win32":
        def uids(self) -> puids: ...
        def gids(self) -> pgids: ...
        def terminal(self) -> str: ...
        def num_fds(self) -> int: ...
    if sys.platform != "darwin":
        def io_counters(self): ...
        def ionice(self, ioclass: int | None = ..., value: int | None = ...) -> pionice: ...
    if sys.platform == "linux":
        def rlimit(self, resource: int, limits: tuple[int, int] | None = ...) -> tuple[int, int]: ...
    if sys.platform != "darwin":
        def cpu_affinity(self, cpus: list[int] | None = ...) -> list[int] | None: ...
    if sys.platform == "linux":
        def cpu_num(self) -> int: ...

    def environ(self) -> dict[str, str]: ...
    if sys.platform == "win32":
        def num_handles(self) -> int: ...

    def num_ctx_switches(self) -> pctxsw: ...
    def num_threads(self) -> int: ...
    def threads(self) -> list[pthread]: ...
    def children(self, recursive: bool = ...) -> list[Process]: ...
    def cpu_percent(self, interval: float | None = ...) -> float: ...
    def cpu_times(self) -> pcputimes: ...
    def memory_info(self) -> pmem: ...
    def memory_info_ex(self) -> pmem: ...
    def memory_full_info(self) -> pfullmem: ...
    def memory_percent(self, memtype: str = ...) -> float: ...
    if sys.platform != "darwin":
        def memory_maps(self, grouped: bool = ...): ...

    def open_files(self) -> list[popenfile]: ...
    def connections(self, kind: str = ...) -> list[pconn]: ...
    def send_signal(self, sig: int) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def wait(self, timeout: int | None = ...) -> int: ...

class Popen(Process):
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, *args, **kwargs) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...

def pids() -> list[int]: ...
def pid_exists(pid: int) -> bool: ...
def process_iter(
    attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = ..., ad_value: Any | None = ...
) -> Iterator[Process]: ...
def wait_procs(
    procs: Iterable[Process], timeout: float | None = ..., callback: Callable[[Process], object] | None = ...
) -> tuple[list[Process], list[Process]]: ...
def cpu_count(logical: bool = ...) -> int: ...
def cpu_times(percpu: bool = ...): ...
def cpu_percent(interval: float | None = ..., percpu: bool = ...) -> float: ...
def cpu_times_percent(interval: float | None = ..., percpu: bool = ...): ...
def cpu_stats() -> scpustats: ...
def cpu_freq(percpu: bool = ...) -> scpufreq: ...
def getloadavg() -> tuple[float, float, float]: ...
def virtual_memory(): ...
def swap_memory() -> sswap: ...
def disk_usage(path: str) -> sdiskusage: ...
def disk_partitions(all: bool = ...) -> list[sdiskpart]: ...
def disk_io_counters(perdisk: bool = ..., nowrap: bool = ...) -> sdiskio: ...
def net_io_counters(pernic: bool = ..., nowrap: bool = ...) -> snetio: ...
def net_connections(kind: str = ...) -> list[sconn]: ...
def net_if_addrs() -> dict[str, list[snicaddr]]: ...
def net_if_stats() -> dict[str, snicstats]: ...

if sys.platform == "linux":
    def sensors_temperatures(fahrenheit: bool = ...) -> dict[str, list[shwtemp]]: ...
    def sensors_fans() -> dict[str, list[sfan]]: ...

if sys.platform != "win32":
    def sensors_battery() -> sbattery | None: ...

def boot_time() -> float: ...
def users() -> list[suser]: ...

if sys.platform == "linux":
    RLIMIT_AS: int
    RLIMIT_CORE: int
    RLIMIT_CPU: int
    RLIMIT_DATA: int
    RLIMIT_FSIZE: int
    RLIMIT_LOCKS: int
    RLIMIT_MEMLOCK: int
    RLIMIT_MSGQUEUE: int
    RLIMIT_NICE: int
    RLIMIT_NOFILE: int
    RLIMIT_NPROC: int
    RLIMIT_RSS: int
    RLIMIT_RTPRIO: int
    RLIMIT_SIGPENDING: int
    RLIMIT_STACK: int
    RLIM_INFINITY: int
