# `fork`

- syscall
- create a duplicate of parent process to create a child process
- uses COW - copy on write mechanism so as to prevent waste of resources
    - COW means that when some data is changed only then a new copy is created for the child process for that data


## COW - Copy on write

- Initial Forking:
    - When a process calls `fork()`, instead of creating an immediate duplicate of the process's address space (which can be very memory-intensive), the operating system sets up both the parent and the child process to share the same physical memory pages.
    - Both processes' page tables (which map virtual memory to physical memory) point to the same physical memory pages.
- Marking Pages as Read-Only:
    - The shared pages are marked as read-only. This is a critical part of the mechanism because it ensures that any attempt to modify these pages triggers a page fault.
- Page Fault Handling:
    - If either the parent or the child process attempts to write to a shared page, a page fault occurs because the page is marked as read-only.
    - The operating system then handles this page fault by creating a private copy of the page for the process attempting the write operation. This private copy is writable, while the original page remains shared and read-only for the other process.
- Updating Page Tables:
    - The page table of the process that caused the page fault is updated to point to the new private copy of the page. The other process’s page table still points to the original shared page.