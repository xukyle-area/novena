> [Java线程池实现原理及其在美团业务中的实践](https://tech.meituan.com/2020/04/02/java-pooling-pratice-in-meituan.html)

# 1. **Chapter 2, Write in front**

 ## **– Why We Need Thread Pools**

You know, when we write multithreaded programs in Java, it’s tempting to just create a new thread every time we have a task to run.

But the problem is — creating and destroying threads is not free. It takes time and system resources, like memory allocation, context switching, and scheduling overhead.

If we have too many threads running, the system actually spends a lot of time just managing them — deciding which one to run next — instead of doing real work. That can **hurt overall performance**.That’s why we use a **thread pool**.

A thread pool keeps a number of worker threads alive and ready to take on tasks.So instead of creating a brand-new thread each time, the pool reuses existing ones.This saves the cost of creating and destroying threads, and also helps us avoid “overscheduling” — where too many threads compete for CPU time and slow everything down.

In Java, this is mainly done through the **`ThreadPoolExecutor`** class in the JDK. It’s the core implementation that lets us create and manage thread pools in a flexible way.

Now, using thread pools gives us several important benefits:

1. **Lower resource consumption.** Since we reuse threads instead of constantly creating and destroying them, we save CPU and memory resources.
2. **Better responsiveness.** When a new task comes in, there’s already a thread available to handle it right away — no need to wait for thread creation.
3. **Better control and stability.** Threads are limited resources. If we create them without control, we might run out of memory or make the CPU spend too much time switching between threads. A thread pool allows us to set limits, tune performance, and monitor usage more easily.
4. **More flexibility and features.** Java’s thread pool system is extensible. For example, `ScheduledThreadPoolExecutor` lets you schedule tasks to run periodically or after a delay.

1. ##  **What Problem Does the Thread Pool Solve?**

The main problem thread pools solve is **resource management**. In a concurrent system, we often don’t know how many tasks will arrive or how much system resource they’ll require. This uncertainty can cause several issues:

1. **Too much overhead.** Constantly creating and destroying threads adds extra cost — sometimes a huge one.
2. **No limits on resource usage.** If we keep creating threads freely, we might run out of CPU or memory, which can crash the system.
3. **Uncontrolled scheduling.** When threads are created without proper management, it becomes difficult to allocate system resources efficiently, leading to instability.

To solve these problems, thread pools use a common idea called **“pooling.”** Pooling simply means **putting resources together and managing them in a unified way** — so we can maximize efficiency and minimize risk. It’s not just a computer science concept — you can find it in finance, manufacturing, and even HR management.

For example, in finance, people might pool their money together to share risk. In computing, we do the same thing — we pool resources like threads, memory, or database connections. Here are some typical examples besides thread pools:

- **Memory Pooling:** Pre-allocate chunks of memory to speed up allocation and reduce fragmentation.
- **Connection Pooling:** Keep a set of open database connections to reuse, so each query doesn’t have to create a new one.
- **Object Pooling:** Reuse objects instead of creating and destroying them repeatedly, which saves initialization cost.

So overall, the main idea is to **share and reuse limited resources** efficiently. After understanding what pooling is and why it’s useful, we can move on to see **how the thread pool works internally**— that’s where the real design comes in.

1. ## Questions

### Q1: Can you explain what a thread pool is and why do we need it?

In Java, creating a new thread is actually quite expensive — it involves allocating memory, scheduling, and system calls. If we create and destroy threads for every single task, it’ll waste a lot of system resources and affect performance. That’s why we use a **thread pool**. It basically keeps a set of pre-created threads that can be reused for different tasks. Instead of starting a brand new thread every time, we just pick an idle one from the pool and give it a new job.

This way, we save the cost of creating threads repeatedly and can also control **how many threads** are running at the same time — which helps prevent resource exhaustion. In Java, the core implementation is the `ThreadPoolExecutor` class, which is part of the `java.util.concurrent` package. It gives us a flexible way to manage concurrent tasks — we can control how many threads to keep alive, how to handle new tasks, and what to do when the queue is full. Typically, we use it through helper classes like `Executors.newFixedThreadPool()`, `Executors.newCachedThreadPool()`, or `Executors.newSingleThreadExecutor()`. But in real production systems, we usually recommend **directly using** `ThreadPoolExecutor` instead of the helper methods, because those factory methods can hide important parameters and sometimes cause issues like unbounded queues or memory risks.

So overall, a thread pool helps us:

1. **Reuse threads** to reduce creation overhead.
2. **Control concurrency** and prevent too many threads from running.
3. **Manage lifecycle** of threads in a unified way.

It’s one of the most important concurrency tools in Java — almost every backend system relies on it for task execution and resource management.

# **Chapter 1, Core design**

In the last part, we talked about how a thread pool helps manage threads using the idea of “pooling.” In Java, this is done through the **ThreadPoolExecutor** class. Now in this chapter, we’ll take a closer look at how it’s actually designed and implemented.

1. ## General design

The main class that implements thread pools in Java is **ThreadPoolExecutor**. In this chapter, we’ll look at its core design and implementation based on the JDK 1.8 source code. First, let’s check out the **UML class diagram** of ThreadPoolExecutor to understand its inheritance structure.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=OTRjMTIxMGU5MDc4YWIwNmQ5MmExMWUwOWRhNzdlMDNfU09sZXF2UExiY1ZkZHVGaGNVem5xQjJmYmdRTWJQUTRfVG9rZW46SjBEcGJ5NlY3bzU1UGx4M2JTb2M2RFhYbjRmXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 1 ThreadPoolExecutor UML class diagram

The top-level interface that **ThreadPoolExecutor** implements is **Executor**. This interface introduces the idea of separating **task submission** from **task execution**. As a user, you don’t need to worry about creating or scheduling threads — you just provide a **Runnable** task, submit it to the executor, and it takes care of running it in the background.

Then we have **ExecutorService**, which extends Executor and adds a few more useful features:

1. It can handle one or multiple asynchronous tasks and return a **future,** so you can track their results.
2. It also provides methods to **control the thread pool**, like shutting it down.

Next, **AbstractExecutorService** is an abstract class that connects the overall process of task execution. It helps simplify the implementation, so subclasses only need to focus on how tasks are actually run.

Finally, the **ThreadPoolExecutor** class does the real work. It manages both the **lifecycle of the pool** and the **execution of tasks**. It coordinates threads and tasks, so they work together efficiently to handle parallel workloads.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=MTlhYjZiMGVmNTE5OTVmYTk0ZTE0NWJiNjg0MWRiYTVfbFZyOFBMZXlZOVh2UDZoaVJmS09YZHlEMEl6OTRIQlVfVG9rZW46VmZDYmJianFib01CRTF4ajIzUWNRMGYwbkdoXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 2 ThreadPoolExecutor running process

So, how does **ThreadPoolExecutor** actually work — how does it manage threads and run tasks at the same time? Here’s the basic idea (as shown in Figure 2):

The thread pool follows a **producer–consumer model**. It separates threads and tasks so they can work independently but efficiently together. Tasks are buffered in a queue, and threads are reused to handle them.

The thread pool mainly does two things:

1. **Task management** – when a task comes in, it decides whether to
   1. run it immediately using a thread,
   2. put it in the queue to wait, or
   3. reject it if the pool is full.
2. **Thread management** – threads are kept inside the pool. They continuously fetch and execute tasks, and when no more work is available, idle threads may eventually be recycled.

Next, we’ll dive deeper into these three key parts of how the thread pool works:

1. How it maintains its internal state.
2. How it manages tasks.
3. How it manages threads.

1. ## Lifecycle management

The running state of a thread pool isn’t something the user sets directly — it’s managed internally as the pool runs.

Inside **ThreadPoolExecutor**, two key values are tracked together:

- the **run state** of the pool (like Running, Shutdown, etc.)
- the **number of active worker threads**

Instead of using two separate variables, the pool combines both into one using an `AtomicInteger` called **`ctl`**:

```Java
private final AtomicInteger ctl = new AtomicInteger(ctlOf(RUNNING, 0));
```

Here, `ctl` stores both pieces of information:

- The **top 3 bits** represent the pool’s run state.
- The **lower 29 bits** represent the number of active worker threads.

Because both values are packed into one variable, the pool can check and update them **atomically** — without locking — which keeps them consistent and improves performance.

This design is important because the thread pool often needs to check **both the state and the thread count** at the same time. Using one atomic variable avoids race conditions and speeds up decision-making.

The pool also provides helper methods to extract these two values using **bitwise operations**, which are much faster than normal arithmetic or synchronization.

```Java
//计算当前运行状态
private static int runStateOf(int c) { 
    return c & ~CAPACITY; 
} 

//计算当前线程数量
private static int workerCountOf(int c)  {
    return c & CAPACITY; 
}  

//通过状态和线程数生成ctl
private static int ctlOf(int rs, int wc) { 
    return rs | wc; 
}   
```

There are five running states of ThreadPoolExecutor, namely:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=YmUxZmQ4NzA5YjE1NjgxN2E3YmY3ODRhZmUxN2UzYzFfbm1HUm9nNGJoaEFUWVdIVmtCY2xXOUh1MzFMUXI5bzJfVG9rZW46UkcybGJVR2pIb2FiaGh4M3FZcWNrekZpbnFmXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Its lifecycle transformation is shown below:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=MTY4Y2E4MWE3ZTgzNmQzOTJhYWZkZmI5YmEzNzUwMzFfVnNDYUF3YmpyQ1JUWkRBaHdhMmpQZXdkN3djdjJEbXFfVG9rZW46Wml5VGJoN3FIb3pnckl4MFpoZWNSQlN4bnM0XzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 3 Thread pool life cycle

1. ## Task execution mechanism

1. ### **Task scheduling**

Task scheduling is basically the entry point to how a thread pool actually works. When you submit a task, this stage decides **how** the task will be executed next — and once you understand it, you’ve basically understood how the thread pool runs under the hood.

All task scheduling in `ThreadPoolExecutor` goes through the **`execute()`** method. This method checks the current state of the pool, how many threads are already running, and what the pool’s configuration or policy is — then decides one of three things:

- Run the task immediately in a new thread,
- Put it into the waiting queue,
- Or reject it.

Here’s the general logic step by step:

1. **Check the pool’s running state.** If it’s not `RUNNING`, the task is rejected right away — only a running pool can accept new tasks.
2. **If the number of threads is below the core size (****`workerCount < corePoolSize`****)**, a new thread is created to run the submitted task immediately.
3. **If the core threads are full but the queue isn’t**, the task is added to the queue to wait for execution.
4. **If both the core threads and queue are full, but the pool can still grow (****`workerCount < maximumPoolSize`****)**, another thread is created to handle the task.
5. **If the pool has reached its maximum size and the queue is also full**, the task is rejected. By default, this throws an exception (`RejectedExecutionException`).

In short:

→ Try to run immediately → then try to queue → then try to expand → else reject.

The overall process looks like this in the diagram below:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=OGVjZmViNmQ2MTJmYWM1NjBhMTViMmVjMzA5NDc0YzRfTlllMTlaUEZFVnNmQW9PeThxZzBqMHlPeWxSdlY5ZXVfVG9rZW46RlR5d2JaRTJvbzdrZU54Tzc4dWM2bklxbklmXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 4 Task scheduling process

1. ### **Task buffering**

The task buffer part is really the heart of how a thread pool manages tasks. The main idea of a thread pool is to separate tasks from threads, so they’re not directly tied together—this makes scheduling and allocation easier.

The thread pool uses a **producer-consumer model** with a **blocking queue**. The queue holds tasks, and worker threads pick tasks from them.

A **BlockingQueue** is just a queue with two extra features:

1. If a thread tries to take an element when the queue is empty, it waits until something is added.
2. If a thread tries to add an element when the queue is full, it waits until there’s space.

This works perfectly for producers and consumers: producers put tasks into the queue, and consumers (threads) take tasks out. The queue is basically the bridge between them.

The diagram below shows thread 1 adding tasks to the queue and thread 2 taking tasks out:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=MzE4N2QyYmFhOWM0ZjMxNDFmYTcyYzhjMTA1OWIxMWZfWEtBWHoxeWphem9iczZPTDJmQW9HdklnUHdpdGpiUjBfVG9rZW46VENzZ2JRam5ob1M5VmV4c3pLUWNrbHpJbkliXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 5 Blocking queue

Different types of queues can implement different task scheduling policies. Next, let’s look at the key members of the blocking queue.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=MzgwNmY5MjgyOWYxYTU1YzczNWMzYTNkZTViN2U4OTZfQmJmdlF0WjhWUm9Dc3ZLYjlGNmo1OGJYOVFIU2d2OUJfVG9rZW46VTBJNWJJSTh2b2E1bUl4cm9GSGNoQmZjbjJmXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

1. ### **Task application**

From the task assignment we saw earlier, there are basically two ways a task gets executed:

1. A newly created thread runs the task directly.
2. An idle thread grabs a task from the task queue, runs it, then goes back to the queue for the next task.

The first happens only when a thread is just created. Most of the time, threads work the second way.

Threads keep pulling tasks from the queue, which connects the thread management part with the task management part. This is done by the `getTask()` method, and its process looks like this:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTg0ZjhkOTU3YjlhODQzMDQyYzA0ZWFmMjRkNzRhMzRfeVJ1bGhudVYydU81UlVmQjhERk5TM2FVT1cyOVlFZkpfVG9rZW46Qjh3T2J6SzY1b1NZcWF4eFYzc2NzQlBNbnZlXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 6 Obtaining the task flow chart

The `getTask()` method is called repeatedly to control how many threads are active and to keep the thread pool in the right state. If the pool doesn’t need more threads at the moment, it returns `null`.

Workers keep pulling new tasks from the queue, and when there are no tasks to get, they start shutting themselves down and getting recycled.

1. ###  **Task rejection**

When the task cache queue of the thread pool is full and the number of threads in the thread pool reaches maximumPoolSize, it is necessary to reject the task and adopt a task rejection policy to protect the thread pool.

The deny policy is an interface that is designed as follows:

```Java
public interface RejectedExecutionHandler {
    void rejectedExecution(Runnable r, ThreadPoolExecutor executor);
}
```

Users can customize the deny policy by implementing this interface, or they can choose from the four existing deny policies provided by the JDK, which have the following characteristics:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=OGQyOGE4YTYwYmU0NDgwZDFhYTNlYjkyMGNjOGNmY2NfcXZibkR1bmloNkFVdWpkVXJOVVRsNEwxU2pxRFA3Tm5fVG9rZW46RjB0VWJuNHlnb1Z5T0F4dXNRSGN3RDM4bkpkXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

1. ## Worker thread management

1. ### Worker threads

In order to grasp the state of threads and maintain the life cycle of threads, the thread pool designs worker workers in the thread pool. Let's take a look at some of its code:

```Java
try {
  while (task != null || (task = getTask()) != null) {
    //执行任务
  }
} finally {
  processWorkerExit(w, completedAbruptly);//获取不到任务时，主动回收自己
}
```

A `Worker` is basically a thread wrapper that implements `Runnable` and holds a thread plus an initial task, `firstTask`.

- `thread` is created by the `ThreadFactory` when the `Worker` is constructed and is responsible for running tasks.
- `firstTask` is the very first task the worker will execute. It can be `null`.
  - If it’s not null, the worker executes it right away—this usually happens when a core thread is created.
  - If it’s null, the worker will pick up tasks from the `workQueue`—this is typical for non-core threads.

So essentially, a `Worker` can either start with a specific task or start idle and pull tasks from the queue.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2FkZTc5YjJkMDA1ZDJjYzM0Y2FiZjkxZjM5MTQ4MmFfakxBY2NtUk0wc0VpVWtzUnBORjI4QzRRZTJvSHlvcFhfVG9rZW46S1BCUWJON0Zobzlqc0F4UEdXRGNGdHVpbklkXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 7 Worker performing a task

The thread pool also needs to manage thread lifecycles, making sure idle threads get recycled after a while. To do this, it keeps references to threads in a hash table—adding a reference keeps a thread alive, removing it lets the JVM recycle it.

The tricky part is knowing whether a thread is running a task. Here’s how it works:

- Each worker inherits from AQS and uses it like a lock. This isn’t a normal ReentrantLock; it’s a simple exclusive lock to track whether the thread is busy.
- If the thread has the lock, it’s running a task.
- If the thread doesn’t have the lock, it’s idle and can be safely interrupted.
- When `shutdown()` or `tryTerminate()` is called, the pool uses `interruptIdleWorkers()` to interrupt idle threads. This method checks each thread with `tryLock()`—if the thread is idle, it can be recycled.

In short, the pool uses a lock to know if a thread is busy and only interrupts threads that are safe to stop.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=OTA4N2FkNzQ1YTdjN2Q5MTE0YWI0MjY5NWRhM2Y1Y2NfWjNqa240dzZFbENNcFQ5c1BONVJuS3FtTnE5eFhjcG9fVG9rZW46TkNWTmJzdXVvbzVGanB4UlRqTmNteXR0bnFkXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 8 Thread pool recycling process

1. ### **Worker threads are increased**

Adding threads is handled by the `addWorker` method in the thread pool. Its job is simple: create a new thread, start it, and return whether it was successful. It doesn’t decide **when** to add a thread—that’s handled earlier during task scheduling.

`addWorker` has two parameters:

1. **firstTask** – the first task the new thread will run (can be null).
2. **core** – if `true`, the thread count is checked against `corePoolSize`; if `false`, it’s checked against `maximumPoolSize`.

Basically, this method just spins up a thread and hands it a task.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=MWI5MTNiZmZlZmQ2NWI1MjRjOTBkMzhhYzA2Mzc1MjBfRDVzOE5uVkR2cEp2OVdnVVl2SjNYMkp0TGpkamI2M3VfVG9rZW46VzNTbWJrMVp5b1hEOE94UHdwWGNTY1dmbkZlXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 9 Application thread execution flow chart

1. ### **Worker thread recycling**

Thread destruction in a thread pool relies on the JVM’s automatic garbage collection. The pool itself just keeps enough thread references alive so the JVM doesn’t recycle them too early.

After a worker is created, it keeps polling for tasks:

- **Core threads** can wait forever for new tasks.
- **Non-core threads** only wait for a limited time.

If a worker fails to get a task (the queue is empty), the loop ends, and the worker removes its own reference from the pool, effectively letting itself be destroyed.

```Java
try {
  while (task != null || (task = getTask()) != null) {
    //执行任务
  }
} finally {
  processWorkerExit(w, completedAbruptly);//获取不到任务时，主动回收自己
}
```

The work of thread recycling is done in the processWorkerExit method.

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=NTc4ZGFkYzVmOTg0YTljMDYyZmQ2MjY3MmQ3NTA1ZTBfcjhNeWVYM1poMTlXengzTTEwOEd3T3E1NTU1Vno3SUJfVG9rZW46TEYwdGJzMHhDb2RaZzR4VUpNN2N5VnR2bjBkXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 10 Thread destruction process

Actually, when a thread reference is removed from the pool, the thread is basically ready to be destroyed. But there are many reasons a thread might end, so the thread pool also needs to figure out:

1. **What caused the thread to stop** – was it idle, timed out, or the pool is shutting down?
2. **Whether the pool’s state needs to be updated** because of this thread ending.
3. **Whether new threads need to be started** to keep the pool running at the right size.

In short, thread destruction isn’t just killing the thread—it’s also about adjusting the pool’s overall state and resources.

1. ### **Worker thread executes tasks**

In the `Worker` class, the **`run()`** method calls **`runWorker()`** to actually execute tasks. Here’s how `runWorker()` works in simple terms:

1. A **while loop** keeps running, fetching tasks one by one using **`getTask()`**.
2. **`getTask()`** pulls a task from the blocking queue.
3. If the thread pool is **stopped**, it makes sure the thread is **interrupted**; otherwise, it ensures the thread is **not interrupted**.
4. The task is executed.
5. If **`getTask()`** returns `null` (no more tasks), the loop ends and **`processWorkerExit()`** is called to clean up and destroy the thread.

So basically, each worker thread keeps fetching tasks, runs them, and shuts down only when there are no tasks left or the pool is stopping.

The flow can be visualized like this:

![img](https://ccnlu0q3xtkj.feishu.cn/space/api/box/stream/download/asynccode/?code=YzA2MTM4YmVkMmE2NDFhYjc2MWM4NDQzNWZkM2M1OTVfNzY1VUk1UXp5ZEx3TDZpcXZrSXY5NDV5dEh3dHh0SkNfVG9rZW46U3ZlM2I5SmNGb21Gamh4akVRVGM3THg1bktiXzE3NjQ4Njk4ODQ6MTc2NDg3MzQ4NF9WNA)

Figure 11 Execution task process

##  Questions

### **Q1: Can you explain the core idea of Java's ThreadPoolExecutor?**

**Answer:** Yeah, basically, ThreadPoolExecutor is a way to manage threads efficiently. Instead of creating a new thread every time a task comes in, it keeps a pool of threads ready to run tasks. If no threads are free, tasks go into a queue. This saves resources, prevents too many threads from running at once, and makes concurrency easier to control.

### **Q2: How does ThreadPoolExecutor manage its internal state?**

**Answer:** It uses one atomic variable called `ctl` to track two things: the pool’s run state, like RUNNING or SHUTDOWN, and the number of active threads. The top bits are for state, the lower bits for thread count. Packing them together lets the pool check both at once safely, without locks, which is fast and avoids inconsistencies.

### **Q3: How does task scheduling work in ThreadPoolExecutor?**

**Answer:** When you submit a task using `execute()`, the pool decides what to do:

1. If the number of threads is less than `corePoolSize`, it starts a new thread to run the task.
2. If core threads are full but the queue has space, it puts the task in the queue.
3. If the queue is full but the total threads are below `maximumPoolSize`, it starts a new thread.
4. If the queue is full and max threads are reached, the task is rejected.

So it’s basically: try to run immediately → then queue → then expand → else reject.

### **Q4: What is the role of the** **`Worker`** **class?**

**Answer:** Each `Worker` wraps a thread and maybe a first task. It handles executing tasks from the queue. Core threads may start with a task or just wait indefinitely for new tasks. Non-core threads wait for a limited time, and if nothing comes, they shut down. Workers also use a lock to track if they’re busy, which helps safely interrupt idle threads.

### **Q5: How does the pool handle task rejection?**

**Answer:** If the queue is full and the pool has reached `maximumPoolSize`, the task can’t be accepted. Java provides a `RejectedExecutionHandler` interface—you can implement it to define what happens. By default, it might throw an exception, discard the task, or discard the oldest task in the queue.

### **Q6: How are threads recycled in the pool?**

**Answer:** Threads are kept alive by references in the pool. Core threads wait forever for new tasks, non-core threads wait only for a limited time. If a thread doesn’t get a task in time, it removes itself from the pool and eventually gets garbage-collected. The pool also checks why the thread ended and may start a new one to keep the pool at the right size.

### **Q7: Why use a single AtomicInteger to track both run state and worker count?**

**Answer:** Because the pool often needs to know both at the same time. Using one atomic variable ensures both are updated together safely and quickly, without needing locks.