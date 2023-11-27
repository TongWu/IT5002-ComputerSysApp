# Intro of OS
## Context Switching
## Kernels
### Monolithic Kernels

### Microkernels
## User Mode

## Kernel Mode

# Process Management
- **程序（program）** 是一组指令，它被写入计算机系统的存储器中，以便在需要时执行。程序是一种静态的实体，它包含了处理任务所需的所有指令和数据，但它本身并没有具体的执行状态。
- **进程（process）** 是执行中的程序的实例。当一个程序被加载到计算机的内存并开始执行时，它成为一个进程。进程是动态的，它有自己的执行状态和运行的上下文。每个进程都有自己的内存空间、程序计数器（记录下一个将被执行的指令的地址）和一组寄存器等。进程可以独立地执行，并与其他进程并行运行。每个进程都有独立的资源分配和管理。
## Interrupts

## Switching between processes

## Process Control Blocks
当一个进程被创建时，操作系统会为其创建一个称为“进程控制块”（Process Control Block，简称PCB）的数据结构，用以维护该进程的相关信息。以下是PCB包含的关键信息：
1. **进程标识符（Process ID，PID）**：
    - 每个进程有一个唯一的标识符，用于区分系统中的不同进程。
2. **栈指针（Stack Pointer）**：
    - 指向进程的栈顶，栈用于存储函数参数、返回地址以及局部变量。
3. **打开文件（Open Files）**：
    - 进程打开的文件列表，通常包括文件描述符和相关的文件状态信息。
4. **挂起信号（Pending Signals）**：
    - 待处理的信号集，信号是进程间通信的一种方式。
5. **CPU使用情况（CPU usage）**：
    - 该进程使用CPU的统计信息，如累计CPU时间。
PCB存储在一个称为“进程表”（Process Table）的结构中，系统中的每个进程都有一个对应的PCB。
当进程终止时：
- 操作系统通常会释放大多数资源，如关闭打开的文件等，并将这些资源返回给系统。
- 然而，PCB会保留在内存中，这允许子进程将结果返回给父进程。
- 父进程通过调用“wait”函数来检索子进程的结果。在这之后，子进程的PCB被释放。
如果父进程从未调用“wait”：
- 子进程的PCB会保留在内存中，这样的子进程被称为“僵尸进程”（Zombie Process）。
- 如果僵尸进程过多，进程表可能会耗尽空间，导致无法创建新的进程。
# Process Scheduling
## Type of Multitaskers
> **批处理** (Batch Processing)：任务逐一执行，直至完成。在一个任务完成之前不会启动另一个任务
> **协作多任务处理**（Co-operative Multitasking）：在这种环境中，当前正在运行的进程不会被操作系统的调度器强制挂起。进程必须自愿放弃CPU时间，使得其他进程有机会运行。
> **抢占式多任务处理**（Pre-emptive Multitasking）：在这种模式下，操作系统的调度器可以强制挂起当前运行的进程，以便其他进程可以使用CPU。这样可以确保所有进程都能获得执行的机会。
> **实时多任务处理**（Real-Time Multitasking）：这种模式要求进程必须在固定的截止时间前完成。如果进程未能在截止时间前完成：
> 	- **硬实时系统**（Hard Real-Time Systems）：系统死机
> 	- **软实时系统**（Soft Real-Time Systems）：通常只是造成不便，系统性能会降低
### Scheduling policies for Multitaskers
- **For all types of multitaskers**: 
	- **固定优先级**（Fixed Priority): 根据设置的优先级顺序来运行任务。
- **批处理** (Batch Processing):
	- **先来先服务**（First-come First-served，FCFS）：按照任务到达的顺序来运行任务。
	- **最短作业优先**（Shortest Job First，SJF）：优先执行预计运行时间最短的任务
- **协作多任务处理**（Co-operative Multitasking):
	- **循环轮询与自愿调度**（Round Robin with Voluntary Scheduling，VC）：任务轮流获得CPU时间，但每个任务在使用CPU时必须自愿放弃CPU时间，从而允许下一个任务运行
- **抢占式多任务处理**（Pre-emptive Multitasking）:
	- **带时间切片的循环轮询** (Round Robin with Timer, RR): 为每个进程分配时间切片，在时间切片结束时调度器将其挂起，并将CPU分配给下一个进程
	- **最短剩余时间** (Shortest Remaining Time, SRT): CPU被分配给(预估)剩余时间最短的进程，这是对SJF的改进
- **实时多任务处理**（Real-Time Multitasking）:
	- **Earliest Deadline First Scheduling (EDF)**：它给即将达到截止时间的任务分配最高优先级。EDF允许任务的周期变化，不需要固定周期，只要任务能在它们的截止时间之前完成。这是一种动态调度策略，任务的优先级在运行时根据截止时间进行调整。
	- **Rate Monotonic Scheduling (RMS)**：它分配优先级基于任务的请求率（即周期的倒数）。周期性任务中，周期短的任务（意味着请求率高的）被赋予更高的优先级。RMS适用于硬实时系统，其中任务的周期是固定的，并且在每个周期内任务必须完成
# Inter-Process Communication