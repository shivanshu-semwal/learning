#include <stdio.h> /* standard input and output */
#include <sys/types.h> /* gives types used in system development Primitive System Data Types */
#include <sys/wait.h> /* wait */
#include <unistd.h>   /* unix standard library, for posix compliance */

int main(int argc, char const *argv[]) {
  /* pid_t is form types.h, a types used for PROCESS_ID, internally is int */
  pid_t pid;

  /* fork is inside unistd.h */
  pid = fork();
  if (pid < 0) {
    /* error */
    fprintf(stderr, "Fork failed!"); /* stderr is inside stdio.h */
    return 1;
  } else if (pid == 0) {
    /* child process */
    /* execlp call exec syscall, is inside unistd */
    /* "ls" the first argument to the program, it's same as it's name, usually
     * some program work differently based on this name */
    execlp("/bin/ls", "ls", "-all", NULL);
  } else {
    /* parent process */
    /* wait for child process to finish, this is inside wait.h */
    wait(NULL);
    printf("Child Complete");
  }
  return 0;
}
