import psutil

"""
1) psutil.cpu_times() – This function gives system CPU times as a named tuple.
Parameters:  
    user – time spent by normal processes executing in user mode
    system – time spent by processes executing in kernel mode
    idle – time when system was idle
    nice – time spent by priority processes executing in user mode
    iowait – time spent waiting for I/O to complete. This is not accounted in idle time counter.
    irq – time spent for servicing hardware interrupts
    softirq – time spent for servicing software interrupts
    steal – time spent by other operating systems running in a virtualized environment
    guest – time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
"""
print(psutil.cpu_times())

"""
    psutil.cpu_percent(interval) – This function calculates the current system-wide CPU utilization as a percentage.
    It is recommended to provide time interval (seconds) as parameter to the function over which the average 
    CPU usage will be calculated, ignoring the interval parameter could result in high variation in usage values.
"""
print(psutil.cpu_percent(1))
#print(psutil.cpu_percent(2))
#print(psutil.cpu_percent(3))

"""
psutil.cpu_count(logical=True) – This function shows a number of logical CPUs in the system. 
The logical core is calculated as the number of physical cores multiplied by the number of threads that can run on each core.
In the absence of logical core, it only counts a number of physical cores.
"""

print("Number of cores in system", psutil.cpu_count())
print("\nNumber of physical cores in system",psutil.cpu_count(logical=True))

"""
psutil.cpu_stats() – This function gives CPU statistics as a named tuple. The statistics includes : 
ctx_switches – number of context switches since boot.
interrupts – number of interrupts since boot.
soft_interrupts – number of software interrupts since boot.
syscalls – number of system calls since boot. Always set to 0 in Ubuntu.
"""

print("CPU Statistics", psutil.cpu_stats())

"""
5) psutil.cpu_freq() – This function gives CPU frequency as a tuple that includes current, min and max frequencies expressed in Mhz.
  On Ubuntu current frequency reports the real-time value. 
  Whereas on all other platforms it represents the nominal “fixed” value. 
"""

#print(psutil.cpu_freq())


"""
6) psutil.getloadavg() – This function gives the average system load in last 1, 5, and 15 minutes as a tuple. 
The load represents the processes which are in a runnable state, either using the CPU or waiting to use the CPU (e.g. waiting for disk I/O). 
"""

print(psutil.getloadavg())

"""
1) psutil.virtual_memory() – This function gives system memory usage in bytes. The sum of used and available may or may not be equal to total. In order to get details of free physical memory this function is used.

Parameters: 

total – total physical memory excluding swap.
available – the memory that can be given instantly to processes without the system going into swap.
used – memory used.
free – memory not used at and is readily available
active – memory currently in use or very recently used.
inactive – memory that is marked as not used.
buffers – cache data like file system metadata.
cached – cached data
shared – memory that may be accessed by multiple processes.
"""

print(psutil.virtual_memory())

"""
2) psutil.swap_memory() – This function provides details of swap memory statistics as a tuple.
Parameters:  
total – total swap memory in bytes
used – used swap memory in bytes
free – free swap memory in bytes
percent – the percentage usage that is calculated as (total – available) / total * 100
sin – the number of bytes the system has swapped in from disk
sout – the number of bytes the system has swapped out from disk
"""

print(psutil.swap_memory())

"""
1) psutil.disk_partitions() – This function provides the details of all mounted disk partitions as a list of tuples 
    including device, mount point and filesystem type.
"""

print(psutil.disk_partitions())

"""
2) psutil.disk_usage(path)- This function gives disk usage statistics as a tuple for a given path. 
Total, used and free space are expressed in bytes, along with the percentage usage.
"""

print(psutil.disk_usage('/'))

"""
1) psutil.net_io_counters()- This function gives the details of network Input output statistics as a tuple.
Parameters:  
    bytes_sent – number of bytes sent
    bytes_recv – number of bytes received
    packets_sent – number of packets sent
    packets_recv – number of packets received
    errin – total number of errors while receiving
    errout – total number of errors while sending
    dropin – total number of incoming packets which were dropped
    dropout – total number of outgoing packets which were dropped
"""
print(psutil.net_io_counters())

"""
psutil.net_if_addrs() – This function is used to get the addresses of each network interface card installed on the system. 
It is a dictionary whose keys are the Network Interface Card names and value is a list of named tuples for each address assigned to it.
Each tuple includes:  
    family – the socket family, either AF_INET or AF_INET6
    address – the primary NIC address
    netmask – the netmask address
    broadcast – the broadcast address.
    ptp – “point to point” it is the destination address on a point to point interface.
"""
print(psutil.net_if_addrs())

"""
psutil.sensors_battery() – This function gives battery status information as a named tuple.
Parameters:  
    percent – battery power left as a percentage.
    secsleft – an approximate time in seconds before battery is completely discharged.
    power_plugged – True if the AC power cable is connected, False if it is not connected.
"""
print(psutil.sensors_battery())

"""
psutil.boot_time() – This function returns the system boot time which is expressed in seconds since the epoch. 
"""
print(psutil.boot_time())

"""
psutil.users() – This function gives the list of users who are connected on the system as a named tuples. 
Parameters: 
    user – It is the system name of the user.
    terminal – the tty of the user.
    host – the host name of the user.
    started – the creation time as a floating point number expressed in seconds since the epoch.
    pid – the PID of the login process.
"""
print(psutil.users())
